import { Component,ViewChild, OnInit, Inject } from '@angular/core';
import { MatSidenavModule } from '@angular/material/sidenav';
import { Router, NavigationStart } from '@angular/router';
import { APP_BASE_HREF } from '@angular/common';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{

  isLoggedIn: boolean = false;
  initialRoute: string | undefined;
  title = 'client';

  constructor(
    private router: Router, @Inject(APP_BASE_HREF) private baseHref: string
  ){
    console.log('APP_BASE_HREF is ${this.baseHref}');
  }


  ngOnInit(){
    this.router.events.subscribe((e)=>{
      if (e instanceof NavigationStart && this.initialRoute == null){
        this.initialRoute = e.url;
      }
    })
  }

  isLoggedInSwitch(){
    this.isLoggedIn = !this.isLoggedIn
  }
}
