function steamrollArray(arr) {
  while (arr.some(element => Array.isArray(element))){
    let newArray=[];
    arr.map(element => {
      if(Array.isArray(element)){
        newArray.push(...element);
      }
      else{
        newArray.push(element);
      }
    })
    arr=newArray;
  }
  return arr
}

console.log(steamrollArray([1, [], [3, [[4]]]]));