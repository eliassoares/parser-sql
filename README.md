## Parser de arquivo SQL
Com o intuito de deixar o código Python mais limpo, sem queries SQL junto com código Python,
essa função foi criada.

Ela parsea um arquivo SQL passado como parâmetro e retorna um dicionário onde os nomes das queries são as chaves
e os SQLs são os valores.

Examplo:
```sql
-- name: select-all-users
SELECT * FROM user;

--name: delete-user
DELETE FROM user WHERE id = %s;

-- name:insert-user
INSERT INTO user(name, cpf)
VALUES (%s, %s);
```

Irá retornar um dicionário:
```python
{
    'select-all-users': 'SELECT * FROM user',
    'delete-user': 'DELETE FROM user WHERE id = %s',
    'insert-user': 'INSERT INTO user(name, cpf) VALUES (%s, %s)'
}
```
