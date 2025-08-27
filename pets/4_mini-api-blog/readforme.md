# Добавить пользователя
```
curl -X POST "http://127.0.0.1:8000/users" -H "Content-Type: application/json" -d "{\"username\": \"someuser\"}"
```
## Ответ JSON
```
{
  "id": 1,
  "username": "trifonix"
}
```
---
