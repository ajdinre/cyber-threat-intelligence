import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, RoutesRecognized } from '@angular/router';
import { SharedModule } from './../../shared/shared.module';
import { HomeComponent } from './home.component';
import { routes } from './home.routes';


@NgModule({
  declarations: [
    HomeComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
    RouterModule.forChild(routes),

  ],

})
export class HomeModule {
  public static routes = routes;
 }
