import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Passenger } from '../models/passenger.model';

@Injectable({
  providedIn: 'root'
})
export class PassengerService {

  private apiUrl = '';

  constructor(private http: HttpClient) { }

  findIfTransported(data: Passenger){
    return this.http.get('localhost/4200');
  }
}
