import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { HttpParams} from '@angular/common/http';
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
  getFilteredDataForMatTable(listOfServersQuery :  string, searchIpAddressesQuery : string){
    let params = new HttpParams();
    params = params.append('serverNames', listOfServersQuery);
    params = params.append('ipAddresses', searchIpAddressesQuery);

    return this.http.get('/ip',{
      responseType : 'json',
      params : params
    });
  }

}
