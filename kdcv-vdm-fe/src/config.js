import { PATH_DASHBOARD } from 'routes/paths';

export const HOST_BASE_URL = process.env.REACT_APP_API_URL;
export const HOST_BASE_PORT = process.env.REACT_APP_API_PORT;

// ==============================|| THEME CONSTANT  ||============================== //
export const drawerWidth = 300;

export const twitterColor = '#1DA1F2';
export const facebookColor = '#3b5998';
export const linkedInColor = '#0e76a8';

// ${HOST_BASE_URL}:${HOST_BASE_PORT}
export const APP_DEFAULT_PATH = `${PATH_DASHBOARD.home}`;
// ==============================|| THEME CONFIG  ||============================== //

const config = {
  defaultPath: '/home',
  fontFamily: `'Public Sans', sans-serif`,
  i18n: 'en',
  miniDrawer: false,
  container: true,
  mode: 'light',
  presetColor: 'default',
  themeDirection: 'ltr'
};

export default config;
