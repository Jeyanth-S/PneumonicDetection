import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './upload.html',
  styleUrl: './upload.css'
})
export class UploadComponent {

  patientId = '';
  selectedFile!: File;
  result: any;

  constructor(private api: ApiService) {}

  onFileChange(event: any) {
    this.selectedFile = event.target.files[0];
  }

  submit() {
    if (!this.patientId || !this.selectedFile) return;

    this.api.predict(this.patientId, this.selectedFile)
      .subscribe(res => this.result = res);
  }
}