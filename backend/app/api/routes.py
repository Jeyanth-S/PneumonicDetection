from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os

from app.services.model_service import ModelService
from app.services.report_service import ReportService
from app.utils.db import JSONDatabase

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

db = JSONDatabase()
model_service = ModelService("../models/best_model.pth")
report_service = ReportService(db)


@router.post("/predict")
async def predict(patient_id: str = Form(...), file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prediction_data = model_service.predict(file_path)

    report = report_service.add_report(
        patient_id, file_path, prediction_data
    )

    return report


@router.get("/report/{patient_id}")
def get_report(patient_id: str):
    reports = report_service.get_reports(patient_id)

    if not reports:
        return {"error": "Patient not found"}

    return reports