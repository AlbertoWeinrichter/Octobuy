# Octobuy

Exec into baremetal instance and execute:

    sudo apt-get update -y
    sudo apt install docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

    git clone https://github.com/AlbertoWeinrichter/Octobuy.git
    cd Octobuy/baremetal/provision

    sudo curl -L "https://s3.eu-west-2.amazonaws.com/baremetal.bucket/Nike.apk" -o Nike.apk
    sudo docker-compose up -d
