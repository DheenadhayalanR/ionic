import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000';
  data={
      "title": "ummmsaaaa",
    "content": "gfgvvhgb",
    "date_posted": "2023-03-01T10:33:05.860385Z"
}
 
  constructor(private http: HttpClient) { }

  public getItems() {
    return this.http.get<any>(`${this.apiUrl}/read/`);
  }
  public postItems() {
    return this.http.post<any>(`${this.apiUrl}/create/`,this.data);
  }
}

