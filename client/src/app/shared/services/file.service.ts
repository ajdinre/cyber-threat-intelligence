import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
@Injectable({
  providedIn: 'root'
})
export class FileService {

  constructor(private http:HttpClient) { }


  uploadFile(formData : FormData, csrf:any){
     return this.http.post('/log/upload', formData, {
      headers: {
        'X-CSRFToken' : csrf
      }
    });
  }

}
