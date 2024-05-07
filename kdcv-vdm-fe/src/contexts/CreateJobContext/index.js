import PropTypes from 'prop-types';
import React, { createContext, useCallback, useMemo, useReducer } from 'react';
import { initialValues } from './initialValues';
import { validatorRules } from 'utils/validatorRules';

export const CreateJobContext = createContext({
  activeStep: 0,
  formValues: initialValues,
  handleChange() {},
  handleNext() {},
  handleBack() {}
});

function reducer(state, action) {
  switch (action.type) {
    case 'increase':
      return {
        ...state,
        activeStep: state.activeStep + 1
      };
    case 'decrease':
      return {
        ...state,
        activeStep: state.activeStep - 1
      };
    case 'form-value':
      return {
        ...state,
        formValues: {
          ...state.formValues,
          [action.name]: {
            ...state.formValues[action.name],
            value: action.fieldValue
          }
        }
      };
    case 'form-error':
      return {
        ...state,
        formValues: {
          ...state.formValues,
          [action.name]: {
            ...state.formValues[action.name],
            error: action.error
          }
        }
      };

    default:
      return state;
  }
}

function CreateJobProvider({ children }) {
  const [{ activeStep, formValues }, dispatch] = useReducer(reducer, {
    activeStep: 0,
    formValues: initialValues
  });

  // Proceed to next step
  const handleNext = useCallback(() => dispatch({ type: 'increase' }), []);
  // Go back to prev step
  const handleBack = useCallback(() => dispatch({ type: 'decrease' }), []);

  // Handle form change
  const handleChange = useCallback((event, checked) => {
    const { type, name, value } = event.target;

    const fieldValue = type === 'checkbox' ? checked : value;

    dispatch({ type: 'form-value', name, fieldValue });

    const fieldName = initialValues[name];
    if (!fieldName) return;

    const { required, validate, minLength, maxLength, helperText } = fieldName;

    let error = '';

    if (required && !!validatorRules.required(fieldValue)) error = validatorRules.required(fieldValue);
    if (minLength && value && validatorRules.min(minLength)(value)) error = validatorRules.min(minLength)(value);
    if (maxLength && value && validatorRules.max(maxLength)(value)) error = validatorRules.max(maxLength)(value);
    if (validate) {
      switch (validate) {
        case 'chars':
          if (value && validatorRules.chars(value)) error = helperText || validatorRules.chars(value);
          break;
        case 'text':
          if (value && validatorRules.text(value)) error = helperText || validatorRules.text(value);
          break;

        case 'number':
          if (value && validatorRules.number(value)) error = helperText || validatorRules.number(value);
          break;

        case 'email':
          if (value && validatorRules.email(value)) error = helperText || validatorRules.email(value);
          break;

        // case 'checkbox':
        //   if (!checked) error = helperText || 'Please provide a valid value.';
        //   break;

        // case 'select':
        //   if (!value) error = helperText || 'Please select a value.';
        //   break;

        default:
          break;
      }
    }

    dispatch({ type: 'form-error', name, error });
  }, []);

  const constextValue = useMemo(
    () => ({
      activeStep,
      formValues,
      handleChange,
      handleNext,
      handleBack
    }),
    [activeStep, formValues, handleChange, handleNext, handleBack]
  );

  return (
    <CreateJobContext.Provider value={constextValue}>
      <div className="mui-step-form">{children}</div>
    </CreateJobContext.Provider>
  );
}

CreateJobProvider.propTypes = {
  children: PropTypes.node.isRequired
};

export default CreateJobProvider;
