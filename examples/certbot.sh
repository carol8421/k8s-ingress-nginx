docker run -it \
           --rm \
           --net host \
            -v /etc/letsencrypt:/etc/letsencrypt \
            -v /var/lib/letsencrypt:/var/lib/letsencrypt \
            gzm55/certbot certonly --manual
