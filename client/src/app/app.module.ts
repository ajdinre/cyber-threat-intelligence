import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
//import { HeaderComponent } from './shared/components/header/header.component';
//import { FooterComponent } from './shared/components/footer/footer.component';
import { SharedModule } from './shared/shared.module';
import { VisitorModule } from './modules/visitor/visitor.module';

@NgModule({
  declarations: [
    AppComponent,
    //SharedModule

    //FooterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SharedModule,
    VisitorModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
