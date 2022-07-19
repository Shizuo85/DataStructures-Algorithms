function f(arr){
    /*
    This function takes in an array of strings and returns a arr with
    the string converted to an object
    */
    
    if(typeof arr != "object"){
      return "Enter a valid object input"
    }
  
    let newArr=[];
    
    for(let i in arr){
      let obj={}; //object for each string 
      let reg= /[\w\s]+\/[\w\s]+\/[\w\s]+/i; //regex to match expected string
      
      if(typeof arr[i] != "string" || ! reg.test(arr[i])){
        return "Invald object element"
      }
  
      let lst=arr[i].split("/");
      [obj["name"], obj["age"], obj["level"]] = [lst[0], lst[1], lst[2]];
      
      newArr.push(obj);
    }
    return newArr
  }
  
  
  let str=["Seern/23/500 level","BBBgh/twenty three/year 1"];
  console.log(f(str))
  str=["Seun/23/100 level"]
  console.log(f(str))