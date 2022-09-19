let normLot = function(risk,pips){
 
 let result = risk / pips 

  return (result / 10)
}
 //console.log(normLot(80,23))





let lotJpy = function(risk,pips){

  let itr1 = pips/4 * 3
  let itr2 = risk / itr1

  return (itr2/10)
}
console.log(lotJpy(15,27)) 