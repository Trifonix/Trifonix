const login = prompt("Кто там?");
if (login === "Админ") {
  const password = prompt("Пароль");
  if (password === "Я Главный") {
    alert("Здравствуйте!");
  } else if (password === null) {
    alert("Отмена");
  } else {
    alert("Неверный пароль");
  }
} else if (login === null) {
  alert("Отмена");
} else {
  alert("Я вас не знаю");
}
