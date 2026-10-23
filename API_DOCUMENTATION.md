# TrustVault – API Documentation

## 1. Project Overview
TrustVault is a secure document management system developed using Python and Django. It allows users to upload, download, delete, and share documents with authorized users.

## 2. Technologies Used
- Python
- Django
- HTML
- SQLite Database

## 3. Application URLs

| Method | URL | Description |
|---|---|---|
| GET | `/accounts/login/` | Displays the login page |
| GET, POST | `/documents/upload/` | Displays documents and uploads a document |
| POST | `/documents/share/<document_id>/` | Shares a document with another user |
| GET | `/documents/download/<document_id>/` | Downloads an authorized document |
| POST | `/documents/delete/<document_id>/` | Deletes a document owned by the logged-in user |
| GET | `/admin/` | Opens the Django administration page |

## 4. Authentication
Users must log in before accessing document-management features. Django authentication is used to identify users.

## 5. Authorization and Security
- Document owners can view, download, and delete their own documents.
- Authorized users can view and download documents shared with them.
- Unauthorized users cannot download documents they do not own or have permission to access.
- Only document owners can share or delete their documents.
- CSRF protection is used for POST forms.

## 6. Database
The Document model stores:
- Title
- Uploaded file
- Upload date and time
- Document owner
- Users authorized to access the document

## 7. Testing
The application should be tested using two separate user accounts to verify uploading, downloading, sharing, deleting, and access restrictions.

## 8. Future Enhancements
- Password reset
- Document previews
- Improved audit logs
- Cloud deployment and storage
