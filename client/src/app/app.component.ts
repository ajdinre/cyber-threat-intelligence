import { InstantiateExpr } from '@angular/compiler';
import { Component,ViewChild, OnInit, Inject } from '@angular/core';
import { MatSidenavModule } from '@angular/material/sidenav';
import { Router,ActivatedRoute, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  name = 'Get Current Url Route Demo';
  currentRoute: string | undefined;
  isLoggedIn: boolean = false;
  initialRoute: string | undefined;
  title = 'client';

  constructor(private router: Router,private ActivatedRoute:ActivatedRoute){
  }


  ngOnInit(){
    this.router.events.pipe(
      filter(event=>event instanceof NavigationEnd)).subscribe(()=>{
        console.log(this.ActivatedRoute.root)
      })

  }

  isLoggedInSwitch(){
    this.isLoggedIn = !this.isLoggedIn
    this.router.navigate(['authorized'])
  }
}
