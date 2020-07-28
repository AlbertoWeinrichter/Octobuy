#!/usr/bin/env bash

# open /Applications/SourceTree.app/Contents/MacOS/SourceTree

docker system prune --all
minikube delete
minikube start --memory 12000 --cpus 4
eval $(minikube docker-env)

### RABBITMQ ###
kubectl delete --filename rabbitmq/deployment.yaml
kubectl apply --filename rabbitmq/deployment.yaml
kubectl apply --filename rabbitmq/service.yaml

### REDIS ###
kubectl delete --filename redis/deployment.yaml
kubectl apply --filename redis/deployment.yaml
kubectl apply --filename redis/service.yaml

### POSTGRES ###
kubectl delete --filename postgres/deployment.yaml
kubectl apply --filename postgres/deployment.yaml
kubectl apply --filename postgres/service.yaml

### AUTH BACKEND ###
docker image rm auth-backend:1 --force
docker build --tag auth-backend:1 --file auth-backend/Dockerfile .
kubectl delete --filename auth-backend/deployment.yaml
kubectl create --filename auth-backend/deployment.yaml
kubectl delete --filename auth-backend/service.yaml
kubectl create --filename auth-backend/service.yaml

### CELERY ###
kubectl delete --filename worker/controller.yaml
kubectl apply --filename worker/controller.yaml

#### AUTH FRONTEND ###
docker image rm auth-frontend:1 --force
docker build --tag auth-frontend:1 --file auth-frontend/Dockerfile .
kubectl delete --filename auth-frontend/deployment.yaml
kubectl apply --filename auth-frontend/deployment.yaml
kubectl delete --filename auth-frontend/service.yaml
kubectl apply --filename auth-frontend/service.yaml

### INGRESS ###
kubectl apply --filename ingress.yaml
sudo echo "$(minikube ip) octobuy-app.local" | sudo tee -a /etc/hosts




# TODO:
#kubectl port-forward deployment/auth-frontend 3000:3000
#kubectl port-forward deployment/auth-backend 5000:5000

# TODO: remove deletes and leave only applys
