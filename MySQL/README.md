## CREATE FILE .env

```shell
MYSQL_ROOT_PASSWORD=Lion333
MYSQL_DATABASE=soccer_evolution
```

## CREATE CONTAINER

```shell
docker build -t mysql-soccer_evolution:1.0.0 .
docker run -d -p 5050:3306 --env-file=.env --name soccer_evolution-db mysql-soccer_evolution:1.0.0
```

## DELETE CONTAINER

```shell
docker stop soccer_evolution-db && docker rm -f soccer_evolution-db
```