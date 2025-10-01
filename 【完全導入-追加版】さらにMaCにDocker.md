# Mac初心者のためのDocker完全ガイド【Git/GitHub完了後】

## 🎯 このガイドについて

**前提条件:**
- ✅ Git/GitHubの導入が完了している
- ✅ VSCodeがインストールされている
- ✅ ターミナルの基本操作ができる
- ✅ MacでGitHubにプッシュ・プルができる

このガイド**だけ**で、MacでのDockerの導入がすべて完了します。
他の資料を見る必要は一切ありません。

**完了後にできること:**
- ✅ Dockerコンテナを作成・実行
- ✅ Dockerイメージをビルド
- ✅ Docker Composeで複数コンテナを管理
- ✅ 開発環境を簡単に構築
- ✅ チームで同じ環境を共有

---

## 📋 目次
1. [Dockerとは](#dockerとは)
2. [事前準備と確認](#事前準備と確認)
3. [Docker Desktopのインストール](#docker-desktopのインストール)
4. [Dockerの基本操作](#dockerの基本操作)
5. [Dockerfileの作成](#dockerfileの作成)
6. [Docker Composeの使い方](#docker-composeの使い方)
7. [実践：Python開発環境を構築](#実践python開発環境を構築)
8. [VSCodeとDockerの連携](#vscodeとdockerの連携)
9. [トラブルシューティング](#トラブルシューティング)
10. [よくある質問（FAQ）](#よくある質問faq)

---

## 🐳 Dockerとは

### Dockerの概要

**Docker（ドッカー）** は、アプリケーションを「コンテナ」という単位で実行するプラットフォームです。

**簡単に言うと:**
- 「どこでも同じように動く箱」を作る技術
- 開発環境をパッケージ化して持ち運べる
- 「私のPCでは動くのに...」問題を解決

### なぜDockerが必要？

**従来の問題:**
```
開発者A: 「私のMacでは動きます」
開発者B: 「私のWindowsでは動きません...」
→ Pythonのバージョンが違う
→ ライブラリのバージョンが違う
→ OSの違いで動作が異なる
```

**Dockerを使うと:**
```
全員が同じDockerコンテナを使う
→ 全員同じ環境
→ 誰でも同じように動く
→ 環境構築が簡単
```

### Dockerの主要概念

#### 1. イメージ（Image）
- アプリケーションの設計図
- OSやライブラリを含んだテンプレート
- 例: `python:3.11`, `node:18`, `mysql:8.0`

#### 2. コンテナ（Container）
- イメージから作られた実行環境
- 隔離された独立した空間
- 複数のコンテナを同時に実行可能

#### 3. Dockerfile
- イメージを作るためのレシピ
- テキストファイルで記述
- コードとして管理できる

#### 4. Docker Compose
- 複数のコンテナを管理するツール
- YAMLファイルで設定
- ワンコマンドで環境構築

**イメージ:**
```
Dockerfile → イメージ → コンテナ
（レシピ）  （設計図）  （実行環境）
```

### Dockerを使う場面

**開発環境:**
- チーム全員が同じ環境で開発
- 新メンバーの環境構築が簡単

**テスト環境:**
- 本番環境と同じ環境でテスト
- 複数バージョンを並行テスト

**本番環境:**
- クラウドへのデプロイが簡単
- スケーリングが容易

**学習:**
- 様々な技術を気軽に試せる
- 環境を汚さない

---

## 🎯 事前準備と確認

### システム要件

**macOS:**
- macOS 11 Big Sur以降
- **Apple Silicon（M1/M2/M3）** または **Intel Mac**

**ハードウェア:**
- メモリ: 最低4GB、推奨8GB以上
- ストレージ: 最低10GB、推奨20GB以上の空き容量

**ソフトウェア:**
- ✅ Git/GitHubの設定完了
- ✅ VSCodeインストール済み
- ✅ ターミナルの基本操作ができる

### 自分のMacを確認

#### 1. macOSバージョンを確認

1. 画面左上の **🍎 アップルメニュー**
2. **「このMacについて」**
3. バージョンを確認

💡 **必要:** macOS 11 Big Sur以降

#### 2. チップを確認

同じ画面で:
- **「チップ」** → Apple M1/M2/M3など → **Apple Silicon**
- **「プロセッサ」** → Intel Core → **Intel Mac**

📝 **メモ:** この情報は後で使います

#### 3. メモリを確認

同じ画面で **「メモリ」** を確認
- 推奨: 8GB以上

#### 4. ストレージを確認

「ストレージ」タブで空き容量を確認
- 推奨: 20GB以上の空き

### 古いDockerがないか確認

以前にDockerをインストールしたことがある場合、確認します。

```bash
docker --version
```

**結果のパターン:**

**パターンA: Dockerがインストール済み**
```
Docker version 24.0.6, build ed223bc
```
→ バージョンが古い場合はアンインストールして再インストール推奨

**パターンB: Dockerがない**
```
zsh: command not found: docker
```
→ 問題なし、次のステップへ

**古いDockerをアンインストールする方法:**
1. アプリケーションフォルダから「Docker」を削除
2. ターミナルで以下を実行:
```bash
rm -rf ~/Library/Group\ Containers/group.com.docker
rm -rf ~/Library/Containers/com.docker.docker
rm -rf ~/.docker
```

---

## 🔧 Docker Desktopのインストール

### ステップ1: Docker Desktopをダウンロード

#### 1-1: 公式サイトにアクセス

https://www.docker.com/products/docker-desktop にアクセス

#### 1-2: 正しいバージョンを選択

**Apple Silicon Mac（M1/M2/M3）の場合:**
- **「Download for Mac - Apple Chip」** をクリック
- ファイル名: `Docker.dmg`（Apple Silicon用）

**Intel Macの場合:**
- **「Download for Mac - Intel Chip」** をクリック
- ファイル名: `Docker.dmg`（Intel用）

💡 **ポイント:** 間違ったバージョンをダウンロードすると動作しません！

**⚠️ どちらか分からない場合:**
1. 🍎 → 「このMacについて」で確認
2. 「チップ」または「プロセッサ」を見る

#### 1-3: ダウンロード完了

ダウンロードフォルダに `Docker.dmg` が保存されます。

### ステップ2: Docker Desktopをインストール

#### 2-1: DMGファイルを開く

1. **Finder** → **「ダウンロード」** フォルダ
2. **`Docker.dmg`** をダブルクリック
3. ウィンドウが開きます

#### 2-2: アプリケーションフォルダにドラッグ

1. **Docker（クジラ）アイコン** を
2. **Applications（アプリケーション）** フォルダに
3. **ドラッグ＆ドロップ**

コピーが始まります（1〜2分）

#### 2-3: DMGをアンマウント

1. Finderのサイドバーで「Docker」を右クリック
2. **「取り出す」** を選択

または、デスクトップの「Docker」アイコンをゴミ箱にドラッグ

### ステップ3: Docker Desktopを起動

#### 3-1: アプリケーションから起動

- **Launchpad** から「Docker」を検索してクリック
- または、**アプリケーション** フォルダから起動

#### 3-2: 初回起動の確認

**セキュリティ警告:**

**「"Docker"はインターネットからダウンロードされたアプリケーションです。開いてもよろしいですか？」**

→ **「開く」** をクリック

**⚠️ 「開発元を確認できないため開けません」と表示された場合:**

1. **「OK」** をクリック
2. **システム環境設定** → **「セキュリティとプライバシー」**
3. 下部に「"Docker"は開発元を確認できないため...」と表示
4. **「このまま開く」** をクリック
5. パスワードを入力
6. もう一度確認画面で **「開く」**

#### 3-3: 使用許諾契約

**「Docker Subscription Service Agreement」**

1. 内容を確認（スクロールして読む）
2. ☑ **「I accept the terms」** にチェック
3. **「Accept」** をクリック

💡 **個人利用・小規模チーム:** 無料で使えます

#### 3-4: 推奨設定の確認

**「Use recommended settings (Requires password)」**

推奨設定を使うか選択:
- ☑ **「Use recommended settings」** にチェック（推奨）
- **「Continue」** をクリック

#### 3-5: パスワード入力

Macのログインパスワードを入力
→ **「OK」** をクリック

💡 **なぜ必要？** Dockerは特権操作が必要なため

#### 3-6: 初期化

**「Starting Docker Desktop...」**

初期化が始まります（2〜5分）
- エンジンの起動
- 必要なファイルのダウンロード

⏳ **待機中:** MacBookの電源を入れたままにしてください

#### 3-7: サインイン画面（オプション）

**「Sign in to Docker」**

- **Docker Hubアカウントがある場合:** サインイン
- **ない場合:** **「Skip」** をクリック

💡 **初心者:** スキップしてOK（後で作成可能）

#### 3-8: チュートリアル

**「Quick Start Guide」**

簡単なチュートリアルが表示されます。
- 見たい場合: 進める
- スキップしたい場合: 画面を閉じる

### ステップ4: Docker Desktopの確認

#### 4-1: Docker Desktopが起動しているか確認

**メニューバー（画面上部）** に **クジラアイコン** 🐳 が表示されていればOK！

#### 4-2: ターミナルで確認

ターミナルを開いて以下を実行:

```bash
docker --version
```

**成功:**
```
Docker version 24.0.6, build ed223bc
```

バージョンが表示されればOK！

```bash
docker compose version
```

**成功:**
```
Docker Compose version v2.23.0
```

これも表示されればOK！

#### 4-3: Hello Worldを実行

Dockerが正しく動作するか確認:

```bash
docker run hello-world
```

**実行中:**
```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
...
Status: Downloaded newer image for hello-world:latest
```

**成功メッセージ:**
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

このメッセージが表示されたら **✅ インストール成功！**

### ステップ5: Docker Desktopの基本設定

#### 5-1: Docker Desktopを開く

メニューバーのクジラアイコンをクリック → **「Dashboard」**

#### 5-2: Settingsを開く

右上の **⚙️（歯車アイコン）** → **「Settings」**

#### 5-3: 推奨設定

**General（一般）:**
- ☑ **「Start Docker Desktop when you log in」** → 自動起動（推奨）
- ☑ **「Use Docker Compose V2」** → チェック

**Resources（リソース）:**

**CPUs:**
- スライダーを調整
- 推奨: 総CPU数の半分（例: 8コアなら4）

**Memory:**
- スライダーを調整
- 推奨: 
  - 8GB以下のMac → 2GB
  - 16GBのMac → 4GB
  - 32GB以上のMac → 8GB

**Disk image size:**
- デフォルトでOK（必要に応じて増やす）

**Advanced（詳細）:**
- デフォルトでOK

#### 5-4: 設定を保存

右下の **「Apply & Restart」** をクリック

Docker Desktopが再起動します（30秒〜1分）

### ✅ Docker Desktopインストール完了チェック

以下をすべて確認:
- [ ] Docker Desktopがインストールされている
- [ ] メニューバーにクジラアイコンが表示される
- [ ] `docker --version` でバージョンが表示される
- [ ] `docker compose version` でバージョンが表示される
- [ ] `docker run hello-world` が成功する

---

## 🚀 Dockerの基本操作

### Dockerの基本コマンド

#### コンテナ操作

```bash
# コンテナ一覧（実行中のみ）
docker ps

# コンテナ一覧（すべて）
docker ps -a

# コンテナを起動
docker start コンテナ名

# コンテナを停止
docker stop コンテナ名

# コンテナを削除
docker rm コンテナ名

# コンテナに入る
docker exec -it コンテナ名 bash
```

#### イメージ操作

```bash
# イメージ一覧
docker images

# イメージを取得
docker pull イメージ名

# イメージを削除
docker rmi イメージ名

# イメージをビルド
docker build -t イメージ名 .
```

#### その他

```bash
# Dockerのバージョン確認
docker --version

# Dockerの詳細情報
docker info

# ヘルプ
docker --help
docker コマンド --help
```

### 実践1: Nginxコンテナを起動

Webサーバー「Nginx」を起動してみましょう。

#### 手順:

```bash
# Nginxコンテナを起動
docker run -d -p 8080:80 --name my-nginx nginx
```

**コマンドの意味:**
- `docker run`: コンテナを実行
- `-d`: バックグラウンドで実行（デタッチモード）
- `-p 8080:80`: ポート8080をコンテナの80にマッピング
- `--name my-nginx`: コンテナ名を指定
- `nginx`: 使用するイメージ

**実行中:**
```
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
...
Status: Downloaded newer image for nginx:latest
a1b2c3d4e5f6...
```

最後の文字列（コンテナID）が表示されたら成功！

#### 確認:

**ブラウザで確認:**
http://localhost:8080 にアクセス

**「Welcome to nginx!」** と表示されればOK！

**ターミナルで確認:**
```bash
docker ps
```

**出力例:**
```
CONTAINER ID   IMAGE   COMMAND                  CREATED         STATUS         PORTS                  NAMES
a1b2c3d4e5f6   nginx   "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:8080->80/tcp   my-nginx
```

#### 停止と削除:

```bash
# コンテナを停止
docker stop my-nginx

# コンテナを削除
docker rm my-nginx

# イメージを削除（オプション）
docker rmi nginx
```

### 実践2: Pythonコンテナで対話的に操作

#### 手順:

```bash
# Pythonコンテナを起動して対話モードに入る
docker run -it python:3.11 python
```

**コマンドの意味:**
- `-it`: 対話モード
- `python:3.11`: Python 3.11のイメージ
- `python`: 実行するコマンド

Pythonの対話シェルが起動します:
```python
Python 3.11.6 (main, Oct  8 2023, 05:06:43)
>>> 
```

**試してみる:**
```python
>>> print("Hello from Docker!")
Hello from Docker!
>>> import sys
>>> sys.version
'3.11.6 ...'
>>> exit()
```

`exit()` で終了します。

### 実践3: コンテナ内でコマンドを実行

#### 手順:

```bash
# Ubuntuコンテナを起動してbashに入る
docker run -it ubuntu bash
```

Ubuntuのシェルが起動します:
```
root@a1b2c3d4e5f6:/#
```

**試してみる:**
```bash
# 現在のディレクトリ
pwd
# → /

# ファイル一覧
ls
# → bin  boot  dev  etc  home  lib ...

# OSの情報
cat /etc/os-release
# → Ubuntu 22.04.3 LTS ...

# 終了
exit
```

### 実践4: ボリュームマウント（ファイル共有）

ホストのファイルをコンテナと共有します。

#### 準備:

```bash
# 作業ディレクトリを作成
mkdir ~/docker-test
cd ~/docker-test

# テストファイルを作成
echo "Hello from host!" > hello.txt
```

#### 実行:

```bash
# カレントディレクトリをコンテナの/dataにマウント
docker run -it -v $(pwd):/data ubuntu bash
```

**コンテナ内で:**
```bash
# マウントされたファイルを確認
cd /data
ls
# → hello.txt

# ファイルの内容
cat hello.txt
# → Hello from host!

# コンテナからファイルを作成
echo "Hello from container!" > from-container.txt

# 終了
exit
```

**ホストで確認:**
```bash
# コンテナで作成したファイルが見える
ls
# → hello.txt  from-container.txt

cat from-container.txt
# → Hello from container!
```

💡 **ポイント:** ホストとコンテナでファイルを共有できます！

### よく使うDockerコマンド早見表

```bash
# === コンテナ操作 ===
docker ps                          # 実行中のコンテナ一覧
docker ps -a                       # すべてのコンテナ一覧
docker run イメージ名              # コンテナ作成＆起動
docker start コンテナ名            # コンテナ起動
docker stop コンテナ名             # コンテナ停止
docker restart コンテナ名          # コンテナ再起動
docker rm コンテナ名               # コンテナ削除
docker rm -f コンテナ名            # 強制削除（実行中でも）

# === イメージ操作 ===
docker images                      # イメージ一覧
docker pull イメージ名             # イメージ取得
docker rmi イメージ名              # イメージ削除
docker build -t 名前 .             # イメージビルド

# === ログ・確認 ===
docker logs コンテナ名             # ログ表示
docker logs -f コンテナ名          # ログをリアルタイム表示
docker inspect コンテナ名          # 詳細情報
docker exec -it コンテナ名 bash    # コンテナ内でコマンド実行

# === クリーンアップ ===
docker system prune                # 未使用データを削除
docker container prune             # 停止中のコンテナを削除
docker image prune                 # 未使用イメージを削除
docker volume prune                # 未使用ボリュームを削除
```

---

## 📄 Dockerfileの作成

### Dockerfileとは

**Dockerfile** は、Dockerイメージを作るための設計書です。

**メリット:**
- コードとして管理できる
- 再現可能な環境
- チームで共有できる
- Gitで管理できる

### Dockerfileの基本構文

```dockerfile
# ベースイメージを指定
FROM イメージ名:タグ

# 作業ディレクトリを設定
WORKDIR /app

# ファイルをコピー
COPY ホストのパス コンテナのパス

# コマンドを実行（ビルド時）
RUN コマンド

# 環境変数を設定
ENV キー=値

# ポートを公開
EXPOSE ポート番号

# コンテナ起動時のコマンド
CMD ["実行ファイル", "引数1", "引数2"]
```

### 実践1: 簡単なPythonアプリをDockerize

#### ステップ1: プロジェクトを作成

```bash
# プロジェクトディレクトリを作成
mkdir ~/docker-python-app
cd ~/docker-python-app
```

#### ステップ2: Pythonスクリプトを作成

`app.py` を作成:

```python
# app.py
print("Hello from Docker!")
print("This is a Python app running in a container.")

# 簡単な計算
for i in range(1, 6):
    print(f"{i} x 2 = {i * 2}")
```

#### ステップ3: Dockerfileを作成

`Dockerfile` を作成（拡張子なし）:

```dockerfile
# Python 3.11をベースイメージとして使用
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# ホストのapp.pyをコンテナの/appにコピー
COPY app.py .

# コンテナ起動時にapp.pyを実行
CMD ["python", "app.py"]
```

#### ステップ4: イメージをビルド

```bash
docker build -t my-python-app .
```

**実行中:**
```
[+] Building 2.3s (8/8) FINISHED
 => [internal] load build definition from Dockerfile
 => [internal] load .dockerignore
 => [internal] load metadata for docker.io/library/python:3.11-slim
 => [1/2] FROM docker.io/library/python:3.11-slim
 => [2/2] COPY app.py .
 => exporting to image
 => => naming to docker.io/library/my-python-app
```

**確認:**
```bash
docker images
```

`my-python-app` が表示されればOK！

#### ステップ5: コンテナを実行

```bash
docker run my-python-app
```

**出力:**
```
Hello from Docker!
This is a Python app running in a container.
1 x 2 = 2
2 x 2 = 4
3 x 2 = 6
4 x 2 = 8
5 x 2 = 10
```

成功！

### 実践2: Flaskアプリをコンテナ化

より実践的なWebアプリを作ります。

#### ステップ1: プロジェクトを作成

```bash
mkdir ~/docker-flask-app
cd ~/docker-flask-app
```

#### ステップ2: requirements.txtを作成

```
Flask==3.0.0
```

#### ステップ3: app.pyを作成

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>Hello from Docker!</h1>
    <p>This Flask app is running in a container.</p>
    '''

@app.route('/api/data')
def data():
    return {
        'message': 'Hello from API',
        'status': 'success'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

#### ステップ4: Dockerfileを作成

```dockerfile
# Python 3.11をベースイメージとして使用
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# requirements.txtをコピーして依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルをコピー
COPY app.py .

# ポート5000を公開
EXPOSE 5000

# Flaskアプリを起動
CMD ["python", "app.py"]
```

#### ステップ5: .dockerignoreを作成

Gitの`.gitignore`と同じ役割です。

```
__pycache__
*.pyc
*.pyo
.git
.env
venv/
```

#### ステップ6: イメージをビルド

```bash
docker build -t flask-app .
```

#### ステップ7: コンテナを実行

```bash
docker run -d -p 5000:5000 --name my-flask-app flask-app
```

**確認:**

ブラウザで http://localhost:5000 にアクセス
→ 「Hello from Docker!」と表示されればOK！

http://localhost:5000/api/data にアクセス
→ JSON が表示されればOK！

**ログを確認:**
```bash
docker logs my-flask-app
```

**停止:**
```bash
docker stop my-flask-app
docker rm my-flask-app
```

### Dockerfileのベストプラクティス

#### 1. .dockerignoreを使う

不要なファイルをコピーしない:
```
.git
.gitignore
.DS_Store
__pycache__
*.pyc
venv/
node_modules/
.env
*.log
```

#### 2. レイヤーを最小化

```dockerfile
# 悪い例
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y pip

# 良い例
RUN apt-get update && \
    apt-get install -y python3 pip && \
    rm -rf /var/lib/apt/lists/*
```

#### 3. キャッシュを活用

変更の少ないものを先に:

```dockerfile
# 依存関係を先にコピー
COPY requirements.txt .
RUN pip install -r requirements.txt

# アプリケーションコードは後で
COPY . .
```

#### 4. マルチステージビルド

本番環境では不要なものを削除:

```dockerfile
# ビルドステージ
FROM python:3.11 as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# 本番ステージ
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
```

---

## 🎼 Docker Composeの使い方

### Docker Composeとは

**Docker Compose** は、複数のコンテナを一括管理するツールです。

**できること:**
- 複数コンテナを一度に起動
- コンテナ間の連携を簡単に設定
- 設定をYAMLファイルで管理
- ワンコマンドで環境構築

**使用例:**
- Webアプリ + データベース
- API + キャッシュサーバー
- フロントエンド + バックエンド + DB

### docker-compose.ymlの基本構文

```yaml
version: '3.8'

services:
  サービス名1:
    image: イメージ名
    ports:
      - "ホストポート:コンテナポート"
    volumes:
      - ホストパス:コンテナパス
    environment:
      - 環境変数=値

  サービス名2:
    build: .
    depends_on:
      - サービス名1
```

### 実践1: WordPress + MySQLを構築

#### ステップ1: プロジェクトを作成

```bash
mkdir ~/docker-wordpress
cd ~/docker-wordpress
```

#### ステップ2: docker-compose.ymlを作成

```yaml
version: '3.8'

services:
  # MySQLデータベース
  db:
    image: mysql:8.0
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppassword

  # WordPress
  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    ports:
      - "8080:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppassword
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress_data:/var/www/html

volumes:
  db_data:
  wordpress_data:
```

#### ステップ3: 起動

```bash
docker compose up -d
```

**実行中:**
```
[+] Running 3/3
 ✔ Network docker-wordpress_default       Created
 ✔ Container docker-wordpress-db-1        Started
 ✔ Container docker-wordpress-wordpress-1 Started
```

#### ステップ4: 確認

**コンテナ確認:**
```bash
docker compose ps
```

**ブラウザで確認:**
http://localhost:8080

WordPressの初期設定画面が表示されればOK！

#### ステップ5: 停止と削除

```bash
# 停止
docker compose stop

# 停止＆削除
docker compose down

# データも削除（注意！）
docker compose down -v
```

### 実践2: Flask + PostgreSQLアプリ

より実践的な構成を作ります。

#### ステップ1: プロジェクトを作成

```bash
mkdir ~/docker-flask-postgres
cd ~/docker-flask-postgres
```

#### ステップ2: requirements.txtを作成

```
Flask==3.0.0
psycopg2-binary==2.9.9
```

#### ステップ3: app.pyを作成

```python
from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

@app.route('/')
def hello():
    return '<h1>Flask + PostgreSQL in Docker!</h1>'

@app.route('/db-test')
def db_test():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({
            'status': 'success',
            'database': 'PostgreSQL',
            'version': db_version[0]
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

#### ステップ4: Dockerfileを作成

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

#### ステップ5: docker-compose.ymlを作成

```yaml
version: '3.8'

services:
  # PostgreSQLデータベース
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myuser"]
      interval: 5s
      timeout: 5s
      retries: 5

  # Flaskアプリ
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      DB_HOST: db
      DB_NAME: mydb
      DB_USER: myuser
      DB_PASSWORD: mypassword
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - .:/app

volumes:
  postgres_data:
```

#### ステップ6: 起動

```bash
docker compose up -d
```

#### ステップ7: 確認

http://localhost:5000 → Flask起動確認
http://localhost:5000/db-test → DB接続確認

**ログを確認:**
```bash
docker compose logs -f
```

### Docker Composeコマンド早見表

```bash
# === 基本操作 ===
docker compose up              # 起動（フォアグラウンド）
docker compose up -d           # 起動（バックグラウンド）
docker compose down            # 停止＆削除
docker compose stop            # 停止
docker compose start           # 開始
docker compose restart         # 再起動

# === 確認 ===
docker compose ps              # コンテナ一覧
docker compose logs            # ログ表示
docker compose logs -f         # ログをリアルタイム表示
docker compose logs サービス名 # 特定サービスのログ

# === ビルド ===
docker compose build           # イメージをビルド
docker compose up --build      # ビルドして起動

# === 実行 ===
docker compose exec サービス名 bash    # コンテナ内でコマンド実行
docker compose run サービス名 コマンド # 一時的にコマンド実行

# === クリーンアップ ===
docker compose down -v         # 停止＆削除（ボリュームも）
docker compose rm              # 停止済みコンテナを削除
```

---

## 🐍 実践：Python開発環境を構築

実際の開発で使える環境を構築しましょう。

### プロジェクト: データ分析環境

#### ステップ1: プロジェクトを作成

```bash
mkdir ~/docker-data-science
cd ~/docker-data-science
```

#### ステップ2: ディレクトリ構成

```
docker-data-science/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── notebooks/          # Jupyter Notebookを保存
└── data/              # データファイルを保存
```

```bash
mkdir notebooks data
```

#### ステップ3: requirements.txtを作成

```
jupyter==1.0.0
pandas==2.1.3
numpy==1.26.2
matplotlib==3.8.2
seaborn==0.13.0
scikit-learn==1.3.2
```

#### ステップ4: Dockerfileを作成

```dockerfile
FROM python:3.11

WORKDIR /workspace

# 依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Jupyter Notebookの設定
RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.token = ''" >> ~/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> ~/.jupyter/jupyter_notebook_config.py

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

#### ステップ5: docker-compose.ymlを作成

```yaml
version: '3.8'

services:
  jupyter:
    build: .
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/workspace/notebooks
      - ./data:/workspace/data
    environment:
      - JUPYTER_ENABLE_LAB=yes
```

#### ステップ6: 起動

```bash
docker compose up -d
```

#### ステップ7: アクセス

**ブラウザで:**
http://localhost:8888

Jupyter Notebookが開きます！

#### ステップ8: 使ってみる

1. 「New」→「Python 3」で新しいノートブック作成
2. 以下を実行:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# データを作成
data = pd.DataFrame({
    'x': range(10),
    'y': np.random.randn(10)
})

# プロット
plt.plot(data['x'], data['y'])
plt.title('Test Plot in Docker')
plt.show()
```

グラフが表示されればOK！

#### ステップ9: ファイルの永続化

ノートブックを保存すると、`notebooks/`フォルダに保存されます。
コンテナを削除しても、ファイルは残ります。

---

## 💻 VSCodeとDockerの連携

VSCodeでDockerコンテナ内を直接編集できるようにします。

### ステップ1: 拡張機能をインストール

#### 1-1: VSCodeを開く

#### 1-2: 拡張機能を検索

`Command + Shift + X` で拡張機能を開く

#### 1-3: 以下をインストール

1. **「Docker」**
   - 作成者: Microsoft
   - Dockerコンテナ・イメージを管理

2. **「Dev Containers」**
   - 作成者: Microsoft
   - コンテナ内で開発

インストール後、VSCodeを再起動

### ステップ2: Dockerサイドバーを確認

左サイドバーに **クジラアイコン** が追加されます。

クリックすると:
- Containers: 実行中のコンテナ一覧
- Images: イメージ一覧
- Volumes: ボリューム一覧

### ステップ3: コンテナ内で開発

#### 方法1: 既存のコンテナに接続

1. **左サイドバーのDockerアイコン** をクリック
2. **Containers** セクションで実行中のコンテナを右クリック
3. **「Attach Visual Studio Code」** を選択

新しいVSCodeウィンドウが開き、コンテナ内が表示されます！

#### 方法2: Dev Containerを使う

プロジェクトに`.devcontainer/devcontainer.json`を作成。

**例: Python開発環境**

`.devcontainer/devcontainer.json`:
```json
{
  "name": "Python Dev Container",
  "image": "python:3.11",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  },
  "postCreateCommand": "pip install -r requirements.txt",
  "forwardPorts": [5000]
}
```

**使い方:**
1. `Command + Shift + P`
2. 「Dev Containers: Reopen in Container」
3. VSCodeがコンテナ内で再起動

### ステップ4: Dockerfileを編集

VSCodeでDockerfileを開くと:
- シンタックスハイライト
- 補完機能
- エラーチェック

が自動的に有効になります。

### ステップ5: docker-compose.ymlを編集

VSCodeでdocker-compose.ymlを開くと:
- YAMLのシンタックスハイライト
- インデントのチェック
- スキーマ検証

が有効になります。

---

## 🐛 トラブルシューティング

### Docker Desktopが起動しない

#### 症状: 起動時にエラー

**対処法1: 完全に再起動**
```bash
# Docker Desktopを終了
killall Docker

# 再起動
open -a Docker
```

**対処法2: キャッシュをクリア**
```bash
rm -rf ~/Library/Group\ Containers/group.com.docker
rm -rf ~/Library/Containers/com.docker.docker
```

その後、Docker Desktopを再インストール

**対処法3: macOSを再起動**

### コンテナが起動しない

#### 症状: `docker run` が失敗

**対処法1: ログを確認**
```bash
docker logs コンテナ名
```

**対処法2: ポートの競合を確認**
```bash
# 使用中のポートを確認
lsof -i :ポート番号

# 例: ポート8080
lsof -i :8080
```

他のプロセスが使っている場合、停止するか別のポートを使う

**対処法3: イメージを再取得**
```bash
docker pull イメージ名
```

### イメージのビルドが失敗

#### 症状: `docker build` でエラー

**対処法1: キャッシュを使わずビルド**
```bash
docker build --no-cache -t イメージ名 .
```

**対処法2: Dockerfileの構文を確認**
- インデントは正しいか
- コマンドは正しいか
- パスは正しいか

**対処法3: ベースイメージを確認**
```bash
docker pull ベースイメージ名
```

### コンテナが見つからない

#### 症状: `Error: No such container`

**対処法: すべてのコンテナを確認**
```bash
docker ps -a
```

停止中のコンテナも含めてすべて表示されます。

### ディスク容量不足

#### 症状: `no space left on device`

**対処法1: 未使用データを削除**
```bash
# すべての未使用データを削除
docker system prune -a

# 確認メッセージ
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all images without at least one container associated to them
  - all build cache

Are you sure you want to continue? [y/N] y
```

**対処法2: 個別に削除**
```bash
# 停止中のコンテナを削除
docker container prune

# 未使用イメージを削除
docker image prune -a

# 未使用ボリュームを削除
docker volume prune
```

**対処法3: ディスクイメージのサイズを確認**
Docker Desktop → Settings → Resources → Disk image size

### パーミッションエラー

#### 症状: `permission denied`

**対処法1: sudoを使う**
```bash
sudo docker run ...
```

**対処法2: ユーザーをdockerグループに追加**
```bash
sudo usermod -aG docker $USER
```

ログアウトして再ログイン

### コンテナ間で通信できない

#### 症状: コンテナAからコンテナBに接続できない

**対処法: 同じネットワークに配置**

```bash
# ネットワークを作成
docker network create my-network

# コンテナを同じネットワークで起動
docker run --network my-network --name container-a ...
docker run --network my-network --name container-b ...
```

Docker Composeを使う場合は自動的に同じネットワークになります。

### M1 Mac特有の問題

#### 症状: `exec format error`

**原因:** Intel用のイメージをApple Siliconで実行しようとしている

**対処法: プラットフォームを指定**
```bash
docker run --platform linux/amd64 イメージ名
```

または、Dockerfileで:
```dockerfile
FROM --platform=linux/amd64 イメージ名
```

---

## 🙋 よくある質問（FAQ）

### Q1: DockerとVMの違いは？

**A:**

**VM（仮想マシン）:**
- OS全体を仮想化
- 重い（GB単位）
- 起動が遅い（数分）

**Docker:**
- アプリケーションのみ隔離
- 軽い（MB単位）
- 起動が速い（数秒）

**例え:**
- VM = 家全体を引っ越し
- Docker = 部屋だけ引っ越し

### Q2: Docker DesktopとDocker Engineの違いは？

**A:**

**Docker Desktop（Mac/Windows）:**
- GUIアプリ
- 初心者に優しい
- 有料（大企業の場合）

**Docker Engine（Linux）:**
- CLIのみ
- 無料
- サーバーで使われる

Macでは**Docker Desktop**を使います。

### Q3: コンテナとイメージの違いは？

**A:**

**イメージ:**
- 設計図・テンプレート
- 読み取り専用
- 1つのイメージから複数のコンテナを作成可能

**コンテナ:**
- イメージから作られた実行環境
- 読み書き可能
- 独立して動作

**例え:**
- イメージ = クッキーの型
- コンテナ = 焼いたクッキー

### Q4: コンテナのデータは消えますか？

**A:** はい、デフォルトでは消えます。

**対策:**
- **ボリューム** を使う
- **バインドマウント** を使う

```bash
# ボリュームを使う
docker run -v my-volume:/data ...

# バインドマウント
docker run -v $(pwd):/data ...
```

### Q5: Dockerは無料ですか？

**A:** 基本的に無料です。

**無料:**
- 個人利用
- 小規模企業（従業員250人未満）
- 教育機関

**有料:**
- 大企業（従業員250人以上）
- 年間売上$10M以上

詳細: https://www.docker.com/pricing/

### Q6: Dockerのセキュリティは大丈夫？

**A:** 適切に使えば安全です。

**セキュリティのポイント:**
- 公式イメージを使う
- イメージを定期的に更新
- 秘密情報を環境変数で管理
- 不要な権限を与えない

### Q7: 本番環境でDockerを使えますか？

**A:** はい、多くの企業で使われています。

**使用例:**
- Netflix
- Uber
- Spotify
- PayPal

**メリット:**
- スケーリングが簡単
- デプロイが高速
- 環境の一貫性

### Q8: KubernetesとDockerの関係は？

**A:**

**Docker:**
- コンテナ実行環境
- 単一マシンでの管理

**Kubernetes:**
- コンテナオーケストレーション
- 複数マシンでの管理
- Dockerコンテナを大規模に運用

**関係:**
Kubernetesは Dockerコンテナを管理するツール

### Q9: Dockerが遅いのですが...

**A:** リソース設定を調整しましょう。

Docker Desktop → Settings → Resources

**推奨設定:**
- CPUs: 総数の半分
- Memory: 
  - 8GBのMac → 4GB
  - 16GBのMac → 6-8GB
- Disk: 十分な空き容量

### Q10: Dockerfileとdocker-compose.ymlの違いは？

**A:**

**Dockerfile:**
- 1つのイメージを作る設計書
- イメージのビルド方法を定義

**docker-compose.yml:**
- 複数のコンテナを管理する設定ファイル
- サービスの組み合わせを定義

**使い分け:**
- 1つのアプリ → Dockerfile
- 複数のサービス → docker-compose.yml

---

## 📚 参考リンク集

### 公式ドキュメント
- [Docker公式サイト](https://www.docker.com/)
- [Docker Docs](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)

### 学習リソース
- [Docker入門（日本語）](https://docs.docker.jp/get-started/toc.html)
- [Play with Docker](https://labs.play-with-docker.com/)（ブラウザで試せる）

### コミュニティ
- [Docker Community](https://www.docker.com/community/)
- [Stack Overflow - Docker](https://stackoverflow.com/questions/tagged/docker)

---

## ✅ 最終チェックリスト

### 基本設定
- [ ] Docker Desktopがインストールされている
- [ ] `docker --version` でバージョン確認できる
- [ ] `docker run hello-world` が成功する
- [ ] メニューバーにクジラアイコンが表示される

### 基本操作
- [ ] コンテナを起動できる
- [ ] コンテナを停止・削除できる
- [ ] イメージを取得できる
- [ ] ログを確認できる

### Dockerfile
- [ ] Dockerfileを作成できる
- [ ] イメージをビルドできる
- [ ] カスタムイメージを実行できる

### Docker Compose
- [ ] docker-compose.ymlを作成できる
- [ ] 複数コンテナを起動できる
- [ ] サービス間で通信できる

### VSCode連携
- [ ] Docker拡張機能をインストールした
- [ ] コンテナ一覧を確認できる
- [ ] Dev Containersの概念を理解した

---

## 🎉 おめでとうございます！

このガイドを完了したあなたは、もう立派なDocker使いです！

**これからできること:**
- ✅ 開発環境を簡単に構築
- ✅ チームで同じ環境を共有
- ✅ 様々な技術を気軽に試せる
- ✅ 本番環境へのデプロイ準備

**次のステップ:**
1. 実際のプロジェクトでDockerを使う
2. Docker Composeで複雑な環境を構築
3. Kubernetes（k8s）を学習
4. CI/CDパイプラインでDockerを活用

**継続的な学習のために:**
- 毎日少しずつDockerを使う
- 公式ドキュメントを読む
- コミュニティに参加する
- 実践あるのみ！

あなたの開発ライフがより快適になりますように！

**Happy Dockering! 🐳**

---

**バージョン:** 1.0（完全版）  
**対応OS:** macOS 11 Big Sur以降  
**前提:** Git/GitHub導入完了  
**最終更新:** 2025年10月