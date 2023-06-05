import { Component } from '@angular/core';
import { ApiService } from '../service/homepage.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  public items: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit() {

    this.apiService.getItems().subscribe((data: any[]) => {  
        this.items = data;
    });
    // this.apiService.createItem().subscribe((data: any[]) => {
    //   console.log(data)
    // });
  }
  public click(){
    
  }

}
