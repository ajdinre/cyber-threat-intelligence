import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import { AnalyseComponent } from './analyse/analyse.component';
import { FileUploadComponent } from './file-upload/file-upload.component';
import { HomeComponent } from './home/home.component';
import { NoContentComponent } from './no-content/no-content.component';
import { UploadedFilesComponent } from './uploaded-files/uploaded-files.component';


export const routes: Routes =
  [
    {
      path: 'uploaded-files',
      component: UploadedFilesComponent

    },
    {
      path: 'analyse',
      component: AnalyseComponent

    },
    {
      path: 'file-upload',
      component: FileUploadComponent

    },
    {
      path: 'home',
      component: HomeComponent
    },
    {
      path: '',
      pathMatch: 'full',
      redirectTo: 'home'
    },
    {
      path: '**',
      component: NoContentComponent
    }
  ];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
