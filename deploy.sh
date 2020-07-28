#!/usr/bin/env bash

# open /Applications/SourceTree.app/Contents/MacOS/SourceTree

#docker system prune --all
minikube delete
minikube start --memory 8192 --cpus 3
eval $(minikube docker-env)

### RABBITMQ ###
kubectl apply --filename rabbitmq/deployment.yaml
kubectl apply --filename rabbitmq/service.yaml

### REDIS ###
kubectl apply --filename redis/deployment.yaml
kubectl apply --filename redis/service.yaml

### POSTGRES ###
kubectl apply --filename postgres/deployment.yaml
kubectl apply --filename postgres/service.yaml

### AUTH BACKEND ###
docker image rm auth-backend:1 --force
docker build --tag auth-backend:1 --file auth-backend/Dockerfile .
kubectl delete --filename auth-backend/deployment.yaml
kubectl delete --filename auth-backend/service.yaml
kubectl create --filename auth-backend/deployment.yaml
kubectl create --filename auth-backend/service.yaml

### CELERY ###
kubectl delete --filename worker/controller.yaml
kubectl apply --filename worker/controller.yaml

### INGRESS ###
kubectl apply --filename ingress.yaml
sudo echo "$(minikube ip) octobuy-app.local" | sudo tee -a /etc/hosts



#TODO: running locally for now
#### AUTH FRONTEND ###
#docker image rm auth-frontend:1 --force
#docker build --tag auth-frontend:1 --file auth-frontend/Dockerfile .
#kubectl apply --filename auth-frontend/deployment.yaml
#kubectl apply --filename auth-frontend/service.yaml
