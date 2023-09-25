import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PassengerService {

  private apiUrl = '';

  constructor(private http: HttpClient) { }

  findTransported(): Observable<any>{
    return this.http.get('<api_url>');
  }
}
