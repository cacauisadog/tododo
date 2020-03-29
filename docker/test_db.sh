docker run --name tododo -e POSTGRES_USER=test_tododo_flask -e POSTGRES_PASSWORD=tododo \
           -p 5432:5432 \
           -v $TODODO/dkdata/test_postgres:/var/lib/postgresql/data \
           postgres:12