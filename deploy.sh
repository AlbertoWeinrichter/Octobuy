#!/usr/bin/env bash

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
docker image rm auth-backend:1
docker build --tag auth-backend:1 --file auth-backend/Dockerfile .
kubectl delete --filename auth-backend/deployment.yaml
kubectl create --filename auth-backend/deployment.yaml
kubectl delete --filename auth-backend/service.yaml
kubectl create --filename auth-backend/service.yaml

### AUTH FRONTEND ###
docker image rm auth-frontend:1
docker build --tag auth-frontend:1 --file auth-frontend/Dockerfile .
kubectl delete --filename auth-frontend/deployment.yaml
kubectl apply --filename auth-frontend/deployment.yaml
kubectl delete --filename auth-frontend/service.yaml
kubectl apply --filename auth-frontend/service.yaml

### INGRESS ###
kubectl apply --filename ingress.yaml

### DASHBOARD BACKEND ###
#docker image rm auth-backend:1
#docker build --tag auth-backend:1 --file auth-backend/Dockerfile .
#kubectl delete --filename auth-backend/deployment.yaml
#kubectl create --filename auth-backend/deployment.yaml
#kubectl delete --filename auth-backend/service.yaml
#kubectl create --filename auth-backend/service.yaml

#### DASHBOARD FRONTEND ###
#docker image rm auth-frontend:1
#docker build --tag auth-frontend:1 --file auth-frontend/Dockerfile .
#kubectl delete --filename auth-frontend/deployment.yaml
#kubectl apply --filename auth-frontend/deployment.yaml
#kubectl delete --filename auth-frontend/service.yaml
#kubectl apply --filename auth-frontend/service.yaml

### CELERY ###
kubectl delete --filename worker/controller.yaml
kubectl apply --filename worker/controller.yaml


echo "$(minikube ip) octobuy-app.com" | sudo tee -a /etc/hosts

# TODO: remove deletes and leave only applys
# TODO:
