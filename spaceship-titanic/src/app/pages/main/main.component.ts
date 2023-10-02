import { NgModule, Type } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatFormFieldModule } from '@angular/material/form-field';
import { Component } from '@angular/core';
import { FormControl, FormGroup, FormArray, FormBuilder } from '@angular/forms';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';

import { Passenger } from '../../models/passenger.model';
import { response } from '../../models/response.model';

import { PassengerService } from '../../services/passenger.service';

import { SuccessDialogComponent } from '../success-dialog/success-dialog.component';
import { FailedDialogComponent } from '../failed-dialog/failed-dialog.component';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent {

  passengerData: FormGroup = new FormGroup({});

  default_passenger_data = {
    PassengerId: '', //
    HomePlanet: [],
    CryoSleep: false,
    Cabin: '', //
    Destination: [],
    Age: 0,
    VIP: false,
    Name: '', //
    RoomService: 0,
    FoodCourt: 0,
    ShoppingMall: 0,
    Spa: 0,
    VRDeck: 0
  };

  constructor(private fb: FormBuilder, public dialog: MatDialog) {
    this.passengerData = this.fb.group(this.default_passenger_data)

    this.passengerData.valueChanges.subscribe();
  }

  ngOnInit() {

  }

  submit(){
    console.log(this.passengerData.value);
    console.log(JSON.stringify(this.passengerData.value));

    // this.get_prediction(this.passengerData.value);
    var response_dummy = {
      data: {
        transported: true,
        confidence: 80
      },
      error: 'none'
    };
    this.openDialog(response_dummy, SuccessDialogComponent);

    this.reset_form(this.passengerData, this.default_passenger_data);
  }

  reset_form(form: FormGroup, data: any){
    form.reset(data);
  }

  get_prediction(passengerData: Passenger){

    console.log(passengerData);

    //response = this.passenger_service.findIfTransported(passengerData); // send data
    var response:any = {};

    if(!response.error){
    if( response?.data["survived"] == true ){
      this.openDialog(response, SuccessDialogComponent);
    } else{
      this.openDialog(response, FailedDialogComponent);
    }
    }else{
      console.log("Error");
    }


  }

  openDialog(data: response, dialog_component: Type<any>): void {
    const dialogRef = this.dialog.open(dialog_component, {
      width: '250px',
      data: data
    });

  }



}

// TODO :: add json-server
//   to check with API temporarily
// TODO :: after verifying integrate with backend
// TODO :: final changes
// TODO :: move to ML
