# https://www.baeldung.com/ops/docker-container-shell

FROM kalilinux/kali-rolling

RUN apt-get update && \
  apt-get install -y \
  python3 \ 
  python3-venv \
  python3-pip \
  python3-bluez \
  # python-obexftp \
  bluetooth \
  wget \
  nmap \
  neovim

WORKDIR /ws

SHELL ["/bin/bash", "-c"]

RUN python3 -m venv violent-python-env && \
  source violent-python-env/bin/activate && \
  pip3 install python-nmap \
  pyPdf \
  pygeoip \
  mechanize \
  BeautifulSoup4

# RUN set -o vi

# CMD wget https://xael.org/pages/python-nmap-0.7.1.tar.gz -O nmap.tar.gz && \
#   tar -xzf nmap.tar.gz

COPY . .
