export const initialValues = {
  jobId: {
    value: '',
    error: '',
    required: true,
    validate: 'chars',
    minLength: 5,
    maxLength: 20
  },
  jobName: {
    value: '',
    error: '',
    required: true,
    validate: 'chars',
    minLength: 2,
    maxLength: 150
  },
  draftedPlace: {
    value: '',
    error: '',
    required: true,
    validate: 'chars',
    minLength: 2,
    maxLength: 20
  },
  drafter: {
    value: '',
    error: '',
    required: true,
    validate: 'chars',
    minLength: 2,
    maxLength: 20
  }
};
