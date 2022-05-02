const btnMinus = document.querySelector('#minusBtn')
const btnPlus = document.querySelector('#plusBtn')
const targetNum = document.querySelector('#number')



btnMinus.addEventListener('click', function () {
  targetNum.textContent = parseInt(targetNum.textContent) - 1
})

btnPlus.addEventListener('click', function () {
  targetNum.textContent = parseInt(targetNum.textContent) + 1
})