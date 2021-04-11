import { Component, Output, EventEmitter} from '@angular/core';
import {FormBuilder, Validators, FormArray, FormGroup} from '@angular/forms';
import { AppComponent } from '../app.component';


@Component({
  selector: 'app-unauthorized',
  templateUrl: './unauthorized.component.html',
  styleUrls: ['./unauthorized.component.css']
})
export class UnauthorizedComponent{
  @Output("isLoggedInSwitch") isLoggedInSwitch: EventEmitter<any> = new EventEmitter();

  constructor(private fb:FormBuilder) { }


  signInForm : FormGroup = this.fb.group({
    username : ['', Validators.compose([Validators.required, Validators.minLength(4), Validators.maxLength(15)])],
    password: ['', Validators.compose([Validators.required,Validators.minLength(4), Validators.maxLength(15)])]
  },{
    updateOn : 'blur'
  }
  );
  get username(){
    return this.signInForm.get('username')
  }
  get password(){
    return this.signInForm.get('password')
  }


  submitForm(){
    //console.log(this.signInForm.get('username'))
    this.isLoggedInSwitch.emit();
  }
}
