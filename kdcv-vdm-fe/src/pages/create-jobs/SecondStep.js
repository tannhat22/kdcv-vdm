import PropTypes from 'prop-types';
import {
  Box,
  Button,
  Checkbox,
  Divider,
  FormControlLabel,
  IconButton,
  Grid,
  TextField,
  Typography,
  Tooltip
} from '@mui/material';

import { AddPhotoAlternateIcon } from '@mui/icons-material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronRight, faChevronLeft, faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';

import { useState, useContext, useCallback, Fragment } from 'react';

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

const SecondStep = () => {
  const { formValues, handleChange, handleBack, handleNext } = useContext(CreateJobContext);
  const { step, checkpointCategory, deviceChange, partCodeChange, powerOutage, isMeasure, isAuto, Asub, Bsub, Csub } =
    formValues;
  const { translate } = useLocales();
  const [steps, setSteps] = useState(1);
  const [images, setImages] = useState({});
  const categories = Array.from({ length: steps }, (_, index) => index);
  console.log(images);

  // Check if all values are not empty and if there are some errors
  // const isError = useCallback(
  //   () =>
  //     Object.keys({
  //       step,
  //       checkpointCategory,
  //       deviceChange,
  //       partCodeChange,
  //       powerOutage,
  //       isMeasure,
  //       isAuto,
  //       Asub,
  //       Bsub,
  //       Csub
  //     }).some((name) => (formValues[name].required && !formValues[name].value) || formValues[name].error),
  //   [
  //     formValues,
  //     step,
  //     checkpointCategory,
  //     deviceChange,
  //     partCodeChange,
  //     powerOutage,
  //     isMeasure,
  //     isAuto,
  //     Asub,
  //     Bsub,
  //     Csub
  //   ]
  // );
  const handleImageChange = (event) => {
    console.log(event.target.dataset.category);
    console.log(event.target.dataset.category);
    const selectedFiles = event.target.files;

    // Duyệt qua từng file và đọc nó bằng FileReader
    Array.from(selectedFiles).forEach((file) => {
      const reader = new FileReader();
      reader.onload = (e) => {
        // Tạo một đối tượng hình ảnh mới với URL xem trước và tệp
        const newImage = {
          file: file,
          preview: e.target.result
        };
        // Thêm đối tượng hình ảnh vào mảng
        setImages((prevImages) => ({
          ...prevImages,
          [event.target.dataset.category]: newImage
        }));
      };
      // Đọc tệp hình ảnh
      reader.readAsDataURL(file);
    });
  };

  const handleRemoveStep = (e) => {
    if (steps > 1) {
      setSteps(steps - 1);
    }
  };

  const handleAddStep = (e) => {
    setSteps(steps + 1);
  };

  return (
    <>
      <Grid container rowSpacing={3.5} columnSpacing={2.75}>
        {categories.map((category) => (
          <Fragment key={category}>
            <Grid item xs={12} md={12} lg={12}>
              <Typography variant="h4">Hạng mục {category + 1}:</Typography>
            </Grid>
            <Grid item xs={12} md={12} lg={12}>
              <Typography variant="subtitle1">Hạng mục điểm kiểm:</Typography>
              <TextField
                name="checkpointCategory"
                type="text"
                fullWidth
                placeholder={translate('Ex: Áp lực hơi')}
                variant="outlined"
                multiline
                maxRows={5}
                // required={checkpointCategory.required}
                // error={!!checkpointCategory.error}
                // helperText={checkpointCategory.error}
                // onChange={handleChange}
              />
            </Grid>
            <Grid item xs={12} md={12} lg={12}>
              <Typography variant="subtitle1">Phương thức điểm kiểm:</Typography>
              <TextField
                name="checkpointMethod"
                type="text"
                fullWidth
                variant="outlined"
                multiline
                maxRows={5}
                // required={draftedPlace.required}
                // error={!!draftedPlace.error}
                // helperText={draftedPlace.error}
                // onChange={handleChange}
              />
            </Grid>
            <Grid item xs={12} md={12} lg={12}>
              <Typography variant="subtitle1">PP xác nhận & bản TMKT:</Typography>
              <TextField
                name="confirmMethod"
                type="text"
                fullWidth
                placeholder={translate('Ex: Kiểm tra ngoại quan vỏ nhỏ')}
                multiline
                maxRows={5}
                variant="outlined"
                // required={jobName.required}
                // error={!!jobName.error}
                // helperText={jobName.error}
                // onChange={handleChange}
              />
            </Grid>
            <Grid item xs={12} md={8} lg={8}>
              <Box>
                <Typography variant="subtitle1">Ký lục khi phát sinh thay đổi, sự cố:</Typography>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <FormControlLabel
                    sx={{ flex: '1' }}
                    control={
                      <Checkbox
                        // checked={agreenemt.value}
                        // onChange={handleChange}
                        name="deviceChange"
                        color="primary"
                        // required={agreenemt.required}
                      />
                    }
                    label="(I) Thay đổi thiết bị"
                  />
                  <FormControlLabel
                    sx={{ flex: '1' }}
                    control={
                      <Checkbox
                        // checked={agreenemt.value}
                        // onChange={handleChange}
                        name="partCodeChange"
                        color="primary"
                        // required={agreenemt.required}
                      />
                    }
                    label="(II) Thay đổi mã hàng"
                  />
                  <FormControlLabel
                    sx={{ flex: '1' }}
                    control={
                      <Checkbox
                        // checked={agreenemt.value}
                        // onChange={handleChange}
                        name="powerOutage"
                        color="primary"
                        // required={agreenemt.required}
                      />
                    }
                    label="(III) Cúp điện, điện chập chờn"
                  />
                </div>
              </Box>
              <Box sx={{ mt: '12px' }}>
                <Typography variant="subtitle1">Phân khu:</Typography>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <FormControlLabel
                    sx={{ flex: '1' }}
                    control={
                      <Checkbox
                        // checked={agreenemt.value}
                        // onChange={handleChange}
                        name="Asub"
                        color="primary"
                        // required={agreenemt.required}
                      />
                    }
                    label="Phân khu A"
                  />
                  <FormControlLabel
                    sx={{ flex: '1' }}
                    control={
                      <Checkbox
                        // checked={agreenemt.value}
                        // onChange={handleChange}
                        name="Bsub"
                        color="primary"
                        // required={agreenemt.required}
                      />
                    }
                    label="Phân khu B"
                  />
                  <FormControlLabel
                    sx={{ flex: '1' }}
                    control={
                      <Checkbox
                        // checked={agreenemt.value}
                        // onChange={handleChange}
                        name="Csub"
                        color="primary"
                        // required={agreenemt.required}
                      />
                    }
                    label="Phân khu C"
                  />
                </div>
              </Box>
              <Box sx={{ mt: '12px' }}>
                <Typography variant="subtitle1">Thuộc tính:</Typography>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <FormControlLabel
                    sx={{ flex: '1' }}
                    control={
                      <Checkbox
                        // checked={agreenemt.value}
                        // onChange={handleChange}
                        name="isMeasure"
                        color="primary"
                        // required={agreenemt.required}
                      />
                    }
                    label="Sử dụng đơn vị đo"
                  />
                  <FormControlLabel
                    sx={{ flex: '1' }}
                    control={
                      <Checkbox
                        // checked={agreenemt.value}
                        // onChange={handleChange}
                        name="isAuto"
                        color="primary"
                        // required={agreenemt.required}
                      />
                    }
                    label="Lấy dữ liệu tự động"
                  />
                </div>
              </Box>
            </Grid>
            <Grid item xs={12} md={4} lg={4}>
              <Typography variant="subtitle1">Vị trí điểm kiểm:</Typography>
              {/* <TextField
                name="checkpointPosition"
                type="text"
                fullWidth
                placeholder={translate('Ex: Nguyen Van A')}
                variant="outlined"
                // required={drafter.required}
                // error={!!drafter.error}
                // helperText={drafter.error}
                // onChange={handleChange}
              /> */}
              <Box>
                <input
                  type="file"
                  name="checkpointPosition"
                  accept="image/*"
                  data-category={category}
                  onChange={handleImageChange}
                />

                {images[category] ? (
                  <div
                    style={{
                      margin: '10px',
                      border: '1px solid black',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center'
                    }}
                  >
                    <img
                      width="100%"
                      alt="hình ảnh vị trí kiểm điểm"
                      src={images[category].preview}
                      style={{ objectFit: 'contain', width: '100%', height: 'auto' }}
                    />
                  </div>
                ) : null}
              </Box>
            </Grid>
            <Grid item xs={12} md={12} lg={12}>
              <Divider />
            </Grid>
          </Fragment>
        ))}
      </Grid>

      <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
        <div>
          <Tooltip title="Remove">
            <IconButton aria-label="Remove Category" size="medium" sx={{ mt: 3 }} onClick={handleRemoveStep}>
              <FontAwesomeIcon icon={faMinus} />
            </IconButton>
          </Tooltip>
          <Tooltip title="Add">
            <IconButton aria-label="Add Category" size="medium" sx={{ mt: 3 }} onClick={handleAddStep}>
              <FontAwesomeIcon icon={faPlus} />
            </IconButton>
          </Tooltip>
        </div>
        <div>
          <Button
            variant="outlined"
            size="medium"
            onClick={handleBack}
            sx={{ mt: 3, mr: 1 }}
            startIcon={<FontAwesomeIcon icon={faChevronLeft} />}
          >
            Back
          </Button>
          <Button
            variant="contained"
            size="medium"
            sx={{ mt: 3, ml: 1 }}
            // disabled={isError()}
            color="primary"
            // onClick={!isError() ? handleNext : () => null}
            endIcon={<FontAwesomeIcon icon={faChevronRight} />}
          >
            Next
          </Button>
        </div>
      </Box>
    </>
  );
};

export default SecondStep;
