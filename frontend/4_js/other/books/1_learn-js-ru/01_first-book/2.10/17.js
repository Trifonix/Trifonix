const login = "qwe";

let message;

login === "Сотрудник"
  ? (message = "Привет")
  : login === "Директор"
  ? (message = "Здравствуйте")
  : login === ""
  ? (message = "Нет логина")
  : (message = "");

console.log(message);
