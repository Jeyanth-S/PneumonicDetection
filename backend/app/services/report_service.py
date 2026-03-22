from datetime import datetime

class ReportService:
    def __init__(self, db):
        self.db = db

    def add_report(self, patient_id, image_path, prediction_data):
        data = self.db.load()

        report = {
            "report_id": f"rep_{int(datetime.now().timestamp())}",
            "image_path": image_path,
            "prediction": prediction_data["prediction"],
            "confidence": prediction_data["confidence"],
            "timestamp": str(datetime.now())
        }

        if patient_id not in data:
            data[patient_id] = []

        data[patient_id].append(report)
        self.db.save(data)

        return report

    def get_reports(self, patient_id):
        data = self.db.load()
        return data.get(patient_id, None)