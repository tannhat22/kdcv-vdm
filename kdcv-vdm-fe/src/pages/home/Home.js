import React from 'react';
// import { useNavigate } from 'react-router-dom';
// import { useDispatch } from 'react-redux';

// import { IconButton, Tooltip } from '@mui/material';
// import MUIDataTable from 'mui-datatables';
import { createTheme, ThemeProvider } from '@mui/material/styles';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faEye } from '@fortawesome/free-solid-svg-icons';
// import { faTrashCan } from '@fortawesome/free-regular-svg-icons';

import axios from 'utils/axios';
// import SignalLight from 'components/SignalLight';
// import { activeItem } from 'store/reducers/menu';
// import menuItems from 'menu-items';
// import { useLocales } from 'locales';

function Home() {
  //   const { translate } = useLocales();
  //   const [data, setData] = React.useState([]);

  //   const dispatch = useDispatch();
  //   const navigate = useNavigate();
  //   const dashboardUrl = menuItems.items[0].children[2].url;
  //   const dashboardId = menuItems.items[0].children[2].id;

  React.useEffect(() => {
    const fetchData = async () => {
      try {
        const { data: response } = await axios.get('/job');
        console.log(response);
      } catch (error) {
        console.error(error.message);
      }
    };

    fetchData();
  }, []);

  //   const redirectToDashboard = (id, stt) => {
  //     // console.log(id);
  //     dispatch(activeItem({ openItem: [dashboardId] }));
  //     navigate(dashboardUrl, {
  //       state: {
  //         id,
  //         stt
  //       }
  //     });
  //   };

  const getMuiTheme = () =>
    createTheme({
      components: {
        MUIDataTableBodyCell: {
          styleOverrides: {
            root: {
              // backgroundColor: '#FF0000',
            }
          }
        }
      }
    });

  //   const columns = [
  //     {
  //       name: 'stt',
  //       label: ' ',
  //       options: {
  //         filter: false,
  //         sort: false
  //       }
  //     },
  //     {
  //       name: 'id',
  //       label: 'ID',
  //       options: {
  //         filter: true,
  //         sort: false
  //       }
  //     },
  //     {
  //       name: 'name',
  //       label: translate('Machine name'),
  //       options: {
  //         filter: true,
  //         sort: true,
  //         sortThirdClickReset: true
  //       }
  //     },
  //     {
  //       name: 'noLoad',
  //       label: translate('No-load operating time'),
  //       options: {
  //         filter: false,
  //         sort: true,
  //         customBodyRender: (value) => {
  //           let hours = Math.floor(value / 60);
  //           let mins = value % 60;
  //           if (hours < 10) hours = `0${hours}`;
  //           if (mins < 10) mins = `0${mins}`;
  //           return `${hours} h : ${mins} m  `;
  //         }
  //       }
  //     },
  //     {
  //       name: 'underLoad',
  //       label: translate('Underload operating time'),
  //       options: {
  //         filter: false,
  //         sort: true,
  //         customBodyRender: (value) => {
  //           let hours = Math.floor(value / 60);
  //           let mins = value % 60;
  //           if (hours < 10) hours = `0${hours}`;
  //           if (mins < 10) mins = `0${mins}`;
  //           return `${hours} h : ${mins} m  `;
  //         }
  //       }
  //     },
  //     {
  //       name: 'offTime',
  //       label: translate('Shutdown time'),
  //       options: {
  //         filter: false,
  //         sort: true,
  //         customBodyRender: (value) => {
  //           let hours = Math.floor(value / 60);
  //           let mins = value % 60;
  //           if (hours < 10) hours = `0${hours}`;
  //           if (mins < 10) mins = `0${mins}`;
  //           return `${hours} h : ${mins} m  `;
  //         }
  //       }
  //     }
  //     // {
  //     //   name: 'signalLight',
  //     //   label: translate('Signal light'),
  //     //   options: {
  //     //     filter: false,
  //     //     sort: false,
  //     //     download: false,
  //     //     setCellHeaderProps: () => ({
  //     //       style: { textAlign: 'center', justifyContent: 'center' }
  //     //     }),
  //     //     customBodyRender: (value) =>
  //     //       value === 1 ? (
  //     //         <SignalLight color="green" />
  //     //       ) : value === 2 ? (
  //     //         <SignalLight color="yellow" />
  //     //       ) : value === 3 ? (
  //     //         <SignalLight color="red" />
  //     //       ) : (
  //     //         <p>No operation</p>
  //     //       )
  //     //   }
  //     // }
  //     // {
  //     //   name: 'action',
  //     //   label: translate('Action'),
  //     //   options: {
  //     //     filter: false,
  //     //     sort: false,
  //     //     download: false,
  //     //     setCellHeaderProps: () => ({
  //     //       style: { textAlign: 'center', justifyContent: 'center' }
  //     //     }),
  //     //     setCellProps: () => ({
  //     //       style: { textAlign: 'center', justifyContent: 'center' }
  //     //     }),
  //     //     customBodyRender: (value, tableMeta) => {
  //     //       return (
  //     //         <div>
  //     //           <Tooltip title="View" arrow>
  //     //             <IconButton
  //     //               aria-label="view"
  //     //               machineid={tableMeta.rowData[1]}
  //     //               stt={tableMeta.rowData[0]}
  //     //               // color="primary"
  //     //               sx={{ fontSize: '1.1rem', '&:hover': { color: '#1890ff' } }}
  //     //               onClick={(event) => {
  //     //                 redirectToDashboard(
  //     //                   Number(event.currentTarget.getAttribute('machineid')),
  //     //                   Number(event.currentTarget.getAttribute('stt'))
  //     //                 );
  //     //               }}
  //     //             >
  //     //               <FontAwesomeIcon icon={faEye} />
  //     //             </IconButton>
  //     //           </Tooltip>
  //     //         </div>
  //     //       );
  //     //     }
  //     //   }
  //     // }
  //   ];

  //   const options = {
  //     filter: true,
  //     // rowsPerPage: 10,
  //     // rowsPerPageOptions: [10, 20, 100],
  //     filterType: 'dropdown',
  //     responsive: 'standard',
  //     fixedHeader: true,
  //     tableBodyHeight: '760px',
  //     selectableRows: 'none',
  //     downloadOptions: {
  //       filename: 'datamachine.csv'
  //     }
  //   };

  return (
    <ThemeProvider theme={getMuiTheme()}>
      {/* <MUIDataTable title={translate('Overall Machine Status Table')} data={data} columns={columns} options={options} /> */}
    </ThemeProvider>
  );
}

export default Home;
