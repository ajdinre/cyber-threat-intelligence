import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { HttpParams} from '@angular/common/http';
import { myFile } from '../components/classes/file';
import { IpAddress } from '../components/classes/ipadrress';
@Injectable({
  providedIn: 'root'
})
export class FileService {

  constructor(
    private http:HttpClient,
    private params:HttpParams
    ) { }


  uploadFile(formData : FormData, csrf:any){
     return this.http.post('/log/upload', formData, {
      headers: {
        'X-CSRFToken' : csrf
      }
    });
  }
  getServerNames(){
    return this.http.get("/servername", {responseType: 'json'});
  }
  getFilteredDataForMatTable(listOfServersQuery :  string, searchIpAddressesQuery : string): Observable<IpAddress[]>{
    let params = new HttpParams();
    params = params.append('servernames', listOfServersQuery);
    params = params.append('ipaddresses', searchIpAddressesQuery);

    return this.http.get<IpAddress[]>('/ip',{
      responseType : 'json',
      params : params
    });
  }
  getAllFiles():Observable<myFile[]>{
    return  this.http.get<myFile[]>("/logfiles", { responseType: "json"})
  }

}
