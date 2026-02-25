fName = 'John';
sName = 'Smith';

str = `
  <ul>
  <li>my first name: ${fName}</li>
  <li>my second name: ${sName}</li>
  </ul>
`;

document.body.innerHTML = str;

console.log(str);
