
docker build [ -t ｛イメージ名｝ [ :｛タグ名｝ ] ] ｛Dockerfileのあるディレクトリ｝

docker build -t jupyter:1.0 .
docker run -it -p 8000:8888 jupyter:1.0
jupyter notebook --port 8000 --ip=0.0.0.0 --allow-root
