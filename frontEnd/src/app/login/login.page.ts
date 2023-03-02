// import { Component, OnInit } from '@angular/core';

// @Component({
//   selector: 'app-login',
//   templateUrl: './login.page.html',
//   styleUrls: ['./login.page.scss'],
// })
// export class LoginPage implements OnInit {

//   constructor() { }

//   ngOnInit() {
//   }

// }

import { Component } from '@angular/core';
import { DataService } from '../service/homepage.service';

@Component({
  selector: 'app-login',
  templateUrl: 'login.page.html',
  styleUrls: ['login.page.scss'],
})
export class LoginPage {

  data: any;

  constructor(private dataService: DataService) {}

  ngOnInit() {
    console.log(this.data);
    
    this.dataService.getData().subscribe(data => {
      this.data = data;
    });
  }

}

