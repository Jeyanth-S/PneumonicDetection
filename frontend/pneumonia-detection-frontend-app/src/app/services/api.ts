import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  predict(patientId: string, file: File) {
    const formData = new FormData();
    formData.append('patient_id', patientId);
    formData.append('file', file);

    return this.http.post(`${this.baseUrl}/predict`, formData);
  }

  getReport(patientId: string) {
    return this.http.get(`${this.baseUrl}/report/${patientId}`);
  }
}