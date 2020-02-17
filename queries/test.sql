-- name: select-all-users
SELECT * FROM user;

--name: delete-user
DELETE FROM user WHERE id = %s;

-- name:insert-user
INSERT INTO user(name, cpf)
VALUES (%s, %s);