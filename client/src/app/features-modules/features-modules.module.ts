import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IpSearchTableComponent } from './ip-search-table/ip-search-table.component';
import { GrafanaComponent } from './grafana/grafana.component';
import { GraphStatsComponent } from './graph-stats/graph-stats.component';
import { FileUploaderComponent } from './file-uploader/file-uploader.component';
import { ToolboxComponent } from './grafana/toolbox/toolbox.component';
import { DashboardComponent } from './grafana/dashboard/dashboard.component';
import { FileSearchTableComponent } from './file-search-table/file-search-table.component';
import { HomeComponent } from './home/home.component';
import { FileUploadComponent } from './file-upload/file-upload.component';



@NgModule({
  declarations: [IpSearchTableComponent, GrafanaComponent, GraphStatsComponent, FileUploaderComponent, ToolboxComponent, DashboardComponent, FileSearchTableComponent, FileUploadComponent],
  imports: [
    CommonModule
  ]
})
export class FeaturesModulesModule { }
