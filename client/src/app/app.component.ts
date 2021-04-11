import { Component,ViewChild, OnInit, Inject } from '@angular/core';
import { MatSidenavModule } from '@angular/material/sidenav';
import { Router } from '@angular/router';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{

  isLoggedIn: boolean = false;
  initialRoute: string | undefined;
  title = 'client';

  constructor(private router: Router){
  }


  ngOnInit(){
  }

  isLoggedInSwitch(){
    this.isLoggedIn = !this.isLoggedIn
    this.router.navigate(['authorized'])
  }
}
