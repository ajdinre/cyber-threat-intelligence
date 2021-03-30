import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
//import { AppModule } from './app.module';
import { FooterComponent } from './shared/components/footer/footer.component';
//import { HeaderComponent } from './shared/components/header/header.component';
import { VisitorModule } from './modules/visitor/visitor.module';
import { WelcomeTextComponent } from './modules/visitor/components/welcome-text/welcome-text.component';
import { PageNotFoundComponent } from './shared/components/page-not-found/page-not-found.component';
import { VisitorComponent } from './modules/visitor/visitor.component';
const routes: Routes = [
  {
    path: 'signin',
    //component: WelcomeTextComponent,
    component: VisitorComponent
  },
  {
    path: 'home',
    component: FooterComponent,


  },
  {
    path: '',   redirectTo: '/signin', pathMatch: 'full' },
  {
    path: '**', component: PageNotFoundComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
