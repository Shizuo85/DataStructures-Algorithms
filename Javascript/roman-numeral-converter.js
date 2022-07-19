function convertToRoman(num) {
  num=num.toString().split("").reverse()

  for(let i=0; i<num.length; i++){
    num[i] = num[i] * 10**(i)
  }

  num=num.reverse();

  num= num.reduce((final, element) => {
    final+=roman(element)
    return final
  }, "")
  
  return num;
}

function roman(num){
  num=num.toString();
  let rom={0:"", 1:"I", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"};

  if(num[0]==2 | num[0]==3){
    let x= 10**(num.length-1)
    return rom[x].repeat(num[0])
  }
  else if(num[0]==4 | num[0]==9){
    let x= 10**(num.length-1)
    return rom[x] + rom[(parseInt(num[0])+1)*x]
  }
  else if(num[0]==6 | num[0]==7 | num[0]==8){
    let x= 10**(num.length-1)
    return rom[5*x] + rom[x].repeat(num[0]-5)
  }
  else{
    return rom[num]
  }
}

console.log(convertToRoman(3999));