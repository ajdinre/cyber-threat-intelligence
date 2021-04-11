/*
import { Routes } from '@angular/router';

import { NoContentComponent } from './no-content/no-content.component';
import { UnauthorizedComponent } from './unauthorized/unauthorized.component';

export const ROUTES: Routes =
  [
    {
      path: '',
      redirectTo: 'home',
      pathMatch: 'full'
    },
    {
      path: 'home',
      loadChildren: ()=> import('src/app/features-modules/home/home.module').then(m=>m.HomeModule)
    },
    {
      path: 'file-upload',
      loadChildren: ()=> import('src/app/features-modules/file-upload/file-upload.module').then(m=>m.FileUploadModule)

    }
    ,
    {
      path: 'unauthorized',
      component: UnauthorizedComponent
    },
    {
      path: '**',
      component: NoContentComponent
    }
  ];
*/
