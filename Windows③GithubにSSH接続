# GitHub SSH 接続 完全ガイド 🚀 【Windows版】

**【エラー完全対応版 - このガイドだけで絶対できる！】**

Windows 10/11 + VSCode 環境で GitHub に SSH 接続する方法を、どんなエラーが出ても解決できるよう超詳しく解説します。実際の初心者の方が遭遇したエラーをすべて網羅しています。

---

## 📖 目次

**基本設定（必須）:**

1. [🚨 最初に必ずやること](#最初に必ずやること)
2. [🎯 ターミナル（Git Bash）の基礎知識](#ターミナルの基礎知識)
3. [ステップ 0: 現在の状態を確認](#ステップ0)
4. [ステップ 1: SSH キーを生成](#ステップ1)
5. [ステップ 2: SSH Agent に登録](#ステップ2)
6. [ステップ 3: GitHub に登録](#ステップ3)
7. [ステップ 4: 接続テスト](#ステップ4)
8. [ステップ 5: Git 初期設定](#ステップ5) ← ここまで必須

**\8.完了/ からの2つのルート:**

- 📚 **学習ルート**: [ステップ 6: 自分のリポジトリで練習](#ステップ6) → [ステップ 7: お客さんのリポジトリ](#お客さんのリポジトリ)
- 🚀 **実務ルート**: [ステップ 7: お客さんのリポジトリ](#お客さんのリポジトリ)へ直行

**困ったときは:**
9. [🔧 トラブルシューティング](#トラブルシューティング)
10. [📚 よくある質問](#よくある質問)

---

## <a id="最初に必ずやること"></a>🚨 最初に必ずやること（超重要！）

**このセクションをスキップすると、後で手戻りが発生します！必ずここから始めてください！**

### Git for Windows のインストール

Windows では、Git と SSH ツールを一緒にインストールします。

#### ステップ A: Git for Windows をダウンロード

1. ブラウザで以下の URL を開く：
   ```
   https://git-scm.com/download/win
   ```

2. 自動的にダウンロードが始まります
   - 「64-bit Git for Windows Setup」がダウンロードされる
   - ファイル名例：`Git-2.43.0-64-bit.exe`

3. ダウンロードが完了するまで待つ

#### ステップ B: Git for Windows をインストール

1. ダウンロードした `.exe` ファイルをダブルクリック

2. **インストール画面が表示されます。以下の推奨設定で進めてください：**

**画面1: ライセンス**
- 「Next」をクリック

**画面2: インストール先**
- デフォルトのまま「Next」をクリック
- 通常：`C:\Program Files\Git`

**画面3: コンポーネント選択**
- デフォルトのまま「Next」をクリック
- ✅ Additional icons（追加アイコン）
- ✅ Windows Explorer integration（右クリックメニュー統合）

**画面4: スタートメニューフォルダ**
- デフォルトのまま「Next」をクリック

**画面5: デフォルトエディタの選択**
- 「Use Visual Studio Code as Git's default editor」を選択（推奨）
- 「Next」をクリック

**画面6: 新規リポジトリの初期ブランチ名**
- 「Override the default branch name for new repositories」を選択
- `main` と入力（推奨）
- 「Next」をクリック

**画面7: PATH環境変数の調整**
- **重要！** 「Git from the command line and also from 3rd-party software」を選択
- 「Next」をクリック

**画面8: SSH実行ファイル**
- **重要！** 「Use bundled OpenSSH」を選択
- 「Next」をクリック

**画面9: HTTPS接続**
- 「Use the OpenSSL library」を選択
- 「Next」をクリック

**画面10: 改行コードの変換**
- **重要！** 「Checkout Windows-style, commit Unix-style line endings」を選択
- 「Next」をクリック

**画面11: ターミナルエミュレータ**
- 「Use MinTTY (the default terminal of MSYS2)」を選択（推奨）
- 「Next」をクリック

**画面12: git pull の動作**
- 「Default (fast-forward or merge)」を選択
- 「Next」をクリック

**画面13: 認証情報ヘルパー**
- 「Git Credential Manager」を選択
- 「Next」をクリック

**画面14: 追加オプション**
- デフォルトのまま「Next」をクリック

**画面15: 実験的機能**
- チェックなしのまま「Install」をクリック

3. **インストール完了まで待つ（1-3分）**

4. 「Finish」をクリック

#### ステップ C: インストール確認

**方法1: Git Bash を起動**

1. Windows キーを押す
2. 「Git Bash」と入力
3. 「Git Bash」が表示されたらクリック

黒い画面（ターミナル）が開けば OK！

**方法2: コマンドで確認**

Git Bash で以下を実行：

```bash
git --version
```

**✅ 成功の表示例：**
```
git version 2.43.0.windows.1
```

次に：

```bash
ssh -V
```

**✅ 成功の表示例：**
```
OpenSSH_9.5p1, OpenSSL 3.1.4 24 Oct 2023
```

**両方のバージョンが表示されれば完璧！次のセクションへ進んでください**

#### ❌ もし「command not found」と出た場合

**原因：** PATH が通っていない

**解決方法：**

1. Git Bash を一度閉じる
2. パソコンを再起動
3. もう一度 Git Bash を開いて確認

それでもダメな場合：
1. Git for Windows を再インストール
2. インストール時に「Git from the command line and also from 3rd-party software」を必ず選択

---

## <a id="ターミナルの基礎知識"></a>🎯 ターミナル（Git Bash）の基礎知識

### Git Bash の起動方法

**方法 1: スタートメニューから**
1. Windows キーを押す
2. 「Git Bash」と入力
3. クリック

**方法 2: 右クリックメニューから**
1. エクスプローラーで任意のフォルダを開く
2. 空白部分を右クリック
3. 「Git Bash Here」をクリック

**方法 3: VSCode の統合ターミナル**
1. VSCode を開く
2. `` Ctrl + ` ``（バッククォート）を押す
3. 右上の「+」横のドロップダウンで「Git Bash」を選択

### 通常の状態

```bash
user@DESKTOP-XXX MINGW64 ~
$
```

または

```bash
user@DESKTOP-XXX MINGW64 /c/Users/user
$
```

**この表示が出ていれば、コマンドを入力できます**

### 異常な状態と脱出方法

#### `>` と表示される

```bash
>
```

- **原因:** 改行や特殊文字の入力待ち、または引用符が閉じられていない
- **脱出方法:** `Ctrl + C` を押す

#### `dquote>` と表示される

```bash
dquote>
```

- **原因:** ダブルクォート（`"`）が閉じられていない
- **脱出方法:** `Ctrl + C` を押す

#### `quote>` と表示される

```bash
quote>
```

- **原因:** シングルクォート（`'`）が閉じられていない
- **脱出方法:** `Ctrl + C` を押す

### 困ったときの魔法のコマンド ✨

**どんな異常な状態でも:**

```
Ctrl + C
```

を押せば、コマンドがキャンセルされて通常の状態に戻ります。

**💡 覚えておこう:**
- `Ctrl + C` = キャンセル（今のコマンドを中断）
- `Ctrl + D` = ターミナルを終了（押さないように注意）

### Windows での パス表記

**Git Bash では2つのパス表記が使えます：**

**Unix形式（推奨）:**
```bash
~/.ssh/id_ed25519
/c/Users/YourName/.ssh/id_ed25519
```

**Windows形式：**
```
C:\Users\YourName\.ssh\id_ed25519
```

**💡 このガイドでは Unix 形式（`~/.ssh`）を使います。Git Bash ではこちらが標準です。**

---

## <a id="ステップ0"></a>ステップ 0: 現在の状態を確認する 🔍

まず、既に SSH キーがあるか確認しましょう。

**Git Bash を開いて**以下を実行:

```bash
ls -la ~/.ssh
```

### ケース 1: フォルダ自体が存在しない

```
ls: cannot access '/c/Users/YourName/.ssh': No such file or directory
```

**→ これは正常です！まっさらな状態なので、ステップ 1 に進んでください**

### ケース 2: フォルダはあるが、id_ed25519 がない

```
total 4
drwxr-xr-x 1 user 197121   0 Jan 15 10:00 ./
drwxr-xr-x 1 user 197121   0 Jan 15 10:00 ../
-rw-r--r-- 1 user 197121 222 Jan 15 09:30 known_hosts
```

**→ よくあるパターンです！.ssh フォルダは作られているけど、SSH キーがまだない状態**

このケースでは、以下を試すと失敗します:

```bash
ls -la ~/.ssh/id_ed25519*
```
```
ls: cannot access '/c/Users/YourName/.ssh/id_ed25519*': No such file or directory
```

**これは正常です。まだファイルがないだけなので、ステップ 1 でキーを作りましょう！**

### ケース 3: 古いタイプの SSH キー（id_rsa）がある

```
total 16
-rw-------  1 user 197121 2602 Jan 15 10:00 id_rsa
-rw-r--r--  1 user 197121  572 Jan 15 10:00 id_rsa.pub
-rw-r--r--  1 user 197121  222 Jan 15 09:30 known_hosts
```

**→ 既に SSH キーがあります！**

**選択肢:**
- **選択肢 A:** 既存の id_rsa キーを使う → ステップ 1 をスキップして、ステップ 2 に進み、すべてのコマンドで `id_ed25519` を `id_rsa` に置き換える
- **選択肢 B:** 新しい ed25519 キーを作る（推奨） → ステップ 1 に進む

### ケース 4: 既に id_ed25519 がある

```
total 16
-rw-------  1 user 197121 464 Jan 15 10:00 id_ed25519
-rw-r--r--  1 user 197121 103 Jan 15 10:00 id_ed25519.pub
-rw-r--r--  1 user 197121 222 Jan 15 09:30 known_hosts
```

**→ 完璧！既に SSH キーが作られています**

**ステップ 1 をスキップして、ステップ 2 に進んでください**

### 📝 結果の読み方

```
-rw-------  1 user 197121 464 Jan 15 10:00 id_ed25519      ← 秘密鍵（絶対に人に見せない）
-rw-r--r--  1 user 197121 103 Jan 15 10:00 id_ed25519.pub  ← 公開鍵（GitHubに登録する）
-rw-r--r--  1 user 197121 222 Jan 15 09:30 known_hosts     ← 接続履歴（自動で作られる）
-rw-r--r--  1 user 197121 150 Jan 15 09:45 config          ← 設定ファイル
```

**重要:**
- `id_ed25519` = 秘密鍵（誰にも見せてはダメ）
- `id_ed25519.pub` = 公開鍵（GitHub に登録する）
- この 2 つがセットで必要

---

## <a id="ステップ1"></a>ステップ 1: SSH キーを生成する 🔑

### 1-1. 事前確認（重要！）

まず、本当に SSH キーがないか再確認:

```bash
ls -la ~/.ssh/id_ed25519*
```

**「No such file or directory」と表示されたら:**
→ 正常です。キーがない状態なので、このまま進めてください

**2 つのファイルが表示されたら:**
→ 既にキーがあります。ステップ 2 に進んでください

### 1-2. .ssh ディレクトリを作成（念のため）

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
```

**何も表示されなければ OK です**（エラーメッセージが出なければ成功）

### 1-3. SSH キーを生成

以下のコマンドを実行します。  
**※ `your_email@example.com` の部分は、あなたの GitHub アカウントのメールアドレスに変更してください**

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

**例:**

```bash
ssh-keygen -t ed25519 -C "taro@example.com"
```

このコマンドを実行すると、いくつか質問されます。次のステップ 1-4 で答え方を説明します。

### 1-4. 質問に答える

**💡 間違えても大丈夫！**
- ✅ パスフレーズを入力してしまった → もう一度ステップ 1-3 からやり直せば OK
- ✅ 違う場所を指定してしまった → もう一度ステップ 1-3 からやり直せば OK
- ✅ 既にファイルがある場合 → 上書き確認が出る（y で上書き、n でキャンセル）

ステップ 1-3 のコマンドを実行すると、以下の質問が順番に表示されます：

**質問 1:** `Enter file in which to save the key (/c/Users/あなたの名前/.ssh/id_ed25519):`  
→ **何も入力せず、Enter キーを押す**

**質問 2:** `Enter passphrase (empty for no passphrase):`  
→ **何も入力せず、Enter キーを押す**

**質問 3:** `Enter same passphrase again:`  
→ **何も入力せず、Enter キーを押す**

**💡 ポイント:** 3 回とも Enter を押すだけ。何も入力しません！

### 1-5. 成功メッセージを確認

以下のような表示が出れば OK:

```
Your identification has been saved in /c/Users/あなたの名前/.ssh/id_ed25519
Your public key has been saved in /c/Users/あなたの名前/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:ランダムな文字列 your_email@example.com
The key's randomart image is:
+--[ED25519 256]--+
|    . o.o        |
|   . + = .       |
（アスキーアート）
+----[SHA256]-----+
```

**✅ この表示が出たら成功です！**

### 1-6. 確認（超重要！）

SSH キーが正しく作られたか確認:

```bash
ls -la ~/.ssh/id_ed25519*
```

**✅ 成功の表示:**

```
-rw-------  1 user 197121 464 Jan 15 10:00 /c/Users/user/.ssh/id_ed25519
-rw-r--r--  1 user 197121 103 Jan 15 10:00 /c/Users/user/.ssh/id_ed25519.pub
```

**2 つのファイルが表示されれば OK！次のステップへ！**

**❌ 失敗の表示:**

```
ls: cannot access '/c/Users/user/.ssh/id_ed25519*': No such file or directory
```

**この表示が出た場合:**
1. ステップ 1-3 のコマンドをもう一度実行
2. 質問には必ず 3 回 Enter を押す
3. エラーメッセージが出ていないか確認

### 🚨 ステップ 1 でよくある失敗

#### 失敗パターン A: コマンドが認識されない

```
bash: ssh-keygen: command not found
```

**原因:** Git for Windows が正しくインストールされていない

**解決方法:** [一番上に戻って](#最初に必ずやること)、Git for Windows を再インストールしてください。その後、ステップ 1-3 からやり直してください。

#### 失敗パターン B: 質問に答えた後、ファイルができない

**原因:** パスフレーズを入力してしまった、または別の場所を指定してしまった

**解決方法:** ステップ 1-3 からやり直し。質問にはすべて Enter のみを押す

#### 失敗パターン C: 既にファイルがあると言われる

```
/c/Users/user/.ssh/id_ed25519 already exists.
Overwrite (y/n)?
```

**既に SSH キーがありました！**

**選択肢:**
- `n` を押してキャンセル → ステップ 2 へ
- `y` を押して上書き → 新しいキーが作られる（古いキーは削除される）

---

## <a id="ステップ2"></a>ステップ 2: SSH Agent にキーを登録する 🎯

Windows では SSH Agent を手動で起動する必要があります。

### 2-1. SSH Agent サービスを有効化（重要！）

**このステップは Windows でのみ必要です。**

#### 方法 A: PowerShell で設定（推奨）

1. **PowerShell を管理者として開く:**
   - Windows キーを押す
   - 「PowerShell」と入力
   - 「Windows PowerShell」を右クリック
   - 「管理者として実行」をクリック
   - ユーザーアカウント制御で「はい」をクリック

2. **以下のコマンドを実行:**

```powershell
Get-Service -Name ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
```

3. **確認:**

```powershell
Get-Service ssh-agent
```

**✅ 成功の表示:**
```
Status   Name               DisplayName
------   ----               -----------
Running  ssh-agent          OpenSSH Authentication Agent
```

`Status` が `Running` になっていれば OK！

4. **PowerShell を閉じる**

#### 方法 B: サービス管理画面から設定

1. `Windows + R` を押す
2. `services.msc` と入力して Enter
3. 「OpenSSH Authentication Agent」を探す
4. ダブルクリック
5. 「スタートアップの種類」を「自動」に変更
6. 「開始」ボタンをクリック
7. 「OK」をクリック

### 2-2. Git Bash で SSH Agent を起動

**Git Bash を開いて**以下を実行:

```bash
eval "$(ssh-agent -s)"
```

**⚠️ コピペ推奨！タイプミスに注意！**

**よくあるタイプミス:**
- ❌ `eval "(ssh-agent -s)` ← `$` がない、`"` が 1 つ
- ❌ `eval $(ssh-agent -s)` ← `"` がない
- ✅ `eval "$(ssh-agent -s)"` ← 正しい

**💡 もし `dquote>` という表示になったら:**

これは**ダブルクォートが閉じられていない**状態です。

**脱出方法:**
1. `Ctrl + C` を押す（コマンドをキャンセル）
2. 正しいコマンドをコピペして実行

**✅ 成功メッセージ:**

```
Agent pid 12345
```

（数字は毎回違います）

### 2-3. 設定ファイルを作成

```bash
touch ~/.ssh/config
```

**何も表示されなければ OK**

次に、設定ファイルを編集します：

```bash
notepad ~/.ssh/config
```

または、VSCode を使う場合：

```bash
code ~/.ssh/config
```

メモ帳または VSCode が開きます（何も書かれていない白いウィンドウ）。

**💡 もし何か既に書かれている場合:** そのまま一番下に追加してください

### 2-4. 設定を記入

**💡 間違えても大丈夫！**
- ✅ 内容を間違えた → もう一度ファイルを開いて編集し直せば OK
- ✅ 保存し忘れた → もう一度開いて保存すれば OK
- ✅ 違う内容を書いた → 削除して正しい内容を書き直せば OK

開いたエディタに、以下を**そのまま**コピー&ペースト:

```
Host github.com
  AddKeysToAgent yes
  IdentityFile ~/.ssh/id_ed25519
```

**重要:**
- 行頭のスペース（インデント）もそのままコピー
- 何も変更しない
- 既に他の内容がある場合は、一番下に追加

**💡 Windows では `UseKeychain` は不要です（Mac専用の設定）**

### 2-5. 保存して閉じる

**メモ帳の場合:**
1. `Ctrl + S` で保存
2. メモ帳を閉じる

**VSCode の場合:**
1. `Ctrl + S` で保存
2. VSCode を閉じる、またはタブを閉じる

### 2-6. SSH キーを Agent に追加

Git Bash に戻って以下を実行:

```bash
ssh-add ~/.ssh/id_ed25519
```

**✅ 成功メッセージ:**

```
Identity added: /c/Users/あなたの名前/.ssh/id_ed25519 (your_email@example.com)
```

**🎉 このメッセージが出たら完璧です！**

### 🚨 ステップ 2 のエラー解決

#### エラー 1: `No such file or directory`

```bash
/c/Users/user/.ssh/id_ed25519: No such file or directory
```

**確認手順:**

**ステップ A: SSH キーがあるか確認**

```bash
ls -la ~/.ssh/id_ed25519*
```

**「No such file or directory」と出た場合:**  
→ ステップ 1 に戻って SSH キーを作成してください

**2 つのファイルが表示された場合:**  
→ ステップ B へ

**ステップ B: SSH Agent を起動し直す**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

#### エラー 2: `Could not open a connection to your authentication agent`

**原因:** SSH Agent サービスが起動していない

**解決方法:**

1. ステップ 2-1 の「SSH Agent サービスを有効化」をもう一度実行
2. その後：

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

#### エラー 3: `Error connecting to agent: No such file or directory`

**原因:** SSH Agent が起動していない

**解決方法:**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

それでもダメな場合：

1. Git Bash を閉じる
2. PowerShell を管理者として開く
3. 以下を実行：

```powershell
Restart-Service ssh-agent
Get-Service ssh-agent
```

4. Git Bash を開き直して、もう一度 `ssh-add` を実行

#### エラー 4: 古いタイプのキー（id_rsa）を使う場合

**ステップ 0 で id_rsa が表示された方:**

すべてのコマンドで `id_ed25519` を `id_rsa` に置き換えてください:

```bash
ssh-add ~/.ssh/id_rsa
```

---

## <a id="ステップ3"></a>ステップ 3: GitHub に SSH キーを登録する 🌐

### 3-1. SSH キー（公開鍵）をコピー

Git Bash で以下のいずれかを実行:

**方法 1: clip コマンドを使う（推奨）**

```bash
cat ~/.ssh/id_ed25519.pub | clip
```

**何も表示されなければ OK です！**（クリップボードにコピーされました）

**方法 2: 内容を表示してコピー**

```bash
cat ~/.ssh/id_ed25519.pub
```

`ssh-ed25519 AAAA...` で始まる長い文字列が表示されます：

1. その文字列全体をマウスでドラッグして選択
2. 右クリック → 「Copy」
3. または Git Bash の場合は `Shift + Insert` でコピー可能

**❌ 「No such file or directory」と出た場合:**

**確認ステップ 1:** ファイルがあるか確認

```bash
ls -la ~/.ssh/id_ed25519.pub
```

ファイルがない場合 → ステップ 1 からやり直し

**確認ステップ 2:** ファイルがある場合は、内容を表示

```bash
cat ~/.ssh/id_ed25519.pub
```

`ssh-ed25519 AAAA...` で始まる長い文字列が表示されたら:

1. その文字列全体をマウスでドラッグして選択
2. 右クリック → 「Copy」
3. 次のステップへ

### 3-2. GitHub にログイン

1. ブラウザで [github.com](https://github.com) を開く
2. ログインしていない場合はログイン

### 3-3. SSH 設定ページへ移動

**方法 1: 直接アクセス（おすすめ）**

以下の URL をブラウザで開く:

```
https://github.com/settings/keys
```

**方法 2: メニューから**

1. 右上のプロフィール画像をクリック
2. 「Settings」をクリック
3. 左サイドバーの「SSH and GPG keys」をクリック

### 3-4. 新しい SSH キーを追加

**💡 間違えても大丈夫！**
- ✅ 間違ったキーを登録してしまった → 削除して再登録できます
- ✅ タイトルを間違えた → 後から編集できます
- ✅ 違うアカウントに登録してしまった → 削除してやり直せます

**⚠️ 注意: この操作はやり直しが簡単なので、安心して進めてください！**

---

1. **「New SSH key」ボタン**（緑色）をクリック

2. **Title（タイトル）**に入力:
   - 例: `Windows PC`
   - 例: `My Laptop 2024`
   - 自分でわかる名前なら何でも OK

3. **Key type**は `Authentication Key` のまま（触らない）

4. **Key**の欄をクリック

5. `Ctrl + V` でペースト

6. **長い文字列が貼り付けられたことを確認**
   - `ssh-ed25519 AAAA...` で始まる
   - 1 行の長い文字列
   - 最後にメールアドレスが入っている

**❌ 何も貼り付けられない場合:**  
ステップ 3-1 をもう一度実行してください

7. **「Add SSH key」ボタン**をクリック

### 3-5. パスワード確認

GitHub のパスワードを入力して確認します。

**✅ 成功すると:**
- 一覧にあなたが追加したキーが表示されます
- 緑色のチェックマークが付いています
- タイトル（例: Windows PC）が表示されます

**🎉 おめでとうございます！GitHub に登録できました！**

---

## <a id="ステップ4"></a>ステップ 4: 接続テスト 🧪

### 4-1. GitHub に接続できるかテスト

Git Bash で以下を実行:

```bash
ssh -T git@github.com
```

### 4-2. 初回の質問に答える

**初めて接続する場合、以下のメッセージが出ます:**

```
The authenticity of host 'github.com (20.27.177.113)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

**→ `yes` と入力して Enter**

**💡 ポイント:** `y` だけではダメです。`yes` と完全に入力してください。

### 4-3. 成功メッセージを確認

**✅ 成功した場合:**

```
Hi あなたのGitHubユーザー名! You've successfully authenticated, but GitHub does not provide shell access.
```

**例:**

```
Hi yamada-taro! You've successfully authenticated, but GitHub does not provide shell access.
```

**🎉🎉🎉 このメッセージが出たら大成功！完璧に動いています！🎉🎉🎉**

「GitHub does not provide shell access」はエラーではありません。「認証成功したけど、シェルは使えないよ」という意味で、これが正常な成功メッセージです！

### 🚨 接続テストのエラー解決

#### エラー: `Permission denied (publickey)`

**完全な表示例:**

```
git@github.com: Permission denied (publickey).
```

**これは最もよくあるエラーです。落ち着いて対処しましょう！**

**原因:**
- GitHub に SSH キーが正しく登録されていない
- 違う SSH キーを登録してしまった
- SSH Agent に登録されていない

**解決ステップ 1: SSH Agent に登録されているか確認**

```bash
ssh-add -l
```

**✅ 以下のような表示が出れば OK:**

```
256 SHA256:ランダムな文字列 your_email@example.com (ED25519)
```

**❌ 「The agent has no identities」と出た場合:**

```bash
ssh-add ~/.ssh/id_ed25519
```

実行後、もう一度 `ssh-add -l` で確認

**❌ 「Could not open a connection to your authentication agent」と出た場合:**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add -l
```

**解決ステップ 2: GitHub に正しいキーが登録されているか確認**

**2-1. ローカルの公開鍵を表示:**

```bash
cat ~/.ssh/id_ed25519.pub
```

**2-2. 表示された内容をコピー**
- `ssh-ed25519 AAAA...` で始まる長い文字列
- 全体をマウスでドラッグして選択
- 右クリック → 「Copy」

**2-3. GitHub で確認:**

1. https://github.com/settings/keys を開く
2. 登録したキーをクリック
3. 表示された内容と、コピーした内容が**完全に一致**するか確認

**❌ 一致しない場合、または登録したキーがない場合:**

1. GitHub でそのキーを削除（あれば）
2. ステップ 3-4 からやり直し（正しいキーを再登録）

**解決ステップ 3: 再テスト**

```bash
ssh -T git@github.com
```

**それでも Permission denied が出る場合:**  
→ [完全リセット手順](#完全リセット手順)へ

#### エラー: `Connection timed out`

```
ssh: connect to host github.com port 22: Connection timed out
```

**原因:** ネットワークの問題、またはファイアウォール

**解決方法:**

1. インターネット接続を確認
2. 会社や学校のネットワークの場合、管理者に確認
3. Windows ファイアウォールを確認
4. 以下を試す:

```bash
ssh -T -p 443 git@ssh.github.com
```

成功したら、`~/.ssh/config` を編集:

```bash
notepad ~/.ssh/config
```

以下の内容に**書き換え**:

```
Host github.com
  Hostname ssh.github.com
  Port 443
  AddKeysToAgent yes
  IdentityFile ~/.ssh/id_ed25519
```

保存して閉じ、もう一度テスト：

```bash
ssh -T git@github.com
```

---

## <a id="ステップ5"></a>ステップ 5: Git の初期設定 ⚙️

### 5-1. ユーザー名を設定

**💡 間違えても大丈夫！**
- ✅ いつでも変更できます
- ✅ 何度でも実行できます
- ✅ 既存のコミットには影響しません（新しいコミットから適用）

**`Your Name` を自分の名前に変更して実行:**

```bash
git config --global user.name "Your Name"
```

例:

```bash
git config --global user.name "Taro Yamada"
```

何も表示されなければ OK です。

### 5-2. メールアドレスを設定

**💡 間違えても大丈夫！**
- ✅ いつでも変更できます
- ✅ 何度でも実行できます
- ✅ 既存のコミットには影響しません（新しいコミットから適用）

**GitHub のメールアドレスに変更して実行:**

```bash
git config --global user.email "your_email@example.com"
```

例:

```bash
git config --global user.email "taro@example.com"
```

### 5-3. デフォルトブランチ名を設定

```bash
git config --global init.defaultBranch main
```

**💡 後から変更できる？**  
**はい！いつでも簡単に変更可能です。間違えても全く問題ありません：**

```bash
git config --global init.defaultBranch develop  # 別の名前に変更
git config --global init.defaultBranch master   # masterに変更
git config --global init.defaultBranch 好きな名前  # 何でもOK
```

**安心してください：**
- ✅ この設定は何度でも変更できる
- ✅ 既存のリポジトリには影響しない（新規作成時のみ適用）
- ✅ 間違えても戻せる
- ✅ プロジェクトごとに違うブランチ名も使える

---

**💡 なぜ「main」を推奨するのか？**

この設定は、新しくリポジトリを作るときの最初のブランチ名を決めます。

**選択肢:**
- `main` ← **推奨！GitHub の現在の標準**
- `master` ← 以前の標準（古い）
- `develop` ← 開発用
- その他、好きな名前（実は何でも OK）

**main を推奨する理由:**

1. ✅ 2020 年以降、GitHub の新規リポジトリは `main` がデフォルト
2. ✅ 最新のベストプラクティス
3. ✅ 新しいプロジェクトで使われている標準
4. ✅ ローカルと GitHub で名前が一致して混乱しない

### 5-4. 改行コード設定（Windows重要！）

Windows特有の設定として、改行コードの自動変換を設定します：

```bash
git config --global core.autocrlf true
```

**これは何？**
- Windows: 改行コードは `CRLF`（`\r\n`）
- Mac/Linux: 改行コードは `LF`（`\n`）
- この設定により、自動的に適切な改行コードに変換されます

### 5-5. 設定確認

```bash
git config --global --list
```

**以下のような表示が出れば OK:**

```
user.name=Your Name
user.email=your_email@example.com
init.defaultbranch=main
core.autocrlf=true
```

**💡 他の設定が表示されても問題ありません！**

よく表示される他の設定：
- `credential.helper=manager-core` - パスワード保存設定（Windows標準）
- `core.editor=code --wait` - デフォルトエディタ設定
- `core.symlinks=false` - シンボリックリンク設定
- その他、過去に設定した内容

**重要なのは上記 4 つだけです。他は気にしなくて OK！**

---

**📚 次にどこへ進む？**

ここまで完了したら、2 つのルートがあります：

### ルート 1: 学習ルート（推奨）📚

**ステップ 6（自分のリポジトリで練習）→ ステップ 7（お客さんのリポジトリ）**

- まず自分のリポジトリで練習したい
- Git の操作に慣れてから実務に入りたい
- 時間に余裕がある

→ **次はステップ 6 へ進んでください**

### ルート 2: 実務ルート（最短）🚀

**ステップ 7（お客さんのリポジトリ）へ直行**

- すぐにお客さんのプロジェクトで作業を始めたい
- 既に Git の基礎知識がある
- 時間がない

→ **ステップ 6 をスキップして、ステップ 7 へ進んでください**

**💡 どちらでも OK！** 自分の状況に合わせて選んでください。

---

## <a id="ステップ6"></a>ステップ 6: VSCode で使ってみる 🎨

### 6-1. VSCode の準備

1. VSCode を開く
2. `Ctrl + ,` で設定を開く
3. 検索欄に `git.terminalAuthentication` と入力
4. チェックが付いていたら**外す**

### 6-2. テスト用リポジトリを作成

#### GitHub でリポジトリを作成

1. https://github.com を開く
2. 右上の「+」→「New repository」をクリック
3. Repository name: `test-ssh-connection` と入力
4. 「Public」を選択
5. 「Add a README file」に**チェックを入れる**
6. 「Create repository」をクリック

#### SSH URL をコピー

1. 作成されたリポジトリページで、緑色の「Code」ボタンをクリック
2. **「SSH」タブ**をクリック（重要！HTTPS ではない）
3. `git@github.com:ユーザー名/test-ssh-connection.git` のような形式の URL が表示される
4. 横のコピーボタン（📋 アイコン）をクリック

**💡 確認:** コピーした URL が `git@github.com:` で始まっていることを確認

### 6-3. VSCode でクローン

1. VSCode で `Ctrl + Shift + P` を押す
2. `Git: Clone` と入力して選択
3. コピーした SSH URL をペースト
4. Enter を押す
5. 保存先フォルダを選択
   - 例: `C:\Users\YourName\Documents\Projects\`
   - または: `C:\Users\YourName\Desktop\`
6. 「Select as Repository Destination」をクリック

**✅ 成功すると:**
- VSCode で新しいウィンドウが開く
- README.md が表示される
- 左下に「main」ブランチが表示される

**❌ エラーが出た場合:**

`Permission denied (publickey)` → ステップ 4 の接続テストをもう一度確認

`Host key verification failed` → Git Bash で一度接続テスト:

```bash
ssh -T git@github.com
```

`yes` を入力後、VSCode でもう一度クローン

**🎉 おめでとうございます！完璧に動いています！**

### 6-4. 使い方の基本

#### ファイルを変更して GitHub に反映する

1. **ファイルを編集**
   - README.md を開いて何か書いてみる
   - `Ctrl + S` で保存

2. **変更をステージング**
   - 左サイドバーの「ソース管理」アイコン（ブランチマーク）をクリック
   - 変更されたファイルの横の「+」をクリック

3. **コミット**
   - 上部のメッセージ欄に「Update README」など入力
   - 「✓ コミット」ボタンをクリック

4. **プッシュ**
   - 「変更の同期」ボタンをクリック
   - または「...」→「プッシュ」

5. **確認**
   - GitHub のリポジトリページを更新
   - 変更が反映されていれば OK！

---

## <a id="お客さんのリポジトリ"></a>🏢 お客さんの GitHub リポジトリに参加する方法

実際の開発現場では、お客さんや会社が所有する GitHub リポジトリに参加して作業することが一般的です。ここでは、その手順を詳しく解説します。

### 前提条件

このセクションを始める前に、**[ステップ 5: Git 初期設定](#ステップ5)まで完了していること**を確認してください。

**✅ 必要な準備:**
- ステップ 4: 接続テスト完了（`ssh -T git@github.com` が成功）
- ステップ 5: Git 初期設定完了（`user.name`と`user.email`を設定）

**💡 ステップ 6（自分のリポジトリで練習）は必須ではありません！**

- 練習したい方 → ステップ 6 を先にやってからこのセクションへ
- すぐ実務を始めたい方 → このセクションに直接進んで OK

### 登場人物の整理

- 🏢 **お客さん（リポジトリオーナー）**: リポジトリを所有している人。招待する側
- 👤 **あなた（開発メンバー）**: リポジトリに参加して開発する人。招待される側

---

## ステップ 7: お客さんのリポジトリに参加する 🤝

### 7-1. あなたの GitHub ユーザー名を確認する（👤 あなた）

お客さんに伝えるために、まず自分の GitHub ユーザー名を確認します。

**確認方法:**

1. https://github.com にログイン
2. 右上のプロフィール画像をクリック
3. 「Signed in as ユーザー名」と表示される部分があなたのユーザー名

**例:** `yamada-taro`

このユーザー名をお客さんに伝えてください。

**💡 連絡例文:**

```
お世話になっております。
GitHubの準備が整いました。
私のGitHubユーザー名は「yamada-taro」です。
リポジトリへの招待をお願いいたします。
```

---

### 7-2. お客さんがあなたを招待する（🏢 お客さん側の操作）

**このセクションは、お客さん（リポジトリオーナー）が実行します。**

お客さんに以下の手順を共有してください。

#### 手順 A: リポジトリにアクセス

1. GitHub にログイン
2. 招待したいリポジトリのページを開く
3. 上部メニューの「Settings」をクリック

#### 手順 B: Collaborators 設定を開く

1. 左サイドバーの「Collaborators and teams」をクリック
   - または「Access」→「Collaborators」
2. 「Add people」ボタン（緑色）をクリック

#### 手順 C: メンバーを追加

1. 検索欄に開発メンバーの GitHub ユーザー名を入力
   - 例: `yamada-taro`
2. 候補が表示されたらクリック
3. 権限レベルを選択:
   - **Write**: コードの読み書き、プッシュが可能（通常の開発メンバー向け）
   - **Maintain**: Write に加えて設定変更も可能
   - **Admin**: すべての権限（慎重に付与）
   - **Read**: 読み取り専用（コードレビューのみなど）

**💡 推奨:** 通常の開発メンバーには「Write」を付与

4. 「Add [ユーザー名] to this repository」ボタンをクリック

#### 手順 D: 招待完了

招待が送信されました！開発メンバーにメールが届きます。

**✅ 確認方法:**
- Collaborators 一覧に「Pending invite」と表示される
- 招待が承認されると、通常のメンバーとして表示される

---

### 7-3. 招待を承認する（👤 あなた）

お客さんから招待されると、以下の 2 つの方法で通知が届きます。

#### 方法 1: メールから承認

1. GitHub から「[お客さんのユーザー名] invited you to [リポジトリ名]」というメールが届く
2. メール内の「View invitation」ボタンをクリック
3. GitHub のページが開く
4. 「Accept invitation」ボタンをクリック

#### 方法 2: GitHub から直接承認

1. https://github.com にログイン
2. 右上のベルアイコン（通知）をクリック
3. 招待の通知が表示される
4. クリックして「Accept invitation」ボタンをクリック

**✅ 承認完了すると:**
- 「You now have access to [リポジトリ名]」と表示される
- そのリポジトリにアクセスできるようになる

---

### 7-4. リポジトリをクローンする（👤 あなた）

招待を承認したら、ローカルにリポジトリをクローンして作業を始めます。

#### ステップ A: リポジトリページを開く

1. https://github.com にログイン
2. 左サイドバーの「Repositories」をクリック
3. 招待されたリポジトリが表示される
4. リポジトリ名をクリック

#### ステップ B: SSH URL をコピー

1. 緑色の「Code」ボタンをクリック
2. **「SSH」タブ**をクリック（重要！HTTPS ではない）

**💡 警告メッセージが表示される場合:**

「SSH」タブを選択すると、以下のような警告が表示されることがあります：

```
You don't have any public SSH keys in your GitHub account.
You can add a new public key, or try cloning this repository via HTTPS.
```

**これは完全に無視して OK！問題ありません！**

**この警告の意味:**
- ❌ あなたの設定が間違っているわけではない
- ❌ あなたが SSH キーを登録していないわけではない
- ✅ **お客さん（リポジトリオーナー）のアカウント**に SSH キーが登録されていないだけ
- ✅ あなたは自分のアカウントに SSH キーを登録済み（ステップ 3 で完了）
- ✅ この警告は**お客さんの画面に出ているメッセージ**で、あなたには関係ない

**重要:** 警告の下に `git@github.com:...` の URL が表示されていれば、それを使ってください！

3. `git@github.com:お客さんのユーザー名/リポジトリ名.git` のような URL が表示される
4. コピーボタンをクリック

**💡 確認:** URL が `git@github.com:` で始まっていることを確認

**🚨 もし HTTPS の URL をコピーしてしまったら:**

もし間違えて「HTTPS」タブから URL をコピーした場合:
- URL: `https://github.com/...` で始まる
- これでも clone できますが、毎回パスワード入力が必要になります
- **必ず「SSH」タブに切り替えてください！**

#### ステップ C: リポジトリをクローンする

**2 つの方法があります。どちらでも OK！**

##### 方法 1: Git Bash からクローン（推奨）

**手順:**

1. **保存先フォルダに移動**

```bash
cd /c/Users/YourName/Documents/Projects
```

または、お客さんごとにフォルダを作る場合:

```bash
mkdir -p /c/Users/YourName/Documents/Projects/お客さん名
cd /c/Users/YourName/Documents/Projects/お客さん名
```

**💡 Windows のパスは Git Bash では以下のように変換されます:**
- `C:\Users\YourName\Documents` → `/c/Users/YourName/Documents`
- `D:\Projects` → `/d/Projects`

2. **クローン実行**

```bash
git clone git@github.com:ユーザー名/リポジトリ名.git
```

**例:**

```bash
git clone git@github.com:acme-corp/project-alpha.git
```

3. **成功メッセージを確認**

```
Cloning into 'project-alpha'...
remote: Enumerating objects: 100, done.
remote: Counting objects: 100% (100/100), done.
remote: Compressing objects: 100% (75/75), done.
remote: Total 100 (delta 25), reused 80 (delta 10), pack-reused 0
Receiving objects: 100% (100/100), 50.00 KiB | 5.00 MiB/s, done.
Resolving deltas: 100% (25/25), done.
```

**✅ この表示が出たら成功！**

4. **VSCode で開く**

```bash
cd リポジトリ名
code .
```

**💡 `code` コマンドが使えない場合:**

VSCode を開いて:
1. `Ctrl + Shift + P` を押す
2. `Shell Command: Install 'code' command in PATH` と入力して実行
3. Git Bash を再起動

その後、もう一度 `code .` を実行

---

##### 方法 2: VSCode からクローン

**手順:**

1. VSCode を開く
2. `Ctrl + Shift + P` を押す
3. `Git: Clone` と入力して選択
4. コピーした SSH URL をペースト
5. Enter を押す
6. 保存先フォルダを選択（プロジェクト用のフォルダ推奨）
   - 例: `C:\Users\YourName\Documents\Projects\お客さん名\`
7. 「Select as Repository Destination」をクリック

---

**どちらの方法でも:**

**✅ 成功すると:**
- VSCode で新しいウィンドウが開く
- リポジトリのファイルが表示される
- 左下にブランチ名が表示される（通常は `main` または `develop`）

**🎉 これで、お客さんのリポジトリで開発できます！**

---

### 🚨 もし HTTPS で clone してしまった場合

**症状:**
- clone はできた
- でも、プッシュやプルのたびにパスワード入力を求められる
- または、「Username for 'https://github.com':」と聞かれる

**原因:**
間違えて HTTPS の URL を使ってしまった

**対処法: 2 つの選択肢**

#### 選択肢 A: 削除して SSH でやり直す（簡単・推奨）

**まだ何も編集していない場合はこちら！**

**手順:**

1. **clone したフォルダを削除**

**エクスプローラーで削除:**
- 該当フォルダを右クリック → 削除
- または `Shift + Delete` で完全削除

**または Git Bash で削除:**

```bash
# リポジトリの親フォルダに移動
cd /c/Users/YourName/Documents/Projects/お客さん名/

# リポジトリフォルダを削除
rm -rf リポジトリ名
```

2. **もう一度正しくクローン**

```bash
# SSH URLを使ってクローン
git clone git@github.com:ユーザー名/リポジトリ名.git

# VSCodeで開く
cd リポジトリ名
code .
```

**💡 確認:** 今度は必ず「SSH」タブから URL をコピーして、`git@github.com:` で始まる URL を使う

#### 選択肢 B: リモート URL を SSH に変更（作業済みの場合）

**既にファイルを編集してしまった場合はこちら！**

**手順:**

1. **Git Bash でリポジトリフォルダに移動**

```bash
cd /c/Users/YourName/Documents/Projects/お客さん名/リポジトリ名
```

または VSCode でそのフォルダを開いて、統合ターミナルを使う（`` Ctrl + ` ``）

2. **現在のリモート URL を確認**

```bash
git remote -v
```

**表示例（HTTPS）:**

```
origin  https://github.com/お客さん/リポジトリ名.git (fetch)
origin  https://github.com/お客さん/リポジトリ名.git (push)
```

3. **SSH に変更**

```bash
git remote set-url origin git@github.com:お客さん/リポジトリ名.git
```

**⚠️ 重要:** `お客さん` と `リポジトリ名` は実際の名前に置き換えてください

**例:**

```bash
git remote set-url origin git@github.com:acme-corp/project-alpha.git
```

4. **確認**

```bash
git remote -v
```

**表示が SSH に変われば OK:**

```
origin  git@github.com:お客さん/リポジトリ名.git (fetch)
origin  git@github.com:お客さん/リポジトリ名.git (push)
```

5. **テスト**

```bash
git pull
```

**✅ パスワードを聞かれずに実行できれば OK！**

**❌ もしパスワードを聞かれたら:**
- URL が正しいか確認（`git remote -v`）
- SSH 接続テストを実行（`ssh -T git@github.com`）

---

**💡 どちらを選ぶ？**
- まだ何も作業していない → **選択肢 A（削除してやり直す）**
- 既にコミットやファイル編集をした → **選択肢 B（URL を変更）**

---

### 7-5. 作業の基本フロー（👤 あなた）

#### フローの全体像

```
1. 最新のコードを取得（Pull）
2. 新しいブランチを作成
3. コードを編集
4. コミット
5. プッシュ
6. プルリクエスト作成
7. レビュー・マージ
```

#### ステップ 1: 最新のコードを取得

作業を始める前に、必ず最新のコードを取得します。

**VSCode で:**
1. 左下のブランチ名の横の「↻」アイコンをクリック
2. または「...」→「プル」

**Git Bash で:**

```bash
git pull origin main
```

（`main`の部分は、プロジェクトのデフォルトブランチ名に合わせてください）

#### ステップ 2: 新しいブランチを作成

**💡 重要:** `main`ブランチで直接作業してはいけません！必ず作業用ブランチを作成します。

**VSCode で:**
1. 左下のブランチ名をクリック
2. 「新しいブランチの作成」を選択
3. ブランチ名を入力
   - 例: `feature/add-login-page`
   - 例: `fix/button-color`
   - 例: `update/readme`
4. Enter

**Git Bash で:**

```bash
git checkout -b feature/add-login-page
```

**💡 ブランチ名のベストプラクティス:**
- `feature/機能名` - 新機能追加
- `fix/修正内容` - バグ修正
- `update/更新内容` - 更新作業
- `refactor/リファクタリング内容` - コード整理

**お客さんからブランチ命名規則を指定される場合もあります。必ず確認しましょう！**

#### ステップ 3: コードを編集

通常通りコードを編集します。

#### ステップ 4: コミット

変更をコミットします。

**VSCode で:**
1. 左サイドバーの「ソース管理」アイコンをクリック
2. 変更されたファイルの横の「+」をクリック（ステージング）
3. コミットメッセージを入力
   - 例: `ログインページを追加`
   - 例: `ボタンの色を修正`
4. 「✓ コミット」ボタンをクリック

**Git Bash で:**

```bash
git add .
git commit -m "ログインページを追加"
```

#### ステップ 5: プッシュ

変更を GitHub にプッシュします。

**VSCode で:**
1. 「...」→「プッシュ」をクリック
2. 初回の場合、「このブランチの上流を公開しますか？」と聞かれたら「OK」

**Git Bash で:**

```bash
git push origin feature/add-login-page
```

#### ステップ 6: プルリクエスト作成

**💡 プルリクエスト（PR）とは:**  
「私の変更をメインブランチに取り込んでください」というお願い。お客さんやチームメンバーがレビューします。

**方法 1: GitHub のバナーから（簡単）**

1. プッシュ後、GitHub のリポジトリページを開く
2. 黄色いバナーが表示される
   - 「feature/add-login-page had recent pushes」
3. 「Compare & pull request」ボタンをクリック

**方法 2: 手動で作成**

1. GitHub のリポジトリページを開く
2. 「Pull requests」タブをクリック
3. 「New pull request」ボタンをクリック
4. base: `main`、compare: `feature/add-login-page` を選択
5. 「Create pull request」をクリック

**PR の説明文を記入:**

```
## 変更内容
ログインページを追加しました。

## 変更箇所
- src/pages/Login.jsx を新規作成
- ログインフォームのコンポーネント
- バリデーション機能

## 確認事項
- [ ] ログインフォームが表示される
- [ ] バリデーションが正しく動作する
- [ ] レスポンシブ対応

## スクリーンショット
（必要に応じて画像を添付）
```

**💡 お客さんから PR テンプレートがある場合、それに従ってください！**

6. 「Create pull request」ボタンをクリック

#### ステップ 7: レビュー・マージ待ち

**あなたの作業はここで完了！**

お客さんやチームメンバーがレビューします：
- ✅ 承認（Approved）→ マージされる
- 💬 コメント → 修正依頼が来る可能性あり
- ❌ 変更要求（Request changes）→ 修正が必要

**修正依頼が来たら:**
1. 同じブランチで修正
2. コミット・プッシュ
3. 自動的に PR に反映される

**マージされたら:**
1. ローカルで `main` ブランチに切り替え
2. `git pull` で最新を取得
3. 作業用ブランチを削除しても OK

---

### 7-6. 日常的な作業の流れ（👤 あなた）

**毎日の作業開始時:**

```bash
# 1. mainブランチに切り替え
git checkout main

# 2. 最新のコードを取得
git pull origin main

# 3. 新しい作業用ブランチを作成
git checkout -b feature/新しい機能名

# 4. 開発開始！
```

**作業終了時:**

```bash
# 1. 変更をステージング
git add .

# 2. コミット
git commit -m "作業内容"

# 3. プッシュ
git push origin feature/新しい機能名

# 4. GitHubでPR作成
```

---

## 🚨 お客さんのリポジトリで注意すること

### 1. main ブランチで直接作業しない

**❌ 絶対ダメ:**

```bash
# mainブランチで直接編集してプッシュ
git checkout main
（編集）
git add .
git commit -m "変更"
git push  # これはダメ！
```

**✅ 正しい方法:**

```bash
# 必ず作業用ブランチを作る
git checkout -b feature/my-work
（編集）
git add .
git commit -m "変更"
git push origin feature/my-work
# その後、PRを作成
```

### 2. プッシュ前に必ず Pull

他のメンバーが変更している可能性があるので、プッシュ前に必ず最新を取得：

```bash
git pull origin main
```

### 3. コミットメッセージは丁寧に

**❌ 悪い例:**

```
修正
あああ
test
```

**✅ 良い例:**

```
ログインページのバリデーション処理を追加
ボタンの色を#007bffに変更（デザイン仕様書に準拠）
README.mdにセットアップ手順を追記
```

### 4. お客さんのルールを確認

プロジェクトによって異なるルールがあります：

**確認すべきこと:**
- ブランチ命名規則（feature/、fix/ など）
- コミットメッセージのフォーマット
- PR のテンプレート
- レビュワーの指定方法
- マージのタイミング

**💡 わからないことは必ず質問しましょう！**

---

## <a id="トラブルシューティング"></a>🔧 トラブルシューティング

### <a id="完全リセット手順"></a>完全リセット手順（最終手段）

すべてやり直したい場合の手順です。

#### リセット 1: ローカルの SSH キーを削除

**Git Bash で:**

```bash
rm -rf ~/.ssh/id_ed25519*
rm -f ~/.ssh/config
```

**確認:**

```bash
ls -la ~/.ssh/
```

id_ed25519 ファイルが消えていれば OK

#### リセット 2: GitHub の SSH キーを削除

1. https://github.com/settings/keys を開く
2. 追加したキーの横の「Delete」をクリック
3. 確認画面で削除

#### リセット 3: SSH Agent サービスをリセット

**PowerShell を管理者として開いて:**

```powershell
Stop-Service ssh-agent
Set-Service -Name ssh-agent -StartupType Automatic
Start-Service ssh-agent
```

#### リセット 4: 最初から

ステップ 1 から、もう一度ゆっくり進めてください。

**💡 リセット後のコツ:**
- 各ステップで確認コマンドを実行
- エラーメッセージをよく読む
- 焦らず 1 つずつ

### 診断フロー

**問題が起きたら、上から順番に確認:**

#### 診断 1: SSH キーは存在する？

```bash
ls -la ~/.ssh/id_ed25519*
```

**期待する結果:** 2 つのファイルが表示される

**NG:** `No such file or directory` → ステップ 1 からやり直し

#### 診断 2: SSH Agent サービスは起動している？

**PowerShell で:**

```powershell
Get-Service ssh-agent
```

**期待する結果:** `Status` が `Running`

**NG:** `Stopped` → 以下を実行:

```powershell
Start-Service ssh-agent
```

#### 診断 3: SSH Agent に登録されている？

**Git Bash で:**

```bash
ssh-add -l
```

**期待する結果:** 何か表示される（256 SHA256:...）

**NG:** `The agent has no identities` → 以下を実行:

```bash
ssh-add ~/.ssh/id_ed25519
```

#### 診断 4: GitHub に登録されている？

https://github.com/settings/keys で確認

**期待する結果:** あなたが追加したキーが表示される

**NG:** 何もない、または違うキーがある → ステップ 3 からやり直し

#### 診断 5: ローカルと GitHub のキーは一致？

```bash
cat ~/.ssh/id_ed25519.pub
```

GitHub の登録内容と完全一致するか確認

**NG:** 一致しない → GitHub のキーを削除して再登録（ステップ 3-4）

#### 診断 6: 接続テストは通る？

```bash
ssh -T git@github.com
```

**期待する結果:** `You've successfully authenticated` と出る

**NG:** `Permission denied` → 上記診断 1-5 を再確認

#### 診断 7: VSCode の設定は正しい？

VSCode 設定で `git.terminalAuthentication` のチェックを外す

#### 診断 8: SSH 接続を使っている？

**お客さんのリポジトリで作業している場合:**

```bash
cd リポジトリのフォルダ
git remote -v
```

**✅ 正しい表示（SSH）:**

```
origin  git@github.com:user/repo.git (fetch)
origin  git@github.com:user/repo.git (push)
```

**❌ HTTPS になっている:**

```
origin  https://github.com/user/repo.git (fetch)
origin  https://github.com/user/repo.git (push)
```

HTTPS の場合 → ステップ 7-4 の「🚨 もし HTTPS で clone してしまった場合」を参照して SSH に変更

### それでも解決しない場合

すべて試してもうまくいかない場合は、以下の情報を集めてください:

**PowerShell で:**

```powershell
# 1. Windowsバージョン
winver

# 2. PowerShellバージョン
$PSVersionTable.PSVersion
```

**Git Bash で:**

```bash
# 3. Gitバージョン
git --version

# 4. SSH バージョン
ssh -V

# 5. SSHキーの状態
ls -la ~/.ssh/

# 6. SSH Agentの状態
ssh-add -l

# 7. 詳細な接続ログ
ssh -vvv -T git@github.com
```

この情報があれば、具体的な問題を特定できます！

**最後の出力（ssh -vvv）は長いですが、最後の 20 行くらいに原因が書かれています。**

---

## <a id="よくある質問"></a>📚 よくある質問

### Q1: `.ssh`フォルダはあるのに`id_ed25519`がないのはなぜ？

**A:** これは正常です！`.ssh`フォルダは他の SSH 接続でも使われるので、自動的に作られることがあります。SSH キーはまだ作られていないだけなので、ステップ 1 でキーを作成してください。

確認方法:

```bash
ls -la ~/.ssh
```

### Q2: Git Bash とコマンドプロンプトと PowerShell、どれを使えばいい？

**A:**

**Git Bash（推奨！）**
- ✅ このガイドで使っている
- ✅ Unix スタイルのコマンドが使える
- ✅ SSH 関連のコマンドが使いやすい
- ✅ Linux/Mac と同じコマンドが使える

**PowerShell**
- ✅ Windows 標準
- ✅ SSH Agent サービスの管理に使う
- ❌ SSH 関連のコマンドは Git Bash の方が使いやすい

**コマンドプロンプト（cmd）**
- ❌ 古い
- ❌ SSH 関連の作業には向いていない
- ❌ 推奨しません

**💡 推奨:** Git Bash をメインで使い、SSH Agent サービスの管理時のみ PowerShell を使う

### Q3: 何度やっても Permission denied になる

**A:** [診断フロー](#診断フロー)に従って 1 つずつ確認してください。ほとんどの場合、GitHub に登録したキーとローカルのキーが一致していないことが原因です。

### Q4: Windows Defender や ウイルス対策ソフトが邪魔をする？

**A:** 通常は問題ありませんが、稀にセキュリティソフトが SSH 接続をブロックすることがあります。

**確認方法:**
1. 一時的にウイルス対策ソフトを無効化
2. SSH 接続テストを実行
3. 成功したら、ウイルス対策ソフトで Git や SSH を例外に追加

**追加すべき場所:**
- `C:\Program Files\Git\`
- `C:\Users\YourName\.ssh\`

### Q5: パスフレーズは設定した方がいい？

**A:** より安全にしたい場合は設定をおすすめしますが、初心者の方はまず無しで始めて問題ありません。慣れてから追加できます。

### Q6: VSCode で「認証に失敗しました」と出る

**A:**

1. Git Bash で接続テストが通るか確認:

```bash
ssh -T git@github.com
```

2. VSCode の設定で `git.terminalAuthentication` のチェックを外す

3. VSCode を再起動

### Q7: id_rsa と id_ed25519 の違いは？

**A:**

- `id_rsa`: 古いタイプの鍵（RSA 方式）
- `id_ed25519`: 新しいタイプの鍵（ED25519 方式、推奨）

どちらも使えますが、新しく作るなら ed25519 がおすすめです。

### Q8: Git Bash で日本語が文字化けする

**A:**

**対処法 1: Git Bash の設定を変更**

1. Git Bash のウィンドウ上部を右クリック
2. 「Options...」をクリック
3. 「Text」→「Locale」を `ja_JP`に、「Character set」を `UTF-8` に変更
4. 「Apply」→「Save」

**対処法 2: Git の設定で日本語を有効化**

```bash
git config --global core.quotepath false
```

### Q9: エクスプローラーから Git Bash を開きたい

**A:** Git for Windows をインストールすると、右クリックメニューに自動追加されます。

**使い方:**
1. エクスプローラーで任意のフォルダを開く
2. 空白部分を右クリック
3. 「Git Bash Here」をクリック

**💡 表示されない場合:**
Git for Windows を再インストールし、インストール時に「Windows Explorer integration」にチェックを入れてください。

### Q10: パスに日本語が含まれても大丈夫？

**A:** 技術的には動作しますが、**おすすめしません**。

**問題点:**
- 文字化けの原因になる
- 一部のツールで動作しないことがある
- チーム開発で問題が起きやすい

**推奨:**
- プロジェクトフォルダは英数字のみ
- 例: `C:\Users\YourName\Documents\Projects\`
- ❌ `C:\Users\太郎\ドキュメント\プロジェクト\`

### Q11: 複数の GitHub アカウントを使いたい

**A:** 高度な設定が必要です。まずは 1 つのアカウントで完璧に動かしましょう。慣れてから挑戦してください。

**簡易的な方法:**
個人用とお客さん用で異なる SSH キーを作り、`~/.ssh/config` で切り替える方法があります。

### Q12: Windows 11 でも使える？

**A:** はい！このガイドは Windows 10 と Windows 11 の両方で動作します。手順は全く同じです。

### Q13: WSL（Windows Subsystem for Linux）を使った方がいい？

**A:** このガイドでは WSL を使わず、Windows ネイティブの Git を使用しています。

**Windows ネイティブ Git の利点:**
- ✅ セットアップが簡単
- ✅ VSCode との統合が良い
- ✅ 初心者に優しい

**WSL の利点:**
- ✅ Linux 環境そのもの
- ✅ より本格的な開発環境
- ❌ 設定が複雑

**💡 推奨:** まずは Windows ネイティブで慣れてから、必要に応じて WSL に移行

### Q14: Git のアップデート方法は？

**A:**

**方法 1: Git for Windows を再インストール**
1. 最新版を https://git-scm.com/download/win からダウンロード
2. インストーラーを実行（上書きインストール）

**方法 2: Git Bash でアップデート確認**

```bash
git update-git-for-windows
```

### Q15: SSH Agent が再起動後に消える

**A:** SSH Agent サービスが自動起動に設定されていない可能性があります。

**解決方法:**

PowerShell を管理者として開いて:

```powershell
Set-Service -Name ssh-agent -StartupType Automatic
Start-Service ssh-agent
```

これで、パソコンを再起動しても SSH Agent が自動的に起動します。

---

## 💪 完璧にできたかチェックリスト

以下すべてにチェックが付けば OK:

- [ ] Git for Windows をインストールした
- [ ] `git --version` と `ssh -V` でバージョンが表示される
- [ ] `ls -la ~/.ssh/id_ed25519*` で 2 つのファイルが表示される
- [ ] PowerShell で `Get-Service ssh-agent` が `Running` になっている
- [ ] `ssh-add -l` で SSH キーが表示される
- [ ] GitHub の SSH 設定ページ（https://github.com/settings/keys）にキーが登録されている
- [ ] `ssh -T git@github.com` で「You've successfully authenticated」と出る
- [ ] `git config --global --list` で名前とメールが設定されている
- [ ] VSCode で SSH URL からクローンできた
- [ ] VSCode で変更をプッシュできた

**全部チェックできたら完璧です！🎉**

---

## 🎉 成功したら

**おめでとうございます！**

あなたは今、プロのエンジニアと同じ環境を手に入れました！

### 次のステップ

1. **実際のプロジェクトを作る**
   - 自分のコードを GitHub にプッシュ
   - ポートフォリオを作成

2. **他の人のコードを見る**
   - 興味あるリポジトリをクローン
   - コードを読んで学ぶ

3. **Git の基本を学ぶ**
   - ブランチの作成
   - コミットの履歴を見る
   - マージを理解する

4. **コラボレーションを始める**
   - オープンソースプロジェクトに貢献
   - プルリクエストを送る

**Happy Coding! 💻✨**

---

## 📝 このガイドについて

このガイドは、Mac版のガイドをベースに Windows 環境向けに完全に書き換えたものです。実際の初心者エンジニアの方が遭遇したエラーや疑問をすべて反映して作成されています。

**Windows 特有の対応:**
- Git for Windows のインストール
- SSH Agent サービスの設定
- PowerShell と Git Bash の使い分け
- Windows のパス表記
- Windows Defender との共存

**フィードバック大歓迎！**
- わかりにくい部分があれば教えてください
- 新しいエラーに遭遇したら共有してください
- より良いガイドにするためのアイデアをください

**このガイドの目標:**  
他の資料を一切見なくても、このガイドだけで 100%完了できること

その目標に向けて、常にアップデートしていきます！🚀
