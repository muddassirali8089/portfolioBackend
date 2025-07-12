
document.addEventListener('DOMContentLoaded', function () {
  const percentField = document.querySelector('input[name="percent"]');
  if (percentField) {
    const display = document.createElement('div');
    display.id = 'percent-value';
    display.style.marginTop = '2px';
    display.style.marginLeft = '20px';
    display.style.fontWeight = 'bold';
    display.innerText = percentField.value + '%';
    percentField.parentNode.appendChild(display);

    percentField.addEventListener('input', function () {
      display.innerText = this.value + '%';
    });
  }
});
