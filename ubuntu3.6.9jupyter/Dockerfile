FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive

# -- Install Emacs, tmux, Font (Ricty Diminished) --
RUN echo 'path-include=/usr/share/locale/ja/LC_MESSAGES/*.mo' > /etc/dpkg/dpkg.cfg.d/includes \
    && apt-get update && apt-get install -y  \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    sudo \
    gosu \
    ibus \
    ibus-mozc \
    language-pack-ja-base \
    language-pack-ja \
    fonts-noto-cjk \
    fonts-noto-color-emoji \
    tzdata \
    emacs \
    tmux \
    fonts-ricty-diminished \
    nfs-common \
    git \
    wget \
    make \
    curl \
    mecab \
    libmecab-dev \
    mecab-ipadic \
    mecab-ipadic-utf8 \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* \
    && rm -rf /var/lib/apt/lists/*

# Python
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# -- Set locale --
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    && echo 'Asia/Tokyo' > /etc/timezone
RUN locale-gen ja_JP.UTF-8 \
    && echo 'LC_ALL=ja_JP.UTF-8' > /etc/default/locale \
    && echo 'LANG=ja_JP.UTF-8' >> /etc/default/locale

# Mecab
RUN mkdir -p /opt/downloads && \
    cd /opt/downloads && \
    git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git

RUN cd /opt/downloads/mecab-ipadic-neologd && \
    ./bin/install-mecab-ipadic-neologd -n -y


# -- Python --
RUN echo 'alias pip=pip3' >> ~/.bashrc
RUN pip install --upgrade pip
RUN echo 'alias python=python3' >> ~/.bashrc

#setup jupyter
RUN pip install jupyter &&  \
    jupyter notebook --generate-config && \
    sed -i -e "s/#c.NotebookApp.ip = 'localhost'/c.NotebookApp.ip = '0.0.0.0'/" /root/.jupyter/jupyter_notebook_config.py && \
    sed -i -e "s/#c.NotebookApp.allow_remote_access = False/c.NotebookApp.allow_remote_access = True/" /root/.jupyter/jupyter_notebook_config.py

COPY ./requirements.txt /root
RUN pip install -r /root/requirements.txt




#ファイルをappディレクトリに追加
COPY app.py /app/

#ルートディレクトリ設定
WORKDIR /app

EXPOSE 8000



