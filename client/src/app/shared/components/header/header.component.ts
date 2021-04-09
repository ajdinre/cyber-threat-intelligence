import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSidenav} from '@angular/material/sidenav';
import {FormsModule} from '@angular/forms';
@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  @ViewChild(MatSidenav)
  sidenav!: MatSidenav;
  events: string[] = [];
  opened: boolean = false;

  constructor() { }

  ngOnInit(): void {
  }

}
