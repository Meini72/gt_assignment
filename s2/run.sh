docker build -t postgres .
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=123456 -d postgres