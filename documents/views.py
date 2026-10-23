

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Document

User = get_user_model()


@login_required
def upload_document(request):
    message = ""

    if request.method == "POST":
        uploaded_file = request.FILES.get("file")

        if uploaded_file:
            Document.objects.create(
                title=uploaded_file.name,
                file=uploaded_file,
                owner=request.user,
            )
            message = "Document uploaded successfully!"
        else:
            message = "Please choose a file first."

    documents = Document.objects.filter(
        owner=request.user
    ).order_by("-uploaded_at")

    shared_documents = Document.objects.filter(
        shared_with=request.user
    ).order_by("-uploaded_at")

    return render(
        request,
        "documents/upload.html",
        {
            "message": message,
            "documents": documents,
            "shared_documents": shared_documents,
        },
    )


@login_required
def share_document(request, document_id):
    if request.method != "POST":
        return redirect("upload_document")

    document = get_object_or_404(
        Document,
        id=document_id,
        owner=request.user,
    )

    username = request.POST.get("username", "").strip()

    try:
        user_to_share = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect("upload_document")

    if user_to_share == request.user:
        messages.error(request, "You already own this document.")
    else:
        document.shared_with.add(user_to_share)
        messages.success(request, "Document shared successfully.")

    return redirect("upload_document")


@login_required
def download_document(request, document_id):
    document = get_object_or_404(
        Document,
        id=document_id,
    )

    if (
        document.owner_id != request.user.id
        and not document.shared_with.filter(id=request.user.id).exists()
    ):
        raise Http404("Document not found")

    if not document.file:
        raise Http404("Document file not found")

    try:
        return FileResponse(
            document.file.open("rb"),
            as_attachment=True,
            filename=document.title,
        )
    except (ValueError, OSError):
        raise Http404("Document file not found")


@login_required
def delete_document(request, document_id):
    if request.method != "POST":
        return redirect("upload_document")

    document = get_object_or_404(
        Document,
        id=document_id,
        owner=request.user,
    )

    document.file.delete(save=False)
    document.delete()

    return redirect("upload_document")
