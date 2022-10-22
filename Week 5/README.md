## Steps to follow in the terminal

# 1. When running the docker-compose.yml file for the first time, build the docker compose file in order to avoid psycopg2 error
docker compose up -build

# 2. If not running the docker-compose.yml file for the first time, run the below code
docker compose up

# 3. Open http://localhost:81/ and you should be able to view the mealname & mealprice in html format

# 4. Open http://localhost:5000/ and you should be able to view the mealname & mealprice in json format

# 5. Open http://localhost:80/ and you should be able to view the PGAdmin page. 
# Enter username : admin@admin.com, password: pass
# To create the server details name: db, username: root, password: pass



