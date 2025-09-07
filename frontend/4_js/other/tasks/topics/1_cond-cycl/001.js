/*
Инициалы имени
Реализуйте функцию, которая по полному имени, состоящему из имени и фамилии, возвращает инициалы:
console.log(abbrevName("Natalie Portman")); // "N.P."
Гарантируется, что полное имя состоит из двух слов, разделенных одним пробелом.
*/

function abbrevName(name) {
  name = name.split(' ');
  name = `${name[0][0]}.${name[1][0]}.`;
  return name;
}

console.log(abbrevName("Natalie Portman"));
