# Windows初心者のためのDocker完全ガイド【Intel/AMD/ARM64完全対応】

## 🎯 このガイドについて

**前提条件:**
- ✅ Git/GitHubの導入が完了している
- ✅ VSCodeがインストールされている
- ✅ ターミナル（PowerShell/コマンドプロンプト）の基本操作ができる
- ✅ WindowsでGitHubにプッシュ・プルができる

このガイド**だけ**で、**すべてのWindows**（Intel/AMD/ARM64）でのDockerの導入が完了します。
他の資料を見る必要は一切ありません。

**対応プロセッサ:**
- ✅ Intel（Core i3/i5/i7/i9など）
- ✅ AMD（Ryzen 3/5/7/9など）
- ✅ **ARM64**（Snapdragon、Surface Pro Xなど）← NEW!

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
3. [WSL2のセットアップ](#wsl2のセットアップ)
4. [Docker Desktopのインストール](#docker-desktopのインストール)
5. [Dockerの基本操作](#dockerの基本操作)
6. [Dockerfileの作成](#dockerfileの作成)
7. [Docker Composeの使い方](#docker-composeの使い方)
8. [実践：Python開発環境を構築](#実践python開発環境を構築)
9. [VSCodeとDockerの連携](#vscodeとdockerの連携)
10. [ARM64特有の注意事項](#arm64特有の注意事項)
11. [トラブルシューティング](#トラブルシューティング)
12. [よくある質問（FAQ）](#よくある質問faq)

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
開発者A: 「私のWindowsでは動きます」
開発者B: 「私のMacでは動きません...」
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

**Windows:**
- **Windows 10 バージョン 2004以降（ビルド19041以降）** または **Windows 11**
- **64ビット版**（32ビット版は非対応）

**エディション:**
- Windows 10/11 Home
- Windows 10/11 Pro
- Windows 10/11 Enterprise
- Windows 10/11 Education

**ハードウェア:**
- メモリ: 最低4GB、推奨8GB以上
- ストレージ: 最低10GB、推奨20GB以上の空き容量
- CPU: 
  - **Intel/AMD**: 仮想化支援機能（Intel VT-x または AMD-V）が必要
  - **ARM64**: ネイティブ対応

**ソフトウェア:**
- ✅ Git/GitHubの設定完了
- ✅ VSCodeインストール済み
- ✅ PowerShellまたはコマンドプロンプトの基本操作ができる

### 自分のWindowsを確認

#### 1. Windowsバージョンを確認

**方法1: 設定から確認**
1. **Windowsキー + I** で設定を開く
2. **「システム」** → **「バージョン情報」**
3. 「Windowsの仕様」セクションを確認
   - **エディション**: Home/Pro/Enterprise
   - **バージョン**: 2004以降
   - **ビルド**: 19041以降

**方法2: コマンドで確認**
PowerShellで以下を実行:
```powershell
winver
```

ウィンドウが開き、バージョン情報が表示されます。

💡 **必要:** Windows 10 バージョン 2004（ビルド19041）以降

#### 2. プロセッサのアーキテクチャを確認（重要！）

同じ「バージョン情報」画面で:
- **「システムの種類」** を確認

**表示例と対応プロセッサ:**

**Intel/AMD（x64）の場合:**
```
システムの種類: x64ベースプロセッサ
プロセッサ: Intel(R) Core(TM) i7-XXXXX
```
または
```
プロセッサ: AMD Ryzen 7 XXXXX
```

**ARM64の場合:**
```
システムの種類: ARM64ベースプロセッサ
プロセッサ: Snapdragon(TM) 8cx Gen 3 @ 3.00 GHz
```
または
```
プロセッサ: Microsoft SQ1/SQ2/SQ3
```

💡 **確認方法（PowerShellでも確認可能）:**
```powershell
Get-ComputerInfo | Select-Object CsProcessors, OsArchitecture
```

**出力例:**
```
# Intel/AMDの場合
OsArchitecture
--------------
64-bit

# ARM64の場合
OsArchitecture
--------------
ARM64
```

📝 **重要:** この情報は後の手順で使います！

**⚠️ ARM64の場合の注意:**
- Surface Pro X
- Lenovo ThinkPad X13s
- Samsung Galaxy Book series
- Dell Inspiron 14 (3420)
などのデバイスが該当します

❌ **「x86ベース」または「32ビット」** → Docker非対応

#### 3. メモリを確認

同じ画面で **「実装RAM」** を確認
- 推奨: 8GB以上

#### 4. ストレージを確認

**エクスプローラー** → **「PC」** でCドライブの空き容量を確認
- 推奨: 20GB以上の空き

### BIOSで仮想化を有効にする（Intel/AMD のみ）

**⚠️ ARM64の場合:** この手順はスキップしてください（仮想化は常に有効）

DockerにはCPUの仮想化機能が必要です。

#### 仮想化が有効か確認（Intel/AMD）

**タスクマネージャーで確認:**
1. **Ctrl + Shift + Esc** でタスクマネージャーを開く
2. **「パフォーマンス」** タブ
3. **「CPU」** を選択
4. 右下に **「仮想化: 有効」** と表示されていればOK

**ARM64の場合:**
- 「仮想化」の項目は表示されない（常に有効）

**無効の場合（Intel/AMD のみ）:** BIOSで有効化が必要

#### BIOSで仮想化を有効化（Intel/AMDで必要な場合のみ）

**⚠️ 注意:** BIOSの操作は慎重に行ってください。

**一般的な手順:**
1. PCを再起動
2. 起動時に **F2** / **F10** / **Del** / **Esc** キーを連打（メーカーによる）
3. BIOS設定画面に入る
4. **「Advanced」** → **「CPU Configuration」**
5. 以下を探して **「Enabled」** にする:
   - **Intel**: Intel VT-x または Intel Virtualization Technology
   - **AMD**: AMD-V または SVM Mode
6. **「Save & Exit」** で保存して終了

💡 **メーカー別の詳細はメーカーのサポートページを確認してください**

### 古いDockerがないか確認

以前にDockerをインストールしたことがある場合、確認します。

PowerShellで:
```powershell
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
'docker' は、内部コマンドまたは外部コマンド、
操作可能なプログラムまたはバッチ ファイルとして認識されていません。
```
→ 問題なし、次のステップへ

**古いDockerをアンインストールする方法:**
1. **Windowsキー + I** → **「アプリ」** → **「アプリと機能」**
2. **「Docker Desktop」** を検索
3. **「アンインストール」** をクリック
4. PCを再起動

---

## 🔧 WSL2のセットアップ

Docker Desktop for Windowsは **WSL2（Windows Subsystem for Linux 2）** を使用します。
WSL2を先にセットアップする必要があります。

### WSL2とは

**WSL2** は、Windows上でLinuxを動かす仕組みです。

**メリット:**
- LinuxコマンドがWindowsで使える
- Dockerが高速に動作
- ファイルシステムのパフォーマンスが向上

**ARM64での動作:**
- ARM64版WindowsでもWSL2は完全動作
- ARM64版Linuxカーネルが自動でインストールされる

### ステップ1: WSL2をインストール

#### 方法1: 自動インストール（Windows 11 / Windows 10 2004以降）

**管理者権限でPowerShellを開く:**
1. **Windowsキー** を押す
2. **「PowerShell」** と入力
3. **「Windows PowerShell」** を右クリック
4. **「管理者として実行」** を選択

**以下のコマンドを実行:**

**Intel/AMD/ARM64共通:**
```powershell
wsl --install
```

**実行中:**
```
インストール中: 仮想マシン プラットフォーム
インストール中: Linux 用 Windows サブシステム
インストール中: Ubuntu
要求された操作は正常に終了しました。変更を有効にするには、システムを再起動する必要があります。
```

💡 **ARM64の場合:** ARM64ネイティブのLinuxカーネルが自動的にインストールされます

💡 **完了したらPCを再起動してください**

#### 方法2: 手動インストール（古いバージョンの場合）

**1. WSL機能を有効化**

管理者権限のPowerShellで:

**Intel/AMD/ARM64共通:**
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

**2. 仮想マシンプラットフォームを有効化**

**Intel/AMD/ARM64共通:**
```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

**3. PCを再起動**

**4. WSL2 Linuxカーネル更新プログラムをダウンロード**

**Intel/AMD（x64）の場合:**
https://aka.ms/wsl2kernel

**ARM64の場合:**
https://aka.ms/wsl2kernelarm64

💡 **ARM64注意:** 必ずARM64版をダウンロードしてください！

**5. WSL2をデフォルトに設定**

**Intel/AMD/ARM64共通:**
```powershell
wsl --set-default-version 2
```

### ステップ2: Linuxディストリビューションをインストール

#### Ubuntuをインストール

PowerShellで:

**Intel/AMD/ARM64共通:**
```powershell
wsl --install -d Ubuntu
```

💡 **ARM64注意:** Ubuntu 20.04以降がARM64対応しています

または、Microsoft Storeから:
1. **Microsoft Store** を開く
2. **「Ubuntu」** を検索
3. **「入手」** をクリック

**ARM64の場合のディストリビューション選択肢:**
- ✅ Ubuntu（推奨）
- ✅ Ubuntu 22.04 LTS
- ✅ Debian
- ✅ Kali Linux

#### 初回セットアップ

Ubuntuを起動すると、初回セットアップが始まります。

1. **ユーザー名** を入力（小文字推奨）
2. **パスワード** を入力（2回）

💡 **このユーザー名とパスワードは後で使います**

**セットアップ完了:**
```
Installation successful!
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

username@DESKTOP-XXXXXX:~$
```

### ステップ3: WSL2の確認

PowerShellで:

**Intel/AMD/ARM64共通:**
```powershell
wsl --list --verbose
```

**正しい出力:**
```
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

**VERSION が 2** であることを確認！

**VERSION が 1 の場合:**
```powershell
wsl --set-version Ubuntu 2
```

### ステップ4: アーキテクチャを確認（ARM64の場合）

WSL内で実行:
```bash
uname -m
```

**Intel/AMDの場合:**
```
x86_64
```

**ARM64の場合:**
```
aarch64
```

💡 **ARM64確認:** `aarch64` と表示されればARM64版Linuxが正しくインストールされています

### ステップ5: WSL2の更新

**Intel/AMD/ARM64共通:**
```powershell
wsl --update
```

最新版に更新されます。

### ✅ WSL2セットアップ完了チェック

以下をすべて確認:
- [ ] `wsl --list --verbose` でUbuntuが表示される
- [ ] VERSIONが2になっている
- [ ] Ubuntuを起動できる
- [ ] Ubuntuでコマンドを実行できる
- [ ] **ARM64の場合:** `uname -m` で `aarch64` と表示される

---

## 🚀 Docker Desktopのインストール

### ステップ1: Docker Desktopをダウンロード

#### 1-1: 公式サイトにアクセス

https://www.docker.com/products/docker-desktop にアクセス

#### 1-2: 正しいバージョンをダウンロード

**Intel/AMD（x64）の場合:**
- **「Download for Windows」** をクリック
- ファイル名: `Docker Desktop Installer.exe`

**ARM64の場合:**
- ページをスクロールして **「Windows on ARM」** を探す
- または直接リンク: https://desktop.docker.com/win/main/arm64/Docker%20Desktop%20Installer.exe
- ファイル名: `Docker Desktop Installer.exe` (ARM64版)

💡 **ARM64重要:** 必ずARM64版をダウンロードしてください！x64版は動作しません！

**⚠️ どちらか分からない場合:**
PowerShellで確認:
```powershell
Get-ComputerInfo | Select-Object OsArchitecture
```
- `64-bit` → Intel/AMD版
- `ARM64` → ARM64版

#### 1-3: ダウンロード完了

ダウンロードフォルダに `Docker Desktop Installer.exe` が保存されます。

### ステップ2: Docker Desktopをインストール

#### 2-1: インストーラーを実行

1. ダウンロードした **`Docker Desktop Installer.exe`** をダブルクリック
2. **ユーザーアカウント制御** が表示されたら **「はい」** をクリック

#### 2-2: 設定を選択

**「Configuration」** 画面で:

**Intel/AMD/ARM64共通:**
- ☑ **「Use WSL 2 instead of Hyper-V (recommended)」** 
  → **必ずチェック**（推奨）

- ☑ **「Add shortcut to desktop」**
  → デスクトップにショートカット作成（任意）

**「OK」** をクリック

#### 2-3: インストール開始

インストールが始まります（3〜5分）
- ファイルのコピー
- サービスの登録
- 設定の適用

**ARM64の場合:** 初回インストール時はやや時間がかかる場合があります（5〜7分）

⏳ **待機中:** PCの電源を入れたままにしてください

#### 2-4: インストール完了

**「Installation succeeded」**

- **「Close and restart」** をクリック

PCが**自動的に再起動**します。

### ステップ3: Docker Desktopを起動

#### 3-1: Docker Desktopを起動

- **デスクトップのアイコン** をダブルクリック
- または、スタートメニューから **「Docker Desktop」** を検索

#### 3-2: 使用許諾契約

**「Docker Subscription Service Agreement」**

1. 内容を確認（スクロールして読む）
2. ☑ **「I accept the terms」** にチェック
3. **「Accept」** をクリック

💡 **個人利用・小規模チーム:** 無料で使えます

#### 3-3: 推奨設定の確認

**「Use recommended settings」**

推奨設定を使うか選択:
- ☑ **「Use recommended settings」** にチェック（推奨）
- **「Finish」** をクリック

#### 3-4: 初期化

**「Starting Docker Desktop...」**

初期化が始まります（2〜5分）
- エンジンの起動
- WSL2との連携
- 必要なファイルのダウンロード

**ARM64の場合:** 初回起動は追加のコンポーネントをダウンロードするため、やや時間がかかります（5〜10分）

⏳ **待機中:** 画面を閉じないでください

#### 3-5: サインイン画面（オプション）

**「Sign in to Docker」**

- **Docker Hubアカウントがある場合:** サインイン
- **ない場合:** **「Skip」** をクリック

💡 **初心者:** スキップしてOK（後で作成可能）

#### 3-6: チュートリアル

**「Quick Start Guide」**

簡単なチュートリアルが表示されます。
- 見たい場合: 進める
- スキップしたい場合: 画面を閉じる

### ステップ4: Docker Desktopの確認

#### 4-1: Docker Desktopが起動しているか確認

**タスクバー（画面右下）** に **クジラアイコン** 🐳 が表示されていればOK！

クジラアイコンを右クリック → **「Dashboard」** でGUIが開きます

#### 4-2: PowerShellで確認

PowerShellを開いて以下を実行:

**Intel/AMD/ARM64共通:**
```powershell
docker --version
```

**成功:**
```
Docker version 24.0.6, build ed223bc
```

バージョンが表示されればOK！

```powershell
docker compose version
```

**成功:**
```
Docker Compose version v2.23.0
```

これも表示されればOK！

#### 4-3: Hello Worldを実行

Dockerが正しく動作するか確認:

**Intel/AMDの場合:**
```powershell
docker run hello-world
```

**ARM64の場合:**
```powershell
# ARM64ネイティブイメージを使用
docker run --platform linux/arm64 hello-world
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

**ARM64の場合の追加確認:**
```powershell
docker run --platform linux/arm64 ubuntu uname -m
```

**出力:**
```
aarch64
```

`aarch64` と表示されればARM64ネイティブで動作しています！

### ステップ5: Docker Desktopの基本設定

#### 5-1: Docker Desktopを開く

タスクバーのクジラアイコンを右クリック → **「Dashboard」**

#### 5-2: Settingsを開く

右上の **⚙️（歯車アイコン）** → **「Settings」**

#### 5-3: 推奨設定

**General（一般）:**

**Intel/AMD/ARM64共通:**
- ☑ **「Start Docker Desktop when you log in」** → 自動起動（推奨）
- ☑ **「Use Docker Compose V2」** → チェック
- ☑ **「Use the WSL 2 based engine」** → チェック

**Resources（リソース）:**

**WSL Integration:**

**Intel/AMD/ARM64共通:**
- ☑ **「Enable integration with my default WSL distro」** → チェック
- ☑ **「Ubuntu」** → チェック（インストールしたディストリビューション）

**Advanced:**

**Intel/AMD/ARM64共通:**
- **CPUs**: スライダーを調整
  - 推奨: 総CPU数の半分（例: 8コアなら4）
  
- **Memory**: スライダーを調整
  - **Intel/AMD:**
    - 8GB以下のPC → 2GB
    - 16GBのPC → 4GB
    - 32GB以上のPC → 8GB
  
  - **ARM64:**
    - 8GB以下のPC → 2-3GB（やや控えめ）
    - 16GBのPC → 4-6GB
    - 32GB以上のPC → 8-10GB
    
💡 **ARM64注意:** エミュレーション時により多くのメモリを使用する場合があるため、やや多めに割り当てると安定します

- **Disk image size**: デフォルトでOK（必要に応じて増やす）

#### 5-4: 設定を保存

右下の **「Apply & Restart」** をクリック

Docker Desktopが再起動します（30秒〜1分）

### ✅ Docker Desktopインストール完了チェック

以下をすべて確認:
- [ ] Docker Desktopがインストールされている
- [ ] タスクバーにクジラアイコンが表示される
- [ ] `docker --version` でバージョンが表示される
- [ ] `docker compose version` でバージョンが表示される
- [ ] `docker run hello-world` が成功する（または `--platform linux/arm64` で成功）
- [ ] WSL2との連携が有効
- [ ] **ARM64の場合:** `docker run --platform linux/arm64 ubuntu uname -m` で `aarch64` が表示される

---

## 🚀 Dockerの基本操作

### PowerShellとコマンドプロンプトについて

Windowsでは以下のターミナルが使えます:

**PowerShell（推奨）:**
- 高機能
- 最新のWindows標準
- このガイドではPowerShellを使用

**コマンドプロンプト:**
- 従来のWindowsコマンドライン
- Dockerコマンドは動作する

**WSL2 Ubuntu:**
- Linuxコマンド
- Dockerも使える

💡 **このガイドではPowerShellを使います**

### Dockerの基本コマンド

#### コンテナ操作

**Intel/AMD/ARM64共通:**
```powershell
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

**Intel/AMD/ARM64共通:**
```powershell
# イメージ一覧
docker images

# イメージを取得
docker pull イメージ名

# イメージを削除
docker rmi イメージ名

# イメージをビルド
docker build -t イメージ名 .
```

**ARM64の場合の追加オプション:**
```powershell
# ARM64ネイティブイメージを取得
docker pull --platform linux/arm64 イメージ名

# x64イメージを取得（エミュレーション）
docker pull --platform linux/amd64 イメージ名
```

#### その他

**Intel/AMD/ARM64共通:**
```powershell
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

**Intel/AMDの場合:**
```powershell
# Nginxコンテナを起動
docker run -d -p 8080:80 --name my-nginx nginx
```

**ARM64の場合:**
```powershell
# ARM64ネイティブのNginxコンテナを起動（推奨）
docker run -d -p 8080:80 --name my-nginx --platform linux/arm64 nginx

# または、x64版をエミュレーション（やや遅い）
docker run -d -p 8080:80 --name my-nginx --platform linux/amd64 nginx
```

💡 **ARM64推奨:** `--platform linux/arm64` を指定するとネイティブ動作で高速！

**コマンドの意味:**
- `docker run`: コンテナを実行
- `-d`: バックグラウンドで実行（デタッチモード）
- `-p 8080:80`: ポート8080をコンテナの80にマッピング
- `--name my-nginx`: コンテナ名を指定
- `--platform`: プラットフォームを指定（ARM64の場合）
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

**ブラウザで確認（Intel/AMD/ARM64共通）:**
http://localhost:8080 にアクセス

**「Welcome to nginx!」** と表示されればOK！

**PowerShellで確認:**
```powershell
docker ps
```

**出力例:**
```
CONTAINER ID   IMAGE   COMMAND                  CREATED         STATUS         PORTS                  NAMES
a1b2c3d4e5f6   nginx   "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:8080->80/tcp   my-nginx
```

#### 停止と削除:

**Intel/AMD/ARM64共通:**
```powershell
# コンテナを停止
docker stop my-nginx

# コンテナを削除
docker rm my-nginx

# イメージを削除（オプション）
docker rmi nginx
```

### 実践2: Pythonコンテナで対話的に操作

#### 手順:

**Intel/AMDの場合:**
```powershell
# Pythonコンテナを起動して対話モードに入る
docker run -it python:3.11 python
```

**ARM64の場合:**
```powershell
# ARM64ネイティブのPythonコンテナ（推奨）
docker run -it --platform linux/arm64 python:3.11 python

# または、x64版をエミュレーション
docker run -it --platform linux/amd64 python:3.11 python
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

**Intel/AMDの場合:**
```powershell
# Ubuntuコンテナを起動してbashに入る
docker run -it ubuntu bash
```

**ARM64の場合:**
```powershell
# ARM64ネイティブのUbuntu（推奨）
docker run -it --platform linux/arm64 ubuntu bash

# または、x64版をエミュレーション
docker run -it --platform linux/amd64 ubuntu bash
```

Ubuntuのシェルが起動します:
```
root@a1b2c3d4e5f6:/#
```

**試してみる（Intel/AMD/ARM64共通）:**
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

# アーキテクチャを確認
uname -m
# Intel/AMD: x86_64
# ARM64: aarch64

# 終了
exit
```

### 実践4: ボリュームマウント（ファイル共有）

ホストのファイルをコンテナと共有します。

#### 準備:

PowerShellで:
```powershell
# 作業ディレクトリを作成
New-Item -ItemType Directory -Path $HOME\docker-test
cd $HOME\docker-test

# テストファイルを作成
"Hello from host!" | Out-File -FilePath hello.txt -Encoding utf8
```

#### 実行:

**Intel/AMDの場合:**
```powershell
# カレントディレクトリをコンテナの/dataにマウント
docker run -it -v ${PWD}:/data ubuntu bash
```

**ARM64の場合:**
```powershell
# ARM64ネイティブ（推奨）
docker run -it --platform linux/arm64 -v ${PWD}:/data ubuntu bash

# または、x64版をエミュレーション
docker run -it --platform linux/amd64 -v ${PWD}:/data ubuntu bash
```

**コンテナ内で（Intel/AMD/ARM64共通）:**
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
```powershell
# コンテナで作成したファイルが見える
Get-ChildItem
# → hello.txt  from-container.txt

Get-Content from-container.txt
# → Hello from container!
```

💡 **ポイント:** ホストとコンテナでファイルを共有できます！

### よく使うDockerコマンド早見表

**Intel/AMD/ARM64共通:**
```powershell
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

**ARM64専用コマンド:**
```powershell
# ARM64ネイティブイメージを取得
docker pull --platform linux/arm64 イメージ名

# x64イメージをエミュレーション
docker pull --platform linux/amd64 イメージ名

# 実行中コンテナのアーキテクチャを確認
docker exec コンテナ名 uname -m
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

**Intel/AMD/ARM64共通:**
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

**ARM64の場合のベストプラクティス:**
```dockerfile
# マルチアーキテクチャ対応
FROM --platform=$BUILDPLATFORM イメージ名:タグ

# または、ARM64を明示的に指定
FROM --platform=linux/arm64 イメージ名:タグ
```

### 実践1: 簡単なPythonアプリをDockerize

#### ステップ1: プロジェクトを作成

PowerShellで:
```powershell
# プロジェクトディレクトリを作成
New-Item -ItemType Directory -Path $HOME\docker-python-app
cd $HOME\docker-python-app
```

#### ステップ2: Pythonスクリプトを作成

VSCodeまたはメモ帳で `app.py` を作成:

**Intel/AMD/ARM64共通:**
```python
# app.py
import platform

print("Hello from Docker!")
print("This is a Python app running in a container.")
print(f"Architecture: {platform.machine()}")
print(f"System: {platform.system()}")

# 簡単な計算
for i in range(1, 6):
    print(f"{i} x 2 = {i * 2}")
```

#### ステップ3: Dockerfileを作成

`Dockerfile` を作成（拡張子なし）:

**Intel/AMDの場合:**
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

**ARM64の場合（推奨）:**
```dockerfile
# ARM64ネイティブのPython 3.11を使用
FROM --platform=linux/arm64 python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# ホストのapp.pyをコンテナの/appにコピー
COPY app.py .

# コンテナ起動時にapp.pyを実行
CMD ["python", "app.py"]
```

**マルチアーキテクチャ対応（推奨・高度）:**
```dockerfile
# ビルドプラットフォームに応じて自動選択
FROM --platform=$BUILDPLATFORM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# ホストのapp.pyをコンテナの/appにコピー
COPY app.py .

# コンテナ起動時にapp.pyを実行
CMD ["python", "app.py"]
```

💡 **Windows注意:** Dockerfileは拡張子なしで保存してください

#### ステップ4: イメージをビルド

**Intel/AMDの場合:**
```powershell
docker build -t my-python-app .
```

**ARM64の場合:**
```powershell
# ARM64ネイティブビルド（推奨）
docker build --platform linux/arm64 -t my-python-app .

# または、x64用にビルド（エミュレーション用）
docker build --platform linux/amd64 -t my-python-app .
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
```powershell
docker images
```

`my-python-app` が表示されればOK！

#### ステップ5: コンテナを実行

**Intel/AMD/ARM64共通:**
```powershell
docker run my-python-app
```

**出力（Intel/AMDの場合）:**
```
Hello from Docker!
This is a Python app running in a container.
Architecture: x86_64
System: Linux
1 x 2 = 2
2 x 2 = 4
3 x 2 = 6
4 x 2 = 8
5 x 2 = 10
```

**出力（ARM64の場合）:**
```
Hello from Docker!
This is a Python app running in a container.
Architecture: aarch64
System: Linux
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

```powershell
New-Item -ItemType Directory -Path $HOME\docker-flask-app
cd $HOME\docker-flask-app
```

#### ステップ2: requirements.txtを作成

**Intel/AMD/ARM64共通:**
```
Flask==3.0.0
```

#### ステップ3: app.pyを作成

**Intel/AMD/ARM64共通:**
```python
from flask import Flask
import platform

app = Flask(__name__)

@app.route('/')
def hello():
    arch = platform.machine()
    return f'''
    <h1>Hello from Docker!</h1>
    <p>This Flask app is running in a container.</p>
    <p><strong>Architecture:</strong> {arch}</p>
    '''

@app.route('/api/data')
def data():
    return {
        'message': 'Hello from API',
        'status': 'success',
        'architecture': platform.machine()
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

#### ステップ4: Dockerfileを作成

**Intel/AMDの場合:**
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

**ARM64の場合（推奨）:**
```dockerfile
# ARM64ネイティブのPython 3.11を使用
FROM --platform=linux/arm64 python:3.11-slim

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

**Intel/AMD/ARM64共通:**
```
__pycache__
*.pyc
*.pyo
.git
.env
venv/
```

#### ステップ6: イメージをビルド

**Intel/AMDの場合:**
```powershell
docker build -t flask-app .
```

**ARM64の場合:**
```powershell
# ARM64ネイティブビルド（推奨）
docker build --platform linux/arm64 -t flask-app .
```

#### ステップ7: コンテナを実行

**Intel/AMD/ARM64共通:**
```powershell
docker run -d -p 5000:5000 --name my-flask-app flask-app
```

**確認:**

ブラウザで http://localhost:5000 にアクセス
→ 「Hello from Docker!」と **Architecture** が表示されればOK！
- Intel/AMD: `x86_64`
- ARM64: `aarch64`

http://localhost:5000/api/data にアクセス
→ JSON が表示されればOK！

**ログを確認:**
```powershell
docker logs my-flask-app
```

**停止:**
```powershell
docker stop my-flask-app
docker rm my-flask-app
```

### Dockerfileのベストプラクティス

#### 1. .dockerignoreを使う

不要なファイルをコピーしない:

**Intel/AMD/ARM64共通:**
```
.git
.gitignore
__pycache__
*.pyc
venv/
node_modules/
.env
*.log
Thumbs.db
```

#### 2. レイヤーを最小化

**Intel/AMD/ARM64共通:**
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

**Intel/AMD/ARM64共通:**
```dockerfile
# 依存関係を先にコピー
COPY requirements.txt .
RUN pip install -r requirements.txt

# アプリケーションコードは後で
COPY . .
```

#### 4. マルチアーキテクチャ対応（高度）

複数のアーキテクチャで動作するイメージ:

```dockerfile
# ビルドプラットフォームに応じて自動選択
FROM --platform=$BUILDPLATFORM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

ビルド時:
```powershell
# 複数プラットフォーム対応ビルド
docker buildx build --platform linux/amd64,linux/arm64 -t my-app .
```

💡 **高度な機能:** Docker Buildxを使うと複数アーキテクチャ対応イメージを一度にビルドできます

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

**Intel/AMD/ARM64共通:**
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

**ARM64の場合の追加設定:**
```yaml
version: '3.8'

services:
  サービス名:
    image: イメージ名
    platform: linux/arm64  # ARM64を明示的に指定
    # または
    # platform: linux/amd64  # エミュレーション
```

### 実践1: WordPress + MySQLを構築

#### ステップ1: プロジェクトを作成

```powershell
New-Item -ItemType Directory -Path $HOME\docker-wordpress
cd $HOME\docker-wordpress
```

#### ステップ2: docker-compose.ymlを作成

**Intel/AMDの場合:**
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

**ARM64の場合（MySQL代替が必要）:**
```yaml
version: '3.8'

services:
  # MariaDB（ARM64対応）
  db:
    image: mariadb:11
    platform: linux/arm64
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppassword

  # WordPress（ARM64対応）
  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    platform: linux/arm64
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

💡 **ARM64注意:** MySQL 8.0の公式イメージはARM64非対応のため、MariaDBを使用します

#### ステップ3: 起動

**Intel/AMD/ARM64共通:**
```powershell
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
```powershell
docker compose ps
```

**ブラウザで確認（Intel/AMD/ARM64共通）:**
http://localhost:8080

WordPressの初期設定画面が表示されればOK！

#### ステップ5: 停止と削除

**Intel/AMD/ARM64共通:**
```powershell
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

```powershell
New-Item -ItemType Directory -Path $HOME\docker-flask-postgres
cd $HOME\docker-flask-postgres
```

#### ステップ2: requirements.txtを作成

**Intel/AMD/ARM64共通:**
```
Flask==3.0.0
psycopg2-binary==2.9.9
```

#### ステップ3: app.pyを作成

**Intel/AMD/ARM64共通:**
```python
from flask import Flask, jsonify
import psycopg2
import os
import platform

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
    arch = platform.machine()
    return f'<h1>Flask + PostgreSQL in Docker!</h1><p>Architecture: {arch}</p>'

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
            'version': db_version[0],
            'architecture': platform.machine()
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

**Intel/AMDの場合:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

**ARM64の場合:**
```dockerfile
FROM --platform=linux/arm64 python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

#### ステップ5: docker-compose.ymlを作成

**Intel/AMDの場合:**
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

**ARM64の場合:**
```yaml
version: '3.8'

services:
  # PostgreSQLデータベース（ARM64対応）
  db:
    image: postgres:15
    platform: linux/arm64
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

  # Flaskアプリ（ARM64ネイティブ）
  web:
    build:
      context: .
      platforms:
        - linux/arm64
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

💡 **ARM64良いニュース:** PostgreSQLはARM64に完全対応しています！

#### ステップ6: 起動

**Intel/AMD/ARM64共通:**
```powershell
docker compose up -d
```

#### ステップ7: 確認

http://localhost:5000 → Flask起動確認
http://localhost:5000/db-test → DB接続確認

**ログを確認:**
```powershell
docker compose logs -f
```

### Docker Composeコマンド早見表

**Intel/AMD/ARM64共通:**
```powershell
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

```powershell
New-Item -ItemType Directory -Path $HOME\docker-data-science
cd $HOME\docker-data-science
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

```powershell
New-Item -ItemType Directory -Path notebooks
New-Item -ItemType Directory -Path data
```

#### ステップ3: requirements.txtを作成

**Intel/AMD/ARM64共通:**
```
jupyter==1.0.0
pandas==2.1.3
numpy==1.26.2
matplotlib==3.8.2
seaborn==0.13.0
scikit-learn==1.3.2
```

💡 **ARM64注意:** これらのライブラリはすべてARM64対応済みです

#### ステップ4: Dockerfileを作成

**Intel/AMDの場合:**
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

**ARM64の場合:**
```dockerfile
FROM --platform=linux/arm64 python:3.11

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

**Intel/AMDの場合:**
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

**ARM64の場合:**
```yaml
version: '3.8'

services:
  jupyter:
    build:
      context: .
      platforms:
        - linux/arm64
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/workspace/notebooks
      - ./data:/workspace/data
    environment:
      - JUPYTER_ENABLE_LAB=yes
```

#### ステップ6: 起動

**Intel/AMD/ARM64共通:**
```powershell
docker compose up -d
```

**ARM64の場合:** 初回ビルドは時間がかかる場合があります（5〜10分）

#### ステップ7: アクセス

**ブラウザで（Intel/AMD/ARM64共通）:**
http://localhost:8888

Jupyter Notebookが開きます！

#### ステップ8: 使ってみる

1. 「New」→「Python 3」で新しいノートブック作成
2. 以下を実行:

**Intel/AMD/ARM64共通:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform

print(f"Running on: {platform.machine()}")

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
- Intel/AMD: `Running on: x86_64`
- ARM64: `Running on: aarch64`

#### ステップ9: ファイルの永続化

ノートブックを保存すると、`notebooks\`フォルダに保存されます。
コンテナを削除しても、ファイルは残ります。

---

## 💻 VSCodeとDockerの連携

VSCodeでDockerコンテナ内を直接編集できるようにします。

### ステップ1: 拡張機能をインストール

#### 1-1: VSCodeを開く

#### 1-2: 拡張機能を検索

`Ctrl + Shift + X` で拡張機能を開く

#### 1-3: 以下をインストール

**Intel/AMD/ARM64共通:**

1. **「Docker」**
   - 作成者: Microsoft
   - Dockerコンテナ・イメージを管理

2. **「Dev Containers」**
   - 作成者: Microsoft
   - コンテナ内で開発

3. **「WSL」**
   - 作成者: Microsoft
   - WSL連携を強化

インストール後、VSCodeを再起動

### ステップ2: Dockerサイドバーを確認

左サイドバーに **クジラアイコン** が追加されます。

クリックすると:
- Containers: 実行中のコンテナ一覧
- Images: イメージ一覧
- Volumes: ボリューム一覧

### ステップ3: コンテナ内で開発

#### 方法1: 既存のコンテナに接続

**Intel/AMD/ARM64共通:**

1. **左サイドバーのDockerアイコン** をクリック
2. **Containers** セクションで実行中のコンテナを右クリック
3. **「Attach Visual Studio Code」** を選択

新しいVSCodeウィンドウが開き、コンテナ内が表示されます！

#### 方法2: Dev Containerを使う

プロジェクトに`.devcontainer\devcontainer.json`を作成。

**例: Python開発環境（Intel/AMD）**

`.devcontainer\devcontainer.json`:
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

**例: Python開発環境（ARM64）**

`.devcontainer\devcontainer.json`:
```json
{
  "name": "Python Dev Container (ARM64)",
  "image": "python:3.11",
  "runArgs": ["--platform=linux/arm64"],
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

**使い方（Intel/AMD/ARM64共通）:**
1. `Ctrl + Shift + P`
2. 「Dev Containers: Reopen in Container」
3. VSCodeがコンテナ内で再起動

### ステップ4: WSL連携

VSCodeでWSL内のプロジェクトを開くこともできます。

**方法（Intel/AMD/ARM64共通）:**
1. `Ctrl + Shift + P`
2. 「WSL: Connect to WSL」
3. WSL内のフォルダを開く

### ステップ5: Dockerfileを編集

VSCodeでDockerfileを開くと:
- シンタックスハイライト
- 補完機能
- エラーチェック

が自動的に有効になります。

### ステップ6: docker-compose.ymlを編集

VSCodeでdocker-compose.ymlを開くと:
- YAMLのシンタックスハイライト
- インデントのチェック
- スキーマ検証

が有効になります。

---

## 🔥 ARM64特有の注意事項

ARM64版Windowsを使用している場合の重要なポイントをまとめます。

### 1. イメージの互換性

#### ARM64ネイティブ対応イメージ（推奨）

以下のイメージはARM64に完全対応:

**✅ 完全対応:**
- `python:3.x`
- `node:x`
- `ubuntu`
- `debian`
- `nginx`
- `postgres:x`
- `redis:x`
- `mariadb:x`
- `mongo:x`

**使用例:**
```powershell
docker pull --platform linux/arm64 python:3.11
docker pull --platform linux/arm64 postgres:15
```

#### ARM64非対応イメージ（エミュレーション必要）

以下のイメージはx64のみ（エミュレーションで動作）:

**⚠️ エミュレーション:**
- `mysql:8.0`（MariaDBを推奨）
- 一部の古いイメージ
- カスタムビルドイメージ

**エミュレーションで使用:**
```powershell
docker pull --platform linux/amd64 mysql:8.0
docker run --platform linux/amd64 mysql:8.0
```

💡 **パフォーマンス:** エミュレーションは動作しますが、ネイティブより遅くなります

### 2. プラットフォームの指定方法

#### コマンドライン

```powershell
# ARM64ネイティブ（推奨）
docker run --platform linux/arm64 イメージ名

# x64エミュレーション
docker run --platform linux/amd64 イメージ名

# イメージ取得
docker pull --platform linux/arm64 イメージ名
```

#### Dockerfile

```dockerfile
# ARM64を明示的に指定
FROM --platform=linux/arm64 python:3.11

# または、ビルド時のプラットフォームを使用
FROM --platform=$BUILDPLATFORM python:3.11
```

#### docker-compose.yml

```yaml
version: '3.8'

services:
  app:
    image: python:3.11
    platform: linux/arm64  # ARM64を指定
```

### 3. パフォーマンス最適化

#### ARM64ネイティブを優先

```powershell
# 悪い例（エミュレーション）
docker run --platform linux/amd64 python:3.11

# 良い例（ネイティブ）
docker run --platform linux/arm64 python:3.11
```

#### マルチステージビルドの活用

```dockerfile
# ビルドステージ（ARM64ネイティブ）
FROM --platform=linux/arm64 python:3.11 as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# 本番ステージ（ARM64ネイティブ）
FROM --platform=linux/arm64 python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
```

### 4. よくある問題と解決方法

#### 問題1: `exec format error`

**原因:** x64イメージをプラットフォーム指定なしで実行

**解決:**
```powershell
# エラーが出る
docker run イメージ名

# 解決方法
docker run --platform linux/arm64 イメージ名
```

#### 問題2: ビルドが遅い

**原因:** エミュレーションを使用している

**解決:**
- ARM64ネイティブイメージを使用
- ビルドキャッシュを活用
- マルチステージビルドを使用

#### 問題3: MySQLが動かない

**原因:** MySQL 8.0はARM64非公式

**解決:**
```yaml
# MySQL の代わりにMariaDBを使用
services:
  db:
    image: mariadb:11
    platform: linux/arm64
```

### 5. ARM64確認コマンド集

```powershell
# システムアーキテクチャ確認
Get-ComputerInfo | Select-Object OsArchitecture

# WSLアーキテクチャ確認
wsl uname -m

# コンテナ内でアーキテクチャ確認
docker run --rm ubuntu uname -m

# イメージのアーキテクチャ確認
docker image inspect イメージ名 | Select-String "Architecture"

# 実行中コンテナのアーキテクチャ確認
docker exec コンテナ名 uname -m
```

### 6. ARM64対応チェックリスト

プロジェクト開始時に確認:

- [ ] 使用するベースイメージがARM64対応か確認
- [ ] Dockerfileで `--platform=linux/arm64` を指定
- [ ] docker-compose.ymlで `platform: linux/arm64` を指定
- [ ] MySQL → MariaDBなど代替が必要か確認
- [ ] ビルド時に `--platform` オプションを使用
- [ ] パフォーマンステストを実施

### 7. 推奨構成（ARM64）

```yaml
# docker-compose.yml（ARM64最適化版）
version: '3.8'

services:
  web:
    build:
      context: .
      platforms:
        - linux/arm64
    platform: linux/arm64
    ports:
      - "5000:5000"

  db:
    image: mariadb:11
    platform: linux/arm64
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: mydb

  cache:
    image: redis:7
    platform: linux/arm64
```

---

## 🐛 トラブルシューティング

### Docker Desktopが起動しない

#### 症状: 起動時にエラー

**対処法1: WSL2を確認（Intel/AMD/ARM64共通）**
```powershell
wsl --list --verbose
```

VERSIONが2であることを確認

**対処法2: WSL2を更新（Intel/AMD/ARM64共通）**
```powershell
wsl --update
```

**対処法3（ARM64のみ）: ARM64版カーネルを確認**
- WSL2カーネルがARM64版かどうか確認
- 必要に応じて https://aka.ms/wsl2kernelarm64 から再インストール

**対処法4: Docker Desktopを再インストール（Intel/AMD/ARM64共通）**
1. アンインストール
2. PCを再起動
3. 正しいアーキテクチャ版を再インストール
   - Intel/AMD: x64版
   - ARM64: ARM64版

**対処法5: Windowsを再起動（Intel/AMD/ARM64共通）**

### WSL2が起動しない

#### 症状: WSL2関連のエラー

**対処法1: 仮想化を確認（Intel/AMDのみ）**
タスクマネージャー → パフォーマンス → CPU → 「仮想化: 有効」

**ARM64の場合:** この確認は不要（常に有効）

**対処法2: WSL機能を再有効化（Intel/AMD/ARM64共通）**
管理者権限のPowerShellで:
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

PCを再起動

**対処法3: WSLカーネルを更新（アーキテクチャ別）**

**Intel/AMDの場合:**
https://aka.ms/wsl2kernel

**ARM64の場合:**
https://aka.ms/wsl2kernelarm64

### コンテナが起動しない

#### 症状: `docker run` が失敗

**対処法1: ログを確認（Intel/AMD/ARM64共通）**
```powershell
docker logs コンテナ名
```

**対処法2: ポートの競合を確認（Intel/AMD/ARM64共通）**
```powershell
# 使用中のポートを確認
netstat -ano | findstr :ポート番号

# 例: ポート8080
netstat -ano | findstr :8080
```

他のプロセスが使っている場合、停止するか別のポートを使う

**対処法3（ARM64のみ）: プラットフォームを確認**
```powershell
# ARM64ネイティブイメージを使用
docker run --platform linux/arm64 イメージ名

# エラーが出る場合はエミュレーション
docker run --platform linux/amd64 イメージ名
```

**対処法4: イメージを再取得（Intel/AMD/ARM64共通）**
```powershell
# Intel/AMD
docker pull イメージ名

# ARM64
docker pull --platform linux/arm64 イメージ名
```

### `exec format error`（ARM64特有）

#### 症状: コンテナ起動時にフォーマットエラー

**原因:** x64イメージをARM64で実行しようとしている

**対処法1: ARM64イメージを使用**
```powershell
# 正しい方法
docker run --platform linux/arm64 イメージ名
```

**対処法2: x64をエミュレーション**
```powershell
# エミュレーションで実行（遅い）
docker run --platform linux/amd64 イメージ名
```

**対処法3: Dockerfileを修正**
```dockerfile
# ARM64を明示的に指定
FROM --platform=linux/arm64 python:3.11
```

### イメージのビルドが失敗

#### 症状: `docker build` でエラー

**対処法1: キャッシュを使わずビルド（Intel/AMD/ARM64共通）**
```powershell
docker build --no-cache -t イメージ名 .
```

**対処法2（ARM64のみ）: プラットフォームを指定**
```powershell
# ARM64ネイティブビルド
docker build --platform linux/arm64 -t イメージ名 .
```

**対処法3: Dockerfileの文字コード確認（Intel/AMD/ARM64共通）**
- UTF-8で保存されているか確認
- BOM（Byte Order Mark）なしで保存

**対処法4: 改行コードを確認（Intel/AMD/ARM64共通）**
- Dockerfileは **LF** を使用（CRLFではない）
- VSCodeで右下の「CRLF」をクリック → 「LF」に変更

### コンテナが見つからない

#### 症状: `Error: No such container`

**対処法: すべてのコンテナを確認（Intel/AMD/ARM64共通）**
```powershell
docker ps -a
```

停止中のコンテナも含めてすべて表示されます。

### ディスク容量不足

#### 症状: `no space left on device`

**対処法1: 未使用データを削除（Intel/AMD/ARM64共通）**
```powershell
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

**対処法2: 個別に削除（Intel/AMD/ARM64共通）**
```powershell
# 停止中のコンテナを削除
docker container prune

# 未使用イメージを削除
docker image prune -a

# 未使用ボリュームを削除
docker volume prune
```

**対処法3: ディスクイメージのサイズを確認（Intel/AMD/ARM64共通）**
Docker Desktop → Settings → Resources → Disk image size

### パス問題（Windows特有）

#### 症状: パスが正しく認識されない

**対処法: パス表記を統一（Intel/AMD/ARM64共通）**

**PowerShellの場合:**
```powershell
# 推奨: 自動変換
docker run -v ${PWD}:/app ...

# または絶対パス（スラッシュ）
docker run -v /c/Users/YourName/project:/app ...
```

**コマンドプロンプトの場合:**
```cmd
# 相対パス
docker run -v %cd%:/app ...
```

### ファイアウォール問題

#### 症状: ネットワーク接続エラー

**対処法: Windowsファイアウォールを確認（Intel/AMD/ARM64共通）**
1. **設定** → **更新とセキュリティ** → **Windowsセキュリティ**
2. **ファイアウォールとネットワーク保護**
3. **アプリケーションをファイアウォール経由で許可する**
4. **Docker Desktop** が許可されているか確認

### メモリ不足

#### 症状: コンテナが頻繁にクラッシュ

**対処法: メモリ割り当てを増やす**

**Intel/AMDの場合:**
1. Docker Desktop → Settings → Resources
2. **Memory** スライダーを調整
3. Apply & Restart

**推奨設定:**
- 8GBのPC → 3-4GB
- 16GBのPC → 6-8GB
- 32GB以上 → 10-12GB

**ARM64の場合:**
- 8GBのPC → 3-4GB（エミュレーション考慮）
- 16GBのPC → 6-8GB
- 32GB以上 → 10-14GB

💡 **ARM64注意:** エミュレーション時により多くのメモリを使用するため、やや多めに割り当てます

### パフォーマンスが遅い（ARM64特有）

#### 症状: コンテナの動作が遅い

**対処法1: ARM64ネイティブイメージを使用**
```powershell
# 遅い（エミュレーション）
docker run --platform linux/amd64 イメージ名

# 速い（ネイティブ）
docker run --platform linux/arm64 イメージ名
```

**対処法2: WSL2の最適化**

`.wslconfig` ファイルを作成（`%USERPROFILE%\.wslconfig`）:
```ini
[wsl2]
memory=8GB
processors=4
swap=4GB
localhostForwarding=true
```

**対処法3: Docker Desktopのリソース増加**
- CPUs: 総数の半分以上
- Memory: 8GB以上（ARM64推奨）

---

## 🙋 よくある質問（FAQ）

### Q1: DockerとVMの違いは？

**A（Intel/AMD/ARM64共通）:**

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

**A（Intel/AMD/ARM64共通）:**

**Docker Desktop（Windows/Mac）:**
- GUIアプリ
- 初心者に優しい
- WSL2統合（Windows）
- 有料（大企業の場合）

**Docker Engine（Linux）:**
- CLIのみ
- 無料
- サーバーで使われる

Windowsでは**Docker Desktop**を使います。

### Q3: ARM64版Windowsでも問題なく使えますか？

**A（ARM64専用）:**

はい、問題なく使えます！ただし注意点があります:

**✅ 完全対応:**
- Docker Desktop自体はARM64に完全対応
- 多くの主要イメージがARM64ネイティブ対応

**⚠️ 注意点:**
- 一部のイメージはx64のみ（エミュレーション必要）
- エミュレーション時はパフォーマンスが落ちる
- `--platform` オプションの指定が必要な場合がある

**推奨:**
- ARM64ネイティブイメージを優先的に使用
- MySQL → MariaDBなど、代替イメージを検討

### Q4: Intel/AMD版とARM64版の違いは？

**A（アーキテクチャ比較）:**

**Intel/AMD（x64）:**
- ✅ すべてのイメージが動作
- ✅ エミュレーション不要
- ✅ 豊富な情報・サポート

**ARM64:**
- ✅ 主要イメージはネイティブ対応
- ⚠️ 一部イメージはエミュレーション必要
- ✅ ネイティブ動作時は高効率
- ⚠️ `--platform` 指定が必要な場合あり

**結論:** どちらも実用的に使えます！

### Q5: コンテナとイメージの違いは？

**A（Intel/AMD/ARM64共通）:**

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

### Q6: コンテナのデータは消えますか？

**A（Intel/AMD/ARM64共通）:**

はい、デフォルトでは消えます。

**対策:**
- **ボリューム** を使う
- **バインドマウント** を使う

```powershell
# ボリュームを使う
docker run -v my-volume:/data ...

# バインドマウント（Windows）
docker run -v ${PWD}:/data ...
```

### Q7: Dockerは無料ですか？

**A（Intel/AMD/ARM64共通）:**

基本的に無料です。

**無料:**
- 個人利用
- 小規模企業（従業員250人未満）
- 教育機関

**有料:**
- 大企業（従業員250人以上）
- 年間売上$10M以上

詳細: https://www.docker.com/pricing/

### Q8: Dockerのセキュリティは大丈夫？

**A（Intel/AMD/ARM64共通）:**

適切に使えば安全です。

**セキュリティのポイント:**
- 公式イメージを使う
- イメージを定期的に更新
- 秘密情報を環境変数で管理
- 不要な権限を与えない

### Q9: 本番環境でDockerを使えますか？

**A（Intel/AMD/ARM64共通）:**

はい、多くの企業で使われています。

**使用例:**
- Netflix
- Uber
- Spotify
- PayPal

**メリット:**
- スケーリングが簡単
- デプロイが高速
- 環境の一貫性

### Q10: KubernetesとDockerの関係は？

**A（Intel/AMD/ARM64共通）:**

**Docker:**
- コンテナ実行環境
- 単一マシンでの管理

**Kubernetes:**
- コンテナオーケストレーション
- 複数マシンでの管理
- Dockerコンテナを大規模に運用

**関係:**
Kubernetesは Dockerコンテナを管理するツール

### Q11: Dockerが遅いのですが...

**A:**

リソース設定を調整しましょう。

Docker Desktop → Settings → Resources

**Intel/AMDの推奨設定:**
- CPUs: 総数の半分
- Memory: 
  - 8GBのPC → 4GB
  - 16GBのPC → 6-8GB
- Disk: 十分な空き容量

**ARM64の推奨設定:**
- CPUs: 総数の半分以上
- Memory:
  - 8GBのPC → 4GB
  - 16GBのPC → 6-10GB
- Disk: 十分な空き容量

**ARM64追加対策:**
- ARM64ネイティブイメージを使用
- エミュレーションを避ける
- WSL2を最適化（.wslconfig）

### Q12: Dockerfileとdocker-compose.ymlの違いは？

**A（Intel/AMD/ARM64共通）:**

**Dockerfile:**
- 1つのイメージを作る設計書
- イメージのビルド方法を定義

**docker-compose.yml:**
- 複数のコンテナを管理する設定ファイル
- サービスの組み合わせを定義

**使い分け:**
- 1つのアプリ → Dockerfile
- 複数のサービス → docker-compose.yml

### Q13: WSL2とDocker Desktopの関係は？

**A（Intel/AMD/ARM64共通）:**

**WSL2:**
- Linuxカーネルを提供
- Dockerのバックエンド

**Docker Desktop:**
- GUIツール
- WSL2上でDockerを動かす
- Windows統合を提供

**関係:**
Docker Desktop は WSL2 を使って動作します

### Q14: パスの書き方がわかりません

**A（Intel/AMD/ARM64共通）:**

**PowerShell:**
```powershell
# カレントディレクトリ
${PWD}

# ホームディレクトリ
$HOME

# 絶対パス
/c/Users/YourName/project
```

**コマンドプロンプト:**
```cmd
# カレントディレクトリ
%cd%

# ホームディレクトリ
%USERPROFILE%
```

**Docker内（Linux形式）:**
```
/app
/data
/workspace
```

### Q15: `--platform`オプションはいつ使う？（ARM64関連）

**A（ARM64ユーザー向け）:**

**必須の場合:**
- イメージがARM64非対応で、エミュレーションが必要
- マルチアーキテクチャイメージで明示的に指定したい

**推奨の場合:**
- ARM64ネイティブ動作を確実にしたい
- パフォーマンスを最適化したい

**例:**
```powershell
# ARM64ネイティブ（推奨）
docker run --platform linux/arm64 python:3.11

# x64エミュレーション（必要な場合のみ）
docker run --platform linux/amd64 mysql:8.0
```

**デフォルト動作:**
- `--platform` なし → 自動選択（通常はARM64）
- エラーが出たら `--platform` を明示的に指定

---

## 📚 参考リンク集

### 公式ドキュメント
- [Docker公式サイト](https://www.docker.com/)
- [Docker Docs](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [WSL2ドキュメント](https://docs.microsoft.com/ja-jp/windows/wsl/)
- [Docker on ARM64](https://docs.docker.com/desktop/arm/)

### ARM64特化リソース
- [Docker Hub ARM64イメージ一覧](https://hub.docker.com/search?q=&type=image&architecture=arm64)
- [Windows on ARM](https://learn.microsoft.com/ja-jp/windows/arm/)

### 学習リソース
- [Docker入門（日本語）](https://docs.docker.jp/get-started/toc.html)
- [Play with Docker](https://labs.play-with-docker.com/)（ブラウザで試せる）

### コミュニティ
- [Docker Community](https://www.docker.com/community/)
- [Stack Overflow - Docker](https://stackoverflow.com/questions/tagged/docker)

---

## ✅ 最終チェックリスト

### システム確認
- [ ] Windowsバージョンが要件を満たしている
- [ ] プロセッサアーキテクチャを確認済み
  - [ ] Intel/AMD（x64）
  - [ ] ARM64（Snapdragonなど）
- [ ] 仮想化が有効（Intel/AMDの場合）
- [ ] ARM64の場合、ARM64版をダウンロード

### WSL2設定
- [ ] WSL2がインストールされている
- [ ] Ubuntuがインストールされている
- [ ] `wsl --list --verbose` でVERSION 2が確認できる
- [ ] **ARM64の場合:** `uname -m` で `aarch64` と表示される

### Docker Desktop
- [ ] Docker Desktopがインストールされている
  - [ ] Intel/AMD: x64版
  - [ ] ARM64: ARM64版
- [ ] `docker --version` でバージョン確認できる
- [ ] `docker run hello-world` が成功する
  - [ ] Intel/AMD: そのまま実行
  - [ ] ARM64: `--platform linux/arm64` で実行
- [ ] タスクバーにクジラアイコンが表示される
- [ ] WSL2統合が有効

### 基本操作
- [ ] コンテナを起動できる
- [ ] コンテナを停止・削除できる
- [ ] イメージを取得できる
- [ ] ログを確認できる
- [ ] **ARM64の場合:** `--platform` オプションを理解している

### Dockerfile
- [ ] Dockerfileを作成できる
- [ ] イメージをビルドできる
  - [ ] Intel/AMD: 通常のビルド
  - [ ] ARM64: `--platform linux/arm64` でビルド
- [ ] カスタムイメージを実行できる

### Docker Compose
- [ ] docker-compose.ymlを作成できる
- [ ] 複数コンテナを起動できる
- [ ] サービス間で通信できる
- [ ] **ARM64の場合:** `platform: linux/arm64` を設定

### VSCode連携
- [ ] Docker拡張機能をインストールした
- [ ] コンテナ一覧を確認できる
- [ ] Dev Containersの概念を理解した
- [ ] WSL拡張機能をインストールした

### ARM64特有（該当する場合）
- [ ] ARM64ネイティブイメージを優先している
- [ ] `--platform` オプションの使い方を理解している
- [ ] MySQL → MariaDBなど代替を把握している
- [ ] パフォーマンス最適化を実施している

---

## 🎉 おめでとうございます！

このガイドを完了したあなたは、もう立派なDocker使いです！

**これからできること:**
- ✅ 開発環境を簡単に構築
- ✅ チームで同じ環境を共有
- ✅ 様々な技術を気軽に試せる
- ✅ 本番環境へのデプロイ準備
- ✅ WindowsでもMacでも同じ環境
- ✅ **Intel/AMD/ARM64すべてに対応**

**次のステップ:**
1. 実際のプロジェクトでDockerを使う
2. Docker Composeで複雑な環境を構築
3. Kubernetes（k8s）を学習
4. CI/CDパイプラインでDockerを活用

**Windows特有のヒント:**
- WSL2を活用しよう
- パスの表記に注意
- VSCodeのWSL連携を使おう
- PowerShellを使いこなそう

**ARM64ユーザーへのヒント:**
- ARM64ネイティブイメージを優先
- `--platform` を使いこなそう
- エミュレーションは最小限に
- パフォーマンスを意識した選択を

**継続的な学習のために:**
- 毎日少しずつDockerを使う
- 公式ドキュメントを読む
- コミュニティに参加する
- 実践あるのみ！

あなたの開発ライフがより快適になりますように！

**Happy Dockering on Windows (Intel/AMD/ARM64)! 🐳**

---

**バージョン:** 2.0（Windows完全版 - Intel/AMD/ARM64対応）  
**対応OS:** Windows 10 バージョン 2004以降、Windows 11  
**対応アーキテクチャ:** Intel x64, AMD x64, ARM64  
**前提:** Git/GitHub導入完了、WSL2セットアップ完了  
**最終更新:** 2025年10月
