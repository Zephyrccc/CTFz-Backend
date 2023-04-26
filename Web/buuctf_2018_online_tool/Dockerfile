FROM ctftraining/base_image_nginx_php_56

COPY ./files /var/www/
RUN apk add --update --no-cache nmap && \
    chown -R www-data:www-data /var/www/
