# Octobuy

First, create baremetal instance:

    cd baremetal
    terraform init
    terraform apply -var-file="fixture.tfvars"


will link to octobuy-app.com, SSH into the instance and:

    ssh -i metal.pem ubuntu@3.9.62.133

    sudo apt-get update -y
    sudo apt install docker.io -y
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

    git clone https://github.com/AlbertoWeinrichter/Octobuy.git
    cd Octobuy/baremetal/provision


    sudo curl -L "https://s3.eu-west-2.amazonaws.com/baremetal.bucket/Nike.apk" -o Nike.apk
    sudo curl -L "https://s3.eu-west-2.amazonaws.com/baremetal.bucket/snkrs.apk" -o snkrs.apk
    sudo docker-compose up -d
