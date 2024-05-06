Help for running the docker:

pip install Flask
pip install Flask.Alchemy
pip install psycopg2-binary


docker-compose up --force-recreate

docker-compose up --build -d


flask --app src/app run 

docker ps -a  #preveris kontejnerje v dockerju 
docker stop ee5ee4ad91bc # pred brisanjem ga je potrebno ustaviti
docker rm -f ee5eee # brises docker kontejner


#if you have problems (linux)
sudo chmod 666 /var/run/docker.sock

Instructions for the db:
-put csv files into the src/staticFiles/uploads
-if first time:
  1) open the folder
  2) open terminal
  3) docker-compose up --build -d
  4) if necesseray sudo chmod 666 /var/run/docker.sock
  5) cd src
  6) flask --app src/app run
-if not first time:
  1) open folder
  2) cd src
  3) flask --app src/app run
-go to the html page that it's written
-upload csv
