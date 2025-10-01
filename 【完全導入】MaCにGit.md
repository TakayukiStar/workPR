# Mac初心者のためのVSCode×GitHub完全ガイド【完全版】

## 🎯 このガイドについて

このガイド**だけ**で、MacでのGit/GitHub/VSCodeの導入がすべて完了します。
他の資料を見る必要は一切ありません。

**対象者:**
- Macユーザー（Intel/Apple Silicon両対応）
- Git/GitHub初心者
- VSCode初心者
- プログラミング初心者

**完了後にできること:**
- ✅ Gitでコードをバージョン管理
- ✅ GitHubでコードを保存・共有
- ✅ VSCodeでの快適な開発
- ✅ チーム開発の基礎

---

## 📋 目次
1. [事前準備と確認](#事前準備と確認)
2. [Gitのインストール](#gitのインストール)
3. [GitHubアカウント作成](#githubアカウント作成)
4. [VSCodeのインストールと設定](#vscodeのインストールと設定)
5. [SSHキーの設定（推奨）](#sshキーの設定推奨)
6. [リポジトリのクローン](#リポジトリのクローン)
7. [基本的なGit操作](#基本的なgit操作)
8. [ファイルのアップロード実践](#ファイルのアップロード実践)
9. [トラブルシューティング](#トラブルシューティング)
10. [よくある質問（FAQ）](#よくある質問faq)
11. [次のステップ](#次のステップ)

---

## 🎯 事前準備と確認

### 必要なもの
- ✅ macOS搭載のMac（どのバージョンでもOK）
- ✅ インターネット接続
- ✅ メールアドレス（Gmail、Yahoo!メールなど）
- ✅ 管理者権限（あなたのMacのパスワードを知っている）
- ✅ 30分〜1時間の時間

### 自分のMacの情報を確認

作業を始める前に、以下を確認しておきましょう：

#### 1. Macのチップ（CPU）を確認

1. 画面左上の **🍎 リンゴマーク** をクリック
2. **「このMacについて」** を選択
3. ウィンドウが開いたら、以下を確認：

**「チップ」という項目がある場合:**
- `Apple M1` / `Apple M2` / `Apple M3` など → **Apple Silicon Mac**

**「プロセッサ」という項目がある場合:**
- `Intel Core i5` / `Intel Core i7` など → **Intel Mac**

📝 **メモ:** ここで確認した情報は後で使います。

#### 2. macOSのバージョンを確認

同じ画面で確認できます：
- `macOS Sonoma 14.x`
- `macOS Ventura 13.x`
- `macOS Monterey 12.x`
- `macOS Big Sur 11.x` など

💡 **推奨:** macOS 11 Big Sur以降（それより古くても動作しますが、アップデート推奨）

#### 3. ストレージ容量を確認

「このMacについて」→「ストレージ」タブで確認
- **必要な空き容量:** 最低5GB（推奨10GB以上）

---

## 🔧 Gitのインストール

### ステップ1: ターミナルを開く

ターミナルは、Macに命令を出すためのアプリです。

**開き方（3つの方法、どれでもOK）:**

**方法1: Spotlight検索（最も簡単）**
1. `Command（⌘） + Space` を同時に押す
2. 「ターミナル」と入力
3. 「ターミナル.app」が表示されたら `Return（Enter）` を押す

**方法2: Finderから**
1. Finderを開く
2. メニューバーの「移動」→「ユーティリティ」
3. 「ターミナル」をダブルクリック

**方法3: Launchpadから**
1. Dock（画面下のバー）の「Launchpad」をクリック（ロケットのアイコン）
2. 「その他」フォルダを開く
3. 「ターミナル」をクリック

💡 **ターミナルの画面:** 黒い（または白い）背景に文字が表示される画面が開きます。

### ステップ2: Gitがインストール済みか確認

ターミナルに以下を入力して `Return` を押します：

```bash
git --version
```

**💡 入力のコツ:**
- コピー＆ペーストでOK（`Command + C` でコピー、`Command + V` でペースト）
- 入力後は必ず `Return` を押す

**結果のパターン:**

#### パターンA: バージョンが表示される
```
git version 2.39.2 (Apple Git-143)
```
このように表示されたら → **✅ すでにインストール済み！[ステップ8: Gitの初期設定](#ステップ8-gitの初期設定)へジャンプ**

#### パターンB: コマンドが見つからない
```
zsh: command not found: git
```
または
```
bash: git: command not found
```
このように表示されたら → **次のステップへ進む**

#### パターンC: ポップアップが表示される

**「"git"コマンドを実行するには、コマンドライン・デベロッパツールが必要です。今すぐインストールしますか？」**

このポップアップが出たら、2つの選択肢があります：

**👉 選択肢1: Xcodeコマンドラインツールをインストール（推奨・簡単）**

1. **「インストール」ボタン** をクリック
2. 使用許諾契約が表示されたら **「同意する」** をクリック
3. ダウンロードとインストールが始まります（**10〜30分かかります**）
4. 進行状況バーが表示されます（MacBookの電源を入れたままにしてください）
5. 「ソフトウェアがインストールされました。」と表示されたら **「完了」** をクリック
6. ターミナルに戻り、再度 `git --version` を実行
7. バージョンが表示されたら **✅ 完了！[ステップ8: Gitの初期設定](#ステップ8-gitの初期設定)へ**

**👉 選択肢2: Homebrewでインストール（柔軟・開発者向け）**

1. **「キャンセル」** をクリック
2. 次のステップ（Homebrewのインストール）へ進む

**どちらを選ぶべき？**
- 初心者・時間を節約したい → **選択肢1（Xcodeコマンドラインツール）**
- 今後他の開発ツールも使いたい → **選択肢2（Homebrew）**

### ステップ3: Homebrewをインストール（選択肢2を選んだ場合）

Homebrewは、Macでソフトウェアを簡単にインストールできるツールです。

#### 3-1: Homebrewのインストールコマンドを実行

ターミナルに以下をコピー＆ペーストして `Return` を押します：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 3-2: パスワードを入力

```
Password:
```
このように表示されたら：

1. **Macのログインパスワード** を入力
2. ⚠️ **重要:** 入力中は画面に何も表示されません（セキュリティのため）
3. パスワードを入力し終わったら `Return` を押す

#### 3-3: インストールの確認

```
Press RETURN/ENTER to continue or any other key to abort:
```
このように表示されたら、`Return` を押します。

#### 3-4: ダウンロードとインストールを待つ

- **所要時間:** 5〜15分
- 画面に色々な文字が流れますが、正常です
- MacBookの電源を入れたままにしてください

#### 3-5: インストール完了の確認

画面の最後に以下のようなメッセージが表示されます：

```
==> Installation successful!
==> Next steps:
```

**⚠️ 超重要:** ここからの手順は、**Apple Silicon MacとIntel Macで異なります**

---

#### 【Apple Silicon Mac（M1/M2/M3など）の場合】

画面に以下のように表示されます：

```
==> Next steps:
- Run these two commands in your terminal to add Homebrew to your PATH:
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
```

**👉 この2つのコマンドを必ず実行してください！**

**手順:**

1. **1つ目のコマンドをコピー＆ペーストして実行:**
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```
`Return` を押す（何も表示されませんが正常です）

2. **2つ目のコマンドをコピー＆ペーストして実行:**
```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```
`Return` を押す（何も表示されませんが正常です）

💡 **なぜ必要？** このコマンドを実行しないと、Homebrewが使えません！

---

#### 【Intel Macの場合】

画面に以下のように表示されます：

```
==> Next steps:
- Run `brew help` to get started
```

**通常は追加作業不要ですが、念のため次のステップで確認します。**

---

### ステップ4: Homebrewのインストール確認

ターミナルで以下を実行：

```bash
brew --version
```

**成功の場合:**
```
Homebrew 4.2.0
```
このようにバージョンが表示されればOK！

**失敗の場合（`command not found: brew`）:**

**対処法1: ターミナルを再起動**
1. ターミナルを完全に終了（`Command + Q`）
2. ターミナルを再度開く
3. もう一度 `brew --version` を実行

**対処法2: パス設定を再実行（Apple Silicon Macのみ）**

以下の2つのコマンドを再度実行：
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**対処法3: シェルの種類を確認**

ターミナルで以下を実行：
```bash
echo $SHELL
```

結果が `/bin/zsh` の場合（ほとんどの場合）:
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
source ~/.zprofile
```

結果が `/bin/bash` の場合:
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.bash_profile
source ~/.bash_profile
```

### ステップ5: Gitをインストール（Homebrewを使う場合）

Homebrewのインストールが確認できたら、以下を実行：

```bash
brew install git
```

**所要時間:** 2〜5分

**完了後、以下で確認:**
```bash
git --version
```

`git version 2.xx.x` と表示されればOK！

### ステップ6: Gitのインストール確認（全員共通）

どの方法でインストールしても、最後に必ず確認：

```bash
git --version
```

**✅ 成功:**
```
git version 2.39.2
```
のように表示される

**❌ 失敗:**
```
command not found: git
```
と表示される → [トラブルシューティング](#gitが正しくインストールされない)を参照

### ステップ7: Gitコマンドの場所を確認

```bash
which git
```

以下のいずれかが表示されればOK：
- `/usr/bin/git`（Xcodeコマンドラインツールの場合）
- `/opt/homebrew/bin/git`（Apple Silicon + Homebrewの場合）
- `/usr/local/bin/git`（Intel + Homebrewの場合）

### ステップ8: Gitの初期設定

**⚠️ このステップは必須です！スキップしないでください。**

Gitを使うために、あなたの名前とメールアドレスを設定します。

#### 8-1: 名前を設定

```bash
git config --global user.name "あなたの名前"
```

**例:**
```bash
git config --global user.name "Taro Yamada"
```

💡 **ポイント:**
- ダブルクォーテーション（`"`）を忘れずに
- 日本語でもローマ字でもOK
- GitHubで表示される名前になります

#### 8-2: メールアドレスを設定

```bash
git config --global user.email "your.email@example.com"
```

**例:**
```bash
git config --global user.email "taro.yamada@gmail.com"
```

💡 **ポイント:**
- 後で作成するGitHubアカウントと同じメールアドレスを使用
- ダブルクォーテーション（`"`）を忘れずに

#### 8-3: 設定を確認

```bash
git config --global --list
```

以下のように表示されればOK：
```
user.name=Taro Yamada
user.email=taro.yamada@gmail.com
...（その他の設定）
```

⚠️ **もし間違えた場合:**
同じコマンドを正しい内容で再実行すれば上書きされます。

### ステップ9: 日本語ファイル名の文字化け防止

```bash
git config --global core.quotepath false
```

`Return` を押す（何も表示されませんが正常です）

これで日本語のファイル名が正しく表示されるようになります。

### ステップ10: デフォルトブランチ名を設定

```bash
git config --global init.defaultBranch main
```

`Return` を押す（何も表示されませんが正常です）

💡 **なぜ必要？** 新しいリポジトリを作成したときに、GitHubの標準である `main` ブランチが使われます。

### ✅ Gitのインストール完了チェック

以下をすべて実行して、正しい結果が表示されることを確認：

```bash
git --version
git config user.name
git config user.email
```

すべて正しく表示されたら、Gitのインストールは完了です！

---

## 👤 GitHubアカウント作成

### GitHubとは？

GitHubは、Gitで管理したコードをインターネット上に保存・共有できるサービスです。
無料で使えて、世界中の開発者が利用しています。

### ステップ1: GitHubにアクセス

1. ブラウザ（Safari、Chrome、Firefoxなど）を開く
2. https://github.com にアクセス
3. 画面右上の **「Sign up」** をクリック

### ステップ2: メールアドレスを入力

1. **「Email address」** の欄に、Gitで設定したメールアドレスを入力
   - 例: `taro.yamada@gmail.com`
2. **「Continue」** をクリック

💡 **ポイント:** Gitの設定と同じメールアドレスを使うと管理が楽です。

### ステップ3: パスワードを作成

1. **「Password」** の欄にパスワードを入力
2. **「Continue」** をクリック

**パスワードの条件:**
- 最低15文字、または
- 8文字以上で数字と小文字を含む

**推奨パスワードの例:**
- `MyGitHub2025!Secure`
- `TaroYamada@GitHub123`

💡 **セキュリティのコツ:**
- 他のサイトで使っているパスワードは避ける
- メモ帳やパスワード管理アプリに保存しておく

### ステップ4: ユーザー名を作成

1. **「Username」** の欄にユーザー名を入力
2. **「Continue」** をクリック

**ユーザー名のルール:**
- 3〜39文字
- 英数字とハイフン（`-`）のみ
- 最初と最後の文字は英数字
- 連続したハイフン（`--`）は不可

**ユーザー名の例:**
- `taro-yamada`
- `yamada-taro-dev`
- `taroyamada123`

💡 **ポイント:**
- このユーザー名がGitHubのURLに使われます（例: `github.com/taro-yamada`）
- 後から変更できますが、変更するとリンクが変わるので慎重に
- 短くて覚えやすい名前がおすすめ

**⚠️ 「Username is already taken」と表示されたら:**
そのユーザー名は既に使われています。別の名前を試してください。

### ステップ5: メール受信の設定

**「Would you like to receive product updates and announcements via email?」**

GitHubからのお知らせメールを受け取るか選択します。

- **`y`** と入力 → メールを受け取る
- **`n`** と入力 → メールを受け取らない

どちらでもOKです。`Return` を押してください。

### ステップ6: 人間認証（CAPTCHA）

**「Verify your account」** 画面が表示されます。

1. **「Verify」** ボタンをクリック
2. パズルが表示されるので、指示に従って解く
   - 画像を回転させる
   - 正しい画像を選ぶ
   - など

3. 完了すると **「Create account」** ボタンが表示される
4. **「Create account」** をクリック

### ステップ7: メール認証

1. 登録したメールアドレスに **GitHubから認証メール** が届きます
   - 件名: 「[GitHub] Please verify your email address」
   - 差出人: `noreply@github.com`

2. メールを開いて、**6桁の認証コード** を確認
   - 例: `123456`

3. GitHubの画面に戻り、6桁のコードを入力

**⚠️ メールが届かない場合:**

**確認事項1: 迷惑メールフォルダを確認**
- メールアプリの「迷惑メール」「スパム」フォルダを確認

**確認事項2: メールアドレスが正しいか確認**
- GitHubの画面に戻り、「Change email」でメールアドレスを修正

**確認事項3: 再送信**
- 「Resend email」をクリックして再送信
- 2〜3分待ってから再度確認

**確認事項4: 別のメールアドレスを試す**
- Gmailを使うのが最も確実です

### ステップ8: アカウント作成完了

認証コードを入力すると、GitHubアカウントが作成されます！

**「Welcome to GitHub」** 画面が表示されます。

### ステップ9: 初期設定（スキップ可能）

GitHubがいくつか質問してきます。答えてもスキップしてもOKです。

**質問例:**
- 「あなたは学生ですか？」
- 「チームで使いますか？」
- 「興味のあるトピックは？」

**👉 すべてスキップする場合:**
- 画面下部の **「Skip personalization」** または **「Continue」** をクリック

### ステップ10: GitHubのダッシュボード

**「Dashboard」** 画面が表示されたら、アカウント作成完了です！

**画面の確認:**
- 左上に自分のユーザー名が表示されている
- 右上にプロフィールアイコンが表示されている

### ステップ11: GitHubのプロフィール設定（オプション）

プロフィールを充実させておくと、他の開発者とつながりやすくなります。

1. 右上の **プロフィールアイコン** をクリック
2. **「Settings」** を選択
3. **「Public profile」** で以下を設定:
   - **Name:** 本名または表示名
   - **Bio:** 自己紹介（例: 「Python学習中」）
   - **Location:** 場所（例: 「Tokyo, Japan」）
   - **Website:** 個人サイトがあれば

4. **「Update profile」** をクリックして保存

### ✅ GitHubアカウント作成完了チェック

以下を確認:
- [ ] GitHubにログインできる
- [ ] ユーザー名とメールアドレスが正しく設定されている
- [ ] ダッシュボードが表示される

---

## 💻 VSCodeのインストールと設定

### VSCodeとは？

Visual Studio Code（VSCode）は、Microsoftが開発した無料のコードエディタです。
Gitとの連携が優れており、世界中の開発者に使われています。

### ステップ1: VSCodeをダウンロード

1. ブラウザで https://code.visualstudio.com にアクセス
2. 青い **「Download for Mac」** ボタンをクリック

**自動的に正しいバージョンがダウンロードされます:**
- **Apple Silicon Mac:** `VSCode-darwin-arm64.zip`
- **Intel Mac:** `VSCode-darwin.zip`

**⚠️ 間違ったバージョンをダウンロードした場合:**
1. ページを下にスクロール
2. 「other platforms」のリンクをクリック
3. 正しいバージョンを選択してダウンロード

💡 **ダウンロード先:** 通常は「ダウンロード」フォルダに保存されます。

### ステップ2: VSCodeをインストール

#### 2-1: zipファイルを解凍

1. **Finderを開く**（Dockの笑顔アイコン）
2. 左サイドバーの **「ダウンロード」** をクリック
3. ダウンロードした **`.zip`ファイル** をダブルクリック
4. 自動的に解凍されて **`Visual Studio Code.app`** が作成されます

**⚠️ 解凍されない場合:**
- `.zip`ファイルを右クリック → 「開く」
- または、`The Unarchiver`などの解凍アプリを使用

#### 2-2: アプリケーションフォルダにコピー

1. 解凍された **`Visual Studio Code.app`** を探す
2. **新しいFinderウィンドウ** を開く（`Command + N`）
3. 左サイドバーの **「アプリケーション」** をクリック
4. **`Visual Studio Code.app`** を「アプリケーション」フォルダに **ドラッグ＆ドロップ**

💡 **ドラッグ＆ドロップ:** マウスでファイルを掴んで、別の場所に移動させる操作

### ステップ3: VSCodeを起動

#### 3-1: 初回起動

**起動方法:**
- **Launchpad** から「Visual Studio Code」をクリック
- または、**アプリケーション** フォルダから起動
- または、Spotlight検索（`Command + Space`）で「vscode」と入力

#### 3-2: セキュリティ警告への対応

**パターンA: 通常の確認画面**

**「"Visual Studio Code.app"はインターネットからダウンロードされたアプリケーションです。開いてもよろしいですか？」**

1. **「開く」** をクリック

**パターンB: ブロックされる場合**

**「"Visual Studio Code"は、App Storeからダウンロードされたものではないため開けません。」**

**対処法:**
1. **「OK」** をクリック
2. 画面左上の **🍎 リンゴマーク** をクリック
3. **「システム環境設定」**（または「システム設定」）を選択
4. **「セキュリティとプライバシー」**（または「プライバシーとセキュリティ」）をクリック
5. 下の方に表示される **「"Visual Studio Code"は開発元を確認できないため、使用がブロックされました。」** を探す
6. **「このまま開く」** ボタンをクリック
7. パスワードを求められたら、**Macのパスワード** を入力
8. もう一度確認画面が出たら **「開く」** をクリック

💡 **これは正常な動作です:** MacがあなたのMacを守るための機能です。

#### 3-3: ファイアウォールの許可

**「"Visual Studio Code.app"がネットワーク接続を受け入れようとしています。許可しますか？」**

1. **「許可」** をクリック

💡 **なぜ必要？** VSCodeがGitHubと通信するために必要です。

### ステップ4: VSCodeの初期画面を確認

VSCodeが起動すると、以下のような画面が表示されます：

- **Welcome画面:** 「Get Started with VS Code」
- **左サイドバー:** アイコンが縦に並んでいる
- **中央:** エディタエリア（ファイルを開く場所）

### ステップ5: 日本語化（オプションだが強く推奨）

VSCodeは初期状態では英語です。日本語化すると使いやすくなります。

#### 5-1: 拡張機能を開く

- **方法1:** `Command + Shift + X` を押す
- **方法2:** 左サイドバーの **四角いブロックのアイコン**（Extensions）をクリック

#### 5-2: 日本語パックを検索

1. 上部の検索ボックスに **「Japanese」** と入力
2. **「Japanese Language Pack for Visual Studio Code」** を探す
   - 作成者: **Microsoft**
   - アイコン: 日本の国旗🇯🇵

#### 5-3: インストール

1. **「Install」** ボタンをクリック
2. インストールが完了すると、右下に通知が表示されます：
   **「Would you like to change VS Code's display language to Japanese and restart?」**
3. **「Change Language and Restart」**（または **「Restart」**）をクリック

VSCodeが再起動し、日本語表示になります。

#### 5-4: 日本語化の確認

VSCodeが再起動したら、メニューバーを確認：
- **「File」** → **「ファイル」**
- **「Edit」** → **「編集」**
- **「View」** → **「表示」**

日本語になっていればOK！

**⚠️ 再起動しても英語のままの場合:**

1. `Command + Shift + P` でコマンドパレットを開く
2. **「Configure Display Language」** と入力して選択
3. **「日本語 (ja)」** を選択
4. VSCodeを再起動（`Command + Q` で終了してから再度起動）

### ステップ6: GitHubとの連携

VSCodeとGitHubを連携させると、VSCode内から直接GitHubにコードをアップロードできます。

#### 6-1: サインイン画面を開く

- **方法1:** 左サイドバー一番下の **人型アイコン**（アカウント）をクリック
- **方法2:** `Command + Shift + P` でコマンドパレットを開き、**「サインイン」** と入力

#### 6-2: GitHubを選択

表示される選択肢から：
- **「GitHub でサインインして設定を同期する」** を選択

**⚠️ 複数の選択肢がある場合:**
- **「GitHub」** を選択（**「GitHub Enterprise」** ではない）

#### 6-3: ブラウザでの認証

1. **自動的にブラウザが開きます**
   - 開かない場合は、VSCodeに表示されるリンクをクリック

2. GitHubのページが開き、以下が表示されます：
   **「Authorize Visual-Studio-Code」**
   
3. **「Authorize Visual-Studio-Code」** ボタンをクリック

4. **GitHubにログインしていない場合:** ユーザー名とパスワードを入力してログイン

5. **認証完了画面:**
   **「Success! You may now close this tab and return to VS Code.」**
   
6. タブを閉じてVSCodeに戻る

#### 6-4: VSCodeに戻る確認

**「Visual Studio Codeを開きますか？」**

1. **「開く」** をクリック

#### 6-5: 連携完了の確認

VSCodeに戻ると：
- 右下に通知: **「GitHub アカウントでサインインしました」**
- 左下の人型アイコンに **GitHubのユーザー名** が表示される

**✅ 連携成功の確認:**
- 左下に自分のGitHubユーザー名が表示されている
- アイコンをクリックすると「サインアウト」が表示される

### ステップ7: VSCodeの基本設定（推奨）

#### 7-1: 自動保存を有効化

1. メニューバーの **「ファイル」** をクリック
2. **「自動保存」** にチェックを入れる

💡 **メリット:** ファイルを編集したら自動的に保存されます。保存忘れを防げます。

#### 7-2: フォーマット設定

1. `Command + ,`（コンマ）で設定を開く
2. 検索ボックスに **「format on save」** と入力
3. **「Editor: Format On Save」** にチェックを入れる

💡 **メリット:** ファイルを保存するときに自動的にコードが整形されます。

#### 7-3: ターミナルの設定

VSCode内でターミナルを使えるようにします。

1. メニューバーの **「表示」** → **「ターミナル」**
2. または `Control + @`（バッククォート）

画面下部にターミナルが表示されます。

**デフォルトシェルの確認:**
- タブに **「zsh」** または **「bash」** と表示されます

**⚠️ ターミナルが開かない場合:**

1. `Command + Shift + P` でコマンドパレットを開く
2. **「ターミナル: 新しいターミナルを作成」** と入力して選択

### ステップ8: codeコマンドをインストール

ターミナルから `code .` と入力してVSCodeでフォルダを開けるようにします。

1. `Command + Shift + P` でコマンドパレットを開く
2. **「shell command」** と入力
3. **「シェル コマンド: PATH内に'code'コマンドをインストールします」** を選択
4. **「インストールしました」** と表示されればOK

**確認方法:**

ターミナル（Mac標準のターミナル.app）を開いて：
```bash
which code
```

`/usr/local/bin/code` などと表示されればOK！

### ✅ VSCodeのインストール完了チェック

以下をすべて確認:
- [ ] VSCodeが起動する
- [ ] 日本語表示になっている
- [ ] GitHubアカウントと連携されている（左下にユーザー名表示）
- [ ] ターミナルが開ける
- [ ] `code` コマンドがインストールされている

---

## 🔐 SSHキーの設定（推奨）

### SSHキーとは？

SSHキーは、GitHubとの安全な通信を行うための「鍵」です。
これを設定すると、GitHubにコードをアップロードするたびにパスワードを入力する必要がなくなります。

### なぜSSHキーが必要？

- ✅ パスワード入力の手間が不要
- ✅ より安全な認証方法
- ✅ GitHubが推奨する方法
- ✅ 自動化がしやすい

### ステップ1: SSHキーが既にあるか確認

ターミナルを開いて、以下を実行：

```bash
ls -al ~/.ssh
```

**結果のパターン:**

#### パターンA: SSHキーが既に存在
```
-rw-------  1 username  staff  2655  Jan 1 12:00 id_ed25519
-rw-r--r--  1 username  staff   574  Jan 1 12:00 id_ed25519.pub
```

`id_ed25519` と `id_ed25519.pub`（または `id_rsa` と `id_rsa.pub`）が表示された
→ **既にSSHキーがあります！[ステップ3](#ステップ3-sshキーをクリップボードにコピー)へ**

#### パターンB: .sshフォルダはあるがキーファイルがない
```
total 0
drwx------  2 username  staff    64  Jan 1 12:00 .
drwxr-xr-x  20 username  staff   640  Jan 1 12:00 ..
```

→ **次のステップへ**

#### パターンC: .sshフォルダが存在しない
```
ls: /Users/username/.ssh: No such file or directory
```

→ **次のステップへ**

### ステップ2: 新しいSSHキーを生成

#### 2-1: キー生成コマンドを実行

ターミナルで以下を実行（**メールアドレスを自分のものに置き換えてください**）：

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

**例:**
```bash
ssh-keygen -t ed25519 -C "taro.yamada@gmail.com"
```

💡 **ポイント:** GitHubアカウントのメールアドレスを使ってください。

#### 2-2: 保存場所の確認

```
Enter file in which to save the key (/Users/username/.ssh/id_ed25519):
```

このように聞かれたら、**何も入力せず `Return` を押してください**（デフォルトでOK）

#### 2-3: パスフレーズの設定

```
Enter passphrase (empty for no passphrase):
```

**選択肢:**

**推奨: パスフレーズなし**
- そのまま **`Return` を押す**
- もう一度 `Return` を押す（確認）

**セキュリティ重視: パスフレーズあり**
- パスフレーズを入力（画面には表示されません）
- `Return` を押す
- 同じパスフレーズを再入力
- `Return` を押す

💡 **パスフレーズなしを推奨する理由:** 
- 毎回の操作が楽
- Macのキーチェーンで保護される
- 個人のMacで使う分には安全

#### 2-4: 生成完了の確認

以下のようなメッセージが表示されれば成功：

```
Your identification has been saved in /Users/username/.ssh/id_ed25519
Your public key has been saved in /Users/username/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx your.email@example.com
The key's randomart image is:
+--[ED25519 256]--+
|                 |
...
+----[SHA256]-----+
```

#### 2-5: トラブルシューティング（古いMacの場合）

**⚠️ `unknown key type ed25519` というエラーが出た場合:**

古いバージョンのmacOSを使っている可能性があります。
代わりにRSAキーを生成してください：

```bash
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```

**例:**
```bash
ssh-keygen -t rsa -b 4096 -C "taro.yamada@gmail.com"
```

その後の手順は同じです（`id_rsa` と `id_rsa.pub` が生成されます）。

### ステップ3: SSHキーをクリップボードにコピー

公開鍵（`.pub`ファイル）をクリップボードにコピーします。

#### 3-1: コピーコマンドを実行

**Ed25519キーの場合（ほとんどの場合）:**
```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

**RSAキーの場合（古いMac）:**
```bash
pbcopy < ~/.ssh/id_rsa.pub
```

`Return` を押す（**画面には何も表示されませんが正常です**）

#### 3-2: コピーできたか確認（オプション）

本当にコピーされたか確認したい場合：

1. **テキストエディット** を開く（Launchpadから）
2. `Command + V` でペースト
3. 以下のような長い文字列が表示されればOK：

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx your.email@example.com
```

4. 確認したら、このテキストは削除してOK（保存不要）

💡 **ポイント:** 
- `ssh-ed25519` または `ssh-rsa` で始まる
- 最後にメールアドレスが含まれている

### ステップ4: GitHubにSSHキーを登録

#### 4-1: GitHubのSSH設定ページを開く

1. ブラウザで https://github.com/settings/keys にアクセス
2. **ログインしていない場合:** ユーザー名とパスワードを入力してログイン

#### 4-2: 新しいSSHキーを追加

1. 右上の緑色の **「New SSH key」** ボタンをクリック

#### 4-3: キー情報を入力

**Title（タイトル）:**
- キーの識別用の名前を入力
- 例: 
  - `My MacBook Pro`
  - `Home Mac`
  - `Work iMac`
  - `Mac Mini 2024`

💡 **複数のMacを使う場合:** どのMacのキーか分かる名前にしましょう。

**Key type（キーの種類）:**
- **「Authentication Key」** を選択（デフォルト）

**Key（キー）:**
1. 入力欄をクリック
2. `Command + V` でペースト
3. 以下のような長い文字列が貼り付けられるはず：
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... your.email@example.com
```

**⚠️ 確認事項:**
- `ssh-ed25519` または `ssh-rsa` で始まっている
- 最後にメールアドレスが含まれている
- 余計な改行や空白がない

#### 4-4: キーを追加

1. 緑色の **「Add SSH key」** ボタンをクリック
2. **パスワード入力を求められたら:** GitHubのパスワードを入力
3. **2段階認証を設定している場合:** 認証コードを入力

#### 4-5: 追加されたことを確認

リストに追加したキーが表示されます：
- タイトル（例: `My MacBook Pro`）
- キーの一部が表示される
- 緑色のチェックマーク ✅

### ステップ5: SSH接続をテスト

GitHubとSSHで接続できるか確認します。

#### 5-1: 接続テストコマンドを実行

ターミナルで以下を実行：

```bash
ssh -T git@github.com
```

#### 5-2: 初回接続時の確認

**初めて接続する場合、以下のようなメッセージが表示されます:**

```
The authenticity of host 'github.com (xxx.xxx.xxx.xxx)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

**👉 `yes` と入力して `Return` を押す**

💡 **これは正常です:** GitHubのサーバーを信頼するかの確認です。

#### 5-3: 成功メッセージの確認

**✅ 成功の場合:**
```
Hi ユーザー名! You've successfully authenticated, but GitHub does not provide shell access.
```

このメッセージが表示されたら成功！

**❌ 失敗の場合:**

**エラー1: `Permission denied (publickey)`**
```
git@github.com: Permission denied (publickey).
```

**原因:** SSHキーが正しく設定されていない

**対処法:**
1. [ステップ2](#ステップ2-新しいsshキーを生成)からやり直す
2. GitHubに正しいキーが登録されているか確認
3. [トラブルシューティング](#ssh接続エラー)を参照

**エラー2: `ssh: Could not resolve hostname github.com`**
```
ssh: Could not resolve hostname github.com
```

**原因:** インターネット接続の問題

**対処法:**
1. Wi-Fiに接続されているか確認
2. ブラウザでGitHubが開けるか確認
3. ファイアウォール設定を確認

### ステップ6: SSH設定ファイルを作成（推奨）

接続をスムーズにするための設定ファイルを作成します。

#### 6-1: 設定ファイルを作成

**Ed25519キーの場合:**
```bash
cat >> ~/.ssh/config << 'EOF'
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
EOF
```

**RSAキーの場合:**
```bash
cat >> ~/.ssh/config << 'EOF'
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa
EOF
```

`Return` を押す（何も表示されませんが正常です）

#### 6-2: 設定の意味

- **AddKeysToAgent:** キーをSSHエージェントに自動追加
- **UseKeychain:** MacのキーチェーンにSSHキーを保存
- **IdentityFile:** 使用するSSHキーのパス

💡 **メリット:** パスフレーズを設定していても、毎回入力する必要がなくなります。

#### 6-3: SSHエージェントにキーを追加

**Ed25519キーの場合:**
```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

**RSAキーの場合:**
```bash
ssh-add --apple-use-keychain ~/.ssh/id_rsa
```

**成功メッセージ:**
```
Identity added: /Users/username/.ssh/id_ed25519 (your.email@example.com)
```

**⚠️ `--apple-use-keychain` がエラーになる場合（古いmacOS）:**
```bash
ssh-add -K ~/.ssh/id_ed25519
```

### ✅ SSH設定完了チェック

以下をすべて確認:
- [ ] SSHキーが生成されている（`ls ~/.ssh` で確認）
- [ ] GitHubにSSHキーが登録されている
- [ ] `ssh -T git@github.com` で成功メッセージが表示される
- [ ] SSH設定ファイルが作成されている

---

## 📥 リポジトリのクローン

### リポジトリとは？

リポジトリ（Repository）は、プロジェクトのファイルとその変更履歴を保存する場所です。
「クローン」とは、GitHubにあるリポジトリをあなたのMacにコピーすることです。

### 準備: GitHubでリポジトリを作成（初めての場合）

クローンする前に、GitHubでリポジトリを作成します。

#### リポジトリ作成手順:

1. GitHubにログイン（https://github.com）
2. 右上の **「+」** をクリック → **「New repository」** を選択
3. リポジトリ情報を入力:
   - **Repository name:** `my-first-repo`（例）
   - **Description:** 「私の最初のリポジトリ」（オプション）
   - **Public/Private:** どちらでもOK（Publicは誰でも見れる、Privateは自分だけ）
   - ✅ **「Add a README file」** にチェック
4. **「Create repository」** をクリック

これでクローンする準備ができました！

### 方法1: VSCodeから直接クローン（初心者におすすめ★）

VSCodeのGUI（画面操作）でクローンします。最も簡単な方法です。

#### 1-1: コマンドパレットを開く

- `Command + Shift + P` を押す
- または、メニューバーの **「表示」** → **「コマンドパレット」**

#### 1-2: Gitクローンを選択

1. **「Git: Clone」** と入力（途中まで入力すると候補が表示されます）
2. **「Git: Clone」**（または **「Git: クローン」**）を選択して `Return`

#### 1-3: クローン元を選択

**「GitHubからクローン」** を選択

💡 これで、あなたのGitHubリポジトリ一覧が表示されます。

#### 1-4: リポジトリを選択

1. クローンしたいリポジトリを選択（例: `my-first-repo`）
2. `Return` を押す

**⚠️ 他の人のリポジトリをクローンする場合:**
- リポジトリのURL全体を入力（例: `https://github.com/octocat/Hello-World`）

#### 1-5: 保存先フォルダを選択

**「リポジトリの場所を選んでください」**

推奨フォルダ構成:
```
/Users/あなたの名前/Documents/
└── GitHub/
    ├── my-first-repo/
    ├── project1/
    └── project2/
```

**初めての場合（GitHubフォルダがない）:**

1. **「Documents」** フォルダを選択
2. 下部の **「新しいフォルダ」** をクリック
3. フォルダ名: **「GitHub」** と入力
4. **「作成」** をクリック
5. **「GitHub」** フォルダを選択
6. **「リポジトリの場所として選択」** をクリック

**2回目以降（GitHubフォルダがある）:**

1. **「GitHub」** フォルダを選択
2. **「リポジトリの場所として選択」** をクリック

#### 1-6: クローン開始

クローンが始まります。画面右下に進行状況が表示されます。

```
Cloning into 'my-first-repo'...
```

#### 1-7: クローン完了

**「クローンしたリポジトリを開きますか？」**

1. **「開く」** をクリック

VSCodeでプロジェクトが開かれます！

#### 1-8: 開いたプロジェクトの確認

- **左サイドバー:** ファイル一覧が表示される
- **README.md** ファイルが見える
- 画面上部: プロジェクト名（例: `my-first-repo`）が表示される

✅ **クローン成功！**

### 方法2: ターミナルからクローン（コマンドを学びたい場合）

コマンドラインでクローンします。プロとしてのスキルが身につきます。

#### 2-1: ターミナルを開く

- Mac標準のターミナル.app
- または、VSCodeのターミナル（`Control + @`）

#### 2-2: クローン先フォルダに移動

```bash
cd ~/Documents
```

`Return` を押す

#### 2-3: GitHubフォルダを作成（初回のみ）

```bash
mkdir GitHub
cd GitHub
```

`Return` を押す

**⚠️ すでにGitHubフォルダがある場合:**
```bash
cd GitHub
```

#### 2-4: 現在の場所を確認

```bash
pwd
```

`/Users/あなたの名前/Documents/GitHub` と表示されればOK

#### 2-5: クローンするリポジトリのURLを取得

1. ブラウザでGitHubのリポジトリページを開く
2. 緑色の **「Code」** ボタンをクリック
3. **「SSH」** タブを選択（SSHキーを設定した場合）
4. URLをコピー（例: `git@github.com:ユーザー名/リポジトリ名.git`）

💡 **SSH vs HTTPS:**
- **SSH:** `git@github.com:user/repo.git`（推奨・パスワード不要）
- **HTTPS:** `https://github.com/user/repo.git`（パスワードが必要）

#### 2-6: クローンコマンドを実行

**SSHを使う場合（推奨）:**
```bash
git clone git@github.com:ユーザー名/リポジトリ名.git
```

**例:**
```bash
git clone git@github.com:taro-yamada/my-first-repo.git
```

**HTTPSを使う場合:**
```bash
git clone https://github.com/ユーザー名/リポジトリ名.git
```

`Return` を押す

#### 2-7: クローン中の出力

```
Cloning into 'my-first-repo'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
```

このように表示されればOK！

#### 2-8: クローンされたフォルダに移動

```bash
cd リポジトリ名
```

**例:**
```bash
cd my-first-repo
```

#### 2-9: ファイルを確認

```bash
ls -la
```

以下のようなファイルが表示されます：
```
.git/
README.md
```

#### 2-10: VSCodeで開く

```bash
code .
```

`.` は「現在のフォルダ」を意味します。

VSCodeでプロジェクトが開かれます！

**⚠️ `command not found: code` と表示される場合:**

[VSCodeのステップ8](#ステップ8-codeコマンドをインストール)を参照してください。

### 方法3: Finderから直接開く（既にクローン済みの場合）

既にクローンしたプロジェクトをVSCodeで開く最も簡単な方法：

1. **Finderを開く**
2. クローンしたフォルダに移動（例: `Documents/GitHub/my-first-repo`）
3. フォルダ内の空白部分を **右クリック**
4. **「サービス」** → **「Codeで開く」** を選択

（VSCodeインストール時に設定した場合のみ利用可能）

### トラブルシューティング: クローン失敗

#### エラー1: `Permission denied (publickey)`

**原因:** SSH接続の問題

**対処法:**
1. [SSHキーの設定](#sshキーの設定推奨)を再確認
2. または、HTTPSを使う：
```bash
git clone https://github.com/ユーザー名/リポジトリ名.git
```

#### エラー2: `Repository not found`

**原因:** リポジトリ名が間違っている、またはアクセス権限がない

**対処法:**
1. GitHubでリポジトリのURLを再確認
2. プライベートリポジトリの場合、アクセス権限があるか確認
3. ユーザー名とリポジトリ名のスペルを確認

#### エラー3: `fatal: destination path 'xxx' already exists`

**原因:** 同じ名前のフォルダが既に存在する

**対処法:**
1. 既存のフォルダを削除またはリネーム
2. 別のフォルダでクローン
3. または、既存のフォルダに移動して `git pull` を実行

### ✅ クローン完了チェック

以下をすべて確認:
- [ ] `~/Documents/GitHub/` フォルダが存在する
- [ ] リポジトリフォルダが作成されている
- [ ] VSCodeでプロジェクトが開ける
- [ ] ファイル一覧にREADME.mdなどが表示される
- [ ] `.git` フォルダが存在する（隠しフォルダ）

---

## 🚀 基本的なGit操作

ここからが本番！実際にファイルを編集して、GitHubにアップロードします。

### Gitの基本的な流れ

```
ファイルを編集
    ↓
ステージング（git add）← 変更をまとめる
    ↓
コミット（git commit）← 変更を記録
    ↓
プッシュ（git push）← GitHubにアップロード
```

### 方法1: VSCodeのGUI操作（初心者におすすめ★）

視覚的で分かりやすい方法です。

#### 手順1: ファイルを編集

1. VSCodeで **README.md** を開く（左サイドバーのファイル一覧から）
2. 内容を編集（例: 「# 私のプロジェクト」を追加）
3. `Command + S` で保存（自動保存を設定した場合は不要）

#### 手順2: 変更を確認

1. **左サイドバーのソース管理アイコン** をクリック（枝分かれマーク）
   - または `Control + Shift + G`

2. **変更されたファイルが一覧表示されます:**
   - `README.md` の横に **M**（Modified = 変更済み）

3. **ファイル名をクリック** すると、変更内容が表示されます:
   - **赤色（左側）:** 削除された行
   - **緑色（右側）:** 追加された行

#### 手順3: ファイルをステージング（変更をまとめる）

**個別にステージング:**
- ファイル名の右にある **「+」ボタン** をクリック

**すべてステージング:**
- 「変更」セクションの右にある **「+」ボタン** をクリック

ステージングされたファイルは **「ステージされている変更」** セクションに移動します。

💡 **ステージングとは？** 「これからコミットする変更」を選ぶ作業です。

#### 手順4: コミット（変更を記録）

1. **上部のメッセージボックス** に変更内容を入力
   - 例: 「READMEを更新」
   - 例: 「プロジェクト説明を追加」

2. **コミットを実行:**
   - `Command + Return` を押す
   - または **「コミット」ボタン** をクリック

**⚠️ メッセージを入力せずにコミットしようとすると:**
「コミットメッセージを入力してください」と警告が表示されます。

💡 **良いコミットメッセージの例:**
- ✅ 「ログイン機能を追加」
- ✅ 「バグ修正: ファイル読み込みエラー」
- ✅ 「READMEを更新」
- ❌ 「更新」（何を更新したか不明）
- ❌ 「aaa」（意味不明）

#### 手順5: プッシュ（GitHubにアップロード）

コミット後、変更をGitHubに送信します。

**方法1: 変更の同期ボタン**
- 上部の **「変更の同期」** ボタンをクリック

**方法2: メニューから**
1. ソース管理パネル右上の **「...」（その他のアクション）** をクリック
2. **「プッシュ」** を選択

**初回プッシュ時の確認:**
「このブランチにはアップストリームブランチがありません。」と表示される場合があります。
→ **「OK」** をクリック（自動的に設定されます）

#### 手順6: GitHubで確認

1. ブラウザでGitHubのリポジトリページを開く
2. **README.md** をクリック
3. 編集した内容が反映されていればOK！
4. コミット履歴も確認できます（「X commits」をクリック）

✅ **成功！** あなたの変更がGitHubにアップロードされました！

### 方法2: ターミナルでのコマンド操作

プロフェッショナルな方法です。コマンドを理解することで、Gitへの理解が深まります。

#### 基本の流れ

```bash
# 1. 最新版を取得（他の人の変更を取り込む）
git pull origin main

# 2. ファイルを編集
# （VSCodeなどで編集作業）

# 3. 現在の状態を確認
git status

# 4. すべてのファイルをステージング
git add .

# 5. コミット
git commit -m "コミットメッセージ"

# 6. GitHubにプッシュ
git push origin main
```

#### 詳しい説明

**ステップ1: 現在の状態を確認**

```bash
git status
```

**出力例:**
```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	new_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

**読み方:**
- **modified:** 変更されたファイル
- **Untracked files:** 新しく追加されたファイル（まだGitが追跡していない）
- **Changes not staged:** まだステージングされていない変更

**ステップ2: ファイルをステージング**

**すべてのファイルをステージング:**
```bash
git add .
```

`.` は「カレントディレクトリ以下すべて」という意味です。

**特定のファイルだけステージング:**
```bash
git add ファイル名
```

**例:**
```bash
git add README.md
git add script.py
git add Papers/analysis.csv
```

**複数ファイルを指定:**
```bash
git add file1.py file2.py folder/file3.txt
```

**ステージングを確認:**
```bash
git status
```

**出力例:**
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   README.md
	new file:   new_file.txt
```

**ステップ3: コミット**

```bash
git commit -m "コミットメッセージ"
```

**例:**
```bash
git commit -m "READMEを更新"
git commit -m "データ分析スクリプトを追加"
git commit -m "バグ修正: CSVファイル読み込みエラー"
```

**成功メッセージ:**
```
[main a1b2c3d] READMEを更新
 1 file changed, 3 insertions(+), 1 deletion(-)
```

**⚠️ コミットメッセージを忘れた場合:**
```bash
git commit
```
と実行すると、エディタが開きます。メッセージを入力して保存すればOK。

**ステップ4: ブランチ名を確認**

```bash
git branch
```

**出力例:**
```
* main
```

`*` が付いているのが現在のブランチです。

**⚠️ `master` と表示された場合:**
古いリポジトリでは `master` が使われています。その場合、プッシュコマンドは:
```bash
git push origin master
```

**ステップ5: GitHubにプッシュ**

```bash
git push origin main
```

**プッシュ中の出力:**
```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 345 bytes | 345.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:ユーザー名/リポジトリ名.git
   a1b2c3d..e4f5g6h  main -> main
```

このように表示されれば成功！

**ステップ6: GitHubで確認**

ブラウザでGitHubのリポジトリページを開き、変更が反映されているか確認しましょう。

### プル（git pull）：最新版を取得

他の人（または別のPCのあなた）が変更した内容を取得します。

```bash
git pull origin main
```

**⚠️ 重要:** 共同作業する場合、作業を始める前に必ずプルしてください！

**成功メッセージ:**
```
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
...
Updating a1b2c3d..e4f5g6h
Fast-forward
 README.md | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
```

**すでに最新の場合:**
```
Already up to date.
```

### よく使うコマンドまとめ

```bash
# 状態確認
git status                    # 現在の状態
git log                       # コミット履歴
git log --oneline             # コミット履歴（簡潔版）
git log --oneline --graph     # コミット履歴（グラフ表示）

# ステージング
git add .                     # すべて追加
git add ファイル名            # 特定ファイル
git add *.py                  # Pythonファイルのみ
git reset ファイル名          # ステージング取り消し

# コミット
git commit -m "メッセージ"    # コミット
git commit -am "メッセージ"   # add + commit（変更ファイルのみ）
git commit --amend            # 直前のコミットを修正

# プッシュ・プル
git push origin main          # プッシュ
git pull origin main          # プル
git fetch                     # リモートの情報だけ取得

# 差分確認
git diff                      # 変更内容を表示
git diff ファイル名           # 特定ファイルの変更
git diff --staged             # ステージング済みの変更

# 取り消し操作
git restore ファイル名        # ファイルの変更を取り消し
git restore --staged ファイル名  # ステージング取り消し
git reset --soft HEAD^        # 直前のコミット取り消し（変更は保持）
git reset --hard HEAD^        # 直前のコミット取り消し（変更も削除）
```

### ✅ 基本操作完了チェック

以下をすべて確認:
- [ ] ファイルを編集できた
- [ ] 変更をステージングできた
- [ ] コミットできた
- [ ] GitHubにプッシュできた
- [ ] GitHubで変更が確認できた
- [ ] git statusコマンドが理解できた

---

## 📤 ファイルのアップロード実践

実際のプロジェクトでよくあるシナリオを練習しましょう。

### シナリオ1: 新しいPythonスクリプトを追加

#### 手順:

1. **VSCodeで新しいファイルを作成**
   - `Command + N`（新規ファイル）
   - `Command + S`（保存）
   - ファイル名: `analysis.py`

2. **簡単なコードを書く:**
```python
# データ分析スクリプト
import pandas as pd

def main():
    print("Hello, Git!")

if __name__ == "__main__":
    main()
```

3. **保存** (`Command + S`)

4. **ソース管理パネル** を開く（`Control + Shift + G`）

5. **ファイルをステージング** （`analysis.py` の横の `+` ボタン）

6. **コミットメッセージを入力:** 「データ分析スクリプトを追加」

7. **コミット** (`Command + Return`)

8. **プッシュ** （「変更の同期」ボタン）

9. **GitHubで確認**

✅ 完了！

### シナリオ2: 複数ファイルを一度にアップロード

#### 手順:

1. **複数のファイルを作成・編集:**
   - `config.py`（設定ファイル）
   - `utils.py`（ユーティリティ関数）
   - `README.md`（説明を追加）

2. **ソース管理パネル** で確認
   - 3つのファイルが表示される

3. **すべてステージング** （「変更」の横の `+` ボタン）

4. **コミットメッセージ:** 「設定ファイルとユーティリティを追加」

5. **コミット & プッシュ**

✅ 完了！

### シナリオ3: フォルダごとアップロード

#### 手順:

1. **新しいフォルダを作成:**
   - VSCodeで `data` フォルダを作成
   - その中に `sample.csv` を作成

2. **ソース管理パネル** で確認
   - `data/sample.csv` が表示される

3. **通常通りステージング・コミット・プッシュ**

💡 **Git特性:** Gitは空のフォルダを追跡しません。フォルダ内に最低1つファイルが必要です。

### シナリオ4: .gitignoreで不要なファイルを除外

#### .gitignoreとは？

Gitで追跡したくないファイルを指定するファイルです。

**よく除外するファイル:**
- `.DS_Store`（macOSが作る隠しファイル）
- `__pycache__/`（Pythonのキャッシュ）
- `.env`（環境変数・秘密情報）
- `*.log`（ログファイル）
- `node_modules/`（Node.jsの依存関係）

#### 作成手順:

1. **リポジトリのルートフォルダで `.gitignore` ファイルを作成**
   - ファイル名の最初は必ず `.`（ドット）

2. **以下の内容を記述:**
```
# macOS
.DS_Store
*.DS_Store

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Jupyter Notebook
.ipynb_checkpoints

# データファイル（必要に応じて）
*.csv
*.xlsx
*.db
data/

# VSCode
.vscode/

# ログファイル
*.log
```

3. **保存してコミット & プッシュ**

💡 **既にコミットしてしまったファイルを除外する場合:**
```bash
git rm --cached ファイル名
git commit -m ".gitignoreを追加してファイルを除外"
git push origin main
```

### シナリオ5: 大きなファイルをアップロード

**⚠️ GitHubの制限:**
- 1ファイル100MBまで
- リポジトリ全体で推奨1GB、最大5GB

**対処法:**

#### 方法1: ファイルを分割または圧縮

```bash
# ファイルを圧縮
zip large_data.zip large_data.csv
```

#### 方法2: Git LFS（Large File Storage）を使う

大きなファイル専用のGit拡張機能です。

**インストール:**
```bash
brew install git-lfs
git lfs install
```

**使い方:**
```bash
# 特定の種類のファイルをLFSで管理
git lfs track "*.csv"
git lfs track "*.xlsx"

# .gitattributesファイルをコミット
git add .gitattributes
git commit -m "LFSを設定"

# 大きなファイルを追加
git add large_file.csv
git commit -m "大きなCSVファイルを追加"
git push origin main
```

### シナリオ6: 間違えてコミットしたファイルを削除

#### 直前のコミットを取り消す:

```bash
# コミット取り消し（変更は保持）
git reset --soft HEAD^

# ファイルを修正または削除

# 再度コミット
git add .
git commit -m "修正版"
git push origin main
```

#### 既にプッシュしてしまった場合:

```bash
# 危険！GitHubの履歴を書き換えます
git reset --hard HEAD^
git push -f origin main
```

**⚠️ 注意:** 他の人と共同作業している場合は使わないでください！

**安全な方法（推奨）:**
```bash
# 新しいコミットで削除
git rm 削除したいファイル
git commit -m "不要なファイルを削除"
git push origin main
```

### ✅ ファイルアップロード実践完了チェック

以下をすべて確認:
- [ ] 新しいファイルを作成してアップロードできた
- [ ] 複数ファイルを一度にアップロードできた
- [ ] .gitignoreを作成して不要なファイルを除外できた
- [ ] 間違えたときの対処法を理解した

---

## 🐛 トラブルシューティング

### Gitが正しくインストールされない

#### 症状: `command not found: git`

**対処法1: Xcodeコマンドラインツールを再インストール**
```bash
xcode-select --install
```

**対処法2: パスを確認**
```bash
echo $PATH
```

`/usr/bin` または `/usr/local/bin` が含まれているか確認

**対処法3: シェルの設定ファイルを確認**
```bash
# zshの場合
cat ~/.zshrc
# bashの場合
cat ~/.bash_profile
```

### Homebrewが使えない

#### 症状: `command not found: brew`

**対処法1: パス設定を再実行（Apple Silicon）**
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**対処法2: パス設定を再実行（Intel Mac）**
```bash
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/usr/local/bin/brew shellenv)"
```

**対処法3: Homebrewが実際にインストールされているか確認**
```bash
ls /opt/homebrew/bin/brew          # Apple Silicon
ls /usr/local/bin/brew             # Intel Mac
```

ファイルが存在しない場合、Homebrewのインストールからやり直してください。

### SSH接続エラー

#### 症状: `Permission denied (publickey)`

**対処法1: SSHキーが正しく生成されているか確認**
```bash
ls -la ~/.ssh
```

`id_ed25519` と `id_ed25519.pub` が存在するか確認

**対処法2: GitHubにSSHキーが登録されているか確認**
https://github.com/settings/keys にアクセスして確認

**対処法3: SSHエージェントにキーを追加**
```bash
eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

**対処法4: SSH設定ファイルを確認**
```bash
cat ~/.ssh/config
```

正しい内容が記述されているか確認

**対処法5: HTTPSを使う**
```bash
git remote set-url origin https://github.com/ユーザー名/リポジトリ名.git
```

### コミットエラー

#### 症状: `Please tell me who you are`

**原因:** Gitの初期設定（user.name, user.email）がされていない

**対処法:**
```bash
git config --global user.name "あなたの名前"
git config --global user.email "your.email@example.com"
```

### プッシュエラー

#### 症状: `Updates were rejected`

**完全なエラーメッセージ:**
```
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:user/repo.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
```

**原因:** GitHubに新しい変更があるが、それを取得していない

**対処法:**
```bash
# 1. 最新版を取得
git pull origin main

# 2. コンフリクトがあれば解決

# 3. プッシュ
git push origin main
```

#### 症状: `Repository not found`

**原因1:** リポジトリ名が間違っている

**対処法:**
```bash
# リモートURLを確認
git remote -v

# 間違っている場合は修正
git remote set-url origin git@github.com:正しいユーザー名/正しいリポジトリ名.git
```

**原因2:** プライベートリポジトリへのアクセス権限がない

**対処法:** リポジトリのオーナーに確認

### コンフリクト（競合）

#### 症状: `CONFLICT (content): Merge conflict`

**原因:** 同じファイルの同じ箇所を複数人が編集した

**VSCodeでの解決方法:**

1. **コンフリクトが発生したファイルを開く**
   - ファイル名に `!` マークが表示される

2. **コンフリクト箇所が表示される:**
```python
<<<<<<< HEAD
# あなたのコード
def function():
    print("version 1")
=======
# 他の人のコード
def function():
    print("version 2")
>>>>>>> origin/main
```

3. **VSCodeの選択肢をクリック:**
   - **「現在の変更を採用」** → あなたの変更を残す
   - **「入力側の変更を採用」** → 他の人の変更を採用
   - **「両方の変更を保持」** → 両方残す（手動で調整が必要）
   - **「変更を比較」** → 違いを詳しく確認

4. **選択後、ファイルを保存**

5. **再度ステージング・コミット・プッシュ:**
```bash
git add .
git commit -m "コンフリクトを解決"
git push origin main
```

**ターミナルでの解決方法:**

1. **コンフリクトを確認:**
```bash
git status
```

2. **ファイルを手動で編集して `<<<<<<<`, `=======`, `>>>>>>>` を削除**

3. **解決後:**
```bash
git add .
git commit -m "コンフリクトを解決"
git push origin main
```

### ファイル名の文字化け

#### 症状: 日本語ファイル名が `"\343\203\206..."` のように表示される

**対処法:**
```bash
git config --global core.quotepath false
```

### .DS_Storeファイルが邪魔

#### 症状: macOSが自動生成する `.DS_Store` がGitに含まれてしまう

**対処法1: .gitignoreに追加**
```bash
echo ".DS_Store" >> .gitignore
git add .gitignore
git commit -m ".gitignoreを更新"
git push origin main
```

**対処法2: 既にコミットしてしまった場合**
```bash
# Gitから削除（ファイル自体は残る）
git rm --cached .DS_Store
git rm --cached -r **/.DS_Store

# コミット & プッシュ
git commit -m ".DS_Storeを削除"
git push origin main
```

**対処法3: グローバルに設定**
```bash
echo ".DS_Store" >> ~/.gitignore_global
git config --global core.excludesfile ~/.gitignore_global
```

### VSCodeでGitが動かない

#### 症状: 「Git が見つかりません」

**対処法1: VSCodeを再起動**
1. `Command + Q` で完全終了
2. VSCodeを再起動

**対処法2: Gitのパスを設定**
1. `Command + ,` で設定を開く
2. 「git.path」を検索
3. 以下のいずれかを入力:
   - `/usr/bin/git`
   - `/usr/local/bin/git`
   - `/opt/homebrew/bin/git`

**対処法3: Gitのパスを確認**
```bash
which git
```

表示されたパスをVSCodeの設定に入力

### パスワードを何度も聞かれる

#### 症状: HTTPSでクローン・プッシュするたびにパスワードを要求される

**対処法1: SSHに切り替え（推奨）**
```bash
git remote set-url origin git@github.com:ユーザー名/リポジトリ名.git
```

**対処法2: 認証情報をキャッシュ**
```bash
git config --global credential.helper osxkeychain
```

### ファイルサイズが大きすぎる

#### 症状: `File is XXX MB; this exceeds GitHub's file size limit of 100 MB`

**対処法1: ファイルを.gitignoreに追加**
```bash
echo "large_file.csv" >> .gitignore
git rm --cached large_file.csv
git commit -m "大きなファイルを除外"
git push origin main
```

**対処法2: Git LFSを使う**
```bash
brew install git-lfs
git lfs install
git lfs track "*.csv"
git add .gitattributes
git commit -m "LFSを設定"
git add large_file.csv
git commit -m "大きなファイルを追加"
git push origin main
```

### ブランチ名が間違っている

#### 症状: `error: src refspec main does not match any`

**原因:** ブランチ名が `main` ではなく `master`

**対処法:**
```bash
# 現在のブランチを確認
git branch

# masterの場合
git push origin master

# mainに変更したい場合
git branch -m master main
git push -u origin main
```

### 間違えてコミットした

#### 直前のコミットを取り消したい

**対処法1: コミット取り消し（変更は保持）**
```bash
git reset --soft HEAD^
```

**対処法2: コミット取り消し（変更も削除）**
```bash
git reset --hard HEAD^
```

⚠️ **注意:** `--hard` はファイルの変更も消えるので慎重に！

#### 間違えたファイルをコミットから除外したい

```bash
git reset --soft HEAD^
git restore --staged 除外したいファイル
git commit -m "修正版"
git push origin main
```

### ターミナルが開かない

#### VSCodeでターミナルが開かない

**対処法1: ショートカットを試す**
- `Control + @`（バッククォート）
- `Command + J`（パネルを開く）

**対処法2: メニューから開く**
「表示」→「ターミナル」

**対処法3: コマンドパレットから**
1. `Command + Shift + P`
2. 「ターミナル: 新しいターミナルを作成」

**対処法4: デフォルトシェルを設定**
1. `Command + Shift + P`
2. 「ターミナル: 既定のプロファイルを選択」
3. 「zsh」または「bash」を選択

### リポジトリが壊れた

#### 症状: 原因不明のエラーが連続

**最終手段: リポジトリを再クローン**

1. **作業中のファイルをバックアップ**
```bash
# 現在のフォルダ名を変更
cd ~/Documents/GitHub
mv my-repo my-repo-backup
```

2. **リポジトリを再クローン**
```bash
git clone git@github.com:ユーザー名/リポジトリ名.git
```

3. **バックアップから必要なファイルをコピー**
```bash
cp my-repo-backup/your-file.py my-repo/
```

4. **通常通りコミット & プッシュ**

---

## 🙋 よくある質問（FAQ）

### Q1: コミットメッセージは日本語でもいいですか？

**A:** はい、問題ありません！

- ✅ **個人プロジェクト:** 日本語でOK
- ✅ **日本人チーム:** 日本語でOK
- ⚠️ **国際的なプロジェクト:** 英語を推奨
- ⚠️ **オープンソース:** 英語を推奨

**例:**
```bash
# 日本語
git commit -m "ログイン機能を追加"

# 英語
git commit -m "Add login feature"
```

### Q2: `main` と `master` どちらを使えばいいですか？

**A:** 新しいリポジトリは `main` を使ってください。

- **2020年10月以降:** GitHubのデフォルトは `main`
- **それ以前:** `master` が使われていた

**古いリポジトリを `main` に変更する方法:**
```bash
git branch -m master main
git push -u origin main
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
```

### Q3: プッシュとプルの違いは？

**A:**
- **プッシュ (push):** ローカルの変更をGitHubに送信（アップロード）
- **プル (pull):** GitHubの最新版をローカルに取得（ダウンロード）

**覚え方:**
- プッシュ = 押し出す = 📤
- プル = 引っ張る = 📥

### Q4: VSCodeとターミナル、どちらを使うべきですか？

**A:** 両方使えると便利です！

**初心者:**
- VSCodeのGUI操作から始める
- 視覚的で分かりやすい

**中級者:**
- ターミナルも使う
- コマンドを理解すると応用が効く

**最終的には:**
- 簡単な操作 → VSCode
- 複雑な操作 → ターミナル

### Q5: 複数のMacで同じリポジトリを使えますか？

**A:** はい、できます！

**手順:**
1. 各Macでリポジトリをクローン
2. 作業前に `git pull`
3. 作業後に `git push`

これで常に同期できます。

**注意点:**
- 各Macで必ずプル・プッシュを忘れずに
- 同時に同じファイルを編集するとコンフリクトが発生する可能性

### Q6: Gitの設定を変更したいのですが？

**A:** `git config` コマンドを使います。

**設定の確認:**
```bash
git config --global --list
```

**名前を変更:**
```bash
git config --global user.name "新しい名前"
```

**メールアドレスを変更:**
```bash
git config --global user.email "new.email@example.com"
```

**エディタを変更:**
```bash
git config --global core.editor "code --wait"
```

### Q7: GitHubに秘密情報を間違えてアップロードしてしまいました！

**A:** すぐに以下を実行してください：

1. **パスワードやAPIキーを即座に変更**
2. **リポジトリをプライベートに変更**（Settings → Change visibility）
3. **該当ファイルを削除**
```bash
git rm 該当ファイル
git commit -m "秘密情報を削除"
git push origin main
```

⚠️ **重要:** コミット履歴には残ってしまうので、本当に重要な情報の場合はGitHubサポートに相談してください。

**今後の対策:**
- `.env` ファイルに秘密情報を保存
- `.gitignore` に `.env` を追加
- 環境変数を使用

### Q8: ブランチは何ですか？使う必要がありますか？

**A:** ブランチは作業を分けるための機能です。

**初心者:**
- まずは `main` ブランチだけでOK
- 慣れてきたらブランチを学習

**ブランチの利点:**
- 機能ごとに作業を分けられる
- 本番環境に影響を与えずに開発できる
- 複数人で並行作業できる

**基本的な使い方:**
```bash
# 新しいブランチを作成
git checkout -b feature-login

# 作業する

# mainブランチに戻る
git checkout main

# ブランチをマージ
git merge feature-login
```

### Q9: Gitのコマンドが覚えられません

**A:** 大丈夫です！よく使うコマンドは限られています。

**最も使う5つのコマンド:**
```bash
git status    # 状態確認
git add .     # ステージング
git commit    # コミット
git pull      # 取得
git push      # 送信
```

**コツ:**
- VSCodeのGUIを使う
- このガイドの[コマンド早見表](#コマンド早見表)をブックマーク
- 使いながら覚える

### Q10: GitとGitHubの違いは？

**A:**
- **Git:** バージョン管理システム（ソフトウェア）
- **GitHub:** GitリポジトリをホスティングするWebサービス

**例え:**
- Git = 写真管理アプリ
- GitHub = 写真を保存するクラウドサービス

### Q11: フォーク（Fork）とは何ですか？

**A:** 他の人のリポジトリを自分のアカウントにコピーする機能です。

**使用例:**
1. 他の人のプロジェクトを改善したい
2. 自分用にカスタマイズしたい
3. プルリクエストを送りたい

**方法:**
1. GitHubで対象のリポジトリを開く
2. 右上の「Fork」ボタンをクリック
3. 自分のアカウントにコピーされる

### Q12: プルリクエスト（Pull Request）とは何ですか？

**A:** 自分の変更を他の人のリポジトリに取り込んでもらうためのリクエストです。

**使用例:**
- オープンソースプロジェクトへの貢献
- チーム開発でのコードレビュー

**基本的な流れ:**
1. リポジトリをフォーク
2. ブランチを作成
3. 変更をコミット & プッシュ
4. GitHubでプルリクエストを作成
5. レビューを受ける
6. 承認されたらマージ

---

## 🎓 次のステップ

基本をマスターしたら、以下を学習しましょう：

### 1. ブランチの使い方

**ブランチとは:** 作業を分けるための仕組み

**メリット:**
- 機能ごとに開発できる
- 本番環境に影響を与えない
- 複数人で並行作業できる

**基本コマンド:**
```bash
# ブランチ一覧
git branch

# 新しいブランチを作成
git branch feature-login

# ブランチを切り替え
git checkout feature-login

# 作成と切り替えを同時に
git checkout -b feature-login

# ブランチを削除
git branch -d feature-login

# ブランチをマージ
git checkout main
git merge feature-login
```

### 2. プルリクエスト（Pull Request）

**プルリクエストとは:** コードレビューを受けるための仕組み

**基本の流れ:**
1. ブランチを作成して作業
2. GitHubにプッシュ
3. GitHub上でプルリクエストを作成
4. レビューを受ける
5. 承認されたらmainブランチにマージ

### 3. .gitignoreの活用

**よく使う.gitignoreパターン:**

```
# macOS
.DS_Store

# Python
__pycache__/
*.py[cod]
.env
venv/

# Jupyter
.ipynb_checkpoints

# データファイル
*.csv
*.xlsx
data/

# VSCode
.vscode/
```

### 4. GitHub Actions

**GitHub Actionsとは:** 自動テスト・自動デプロイの仕組み

**できること:**
- コードをプッシュしたら自動テスト
- mainにマージしたら自動デプロイ
- 定期的にスクリプトを実行

### 5. Gitの高度なコマンド

```bash
# スタッシュ（一時保存）
git stash               # 変更を一時保存
git stash pop           # 一時保存を戻す

# リベース
git rebase main         # コミット履歴を整理

# チェリーピック
git cherry-pick コミットID  # 特定のコミットだけ取り込む

# タグ
git tag v1.0.0          # バージョンタグを作成
git push origin v1.0.0  # タグをプッシュ
```

### 6. GitHubの便利機能

- **Issues:** タスク管理
- **Projects:** プロジェクト管理
- **Wiki:** ドキュメント作成
- **GitHub Pages:** 静的サイトのホスティング
- **GitHub Copilot:** AI コーディングアシスタント

---

## 📚 参考リンク集

### 公式ドキュメント

- [Git公式サイト](https://git-scm.com/)
- [Git公式ドキュメント（日本語）](https://git-scm.com/book/ja/v2)
- [GitHub Docs（日本語）](https://docs.github.com/ja)
- [VSCode公式サイト](https://code.visualstudio.com/)
- [VSCode Git統合](https://code.visualstudio.com/docs/sourcecontrol/overview)

### 学習リソース

- [サル先生のGit入門](https://backlog.com/ja/git-tutorial/)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=ja)（インタラクティブ学習）
- [GitHub Skills](https://skills.github.com/)（無料コース）

### コミュニティ

- [GitHub Community](https://github.community/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/git)

---

## 🔖 コマンド早見表

### 基本コマンド

```bash
# 状態確認
git status                    # 現在の状態
git log                       # コミット履歴
git log --oneline             # コミット履歴（簡潔版）
git log --graph --all         # コミット履歴（グラフ表示）

# ステージング
git add .                     # すべて追加
git add ファイル名            # 特定ファイル
git add *.py                  # 特定の種類のファイル
git reset ファイル名          # ステージング取り消し

# コミット
git commit -m "メッセージ"    # コミット
git commit -am "メッセージ"   # add + commit
git commit --amend            # 直前のコミットを修正

# プッシュ・プル
git push origin main          # プッシュ
git pull origin main          # プル
git fetch                     # リモートの情報だけ取得

# ブランチ
git branch                    # ブランチ一覧
git branch 名前               # ブランチ作成
git checkout 名前             # ブランチ切り替え
git checkout -b 名前          # 作成 + 切り替え
git merge ブランチ名          # マージ
git branch -d 名前            # ブランチ削除

# 差分確認
git diff                      # 変更内容を表示
git diff --staged             # ステージ済みの変更

# 取り消し
git restore ファイル名        # ファイルの変更を取り消し
git restore --staged ファイル名  # ステージング取り消し
git reset --soft HEAD^        # 直前のコミット取り消し（変更保持）
git reset --hard HEAD^        # 直前のコミット取り消し（変更削除）

# リモート
git remote -v                 # リモートリポジトリ確認
git remote add origin URL     # リモート追加
git remote set-url origin URL # リモートURL変更
```

### 設定コマンド

```bash
# グローバル設定
git config --global user.name "名前"
git config --global user.email "メール"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main

# 設定確認
git config --global --list
git config user.name
git config user.email
```

---

## ✅ 最終チェックリスト

すべて完了したかチェックしましょう！

### 基本設定
- [ ] Gitがインストールされている（`git --version`）
- [ ] Gitの初期設定完了（user.name, user.email）
- [ ] GitHubアカウントを作成した
- [ ] VSCodeをインストールした
- [ ] VSCodeを日本語化した
- [ ] VSCodeとGitHubを連携した

### SSH設定
- [ ] SSHキーを生成した
- [ ] GitHubにSSHキーを登録した
- [ ] SSH接続テストが成功した（`ssh -T git@github.com`）
- [ ] SSH設定ファイルを作成した

### リポジトリ操作
- [ ] リポジトリを作成できた
- [ ] リポジトリをクローンできた
- [ ] VSCodeでプロジェクトを開けた

### Git操作（VSCode）
- [ ] ファイルを編集できた
- [ ] ソース管理パネルの使い方を理解した
- [ ] ファイルをステージングできた
- [ ] コミットができた
- [ ] GitHubにプッシュできた
- [ ] GitHubからプルできた

### Git操作（ターミナル）
- [ ] `git status` で状態確認ができた
- [ ] `git add .` でステージングできた
- [ ] `git commit` でコミットできた
- [ ] `git push` でプッシュできた
- [ ] `git pull` でプルできた

### 実践
- [ ] 新しいファイルを作成してアップロードできた
- [ ] 複数ファイルを一度にアップロードできた
- [ ] .gitignoreを作成して使えた
- [ ] GitHubで変更が確認できた

### トラブル対応
- [ ] エラーメッセージを読んで対処できる
- [ ] コンフリクトの解決方法を知っている
- [ ] このガイドで問題を解決できる

---

## 🎉 おめでとうございます！

このガイドを完了したあなたは、もう立派なGit/GitHub使いです！

**これからできること:**
- ✅ コードをバージョン管理
- ✅ GitHubでコードを保存・共有
- ✅ チームでの共同開発
- ✅ オープンソースプロジェクトへの貢献
- ✅ ポートフォリオの作成

**継続的な学習のために:**
1. 毎日少しずつ使ってみる
2. 小さなプロジェクトから始める
3. わからないことがあれば、このガイドを見返す
4. GitHubの他のプロジェクトを見て学ぶ
5. コミュニティに参加する

**最後に:**
- このガイドは常に手元に置いておきましょう
- 困ったときはトラブルシューティングセクションを確認
- 新しいことに挑戦し続けてください

あなたの開発ライフが素晴らしいものになりますように！

**Happy Coding! 🚀**

---

## 📮 このガイドについて

**バージョン:** 1.0（完全版）
**対応OS:** macOS 11 Big Sur以降
**最終更新:** 2025年10月

**このガイドの特徴:**
- ✅ 他の資料を参照する必要なし
- ✅ 完全な初心者対応
- ✅ すべての例外・トラブルをカバー
- ✅ 実践的なシナリオ付き
- ✅ VSCodeとターミナル両対応

**このガイドで学べること:**
1. Gitの基礎から実践まで
2. GitHubの使い方
3. VSCodeとの連携
4. トラブルシューティング
5. 実務で使えるワークフロー

このガイドがあなたの開発の第一歩をサポートできれば幸いです！