import PropTypes from 'prop-types';
import {
  Box,
  Button,
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

import { useState, useContext } from 'react';

import { useLocales } from 'locales';
import axios from 'utils/axios';
import { validatorRules } from 'utils/rules';

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

  const [values, setValues] = useState({
    job_id: '',
    job_name: '',
    drafted_place: '',
    drafter: ''
  });
  const [errors, setErrors] = useState({
    job_id: '',
    job_name: '',
    drafted_place: '',
    drafter: ''
  });

  console.log(errors);
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(values);
    const postNewJob = async (job) => {
      try {
        const { data: response } = await axios.post('/job', job);
        console.log(response);
      } catch (error) {
        console.error(error.message);
      }
    };

    postNewJob(values);
  };

  const handleChange = (e) => {
    setValues({
      ...values,
      [e.target.name]: e.target.value
    });
  };

  const handleBlur = (e) => {
    const validate = validatorRules.required(e.target.value);
    setErrors({
      ...errors,
      [e.target.name]: validate
    });
  };

  const handleInput = (e) => {
    if (errors[e.target.name] !== undefined) {
      setErrors({
        ...errors,
        [e.target.name]: undefined
      });
    }
  };

  return (
    <p>
      <form onSubmit={handleSubmit}>
        <Grid container rowSpacing={4.5} columnSpacing={2.75}>
          <Grid item xs={12} md={12} lg={12}>
            <Typography sx={{ color: 'green' }}>{translate('Add new job')}</Typography>
          </Grid>
          <Grid item xs={12} md={4} lg={4}>
            <Typography>Job ID:</Typography>
            <TextField
              name="job_id"
              type="text"
              fullWidth
              placeholder={translate('Ex: T19Y001V00-VDM001-AE')}
              variant="outlined"
              required
              error={!!errors.job_id}
              helperText={errors.job_id}
              onChange={handleChange}
              onBlur={handleBlur}
              onInput={handleInput}
            />
          </Grid>
          <Grid item xs={12} md={8} lg={8}>
            <Typography>Job name:</Typography>
            <TextField
              name="job_name"
              type="text"
              fullWidth
              placeholder={translate('Ex: Kiểm tra ngoại quan vỏ nhỏ')}
              variant="outlined"
              required
              error={!!errors.job_name}
              helperText={errors.job_name}
              onChange={handleChange}
              onBlur={handleBlur}
              onInput={handleInput}
            />
          </Grid>
          <Grid item xs={12} md={6} lg={6}>
            <TextField
              name="drafted_place"
              type="text"
              fullWidth
              placeholder={translate('Ex: VDM')}
              variant="outlined"
              required
              error={!!errors.drafted_place}
              helperText={errors.drafted_place}
              onChange={handleChange}
              onBlur={handleBlur}
              onInput={handleInput}
            />
          </Grid>
          <Grid item xs={12} md={6} lg={6}>
            <TextField
              name="drafter"
              type="text"
              fullWidth
              placeholder={translate('Ex: Nguyen Van A')}
              variant="outlined"
              required
              error={!!errors.drafter}
              helperText={errors.drafter}
              onChange={handleChange}
              onBlur={handleBlur}
              onInput={handleInput}
            />
          </Grid>

          <Grid item>
            <Button disabled={false} type="submit" fullWidth variant="contained">
              {translate('Add Job')}
            </Button>
          </Grid>

          {/* {isLoad ? (
            <Grid item>
              <LinearProgress />
            </Grid>
          ) : null} */}
        </Grid>
      </form>
    </p>
  );
};

export default CreateJobs;
