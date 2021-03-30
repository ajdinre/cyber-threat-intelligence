import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WelcomeTextComponent } from './components/welcome-text/welcome-text.component';
import { VisitorComponent } from './visitor.component';
//import { VisitorComponent } from './visitor.component';




@NgModule({
  declarations: [WelcomeTextComponent,VisitorComponent],
  imports: [
    CommonModule,

  ],
  exports: [
    WelcomeTextComponent
  ]
})
export class VisitorModule { }
