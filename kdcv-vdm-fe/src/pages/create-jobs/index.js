import PropTypes from 'prop-types';
import {
  Box,
  Button,
  Container,
  IconButton,
  Grid,
  Paper,
  FormControl,
  Select,
  TextField,
  Tooltip,
  InputAdornment,
  InputLabel,
  Modal,
  MenuItem,
  Typography,
  LinearProgress
} from '@mui/material';

import { useState, useContext, Fragment } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus } from '@fortawesome/free-solid-svg-icons';

import { useLocales } from 'locales';
import axios from 'utils/axios';
import CreateJobProvider from 'contexts/CreateJobContext';
import StepForm from './StepForm';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: '50%',
  padding: 0
};

// ==============================|| CREATE-JOBS ||============================== //

const CreateJobs = () => {
  const { translate } = useLocales();
  return (
    <CreateJobProvider>
      <Container component="main" maxWidth="lg" sx={{ mb: 4 }}>
        <Paper variant="outlined" sx={{ p: '24px' }}>
          <StepForm />
        </Paper>
      </Container>
    </CreateJobProvider>
  );
};

export default CreateJobs;
