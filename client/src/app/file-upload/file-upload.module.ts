import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, RoutesRecognized } from '@angular/router';
import { SharedModule } from '../shared/shared.module';
import { FileUploadComponent } from './file-upload.component';
import { FileUploadRoutingModule } from './file-upload-routing.module';
import { AngularFileUploaderModule } from "angular-file-uploader";
import { FlexLayoutModule } from '@angular/flex-layout';

@NgModule({
  declarations: [
    FileUploadComponent
  ],
  imports: [
    CommonModule,
    FileUploadRoutingModule,
    AngularFileUploaderModule,
    FlexLayoutModule
    //BrowserModule,
    //HttpClientModule
    //SharedModule,
    //RouterModule.forChild(routes),

  ],
  exports: [
    FileUploadComponent,
    AngularFileUploaderModule
  ]

})
export class FileUploadModule{
  //public static routes = routes;
 }
