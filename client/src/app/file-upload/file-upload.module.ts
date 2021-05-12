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
import { CookieService } from 'ngx-cookie-service';
import { FileService } from '../shared/services/file.service';
import { HttpParams } from '@angular/common/http';
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
  ],
  providers: [
    CookieService,
    FileService,
    HttpParams
  ]

})
export class FileUploadModule{
  //public static routes = routes;
 }
