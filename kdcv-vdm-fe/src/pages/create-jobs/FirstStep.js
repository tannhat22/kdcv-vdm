import PropTypes from 'prop-types';
import { Box, Button, Grid, TextField, Typography } from '@mui/material';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronRight, faChevronLeft } from '@fortawesome/free-solid-svg-icons';

import { useState, useContext, useCallback } from 'react';

import { useLocales } from 'locales';
import { CreateJobContext } from 'contexts/CreateJobContext';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: '50%',
  padding: 0
};

// ==============================|| CREATE-JOBS ||============================== //

const FirstStep = () => {
  const { formValues, handleChange, handleBack, handleNext } = useContext(CreateJobContext);
  const { jobId, jobName, draftedPlace, drafter } = formValues;
  const { translate } = useLocales();

  // Check if all values are not empty and if there are some errors
  const isError = useCallback(
    () =>
      Object.keys({ jobId, jobName, draftedPlace, drafter }).some(
        (name) => (formValues[name].required && !formValues[name].value) || formValues[name].error
      ),
    [formValues, jobId, jobName, draftedPlace, drafter]
  );

  // const [values, setValues] = useState({
  //   job_id: '',
  //   job_name: '',
  //   drafted_place: '',
  //   drafter: ''
  // });
  // const [errors, setErrors] = useState({
  //   job_id: '',
  //   job_name: '',
  //   drafted_place: '',
  //   drafter: ''
  // });

  // const handleSubmit = (e) => {
  //   e.preventDefault();
  //   console.log(values);
  //   const postNewJob = async (job) => {
  //     try {
  //       const { data: response } = await axios.post('/job', job);
  //       console.log(response);
  //     } catch (error) {
  //       console.error(error.message);
  //     }
  //   };

  //   postNewJob(values);
  // };

  // const handleChange = (e) => {
  //   setValues({
  //     ...values,
  //     [e.target.name]: e.target.value
  //   });
  // };

  // const handleBlur = (e) => {
  //   const validate = validatorRules.required(e.target.value);
  //   setErrors({
  //     ...errors,
  //     [e.target.name]: validate
  //   });
  // };

  // const handleInput = (e) => {
  //   if (errors[e.target.name] !== undefined) {
  //     setErrors({
  //       ...errors,
  //       [e.target.name]: undefined
  //     });
  //   }
  // };

  return (
    <>
      <Grid container rowSpacing={3.5} columnSpacing={2.75}>
        <Grid item xs={12} md={12} lg={12}>
          <Typography>Job ID:</Typography>
          <TextField
            name="jobId"
            type="text"
            fullWidth
            placeholder={translate('Ex: T19Y001V00-VDM001-AE')}
            variant="outlined"
            required={jobId.required}
            error={!!jobId.error}
            helperText={jobId.error}
            onChange={handleChange}
          />
        </Grid>
        <Grid item xs={12} md={6} lg={6}>
          <Typography>Drafted place:</Typography>
          <TextField
            name="draftedPlace"
            type="text"
            fullWidth
            placeholder={translate('Ex: VDM')}
            variant="outlined"
            required={draftedPlace.required}
            error={!!draftedPlace.error}
            helperText={draftedPlace.error}
            onChange={handleChange}
          />
        </Grid>
        <Grid item xs={12} md={6} lg={6}>
          <Typography>Drafter:</Typography>

          <TextField
            name="drafter"
            type="text"
            fullWidth
            placeholder={translate('Ex: Nguyen Van A')}
            variant="outlined"
            required={drafter.required}
            error={!!drafter.error}
            helperText={drafter.error}
            onChange={handleChange}
          />
        </Grid>
        <Grid item xs={12} md={12} lg={12}>
          <Typography>Job name:</Typography>
          <TextField
            name="jobName"
            type="text"
            fullWidth
            placeholder={translate('Ex: Kiểm tra ngoại quan vỏ nhỏ')}
            multiline
            maxRows={5}
            variant="outlined"
            required={jobName.required}
            error={!!jobName.error}
            helperText={jobName.error}
            onChange={handleChange}
          />
        </Grid>

        {/* {isLoad ? (
              <Grid item>
                <LinearProgress />
              </Grid>
            ) : null} */}
      </Grid>
      <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
        <Button
          variant="contained"
          size="medium"
          sx={{ mt: 3, ml: 1 }}
          disabled={isError()}
          color="primary"
          onClick={!isError() ? handleNext : () => null}
          endIcon={<FontAwesomeIcon icon={faChevronRight} />}
        >
          Next
        </Button>
      </Box>
    </>
  );
};

export default FirstStep;
