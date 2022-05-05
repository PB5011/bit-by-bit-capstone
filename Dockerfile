#Download base image
FROM ubuntu:21.10

# Set ENV
ENV nginx_vhost /etc/nginx/sites-available/default
ENV php_conf /etc/php/7.4/fpm/php.ini
ENV nginx_conf /etc/nginx/nginx.conf
ENV supervisor_conf /etc/supervisor/supervisord.conf

# LABEL about the custom image
LABEL maintainer="46569055+davidlentsch@users.noreply.github.com"
LABEL version="0.1"
LABEL description="This is a custom Docker image for running the CryptoTutor application."

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Update Ubuntu
RUN apt update && apt upgrade -y

# Install needed packages
RUN apt install build-essential python3-pip python3-django python-is-python3 wget g++ git nginx supervisor -y && apt clean -y

# Build FreeTXL
RUN mkdir /tmp/freetxl-build/ && cd /tmp/freetxl-build && wget http://www.txl.ca/download/29321-txl10.8a.linux64.tar.gz && tar -xvf 29321-txl10.8a.linux64.tar.gz
RUN cd /tmp/freetxl-build/txl10.8a.linux64/ && ./InstallTxl
RUN rm -rf /tmp/freetxl-build

# Build NiCad
RUN mkdir /tmp/nicad-build/ && cd /tmp/nicad-build && wget http://www.txl.ca/download/5659-NiCad-6.2.tar.gz && tar -xvf 5659-NiCad-6.2.tar.gz
RUN cd /tmp/nicad-build/NiCad-6.2 && make
RUN mkdir /usr/local/lib/nicad6 && cp -r /tmp/nicad-build/NiCad-6.2/* /usr/local/lib/nicad6
RUN sed -i 's/LIB=./LIB=\/usr\/local\/lib\/nicad6/g' /tmp/nicad-build/NiCad-6.2/nicad6
RUN sed -i 's/LIB=./LIB=\/usr\/local\/lib\/nicad6/g' /tmp/nicad-build/NiCad-6.2/nicad6cross
RUN cp /tmp/nicad-build/NiCad-6.2/nicad6 /usr/local/bin/
RUN cp /tmp/nicad-build/NiCad-6.2/nicad6cross /usr/local/bin
RUN chmod +x /usr/local/bin/nicad6
RUN chmod +x /usr/local/bin/nicad6cross
RUN rm -rf /tmp/nicad-build

# Get Project
RUN cd /opt && git clone https://github.com/davidlentsch/bit-by-bit-capstone

# Copy NiCad configs to default folder
RUN cp /opt/bit-by-bit-capstone/cryptotutor/nicad_configs/* /usr/local/lib/nicad6/config

# Install pip dependencies
RUN pip install -r /opt/bit-by-bit-capstone/requirement_file.txt

# Configure nginx
RUN rm /etc/nginx/sites-enabled/default
RUN mkdir /var/www/cryptotutor
RUN cp -r /opt/bit-by-bit-capstone/cryptotutor/static /var/www/cryptotutor
RUN cp /opt/bit-by-bit-capstone/cryptotutor-nginx.conf /etc/nginx/sites-available
RUN ln -s /etc/nginx/sites-available/cryptotutor-nginx.conf /etc/nginx/sites-enabled/
#RUN systemctl reload nginx
#RUN nginx -s reload

# Configure project to run in prod mode
# Configuring the secret key doesn't work yet.
# RUN cd /opt/bit-by-bit-capstone/capstone && sed -i "/^SECRET_KEY = .*$/d" settings.py && echo $'\n\n' >> settings.py
# RUN cd /opt/bit-by-bit-capstone/capstone && DJANGO_SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())') && echo SECRET_KEY = \"${DJANGO_SECRET_KEY}\" >> settings.py
RUN cd /opt/bit-by-bit-capstone/capstone && sed -i '/DEBUG = True/c\DEBUG = False' settings.py

# Export the port
EXPOSE 80/tcp

# Copy supervisor configuration
COPY supervisord.conf ${supervisor_conf}

# Specify runtime command
CMD /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
