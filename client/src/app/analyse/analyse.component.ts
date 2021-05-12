import { AfterViewInit, Component, ViewChild } from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import {MatSort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import {FlexLayoutModule} from '@angular/flex-layout';
import { FormControl } from '@angular/forms';
import { MatSelectModule } from '@angular/material/select';
import { FileService } from '../shared/services/file.service';
import { HttpClient, HttpParams } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';

export interface FileData {
  id: string;
  serverName: string;
  fileName: string;
  fileSize: string;
  dateUploaded: string;
}

/** Constants used to fill up our data base. */

const NAMES: string[] = [
  'Maia', 'Asher', 'Olivia', 'Atticus', 'Amelia', 'Jack', 'Charlotte', 'Theodore', 'Isla', 'Oliver',
  'Isabella', 'Jasper', 'Cora', 'Levi', 'Violet', 'Arthur', 'Mia', 'Thomas', 'Elizabeth'
];



@Component({
  selector: 'app-analyse',
  templateUrl: './analyse.component.html',
  styleUrls: ['./analyse.component.css']
})
export class AnalyseComponent implements AfterViewInit{
  serverNames = new FormControl();
  private csrf : any;
  serverNamesList : string[] = [];
  searchIpAddressesQuery : string = '';
  ipInputList : string = '';
  displayedColumns: string[] = ['id', 'server name', 'file name', 'file size', 'date uploaded'];
  dataSource: MatTableDataSource<FileData>;
  currentUserName="Karlo";
  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private fileService : FileService,
    private cookieService : CookieService,
    private httpParams : HttpParams
  ) {
    //Pie part
    this.csrf = this.cookieService.get("csrftoken");
      if (typeof(this.csrf) === 'undefined'){
        this.csrf = '';
      }
    // Create 100 users
    const users = Array.from({length: 100}, (_, k) => createNewUser(k + 1));
    this.getServerNames();
    // Assign the data to the data source for the table to render
    this.dataSource = new MatTableDataSource(users);
  }

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
  onSelect(data): void {
    console.log('Item clicked', JSON.parse(JSON.stringify(data)));
  }

  onActivate(data): void {
    console.log('Activate', JSON.parse(JSON.stringify(data)));
  }

  onDeactivate(data): void {
    console.log('Deactivate', JSON.parse(JSON.stringify(data)));

  }
  getServerNames(){
    this.fileService.getServerNames().subscribe((res : any) => {
      JSON.parse(res.forEach(item => {
        console.log(item);
        this.serverNamesList.push(item);
    }))
    });
  }
  searchWithNeo4j(){
    const chosenServerNames = this.serverNamesList.join(',');
    this.fileService.getFilteredData(chosenServerNames, this.searchIpAddressesQuery)
      .subscribe((res)=>{
        console.log(res);
      });


  }
  searchWithGrafana(){
    console.log("Search with Grafana Button Clicked!")
  }
  searchWithKibana(){
    console.log("Search with Kibana Button Clicked!")
  }
}

/** Builds and returns a new User. */
function createNewUser(id: number): FileData {
  const name = NAMES[Math.round(Math.random() * (NAMES.length - 1))] + ' ' +
      NAMES[Math.round(Math.random() * (NAMES.length - 1))].charAt(0) + '.';

  return {
    id: id.toString(),
    serverName: name,
    fileName: Math.round(Math.random() * 100).toString(),
    fileSize: "20MB",
    dateUploaded: 'today'
  };
}
