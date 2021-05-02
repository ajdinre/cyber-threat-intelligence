import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, RoutesRecognized } from '@angular/router';
import { SharedModule } from '../shared/shared.module';
import { FileUploadComponent } from './file-upload.component';
import { FileUploadRoutingModule } from './file-upload-routing.module';
import { AngularFileUploaderModule } from "angular-file-uploader";
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatCardModule } from '@angular/material/card';
import { ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';

@NgModule({
  declarations: [
    FileUploadComponent
  ],
  imports: [
    CommonModule,
    FileUploadRoutingModule,
    AngularFileUploaderModule,
    FlexLayoutModule,
    MatButtonModule,
    MatCardModule,
    ReactiveFormsModule

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
