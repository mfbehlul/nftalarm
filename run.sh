sudo docker build -t nftalarm .

sudo docker rm nftalarm -f

sudo docker run -p 8000:8000 -d --name nftalarm nftalarm

sudo docker system prune --all -f

