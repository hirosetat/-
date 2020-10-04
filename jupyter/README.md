# jupyter実行

Dockerfileがあるpathで
```
docker build -t .
docker build -t jupyter .
```

buildが終わったら
```
docker run -it --name jupyternote -p 8000:8888 jupyter /bin/
```

buildが終わったらDocker内の環境に入って以下のコマンドを入力し、jupyterを起動
```
jupyter notebook --allow-root
```
その後、localhost:8000をブラウザ上で入力し、画面にtokenを入力したら分析環境の構築終了です

# その他(再度Docker内の環境に入る場合、以下のコマンドを入力する)

```
docker exec -i -t f44cfe7eda58 bashs
```

# Anaconda環境

- Anaconda 4.8.0
- Python 3.7.1