

CMD apt-get update && apt-get -y install python openssl python-dev libssl-dev 
CMD set -eux;\
    pip install --upgrade pip;\
    pip install flask-ask cryptography;
