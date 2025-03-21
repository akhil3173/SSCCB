# Secure Cloud Storage System

A secure cloud storage system built with Django that provides encrypted file storage, sharing capabilities, and robust user management.

## Features

- Secure file upload and storage with encryption
- User registration and authentication
- File sharing with access control
- Download tracking (self and other users)
- File metadata management
- Private/Public key encryption system
- Email notifications

## Prerequisites

- Python 3.7+
- MySQL Server
- pip package manager

## Installation

1. Clone the repository or download the source code

2. Create and activate a virtual environment:
```bash
python -m venv ssccbenv
ssccbenv\Scripts\activate  # On Windows
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Database Configuration

1. Create a MySQL database named 'server_security'

2. Update database settings in `ssccb/settings.py` if needed:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'server_security',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '3306'
    }
}
```

3. Run database migrations:
```bash
python manage.py migrate
```

## Email Configuration

Configure email settings in `ssccb/emailsettings.py` for notifications:

```python
SET_EMAIL_USE_TLS = True
SET_EMAIL_HOST = 'your-smtp-server'
SET_EMAIL_HOST_USER = 'your-email@domain.com'
SET_EMAIL_HOST_PASSWORD = 'your-password'
SET_EMAIL_PORT = 587
```

## Running the Application

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the application at `http://127.0.0.1:8000`

## Project Structure

- `adminapp/` - Admin module for system management
- `userapp/` - User module for file operations
- `assets/` - Static files and templates
- `media/` - Uploaded files and encryption keys

## Security Features

- RSA encryption for file security
- Secure key management
- Session management
- Access control and user permissions
- Encrypted file storage

## File Management

- Supports various file types
- Automatic file size tracking
- Download count monitoring
- Secure file sharing mechanism
- Private key-based access control

## Database Management

- User data management
- File metadata storage
- Encryption key management
- Access log maintenance
- Backup and recovery operations

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
