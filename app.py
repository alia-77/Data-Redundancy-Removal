from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database import Base, engine, SessionLocal
from models import Record
from validator import classify_record


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(lifespan=lifespan)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):

    db = SessionLocal()
    records = db.query(Record).all()
    total = len(records)
    db.close()

    return templates.TemplateResponse(

        request=request,

        name="dashboard.html",

        context={

            "records": records,
            "total": total,
            "unique": total,
            "duplicates": 0,
            "possible": 0

        }

    )


@app.get("/add", response_class=HTMLResponse)
def add_page(request: Request):

    return templates.TemplateResponse(

        request=request,
        name="add_record.html",

        context={

            "message": None,

            "status": None,

            "record": None

        }

    )


@app.post("/add", response_class=HTMLResponse)
def add_record(

    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    address: str = Form(...)

):

    db = SessionLocal()

    existing = db.query(Record).all()

    new_record = {

        "name": name,
        "email": email,
        "phone": phone,
        "address": address

    }

    classification, reason = classify_record(

        new_record,

        existing

    )

    if classification == "Duplicate":

        db.close()

        return templates.TemplateResponse(

            request=request,
            name="add_record.html",

            context={

                "status": "duplicate",

                "message": reason,

                "record": new_record

            }

        )

    if classification == "Possible Duplicate":

        db.close()

        return templates.TemplateResponse(

            request=request,
            name="add_record.html",

            context={

                "status": "warning",

                "message": reason,

                "record": new_record

            }

        )

    db.close()

    return templates.TemplateResponse(

        request=request,
        name="add_record.html",

        context={

            "status": "success",

            "message": "Please verify your information before saving.",

            "record": new_record

        }

    )


@app.post("/confirm", response_class=HTMLResponse)
def confirm_record(

    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    address: str = Form(...)

):

    db = SessionLocal()

    record = Record(

        name=name,
        email=email,
        phone=phone,
        address=address

    )

    db.add(record)

    db.commit()

    db.close()

    return HTMLResponse(
        """
        <script>
        alert("Record verified and saved successfully.");
        window.location.href="/";
        </script>
        """
    )

@app.post("/delete/{record_id}")
def delete_record(record_id: int):

    db = SessionLocal()

    record = db.query(Record).filter(
        Record.id == record_id
    ).first()

    if record:

        db.delete(record)
        db.commit()

    db.close()

    return HTMLResponse(
        """
        <script>
        window.location.href="/";
        </script>
        """
    )