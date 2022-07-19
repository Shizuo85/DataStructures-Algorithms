function spinalCase(str) {
  let reg=/[A-Z][a-z]+|[a-z]+/g
  str=str.match(reg).map(i => i.toLowerCase()).join("-");
  return str;
}

console.log(spinalCase('This Is Spinal Tap'));