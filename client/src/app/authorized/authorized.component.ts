import { Component,ViewChild,AfterViewInit, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {MatSidenavModule} from '@angular/material/sidenav';
import * as EventEmitter from 'events';

@Component({
  selector: 'app-authorized',
  templateUrl: './authorized.component.html',
  styleUrls: ['./authorized.component.css']
})
export class AuthorizedComponent implements AfterViewInit{
  public showMenu = false;
  public toggleSelected = true;

  constructor(private router: Router) {

   }

  ngAfterViewInit(){
    setTimeout(() => {
      this.showMenu = window.innerWidth > 700 ? true : false;
      this.toggleSelected = this.showMenu;
    }, 0);
  }

  chooseRoutedComponent(routeUrl:any[]){
    this.router.navigateByUrl('no-content', {skipLocationChange: true}).then(()=>
      this.router.navigate([routeUrl]));
  }

  onResize(event){
    this.showMenu = event.target.innerwidth > 700 ? true : false;
    this.toggleSelected = this.showMenu;
  }
  toggle(){
    this.toggleSelected = !this.toggleSelected;
  }

}
