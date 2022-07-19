function f(arr){
    /*
    This function takes in an array of objects and returns an array
    of the objects converted to strings
    */
    
    if (typeof arr != "object"){
     return "Input isn't an array" 
    }//this ensures the input to the function is an object
    
    let lst=[];
    
    for(let i in arr){
      if(arr[i]["name"]==undefined || arr[i]["age"]==undefined || arr[i]["level"]==undefined){
        return "Wrong object element"
      } //This checks each object of the array for the right property
      
      lst.push(arr[i]["name"] + "/" + arr[i]["age"] + "/" + arr[i]["level"]);
    }
    
    return lst;
  }
  
  
  let arr= [{name: 'Seern', age: 23, level: '500 level'}, {name:'BBBgh', age:'twenty three', level: 'year 1'}];
  console.log(f(arr))
  
  arr= {name: 'Seun', age: 23};
  console.log(f(arr))