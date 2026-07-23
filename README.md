# Cloud Data Redundancy Removal System

A FastAPI-based web application that improves cloud database accuracy by detecting redundant data before it is stored. The system validates every submitted record, prevents duplicate entries, identifies possible false positives, and only stores records after user verification.

---

## Features

- Detects duplicate records using unique identifiers.
- Validates every new record against existing database entries.
- Prevents duplicate records from being added to the database.
- Identifies possible false positives for manual verification.
- Requires user confirmation before saving a validated record.
- Delete existing records from the database.
- Responsive navy-and-white web interface.

---

## How It Works

When a user submits a new record, the system compares it against all existing records.

### Duplicate Detection

A record is classified as a **Duplicate** if:

- The email already exists, or
- The phone number already exists.

Duplicate records are rejected and are not stored in the database.

### Possible Duplicate (False Positive)

A record is classified as a **Possible Duplicate** when it closely resembles an existing record (for example, a very similar name). Since this may represent two different individuals, the system asks the user to verify the information before continuing.

### Verification

If the submitted record is unique, the system displays a confirmation dialog allowing the user to verify the entered information before it is permanently stored in the database.

Only verified, unique records are added to the database.

---

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Jinja2 Templates
- HTML
- CSS
- JavaScript

---

## Project Structure

```
CodeAlpha_DataRedundancyRemoval/
│
├── app.py
├── database.py
├── models.py
├── validator.py
├── requirements.txt
├── README.md
├── static/
│   └── style.css
└── templates/
    ├── dashboard.html
    └── add_record.html
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/alia-77/CodeAlpha_DataRedundancyRemoval.git
cd CodeAlpha_DataRedundancyRemoval
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

---

## Assignment Requirements Covered

✔ Design a system that identifies and classifies redundant and possible false-positive data.

✔ Validate new records against existing database records.

✔ Prevent duplicate data from being inserted into the cloud database.

✔ Store only unique and user-verified records.

✔ Improve database accuracy by avoiding redundant information.

---

## Future Improvements

- Persistent validation history and audit logs.
- Bulk CSV import with automatic validation.
- Role-based authentication.
- Cloud deployment on Azure, AWS, or Render.
- Machine learning–based duplicate detection.
