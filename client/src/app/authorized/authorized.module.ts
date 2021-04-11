//predefined modules
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router,RouterModule,Routes } from '@angular/router';

//my modules
    //import { AppModule } from './../app.module';
import { AuthorizedRoutingModule } from './authorized-routing.module';

//my components
import { AuthorizedComponent } from './authorized.component';

//angular material
import { MatSidenavModule} from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';


@NgModule({
  declarations: [AuthorizedComponent],
  imports: [
    CommonModule,
    AuthorizedRoutingModule,
    MatIconModule,
    MatListModule,
    MatSidenavModule,
    MatToolbarModule
  ],
  exports:[
    AuthorizedComponent
  ]
})
export class AuthorizedModule { }
