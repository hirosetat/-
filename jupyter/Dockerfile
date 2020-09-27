# FROM rottenfruits/analyticker:common
FROM ubuntu:18.04
#install jupyter
#https://daichan.club/linux/78323
# -- Install Emacs, tmux, Font (Ricty Diminished) --
RUN echo 'path-include=/usr/share/locale/ja/LC_MESSAGES/*.mo' > /etc/dpkg/dpkg.cfg.d/includes \
    && apt-get update \
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
    mecab \
    libmecab-dev \
    mecab-ipadic \
    mecab-ipadic-utf8 && \    
    wget -q https://repo.continuum.io/archive/Anaconda3-2018.12-Linux-x86_64.sh -P ./downloads/ && \
    bash ./downloads/Anaconda3-2018.12-Linux-x86_64.sh -b
    # && apt-get clean \
    # && rm -rf /var/cache/apt/archives/* \
    # && rm -rf /var/lib/apt/lists/*
ENV PATH $PATH:/root/anaconda3/bin

#setup jupyter
RUN jupyter notebook --generate-config && \
    sed -i -e "s/#c.NotebookApp.ip = 'localhost'/c.NotebookApp.ip = '0.0.0.0'/" /root/.jupyter/jupyter_notebook_config.py && \
    sed -i -e "s/#c.NotebookApp.allow_remote_access = False/c.NotebookApp.allow_remote_access = True/" /root/.jupyter/jupyter_notebook_config.py


#conda config --remove channels conda-forge && \
RUN conda upgrade -y --all && \
    conda clean -y --packages && \
    conda install -y python=3.7.1 && \
    conda install conda=4.8.0=py37_1 python=3.7.1

#install python packages
RUN conda install -y -c conda scikit-learn && \
    conda install -y -c conda-forge pystan && \
    conda install -y tensorflow && \
    conda install -y keras && \
    conda install -y pytorch-cpu torchvision-cpu -c pytorch && \
    conda install -c pytorch torchtext && \
    conda install -y -c anaconda swig && \
    conda install -y -c anaconda gensim
    # conda install -y -c conda-forge lightgbm
#insatll nlp tool
RUN pip install janome && \
    pip install mecab-python3==0.996.5 && \
    pip install sentencepiece

EXPOSE 8000