
# TrustVault - Security Threat Model

## 1. Project Overview

TrustVault is a Django-based document management system. It supports document uploading, downloading, deleting, user login, and administrator management.

## 2. Assets to Protect

- Uploaded documents and their contents
- User accounts and passwords
- Document ownership and sharing permissions
- Administrator access
- Application configuration and database

## 3. Potential Threats

| Threat | Impact | Mitigation |
|---|---|---|
| Unauthorized access | Private documents may be exposed | Require authentication and verify document permissions |
| Insecure file upload | Malicious or unwanted files may be uploaded | Validate file type and size; reject unsafe uploads |
| Path traversal | An attacker may try to access files outside the document folder | Validate filenames and restrict file access to the intended directory |
| Cross-site request forgery (CSRF) | Unauthorized actions may be submitted through a user's session | Enable Django CSRF protection for forms |
| Weak passwords | User accounts may be compromised | Enforce strong passwords and use Django password validation |
| Broken access control | Users may download or delete another user's files | Check document ownership and sharing permissions on every request |
| Administrator compromise | Attackers may gain control of users and documents | Protect administrator credentials and restrict admin access |
| Information leakage | Sensitive information may be exposed through error pages | Disable DEBUG mode in production and configure safe error handling |

## 4. Security Controls

- Use Django's built-in authentication system.
- Apply login requirements to protected views.
- Validate permissions before downloading or deleting documents.
- Validate uploaded file names, types, and sizes.
- Keep CSRF protection enabled.
- Use Django's password hashing and password validation.
- Keep secrets out of source control.
- Run automated security tests before submission.

## 5. Testing Plan

- Verify that anonymous users cannot access protected pages.
- Verify that authenticated users can access permitted pages.
- Verify that invalid or missing files cannot be downloaded.
- Verify that users cannot access documents belonging to others.
- Verify that unauthorized delete requests are rejected.

## 6. Limitations

These threats and mitigations describe the planned security controls. A control must be implemented and tested before it can be considered verified. Passing automated tests does not guarantee complete security.

## 7. Future Improvements

- Implement and test document ownership and sharing.
- Add file type and file size restrictions.
- Add audit logs for document operations.
- Configure HTTPS and production security settings.
- Perform additional security testing before deployment.
