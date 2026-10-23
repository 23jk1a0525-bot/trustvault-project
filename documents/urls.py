

    

from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_document, name="upload_document"),
    path("delete/<int:document_id>/", views.delete_document, name="delete_document"),
    path("download/<int:document_id>/", views.download_document, name="download_document"),
    path("share/<int:document_id>/", views.share_document, name="share_document"),
]
    



