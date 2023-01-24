With all the services ready in docker-compose.yaml ....
1. We need to create a laravel project in src 
    docker-compose run -d --rm composer(serviceName) create-project laravel/laravel .
        . represents the Working directory of composer i.e var/www/html
        due to bind mount it gets reflected in src folder on host
2. Change the mysql config in src/.env created by laravel
    Change DB_HOST to mysql serviceName
    Change DB_DATABASE, DB_USERNAME, DB_PASSWORD as per mysql env maintained for mysql container
3. Run all the CONTAINERS
    docker-compose up -d --build
