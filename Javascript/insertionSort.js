function fsort(arr){
    /*
    This function takes in an array arr and returns the ordred version
    */
    if(typeof arr != "object"){
      return "invalid input"
    }
    for(let n in arr){
      for(let i=1; i<arr.length; i++){
        if (arr[i-1]>arr[i]){
          [arr[i-1], arr[i]]= [arr[i], arr[i-1]]
        }
      }
    }
    return arr
  }
  
  let arr=[1,9,4,5,3, 0];
  console.log(fsort(arr));