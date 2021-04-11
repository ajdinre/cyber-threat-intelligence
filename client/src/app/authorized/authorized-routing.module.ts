import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from '../features-modules/home/home.component';
import { HomeModule } from '../features-modules/home/home.module';
import { AuthorizedComponent } from './authorized.component';

const routes: Routes = [

  {
    path:'',
    //component: HomeComponent,
    pathMatch: 'full',
    loadChildren: ()=> import('./../features-modules/home/home.module').then(m=>m.HomeModule)
  },
  {
    path:'file-upload',
    pathMatch: 'full',
    loadChildren: ()=> import('./../features-modules/file-upload/file-upload.module').then(m=>m.FileUploadModule)
  },

    /*children: [
      {
        path:'home',
        loadChildren: ()=> import('./../features-modules/home/home.module').then(m=>m.HomeModule)

      },
      {
        path:'file-upload',
        loadChildren: ()=> import('./../features-modules/file-upload/file-upload.module').then(m=>m.FileUploadModule)
      }
    ]*/

  /*{
    path:'home',
    loadChildren: ()=> import('./../features-modules/home/home.module').then(m=>m.HomeModule)


  },*/
  /*{
    path:'authorized/file-upload',
    loadChildren: ()=> import('./../features-modules/file-upload/file-upload.module').then(m=>m.FileUploadModule)

  },*/
  /*
  {
    path:'',
    component: AuthorizedComponent
  }*/
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AuthorizedRoutingModule { }
