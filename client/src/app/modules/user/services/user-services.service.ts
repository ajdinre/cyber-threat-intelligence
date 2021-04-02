import { Injectable } from '@angular/core';



// Services for handling information about the current user

@Injectable({
  providedIn: 'root'
})
export class UserServicesService {

  constructor() { }


  // TODO: Implement getting username from backend
  getUserName(): string{
    return 'Username';
  }




}
