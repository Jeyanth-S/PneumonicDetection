import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { UploadComponent } from './components/upload/upload';
import { ReportComponent } from './components/report/report';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, UploadComponent, ReportComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('pneumonia-detection-frontend-app');
}
