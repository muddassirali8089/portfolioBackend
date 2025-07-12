document.addEventListener('DOMContentLoaded', function () {
  const isPresentCheckbox = document.querySelector('#id_is_present');
  const endMonthInput = document.querySelector('#id_end_month');
  const endYearInput = document.querySelector('#id_end_year');

  const endMonthRow = endMonthInput.closest('.form-row') || endMonthInput.closest('div');
  const endYearRow = endYearInput.closest('.form-row') || endYearInput.closest('div');

  function toggleEndFields() {
    const checked = isPresentCheckbox.checked;

    if (checked) {
      endMonthInput.value = ''; // Clear value
      endYearInput.value = '';  // Clear value
    }

    endMonthInput.disabled = checked;
    endYearInput.disabled = checked;

    if (endMonthRow) endMonthRow.style.display = checked ? 'none' : '';
    if (endYearRow) endYearRow.style.display = checked ? 'none' : '';
  }

  if (isPresentCheckbox) {
    toggleEndFields(); // Initial load
    isPresentCheckbox.addEventListener('change', toggleEndFields);
  }
});
