import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000';
  
  constructor(private http: HttpClient) { }

  public getItems() {
    return this.http.get<any>(`${this.apiUrl}/read/`);
  }
    public getItem(id: number) {
        return this.http.get<any>(`${this.apiUrl}/read/${id}`);
  }
  //   public createItem(data: any) {  
  //       return this.http.post<any>(`${this.apiUrl}/create/`, data);
    // }
  }

