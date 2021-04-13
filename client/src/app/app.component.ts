import { Component,ViewChild, OnInit, Inject, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, AfterViewInit{
  title = 'Cyber Threat Intelligence';
  public showMenu = false;
  public toggleSelected = true;
  constructor(private router: Router) {
  }


  ngOnInit(){
  }

  ngAfterViewInit(){
    setTimeout(() => {
      this.showMenu = window.innerWidth > 700 ? true : false;
      this.toggleSelected = this.showMenu;
    }, 0);
  }
  onResize(event){
    this.showMenu = event.target.innerwidth > 700 ? true : false;
    this.toggleSelected = this.showMenu;
  }
  toggle(){
    this.toggleSelected = !this.toggleSelected;
  }
}
