let value = NaN;

value &&= 10; // 10
value ||= 20; // 10
value &&= 30; // 30
value ||= 40; // 30

console.log(value); // 30

/**
 * NaN
 * 20
 * 30
 * 30
 * 
 * 30
 */