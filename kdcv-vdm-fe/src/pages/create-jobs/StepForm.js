import React, { useContext } from 'react';
import { Box, Stepper, Step, StepLabel, Typography } from '@mui/material';
import FirstStep from './FirstStep';
import SecondStep from './SecondStep';
// import Confirm from './Confirm';
// import Success from './Success';
import { CreateJobContext } from 'contexts/CreateJobContext';

// Step titles
const labels = ['First Step', 'Second Step', 'Confirmation'];
const handleSteps = (step) => {
  switch (step) {
    case 0:
      return <SecondStep />;
    case 1:
      return <SecondStep />;
    case 2:
      return <SecondStep />;
    default:
      throw new Error('Unknown step');
  }
};

export default function StepForm() {
  const { activeStep } = useContext(CreateJobContext);

  return (
    <>
      {activeStep === labels.length ? (
        <FirstStep />
      ) : (
        <>
          <Box sx={{ my: 5 }}>
            <Typography variant="h4" align="center">
              Tạo biểu khởi đầu công việc
            </Typography>
            <Typography variant="subtitle2" align="center" sx={{ mt: 2 }}>
              Hãy làm theo từng bước sau đây để thêm một biểu khởi đầu công việc mới
            </Typography>
          </Box>
          <Stepper activeStep={activeStep} sx={{ py: 3 }} alternativeLabel>
            {labels.map((label) => (
              <Step key={label}>
                <StepLabel>{label}</StepLabel>
              </Step>
            ))}
          </Stepper>

          {handleSteps(activeStep)}
        </>
      )}
    </>
  );
}
