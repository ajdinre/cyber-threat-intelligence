import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { SharedModule } from './../../shared/shared.module';
import { HomeComponent } from './home.component';
import { HomeRoutingModule } from './home-routing.module';
import { AppModule } from 'src/app/app.module';

@NgModule({
  declarations: [
    HomeComponent
  ],
  imports: [
    CommonModule,
    HomeRoutingModule,
    AppModule
    //SharedModule,
    //RouterModule.forChild(routes),

  ],
  exports:[
    HomeComponent
  ]

})
export class HomeModule {
  //public static routes = routes;
 }
