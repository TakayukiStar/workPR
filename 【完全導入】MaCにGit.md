# Mac初心者のためのVSCode×GitHub完全ガイド

## 📋 目次
1. [事前準備](#事前準備)
2. [Gitのインストール](#gitのインストール)
3. [GitHubアカウント作成](#githubアカウント作成)
4. [VSCodeのインストールと設定](#vscodeのインストールと設定)
5. [SSHキーの設定（推奨）](#sshキーの設定推奨)
6. [リポジトリのクローン](#リポジトリのクローン)
7. [基本的なGit操作](#基本的なgit操作)
8. [トラブルシューティング](#トラブルシューティング)

---

## 🎯 事前準備

### 必要なもの
- macOS搭載のMac（Intel/Apple SiliconどちらでもOK）
- インターネット接続
- Gmailなどのメールアドレス

---

## 🔧 Gitのインストール

### ステップ1: Gitがインストール済みか確認

1. **ターミナルを開く**
   - Finder → アプリケーション → ユーティリティ → ターミナル
   - または、Spotlight検索（Command + Space）で「ターミナル」と入力

2. **以下のコマンドを入力してEnter**
```bash
git --version
```

3. **結果の確認**
   - `git version 2.xx.x` のように表示されたら → **すでにインストール済み！次のセクションへ**
   - `command not found` と表示されたら → 次のステップへ

### ステップ2: Homebrewをインストール（Gitがない場合）

1. **ターミナルで以下のコマンドを実行**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. **パスワードを求められたら入力**（入力中は画面に表示されませんが正常です）

3. **インストール完了後、画面の指示に従う**
   - Apple Siliconの場合、追加コマンドの実行が必要な場合があります

### ステップ3: Gitをインストール

```bash
brew install git
```

### ステップ4: Gitの初期設定

```bash
git config --global user.name "あなたの名前"
git config --global user.email "your.email@example.com"
```

**例:**
```bash
git config --global user.name "Taro Yamada"
git config --global user.email "taro.yamada@gmail.com"
```

---

## 👤 GitHubアカウント作成

### ステップ1: GitHubにアクセス

1. ブラウザで https://github.com にアクセス
2. 右上の「Sign up」をクリック

### ステップ2: アカウント情報を入力

1. メールアドレスを入力
2. パスワードを設定（強力なものを推奨）
3. ユーザー名を決定（後から変更可能）
4. 認証パズルを完了

### ステップ3: メール認証

1. 登録したメールアドレスに届いた認証コードを入力
2. アカウント作成完了！

---

## 💻 VSCodeのインストールと設定

### ステップ1: VSCodeをダウンロード

1. https://code.visualstudio.com にアクセス
2. 「Download for Mac」をクリック
3. ダウンロードした `.zip` ファイルを開く

### ステップ2: VSCodeをインストール

1. 解凍された `Visual Studio Code.app` を
2. アプリケーションフォルダにドラッグ＆ドロップ

### ステップ3: VSCodeを起動

1. Launchpadまたはアプリケーションフォルダから起動
2. 初回起動時、「開発元を確認できません」と表示されたら
   - システム環境設定 → セキュリティとプライバシー → 「このまま開く」

### ステップ4: 日本語化（オプション）

1. VSCodeで `Command + Shift + X` を押す（拡張機能を開く）
2. 検索ボックスに「Japanese」と入力
3. 「Japanese Language Pack for Visual Studio Code」をインストール
4. VSCodeを再起動

### ステップ5: GitHubとの連携

1. VSCodeの左サイドバーから「アカウント」アイコン（人型）をクリック
2. 「GitHubでサインイン」を選択
3. ブラウザが開くので「Authorize Visual-Studio-Code」をクリック
4. VSCodeに戻ると連携完了！

---

## 🔐 SSHキーの設定（推奨）

SSHキーを使うと、毎回パスワードを入力せずにGitHubとやり取りできます。

### ステップ1: SSHキーの存在確認

```bash
ls -al ~/.ssh
```

`id_ed25519.pub` や `id_rsa.pub` が表示されたら既にキーが存在します → ステップ3へ

### ステップ2: 新しいSSHキーを生成

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

1. ファイルの保存場所を聞かれたら **Enterを押す**（デフォルトでOK）
2. パスフレーズを聞かれたら **Enterを2回押す**（空欄でOK）

### ステップ3: SSHキーをクリップボードにコピー

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

### ステップ4: GitHubにSSHキーを登録

1. https://github.com/settings/keys にアクセス
2. 「New SSH key」をクリック
3. Title: 「My Mac」など分かりやすい名前を入力
4. Key: `Command + V` でペースト
5. 「Add SSH key」をクリック

### ステップ5: 接続テスト

```bash
ssh -T git@github.com
```

「Hi ユーザー名! You've successfully authenticated」と表示されたら成功！

---

## 📥 リポジトリのクローン

### 方法1: VSCodeから直接クローン（初心者におすすめ）

#### ステップ1: コマンドパレットを開く

`Command + Shift + P` を押す

#### ステップ2: Gitクローンを実行

1. 「Git: Clone」と入力してEnter
2. 「GitHubからクローン」を選択
3. クローンしたいリポジトリを選択（または検索）
4. 保存先フォルダを選択（例: `~/Documents/GitHub`）
5. 「リポジトリの場所として選択」をクリック

### 方法2: ターミナルからクローン

#### ステップ1: クローン先のフォルダに移動

```bash
cd ~/Documents
mkdir GitHub
cd GitHub
```

#### ステップ2: リポジトリをクローン

**SSHを使う場合（推奨）:**
```bash
git clone git@github.com:ユーザー名/リポジトリ名.git
```

**HTTPSを使う場合:**
```bash
git clone https://github.com/ユーザー名/リポジトリ名.git
```

**例:**
```bash
git clone git@github.com:octocat/Hello-World.git
```

#### ステップ3: クローンしたフォルダに移動

```bash
cd リポジトリ名
```

#### ステップ4: VSCodeで開く

```bash
code .
```

---

## 🚀 基本的なGit操作

### VSCodeのGUI操作（視覚的で分かりやすい！）

#### 1. ファイルの変更を確認

1. 左サイドバーの「ソース管理」アイコン（枝分かれマーク）をクリック
2. 変更されたファイルが一覧表示されます

#### 2. ファイルをステージング（git add）

- **個別にステージング**: ファイル名の右にある「+」ボタンをクリック
- **すべてステージング**: 「変更」の右にある「+」ボタンをクリック

#### 3. コミット（git commit）

1. 上部のメッセージボックスに変更内容を入力（例: 「データ分析スクリプトを追加」）
2. `Command + Enter` または「コミット」ボタンをクリック

#### 4. プッシュ（git push）

1. 「変更の同期」ボタンをクリック
2. または、「...」メニュー → 「プッシュ」

### ターミナル操作（コマンドで理解を深める）

#### 現在の状態を確認

```bash
git status
```

これで何が変更されているかが分かります。

#### すべてのファイルをステージング

```bash
git add .
```

`.` は「すべて」という意味です。

#### 特定のファイルだけステージング

```bash
git add ファイル名
```

**例:**
```bash
git add script.py
git add Papers/analysis.csv
```

#### コミット

```bash
git commit -m "コミットメッセージ"
```

**例:**
```bash
git commit -m "ゴルフスイング分析スクリプトを追加"
```

#### GitHubにプッシュ

```bash
git push origin main
```

`main` はブランチ名です（古いリポジトリでは `master` の場合もあります）。

#### GitHubから最新版を取得（プル）

```bash
git pull origin main
```

---

## 💡 よく使うワークフロー

### 基本の流れ

```bash
# 1. 最新版を取得
git pull origin main

# 2. ファイルを編集
# （VSCodeで編集作業）

# 3. 変更を確認
git status

# 4. すべての変更をステージング
git add .

# 5. コミット
git commit -m "変更内容の説明"

# 6. GitHubにプッシュ
git push origin main
```

### VSCodeでの流れ

1. ファイルを編集
2. ソース管理アイコンをクリック
3. 変更をすべてステージング（+ボタン）
4. コミットメッセージを入力
5. `Command + Enter` でコミット
6. 「変更の同期」でプッシュ

---

## 🐛 トラブルシューティング

### ❌ エラー: `Permission denied (publickey)`

**原因:** SSHキーが正しく設定されていない

**解決策:**
1. SSHキーの設定セクションを再確認
2. または、HTTPSを使う

```bash
git remote set-url origin https://github.com/ユーザー名/リポジトリ名.git
```

### ❌ エラー: `fatal: not a git repository`

**原因:** Gitリポジトリのフォルダ外で実行している

**解決策:**
```bash
cd 正しいフォルダ名
```

### ❌ エラー: `Your branch is behind 'origin/main'`

**原因:** ローカルが古い状態

**解決策:**
```bash
git pull origin main
```

### ❌ コンフリクト（競合）が発生

**原因:** 同じファイルを複数人が編集した

**解決策:**
1. VSCodeでコンフリクトが表示されます
2. 「現在の変更を採用」「入力側の変更を採用」「両方の変更を保持」から選択
3. 選択後、再度コミット＆プッシュ

### 💡 日本語ファイル名が文字化け

```bash
git config --global core.quotepath false
```

---

## 🎓 次のステップ

慣れてきたら以下を学習しましょう：

1. **ブランチの使い方** - 機能ごとに作業を分ける
2. **プルリクエスト** - コードレビューを受ける
3. **.gitignore** - 不要なファイルを除外
4. **GitHub Actions** - 自動テスト・デプロイ

---

## 📚 便利なリンク

- [Git公式ドキュメント（日本語）](https://git-scm.com/book/ja/v2)
- [GitHub Docs（日本語）](https://docs.github.com/ja)
- [VSCode Git統合](https://code.visualstudio.com/docs/sourcecontrol/overview)

---

## 🙋 よくある質問

**Q: コミットメッセージは日本語でもいいですか？**  
A: はい、問題ありません！ただし、国際的なプロジェクトでは英語が推奨されます。

**Q: 間違えてコミットしてしまいました！**  
A: 直前のコミットなら以下で取り消せます：
```bash
git reset --soft HEAD^
```

**Q: GitHubに秘密情報をアップロードしてしまいました！**  
A: すぐにリポジトリを削除し、パスワードやAPIキーを変更してください。コミット履歴からの完全削除は複雑です。

---

## ✅ チェックリスト

完了したらチェック！

- [ ] Gitがインストールされている
- [ ] GitHubアカウントを作成した
- [ ] VSCodeをインストールした
- [ ] VSCodeとGitHubを連携した
- [ ] SSHキーを設定した（推奨）
- [ ] リポジトリをクローンできた
- [ ] `git add .` → `git commit` → `git push` の流れを理解した
- [ ] VSCodeのGUI操作を試した

---

**お疲れ様でした！これであなたもGitHub使いです！🎉**

何か困ったことがあれば、このガイドを見返してください。
練習を重ねれば、すぐに慣れますよ！
