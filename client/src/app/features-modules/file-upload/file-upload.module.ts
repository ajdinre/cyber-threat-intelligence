import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, RoutesRecognized } from '@angular/router';
import { SharedModule } from './../../shared/shared.module';
import { FileUploadComponent } from './file-upload.component';
import { routes } from './file-upload.routes';


@NgModule({
  declarations: [
    FileUploadComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
    RouterModule.forChild(routes),

  ],

})
export class FileUploadModule{
  public static routes = routes;
 }
