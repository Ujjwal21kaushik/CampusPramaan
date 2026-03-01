# Attendance System

A Django-based attendance system with multiple authentication methods (face, location, network) and role-based dashboards for students and teachers.

## Features
- User accounts and role-based dashboards (`accounts`)
- Attendance recording and management (`attendance`)
- Face authentication (`face_auth`)
- Location-based authentication (`location_auth`)
- Network-based authentication (`network_auth`)

## Requirements
- Python 3.8+
- See `requirements.txt` for Python package dependencies

## Setup
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
# or .\.venv\Scripts\activate   # cmd
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. (Optional) Create a superuser:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

## Project layout (top-level)
- `accounts/` — user models, views, dashboards
- `attendance/` — attendance models and marking UI
- `face_auth/` — face registration and verification
- `location_auth/` — location-based checks
- `network_auth/` — network/session-based checks
- `templates/` — base templates and auth pages

## Usage
- Open `http://127.0.0.1:8000/` after running the server and log in as a teacher or student.
- Teachers can mark attendance via the attendance UI; students can view their dashboard.

## Contributing
- Open issues or submit pull requests. Create a feature branch, add tests, and open a PR.

## License
No license specified. Add a `LICENSE` file if you want to set a project license.

---
If you want, I can commit this file, create a basic `LICENSE`, or add usage examples for the auth flows.
