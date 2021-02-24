run-app:
	docker-compose up --build

run-tests:
	docker-compose exec api python -m pytest "src/tests"

stop:
	docker-compose down 

run-lftests:
	docker-compose exec api python -m pytest "src/tests" --lf

run-fftests:
	docker-compose exec api python -m pytest "src/tests" --ff

run-sh:
	docker-compose exec api sh

run-psql:
	docker-compose exec api-db psql -U postgres

cpsql:
	psql -U postgres -h localhost -p 5432 

# Utilities

local-createdb:
	docker-compose exec api python manage.py recreate_db
local-seed:
	docker-compose exec api python manage.py seed_db

# Running a specific test
# docker-compose exec api python -m pytest "src/tests" -k "test_upload_valid_file"
# activate env 		=>	source env/bin/activate
# deactivate env 	=>	deactivate
# change permission $ sudo chown -R <user-name> <directory-name>
# change permission $ sudo chown -R hphesto .

# git remote rm, -v


# For times in need

docker-stop-all:
	docker container stop $(docker container ls -aq)

kill-postgres:
	sudo systemctl stop postgres

kill-redis:
	sudo /etc/init.d/redis-server stop
	
kill-switch:
	docker system prune



# Heroku deploy 

hcreate:
	heroku create

hlogin: 
	heroku container:login 

hpostgres:
	heroku addons:create heroku-postgresql:hobby-dev --app murmuring-beyond-76885

hregistry:
	docker build -f Dockerfile.prod -t registry.heroku.com/murmuring-beyond-76885/web .

hrun-local:
	docker run --name flask-tdd -e "PORT=8765" -p 5005:8765 registry.heroku.com/murmuring-beyond-76885/web:latest

hremove:
	docker rm flask-tdd

hpush:
	docker push registry.heroku.com/murmuring-beyond-76885/web:latest

hrelease:
	heroku container:release web --app murmuring-beyond-76885

hlogs:
	heroku logs --app murmuring-beyond-76885

hcreatedb:
	heroku run python manage.py recreate_db --app murmuring-beyond-76885

hseed:
	heroku run python manage.py seed_db --app murmuring-beyond-76885


# CI
htoken:
	heroku auth:token

## app url https://murmuring-beyond-76885.herokuapp.com

