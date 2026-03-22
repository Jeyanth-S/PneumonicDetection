import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-report',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './report.html',
  styleUrl: './report.css'
})
export class ReportComponent {

  patientId = '';
  reports: any[] = [];

  constructor(private api: ApiService) {}

  fetchReports() {
    this.api.getReport(this.patientId)
      .subscribe((res: any) => {
        console.log("RAW:", res);

        if (Array.isArray(res)) {
          this.reports = res;
        } else {
          // 🔥 convert object → array
          this.reports = Object.values(res);
        }

        console.log("FINAL:", this.reports);
      });
  }
}