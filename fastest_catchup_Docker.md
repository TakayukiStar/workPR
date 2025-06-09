# Docker 超入門: 非エンジニア向け最速学習ガイド

このガイドは、全くの非エンジニアでも Docker を『最速』で使い始められるように作成した学習教材です。実際に手を動かしながら、コンテナ技術の基礎から実践的な開発環境の構築まで学んでいきましょう。

## 目次

1. [Docker とは？](#1-dockerとは)
2. [Docker のインストール](#2-dockerのインストール)
3. [Docker の基本概念](#3-dockerの基本概念)
4. [基本的なコマンド](#4-基本的なコマンド)
5. [Dockerfile の作成](#5-dockerfileの作成)
6. [Docker イメージのビルドと実行](#6-dockerイメージのビルドと実行)
7. [Docker Hub の活用](#7-docker-hubの活用)
8. [Docker Compose の利用](#8-docker-composeの利用)
9. [複数コンテナの連携](#9-複数コンテナの連携)
10. [ボリュームとデータ永続化](#10-ボリュームとデータ永続化)
11. [ネットワーク設定](#11-ネットワーク設定)
12. [Makefile による自動化](#12-makefileによる自動化)
13. [開発環境の構築例](#13-開発環境の構築例)
14. [本番環境へのデプロイ](#14-本番環境へのデプロイ)
15. [Docker のベストプラクティス](#15-dockerのベストプラクティス)
16. [よくある質問と回答](#16-よくある質問と回答)
17. [次のステップ](#17-次のステップ)

---

## 1. Docker とは？

Docker はアプリケーションとその依存関係をコンテナとして一緒にパッケージ化するプラットフォームです。

### Docker の特徴

- **環境の一貫性**: どこでも同じ環境で実行できる（「私の環境では動くのに…」問題の解決）
- **軽量**: 仮想マシンより軽量で起動が速い
- **移植性**: 異なるシステム間で簡単に移動・展開できる
- **スケーラビリティ**: アプリケーションの拡張が容易

### なぜ Docker を学ぶべきか

- 開発環境のセットアップが簡単になる
- チーム全体で同じ環境を使える
- 本番環境と開発環境の差異をなくせる
- クラウドや様々なサーバー環境への展開が容易
- マイクロサービスアーキテクチャの構築に最適

---

## 2. Docker のインストール

### Windows への Docker インストール

1. [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop) をダウンロード
2. インストーラを実行して指示に従う
3. WSL 2 (Windows Subsystem for Linux) の有効化が求められたら指示に従う
4. インストール完了後、Docker Desktop を起動

### Mac への Docker インストール

1. [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop) をダウンロード
2. ダウンロードした .dmg ファイルを開き、Docker アプリケーションを Applications フォルダにドラッグ
3. Docker を起動

### Linux への Docker インストール

Ubuntu の場合:

```bash
# 必要なパッケージのインストール
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Docker の公式 GPG キーの追加
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Docker のリポジトリを追加
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Docker エンジンのインストール
sudo apt update
sudo apt install docker-ce

# Docker サービスの開始と自動起動の設定
sudo systemctl start docker
sudo systemctl enable docker

# 現在のユーザーを docker グループに追加（sudo なしで Docker を使えるようにする）
sudo usermod -aG docker ${USER}
```

### インストールの確認

ターミナルやコマンドプロンプトで以下のコマンドを実行して、Docker が正常にインストールされたか確認します。

```bash
docker --version
docker run hello-world
```

> 💡 **初心者向けヒント**：
> Docker Desktop には GUI も付属しており、コマンドラインが苦手な方でも操作できます。

---

## 3. Docker の基本概念

Docker を理解するための重要な概念を押さえましょう。

### コンテナ

軽量で独立した実行環境。アプリケーションとその依存関係を一緒にパッケージ化します。

### イメージ

コンテナの不変のテンプレート。アプリケーションのコードや依存関係、ツール、ライブラリなど、必要なものすべてを含みます。

### Dockerfile

イメージを作成するための指示書。どのベースイメージを使用し、どのコマンドを実行し、どのファイルをコピーするかなどを定義します。

### レジストリ

Docker イメージを保存・共有するためのリポジトリ。Docker Hub は公式のレジストリです。

### Docker Compose

複数のコンテナを定義・実行するためのツール。YAML ファイルで設定を管理します。

### ボリューム

コンテナのデータを永続化するための仕組み。コンテナが削除されてもデータは保持されます。

> 💡 **初心者向けヒント**：
> コンテナは「使い捨て」を前提とし、状態を持たないことが理想です。永続化が必要なデータはボリュームに保存します。

---

## 4. 基本的なコマンド

Docker を使い始めるための基本的なコマンドを紹介します。

### イメージ関連のコマンド

```bash
# イメージの一覧表示
docker images

# イメージのダウンロード
docker pull [イメージ名]:[タグ]
docker pull nginx:latest

# イメージのビルド
docker build -t [イメージ名]:[タグ] [Dockerfileのパス]
docker build -t myapp:1.0 .

# イメージの削除
docker rmi [イメージID or イメージ名]:[タグ]
```

### コンテナ関連のコマンド

```bash
# コンテナの作成と起動
docker run [オプション] [イメージ名]:[タグ]
docker run -d -p 8080:80 --name mywebserver nginx:latest

# 実行中のコンテナ一覧表示
docker ps

# すべてのコンテナ一覧表示（停止中も含む）
docker ps -a

# コンテナの停止
docker stop [コンテナID or コンテナ名]

# コンテナの再開
docker start [コンテナID or コンテナ名]

# コンテナの削除
docker rm [コンテナID or コンテナ名]

# コンテナ内でコマンド実行
docker exec -it [コンテナID or コンテナ名] [コマンド]
docker exec -it mywebserver bash
```

### docker run の主なオプション

```bash
-d, --detach                # バックグラウンドで実行
-p, --publish HOST:CONTAINER # ポートマッピング
--name                      # コンテナに名前を付ける
-v, --volume HOST:CONTAINER # ボリュームマウント
-e, --env                   # 環境変数の設定
--rm                        # 終了時にコンテナを自動削除
-it                         # インタラクティブモード（ターミナル接続）
--network                   # 使用するネットワーク
```

### システム管理コマンド

```bash
# Docker システム情報の表示
docker info

# 未使用のリソース（コンテナ、イメージ、ネットワーク、ボリューム）を削除
docker system prune

# 使用状況の確認
docker system df
```

> 💡 **初心者向けヒント**：
> `docker run` は新しいコンテナを作成して起動しますが、`docker start` は既存のコンテナを起動します。目的に応じて使い分けましょう。

---

## 5. Dockerfile の作成

Dockerfile は Docker イメージを作成するための設計図です。基本的な構文を学びましょう。

### 基本的な Dockerfile の例

```dockerfile
# ベースイメージの指定
FROM node:14

# 作業ディレクトリの設定
WORKDIR /app

# ファイルのコピー
COPY package*.json ./

# コマンドの実行
RUN npm install

# ソースコードのコピー
COPY . .

# 環境変数の設定
ENV PORT=3000

# 公開するポートの指定
EXPOSE 3000

# コンテナ起動時に実行するコマンド
CMD ["npm", "start"]
```

### 主な Dockerfile 命令

```dockerfile
# FROM: ベースイメージの指定
FROM ubuntu:20.04

# WORKDIR: 作業ディレクトリの設定
WORKDIR /app

# COPY: ホストからのファイルコピー
COPY . /app/

# ADD: ファイルコピー（URL やアーカイブからも可能）
ADD https://example.com/file.tar.gz /app/

# RUN: イメージビルド時に実行するコマンド
RUN apt-get update && apt-get install -y nodejs

# ENV: 環境変数の設定
ENV NODE_ENV=production

# ARG: ビルド時の変数（ENV とは異なり、コンテナ実行時には使えない）
ARG VERSION=1.0

# EXPOSE: 公開するポート
EXPOSE 80

# VOLUME: ボリュームのマウントポイント
VOLUME /data

# USER: コマンド実行ユーザーの指定
USER node

# ENTRYPOINT: コンテナ起動時に必ず実行されるコマンド
ENTRYPOINT ["node", "app.js"]

# CMD: デフォルトのコマンド（ENTRYPOINT の引数としても使える）
CMD ["--help"]
```

### マルチステージビルドの例

コンパイルが必要な言語などで、最終イメージを小さくするための方法です。

```dockerfile
# ビルドステージ
FROM golang:1.16 AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp

# 実行ステージ
FROM alpine:3.14
WORKDIR /app
COPY --from=builder /app/myapp .
CMD ["./myapp"]
```

> 💡 **初心者向けヒント**：
> Dockerfile の各行は「レイヤー」と呼ばれ、キャッシュされます。変更が少ない処理を先に、頻繁に変更されるファイルのコピーを後に書くとビルドが速くなります。

---

## 6. Docker イメージのビルドと実行

Dockerfile からイメージをビルドし、コンテナとして実行する方法を学びましょう。

### イメージのビルド

```bash
# 基本的なビルド
docker build -t myapp:latest .

# タグの指定
docker build -t myapp:1.0 -t myapp:latest .

# ビルド引数の指定
docker build --build-arg VERSION=2.0 -t myapp:2.0 .

# キャッシュを使わずにビルド
docker build --no-cache -t myapp:latest .
```

### コンテナの実行

```bash
# 基本的な実行
docker run myapp:latest

# ポートマッピング
docker run -p 8080:3000 myapp:latest

# 環境変数の設定
docker run -e NODE_ENV=development myapp:latest

# バックグラウンドで実行
docker run -d myapp:latest

# コンテナに名前を付ける
docker run --name my-container myapp:latest

# ボリュームのマウント
docker run -v /host/path:/container/path myapp:latest

# 組み合わせ例
docker run -d --name my-webapp -p 8080:3000 -e NODE_ENV=production -v /logs:/app/logs myapp:latest
```

### コンテナのライフサイクル管理

```bash
# コンテナの停止
docker stop my-container

# コンテナの再開
docker start my-container

# コンテナのログ確認
docker logs my-container

# コンテナ内でコマンドを実行
docker exec -it my-container bash
```

> 💡 **初心者向けヒント**：
> `-p` オプションの書式は `ホストポート:コンテナポート` です。例えば `-p 8080:80` は、ホストの 8080 ポートへのアクセスをコンテナの 80 ポートに転送します。

---

## 7. Docker Hub の活用

Docker Hub は Docker の公式イメージレジストリで、多くの公式イメージや他のユーザーのイメージを利用できます。

### Docker Hub からのイメージ検索とダウンロード

```bash
# イメージの検索
docker search nginx

# イメージのダウンロード
docker pull nginx:latest

# 特定のバージョンを指定
docker pull mysql:8.0
```

### イメージのタグ付けとアップロード

```bash
# Docker Hub にログイン
docker login

# イメージにタグを付ける
docker tag myapp:latest username/myapp:latest

# イメージのアップロード
docker push username/myapp:latest

# Docker Hub からログアウト
docker logout
```

### プライベートレジストリの利用

```bash
# プライベートレジストリへのログイン
docker login registry.example.com

# プライベートレジストリ用のタグ付け
docker tag myapp:latest registry.example.com/myapp:latest

# プライベートレジストリへのプッシュ
docker push registry.example.com/myapp:latest
```

> 💡 **初心者向けヒント**：
> Docker Hub の公式イメージは信頼性が高く、セキュリティも考慮されています。未知のユーザーのイメージを使用する際は注意しましょう。

---

## 8. Docker Compose の利用

Docker Compose は複数のコンテナを定義し、一度に実行するためのツールです。

### docker-compose.yml の基本構造

```yaml
version: "3"

services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    depends_on:
      - app

  app:
    build: ./app
    environment:
      - DB_HOST=db
      - DB_PASSWORD=example
    depends_on:
      - db

  db:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=example
      - MYSQL_DATABASE=myapp
    volumes:
      - db-data:/var/lib/mysql

volumes:
  db-data:
```

### Docker Compose の基本コマンド

```bash
# 定義されたサービスの起動
docker-compose up

# バックグラウンドで起動
docker-compose up -d

# サービスの停止
docker-compose down

# サービスの停止とボリューム削除
docker-compose down -v

# 特定のサービスだけを起動
docker-compose up -d web

# サービスのログを表示
docker-compose logs app

# サービス内でコマンドを実行
docker-compose exec app bash

# サービスの構成を確認
docker-compose config
```

### docker-compose.yml の詳細オプション

```yaml
version: "3.8"

services:
  web:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev
      args:
        - NODE_ENV=development
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - API_URL=http://api:4000
    depends_on:
      - api
    restart: unless-stopped
    networks:
      - frontend-network
      - backend-network

  api:
    build: ./backend
    ports:
      - "4000:4000"
    environment:
      - DB_HOST=db
      - DB_USER=root
      - DB_PASSWORD_FILE=/run/secrets/db_password
    depends_on:
      - db
    secrets:
      - db_password
    networks:
      - backend-network

  db:
    image: postgres:13
    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password
      - POSTGRES_DB=myapp
    secrets:
      - db_password
    networks:
      - backend-network

networks:
  frontend-network:
  backend-network:

volumes:
  db-data:

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

> 💡 **初心者向けヒント**：
> Docker Compose は開発環境のセットアップを劇的に簡単にします。一つのファイルでプロジェクトの全依存関係を定義できます。

---

## 9. 複数コンテナの連携

実際のアプリケーションは複数のサービスで構成されることが多いです。Docker でこれらを連携させる方法を学びましょう。

### Web アプリケーションの構成例

以下は典型的な Web アプリケーションの Docker Compose 設定です：

```yaml
version: "3"

services:
  # Nginx - Web サーバー
  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./nginx/conf:/etc/nginx/conf.d
      - ./static:/usr/share/nginx/html
    depends_on:
      - app
    restart: always

  # バックエンドアプリケーション
  app:
    build: ./app
    expose:
      - "5000"
    environment:
      - DATABASE_URL=postgres://user:password@db:5432/mydb
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
    restart: always

  # データベース
  db:
    image: postgres:13
    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    restart: always

  # キャッシュ
  redis:
    image: redis:alpine
    volumes:
      - redis-data:/data
    restart: always

volumes:
  db-data:
  redis-data:
```

### サービス間通信の仕組み

Docker Compose では、サービス名がホスト名として機能します。例えば、`app` サービスから `db` サービスへは、単に `db` というホスト名で接続できます。

```python
# Python でのデータベース接続例
import psycopg2

conn = psycopg2.connect(
    host="db",        # サービス名をホスト名として使用
    database="mydb",
    user="user",
    password="password"
)
```

### ネットワークの分離

複雑なアプリケーションでは、ネットワークを分離することでセキュリティを高められます。

```yaml
version: "3"

services:
  frontend:
    # ... 設定 ...
    networks:
      - frontend-network

  backend:
    # ... 設定 ...
    networks:
      - frontend-network
      - backend-network

  db:
    # ... 設定 ...
    networks:
      - backend-network

networks:
  frontend-network:
  backend-network:
```

> 💡 **初心者向けヒント**：
> `depends_on` は起動順序の制御だけで、サービスの準備完了を保証するものではありません。重要なサービスの準備が整うまで待機するロジックをアプリケーション側で実装することを検討しましょう。

---

## 10. ボリュームとデータ永続化

コンテナは一時的なものですが、データを永続化する方法があります。

### ボリュームの種類

1. **名前付きボリューム**: Docker が管理するボリューム
2. **バインドマウント**: ホストシステムの特定のパスをマウント
3. **tmpfs マウント**: メモリ上の一時的なファイルシステム

### ボリュームの作成と使用

```bash
# 名前付きボリュームの作成
docker volume create my-volume

# ボリュームの一覧表示
docker volume ls

# ボリュームの詳細表示
docker volume inspect my-volume

# ボリュームの削除
docker volume rm my-volume

# 未使用ボリュームの削除
docker volume prune
```

### Docker Compose でのボリューム定義

```yaml
version: "3"

services:
  db:
    image: postgres:13
    volumes:
      - db-data:/var/lib/postgresql/data # 名前付きボリューム
      - ./init-scripts:/docker-entrypoint-initdb.d # バインドマウント
    environment:
      - POSTGRES_PASSWORD=example

  web:
    image: nginx
    volumes:
      - ./html:/usr/share/nginx/html:ro # 読み取り専用マウント
      - nginx-logs:/var/log/nginx # ログ用ボリューム

volumes:
  db-data: # Docker が管理する名前付きボリューム
  nginx-logs:
```

### データ永続化のベストプラクティス

1. データベースデータは名前付きボリュームを使用する
2. 設定ファイルはバインドマウントで管理する
3. 読み取り専用データは `:ro` オプションを付ける
4. 一時的なデータには tmpfs を使用する
5. バックアップ戦略を検討する

```bash
# ボリュームのバックアップ例
docker run --rm -v my-volume:/data -v $(pwd):/backup alpine tar czf /backup/my-volume-backup.tar.gz /data

# ボリュームの復元例
docker run --rm -v my-volume:/data -v $(pwd):/backup alpine sh -c "cd /data && tar xzf /backup/my-volume-backup.tar.gz --strip 1"
```

> 💡 **初心者向けヒント**：
> データが重要な場合は、コンテナ内だけでなく、定期的なバックアップを別の場所に保存することを忘れないでください。

---

## 11. ネットワーク設定

Docker コンテナ間のネットワーク通信について学びましょう。

### Docker ネットワークの種類

1. **bridge**: デフォルトのネットワーク。同じホスト上のコンテナ間通信用
2. **host**: ホストのネットワークをコンテナで直接使用
3. **none**: ネットワーク接続なし
4. **overlay**: 複数の Docker デーモン間のコンテナ通信用（Swarm モードで使用）
5. **macvlan**: コンテナに物理ネットワークへの直接アクセスを提供

### ネットワークの管理

```bash
# ネットワークの一覧表示
docker network ls

# ネットワークの作成
docker network create my-network

# ネットワークの詳細表示
docker network inspect my-network

# コンテナをネットワークに接続
docker network connect my-network my-container

# コンテナをネットワークから切断
docker network disconnect my-network my-container

# ネットワークの削除
docker network rm my-network

# 未使用ネットワークの削除
docker network prune
```

### Docker Compose でのネットワーク設定

```yaml
version: "3"

networks:
  frontend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/24
  backend:
    driver: bridge
    internal: true # 外部接続不可のネットワーク

services:
  web:
    image: nginx
    networks:
      - frontend
    ports:
      - "80:80"

  api:
    image: myapi
    networks:
      - frontend
      - backend

  db:
    image: postgres
    networks:
      - backend
```

### ポートマッピングと公開

```yaml
services:
  web:
    image: nginx
    ports:
      - "8080:80" # ホストの8080ポートをコンテナの80ポートにマッピング
      - "443:443" # 複数ポートの公開

  api:
    image: myapi
    expose:
      - "5000" # コンテナ間通信用にポートを公開（ホストからはアクセス不可）
```

> 💡 **初心者向けヒント**：
> セキュリティのため、公開する必要のないサービス（データベースなど）は `internal: true` のネットワークに配置し、外部からのアクセスを防ぐことをおすすめします。

---

## 12. Makefile による自動化

Docker コマンドは長くなりがちで、毎回入力するのは大変です。Makefile を使えば、複雑なコマンドを短いコマンドで実行できます。

### Makefile とは

Makefile は、コマンドをショートカット化するためのツールです。特に長い Docker コマンドを簡単に実行できるようになります。

### Makefile の基本構造

```makefile
# 基本的なMakefileの構造
target: dependencies
	command
```

### Docker 用の Makefile の例

以下は典型的な Docker 開発用の Makefile です：

```makefile
# Docker操作を簡単にするMakefile

# 変数定義
IMAGE_NAME = myapp
CONTAINER_NAME = myapp-container
PORT = 8080:80

# イメージのビルド
build:
	docker build -t $(IMAGE_NAME) .

# コンテナの起動
up:
	docker run -d -p $(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

# コンテナの停止と削除
down:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

# コンテナ内でシェルを起動
shell:
	docker exec -it $(CONTAINER_NAME) bash

# コンテナのログを表示
logs:
	docker logs -f $(CONTAINER_NAME)

# 全てのリソースをクリーンアップ
clean: down
	docker rmi $(IMAGE_NAME) || true

# 開発環境の完全リセット（全てのコンテナ、イメージ、ボリュームを削除）
clean-all:
	docker system prune -af --volumes

# ヘルプメッセージの表示
help:
	@echo "使用可能なコマンド:"
	@echo "  make build      - イメージをビルドする"
	@echo "  make up         - コンテナを起動する"
	@echo "  make down       - コンテナを停止して削除する"
	@echo "  make shell      - コンテナ内でシェルを起動する"
	@echo "  make logs       - コンテナのログを表示する"
	@echo "  make clean      - コンテナとイメージを削除する"
	@echo "  make clean-all  - 全てのDockerリソースを削除する"
```

### Makefile の使い方

1. 上記の Makefile をプロジェクトのルートディレクトリに保存します
2. ターミナルで以下のように実行します:

```bash
# イメージのビルド
make build

# コンテナの起動
make up

# コンテナ内でシェルを起動
make shell

# コンテナのログを表示
make logs

# コンテナの停止と削除
make down

# 使用可能なコマンドの一覧表示
make help
```

> 💡 **初心者向けヒント**：
> Makefile は必ずタブインデントを使用します（スペースでは NG）。エディタによっては自動的にスペースに変換するので注意しましょう。

---

## 13. 開発環境の構築例

実際のプロジェクトで Docker を使った開発環境を構築する例を見ていきましょう。

### Web アプリケーション開発環境の例

#### プロジェクト構成

```
my-webapp/
├── docker-compose.yml
├── Makefile
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
└── nginx/
    ├── Dockerfile
    └── nginx.conf
```

#### backend/Dockerfile (Python/Flask)

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
```

#### frontend/Dockerfile (Node.js/React)

```dockerfile
FROM node:16-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### nginx/Dockerfile

```dockerfile
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
```

#### nginx/nginx.conf

```nginx
server {
    listen 80;

    location /api {
        proxy_pass http://backend:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location / {
        proxy_pass http://frontend:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### docker-compose.yml

```yaml
version: "3.8"

services:
  backend:
    build: ./backend
    volumes:
      - ./backend:/app
    environment:
      - FLASK_APP=app.py
      - FLASK_ENV=development
    networks:
      - app-network
    depends_on:
      - db

  frontend:
    build: ./frontend
    volumes:
      - ./frontend:/app
      - /app/node_modules
    networks:
      - app-network

  nginx:
    build: ./nginx
    ports:
      - "8080:80"
    networks:
      - app-network
    depends_on:
      - backend
      - frontend

  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=password
      - POSTGRES_USER=user
      - POSTGRES_DB=appdb
    networks:
      - app-network

networks:
  app-network:
    driver: bridge

volumes:
  postgres_data:
```

#### Makefile

```makefile
dev:
	docker-compose up

build:
	docker-compose build

down:
	docker-compose down

clean:
	docker-compose down -v --rmi all

logs:
	docker-compose logs -f

backend-shell:
	docker-compose exec backend bash

db-shell:
	docker-compose exec db psql -U user -d appdb
```

### 使い方

上記の開発環境は以下のコマンドで操作できます:

```bash
# 開発環境を起動
make dev

# バックエンドのシェルにアクセス
make backend-shell

# データベースのシェルにアクセス
make db-shell

# ログの表示
make logs

# 開発環境の停止
make down

# 完全クリーンアップ
make clean
```

開発環境が起動したら、ブラウザで `http://localhost:8080` にアクセスすると、アプリケーションが表示されます。

> 💡 **初心者向けヒント**：
> 実際の開発では、ローカルのファイルをコンテナ内にマウントすることで、コードの変更がリアルタイムで反映されるようにしています。これにより、コンテナを再起動せずに開発が可能になります。

---

## 14. 本番環境へのデプロイ

開発が完了したら、本番環境にアプリケーションをデプロイする方法を学びましょう。

### 本番用 Dockerfile の最適化

本番環境用の Dockerfile は、開発用と異なる点がいくつかあります:

1. マルチステージビルドを使用してイメージサイズを小さくする
2. セキュリティ向上のため、非 root ユーザーで実行する
3. 本番用の設定を適用する

#### 本番用バックエンド Dockerfile の例

```dockerfile
# ビルドステージ
FROM python:3.10-slim AS builder

WORKDIR /app

# 依存関係のインストール
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# 実行ステージ
FROM python:3.10-slim

# セキュリティのため非rootユーザーを作成
RUN useradd -m appuser

WORKDIR /app

# ビルドステージから依存関係をコピー
COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*

# アプリケーションのコピー
COPY . .

# 所有者を非rootユーザーに変更
RUN chown -R appuser:appuser /app
USER appuser

# 環境変数の設定
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

# アプリケーションの実行
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

### デプロイ戦略

#### 1. クラウドプロバイダーのコンテナサービスを利用

- **AWS**: ECS (Elastic Container Service) または Fargate
- **Google Cloud**: GKE (Google Kubernetes Engine)
- **Azure**: AKS (Azure Kubernetes Service)
- **Heroku**: Container Registry & Runtime

#### 2. Kubernetes (k8s) を利用

大規模なアプリケーションでは、Kubernetes を使用してコンテナのオーケストレーションを行うことが一般的です。

基本的な Kubernetes のマニフェストファイル例:

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp
          image: myregistry/myapp:1.0
          ports:
            - containerPort: 8080
          env:
            - name: DB_HOST
              value: "db-service"
          resources:
            limits:
              cpu: "500m"
              memory: "500Mi"
            requests:
              cpu: "200m"
              memory: "200Mi"
---
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080
  type: LoadBalancer
```

#### 3. CI/CD パイプラインの構築

GitHub Actions や Jenkins などの CI/CD ツールを使って、自動デプロイパイプラインを構築することも重要です。

GitHub Actions の例:

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Login to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_HUB_USERNAME }}
          password: ${{ secrets.DOCKER_HUB_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v2
        with:
          context: .
          push: true
          tags: myregistry/myapp:latest,myregistry/myapp:${{ github.sha }}

      - name: Deploy to Kubernetes
        uses: steebchen/kubectl@v2
        with:
          config: ${{ secrets.KUBE_CONFIG_DATA }}
          command: set image deployment/myapp myapp=myregistry/myapp:${{ github.sha }}
```

### デプロイ後のモニタリング

本番環境では、コンテナのモニタリングも重要です:

- **Prometheus**: メトリクス収集
- **Grafana**: ダッシュボードとアラート
- **ELK Stack**: ログ管理 (Elasticsearch, Logstash, Kibana)

> 💡 **初心者向けヒント**：
> 最初は単純なデプロイから始めて、徐々に複雑な構成に移行するのがおすすめです。例えば、最初は Docker のみで、次に Docker Compose を使い、その後 Kubernetes を導入するというステップで進めるとよいでしょう。

---

## 15. Docker のベストプラクティス

Docker を効果的に使うためのベストプラクティスを紹介します。

### イメージに関するベストプラクティス

- **軽量なベースイメージを使用する**: Alpine Linux ベースのイメージや Slim バージョンを使う
- **マルチステージビルドを活用する**: ビルド環境と実行環境を分離し、イメージサイズを小さくする
- **レイヤーを最小限に抑える**: RUN, COPY, ADD コマンドは少なくする
- **キャッシュを効率的に使う**: 変更頻度の低いレイヤーを先に配置する
- **適切なタグを使用する**: `latest`タグだけでなく、明示的なバージョンタグも使う

### セキュリティに関するベストプラクティス

- **非 root ユーザーで実行する**: Dockerfile で専用ユーザーを作成して使う
- **機密情報をイメージに含めない**: 環境変数や Docker シークレットを使用する
- **イメージをスキャンする**: Clair, Trivy, Docker のセキュリティスキャンなどを使う
- **最小限の特権で実行する**: `--cap-drop=ALL`などで不要な機能を無効化する
- **イメージを定期的に更新する**: セキュリティパッチが適用された最新イメージを使う

### パフォーマンスに関するベストプラクティス

- **適切なリソース制限を設定する**: CPU, メモリの制限を指定する
- **ヘルスチェックを実装する**: `HEALTHCHECK`命令を使用する
- **効率的なキャッシュ戦略を採用する**: ボリュームやコンテナ間でキャッシュを共有する
- **不要なファイルをコピーしない**: `.dockerignore`ファイルを活用する

### Docker Compose のベストプラクティス

- **環境変数を`.env`ファイルで管理する**: 機密情報はリポジトリに含めない
- **サービス間の依存関係を明示する**: `depends_on`を使用する
- **各サービスに適切なヘルスチェックを設定する**: 依存関係のあるサービスが正常に起動するのを待つ
- **ネットワークを明示的に定義する**: サービス間の通信を制御する

### 開発ワークフローのベストプラクティス

- **開発環境と本番環境で同じ Dockerfile を使用する**: 環境差異を減らす
- **ボリュームを使ってコードの変更をリアルタイムに反映させる**: 開発効率を向上させる
- **自動テストを Docker で実行する**: CI パイプラインに組み込む
- **バージョン管理を徹底する**: Docker イメージのバージョニングを適切に行う

### ベストプラクティスの例: Web アプリケーション用の Dockerfile

```dockerfile
# ビルドステージ
FROM node:16-alpine AS builder

WORKDIR /app

# 依存関係のインストール (キャッシュを活用)
COPY package*.json ./
RUN npm ci

# ソースのコピーとビルド
COPY . .
RUN npm run build

# 実行ステージ
FROM nginx:alpine

# 非rootユーザーの作成
RUN adduser -D -u 1000 appuser

# ビルド成果物のコピー
COPY --from=builder /app/build /usr/share/nginx/html

# Nginxの設定
COPY nginx.conf /etc/nginx/conf.d/default.conf

# ヘルスチェックの追加
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -q --spider http://localhost/ || exit 1

# 権限の変更
RUN chown -R appuser:appuser /usr/share/nginx/html && \
    chown -R appuser:appuser /var/cache/nginx && \
    chown -R appuser:appuser /var/log/nginx && \
    touch /var/run/nginx.pid && \
    chown -R appuser:appuser /var/run/nginx.pid

# 非rootユーザーに切り替え
USER appuser

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

> 💡 **初心者向けヒント**：
> 最初からすべてのベストプラクティスを適用する必要はありません。徐々に学んで取り入れていきましょう。最も重要なのは、セキュリティに関するベストプラクティスです。

---

## 16. よくある質問と回答

初心者がよく疑問に思うことへの回答をまとめました。

### Q: Docker、Docker Compose、Kubernetes の違いは何ですか？

**A**:

- **Docker**: 単一のコンテナを管理するためのツール
- **Docker Compose**: 複数のコンテナを管理するためのツール（小〜中規模のアプリケーション向け）
- **Kubernetes**: 大規模なコンテナのオーケストレーションを行うツール（大規模アプリケーション向け）

### Q: コンテナ内のデータが消えてしまうのはなぜですか？

**A**: コンテナは「ステートレス」（状態を持たない）設計が基本です。コンテナが削除されると、中のデータも消えます。データを永続化するには、ボリュームを使いましょう。

### Q: Dockerfile と Docker Compose ファイルの違いは何ですか？

**A**:

- **Dockerfile**: 単一のコンテナイメージを作るための設計図
- **Docker Compose**: 複数のコンテナの設定や関係性を定義するファイル

### Q: `docker-compose up`と`docker-compose up -d`の違いは何ですか？

**A**: `-d`はデタッチドモード（バックグラウンド実行）を意味します。`docker-compose up`だけだとターミナルを占有し、Ctrl+C で停止します。`-d`を付けるとバックグラウンドで実行され、ターミナルを使い続けられます。

### Q: コンテナ内でファイルを編集できますか？

**A**: できますが、推奨されません。コンテナ内での変更は、コンテナを再起動すると失われます。代わりにボリュームを使ってホストマシンとファイルを共有し、ホスト側で編集するのがベストプラクティスです。

### Q: Docker Hub の無料アカウントの制限は？

**A**: 無料アカウントでは、公開リポジトリは無制限に作れますが、プライベートリポジトリは制限があります。また、ダウンロード回数にも制限があります。

### Q: データベースもコンテナ化すべきですか？

**A**: 開発環境ではデータベースもコンテナ化すると便利ですが、本番環境では専用のデータベースサービス（RDS、Cloud SQL 等）を使うことが一般的です。

### Q: Docker の GUI ツールはありますか？

**A**: はい、Docker Desktop に加え、Portainer、Kinematic、Rancher Desktop など様々な GUI ツールがあります。

### Q: コンテナのログはどうやって見ますか？

**A**: `docker logs [コンテナID/名前]`または`docker-compose logs [サービス名]`でログを確認できます。`-f`オプションを付けると、リアルタイムでログを追跡できます。

### Q: コンテナの起動が遅いのですが？

**A**: イメージのサイズを小さくする、不要なサービスを削除する、マルチステージビルドを使うなどで改善できます。

### Q: 本番環境で Docker を使うべきですか？

**A**: 適切に設計・管理されていれば、本番環境でも Docker は効果的です。ただし、運用ノウハウが必要なので、小規模なら専用の PaaS サービスから始めるのも良い選択です。

---

## 17. 次のステップ

この入門ガイドを読み終えたら、次のステップに進みましょう。

### さらに学ぶべきトピック

1. **Kubernetes**: 大規模なコンテナオーケストレーション
2. **Docker Swarm**: Docker ネイティブのクラスタリング
3. **CI/CD**: Jenkins や GitHub Actions との統合
4. **マイクロサービスアーキテクチャ**: コンテナを使った分散システム設計
5. **サーバーレスコンテナ**: AWS Fargate や Cloud Run など

### 実践的な次のステップ

1. **小さなプロジェクトを作る**: 自分のアプリを Docker で動かしてみる
2. **既存のプロジェクトをコンテナ化**: 現在のプロジェクトを Docker に移行する
3. **開発環境を完全に Docker で構築**: 開発作業を Docker コンテナで行う
4. **本番環境にデプロイ**: 小規模なサービスを本番環境にデプロイしてみる
5. **チームに Docker を導入**: 同僚と開発環境を共有する

### 有用なリソース

#### ドキュメント

- [Docker 公式ドキュメント](https://docs.docker.com/)
- [Docker Compose 公式ドキュメント](https://docs.docker.com/compose/)
- [Docker Hub](https://hub.docker.com/)

#### 書籍

- 『Docker: Up & Running』by Karl Matthias & Sean P. Kane
- 『入門 Docker』by 古賀政純
- 『Docker 実践ガイド』by 高橋宣成

#### オンラインコース

- Udemy の『Docker & Kubernetes: The Practical Guide』
- Pluralsight の『Docker and Containers: The Big Picture』
- Coursera の『Introduction to Containers, Kubernetes and OpenShift』

#### コミュニティ

- Docker 公式フォーラム
- Stack Overflow
- Docker Meetups

### 実践プロジェクト例

1. **個人ブログ**: WordPress + MySQL を Docker で構築
2. **ToDo アプリ**: フロントエンド + バックエンド + DB の構成
3. **開発環境**: 普段使う開発ツールをすべて Docker で用意
4. **CI パイプライン**: GitHub Actions + Docker でテスト/デプロイを自動化
5. **マイクロサービス**: 複数の小さなサービスを Docker Compose で連携

---

## まとめ

この「Docker 超入門」では、非エンジニアでも Docker を使いこなせるよう、基本から実践的なトピックまで幅広く解説しました。

Docker を使うと、「環境構築の手間」「動かない問題」「本番環境との差異」といった多くの問題を解決できます。最初は難しく感じるかもしれませんが、少しずつ実践しながら学べば、開発作業が格段に効率化されるでしょう。

このガイドが皆さんの Docker 学習の一助となれば幸いです。分からないことがあれば、Docker コミュニティは親切でサポートが充実しています。ぜひ質問してみてください。

Happy Dockering! 🐳
