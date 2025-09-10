console.log('1', "" + 1 + 1);      // "11"
console.log('2', "" - 1 + 0);      // error     "-1"
console.log('3', true + false);    // 1          
console.log('4', 6 / "3");         // 2          
console.log('5', "2" * "3");       // error     6
console.log('6', 4 + 5 + "px");    // "9px"       
console.log('7', "$" + 4 + 5);     // "$45"
console.log('8', "4" - 2);         // error     2
console.log('9', "4px" - 2);       // error     NaN
console.log('10', " -9 " + 5);      // " -9 5"  
console.log('11', " -9 " - 5);      // error    -14
console.log('12', null + 1);        // NaN      1
console.log('13', undefined + 1);   // 1        NaN
console.log('14', " \t \n" - 2);    // error    -2
