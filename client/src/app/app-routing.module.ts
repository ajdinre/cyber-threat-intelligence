import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {UnauthorizedComponent} from './unauthorized/unauthorized.component'
import { AuthorizedModule } from './authorized/authorized.module';

//import {AuthorizedComponent} from './authorized/authorized.component';


export const routes: Routes =
  [
    {
      path: '',
      redirectTo: 'unauthorized',
      pathMatch: 'full'
    },
    {
      path: 'authorized',
      pathMatch: 'full',
      loadChildren: ()=> import('./authorized/authorized.module').then(m=>m.AuthorizedModule)
    }
    ,

    {
      path: 'unauthorized',
      pathMatch: 'full',
      component: UnauthorizedComponent
    },
    {
      path: '**',
      redirectTo: '',
    }
  ];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
