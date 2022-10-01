FROM nginx:1.23.1-alpine

RUN apk add --no-cache bash

COPY wait.sh /wait.sh

RUN chmod +x /wait.sh

CMD ["/wait.sh", "localhost:3000", "--", "nginx", "-g", "daemon off;"]

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d