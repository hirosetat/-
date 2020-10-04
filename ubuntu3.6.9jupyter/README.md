
docker build [ -t ｛イメージ名｝ [ :｛タグ名｝ ] ] ｛Dockerfileのあるディレクトリ｝

docker build -t jupyter:1.0 .
docker run -it -p 8000:8888 jupyter:1.0
jupyter notebook --port 8000 --ip=0.0.0.0 --allow-root



docker run -it -p 8000:8888 -v /c/Users/ryu11:mnt   jupyter:1.0


docker build -t anaconda .
docker run -it --name jupyternote -p 8000:8888 anaconda
docker run -it -p 8888:8888 -v /c/Users/{自身のosユーザ名}:mnt anaconda
jupyter notebook --allow-root
docker exec -i -t jupyternote bash

docker run -it -p 8888:8888 -v /c/Users/ryu11/ishiduka:/mnt/src jupyter:1.0

docker build -t jupyter .
docker run -it -p 8888:8888 -v /c/Users/ryu11/ishiduka:/mnt/src jupyter
docker run -it -p 8888:8888 -v /c/Users/ryu11/ishiduka:/mnt/src 

docker exec -i -t 4c02304c53f7  bash
uvicorn main:app --port 8000 --host 0.0.0.0
uvicorn app.main:app --host 0.0.0.0
"uvicorn", "app.main:app", "--host", "0.0.0.0"






ドキュメント