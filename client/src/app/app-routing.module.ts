import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {UnauthorizedComponent} from './unauthorized/unauthorized.component'
import { AuthorizedModule } from './authorized/authorized.module';
import { NoContentComponent } from './no-content/no-content.component';

//import {AuthorizedComponent} from './authorized/authorized.component';


export const routes: Routes =
  [
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
      path: '',
      redirectTo: 'unauthorized',
      pathMatch: 'full'
    },
    {
      path: '**',
      //pathMatch: 'full',
      component: NoContentComponent
    }
  ];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
