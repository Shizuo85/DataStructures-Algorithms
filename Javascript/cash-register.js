function checkCashRegister(price, cash, cid) {
  let currency = {"PENNY"	:0.01, "NICKEL"	: 0.05, "DIME" : 0.1, "QUARTER"	: 0.25, "ONE" : 1, "FIVE"	: 5, "TEN"	: 10, "TWENTY"	: 20, "ONE HUNDRED"	: 100}
  let change= cash-price;
  if (cid.reduce((sum, element) => 
  {
    sum+= element[1]
    return sum
  }, 0)==change){
      return {status: "CLOSED", change: cid}
  }
  cid = cid.map( element => {
    element[1] = parseInt((element[1]/currency[element[0]]).toFixed());
    return element
  }).reverse()
  let finalChange=[];
  for(let i=0; i<cid.length; i++){
    if(change/currency[cid[i][0]]>=1 & cid[i][1]!=0){
      let x=Math.floor(change/currency[cid[i][0]])
      if (x>cid[i][1]){
        x=cid[i][1]
        change-=x*currency[cid[i][0]]
        change=parseFloat(change.toFixed(2))
      }
      else{
        change-=x*currency[cid[i][0]]
        change=parseFloat(change.toFixed(2))
      }
      finalChange.push([cid[i][0], x*currency[cid[i][0]]])
    }
  }
  if(change!=0){
    return {status: "INSUFFICIENT_FUNDS", change: []}
  }
  else{
    return {status: "OPEN", change: finalChange}
  }
}

console.log(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));