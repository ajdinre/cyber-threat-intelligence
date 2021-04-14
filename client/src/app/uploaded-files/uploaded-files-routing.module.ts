import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UploadedFilesComponent } from './uploaded-files.component';

const routes: Routes = [
  {
    path: '',
    pathMatch:'full',
    component: UploadedFilesComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UploadedFilesRoutingModule { }
