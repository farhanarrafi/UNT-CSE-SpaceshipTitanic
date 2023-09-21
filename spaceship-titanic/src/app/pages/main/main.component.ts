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
  }

}
