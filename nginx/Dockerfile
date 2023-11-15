# For testing purposes: 

FROM nginx:1.19-alpine

COPY ./nginx.conf /etc/nginx/templates/nginx.conf.template

COPY certificates/nginx.crt nginx/certificates/nginx.crt
COPY certificates/nginx.key nginx/certificates/nginx.key

COPY logs/access.log /var/log/nginx/access.log
COPY logs/error.log /var/log/nginx/error.log

EXPOSE 80 443

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]