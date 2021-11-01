FROM python:3.8

# 以降の RUN, CMD で使われる作業ディレクトリ
WORKDIR /app

# カレントディレクトリにある情報をコンテナ内の ｢/app｣ にコピー
ADD . /app

# requirements.txt に従いパッケージをインストール
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# 待受ポート指定
EXPOSE 5000

# コンテナが起動時に実行するコマンド
CMD ["python", "app.py"]