import { lazy } from 'react';

// project import
import Loadable from 'components/Loadable';
import MainLayout from 'layout/MainLayout';
import CommonLayout from 'layout/CommonLayout';
import { PATH_ROOT, PATH_DASHBOARD, PATH_MAINTENANCE } from './paths';

// pages routing
const MaintenanceError = Loadable(lazy(() => import('pages/maintenance/404')));
const MaintenanceError500 = Loadable(lazy(() => import('pages/maintenance/500')));
const MaintenanceUnderConstruction = Loadable(lazy(() => import('pages/maintenance/under-construction')));
// const MaintenanceComingSoon = Loadable(lazy(() => import('pages/maintenance/coming-soon')));

// render - dashboard
const HomeDefault = Loadable(lazy(() => import('pages/home')));
const DashboardDefault = Loadable(lazy(() => import('pages/dashboard')));
const CreateJobs = Loadable(lazy(() => import('pages/create-jobs')));

// render - sample page

// render - utilities
// const Color = Loadable(lazy(() => import('pages/components-overview/Color')));

// ==============================|| MAIN ROUTING ||============================== //

const MainRoutes = {
  path: PATH_ROOT,
  children: [
    {
      path: PATH_ROOT,
      element: <MainLayout />,
      children: [
        {
          path: PATH_DASHBOARD.home,
          element: <HomeDefault />
        },
        {
          path: PATH_DASHBOARD.kdcv,
          element: <DashboardDefault />
        },
        {
          path: PATH_DASHBOARD.setting,
          element: <CreateJobs />
        }
      ]
    },
    {
      path: PATH_ROOT,
      element: <CommonLayout />,
      children: [
        {
          path: PATH_MAINTENANCE.error,
          element: <MaintenanceError />
        },
        {
          path: PATH_MAINTENANCE.error500,
          element: <MaintenanceError500 />
        },
        {
          path: PATH_MAINTENANCE.underConstruction,
          element: <MaintenanceUnderConstruction />
        }
      ]
    },
    {
      path: '*',
      element: <CommonLayout />,
      children: [
        {
          path: '*',
          element: <MaintenanceError />
        }
      ]
    }
  ]
};

export default MainRoutes;
