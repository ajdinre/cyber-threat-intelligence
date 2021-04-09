import { Routes } from '@angular/router';

import { NoContentComponent } from './no-content/no-content.component';
import { UnauthorizedComponent } from './unauthorized/unauthorized.component';

export const ROUTES: Routes =
  [
    {
      path: '',
      redirectTo: 'home',
      pathMatch: 'full',
    },
    {
      path: 'home',
      loadChildren: './feature-modules/dashboard/dashboard.module#DashboardModule'
    },
    {
      path: 'unauthorized',
      component: UnauthorizedComponent
    },
    {
      path: '**',
      component: NoContentComponent
    }
  ];
