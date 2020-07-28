# Octobuy

First, create baremetal instance:

    cd baremetal
    terraform init
    terraform apply -var-file="fixture.tfvars"


will link to an elastic IP (3.9.62.133), SSH into the instance and:

    ssh -i metal.pem ubuntu@3.9.62.133

    sudo apt-get update -y
    sudo apt install docker.io -y
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

    git clone https://github.com/AlbertoWeinrichter/Octobuy.git
    cd Octobuy/baremetal/provision

    sudo curl -L "https://s3.eu-west-2.amazonaws.com/baremetal.bucket/snkrs.apk" -o snkrs.apk
    sudo docker-compose up -d



### Solar System Exploration, 1950s – 1960s

- [x] Add Terraform configuration for baremetal instance and .apk provision
- [x] Kubernetize whole application
- [x] Nuxt front end
- [x] Redis result backend
- [x] Authentication with JWT token
- [ ] Add lambda scraper module for product listings
- [ ] Automate Flask migrations
- [ ] Make Android Emulator VNC scale
- [ ] Websockets to follow task progress
