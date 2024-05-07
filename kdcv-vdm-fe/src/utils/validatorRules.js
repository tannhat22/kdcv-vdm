export const validatorRules = {
  required: function (value) {
    return value ? undefined : 'Vui lòng nhập trường này';
  },
  email: function (value) {
    // eslint-disable-next-line no-useless-escape
    const regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    return regex.test(value) ? undefined : 'Trường này phải là email';
  },
  min: function (min) {
    return function (value) {
      return value.length >= min ? undefined : `Vui lòng nhập ít nhất ${min} kí tự`;
    };
  },
  max: function (max) {
    return function (value) {
      return value.length <= max ? undefined : `Vui lòng nhập tối đa ${max} kí tự`;
    };
  },
  number: function (value) {
    const regex = /^[0-9]*$/;
    return regex.test(value) ? undefined : 'Trường này phải là số';
  },
  text: function (value) {
    const regex = /^[A-Z ]+$/i;
    return regex.test(value) ? undefined : 'Trường này phải là chữ';
  },
  chars: function (value) {
    return value.trim().length >= 1 ? undefined : 'Kí tự nhập vào không hợp lệ';
  },
  confirmed: function (elementReference) {
    return function (value) {
      return value === document.querySelector(elementReference).value ? undefined : 'Giá trị nhập vào không khớp';
    };
  }
};
