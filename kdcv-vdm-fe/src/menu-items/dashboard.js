// assets
import { FormOutlined, HomeOutlined, SettingOutlined } from '@ant-design/icons';
// icons
const icons = {
  FormOutlined,
  HomeOutlined,
  SettingOutlined
};

// ==============================|| MENU ITEMS - DASHBOARD ||============================== //

const dashboard = {
  id: 'group-dashboard',
  title: 'Navigation',
  type: 'group',
  children: [
    {
      id: 'home',
      title: 'Home',
      type: 'item',
      url: '/home',
      icon: icons.HomeOutlined,
      breadcrumbs: true
    },
    {
      id: 'kdcv',
      title: 'Khởi đầu công việc',
      type: 'item',
      url: '/kdcv',
      icon: icons.FormOutlined,
      breadcrumbs: true
    },
    {
      id: 'setting',
      title: 'Setting',
      type: 'item',
      url: '/setting',
      icon: icons.SettingOutlined,
      breadcrumbs: true
    }
  ]
};

export default dashboard;
