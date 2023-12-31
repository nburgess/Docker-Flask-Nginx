﻿# Docker-Flask-Nginx
 **Author**: Nicolas Burgess

This application involves two containers: Flask API and Nginx. The Flask API serves endpoints to retrieve information about system resources, including Docker container stats, CPU usage and memory usage. Nginx acts as a reverse proxy, forwarding requests to the Flask API. The application uses a .env file for environment variables. Additionally, SSL/TLS is implemented for secure communication, and the entire setup is orchestrated using Docker Compose for ease of deployment and management.   
  
Endpoints:  
```/data/memory``` retrieves current RAM usage.  
```/data/cpu``` retrieves current CPU usage.  
```/data/containers/stats``` retrieves a list of currently running containers and their running stats.  
  
## 1. Build the Flask Application
Navigate to the app directory and run the following command:  
```
docker build -t nburgess/flask-api:1.0 .
```
## 2. Run the Docker Container
From the root project directory run the following commands:
```
docker-compose build
docker-compose up
```
## 3. Call the application through Nginx
Use the request header 'API-KEY: 42' to access the application.
```
curl --location --request GET 'http://localhost:80/data/containers/stats' \
--header 'API-KEY: 42'
```
