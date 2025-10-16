# 🐍 Python開発環境 完全構築ガイド 2025

**【Mac M2 + VSCode + pyenv + venv - 絶対に失敗しない決定版】**

> **📌 このガイドの特徴**
> - ✅ 他の資料は一切不要！このガイドだけで100%完了
> - ✅ すべてのコマンドを実行結果付きで解説  
> - ✅ よくあるエラーと解決方法を完全網羅
> - ✅ 2025年1月時点の最新情報
> - ✅ AI/生成AI開発にも完全対応

---

## 📑 クイックナビゲーション

### 🎯 あなたの状況に合わせて選択

**今すぐ環境構築したい →** [PART 2: 基本環境構築](#part-2-基本環境構築)

**理解してから進みたい →** [PART 1: 準備と理解](#part-1-準備と理解)

**エラーが出た →** [PART 6: トラブルシューティング](#part-6-トラブルシューティング)

**AI開発がしたい →** [PART 5: AI/生成AI開発](#part-5-ai生成ai開発)

---

## 目次

### PART 1: 準備と理解
1. [Python環境の選択肢を完全理解](#1-python環境の選択肢を完全理解)
2. [なぜpyenv + venvなのか？](#2-なぜpyenv--venvなのか)
3. [完成イメージ](#3-完成イメージ)
4. [表記ルール](#4-表記ルール)

### PART 2: 基本環境構築
5. [現在の状態確認](#5-現在の状態確認)
6. [Homebrewインストール](#6-homebrewインストール)
7. [pyenvインストール](#7-pyenvインストール)
8. [Pythonインストール](#8-pythonインストール)
9. [venv使い方](#9-venv使い方)

### PART 3: VSCode統合
10. [VSCode Python設定](#10-vscode-python設定)

### PART 4: 実践プロジェクト
11. [新規プロジェクト作成](#11-新規プロジェクト作成)
12. [既存プロジェクトクローン](#12-既存プロジェクトクローン)
13. [requirements.txt管理](#13-requirementstxt管理)

### PART 5: AI/生成AI開発
14. [AI開発環境](#14-ai開発環境)

### PART 6: トラブルシューティング
15. [エラー解決](#15-エラー解決)
16. [よくある質問](#16-よくある質問)

---

## PART 1: 準備と理解

### 1. Python環境の選択肢を完全理解

#### 8つの選択肢

| # | 選択肢 | 推奨度 | 対象 |
|---|--------|--------|------|
| 1 | macOSプリインストール | ❌❌❌ | 使わない |
| 2 | python.org公式 | ❌❌ | Windows推奨 |
| 3 | **pyenv** | ⭐⭐⭐⭐⭐ | **Mac/Linux必須** |
| 4 | **venv** | ⭐⭐⭐⭐⭐ | **全員必須** |
| 5 | uv | ⭐⭐⭐⭐ | 上級者 |
| 6 | Anaconda | ⭐⭐⭐ | データサイエンス |
| 7 | Poetry | ⭐⭐⭐ | モダン開発 |
| 8 | Docker | ⭐⭐⭐⭐ | 本番環境 |

#### 詳細比較

**1. macOSプリインストール版**

❌ **絶対に使わない理由:**
```bash
# これはシステム用Python
/usr/bin/python3

# 問題点:
# - macOSシステムが使用（触ると壊れる）
# - バージョンが古い（macOS依存）
# - パッケージインストール制限
# - プロジェクト管理不可
```

**2. python.org公式版**

⚠️ **Mac非推奨:**
- バージョン切り替え不可
- 複数バージョン管理困難
- PATH設定複雑
- アンインストール面倒

**3. pyenv** ⭐⭐⭐⭐⭐

✅ **これを使う！**

```
役割: Pythonバージョン管理ツール

できること:
- Python 3.9, 3.10, 3.11, 3.12を共存
- プロジェクトごとにバージョン指定
- 簡単にインストール・切り替え

メリット:
✅ 複数バージョン共存
✅ プロジェクト別バージョン
✅ システムPythonに影響なし
✅ Mac/Linux標準

デメリット:
⚠️ 初期設定が必要
⚠️ Windows非対応（pyenv-win必要）
```

**4. venv** ⭐⭐⭐⭐⭐

✅ **これも使う！**

```
役割: 仮想環境作成ツール（Python標準）

できること:
- プロジェクトごとに独立環境
- パッケージを分離管理

メリット:
✅ Python標準搭載（追加不要）
✅ 完全クロスプラットフォーム
✅ 軽量・シンプル
✅ プロジェクト間干渉なし

用途:
pyenv: Pythonバージョン管理
venv: パッケージ管理
```

**pyenv vs venv の違い:**

```
┌─────────────────────────────────────┐
│         pyenv（バージョン管理）        │
│  ┌─────────────────────────────┐   │
│  │  Python 3.9                  │   │
│  │  ├─ venv1 (Django 4.2)      │   │
│  │  └─ venv2 (Flask 2.3)       │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │  Python 3.12                 │   │
│  │  ├─ venv3 (Django 5.0)      │   │
│  │  └─ venv4 (FastAPI 0.109)   │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘

両方使う理由:
- pyenv: Pythonバージョンを選ぶ
- venv: パッケージを分離する
```

**5. uv** ⭐⭐⭐⭐

⚡ **次世代ツール（上級者向け）**

```
特徴:
- Rust製超高速ツール
- pip + venv + pyenv統合
- 10〜100倍速い

推奨タイミング:
1. pyenv + venvマスター
2. 3〜6ヶ月Python開発経験
3. より高速な環境が欲しい時

初心者は:
❌ まだ使わない
✅ pyenv + venvから始める
```

**6. conda/Anaconda** ⭐⭐⭐

📊 **データサイエンス特化**

```
向いている:
✅ データサイエンス専門
✅ 科学計算ライブラリ多用
✅ GUI管理が好き

向いていない:
❌ Web開発
❌ 汎用Python開発
❌ 容量節約したい（数GB）

結論:
AI開発でもpyenv + venvで十分
```

**7. Poetry** ⭐⭐⭐

🎨 **モダンプロジェクト管理**

```
特徴:
- pyproject.toml一元管理
- 依存関係解決優秀
- 仮想環境自動作成

推奨タイミング:
慣れてから（6ヶ月後）

初心者は:
❌ 学習コスト高い
✅ まずpyenv + venv
```

**8. Docker** ⭐⭐⭐⭐

🐳 **本番環境・チーム開発**

```
用途:
- 本番環境
- CI/CD
- チーム開発

推奨:
開発: pyenv + venv
本番: Docker

初心者は:
✅ ローカル開発はpyenv + venv
✅ 慣れたらDockerも学ぶ
```

---

### 2. なぜpyenv + venvなのか？

#### 結論

```
Mac/Linux開発者にとって:

pyenv + venv = 黄金の組み合わせ

理由:
1. ✅ 柔軟性: 複数バージョン自在
2. ✅ 分離性: プロジェクト完全独立
3. ✅ 標準性: コミュニティ標準
4. ✅ シンプル: 最小構成
5. ✅ AI対応: ML/DL開発も最適
6. ✅ 学習: 転職先でも通用
```

#### 実例で理解

**シナリオ: 3つのプロジェクトを担当**

```bash
# お客様A: Python 3.9 + Django 4.2
~/Projects/客A/
  └─ project-a/
      ├─ .python-version (3.9.18)
      └─ .venv/ (Django==4.2)

# お客様B: Python 3.12 + Django 5.0
~/Projects/客B/
  └─ project-b/
      ├─ .python-version (3.12.1)
      └─ .venv/ (Django==5.0)

# 自分: Python 3.11 + FastAPI
~/Projects/my/
  └─ my-api/
      ├─ .python-version (3.11.7)
      └─ .venv/ (FastAPI==0.109)

# 完全に独立！干渉ゼロ！
```

**日常の切り替え:**

```bash
# 午前: お客様Aのプロジェクト
cd ~/Projects/客A/project-a
source .venv/bin/activate
python --version
# → Python 3.9.18
pip list
# → Django 4.2

# 午後: お客様Bのプロジェクト  
cd ~/Projects/客B/project-b
source .venv/bin/activate
python --version
# → Python 3.12.1
pip list
# → Django 5.0

# シームレス！
```

#### Windows開発者との共存

**チーム開発での共通言語:**

```
Mac開発者:
  pyenv + venv + requirements.txt

Windows開発者:
  公式Python + venv + requirements.txt

共通:
  ✅ venv（完全互換）
  ✅ requirements.txt（環境共有）

相違:
  - Pythonインストール方法のみ
  - venv有効化コマンドのみ
```

**README例:**

```markdown
# セットアップ

## Mac/Linux
```bash
pyenv local 3.12.1
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Windows
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
```

---

### 3. 完成イメージ

#### フォルダ構造

```
/Users/あなた/
├─ .pyenv/                    # pyenvホーム
│  └─ versions/               # Pythonバージョン
│     ├─ 3.9.18/
│     ├─ 3.11.7/
│     └─ 3.12.1/
│
└─ Projects/                  # プロジェクト置き場
   ├─ 客A/
   │  └─ project-a/
   │     ├─ .python-version   # 3.9.18
   │     ├─ .venv/            # 仮想環境
   │     ├─ .gitignore
   │     ├─ requirements.txt
   │     └─ (ソースコード)
   │
   ├─ 客B/
   │  └─ project-b/
   │     ├─ .python-version   # 3.12.1
   │     ├─ .venv/
   │     ├─ requirements.txt
   │     └─ (ソースコード)
   │
   └─ my/
      └─ my-project/
          ├─ .python-version   # 3.11.7
          ├─ .venv/
          ├─ requirements.txt
          └─ (ソースコード)
```

#### 完成後にできること

```bash
# ✅ 複数Pythonバージョン管理
pyenv versions
# * 3.9.18
#   3.11.7
#   3.12.1

# ✅ プロジェクトごとにバージョン切り替え
cd project-a && python --version
# Python 3.9.18
cd project-b && python --version  
# Python 3.12.1

# ✅ パッケージ完全分離
cd project-a && pip list
# Django 4.2
cd project-b && pip list
# Django 5.0

# ✅ 干渉ゼロ！
```

---

### 4. 表記ルール

#### 重要度マーク

| マーク | 意味 | 説明 |
|--------|------|------|
| ✅ **必須** | 絶対実行 | スキップNG |
| 🔶 **推奨** | 強く推奨 | なくても動くがベスト |
| ⭐ **任意** | 便利 | 好みによる |

#### 実行場所

| マーク | 場所 | 例 |
|--------|------|-----|
| 🌍 **どこでもOK** | 任意 | `brew --version` |
| 📁 **プロジェクト内** | プロジェクトフォルダ | `source .venv/bin/activate` |
| 🏠 **ホーム推奨** | `~/` | `mkdir ~/Projects` |

#### 再実行影響

| マーク | 影響 | 例 |
|--------|------|-----|
| 🟢 **OK** | 何度でも | `brew install pyenv` |
| 🟡 **注意** | 重複 | `echo >> ~/.zshrc` |
| 🔴 **NG** | 1回のみ | `python -m venv .venv` |

#### コマンド表記

```bash
# コメント（説明）
コマンド  # ← 実行する

# 出力結果
表示される内容
```

---

## PART 2: 基本環境構築

### 5. 現在の状態確認

#### チェックリスト

```bash
# ✅ 前提条件確認

# 1. Mac M2か？
system_profiler SPHardwareDataType | grep "Chip"
# Apple M2 と表示されればOK

# 2. macOSバージョン
sw_vers
# ProductVersion: 14.x以降推奨

# 3. Git設定済みか？
git --version
git config --global user.name
git config --global user.email

# 4. VSCode設置済みか？
code --version

# 5. Docker設定済みか？
docker --version

# 6. GitHub SSH接続済みか？
ssh -T git@github.com
# Hi username! と表示されればOK
```

**すべてOK？ → 次へ進む**

**NGがある？ → 該当部分を先に設定**

---

### 6. Homebrewインストール

#### ステップ6-1: 確認

✅ **必須**  
📍 🌍 どこでもOK  
🔄 🟢 何度でもOK

```bash
brew --version
```

**✅ 表示例:**
```
Homebrew 4.2.9
```
→ **既にあり！ステップ6-4へジャンプ**

**❌ エラー:**
```
-bash: brew: command not found
```
→ **次のステップ6-2へ**

#### ステップ6-2: インストール

✅ **必須**  
📍 🌍 どこでもOK  
🔄 🟡 既にある場合不要

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**💡 このコマンドの意味:**
```
/bin/bash -c "..."
└─┬─┘ └┬┘ └───┬────
  │    │      └─ "..."の中身を実行
  │    └─ コマンド実行オプション
  └─ bashシェルを実行

curl -fsSL URL
└┬┘ └─┬──┘ └┬┘
 │    │      └─ ダウンロード元URL
 │    └─ オプション（fail/silent/show error/Location）
 └─ ダウンロードツール
```

**実行時の流れ:**

**1. パスワード要求:**
```
Password: _
```
→ Macログインパスワード入力（見えないが入力されている）

**2. Enter要求:**
```
Press RETURN to continue or any other key to abort:
```
→ Enterキー押下

**3. インストール中:**
```
==> Downloading and installing Homebrew...
...（数分かかる）...
```

**4. 完了メッセージ:**
```
==> Installation successful!

==> Next steps:
- Run these commands in your terminal:
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
```

#### ステップ6-3: PATH設定

✅ **必須**（M2 Mac）  
📍 🌍 どこでもOK  
🔄 🟡 重複注意

**シェル確認:**
```bash
echo $SHELL
```

**zshの場合（M2 Macデフォルト）:**
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**bashの場合:**
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.bash_profile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**💡 重複チェック:**
```bash
grep -c "brew shellenv" ~/.zshrc
# 1 → 正常
# 2以上 → 重複（動作は問題ないが整理推奨）
```

#### ステップ6-4: 確認

✅ **必須**

**ターミナル再起動:**
```bash
# ⌘ + Q で完全終了
# ターミナル再起動
```

**確認:**
```bash
brew --version
```

**✅ 成功:**
```
Homebrew 4.2.9
Homebrew/homebrew-core (git revision...
```

#### ステップ6-5: 更新

✅ **必須**

```bash
brew update
```

**✅ 成功:**
```
Already up-to-date.
```

または

```
Updated 1 tap (homebrew/core).
==> New Formulae
...
```

**🎉 Homebrew完了！**

---

### 7. pyenvインストール

#### ステップ7-1: インストール

✅ **必須**  
📍 🌍 どこでもOK  
🔄 🟢 何度でもOK

```bash
brew install pyenv
```

**実行結果:**
```
==> Downloading https://ghcr.io/v2/homebrew/core/pyenv/manifests/2.3.36
...
==> Pouring pyenv--2.3.36.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pyenv/2.3.36: xxx files, xx.xMB
```

**⏰ 所要時間: 2-3分**

**💡 最後にヒントメッセージが表示されることがあります:**
```
Disable this behaviour by setting `HOMEBREW_NO_INSTALL_CLEANUP=1`.
Hide these hints with 'HOMEBREW_NO_ENV_HINTS=1` (see `man brew`).
```
**👉 これはエラーではありません！無視してOK！次へ進んでください**

---

#### ステップ7-2: PATH設定【超重要・超詳細版】

✅ **必須**  
📍 🌍 **どこで実行してもOK**（重要！）  
🔄 🟡 重複注意

---

##### 🎯 最重要ポイント

**結論: この設定コマンドは、今どこのフォルダにいても実行できます！**

理由:
- ✅ デスクトップで実行してもOK
- ✅ ホームディレクトリで実行してもOK
- ✅ プロジェクトフォルダで実行してもOK
- ✅ ダウンロードフォルダで実行してもOK
- ✅ **どこで実行しても同じ結果になります**

---

##### 📂 なぜ「どこでもOK」なのか？

```bash
echo '設定内容' >> ~/.zshrc
                   └───┬───┘
                       └─ このファイルは常に同じ場所にある
```

**重要な理解:**
- `~/.zshrc` というファイルは**常に**あなたのホームディレクトリにあります
- `~/` は**どこから実行しても**「あなたのホームディレクトリ」を意味します
- だから、**今いる場所（カレントディレクトリ）は関係ない**んです！

**具体例:**
```bash
# デスクトップから実行
cd ~/Desktop
echo 'test' >> ~/.zshrc
# → /Users/あなた/.zshrc に書き込まれる

# プロジェクトフォルダから実行
cd ~/Projects/my-project
echo 'test' >> ~/.zshrc
# → /Users/あなた/.zshrc に書き込まれる（同じファイル！）

# 結論: どこから実行しても、編集するファイルは同じ！
```

---

##### 🏠 参考: ホームディレクトリとは？

```
ホームディレクトリ = あなた専用のフォルダ

記号: ~ (チルダ)
実体: /Users/あなたのユーザー名

例:
~ = /Users/tanaka
~ = /Users/yamada
```

**ホームディレクトリに移動:**
```bash
cd ~
# または単に
cd
```

**現在地確認:**
```bash
pwd
# 表示例: /Users/あなたのユーザー名
```

---

##### 🎬 実行手順

**ステップ1: シェルの種類を確認**

```bash
echo $SHELL
```

**パターンA: zshの場合（M2 Macのデフォルト）**
```
/bin/zsh
```
→ 次のzsh用コマンドを実行

**パターンB: bashの場合**
```
/bin/bash
```
→ 後述のbash用コマンドを実行

---

**ステップ2-A: zsh用コマンド実行（ほとんどの人）**

**💡 今いる場所は関係ありません！そのまま実行してOK！**

```bash
# 1行目
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
```
**実行後:** 何も表示されない → **正常です！**

```bash
# 2行目
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
```
**実行後:** 何も表示されない → **正常です！**

```bash
# 3行目
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
```
**実行後:** 何も表示されない → **正常です！**

```bash
# 4行目
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```
**実行後:** 何も表示されない → **正常です！**

**👉 エラーが出なければ成功！次の確認へ**

---

**全部まとめてコピペもOK:**

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

---

**ステップ2-B: bash用コマンド（少数派）**

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

---

**ステップ3: 設定できたか確認**

```bash
cat ~/.zshrc
```

**✅ ファイルの最後の方にこの4行があればOK:**
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

**💡 他にも色々書いてあっても大丈夫！この4行が追加されていればOK！**

---

**ステップ4: 重複チェック（重要！）**

```bash
grep -c "PYENV_ROOT" ~/.zshrc
```

**💡 重要な理解:**
設定4行の中で`PYENV_ROOT`は2箇所に出現します：
```bash
export PYENV_ROOT="$HOME/.pyenv"      # ← 1箇所目
export PATH="$PYENV_ROOT/bin:$PATH"   # ← 2箇所目
```

**✅ 表示が「2」:**
```
2
```
→ **完璧！正常です！次のステップへ**

**⚠️ 表示が「4」以上:**
```
4
```
→ **重複しています（2セット以上）。後述の修正方法へ**

**判定基準:**
- **2** = 1セット（正常）✅
- **4** = 2セット（重複）⚠️
- **6** = 3セット（重複）⚠️

---

##### 💡 各コマンドの意味

```bash
export PYENV_ROOT="$HOME/.pyenv"
# pyenvのホームディレクトリ設定

export PATH="$PYENV_ROOT/bin:$PATH"
# pyenvコマンドを使えるようにPATHに追加

eval "$(pyenv init --path)"
# pyenvのパス初期化

eval "$(pyenv init -)"
# pyenv本体の初期化
```

---

##### 🔧 重複してしまった場合の修正

**確認:**
```bash
grep -c "PYENV_ROOT" ~/.zshrc
```

**💡 判定:**
- **2** = 正常（1セット）✅
- **4** = 重複（2セット）⚠️
- **6** = 重複（3セット）⚠️

**4以上の場合は修正が必要です**

**修正手順:**

**1. ファイルを開く:**
```bash
open -e ~/.zshrc
```
**💡 テキストエディットで開きます**

**2. 重複を探す:**

以下の4行が**複数回**書かれているか確認：
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

**3. 削除:**
- 重複している部分を削除（1セットだけ残す）
- 通常はファイルの最後の方にあります

**4. 保存:**
- `⌘ + S` で保存
- テキストエディットを閉じる

**5. 確認:**
```bash
grep -c "PYENV_ROOT" ~/.zshrc
# 2 になっていればOK（1セット = PYENV_ROOTが2箇所出現）
```

---

#### ステップ7-3: 反映【超詳細版】

✅ **必須**

**💡 重要な理解:**
PATH設定をしただけでは**まだ有効になっていません**。

理由: `.zshrc`ファイルはターミナル起動時に読み込まれるため

**有効にする方法は2つ:**

---

##### 方法1: sourceコマンドで反映（推奨）

**💡 今いる場所は関係ありません！そのまま実行してOK！**

```bash
source ~/.zshrc
```

**実行後:**
```
（何も表示されない）
```
**👉 エラーが出なければ成功！**

---

##### 方法2: ターミナル再起動（より確実）

**手順:**

**1. ターミナルを完全に終了**
```
⌘ + Q キーを押す
```
**💡 重要: ウィンドウを閉じる（⌘ + W）だけではダメ！**
**完全終了（⌘ + Q）が必要！**

**2. ターミナルを再起動**
- Spotlight（⌘ + Space）→「ターミナル」
- または、アプリケーション → ユーティリティ → ターミナル

**3. 自動的に設定が反映される**

---

#### ステップ7-4: 確認

✅ **必須**

```bash
pyenv --version
```

**✅ 成功の表示:**
```
pyenv 2.3.36
```
**または**
```
pyenv 2.3.35
```
**👉 バージョン番号が表示されればOK！（数字は多少違ってもOK）**

---

**❌ エラーが出た場合:**

**表示:**
```
-bash: pyenv: command not found
```

**対処法:**

**1. ターミナル完全再起動:**
```bash
# ⌘ + Q でターミナル完全終了
# 再起動後
pyenv --version
```

**2. シェル確認:**
```bash
echo $SHELL
```
- `/bin/bash` の場合 → ステップ7-2でbash用コマンド実行したか確認

**3. 設定ファイル確認:**
```bash
cat ~/.zshrc
```
4行の設定が書かれているか確認

**4. もう一度設定実行:**
```bash
# もう一度実行（重複しても動作します）
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# 反映
source ~/.zshrc

# 確認
pyenv --version
```

---

**🎉 pyenv完了！次のステップへ進みましょう！**

---

### 8. Pythonインストール

#### ステップ8-1: インストール可能バージョン確認

⭐ **任意**

```bash
pyenv install --list | grep "^\s*3\.[0-9]*\.[0-9]*$"
```

**表示例:**
```
  3.9.18
  3.10.13
  3.11.7
  3.12.1
  3.13.0
```

**💡 2025年1月時点の推奨:**
- **3.12.1**: 最新安定版
- **3.11.7**: 互換性重視
- **3.9.18**: レガシープロジェクト

#### ステップ8-2: Python 3.12インストール

✅ **必須**  
📍 🌍 どこでもOK  
🔄 🟢 既にあれば「already installed」

```bash
pyenv install 3.12.1
```

**実行結果:**
```
Downloading Python-3.12.1.tar.xz...
-> https://www.python.org/ftp/python/3.12.1/Python-3.12.1.tar.xz
Installing Python-3.12.1...
...
Installed Python-3.12.1 to /Users/あなた/.pyenv/versions/3.12.1
```

**⏰ 所要時間: 5-10分**

**💡 コーヒーブレイク推奨 ☕**

#### ステップ8-3: Python 3.11インストール

🔶 **推奨**（互換性のため）

```bash
pyenv install 3.11.7
```

**⏰ 所要時間: 5-10分**

#### ステップ8-4: インストール確認

✅ **必須**

```bash
pyenv versions
```

**✅ 表示:**
```
* system (set by /Users/あなた/.pyenv/version)
  3.11.7
  3.12.1
```

**💡 `*` = 現在使用中**

#### ステップ8-5: グローバルバージョン設定

✅ **必須**

```bash
pyenv global 3.12.1
```

**何も表示されなければOK**

---

##### 🎯 なぜこのステップが必須なのか？

**問題: 設定しないとどうなる？**

```bash
# グローバル設定をしない状態で
python --version

# 表示される可能性:
Python 2.7.18  # ← macOSプリインストール版（古い！）
# または
Python 3.9.6   # ← macOSシステム版（これも使わない！）
# または
-bash: python: command not found  # ← コマンドが見つからない
```

**グローバル設定の役割:**

```
【インストールしただけの状態】
┌────────────────────────────┐
│ pyenvの中にPythonがある     │
│  ├─ Python 3.11.7          │
│  └─ Python 3.12.1          │
└────────────────────────────┘
      ↓
 使える状態だが
 どれを使うか指定していない


【グローバル設定後】
┌────────────────────────────┐
│ デフォルトのPythonを指定    │
│  ├─ Python 3.11.7          │
│  └─ Python 3.12.1 ← これ！  │
└────────────────────────────┘
      ↓
 pythonコマンド = 3.12.1
```

**必須の4つの理由:**

**1. デフォルトPythonの指定**
```
設定しないと:
❌ システムPythonが使われる
❌ 古いバージョン（2.7や3.9）
❌ pyenvでインストールした意味がない

設定すると:
✅ pyenv管理下のPythonが使われる
✅ 最新版（3.12.1）
✅ 正しい環境で開発できる
```

**2. どこでも同じバージョン**
```bash
# 設定後は、どこでも同じ
cd ~/Desktop
python --version  # 3.12.1

cd ~/Downloads
python --version  # 3.12.1
```

**3. この先の手順でpythonコマンドを使う**
```bash
python -m venv .venv  # ← pythonコマンド使用
pip install django    # ← pipもpythonに依存

# グローバル設定がないと、これらが正しく動かない
```

**4. プロジェクトのlocal設定の基準になる**
```
プロジェクトA:
- globalは3.12.1（ベースライン）
- localで3.9.18を指定 → 3.9.18が使われる

プロジェクトB:
- globalは3.12.1
- local指定なし → 3.12.1が使われる（globalのおかげ）
```

**所要時間: 5秒**
**効果: この先のトラブルを全て回避**

#### ステップ8-6: 確認

✅ **必須**

```bash
python --version
```

**✅ 成功:**
```
Python 3.12.1
```

**❌ 古いバージョン表示:**
```bash
# 再設定
source ~/.zshrc
pyenv rehash
python --version
```

#### ステップ8-7: pip確認

✅ **必須**

```bash
pip --version
```

**✅ 表示:**
```
pip 23.3.1 from /Users/あなた/.pyenv/versions/3.12.1/lib/python3.12/site-packages/pip (python 3.12)
```

**💡 pyenvのパスが表示されていればOK**

#### ステップ8-8: pip更新

✅ **必須**

```bash
pip install --upgrade pip
```

**✅ 成功:**
```
Successfully installed pip-24.0
```

**🎉 Python環境完成！**

---

### 9. venv使い方

#### venvとは？

```
venv = 仮想環境作成ツール（Python標準）

役割:
プロジェクトごとに独立した環境を作る

なぜ必要?
┌─────────────────────────────┐
│ ❌ グローバル環境の問題       │
├─────────────────────────────┤
│ プロジェクトA: Django 4.2    │
│ プロジェクトB: Django 5.0    │
│ → 同時に使えない！           │
└─────────────────────────────┘

┌─────────────────────────────┐
│ ✅ 仮想環境で解決            │
├─────────────────────────────┤
│ プロジェクトA: .venv/        │
│   └─ Django 4.2             │
│ プロジェクトB: .venv/        │
│   └─ Django 5.0             │
│ → 完全に独立！               │
└─────────────────────────────┘
```

#### 基本コマンド4つ

**1. 作成**

✅ **必須**  
📍 📁 プロジェクト内  
🔄 🔴 再実行で初期化（注意）

```bash
python -m venv .venv
```

**コマンド詳細:**
```
python -m venv .venv
└──┬─┘ └┬┘└┬┘ └─┬─┘
   │    │  │    └─ フォルダ名（推奨: .venv）
   │    │  └─ モジュール名
   │    └─ モジュール実行オプション
   └─ Python実行
```

**⚠️ 重要: 再実行すると？**
```bash
# 初回
python -m venv .venv
pip install django
pip list
# Django表示

# 誤って再実行
python -m venv .venv
pip list
# Djangoが消えている！
```

**💡 だからrequirements.txt重要！**

**2. 有効化**

✅ **必須**  
📍 📁 `.venv`があるフォルダ  
🔄 🟢 何度でもOK

```bash
# Mac/Linux
source .venv/bin/activate
```

**成功すると:**
```bash
(.venv) user@MacBook project %
└──┬──┘
   └─ 有効化されている印
```

**Windows版:**
```bash
.venv\Scripts\activate
```

**3. 無効化**

⭐ **任意**

```bash
deactivate
```

**プロンプトが元に戻る:**
```bash
user@MacBook project %
# (.venv) が消える
```

**4. 削除**

⭐ **任意**（やり直したい時）

```bash
# 無効化
deactivate

# フォルダ削除
rm -rf .venv

# 再作成
python -m venv .venv
```

#### 実践練習

```bash
# 練習フォルダ作成
mkdir ~/python-test
cd ~/python-test

# 仮想環境作成
python -m venv .venv

# 確認
ls -la
# .venv/ が作成されている

# 有効化
source .venv/bin/activate

# プロンプト確認
# (.venv) が表示される

# Pythonバージョン
python --version
# Python 3.12.1

# pip確認
pip list
# pip, setuptools のみ

# パッケージインストール
pip install requests

# 確認
pip list
# pip, setuptools, requests, その他依存

# 無効化
deactivate

# プロンプト確認
# (.venv) が消える

# グローバルで確認
pip list
# requestsは入っていない

# 練習フォルダ削除
cd ~
rm -rf ~/python-test
```

**🎉 venv理解完了！**

---

## PART 3: VSCode統合

### 10. VSCode Python設定

#### ステップ10-1: 拡張機能インストール

✅ **必須**

**手順:**
1. VSCode起動
2. 左サイドバー「拡張機能」（`⌘ + Shift + X`）
3. 検索: `Python`
4. **Python** (Microsoft) を選択
5. 「インストール」クリック

**同時インストール:**
- Pylance（言語サーバー）
- Python Debugger

#### ステップ10-2: インタープリター選択

✅ **必須**（プロジェクトごと）

**方法1: コマンドパレット**
```
⌘ + Shift + P
→ "Python: Select Interpreter"
→ Python 3.12.1 選択
```

**方法2: ステータスバー**
```
右下のPythonバージョン表示クリック
→ リストから選択
```

#### ステップ10-3: 仮想環境自動認識

✅ **必須**

**settings.json:**
```
⌘ + Shift + P
→ "Preferences: Open User Settings (JSON)"
```

**追加:**
```json
{
  "python.terminal.activateEnvironment": true,
  "python.defaultInterpreterPath": "python",
  "python.analysis.typeCheckingMode": "basic",
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.venv": false
  }
}
```

#### ステップ10-4: 動作確認

⭐ **任意**

**test.py作成:**
```python
print("Hello, Python!")
```

**実行方法:**
- **方法1:** 右上▶️ボタン
- **方法2:** 右クリック →「Run Python File」
- **方法3:** ターミナルで `python test.py`

**✅ 出力:**
```
Hello, Python!
```

**🎉 VSCode設定完了！**

---

## PART 4: 実践プロジェクト

### 11. 新規プロジェクト作成

#### シナリオ: Djangoブログアプリ

**完全手順:**

```bash
# ステップ1: フォルダ作成
mkdir -p ~/Projects/my-blog
cd ~/Projects/my-blog

# ステップ2: Pythonバージョン指定
pyenv local 3.12.1

# 確認
cat .python-version
# 3.12.1

# ステップ3: 仮想環境作成
python -m venv .venv

# ステップ4: 有効化
source .venv/bin/activate

# プロンプト確認
# (.venv) が表示される

# ステップ5: pip更新
pip install --upgrade pip

# ステップ6: Django install
pip install django

# ステップ7: プロジェクト作成
django-admin startproject config .

# フォルダ構造確認
tree -L 2 -a
# .
# ├── .python-version
# ├── .venv/
# ├── config/
# │   ├── __init__.py
# │   ├── asgi.py
# │   ├── settings.py
# │   ├── urls.py
# │   └── wsgi.py
# └── manage.py

# ステップ8: データベース初期化
python manage.py migrate

# ステップ9: スーパーユーザー作成
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: (入力)

# ステップ10: 開発サーバー起動
python manage.py runserver

# ブラウザで http://127.0.0.1:8000/ 確認

# ステップ11: requirements.txt作成
pip freeze > requirements.txt

# ステップ12: .gitignore作成
cat > .gitignore << 'EOF'
.venv/
__pycache__/
*.py[cod]
*.sqlite3
.DS_Store
EOF

# ステップ13: Git初期化
git init
git add .
git commit -m "Initial commit"

# ステップ14: VSCodeで開く
code .
```

**完成！🎉**

---

### 12. 既存プロジェクトクローン

#### シナリオ: GitHubからクローン

```bash
# ステップ1: クローン
cd ~/Projects
git clone git@github.com:client/project.git
cd project

# ステップ2: README確認
cat README.md
# → Python 3.11必要と記載

# ステップ3: Python 3.11インストール
pyenv install 3.11.7
pyenv local 3.11.7

# ステップ4: 仮想環境作成
python -m venv .venv
source .venv/bin/activate

# ステップ5: 依存パッケージインストール
pip install --upgrade pip
pip install -r requirements.txt

# ステップ6: 環境変数設定（必要なら）
cp .env.example .env
# .envを編集

# ステップ7: データベース設定
python manage.py migrate

# ステップ8: 起動
python manage.py runserver

# ステップ9: VSCodeで開く
code .
```

**完了！🎉**

---

### 13. requirements.txt管理

#### 作成

✅ **必須**（プロジェクト完成時）

```bash
# 仮想環境有効化状態で
pip freeze > requirements.txt
```

**内容確認:**
```bash
cat requirements.txt
```

**例:**
```
asgiref==3.7.2
Django==5.0.1
sqlparse==0.4.4
```

#### インストール

✅ **必須**（新環境セットアップ時）

```bash
pip install -r requirements.txt
```

#### 更新

✅ **必須**（新パッケージ追加時）

```bash
# 1. パッケージインストール
pip install 新パッケージ

# 2. requirements.txt更新
pip freeze > requirements.txt

# 3. Git commit
git add requirements.txt
git commit -m "Add 新パッケージ"
git push
```

#### ベストプラクティス

**シンプル版（推奨）:**
```txt
Django==5.0.1
requests==2.31.0
python-dotenv==1.0.0
```

**完全版（本番環境）:**
```bash
pip freeze > requirements.txt
```

**分割管理（大規模）:**
```
requirements/
├── base.txt      # 共通
├── dev.txt       # 開発環境
└── prod.txt      # 本番環境
```

**base.txt:**
```txt
Django==5.0.1
requests==2.31.0
```

**dev.txt:**
```txt
-r base.txt
pytest==7.4.3
black==23.12.0
```

**prod.txt:**
```txt
-r base.txt
gunicorn==21.2.0
psycopg2-binary==2.9.9
```

**インストール:**
```bash
# 開発環境
pip install -r requirements/dev.txt

# 本番環境
pip install -r requirements/prod.txt
```

---

## PART 5: AI/生成AI開発

### 14. AI開発環境

#### 基本セットアップ

```bash
# プロジェクト作成
mkdir -p ~/Projects/ai-project
cd ~/Projects/ai-project

# Python 3.11（AI開発安定版）
pyenv local 3.11.7

# 仮想環境
python -m venv .venv
source .venv/bin/activate

# 基本ライブラリ
pip install --upgrade pip
pip install numpy pandas matplotlib scikit-learn jupyter
```

#### Jupyter Notebook

🔶 **推奨**

```bash
# インストール
pip install jupyter

# 起動
jupyter notebook

# ブラウザが自動で開く
```

#### TensorFlow（M2 Mac）

⭐ **任意**（DL開発時）

```bash
# M2 Mac用TensorFlow
pip install tensorflow-macos tensorflow-metal
```

**確認:**
```python
import tensorflow as tf
print(tf.__version__)
print("GPU:", tf.config.list_physical_devices('GPU'))
```

**✅ 出力例:**
```
2.15.0
GPU: [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

#### PyTorch

⭐ **任意**（DL開発時）

```bash
# PyTorch公式で最新コマンド確認
# https://pytorch.org/get-started/locally/

# M2 Mac
pip install torch torchvision torchaudio
```

**確認:**
```python
import torch
print(torch.__version__)
print("MPS:", torch.backends.mps.is_available())
```

**✅ 出力:**
```
2.1.2
MPS: True
```

#### OpenAI API

⭐ **任意**（生成AI開発時）

```bash
# インストール
pip install openai python-dotenv
```

**.env作成:**
```bash
cat > .env << 'EOF'
OPENAI_API_KEY=your-api-key-here
EOF
```

**.gitignore追加:**
```bash
echo ".env" >> .gitignore
```

**コード例:**
```python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

#### LangChain

⭐ **任意**（LLMアプリ開発時）

```bash
pip install langchain langchain-openai
```

**コード例:**
```python
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model="gpt-4")
messages = [HumanMessage(content="こんにちは！")]
response = llm.invoke(messages)
print(response.content)
```

#### AI開発用requirements.txt例

```txt
# データサイエンス
numpy==1.26.2
pandas==2.1.4
matplotlib==3.8.2
scikit-learn==1.3.2

# Jupyter
jupyter==1.0.0

# ディープラーニング（選択）
tensorflow-macos==2.15.0
tensorflow-metal==1.1.0
# または
torch==2.1.2
torchvision==0.16.2
torchaudio==2.1.2

# 生成AI
openai==1.6.1
langchain==0.1.0
langchain-openai==0.0.2
python-dotenv==1.0.0
```

---

## PART 6: トラブルシューティング

### 15. エラー解決

#### エラー1: pyenvインストール失敗

**症状:**
```bash
brew install pyenv
# Error: ...
```

**解決策:**

**1. Homebrew更新:**
```bash
brew update
brew upgrade
brew install pyenv
```

**2. Xcode CLT再インストール:**
```bash
xcode-select --install
```

**3. 依存関係インストール:**
```bash
brew install openssl readline sqlite3 xz zlib
```

---

#### エラー2: Pythonインストール失敗

**症状:**
```bash
pyenv install 3.12.1
# BUILD FAILED
```

**解決策:**

**1. 依存関係インストール:**
```bash
brew install openssl readline sqlite3 xz zlib
```

**2. 環境変数設定してインストール:**
```bash
CFLAGS="-I$(brew --prefix openssl)/include" \
LDFLAGS="-L$(brew --prefix openssl)/lib" \
pyenv install 3.12.1
```

---

#### エラー3: python not found

**症状:**
```bash
python --version
# command not found
```

**解決策:**

**1. python3で試す:**
```bash
python3 --version
```

**2. pyenv確認:**
```bash
# パス確認
echo $PATH | grep pyenv

# なければ設定再実行
source ~/.zshrc
```

**3. rehash:**
```bash
pyenv rehash
python --version
```

---

#### エラー4: 仮想環境有効化失敗

**症状:**
```bash
source .venv/bin/activate
# No such file or directory
```

**解決策:**

**1. 場所確認:**
```bash
# 現在地
pwd

# .venvあるか?
ls -la | grep .venv
```

**2. 正しい場所に移動:**
```bash
cd /path/to/project
source .venv/bin/activate
```

**3. 再作成:**
```bash
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
```

---

#### エラー5: Permission denied

**症状:**
```bash
pip install django
# Permission denied
```

**原因:** グローバル環境にインストールしようとしている

**解決策:**

```bash
# 仮想環境作成
python -m venv .venv
source .venv/bin/activate

# 再度インストール
pip install django
```

**❌ 絶対NG:**
```bash
sudo pip install  # これは絶対ダメ！
```

---

#### エラー6: VSCode インタープリター表示されない

**解決策:**

**1. Python拡張機能再インストール:**
- 拡張機能 → Python → アンインストール
- VSCode再起動
- Python再インストール

**2. VSCode完全再起動:**
```
⌘ + Q で終了
再起動
```

**3. 手動パス指定:**
```
⌘ + Shift + P
→ Python: Select Interpreter
→ Enter interpreter path...
→ /Users/あなた/.pyenv/versions/3.12.1/bin/python
```

---

#### エラー7: M2 Mac パッケージインストール失敗

**症状:**
```bash
pip install パッケージ
# Building wheel ... error
```

**解決策: Rosetta 2使用**

```bash
# Rosetta 2インストール（初回のみ）
softwareupdate --install-rosetta

# x86_64版Python
arch -x86_64 pyenv install 3.11.7

# プロジェクトで使用
arch -x86_64 pyenv local 3.11.7
```

**💡 最終手段！ほとんどのパッケージはM2ネイティブで動作**

---

### 16. よくある質問

#### Q1: pyenv vs venv違いは？

**A:**

| 項目 | pyenv | venv |
|------|-------|------|
| **役割** | Pythonバージョン管理 | 環境分離 |
| **管理** | Python本体 | パッケージ |
| **必須度** | ✅必須 | ✅必須 |

**両方使う！**

---

#### Q2: .venv vs venv どっち？

**A:** ただの名前の違い

```bash
python -m venv .venv  # 推奨（隠しフォルダ）
python -m venv venv   # OK
python -m venv env    # OK
```

**推奨: `.venv`**（Python公式推奨）

---

#### Q3: グローバルにインストールOK？

**A:** ❌基本NG

**例外的にOK:**
- `pip`自体
- `jupyter`などの汎用ツール

**基本ルール:**
すべてのパッケージは仮想環境に！

---

#### Q4: global vs local違いは？

**A:**

```bash
# global: システムデフォルト
pyenv global 3.12.1
# どこでも3.12.1

# local: プロジェクト専用
cd project-a
pyenv local 3.11.7
# project-aだけ3.11.7
```

**優先順位:**
local > global

---

#### Q5: 複数バージョン同時使用OK？

**A:** ✅OK！それがpyenvの目的

```bash
# プロジェクトAは3.9
cd project-a
python --version  # 3.9.18

# プロジェクトBは3.12
cd project-b
python --version  # 3.12.1
```

---

#### Q6: 仮想環境削除方法は？

**A:**

```bash
# 無効化
deactivate

# フォルダ削除
rm -rf .venv

# 再作成
python -m venv .venv
```

**💡 ただのフォルダ！気軽に作り直せる**

---

#### Q7: pip freeze vs pip list違いは？

**A:**

```bash
# pip list: 確認用
pip list
# 表形式で見やすい

# pip freeze: ファイル出力用
pip freeze > requirements.txt
# requirements.txt形式
```

---

#### Q8: Python 2 vs 3違いは？

**A:**

```
Python 2: 2020年サポート終了
Python 3: 現在の標準

結論:
Python 3だけ覚えればOK
Python 2は無視
```

---

#### Q9: Anaconda使うべき？

**A:**

**Anaconda向き:**
- データサイエンス専門
- GUI管理好き

**pyenv + venv向き:**
- Web開発も
- シンプル好き
- 容量節約

**初心者推奨:**
pyenv + venvから始める

---

#### Q10: .venvをGitにcommit？

**A:** ❌絶対ダメ！

**.gitignore必須:**
```gitignore
.venv/
venv/
env/
```

**代わりに:**
requirements.txt をcommit

---

#### Q11: プロジェクト移動方法は？

**A:**

**元PC:**
```bash
pip freeze > requirements.txt
git add requirements.txt .python-version
git commit -m "Add requirements"
git push
```

**新PC:**
```bash
git clone URL
cd repo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

#### Q12: macOSプリインストールPythonは？

**A:** 無視！触らない！

```bash
which python3
# /usr/bin/python3 ← これはシステム用

which python
# ~/.pyenv/shims/python ← これを使う
```

---

#### Q13: TensorFlow vs PyTorch選択は？

**A:**

**TensorFlow:**
- Google製
- 本番環境向け

**PyTorch:**
- Meta製
- 研究向け
- 初心者に優しい

**初心者推奨: PyTorch**

---

#### Q14: uv使うべき？

**A:**

**段階的アプローチ:**
```
1. pyenv + venv マスター（今）
2. 3-6ヶ月Python経験
3. uvを試す
```

**初心者は:**
pyenv + venv で十分！

---

#### Q15: Windows開発者との共存は？

**A:**

**共通言語: venv**

```
Mac: pyenv + venv
Windows: 公式Python + venv

共通: requirements.txt
```

**README記載:**
```markdown
# Mac/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

---

#### Q16: 必須ファイルは？

**A:**

```
プロジェクト/
├── .python-version    # ⭐任意（便利）
├── requirements.txt   # ✅必須（チーム開発）
├── .gitignore        # ✅必須（Git使用時）
└── README.md         # 🔶推奨
```

---

#### Q17: コマンド間違えた場所で実行！

**A:**

**ケース別対処:**

```bash
# ❌ python -m venv .venv を ~/で実行
cd ~
rm -rf .venv

# ✅ 正しい場所で再実行
cd ~/Projects/my-project
python -m venv .venv
```

---

#### Q18: 同じコマンド2回実行したら？

**A:**

| コマンド | 影響 |
|---------|------|
| `brew install` | 🟢OK（既にあると表示） |
| `pyenv install` | 🟢OK（既にあると表示） |
| `python -m venv` | 🔴初期化される |
| `echo >>` | 🟡重複（動作はするが整理推奨） |
| `source activate` | 🟢OK |

**💡 echo >> の重複確認:**
```bash
grep -c "PYENV_ROOT" ~/.zshrc
# 2 = 正常（1セット）
# 4 = 重複（2セット）
```

---

#### Q19: エラーメッセージ英語で読めない

**A:**

**Google翻訳活用:**
```
エラーメッセージコピー
→ Google翻訳
→ 理解
→ 解決策検索
```

**主なエラーパターン:**
- `command not found`: コマンドがない
- `Permission denied`: 権限エラー
- `No such file`: ファイルがない
- `Already exists`: 既に存在

---

#### Q20: もっと学びたい

**A:**

**公式ドキュメント:**
- Python: https://docs.python.org/ja/3/
- Django: https://docs.djangoproject.com/ja/
- Flask: https://flask.palletsprojects.com/

**コミュニティ:**
- Stack Overflow
- Qiita
- Reddit r/Python

**コース:**
- Udemy
- Coursera
- freeCodeCamp

---

## 完成チェックリスト

### 基本環境

- [ ] Homebrew動作確認（`brew --version`）
- [ ] pyenv動作確認（`pyenv --version`）
- [ ] Python 3.12インストール済み
- [ ] Python 3.11インストール済み
- [ ] グローバルバージョン設定済み（`python --version`）

### VSCode

- [ ] Python拡張機能インストール済み
- [ ] インタープリター選択可能
- [ ] 仮想環境自動認識設定済み

### 実践

- [ ] 仮想環境作成できる
- [ ] 仮想環境有効化できる
- [ ] パッケージインストールできる
- [ ] requirements.txt作成できる
- [ ] Djangoプロジェクト作成できる

**全部✅ → 完璧！🎉**

---

## 次のステップ

### 初心者

1. **Python基礎学習**
   - 変数、関数、クラス
   - 公式チュートリアル

2. **フレームワーク学習**
   - Django/Flask
   - 公式チュートリアル

3. **プロジェクト作成**
   - ブログ
   - TODO アプリ
   - API

### 中級者

1. **Git完全習得**
   - ブランチ戦略
   - プルリクエスト

2. **テスト導入**
   - pytest
   - カバレッジ

3. **CI/CD**
   - GitHub Actions
   - デプロイ自動化

### 上級者

1. **モダンツール**
   - uv
   - Poetry
   - Docker

2. **AI/ML**
   - TensorFlow
   - PyTorch
   - LangChain

3. **OSS貢献**
   - GitHub探索
   - Issue解決
   - プルリクエスト

---

## 最後に

**🎉 おめでとうございます！**

プロのPythonエンジニアと同じ環境を手に入れました！

**この先:**
- 楽しく学ぶ
- たくさん作る
- エラーを恐れない
- コミュニティに参加

**Happy Coding! 🐍✨**

---

## ドキュメント情報

**バージョン:** 3.0  
**最終更新:** 2025年1月  
**対象:** Mac M2 + VSCode  
**前提:** Git・VSCode・Docker・GitHub SSH完了

**改訂内容:**
- 2025年最新情報
- より詳細な解説
- エラー解決強化
- AI開発セクション拡充
- 完全なる網羅性

**目標:**
このガイドだけで100%完了

**フィードバック歓迎！**

---

*このガイドがあなたのPython開発の旅を最高のスタートにしますように！*
