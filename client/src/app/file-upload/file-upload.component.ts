import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Validators } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatButton } from '@angular/material/button';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { FileService } from '../shared/services/file.service';


@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent implements OnInit {
  fileUploadForm;
  private csrf : any;
  constructor(
    private fb : FormBuilder,
    private http : HttpClient,
    private fileService : FileService,
    private cookieService : CookieService
    ) {
      this.csrf = this.cookieService.get("csrftoken");
      if (typeof(this.csrf) === 'undefined'){
        this.csrf = '';
      }
    }

  ngOnInit(): void {
    this.initializeForm();
  }

  onFileChange(event) {

    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.fileUploadForm.patchValue({
        fileSource: file
      });
    }
  }
  get f(){
    return this.fileUploadForm.controls;
  }

  initializeForm():void{
    this.fileUploadForm = this.fb.group({
      serverName : ['', [Validators.required,Validators.maxLength(20)]],
      file : ['', [Validators.required]],
      fileSource : ['', [Validators.required]]
    },
    {
     updateOn : 'change'
    });
  }

  submitForm(): void{
    console.log(this.fileUploadForm.value);
    const formData = new FormData();
    formData.append('file', this.fileUploadForm.get('fileSource').value);
    formData.append('servername', this.fileUploadForm.get('serverName').value);
    this.fileService.uploadFile(formData, this.csrf).subscribe(res => {
      alert('Upload Successfully.');
    });
  }
}
