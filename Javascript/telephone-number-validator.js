function telephoneCheck(str) {
  return /^[1]? ?[\d]{3}-[\d]{3}-[$\d]{4}|^[1]? ?[(][\d]{3}[)] [\d]{3}-[$\d]{4}|^[1]? ?[(][\d]{3}[)][\d]{3}-[$\d]{4}|^[1]? ?[\d]{3} [\d]{3} [$\d]{4}|^[\d]{10}$/.test(str)
}

console.log(telephoneCheck("5555555555"));