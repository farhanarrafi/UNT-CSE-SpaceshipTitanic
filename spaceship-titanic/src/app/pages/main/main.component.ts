import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatFormFieldModule } from '@angular/material/form-field';
import { Component } from '@angular/core';
import { FormControl, FormGroup, FormArray, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent {

  passengerData: FormGroup = new FormGroup({});

  constructor(private fb: FormBuilder) {
    this.passengerData = this.fb.group({
      PassengerId: '',
      HomePlanet: [],
      CryoSleep: false,
      Cabin: '',
      Destination: [],
      Age: 0,
      VIP: false,
      Name: '',
      Transported: false,
      RoomService: 0,
      FoodCourt: 0,
      ShoppingMall: 0,
      Spa: 0,
      VRDeck: 0
    })

    this.passengerData.valueChanges.subscribe();
  }

  ngOnInit() {

  }

  submit(passengerData: FormGroup){
    console.log(this.passengerData.value);
    console.log(JSON.stringify(this.passengerData.value));

    passengerData.reset({
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
    });
  }

}
