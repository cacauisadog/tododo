docker run --name tododo -e POSTGRES_USER=tododo -e POSTGRES_PASSWORD=tododo \
           -p 5432:5432 \
           -v $TODODO/dkdata/postgres:/var/lib/postgresql/data \
           postgres:12