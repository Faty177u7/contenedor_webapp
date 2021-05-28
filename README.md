# contenedor_webapp

docker pull ubuntu:20.04

docker run -it -p 8080:8080 -v /workspace/contenedor_webapp/volume:/volume --name webpy -h webpy ubuntu:20.04

apt update
apt install -y python3
apt install -y python3-pip 
pip3 install  web.py