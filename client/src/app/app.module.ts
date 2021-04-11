//predefined modules and components

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Router, Routes } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';

//angular materials modules
import { MatButtonModule } from  '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';

//my componentns
import { NoContentComponent } from './no-content/no-content.component';
import { AppComponent } from './app.component';
import { UnauthorizedComponent } from './unauthorized/unauthorized.component';
import { HomeComponent } from './features-modules/home/home.component';
import { AuthorizedComponent } from './authorized';
import { SharedComponent } from './shared/shared.component';

//my modules
import { AppRoutingModule } from './app-routing.module';
import { routes } from './app-routing.module'
import { SharedModule } from './shared/shared.module';
import { AuthorizedModule } from './authorized/authorized.module';





@NgModule({
  declarations: [
    AppComponent,
    UnauthorizedComponent,
    NoContentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AuthorizedModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatToolbarModule,
    MatIconModule,
    MatSidenavModule,
    MatListModule,


  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
