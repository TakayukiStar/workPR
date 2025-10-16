# Windows初心者のためのVSCode×GitHub完全ガイド【完全版】

## 🎯 このガイドについて

このガイド**だけ**で、WindowsでのGit/GitHub/VSCodeの導入がすべて完了します。
他の資料を見る必要は一切ありません。

**対象者:**
- Windowsユーザー（Windows 10/11対応）
- **x64（Intel/AMD）とARM64（最新Surface等）の両方に完全対応**
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
- ✅ Windows 10またはWindows 11搭載のPC
- ✅ インターネット接続
- ✅ メールアドレス（Gmail、Outlook、Yahoo!メールなど）
- ✅ 管理者権限（あなたのPCのパスワードを知っている）
- ✅ 30分〜1時間の時間

### 自分のPCの情報を確認

作業を始める前に、以下を確認しておきましょう：

#### 1. Windowsのバージョンを確認

**手順:**
1. **Windowsキー + I** を押して「設定」を開く
2. 左メニューから **「システム」** をクリック
3. 下にスクロールして **「バージョン情報」** をクリック
4. **「Windowsの仕様」** セクションを確認

**確認項目:**

**エディション:**
- `Windows 11 Home` / `Windows 11 Pro`
- `Windows 10 Home` / `Windows 10 Pro`

**バージョン:**
- Windows 11: `24H2` / `23H2` など
- Windows 10: `22H2` / `21H2` など

**OSビルド:**
- Windows 11: `22000` 以降
- Windows 10: `19041` 以降（バージョン2004以降）

📝 **メモ:** Windows 10の古いバージョン（1903以前）を使っている場合は、Windows Updateを実行することを推奨します。

#### 2. システムの種類（アーキテクチャ）を確認 ⭐超重要⭐

**同じ「バージョン情報」画面で確認します:**

**確認場所:**
- 画面を上にスクロール
- **「デバイスの仕様」** セクションを見る
- **「システムの種類」** という項目を確認

**表示内容の見方:**

**🔷 x64ベース（従来型Intel/AMD）の場合:**
```
システムの種類: 64 ビット オペレーティング システム, x64 ベース プロセッサ
```
または英語版Windowsの場合:
```
System type: 64-bit operating system, x64-based processor
```

**🔶 ARM64ベース（最新Surface、Copilot+ PC等）の場合:**
```
システムの種類: 64 ビット オペレーティング システム, ARM ベース プロセッサ
```
または英語版Windowsの場合:
```
System type: 64-bit operating system, ARM-based processor
```

**🔸 32bit版（古いPC）の場合:**
```
システムの種類: 32 ビット オペレーティング システム, x86 ベース プロセッサ
```

📝 **超重要:** この「システムの種類」の情報は、ソフトウェアのダウンロード時に必ず使います！
📝 **確認箇所:** 「設定」→「システム」→「バージョン情報」→「デバイスの仕様」セクション→「システムの種類」

#### 2-1: より詳細な確認方法（オプション）

**方法1: PowerShellで確認（推奨・最速）**

1. **Windowsキー** を押す
2. **「PowerShell」** と入力
3. **「Windows PowerShell」** をクリック
4. 以下のコマンドを入力して **Enter** を押す：

```powershell
$env:PROCESSOR_ARCHITECTURE
```

**表示される結果:**
```
AMD64     → x64（Intel/AMD）です
ARM64     → ARM64（Surface Pro X、Copilot+ PC等）です
x86       → 32bit（古いPC）です
```

📝 **確認箇所:** スタートメニュー → 「PowerShell」と入力 → コマンド実行

**方法2: systeminfoコマンド**

1. **Windowsキー** を押す
2. **「cmd」** と入力
3. **「コマンドプロンプト」** をクリック
4. 以下のコマンドを入力して **Enter** を押す：

日本語版Windowsの場合:
```cmd
systeminfo | findstr /C:"システムの種類"
```

英語版Windowsの場合:
```cmd
systeminfo | findstr /C:"System Type"
```

**表示例:**
```
システムの種類:           x64-based PC
```
または
```
システムの種類:           ARM64-based PC
```

📝 **確認箇所:** スタートメニュー → 「cmd」と入力 → コマンド実行

#### 3. 搭載プロセッサの確認

**確認場所:**
- 「設定」→「システム」→「バージョン情報」
- **「デバイスの仕様」** セクション
- **「プロセッサ」** という項目を確認

**表示例:**

**x64（Intel/AMD）の場合:**
```
プロセッサ: Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz
```
または
```
プロセッサ: AMD Ryzen 7 5800H with Radeon Graphics
```
または
```
プロセッサ: Intel(R) Core(TM) Ultra 7 155H
```

**ARM64の場合:**
```
プロセッサ: Snapdragon(R) X Elite - X1E80100 - Qualcomm(R) Oryon(TM) CPU
```
または
```
プロセッサ: Microsoft SQ2 @ 3.00 GHz
```
または
```
プロセッサ: Microsoft SQ3
```

💡 **見分け方:** 
- **Snapdragon** または **Microsoft SQ** と表示 → **ARM64です**
- **Intel Core** または **AMD Ryzen** と表示 → **x64です**

📝 **確認箇所:** 「設定」→「システム」→「バージョン情報」→「デバイスの仕様」セクション→「プロセッサ」

#### 4. ストレージ容量を確認

**手順:**
1. **Windowsキー + E** を押して **エクスプローラー** を開く
2. 左サイドバーの **「PC」** または **「このPC」** をクリック
3. **「デバイスとドライブ」** セクションを見る
4. **「ローカルディスク(C:)」** の空き容量を確認

**表示例:**
```
ローカル ディスク (C:)
237 GB の空き領域 / 476 GB
```

**必要な容量:**
- ✅ **最低: 5GB** の空き容量
- ✅ **推奨: 10GB以上** の空き容量

📝 **確認箇所:** エクスプローラー（Windowsキー + E）→ 左サイドバー「PC」→「デバイスとドライブ」セクション

#### 5. ユーザー名を確認

**手順:**
1. **Windowsキー** を押す
2. **「cmd」** と入力
3. **「コマンドプロンプト」** をクリック
4. 以下のコマンドを入力して **Enter** を押す：

```cmd
echo %USERNAME%
```

**表示例:**
```
TaroYamada
```

この表示された名前があなたのWindowsユーザー名です。

📝 **重要:** このユーザー名は後でファイルパスに使います（例: `C:\Users\TaroYamada\`）
📝 **確認箇所:** コマンドプロンプト → `echo %USERNAME%` コマンド実行

#### ✅ 事前確認まとめ

以下を確認してメモしておきましょう：

```
□ Windowsバージョン: Windows ___（10 or 11）
□ アーキテクチャ: ___（x64 or ARM64）
□ プロセッサ: ___
□ 空き容量: ___ GB
□ ユーザー名: ___
```

---

## 🔧 Gitのインストール

### ステップ1: Git for Windowsをダウンロード

**⚠️ 超重要:** アーキテクチャ（x64 / ARM64）によってダウンロードするファイルが異なります！

#### 1-1: ダウンロードページにアクセス

ブラウザで以下のURLにアクセス：
https://git-scm.com/download/win

#### 1-2: 正しいバージョンを選択

**🔷 x64（Intel/AMD）の場合:**

ページ上部の **「Click here to download」** をクリックすると、自動的に以下がダウンロードされます：
- `Git-2.43.0-64-bit.exe`（バージョン番号は変わります）

**🔶 ARM64（Surface Pro X等）の場合:**

⚠️ 自動ダウンロードは**x64版**なので、手動で選択が必要です！

1. ページを少し下にスクロール
2. **「Other Git for Windows downloads」** セクションを探す
3. **「ARM64」** のリンクをクリック
4. 最新の **`Git-2.xx.x-arm64.exe`** をクリックしてダウンロード

**例:**
- ❌ `Git-2.43.0-64-bit.exe` （これはx64版！）
- ✅ `Git-2.43.0-arm64.exe` （ARM64ネイティブ版）

💡 **ARM64の見分け方:** ファイル名に **`arm64`** が含まれていることを確認！

#### 1-3: ダウンロード確認

**エクスプローラー** の「ダウンロード」フォルダで確認：

**x64の場合:**
```
Git-2.43.0-64-bit.exe
```

**ARM64の場合:**
```
Git-2.43.0-arm64.exe
```

### ステップ2: インストーラーを起動

1. **エクスプローラー** を開く（Windowsキー + E）
2. 左側の **「ダウンロード」** をクリック
3. ダウンロードした **`.exe`ファイル** をダブルクリック

**ユーザーアカウント制御の画面が表示される場合:**
「このアプリがデバイスに変更を加えることを許可しますか？」
→ **「はい」** をクリック

### ステップ3: インストール設定

インストーラーが起動します。以下の画面が順番に表示されるので、推奨設定を選択していきます。

**💡 ポイント:** x64とARM64で設定内容は同じです！

#### 3-1: ライセンス同意

**「Information」** 画面
- **「Next」** をクリック

#### 3-2: インストール先

**「Select Destination Location」** 画面

**推奨設定（両アーキテクチャ共通）:**
- デフォルトのまま（`C:\Program Files\Git`）
- **「Next」** をクリック

💡 **変更不要:** 特別な理由がない限りデフォルトでOKです。

#### 3-3: コンポーネントの選択

**「Select Components」** 画面

以下の項目に **チェックを入れる:**
- ✅ **「Windows Explorer integration」** （右クリックメニューに追加）
  - ✅ **「Git Bash Here」**
  - ✅ **「Git GUI Here」**
- ✅ **「Git LFS (Large File Support)」**
- ✅ **「Associate .git* configuration files with the default text editor」**
- ✅ **「Associate .sh files to be run with Bash」**
- ✅ **「Add a Git Bash Profile to Windows Terminal」**（Windows 11の場合）

**「Next」** をクリック

#### 3-4: スタートメニューフォルダ

**「Select Start Menu Folder」** 画面
- デフォルトのまま（`Git`）
- **「Next」** をクリック

#### 3-5: デフォルトエディタの選択

**「Choosing the default editor used by Git」** 画面

**推奨設定:**
- プルダウンメニューから **「Use Visual Studio Code as Git's default editor」** を選択

💡 **理由:** 後でインストールするVSCodeと連携するため

**「Next」** をクリック

#### 3-6: 新しいリポジトリの初期ブランチ名

**「Adjusting the name of the initial branch in new repositories」** 画面

**推奨設定:**
- ☑️ **「Override the default branch name for new repositories」** を選択
- テキストボックスに **`main`** と入力

💡 **理由:** GitHubの標準ブランチ名が `main` のため

**「Next」** をクリック

#### 3-7: PATH環境変数の設定

**「Adjusting your PATH environment」** 画面

**推奨設定:**
- ☑️ **「Git from the command line and also from 3rd-party software」** を選択（中央の選択肢）

💡 **理由:** コマンドプロンプト、PowerShell、VSCodeすべてでGitを使えるようにするため

**「Next」** をクリック

#### 3-8: SSH実行ファイル

**「Choosing the SSH executable」** 画面

**推奨設定:**
- ☑️ **「Use bundled OpenSSH」** を選択（デフォルト）

**「Next」** をクリック

#### 3-9: HTTPS接続のバックエンド

**「Choosing HTTPS transport backend」** 画面

**推奨設定:**
- ☑️ **「Use the OpenSSL library」** を選択（デフォルト）

**「Next」** をクリック

#### 3-10: 改行コードの変換

**「Configuring the line ending conversions」** 画面

**推奨設定:**
- ☑️ **「Checkout Windows-style, commit Unix-style line endings」** を選択（デフォルト）

💡 **重要:** Windows（CRLF）とLinux/Mac（LF）の改行コードを自動変換します

**「Next」** をクリック

#### 3-11: ターミナルエミュレーター

**「Configuring the terminal emulator to use with Git Bash」** 画面

**推奨設定:**
- ☑️ **「Use MinTTY (the default terminal of MSYS2)」** を選択（デフォルト）

**「Next」** をクリック

#### 3-12: git pullの動作

**「Choose the default behavior of 'git pull'」** 画面

**推奨設定:**
- ☑️ **「Default (fast-forward or merge)」** を選択（デフォルト）

**「Next」** をクリック

#### 3-13: 認証情報ヘルパー

**「Choose a credential helper」** 画面

**推奨設定:**
- ☑️ **「Git Credential Manager」** を選択（デフォルト）

💡 **メリット:** GitHubのパスワードを安全に保存してくれます

**「Next」** をクリック

#### 3-14: 追加オプション

**「Configuring extra options」** 画面

**推奨設定:**
- ✅ **「Enable file system caching」** （デフォルトでチェック済み）
- ✅ **「Enable symbolic links」** （デフォルトでチェック済み）

**「Next」** をクリック

#### 3-15: 実験的機能（オプション）

**「Configuring experimental options」** 画面

**推奨設定:**
- すべてチェックなし（デフォルト）

💡 **理由:** 安定性を優先

**「Install」** をクリック

#### 3-16: インストール実行

インストールが開始されます。

**所要時間:**
- **x64版:** 2〜5分
- **ARM64版:** 3〜7分（若干長め）

進行状況バーが表示されます。

#### 3-17: インストール完了

**「Completing the Git Setup Wizard」** 画面

- ✅ **「View Release Notes」** のチェックを外す（不要）
- **「Finish」** をクリック

### ステップ4: Gitのインストール確認

#### 4-1: コマンドプロンプトを開く

**開き方（3つの方法、どれでもOK）:**

**方法1: Windowsキーから検索（最も簡単）**
1. **Windowsキー** を押す
2. **「cmd」** と入力
3. **「コマンドプロンプト」** が表示されたら **Enter** を押す

**方法2: ファイル名を指定して実行**
1. **Windowsキー + R** を押す
2. **「cmd」** と入力
3. **「OK」** をクリック

**方法3: スタートメニューから**
1. **スタートボタン** を右クリック
2. **「ターミナル」**（Windows 11）または **「Windows PowerShell」**（Windows 10）を選択

💡 **コマンドプロンプトとPowerShellの違い:**
- どちらでもGitコマンドは使えます
- このガイドでは「コマンドプロンプト」を使って説明しますが、PowerShellでも同じです

#### 4-2: Gitのバージョンを確認

コマンドプロンプトで以下を入力して **Enter** を押します：

```cmd
git --version
```

**💡 入力のコツ:**
- コピー＆ペーストでOK（右クリック→貼り付け、またはCtrl + V）
- 入力後は必ず **Enter** を押す

**✅ 成功の場合:**

**x64版の場合:**
```
git version 2.43.0.windows.1
```

**ARM64版の場合:**
```
git version 2.43.0.windows.1
```

💡 **表示は同じ:** バージョン番号の表示自体は同じですが、内部的にARM64ネイティブで動作しています

このように表示されれば、Gitのインストール成功！

**❌ 失敗の場合:**
```
'git' は、内部コマンドまたは外部コマンド、
操作可能なプログラムまたはバッチ ファイルとして認識されていません。
```
このように表示された場合 → [トラブルシューティング](#gitが正しくインストールされない)を参照

#### 4-3: アーキテクチャの確認（ARM64ユーザー向け）

**ARM64ユーザーは、ネイティブ版がインストールされているか必ず確認しましょう：**

**手順:**
1. **Windowsキー** を押す
2. **「PowerShell」** と入力
3. **「Windows PowerShell」** をクリック
4. 以下のコマンドをコピー＆ペーストして **Enter** を押す：

```powershell
Get-Command git | Select-Object Source
(Get-Item (Get-Command git).Source).VersionInfo.FileDescription
```

**✅ 正しくARM64ネイティブ版の場合:**
```
Source
------
C:\Program Files\Git\cmd\git.exe

Git for Windows (ARM64)
```

**最後の行に `(ARM64)` と表示されていればネイティブ版です！**

**❌ もしx64版（エミュレーション）の場合:**
```
Source
------
C:\Program Files\Git\cmd\git.exe

Git for Windows (x64)
```

⚠️ **x64版がインストールされている場合:** 
動作はしますが、ARM64ネイティブ版の方が高速です。アンインストールして、ARM64版を正しくダウンロードして再インストールすることを推奨します。

📝 **確認箇所:** PowerShell → 上記の2つのコマンドを実行 → 2行目の出力で `(ARM64)` を確認

#### 4-4: コマンドプロンプトを再起動（必要な場合）

インストール前にコマンドプロンプトを開いていた場合、再起動が必要です：

1. コマンドプロンプトを閉じる（右上の×ボタン）
2. もう一度コマンドプロンプトを開く
3. `git --version` を再実行

### ステップ5: Git Bashの確認（オプション）

Git Bashは、LinuxやMacと同じようなコマンドが使えるターミナルです。

**💡 ARM64の注意点:** Git BashもARM64ネイティブで動作しますが、一部のツールはx64エミュレーションで動作する場合があります。

**Git Bashを開く方法:**

**方法1: スタートメニューから**
1. **Windowsキー** を押す
2. **「Git Bash」** と入力
3. **「Git Bash」** をクリック

**方法2: 右クリックメニューから**
1. デスクトップまたはエクスプローラーの空白部分を右クリック
2. **「その他のオプションを表示」**（Windows 11）をクリック
3. **「Git Bash Here」** を選択

**Git Bashで確認:**
```bash
git --version
uname -m
```

**表示される結果:**

**x64の場合:**
```
git version 2.43.0.windows.1
x86_64
```

**ARM64の場合:**
```
git version 2.43.0.windows.1
aarch64
```

💡 **`aarch64` = ARM64** です！

💡 **Git BashとCmd（コマンドプロンプト）の違い:**
- **Git Bash:** Linux/Mac風のコマンド（`ls`, `cat`, `grep`など）が使える
- **Cmd:** Windows標準のコマンド（`dir`, `type`など）

このガイドでは主に**コマンドプロンプト**を使いますが、Git Bashでも動作します。

### ステップ6: Gitの初期設定

**⚠️ このステップは必須です！スキップしないでください。**

Gitを使うために、あなたの名前とメールアドレスを設定します。

**💡 x64とARM64で設定内容は同じです！**

#### 6-1: 名前を設定

コマンドプロンプトで以下を実行：

```cmd
git config --global user.name "あなたの名前"
```

**例:**
```cmd
git config --global user.name "Taro Yamada"
```

💡 **ポイント:**
- ダブルクォーテーション（`"`）を忘れずに
- 日本語でもローマ字でもOK
- GitHubで表示される名前になります

#### 6-2: メールアドレスを設定

```cmd
git config --global user.email "your.email@example.com"
```

**例:**
```cmd
git config --global user.email "taro.yamada@gmail.com"
```

💡 **ポイント:**
- 後で作成するGitHubアカウントと同じメールアドレスを使用
- ダブルクォーテーション（`"`）を忘れずに

#### 6-3: 設定を確認

```cmd
git config --global --list
```

以下のように表示されればOK：
```
user.name=Taro Yamada
user.email=taro.yamada@gmail.com
core.editor=code --wait
init.defaultbranch=main
...（その他の設定）
```

⚠️ **もし間違えた場合:**
同じコマンドを正しい内容で再実行すれば上書きされます。

#### 6-4: 日本語ファイル名の文字化け防止

```cmd
git config --global core.quotepath false
```

**Enter** を押す（何も表示されませんが正常です）

これで日本語のファイル名が正しく表示されるようになります。

#### 6-5: 改行コード設定の確認

```cmd
git config --global core.autocrlf
```

**表示される結果:**
```
true
```

💡 **`true` が表示されればOK:** Windows（CRLF）とLinux/Mac（LF）の改行コードを自動変換します

**もし何も表示されない場合:**
```cmd
git config --global core.autocrlf true
```

### ✅ Gitのインストール完了チェック

以下をすべて実行して、正しい結果が表示されることを確認：

```cmd
git --version
git config user.name
git config user.email
git config core.autocrlf
```

**ARM64ユーザーは追加で確認（PowerShell）:**
```powershell
(Get-Item (Get-Command git).Source).VersionInfo.FileDescription
```

**「Git for Windows (ARM64)」** と表示されればネイティブ版で完璧！

すべて正しく表示されたら、Gitのインストールは完了です！

---

## 👤 GitHubアカウント作成

### GitHubとは？

GitHubは、Gitで管理したコードをインターネット上に保存・共有できるサービスです。
無料で使えて、世界中の開発者が利用しています。

**💡 アーキテクチャの違いは関係ありません:** x64でもARM64でも、GitHubアカウント作成手順は完全に同じです。

### ステップ1: GitHubにアクセス

1. ブラウザ（Edge、Chrome、Firefoxなど）を開く
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

どちらでもOKです。**「Continue」** をクリック

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

**⚠️ 超重要:** アーキテクチャ（x64 / ARM64）によってダウンロードするファイルが異なります！

#### 1-1: ダウンロードページにアクセス

ブラウザで以下のURLにアクセス：
https://code.visualstudio.com

#### 1-2: 正しいバージョンを選択

**🔷 x64（Intel/AMD）の場合:**

青い **「Download for Windows」** ボタンをクリックすると、自動的に以下がダウンロードされます：
- `VSCodeUserSetup-x64-1.85.0.exe`（バージョン番号は変わります）

**🔶 ARM64（Surface Pro X等）の場合:**

⚠️ 自動ダウンロードは**x64版**なので、手動で選択が必要です！

1. 青い **「Download for Windows」** ボタンの **右側の下向き矢印** をクリック
2. ドロップダウンメニューから **「ARM64」** を選択
3. または、ボタンの下にある **「Other downloads」** リンクをクリック
4. **「Windows ARM 64 User Installer」** をクリック

**ダウンロードされるファイル:**
- ❌ `VSCodeUserSetup-x64-1.85.0.exe` （x64版！）
- ✅ `VSCodeUserSetup-arm64-1.85.0.exe` （ARM64ネイティブ版）

💡 **ARM64の見分け方:** ファイル名に **`arm64`** が含まれていることを確認！

💡 **ダウンロード先:** 通常は「ダウンロード」フォルダに保存されます。

### ステップ2: VSCodeをインストール

**💡 x64とARM64でインストール手順は同じです！**

#### 2-1: インストーラーを起動

1. **エクスプローラー** を開く（Windowsキー + E）
2. 左側の **「ダウンロード」** をクリック
3. ダウンロードした **`.exe`ファイル** をダブルクリック

**ユーザーアカウント制御の画面が表示される場合:**
「このアプリがデバイスに変更を加えることを許可しますか？」
→ **「はい」** をクリック

#### 2-2: セットアップウィザード

**ライセンス同意画面:**
1. **「同意する」** を選択
2. **「次へ」** をクリック

**インストール先の選択:**
1. デフォルトのまま（`C:\Users\ユーザー名\AppData\Local\Programs\Microsoft VS Code`）
2. **「次へ」** をクリック

**スタートメニューフォルダ:**
1. デフォルトのまま（`Visual Studio Code`）
2. **「次へ」** をクリック

**追加タスクの選択（重要！）:**

以下の項目に**必ずチェックを入れてください:**

- ✅ **「デスクトップ上にアイコンを作成する」**
- ✅ **「エクスプローラーのファイル コンテキスト メニューに [Code で開く] アクションを追加する」**
- ✅ **「エクスプローラーのディレクトリ コンテキスト メニューに [Code で開く] アクションを追加する」**
- ✅ **「サポートされているファイルの種類のエディターとして、Code を登録する」**
- ✅ **「PATH への追加（再起動後に使用可能）」**

💡 **重要:** 特に「PATH への追加」は必須です！

**「次へ」** をクリック

**インストール準備完了:**
1. 設定内容を確認
2. **「インストール」** をクリック

#### 2-3: インストール実行

インストールが開始されます。

**所要時間:**
- **x64版:** 2〜5分
- **ARM64版:** 3〜7分（若干長め）

進行状況バーが表示されます。

#### 2-4: インストール完了

**「Visual Studio Code セットアップウィザードの完了」** 画面

- ✅ **「Visual Studio Code を実行する」** にチェック
- **「完了」** をクリック

VSCodeが自動的に起動します。

### ステップ3: VSCodeの初期画面とアーキテクチャ確認

VSCodeが起動すると、以下のような画面が表示されます：

- **Welcome画面:** 「Get Started with VS Code」
- **左サイドバー:** アイコンが縦に並んでいる
- **中央:** エディタエリア（ファイルを開く場所）

#### 3-1: インストールされたバージョンの確認

**ARM64ユーザーは、ネイティブ版がインストールされているか必ず確認しましょう：**

**手順:**
1. VSCodeを起動
2. 画面上部のメニューバーから **「Help」**（または **「ヘルプ」**）をクリック
3. ドロップダウンメニューから **「About」**（または **「バージョン情報」**）をクリック
4. バージョン情報ウィンドウが開きます

**確認項目:**
- ウィンドウ内の情報をスクロール
- **「OS:」** で始まる行を探す

**✅ 正しくARM64ネイティブ版の場合:**
```
Version: 1.85.0
Commit: abc123def456...
Date: 2024-01-15T10:30:00.000Z
Electron: 27.1.3
Chromium: 118.0.5993.159
Node.js: 18.17.1
V8: 11.8.172.18-electron.0
OS: Windows_NT arm64 10.0.22631
```

**重要:** `OS:` の行の最後に **`arm64`** が含まれていればOK！

**❌ もしx64版（エミュレーション）の場合:**
```
OS: Windows_NT x64 10.0.22631
```

⚠️ **x64版がインストールされている場合:** 
動作はしますが、ARM64ネイティブ版の方が高速でバッテリー消費も少ないです。アンインストールして再インストールすることを推奨します。

📝 **確認箇所:** VSCodeメニューバー → 「Help」（ヘルプ）→「About」（バージョン情報）→ 「OS:」の行を確認

### ステップ4: 日本語化（オプションだが強く推奨）

VSCodeは初期状態では英語です。日本語化すると使いやすくなります。

**💡 日本語化の手順はx64とARM64で同じです！**

#### 4-1: 拡張機能を開く

- **方法1:** **Ctrl + Shift + X** を押す
- **方法2:** 左サイドバーの **四角いブロックのアイコン**（Extensions）をクリック

#### 4-2: 日本語パックを検索

1. 上部の検索ボックスに **「Japanese」** と入力
2. **「Japanese Language Pack for Visual Studio Code」** を探す
   - 作成者: **Microsoft**
   - アイコン: 日本の国旗🇯🇵

#### 4-3: インストール

1. **「Install」** ボタンをクリック
2. インストールが完了すると、右下に通知が表示されます：
   **「Would you like to change VS Code's display language to Japanese and restart?」**
3. **「Change Language and Restart」**（または **「Restart」**）をクリック

VSCodeが再起動し、日本語表示になります。

💡 **ARM64の注意:** 拡張機能のインストール時間が若干長い場合がありますが、正常です。

#### 4-4: 日本語化の確認

VSCodeが再起動したら、メニューバーを確認：
- **「File」** → **「ファイル」**
- **「Edit」** → **「編集」**
- **「View」** → **「表示」**

日本語になっていればOK！

**⚠️ 再起動しても英語のままの場合:**

1. **Ctrl + Shift + P** でコマンドパレットを開く
2. **「Configure Display Language」** と入力して選択
3. **「日本語 (ja)」** を選択
4. VSCodeを再起動（完全に閉じてから再度起動）

### ステップ5: GitHubとの連携

VSCodeとGitHubを連携させると、VSCode内から直接GitHubにコードをアップロードできます。

**💡 連携手順はx64とARM64で同じです！**

#### 5-1: サインイン画面を開く

- **方法1:** 左サイドバー一番下の **人型アイコン**（アカウント）をクリック
- **方法2:** **Ctrl + Shift + P** でコマンドパレットを開き、**「サインイン」** と入力

#### 5-2: GitHubを選択

表示される選択肢から：
- **「GitHub でサインインして設定を同期する」** を選択

**⚠️ 複数の選択肢がある場合:**
- **「GitHub」** を選択（**「GitHub Enterprise」** ではない）

#### 5-3: ブラウザでの認証

1. **自動的にブラウザが開きます**
   - 開かない場合は、VSCodeに表示されるリンクをクリック

2. GitHubのページが開き、以下が表示されます：
   **「Authorize Visual-Studio-Code」**
   
3. **「Authorize Visual-Studio-Code」** ボタンをクリック

4. **GitHubにログインしていない場合:** ユーザー名とパスワードを入力してログイン

5. **認証完了画面:**
   **「Success! You may now close this tab and return to VS Code.」**
   
6. タブを閉じてVSCodeに戻る

#### 5-4: VSCodeに戻る確認

**「Visual Studio Codeを開きますか？」**（ブラウザの確認ダイアログ）

1. **「Visual Studio Code を開く」** をクリック

#### 5-5: 連携完了の確認

VSCodeに戻ると：
- 右下に通知: **「GitHub アカウントでサインインしました」**
- 左下の人型アイコンに **GitHubのユーザー名** が表示される

**✅ 連携成功の確認:**
- 左下に自分のGitHubユーザー名が表示されている
- アイコンをクリックすると「サインアウト」が表示される

### ステップ6: VSCodeの基本設定（推奨）

**💡 設定内容はx64とARM64で同じです！**

#### 6-1: 自動保存を有効化

1. メニューバーの **「ファイル」** をクリック
2. **「自動保存」** にチェックを入れる

💡 **メリット:** ファイルを編集したら自動的に保存されます。保存忘れを防げます。

#### 6-2: フォーマット設定

1. **Ctrl + ,**（コンマ）で設定を開く
2. 検索ボックスに **「format on save」** と入力
3. **「Editor: Format On Save」** にチェックを入れる

💡 **メリット:** ファイルを保存するときに自動的にコードが整形されます。

#### 6-3: ターミナルの設定

VSCode内でターミナルを使えるようにします。

1. メニューバーの **「表示」** → **「ターミナル」**
2. または **Ctrl + @**（バッククォート）

画面下部にターミナルが表示されます。

**デフォルトシェルの確認:**
- タブに **「powershell」** または **「cmd」** と表示されます

**デフォルトシェルを変更する場合:**

1. ターミナルタブの横にある **「+」の横の下向き矢印** をクリック
2. **「既定のプロファイルの選択」** を選択
3. お好みのシェルを選択:
   - **PowerShell** （Windows 11推奨）
   - **コマンドプロンプト** （従来型）
   - **Git Bash** （Linux風コマンド）

**⚠️ ターミナルが開かない場合:**

1. **Ctrl + Shift + P** でコマンドパレットを開く
2. **「ターミナル: 新しいターミナルを作成」** と入力して選択

### ステップ7: codeコマンドの確認

**Windowsの場合、インストール時にPATHに追加されているので、すぐに使えます。**

**確認方法:**

コマンドプロンプトを開いて：
```cmd
code --version
```

バージョンが表示されればOK！

**ARM64の場合も同じように動作:**
```cmd
code --version
```
```
1.85.0
...
arm64
```

最後の行に `arm64` と表示されればネイティブ版！

**使い方:**
```cmd
REM 現在のフォルダをVSCodeで開く
code .

REM 特定のフォルダを開く
code C:\Users\YourName\Documents\GitHub\my-project

REM 特定のファイルを開く
code README.md
```

**⚠️ `code` コマンドが使えない場合:**

1. VSCodeを再インストール
2. インストール時に **「PATH への追加」** に必ずチェックを入れる

### ✅ VSCodeのインストール完了チェック

以下をすべて確認:
- [ ] VSCodeが起動する
- [ ] 日本語表示になっている
- [ ] GitHubアカウントと連携されている（左下にユーザー名表示）
- [ ] ターミナルが開ける
- [ ] `code` コマンドが使える

**ARM64ユーザーは追加で確認:**
- [ ] Help → About で `arm64` と表示される
- [ ] `code --version` の出力に `arm64` が含まれる

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

**💡 SSHキーの生成と使用方法はx64とARM64で同じです！**

### ステップ1: SSHキーが既にあるか確認

コマンドプロンプトまたはPowerShellを開いて、以下を実行：

```cmd
dir %USERPROFILE%\.ssh
```

**PowerShellの場合:**
```powershell
ls ~\.ssh
```

**結果のパターン:**

#### パターンA: SSHキーが既に存在
```
2024/01/15  12:00    <DIR>          .
2024/01/15  12:00    <DIR>          ..
2024/01/15  12:00             2,655 id_ed25519
2024/01/15  12:00               574 id_ed25519.pub
```

`id_ed25519` と `id_ed25519.pub`（または `id_rsa` と `id_rsa.pub`）が表示された
→ **既にSSHキーがあります！[ステップ3](#ステップ3-sshキーをクリップボードにコピー)へ**

#### パターンB: .sshフォルダが存在しない
```
ファイルが見つかりません。
```

→ **次のステップへ**

### ステップ2: 新しいSSHキーを生成

**💡 コマンドはx64とARM64で同じです！**

#### 2-1: .sshフォルダを作成（存在しない場合）

```cmd
mkdir %USERPROFILE%\.ssh
```

**PowerShellの場合:**
```powershell
mkdir ~\.ssh
```

#### 2-2: キー生成コマンドを実行

コマンドプロンプトまたはPowerShellで以下を実行（**メールアドレスを自分のものに置き換えてください**）：

```cmd
ssh-keygen -t ed25519 -C "your.email@example.com"
```

**例:**
```cmd
ssh-keygen -t ed25519 -C "taro.yamada@gmail.com"
```

💡 **ポイント:** GitHubアカウントのメールアドレスを使ってください。

💡 **ARM64の注意:** キー生成はネイティブで高速に動作します。

#### 2-3: 保存場所の確認

```
Enter file in which to save the key (C:\Users\YourName/.ssh/id_ed25519):
```

このように聞かれたら、**何も入力せずEnterを押してください**（デフォルトでOK）

#### 2-4: パスフレーズの設定

```
Enter passphrase (empty for no passphrase):
```

**選択肢:**

**推奨: パスフレーズなし**
- そのまま **Enter を押す**
- もう一度 **Enter を押す**（確認）

**セキュリティ重視: パスフレーズあり**
- パスフレーズを入力（画面には表示されません）
- **Enter** を押す
- 同じパスフレーズを再入力
- **Enter** を押す

💡 **パスフレーズなしを推奨する理由:** 
- 毎回の操作が楽
- Windowsの認証情報マネージャーで保護される
- 個人のPCで使う分には安全

#### 2-5: 生成完了の確認

以下のようなメッセージが表示されれば成功：

```
Your identification has been saved in C:\Users\YourName/.ssh/id_ed25519
Your public key has been saved in C:\Users\YourName/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx your.email@example.com
The key's randomart image is:
+--[ED25519 256]--+
|                 |
...
+----[SHA256]-----+
```

#### 2-6: トラブルシューティング（古いWindowsの場合）

**⚠️ `unknown key type ed25519` というエラーが出た場合:**

古いバージョンのWindowsまたはOpenSSHを使っている可能性があります。
代わりにRSAキーを生成してください：

```cmd
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```

**例:**
```cmd
ssh-keygen -t rsa -b 4096 -C "taro.yamada@gmail.com"
```

その後の手順は同じです（`id_rsa` と `id_rsa.pub` が生成されます）。

### ステップ3: SSHキーをクリップボードにコピー

公開鍵（`.pub`ファイル）をクリップボードにコピーします。

**💡 コマンドはx64とARM64で同じです！**

#### 3-1: コピーコマンドを実行

**Ed25519キーの場合（ほとんどの場合）:**
```cmd
type %USERPROFILE%\.ssh\id_ed25519.pub | clip
```

**PowerShellの場合:**
```powershell
Get-Content ~\.ssh\id_ed25519.pub | Set-Clipboard
```

**RSAキーの場合（古いWindows）:**
```cmd
type %USERPROFILE%\.ssh\id_rsa.pub | clip
```

**PowerShellの場合:**
```powershell
Get-Content ~\.ssh\id_rsa.pub | Set-Clipboard
```

**Enter** を押す（**画面には何も表示されませんが正常です**）

#### 3-2: コピーできたか確認（オプション）

本当にコピーされたか確認したい場合：

1. **メモ帳** を開く（Windowsキー → 「メモ帳」と入力）
2. **Ctrl + V** でペースト
3. 以下のような長い文字列が表示されればOK：

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx your.email@example.com
```

4. 確認したら、このテキストは削除してOK（保存不要）

💡 **ポイント:** 
- `ssh-ed25519` または `ssh-rsa` で始まる
- 最後にメールアドレスが含まれている

### ステップ4: GitHubにSSHキーを登録

**💡 GitHubへの登録手順はx64とARM64で同じです！**

#### 4-1: GitHubのSSH設定ページを開く

1. ブラウザで https://github.com/settings/keys にアクセス
2. **ログインしていない場合:** ユーザー名とパスワードを入力してログイン

#### 4-2: 新しいSSHキーを追加

1. 右上の緑色の **「New SSH key」** ボタンをクリック

#### 4-3: キー情報を入力

**Title（タイトル）:**
- キーの識別用の名前を入力
- 例: 
  - **x64の場合:** `My Windows Desktop`, `Work Laptop x64`
  - **ARM64の場合:** `Surface Pro X`, `Copilot+ PC ARM64`, `My ARM Laptop`

💡 **ARM64ユーザーへの推奨:** タイトルに「ARM64」を含めると、後で見分けやすいです。

💡 **複数のPCを使う場合:** どのPCのキーか分かる名前にしましょう。

**Key type（キーの種類）:**
- **「Authentication Key」** を選択（デフォルト）

**Key（キー）:**
1. 入力欄をクリック
2. **Ctrl + V** でペースト
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
- タイトル（例: `Surface Pro X ARM64`）
- キーの一部が表示される
- 緑色のチェックマーク ✅

### ステップ5: SSH接続をテスト

GitHubとSSHで接続できるか確認します。

**💡 テストコマンドはx64とARM64で同じです！**

#### 5-1: 接続テストコマンドを実行

コマンドプロンプトまたはPowerShellで以下を実行：

```cmd
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

**👉 `yes` と入力してEnterを押す**

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
1. Wi-Fiまたは有線LANに接続されているか確認
2. ブラウザでGitHubが開けるか確認
3. ファイアウォール設定を確認

### ステップ6: SSH設定ファイルを作成（推奨）

接続をスムーズにするための設定ファイルを作成します。

**💡 設定ファイルの内容はx64とARM64で同じです！**

#### 6-1: .ssh\configファイルを作成

**メモ帳で作成する方法:**

1. **メモ帳** を開く
2. 以下の内容を入力：

**Ed25519キーの場合:**
```
Host github.com
  User git
  HostName github.com
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_ed25519
```

**RSAキーの場合:**
```
Host github.com
  User git
  HostName github.com
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_rsa
```

3. **「ファイル」** → **「名前を付けて保存」**
4. 保存場所: `C:\Users\あなたのユーザー名\.ssh\`
5. ファイル名: `config`（**拡張子なし**）
6. ファイルの種類: **「すべてのファイル」** を選択
7. **「保存」** をクリック

**コマンドで作成する方法（PowerShell）:**

**Ed25519キーの場合:**
```powershell
@"
Host github.com
  User git
  HostName github.com
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_ed25519
"@ | Out-File -FilePath ~\.ssh\config -Encoding utf8
```

**RSAキーの場合:**
```powershell
@"
Host github.com
  User git
  HostName github.com
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_rsa
"@ | Out-File -FilePath ~\.ssh\config -Encoding utf8
```

#### 6-2: 設定の意味

- **Host:** 接続先のホスト名
- **User:** ユーザー名（GitHubはgit固定）
- **HostName:** 実際の接続先
- **PreferredAuthentications:** 認証方法
- **IdentityFile:** 使用するSSHキーのパス

💡 **メリット:** この設定により、よりスムーズにGitHubと接続できます。

### ステップ7: ssh-agentの設定（Windows 10/11）

WindowsのSSHエージェントサービスを有効化します。

**💡 ssh-agentの設定はx64とARM64で同じです！**

#### 7-1: サービスの状態を確認

**手順:**
1. **スタートボタン** を右クリック
2. **「Windows PowerShell (管理者)」** を選択
   - Windows 11の場合: **「ターミナル (管理者)」** を選択
3. ユーザーアカウント制御で **「はい」** をクリック
4. PowerShellが管理者権限で起動します
5. 以下のコマンドを入力して **Enter** を押す：

```powershell
Get-Service ssh-agent
```

**表示される結果:**
```
Status   Name           DisplayName
------   ----           -----------
Stopped  ssh-agent      OpenSSH Authentication Agent
```

または
```
Status   Name           DisplayName
------   ----           -----------
Running  ssh-agent      OpenSSH Authentication Agent
```

**Status（状態）の確認:**
- `Stopped` → 次のステップへ進む
- `Running` → すでに起動しているので、[ステップ7-4](#7-4-sshキーをエージェントに追加)へスキップ

📝 **確認箇所:** 管理者権限のPowerShell → `Get-Service ssh-agent` コマンド実行 → 「Status」列を確認

#### 7-2: サービスを開始

**手順:**
管理者権限のPowerShellで以下を実行：

```powershell
Start-Service ssh-agent
```

**Enter** を押す（エラーが出なければ成功）

#### 7-3: 自動起動を設定

**手順:**
管理者権限のPowerShellで以下を実行：

```powershell
Set-Service ssh-agent -StartupType Automatic
```

**Enter** を押す（エラーが出なければ成功）

💡 **効果:** PC起動時に自動的にssh-agentが起動するようになります

**確認:**
もう一度以下を実行して、Statusが `Running` になっていることを確認：
```powershell
Get-Service ssh-agent
```

📝 **確認箇所:** 管理者権限のPowerShell → `Get-Service ssh-agent` コマンド実行 → 「Status」が「Running」

#### 7-4: SSHキーをエージェントに追加

**管理者権限のPowerShell** で実行：

**Ed25519キーの場合:**
```powershell
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

**RSAキーの場合:**
```powershell
ssh-add $env:USERPROFILE\.ssh\id_rsa
```

**成功メッセージ:**
```
Identity added: C:\Users\YourName/.ssh/id_ed25519 (your.email@example.com)
```

### ✅ SSH設定完了チェック

以下をすべて確認:
- [ ] SSHキーが生成されている（`dir %USERPROFILE%\.ssh` で確認）
- [ ] GitHubにSSHキーが登録されている
- [ ] `ssh -T git@github.com` で成功メッセージが表示される
- [ ] SSH設定ファイル（config）が作成されている
- [ ] ssh-agentサービスが起動している

**ARM64ユーザーは追加で確認:**
- [ ] GitHubのキータイトルにARM64と記載した（推奨）

---

## 📥 リポジトリのクローン

### リポジトリとは？

リポジトリ（Repository）は、プロジェクトのファイルとその変更履歴を保存する場所です。
「クローン」とは、GitHubにあるリポジトリをあなたのPCにコピーすることです。

**💡 リポジトリのクローン操作はx64とARM64で同じです！**

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

**💡 VSCodeでのクローン操作はx64とARM64で同じです！**

#### 1-1: コマンドパレットを開く

- **Ctrl + Shift + P** を押す
- または、メニューバーの **「表示」** → **「コマンドパレット」**

#### 1-2: Gitクローンを選択

1. **「Git: Clone」** と入力（途中まで入力すると候補が表示されます）
2. **「Git: Clone」**（または **「Git: クローン」**）を選択して **Enter**

#### 1-3: クローン元を選択

**「GitHubからクローン」** を選択

💡 これで、あなたのGitHubリポジトリ一覧が表示されます。

#### 1-4: リポジトリを選択

1. クローンしたいリポジトリを選択（例: `my-first-repo`）
2. **Enter** を押す

**⚠️ 他の人のリポジトリをクローンする場合:**
- リポジトリのURL全体を入力（例: `https://github.com/octocat/Hello-World`）

#### 1-5: 保存先フォルダを選択

**「リポジトリの場所を選んでください」**

推奨フォルダ構成:
```
C:\Users\あなたの名前\Documents\
└── GitHub\
    ├── my-first-repo\
    ├── project1\
    └── project2\
```

**初めての場合（GitHubフォルダがない）:**

1. **「Documents」** フォルダを選択
2. 下部の **「新しいフォルダーの作成」** をクリック
3. フォルダ名: **「GitHub」** と入力
4. **「選択」** をクリック
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

💡 **ARM64の注意:** クローン速度は通常x64と同等ですが、大きなリポジトリの場合は若干遅いことがあります。

#### 1-7: クローン完了

**「クローンしたリポジトリを開きますか？」**

1. **「開く」** をクリック

VSCodeでプロジェクトが開かれます！

#### 1-8: 開いたプロジェクトの確認

- **左サイドバー:** ファイル一覧が表示される
- **README.md** ファイルが見える
- 画面上部: プロジェクト名（例: `my-first-repo`）が表示される

✅ **クローン成功！**

### 方法2: コマンドプロンプトからクローン（コマンドを学びたい場合）

コマンドラインでクローンします。プロとしてのスキルが身につきます。

**💡 クローンコマンドはx64とARM64で同じです！**

#### 2-1: コマンドプロンプトを開く

- **Windowsキー** を押して **「cmd」** と入力
- または、VSCodeのターミナル（**Ctrl + @**）

#### 2-2: クローン先フォルダに移動

```cmd
cd %USERPROFILE%\Documents
```

**PowerShellの場合:**
```powershell
cd ~\Documents
```

**Enter** を押す

#### 2-3: GitHubフォルダを作成（初回のみ）

```cmd
mkdir GitHub
cd GitHub
```

**Enter** を押す

**⚠️ すでにGitHubフォルダがある場合:**
```cmd
cd GitHub
```

#### 2-4: 現在の場所を確認

```cmd
cd
```

`C:\Users\あなたの名前\Documents\GitHub` と表示されればOK

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
```cmd
git clone git@github.com:ユーザー名/リポジトリ名.git
```

**例:**
```cmd
git clone git@github.com:taro-yamada/my-first-repo.git
```

**HTTPSを使う場合:**
```cmd
git clone https://github.com/ユーザー名/リポジトリ名.git
```

**Enter** を押す

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

```cmd
cd リポジトリ名
```

**例:**
```cmd
cd my-first-repo
```

#### 2-9: ファイルを確認

```cmd
dir
```

以下のようなファイルが表示されます：
```
2024/01/15  12:00    <DIR>          .git
2024/01/15  12:00                45 README.md
```

#### 2-10: VSCodeで開く

```cmd
code .
```

`.` は「現在のフォルダ」を意味します。

VSCodeでプロジェクトが開かれます！

**⚠️ `'code' は、内部コマンドまたは外部コマンド...` と表示される場合:**

[VSCodeのステップ7](#ステップ7-codeコマンドの確認)を参照してください。

### 方法3: エクスプローラーから直接開く（既にクローン済みの場合）

既にクローンしたプロジェクトをVSCodeで開く最も簡単な方法：

1. **エクスプローラー** を開く（Windowsキー + E）
2. クローンしたフォルダに移動（例: `Documents\GitHub\my-first-repo`）
3. フォルダ内の空白部分を **右クリック**
4. **「その他のオプションを表示」**（Windows 11）をクリック
5. **「Codeで開く」** を選択

（VSCodeインストール時に設定した場合のみ利用可能）

### トラブルシューティング: クローン失敗

#### エラー1: `Permission denied (publickey)`

**原因:** SSH接続の問題

**対処法:**
1. [SSHキーの設定](#sshキーの設定推奨)を再確認
2. または、HTTPSを使う：
```cmd
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
- [ ] `C:\Users\あなたの名前\Documents\GitHub\` フォルダが存在する
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

**💡 Git操作はx64とARM64で完全に同じです！**

### 方法1: VSCodeのGUI操作（初心者におすすめ★）

視覚的で分かりやすい方法です。

#### 手順1: ファイルを編集

1. VSCodeで **README.md** を開く（左サイドバーのファイル一覧から）
2. 内容を編集（例: 「# 私のプロジェクト」を追加）
3. **Ctrl + S** で保存（自動保存を設定した場合は不要）

#### 手順2: 変更を確認

1. **左サイドバーのソース管理アイコン** をクリック（枝分かれマーク）
   - または **Ctrl + Shift + G**

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
   - **Ctrl + Enter** を押す
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

### 方法2: コマンドプロンプトでのコマンド操作

プロフェッショナルな方法です。コマンドを理解することで、Gitへの理解が深まります。

**💡 Gitコマンドはx64とARM64で完全に同じです！**

#### 基本の流れ

```cmd
REM 1. 最新版を取得（他の人の変更を取り込む）
git pull origin main

REM 2. ファイルを編集
REM （VSCodeなどで編集作業）

REM 3. 現在の状態を確認
git status

REM 4. すべてのファイルをステージング
git add .

REM 5. コミット
git commit -m "コミットメッセージ"

REM 6. GitHubにプッシュ
git push origin main
```

#### 詳しい説明

**ステップ1: 現在の状態を確認**

```cmd
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
```cmd
git add .
```

`.` は「カレントディレクトリ以下すべて」という意味です。

**特定のファイルだけステージング:**
```cmd
git add ファイル名
```

**例:**
```cmd
git add README.md
git add script.py
git add Papers\analysis.csv
```

**複数ファイルを指定:**
```cmd
git add file1.py file2.py folder\file3.txt
```

**ステージングを確認:**
```cmd
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

```cmd
git commit -m "コミットメッセージ"
```

**例:**
```cmd
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
```cmd
git commit
```
と実行すると、エディタ（VSCode）が開きます。メッセージを入力して保存すればOK。

**ステップ4: ブランチ名を確認**

```cmd
git branch
```

**出力例:**
```
* main
```

`*` が付いているのが現在のブランチです。

**⚠️ `master` と表示された場合:**
古いリポジトリでは `master` が使われています。その場合、プッシュコマンドは:
```cmd
git push origin master
```

**ステップ5: GitHubにプッシュ**

```cmd
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

💡 **ARM64の注意:** プッシュ速度はネットワーク速度に依存するため、x64と同等です。

**ステップ6: GitHubで確認**

ブラウザでGitHubのリポジトリページを開き、変更が反映されているか確認しましょう。

### プル（git pull）：最新版を取得

他の人（または別のPCのあなた）が変更した内容を取得します。

```cmd
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

**💡 すべてのコマンドはx64とARM64で同じです！**

```cmd
REM 状態確認
git status                    REM 現在の状態
git log                       REM コミット履歴
git log --oneline             REM コミット履歴（簡潔版）
git log --oneline --graph     REM コミット履歴（グラフ表示）

REM ステージング
git add .                     REM すべて追加
git add ファイル名            REM 特定ファイル
git add *.py                  REM Pythonファイルのみ
git reset ファイル名          REM ステージング取り消し

REM コミット
git commit -m "メッセージ"    REM コミット
git commit -am "メッセージ"   REM add + commit（変更ファイルのみ）
git commit --amend            REM 直前のコミットを修正

REM プッシュ・プル
git push origin main          REM プッシュ
git pull origin main          REM プル
git fetch                     REM リモートの情報だけ取得

REM 差分確認
git diff                      REM 変更内容を表示
git diff ファイル名           REM 特定ファイルの変更
git diff --staged             REM ステージング済みの変更

REM 取り消し操作
git restore ファイル名        REM ファイルの変更を取り消し
git restore --staged ファイル名  REM ステージング取り消し
git reset --soft HEAD^        REM 直前のコミット取り消し（変更は保持）
git reset --hard HEAD^        REM 直前のコミット取り消し（変更も削除）
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

**💡 すべての実践シナリオはx64とARM64で同じです！**

### シナリオ1: 新しいPythonスクリプトを追加

#### 手順:

1. **VSCodeで新しいファイルを作成**
   - **Ctrl + N**（新規ファイル）
   - **Ctrl + S**（保存）
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

3. **保存** (**Ctrl + S**)

4. **ソース管理パネル** を開く（**Ctrl + Shift + G**）

5. **ファイルをステージング** （`analysis.py` の横の `+` ボタン）

6. **コミットメッセージを入力:** 「データ分析スクリプトを追加」

7. **コミット** (**Ctrl + Enter**)

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
- `Thumbs.db`（Windowsのサムネイルキャッシュ）
- `desktop.ini`（Windowsのフォルダ設定）
- `__pycache__/`（Pythonのキャッシュ）
- `.env`（環境変数・秘密情報）
- `*.log`（ログファイル）
- `node_modules/`（Node.jsの依存関係）

#### 作成手順:

1. **リポジトリのルートフォルダで `.gitignore` ファイルを作成**
   - ファイル名の最初は必ず `.`（ドット）

2. **以下の内容を記述:**
```
# Windows
Thumbs.db
ehthumbs.db
Desktop.ini
$RECYCLE.BIN/
*.lnk
*.stackdump

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
```cmd
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

Windowsの圧縮機能またはコマンドで圧縮：

**エクスプローラーで圧縮:**
1. ファイルを右クリック
2. **「送る」** → **「圧縮(zip形式)フォルダー」**

**PowerShellで圧縮:**
```powershell
Compress-Archive -Path large_data.csv -DestinationPath large_data.zip
```

#### 方法2: Git LFS（Large File Storage）を使う

大きなファイル専用のGit拡張機能です。

**Git LFSのインストール:**

Git for Windowsに付属しているので、すでにインストールされています。

**💡 ARM64でもGit LFSは動作します！**

**使い方:**
```cmd
REM リポジトリでLFSを初期化
git lfs install

REM 特定の種類のファイルをLFSで管理
git lfs track "*.csv"
git lfs track "*.xlsx"

REM .gitattributesファイルをコミット
git add .gitattributes
git commit -m "LFSを設定"

REM 大きなファイルを追加
git add large_file.csv
git commit -m "大きなCSVファイルを追加"
git push origin main
```

### シナリオ6: 間違えてコミットしたファイルを削除

#### 直前のコミットを取り消す:

```cmd
REM コミット取り消し（変更は保持）
git reset --soft HEAD^

REM ファイルを修正または削除

REM 再度コミット
git add .
git commit -m "修正版"
git push origin main
```

#### 既にプッシュしてしまった場合:

```cmd
REM 危険！GitHubの履歴を書き換えます
git reset --hard HEAD^
git push -f origin main
```

**⚠️ 注意:** 他の人と共同作業している場合は使わないでください！

**安全な方法（推奨）:**
```cmd
REM 新しいコミットで削除
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

#### 症状: `'git' は、内部コマンドまたは外部コマンド...`

**🔶 ARM64特有の問題: x64版がインストールされている可能性**

**確認方法（PowerShell）:**
```powershell
(Get-Item (Get-Command git).Source).VersionInfo.FileDescription
```

**「Git for Windows (x64)」** と表示された場合:
1. Gitをアンインストール
2. ARM64版を正しくダウンロード
3. 再インストール

**対処法1: PATH環境変数を確認**

**手順:**
1. **Windowsキー** を押す
2. **「環境変数」** と入力
3. **「環境変数を編集」** または **「システム環境変数の編集」** を選択
4. **「システムのプロパティ」** ウィンドウが開く
5. 下部の **「環境変数」** ボタンをクリック
6. **「環境変数」** ウィンドウが開く
7. 下半分の **「システム環境変数」** セクションを見る
8. リストから **「Path」** を探して選択
9. **「編集」** ボタンをクリック
10. **「環境変数名の編集」** ウィンドウが開く
11. 以下のパスが含まれているか確認:
    - `C:\Program Files\Git\cmd`
    - `C:\Program Files\Git\bin`

**含まれていない場合:**
1. **「新規」** ボタンをクリック
2. `C:\Program Files\Git\cmd` を入力
3. **「OK」** をクリック
4. もう一度 **「新規」** ボタンをクリック
5. `C:\Program Files\Git\bin` を入力
6. **「OK」** をクリック
7. すべてのウィンドウで **「OK」** をクリックして閉じる
8. コマンドプロンプトを **完全に閉じて** から再起動
9. `git --version` を再実行

📝 **確認箇所:** スタートメニュー → 「環境変数」で検索 → 「システム環境変数」セクション → 「Path」を選択 → 「編集」

**対処法2: Gitを再インストール**

1. コントロールパネル → プログラムのアンインストール
2. **「Git」** を選択して **「アンインストール」**
3. [Gitのインストール](#gitのインストール)からやり直す
4. **ARM64ユーザーは必ずARM64版をダウンロード！**
5. インストール時に **「PATH環境変数の設定」** で中央の選択肢を必ず選ぶ

### VSCodeが遅い（ARM64特有）

#### 症状: ARM64 PCでVSCodeの動作が遅い

**原因:** x64版（エミュレーション）がインストールされている可能性

**確認方法:**
VSCodeで **「Help」** → **「About」** を開き、`OS:` の行を確認

**対処法:**
1. VSCodeをアンインストール
2. ARM64版を正しくダウンロード（`VSCodeUserSetup-arm64-*.exe`）
3. 再インストール

**💡 効果:** ARM64ネイティブ版では動作が大幅に高速化され、バッテリー持続時間も向上します

### 拡張機能がインストールできない（ARM64）

#### 症状: VSCodeの一部の拡張機能がインストールできない

**原因:** 一部の拡張機能はARM64未対応

**対処法:**
1. 拡張機能のページで「ARM64」対応を確認
2. 代替の拡張機能を探す
3. 問題が解決しない場合は、拡張機能の開発者に問い合わせ

**💡 主要な拡張機能の多くはARM64対応済み:**
- Japanese Language Pack ✅
- Python ✅
- Prettier ✅
- ESLint ✅

### SSH接続エラー

#### 症状: `Permission denied (publickey)`

**💡 SSH接続のトラブルシューティングはx64とARM64で同じです！**

**対処法1: SSHキーが正しく生成されているか確認**
```cmd
dir %USERPROFILE%\.ssh
```

`id_ed25519` と `id_ed25519.pub` が存在するか確認

**対処法2: GitHubにSSHキーが登録されているか確認**
https://github.com/settings/keys にアクセスして確認

**対処法3: ssh-agentにキーを追加**

PowerShell（管理者権限）で実行：
```powershell
Start-Service ssh-agent
Set-Service ssh-agent -StartupType Automatic
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

**対処法4: SSH設定ファイルを確認**
```cmd
type %USERPROFILE%\.ssh\config
```

正しい内容が記述されているか確認

**対処法5: HTTPSを使う**
```cmd
git remote set-url origin https://github.com/ユーザー名/リポジトリ名.git
```

### コミットエラー

#### 症状: `Please tell me who you are`

**原因:** Gitの初期設定（user.name, user.email）がされていない

**対処法:**
```cmd
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
```cmd
REM 1. 最新版を取得
git pull origin main

REM 2. コンフリクトがあれば解決

REM 3. プッシュ
git push origin main
```

#### 症状: `Repository not found`

**原因1:** リポジトリ名が間違っている

**対処法:**
```cmd
REM リモートURLを確認
git remote -v

REM 間違っている場合は修正
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
```cmd
git add .
git commit -m "コンフリクトを解決"
git push origin main
```

**コマンドプロンプトでの解決方法:**

1. **コンフリクトを確認:**
```cmd
git status
```

2. **ファイルを手動で編集して `<<<<<<<`, `=======`, `>>>>>>>` を削除**

3. **解決後:**
```cmd
git add .
git commit -m "コンフリクトを解決"
git push origin main
```

### 改行コードの問題

#### 症状: `warning: LF will be replaced by CRLF`

**原因:** WindowsとLinux/Macの改行コードの違い

**対処法:**

これは警告であり、エラーではありません。通常は問題ありません。

**設定を確認:**
```cmd
git config core.autocrlf
```

**`true` が表示されればOK**（自動変換される）

**もし `false` の場合:**
```cmd
git config --global core.autocrlf true
```

### ファイル名の文字化け

#### 症状: 日本語ファイル名が `"\343\203\206..."` のように表示される

**対処法:**
```cmd
git config --global core.quotepath false
```

### Thumbs.dbやdesktop.iniが邪魔

#### 症状: Windowsが自動生成するファイルがGitに含まれてしまう

**対処法1: .gitignoreに追加**
```cmd
echo Thumbs.db >> .gitignore
echo desktop.ini >> .gitignore
git add .gitignore
git commit -m ".gitignoreを更新"
git push origin main
```

**対処法2: 既にコミットしてしまった場合**
```cmd
REM Gitから削除（ファイル自体は残る）
git rm --cached Thumbs.db
git rm --cached desktop.ini

REM コミット & プッシュ
git commit -m "Thumbs.dbとdesktop.iniを削除"
git push origin main
```

**対処法3: グローバルに設定**
```cmd
echo Thumbs.db >> %USERPROFILE%\.gitignore_global
echo desktop.ini >> %USERPROFILE%\.gitignore_global
git config --global core.excludesfile %USERPROFILE%\.gitignore_global
```

### VSCodeでGitが動かない

#### 症状: 「Git が見つかりません」

**対処法1: VSCodeを再起動**
1. VSCodeを完全に閉じる（**Alt + F4**）
2. VSCodeを再起動

**対処法2: Gitのパスを設定**
1. **Ctrl + ,** で設定を開く
2. 「git.path」を検索
3. 以下を入力:
   - `C:\Program Files\Git\cmd\git.exe`

**対処法3: Gitのパスを確認**
```cmd
where git
```

表示されたパスをVSCodeの設定に入力

### 認証エラー

#### 症状: HTTPSでクローン・プッシュするたびにパスワードを要求される

**対処法1: SSHに切り替え（推奨）**
```cmd
git remote set-url origin git@github.com:ユーザー名/リポジトリ名.git
```

**対処法2: Git Credential Managerを使う**

Git for Windowsインストール時に自動的に設定されています。

**確認:**
```cmd
git config --global credential.helper
```

**`manager` または `manager-core` と表示されればOK**

### ファイルサイズが大きすぎる

#### 症状: `File is XXX MB; this exceeds GitHub's file size limit of 100 MB`

**対処法1: ファイルを.gitignoreに追加**
```cmd
echo large_file.csv >> .gitignore
git rm --cached large_file.csv
git commit -m "大きなファイルを除外"
git push origin main
```

**対処法2: Git LFSを使う**
```cmd
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
```cmd
REM 現在のブランチを確認
git branch

REM masterの場合
git push origin master

REM mainに変更したい場合
git branch -m master main
git push -u origin main
```

### 間違えてコミットした

#### 直前のコミットを取り消したい

**対処法1: コミット取り消し（変更は保持）**
```cmd
git reset --soft HEAD^
```

**対処法2: コミット取り消し（変更も削除）**
```cmd
git reset --hard HEAD^
```

⚠️ **注意:** `--hard` はファイルの変更も消えるので慎重に！

#### 間違えたファイルをコミットから除外したい

```cmd
git reset --soft HEAD^
git restore --staged 除外したいファイル
git commit -m "修正版"
git push origin main
```

### Windowsのパス区切り文字の問題

#### 症状: コマンドでパスがうまく認識されない

**原因:** WindowsとLinux/Macのパス区切り文字の違い
- Windows: `\`（バックスラッシュ）
- Linux/Mac: `/`（スラッシュ）

**対処法:**

Gitコマンドでは**どちらでも使えます**が、**スラッシュ（`/`）を推奨**

```cmd
REM どちらでもOK
git add folder\file.txt
git add folder/file.txt

REM スラッシュを推奨（クロスプラットフォーム対応）
git add folder/file.txt
```

### Windows Defenderの警告（ARM64で稀に発生）

#### 症状: ARM64版のGitやVSCodeがWindows Defenderに誤検知される

**原因:** ARM64アプリケーションが新しく、署名データベースが不完全

**対処法:**
1. **Windowsセキュリティ** を開く
2. **「ウイルスと脅威の防止」** → **「設定の管理」**
3. **「除外」** → **「除外の追加または削除」**
4. **「フォルダー」** を選択
5. 以下を追加:
   - `C:\Program Files\Git`
   - `C:\Users\ユーザー名\AppData\Local\Programs\Microsoft VS Code`

---

## 🙋 よくある質問（FAQ）

### Q1: コマンドプロンプトとPowerShell、どちらを使えばいいですか？

**A:** どちらでもGitコマンドは使えます。

**コマンドプロンプト（cmd）:**
- 従来型のWindowsコマンドライン
- シンプルで軽量
- このガイドの例はcmd形式

**PowerShell:**
- 新しいWindowsのシェル
- より高機能（オブジェクト指向）
- Windows 10/11のデフォルト
- ARM64でも完全対応

**Git Bash:**
- Linux/Mac風のコマンドが使える
- Git for Windowsに付属
- `ls`, `cat`, `grep`などが使える
- ARM64でも動作（一部x64エミュレーション）

**おすすめ:** 初心者は**コマンドプロンプト**から始めて、慣れたら**PowerShell**や**Git Bash**を試しましょう。

### Q2: x64とARM64、どちらのPCを使っていますか？

**A:** [事前準備と確認](#事前準備と確認)のセクションで確認方法を説明しています。

**簡単な確認方法:**
- **設定** → **システム** → **バージョン情報** → **システムの種類** を確認
- または PowerShellで `$env:PROCESSOR_ARCHITECTURE` を実行

**結果:**
- `AMD64` または `x64 ベース プロセッサ` → **x64（従来型）**
- `ARM64` または `ARM ベース プロセッサ` → **ARM64（最新型）**

### Q3: ARM64版のソフトウェアをインストールしないとどうなりますか？

**A:** x64版もエミュレーションで動作しますが、以下のデメリットがあります：

**x64版（エミュレーション）のデメリット:**
- ❌ 動作が遅い（特にCPU負荷の高い作業）
- ❌ バッテリー消費が多い
- ❌ 発熱しやすい
- ❌ メモリ使用量が多い

**ARM64版（ネイティブ）のメリット:**
- ✅ 高速動作
- ✅ バッテリー持続時間が長い
- ✅ 発熱が少ない
- ✅ 効率的なメモリ使用

**💡 推奨:** ARM64 PCを使っている場合は、必ずARM64ネイティブ版をインストールしましょう！

### Q4: `main` と `master` どちらを使えばいいですか？

**A:** 新しいリポジトリは `main` を使ってください。

- **2020年10月以降:** GitHubのデフォルトは `main`
- **それ以前:** `master` が使われていた

**古いリポジトリを `main` に変更する方法:**
```cmd
git branch -m master main
git push -u origin main
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
```

### Q5: WindowsとMac/Linuxで同じリポジトリを使えますか？

**A:** はい、できます！

**注意点:**

1. **改行コードの設定:**
```cmd
REM Windowsで設定
git config --global core.autocrlf true
```

Mac/Linuxでは:
```bash
# Mac/Linuxで設定
git config --global core.autocrlf input
```

2. **パス区切り文字:**
- Gitコマンドでは `/` を使う（クロスプラットフォーム対応）

3. **ファイル名の大文字小文字:**
- Windowsは大文字小文字を区別しない
- Mac/Linuxは区別する
- 注意して命名しましょう

**💡 ARM64 WindowsとIntel Macの組み合わせも問題なく動作します！**

### Q6: VSCodeとコマンドライン、どちらを使うべきですか？

**A:** 両方使えると便利です！

**初心者:**
- VSCodeのGUI操作から始める
- 視覚的で分かりやすい

**中級者:**
- コマンドラインも使う
- コマンドを理解すると応用が効く

**最終的には:**
- 簡単な操作 → VSCode
- 複雑な操作 → コマンドライン

**💡 ARM64でもx64でも、使い方は同じです！**

### Q7: Gitの設定を変更したいのですが？

**A:** `git config` コマンドを使います。

**設定の確認:**
```cmd
git config --global --list
```

**名前を変更:**
```cmd
git config --global user.name "新しい名前"
```

**メールアドレスを変更:**
```cmd
git config --global user.email "new.email@example.com"
```

**エディタを変更:**
```cmd
git config --global core.editor "code --wait"
```

### Q8: GitHubに秘密情報を間違えてアップロードしてしまいました！

**A:** すぐに以下を実行してください：

1. **パスワードやAPIキーを即座に変更**
2. **リポジトリをプライベートに変更**（Settings → Change visibility）
3. **該当ファイルを削除**
```cmd
git rm 該当ファイル
git commit -m "秘密情報を削除"
git push origin main
```

⚠️ **重要:** コミット履歴には残ってしまうので、本当に重要な情報の場合はGitHubサポートに相談してください。

**今後の対策:**
- `.env` ファイルに秘密情報を保存
- `.gitignore` に `.env` を追加
- 環境変数を使用

### Q9: WindowsでGitのコマンドが文字化けします

**A:** コマンドプロンプトの文字コードを変更します。

**一時的な対処:**
```cmd
chcp 65001
```

**恒久的な対処:**

1. レジストリエディタを開く（**Windowsキー + R** → `regedit`）
2. `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor`
3. 右クリック → 新規 → DWORD値
4. 名前: `Autorun`
5. 値: `chcp 65001`

**または、PowerShellを使う:**
PowerShellは最初からUTF-8対応なので文字化けしません。

### Q10: 複数のGitHubアカウントを使い分けたい

**A:** SSH設定ファイルで使い分けます。

**~/.ssh/config ファイルを編集:**
```
# 個人アカウント
Host github.com-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_personal

# 仕事アカウント
Host github.com-work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_work
```

**使い方:**
```cmd
REM 個人アカウント用
git clone git@github.com-personal:username/repo.git

REM 仕事アカウント用
git clone git@github.com-work:username/repo.git
```

### Q11: Windows ARM64 PCのバッテリー持ちを最大化したい

**A:** すべてのソフトウェアでARM64ネイティブ版を使いましょう。

**確認すべきソフトウェア:**
- ✅ Git for Windows → ARM64版
- ✅ VSCode → ARM64版
- ✅ ブラウザ → Edge ARM64版（Windows 11に標準搭載）
- ✅ Python → ARM64版（必要な場合）

**効果:**
- バッテリー持続時間が30-50%向上
- 発熱が大幅に減少
- ファンの回転音が静かに
- 全体的なパフォーマンス向上

### Q12: 日本語のコミットメッセージが使えません

**A:** エディタとターミナルの文字コード設定を確認します。

**VSCodeの場合:**

1. **Ctrl + ,** で設定を開く
2. 「files.encoding」を検索
3. **「UTF-8」** に設定

**コマンドプロンプトの場合:**
```cmd
chcp 65001
git commit -m "日本語メッセージ"
```

**PowerShellの場合:**
PowerShellはデフォルトでUTF-8対応なので問題ありません。

### Q13: ARM64 PCでx64版のツールは使えますか？

**A:** はい、使えますが推奨しません。

**Windows 11 on ARM64の特徴:**
- ✅ x64アプリケーションがエミュレーションで動作
- ✅ 互換性は高い（ほとんどのアプリが動作）
- ❌ パフォーマンスが低下（約50-70%の速度）
- ❌ バッテリー消費が増加

**推奨:**
- まずARM64ネイティブ版を探す
- なければx64版を使用（互換性モードで動作）
- 重要なツール（Git、VSCode等）は必ずARM64版を使用

### Q14: Surface Pro XやCopilot+ PCを使っています

**A:** おめでとうございます！最新のARM64デバイスですね。

**このガイドの設定:**
- ✅ すべてARM64ネイティブ対応
- ✅ バッテリー効率を最大化
- ✅ 最高のパフォーマンスを実現

**追加の推奨事項:**
- Windows 11を最新版に更新（ARM64最適化が進んでいます）
- Microsoft Store版のアプリを優先（ARM64最適化済み）
- ブラウザは Microsoft Edge ARM64版を使用（最適化済み）

**パフォーマンス確認:**
- タスクマネージャーで「アプリの履歴」を確認
- ARM64アプリは「ARM64」と表示される
- x64アプリは「x64 (エミュレート)」と表示される

---

## 🎓 次のステップ

基本をマスターしたら、以下を学習しましょう：

**💡 すべての学習内容はx64とARM64で同じです！**

### 1. ブランチの使い方

**ブランチとは:** 作業を分けるための仕組み

**メリット:**
- 機能ごとに開発できる
- 本番環境に影響を与えない
- 複数人で並行作業できる

**基本コマンド:**
```cmd
REM ブランチ一覧
git branch

REM 新しいブランチを作成
git branch feature-login

REM ブランチを切り替え
git checkout feature-login

REM 作成と切り替えを同時に
git checkout -b feature-login

REM ブランチを削除
git branch -d feature-login

REM ブランチをマージ
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

**Windows（x64/ARM64共通）向け.gitignoreパターン:**

```
# Windows
Thumbs.db
ehthumbs.db
Desktop.ini
$RECYCLE.BIN/
*.lnk
*.stackdump

# Visual Studio
.vs/
*.suo
*.user
*.userosscache
*.sln.docstates

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

# ログファイル
*.log
```

### 4. GitHub Actions

**GitHub Actionsとは:** 自動テスト・自動デプロイの仕組み

**できること:**
- コードをプッシュしたら自動テスト
- mainにマージしたら自動デプロイ
- 定期的にスクリプトを実行

**💡 ARM64での注意:**
- GitHub Actionsはクラウドで実行されるため、ローカルのアーキテクチャは無関係
- ARM64対応のDockerイメージを使用する場合は注意が必要

### 5. Gitの高度なコマンド

```cmd
REM スタッシュ（一時保存）
git stash               REM 変更を一時保存
git stash pop           REM 一時保存を戻す

REM リベース
git rebase main         REM コミット履歴を整理

REM チェリーピック
git cherry-pick コミットID  REM 特定のコミットだけ取り込む

REM タグ
git tag v1.0.0          REM バージョンタグを作成
git push origin v1.0.0  REM タグをプッシュ
```

### 6. GitHubの便利機能

- **Issues:** タスク管理
- **Projects:** プロジェクト管理
- **Wiki:** ドキュメント作成
- **GitHub Pages:** 静的サイトのホスティング
- **GitHub Copilot:** AI コーディングアシスタント（ARM64でも動作）

### 7. ARM64開発環境の最適化

**ARM64 PCを使っている場合の追加tips:**

**開発言語のARM64対応:**
- **Python:** ARM64版あり（python.orgから）
- **Node.js:** ARM64版あり
- **Java:** ARM64版あり（Azul Zulu等）
- **.NET:** ARM64完全対応

**エミュレータの使用:**
- Android Studio: ARM64ネイティブ、Androidエミュレータも高速
- Docker Desktop: ARM64対応（Linuxコンテナのみ）

**開発ツール:**
- Windows Terminal: ARM64ネイティブ
- PowerToys: ARM64対応
- WSL2: ARM64対応（Ubuntu ARM64が動作）

---

## 📚 参考リンク集

### 公式ドキュメント

- [Git公式サイト](https://git-scm.com/)
- [Git公式ドキュメント（日本語）](https://git-scm.com/book/ja/v2)
- [GitHub Docs（日本語）](https://docs.github.com/ja)
- [VSCode公式サイト](https://code.visualstudio.com/)
- [VSCode Git統合](https://code.visualstudio.com/docs/sourcecontrol/overview)

### ARM64関連リソース

- [Windows on ARM](https://www.microsoft.com/windows/windows-on-arm)
- [ARM64版アプリ一覧（非公式）](https://armrepo.ver.lt/)
- [Qualcomm開発者リソース](https://developer.qualcomm.com/software/windows-on-snapdragon)

### 学習リソース

- [サル先生のGit入門](https://backlog.com/ja/git-tutorial/)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=ja)（インタラクティブ学習）
- [GitHub Skills](https://skills.github.com/)（無料コース）

### コミュニティ

- [GitHub Community](https://github.community/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/git)

---

## 🔖 コマンド早見表

### 基本コマンド（cmd/PowerShell共通）

**💡 すべてのコマンドはx64とARM64で同じです！**

```cmd
REM 状態確認
git status                    REM 現在の状態
git log                       REM コミット履歴
git log --oneline             REM コミット履歴（簡潔版）
git log --graph --all         REM コミット履歴（グラフ表示）

REM ステージング
git add .                     REM すべて追加
git add ファイル名            REM 特定ファイル
git add *.py                  REM 特定の種類のファイル
git reset ファイル名          REM ステージング取り消し

REM コミット
git commit -m "メッセージ"    REM コミット
git commit -am "メッセージ"   REM add + commit
git commit --amend            REM 直前のコミットを修正

REM プッシュ・プル
git push origin main          REM プッシュ
git pull origin main          REM プル
git fetch                     REM リモートの情報だけ取得

REM ブランチ
git branch                    REM ブランチ一覧
git branch 名前               REM ブランチ作成
git checkout 名前             REM ブランチ切り替え
git checkout -b 名前          REM 作成 + 切り替え
git merge ブランチ名          REM マージ
git branch -d 名前            REM ブランチ削除

REM 差分確認
git diff                      REM 変更内容を表示
git diff --staged             REM ステージ済みの変更

REM 取り消し
git restore ファイル名        REM ファイルの変更を取り消し
git restore --staged ファイル名  REM ステージング取り消し
git reset --soft HEAD^        REM 直前のコミット取り消し（変更保持）
git reset --hard HEAD^        REM 直前のコミット取り消し（変更削除）

REM リモート
git remote -v                 REM リモートリポジトリ確認
git remote add origin URL     REM リモート追加
git remote set-url origin URL REM リモートURL変更
```

### 設定コマンド

```cmd
REM グローバル設定
git config --global user.name "名前"
git config --global user.email "メール"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main
git config --global core.autocrlf true

REM 設定確認
git config --global --list
git config user.name
git config user.email
```

### アーキテクチャ確認コマンド（Windows）

```powershell
# システムアーキテクチャ確認
$env:PROCESSOR_ARCHITECTURE

# Gitのアーキテクチャ確認
(Get-Item (Get-Command git).Source).VersionInfo.FileDescription

# VSCodeのアーキテクチャ確認（VSCodeのAbout画面を開く）
code --version
```

### VSCodeのショートカット（Windows）

```
Ctrl + Shift + P       コマンドパレット
Ctrl + Shift + G       ソース管理
Ctrl + Shift + X       拡張機能
Ctrl + @               ターミナル
Ctrl + N               新規ファイル
Ctrl + S               保存
Ctrl + ,               設定
Ctrl + Enter           コミット（ソース管理パネル内）
```

---

## ✅ 最終チェックリスト

すべて完了したかチェックしましょう！

### システム確認
- [ ] Windowsのバージョンを確認した（Windows 10/11）
- [ ] アーキテクチャを確認した（x64 or ARM64）
- [ ] 必要な空き容量がある（5GB以上）

### 基本設定
- [ ] Gitがインストールされている（`git --version`）
- [ ] **ARM64ユーザー:** ARM64版Gitを確認した
- [ ] Gitの初期設定完了（user.name, user.email）
- [ ] 改行コード設定（core.autocrlf=true）
- [ ] GitHubアカウントを作成した
- [ ] VSCodeをインストールした
- [ ] **ARM64ユーザー:** ARM64版VSCodeを確認した
- [ ] VSCodeを日本語化した
- [ ] VSCodeとGitHubを連携した

### SSH設定
- [ ] SSHキーを生成した
- [ ] GitHubにSSHキーを登録した
- [ ] **ARM64ユーザー:** キータイトルにARM64と記載した（推奨）
- [ ] SSH接続テストが成功した（`ssh -T git@github.com`）
- [ ] SSH設定ファイルを作成した
- [ ] ssh-agentサービスが起動している

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

### Git操作（コマンドライン）
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

### ARM64ユーザー専用チェック
- [ ] すべてのソフトウェアでARM64ネイティブ版を使用
- [ ] Git: ARM64版確認済み
- [ ] VSCode: ARM64版確認済み
- [ ] パフォーマンスとバッテリー持ちが良好

---

## 🎉 おめでとうございます！

このガイドを完了したあなたは、もう立派なGit/GitHub使いです！

**これからできること:**
- ✅ コードをバージョン管理
- ✅ GitHubでコードを保存・共有
- ✅ チームでの共同開発
- ✅ オープンソースプロジェクトへの貢献
- ✅ ポートフォリオの作成

**💡 ARM64ユーザーへ:**
あなたは最新のARM64テクノロジーを活用し、効率的な開発環境を構築しました！
- ⚡ 高速なパフォーマンス
- 🔋 優れたバッテリー持続時間
- 🌡️ 低発熱
- 🌍 環境に優しい省電力設計

**継続的な学習のために:**
1. 毎日少しずつ使ってみる
2. 小さなプロジェクトから始める
3. わからないことがあれば、このガイドを見返す
4. GitHubの他のプロジェクトを見て学ぶ
5. コミュニティに参加する

**ARM64開発環境の今後:**
- Windows on ARMは急速に進化中
- 対応アプリケーションが日々増加
- パフォーマンスも継続的に改善
- あなたは未来の開発環境を先取りしています！

**最後に:**
- このガイドは常に手元に置いておきましょう
- 困ったときはトラブルシューティングセクションを確認
- 新しいことに挑戦し続けてください
- ARM64 PCの性能を最大限に活用してください

あなたの開発ライフが素晴らしいものになりますように！

**Happy Coding! 🚀**

**Special thanks to ARM64 users! 💪**

---

## 📮 このガイドについて

**バージョン:** 2.0（ARM64完全対応版）
**対応OS:** Windows 10/11
**対応アーキテクチャ:** x64（Intel/AMD）、ARM64（Snapdragon、Microsoft SQ）
**最終更新:** 2025年10月

**このガイドの特徴:**
- ✅ 他の資料を参照する必要なし
- ✅ 完全な初心者対応
- ✅ すべての例外・トラブルをカバー
- ✅ 実践的なシナリオ付き
- ✅ VSCodeとコマンドライン両対応
- ✅ Windows特有の問題に完全対応
- ✅ **x64とARM64の両方に完全対応**
- ✅ **ARM64特有の注意点を詳細に記載**
- ✅ **最新のWindows on ARM環境に最適化**

**ARM64対応の詳細:**
- すべてのダウンロードリンクでx64とARM64を明確に区別
- アーキテクチャの確認方法を複数掲載
- ARM64ネイティブ版の確認コマンドを提供
- エミュレーションとネイティブの違いを説明
- パフォーマンスとバッテリー効率の最適化tips

**このガイドで学べること:**
1. Gitの基礎から実践まで
2. GitHubの使い方
3. VSCodeとの連携
4. トラブルシューティング
5. 実務で使えるワークフロー
6. **ARM64環境での最適な開発セットアップ**

**対応デバイス:**
- **x64:** すべてのIntel/AMD搭載Windows PC
- **ARM64:** 
  - Surface Pro X / Surface Pro 9 5G
  - Surface Laptop 5 / Surface Laptop 6
  - Samsung Galaxy Book S / Book2 Go
  - Lenovo ThinkPad X13s
  - ASUS Vivobook S 15
  - Microsoft Copilot+ PC（全機種）
  - その他Snapdragon搭載Windowsデバイス

このガイドがあなたの開発の第一歩をサポートできれば幸いです！

---

## 🔄 改訂履歴

**Version 2.0 (2025年10月) - ARM64完全対応版**
- ARM64アーキテクチャへの完全対応を追加
- x64とARM64の違いを明確化
- ソフトウェアダウンロード時の注意点を詳細化
- ARM64ネイティブ版の確認方法を追加
- パフォーマンス最適化のtipsを追加
- ARM64特有のトラブルシューティングを追加

**Version 1.0 (2025年10月) - 初版**
- Windows版の基本ガイドを作成
- x64環境を中心に解説

---

**🌟 あなたは完璧な開発環境を手に入れました！🌟**
