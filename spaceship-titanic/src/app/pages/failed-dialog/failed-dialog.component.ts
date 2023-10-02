import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { response } from 'src/app/models/response.model';

@Component({
  selector: 'app-failed-dialog',
  templateUrl: './failed-dialog.component.html',
  styleUrls: ['./failed-dialog.component.css']
})
export class FailedDialogComponent {

  constructor(public dialogRef: MatDialogRef<FailedDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public ml_response: response){

  }

  onNoClick(): void {
    this.dialogRef.close();
  }

}
