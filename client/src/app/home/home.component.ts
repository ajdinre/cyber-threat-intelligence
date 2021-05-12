import { AfterViewInit, Component, ViewChild, OnInit } from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import {MatSort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import {FlexLayoutModule} from '@angular/flex-layout';
import { User } from '../shared/components/classes/user';
import { UserService } from '../shared/services/user.service';
import { FileService } from '../shared/services/file.service';
import { HttpParams } from '@angular/common/http';
import { myFile} from '../shared/components/classes/file';



@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit, AfterViewInit {
  public currentUser : User = new User();
  displayedColumns: string[] = ['id', 'log_file', 'created', 'analyzed'];
  dataSource: MatTableDataSource<myFile>;
  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private userService : UserService,
    private fileService : FileService

    )

    {
      this.fileService.getAllFiles().subscribe((res) =>{
        this.dataSource = new MatTableDataSource(res);
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
      });

  }
  ngOnInit(): void{
    this.getUserInfo();
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
  getUserInfo(){
    this.userService.getUserData()
      .subscribe((data:any)=>{
        this.currentUser = data;
      },
      error => {
        console.log(error);
      });
  }
}

