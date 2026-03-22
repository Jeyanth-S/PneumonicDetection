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
      .subscribe((res: any) => this.reports = res);
  }
}