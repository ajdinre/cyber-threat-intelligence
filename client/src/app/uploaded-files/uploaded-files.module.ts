import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UploadedFilesRoutingModule } from './uploaded-files-routing.module';
import { UploadedFilesComponent } from './uploaded-files.component';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { FlexLayoutModule } from '@angular/flex-layout';



@NgModule({
  declarations: [UploadedFilesComponent],
  imports: [
    CommonModule,
    UploadedFilesRoutingModule,
    MatTableModule,
    MatPaginatorModule,
    MatSortModule,
    MatFormFieldModule,
    MatInputModule,
    FlexLayoutModule
  ],
  exports: [
    UploadedFilesComponent
  ]
})
export class UploadedFilesModule { }
