import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Passenger } from '../models/passenger.model';
import { response } from '../models/response.model';

@Injectable({
  providedIn: 'root'
})
export class PassengerService {

  // private apiUrl = 'https://spaceship-titanic-f20313314e4a.herokuapp.com';

  constructor(private http: HttpClient) { }

  // findIfTransported(data: Passenger): response{

  //   console.log('Data recieved in service')
  //   console.log(data);

  //   var prediction_response: response | any;

  //   this.http.get(this.apiUrl + JSON.stringify(data)).subscribe((api_response) => {
  //       prediction_response = api_response;
  //   });

  //   return prediction_response
  // }


  findIfTransported(data: Passenger): Observable<response> {
    console.log('Data received in service', data);

    // If you're trying to send data via GET (not typical, but possible)
    // It'd be in the format of: this.apiUrl?param1=value1&param2=value2...

    // If your server expects a POST request:
    return this.http.post<response>('/predict', data);
      // .pipe(
      //   catchError(this.handleError)
      // );
  }

}
