import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Validators } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatButton } from '@angular/material/button';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent implements OnInit {
  fileUploadForm;
  constructor(
    private fb : FormBuilder,
    private http : HttpClient
    ) { }

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
      fileName : ['',[Validators.required,Validators.maxLength(20)]],
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
    /**
     * TODO:
     * Upload file to server
     * Send input fileName and serverName
     * Send file size.
     * Send date of making the request.
     */
    const formData = new FormData();
    formData.append('file', this.fileUploadForm.get('fileSource').value);

    this.http.post('/log/upload', formData)
      .subscribe(res => {
        console.log(res);
        alert('Uploaded Successfully.');
      })
  }
}
