import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Validators } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatButton } from '@angular/material/button';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent implements OnInit {
  fileUploadForm;
  constructor(private fb: FormBuilder) { }

  ngOnInit(): void {
    this.initializeForm();

  }
  afuConfig = {
    multiple: false,
    formatsAllowed: ".txt,.docx,.pdf,.",
    maxSize: 40, // File size in MBs
    uploadAPI:  {
      url:"https://example-file-upload-api",
      /*method:"POST",
      headers: {
     "Content-Type" : "text/plain;charset=UTF-8",
     "Authorization" : `Bearer ${token}`
      },
      params: {
        'page': '1'
      },
      responseType: 'blob',*/
    },
    theme: "attachPin",
    hideProgressBar: false,
    hideResetBtn: false,
    hideSelectBtn: false,
    fileNameIndex: true,
    replaceTexts: {
      selectFileBtn: 'Select Files',
      resetBtn: 'Reset',
      uploadBtn: 'Upload',
      dragNDropBox: 'Drag N Drop',
      attachPinBtn: 'Attach Files...',
      afterUploadMsg_success: 'Successfully Uploaded !',
      afterUploadMsg_error: 'Upload Failed !',
      sizeLimit: 'Size Limit'
    }
  };
  initializeForm():void{
    this.fileUploadForm = this.fb.group({
      fileName : ['',[Validators.required,Validators.maxLength(20)]],
      serverName : ['', [Validators.required,Validators.maxLength(20)]],
      fileUploadSuccess : [false, Validators.requiredTrue]
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
  }
}
