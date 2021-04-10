import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { NoContentComponent } from './no-content/no-content.component';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SharedComponent } from './shared/shared.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from  '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { UnauthorizedComponent } from './unauthorized/unauthorized.component';
import { AuthorizedComponent } from './authorized/authorized.component';
import { ROUTES } from './app.routes'
import { FormsModule,ReactiveFormsModule } from '@angular/forms';
import { HomeComponent } from './features-modules/home/home.component';
import { SharedModule } from './shared/shared.module';
import { APP_BASE_HREF, PlatformLocation } from '@angular/common';

export function getBaseHref(platformLocation: PlatformLocation):string{
  return platformLocation.getBaseHrefFromDOM();
}

@NgModule({
  declarations: [
    AppComponent,
    UnauthorizedComponent,
    AuthorizedComponent,
    NoContentComponent


  ],
  imports: [
    RouterModule.forRoot(ROUTES),
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatToolbarModule,
    MatIconModule,
    MatSidenavModule,
    MatListModule
  ],
  providers: [
    {
      provide:APP_BASE_HREF,
      useFactory: getBaseHref,
      deps: [PlatformLocation]}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
