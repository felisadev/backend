docker rm -f $(docker ps -aq)
docker rmi -f `docker images -qa`
docker pull reddytocode/backend_felisa:main
docker run -d -p 8000:8000 reddytocode/backend_felisa:main
