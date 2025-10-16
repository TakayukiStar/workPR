# Python 開発環境 完全構築ガイド 🐍

**【Mac M2 + VSCode + pyenv + venv - このガイドだけで絶対できる！】**

Git・VSCode・Docker・GitHub SSH 接続が完了した状態から、プロフェッショナルな Python 開発環境を構築します。実際の初心者の方が遭遇するエラーをすべて網羅しています。

**📌 このガイドの表記ルール:**
- ✅ **必須** - 必ず実行・作成する
- 🔶 **推奨** - 強く推奨（なくても動くが、あるべき）
- ⭐ **任意** - あると便利（プロジェクトによる）

---

## 📖 目次

**環境選択と基礎知識:**

1. [🤔 Python 環境の選択肢](#python-環境の選択肢)
2. [💻 Windows 開発者との共存性](#windows-開発者との共存性)
3. [✨ 推奨構成と理由](#推奨構成と理由)
4. [🎯 このガイドで構築する環境](#このガイドで構築する環境)

**基本設定（必須）:**

5. [ステップ 1: Homebrew のインストール](#ステップ-1-homebrew-のインストール-)
6. [ステップ 2: pyenv のインストール](#ステップ-2-pyenv-のインストール-)
7. [ステップ 3: Python のインストール](#ステップ-3-python-のインストール-)
8. [ステップ 4: pip と仮想環境の基礎](#ステップ-4-pip-と仮想環境の基礎-)
9. [ステップ 5: VSCode の Python 設定](#ステップ-5-vscode-の-python-設定-)

**実践編:**

10. [ステップ 6: プロジェクトでの実践](#ステップ-6-プロジェクトでの実践-)
11. [ステップ 7: お客様のプロジェクトで使う](#ステップ-7-お客様のプロジェクトで使う-)
12. [ステップ 8: requirements.txt の使い方](#ステップ-8-requirementstxt-の使い方-)

**AI/生成AI 開発向け:**

13. [ステップ 9: AI 開発の追加設定](#ステップ-9-ai-開発の追加設定-)

**困ったときは:**

14. [🔧 トラブルシューティング](#トラブルシューティング)
15. [📚 よくある質問](#よくある質問)
16. [🎓 実践シナリオ集](#実践シナリオ集)

---

## 🤔 Python 環境の選択肢

Python の環境構築には、いくつかの選択肢があります。まず、それぞれの特徴を理解しましょう。

### 選択肢 1: Mac にプリインストールされている Python

**特徴:**
- Mac には最初から Python が入っている
- コマンド: `python3`

**❌ なぜ使わない方が良い？**
- macOS システムが使う Python（勝手に触ると Mac が壊れる可能性）
- バージョンが古い（macOS のバージョンに依存）
- 自由にパッケージをインストールできない
- プロジェクトごとの管理ができない

**結論:** 絶対に使わない。これはシステム用！

---

### 選択肢 2: python.org から直接インストール

**特徴:**
- 公式サイトからダウンロードしてインストール
- Windows では一般的

**❌ Mac では推奨しない理由:**
- バージョンの切り替えができない
- 複数のプロジェクトで異なるバージョンが必要になると困る
- アンインストールが面倒
- PATH の設定が複雑になる

**結論:** Mac では使わない

---

### 選択肢 3: pyenv（Python のバージョン管理ツール）

**特徴:**
- 複数の Python バージョンをインストール・切り替えできる
- プロジェクトごとに異なるバージョンを指定可能
- Mac/Linux で標準的

**✅ メリット:**
- Python 3.9、3.10、3.11、3.12 など複数バージョンを共存
- お客様 A は Python 3.9、お客様 B は Python 3.11 が必要でも対応可能
- システムの Python に影響を与えない
- 簡単にインストール・切り替え

**❌ デメリット:**
- 初期設定が少し必要
- プロジェクトごとの依存関係の分離は別途必要
- Windows では pyenv-win（別プロジェクト）が必要

**結論:** Mac/Linux では必須！（Python のバージョン管理に最適）

---

### 選択肢 4: venv（仮想環境ツール）⭐最重要⭐

**特徴:**
- Python 標準搭載の仮想環境作成ツール
- プロジェクトごとに独立した環境を作成

**✅ メリット:**
- プロジェクト A と B で異なるパッケージバージョンを使える
- グローバル環境を汚さない
- Python に標準で入っている（追加インストール不要）
- 軽量・シンプル
- **完全クロスプラットフォーム（Mac/Linux/Windows で同じコマンド）**

**用途:**
- パッケージの依存関係を分離
- プロジェクトごとの環境構築

**結論:** これも使う！（プロジェクトごとの環境分離に必須）

**💡 重要:** pyenv と venv は役割が違うので、両方使います！
- **pyenv:** Python のバージョンを管理（3.9、3.10、3.11、3.12 など）
- **venv:** パッケージを管理（Django、requests など）

---

### 選択肢 5: uv（超高速パッケージマネージャー）⚡

**特徴:**
- Rust で書かれた超高速な Python パッケージ＆プロジェクト管理ツール
- pip + venv + pyenv の機能を統合
- 2023 年に登場した新しいツール（Astral 社が開発）
- **完全クロスプラットフォーム（Mac/Linux/Windows で同一コマンド）**

**✅ メリット:**
- **異次元の速さ**（pip より 10〜100 倍速い）
- Python のインストールからパッケージ管理まで一元化
- 依存関係の解決が優秀
- モダンな設計
- Windows/Mac/Linux で完全に同じ操作

**❌ デメリット:**
- 新しすぎる（歴史が浅い）
- 日本語ドキュメントが少ない
- トラブル時の情報が少ない
- 一部のパッケージで互換性問題がある可能性
- 学習コストがある
- チームメンバー全員が理解する必要がある

**結論:** 初心者は pyenv + venv から始めて、慣れたら uv を試すのが最適！

---

### 選択肢 6: conda/Anaconda

**特徴:**
- データサイエンス向けのパッケージマネージャー
- Python + 科学計算ライブラリを一括管理
- **完全クロスプラットフォーム**

**✅ メリット:**
- NumPy、Pandas などが簡単にインストールできる
- データサイエンス・機械学習向け
- Windows/Mac/Linux で同じ操作

**❌ デメリット:**
- 容量が大きい（数 GB）
- インストールに時間がかかる
- pyenv と競合することがある
- Web 開発には過剰

**結論:** AI 開発でも pyenv + venv の方がシンプル（必要なら後で追加可能）

---

### 選択肢 7: Poetry

**特徴:**
- Python のパッケージ・依存関係管理ツール
- モダンなプロジェクト管理
- **完全クロスプラットフォーム**

**✅ メリット:**
- 依存関係の解決が優秀
- pyproject.toml で一元管理
- 仮想環境も自動作成
- Windows/Mac/Linux で同じ操作

**❌ デメリット:**
- 学習コストが高い
- 初心者には複雑
- 慣れてから導入すべき

**結論:** まずは pyenv + venv を完璧に使えるようになってから検討

---

### 選択肢 8: Docker

**特徴:**
- コンテナで完全に環境を分離
- OS レベルでの仮想化
- **完全クロスプラットフォーム**

**✅ メリット:**
- 完全な環境の再現性
- チーム開発で有利
- Windows/Mac/Linux で同じ環境

**❌ 初心者には:**
- 学習コストが高い
- ローカル開発では過剰なことも

**結論:** pyenv + venv で開発、本番環境やチーム開発で Docker を使う

---

## 💻 Windows 開発者との共存性

### 重要な結論

**🎯 Windows 開発者とのチーム開発で最も共存性が高いのは：**

```
1位: venv（Python標準）⭐⭐⭐⭐⭐
2位: uv（新しいが完全統一）⭐⭐⭐⭐
3位: Poetry（クロスプラットフォーム）⭐⭐⭐
4位: Anaconda（データサイエンス向け）⭐⭐⭐
5位: pyenv + venv（OS別設定が必要）⭐⭐
```

### 詳細比較

#### 1位: venv（最強の共存性）✅

**なぜ venv が最強？**

- ✅ Python に標準搭載（Python 3.3 以降）
- ✅ 追加インストール不要
- ✅ Windows/Mac/Linux で**完全に同じコマンド**
- ✅ どんな環境でも確実に動作

**チーム開発での使い方:**

```bash
# Mac/Linux
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate

# パッケージインストール（全OS共通）
pip install -r requirements.txt
```

**💡 ポイント:**
- `requirements.txt` を共有すれば、どの OS でも同じ環境が再現できる
- venv の有効化コマンドだけが OS で異なる
- プロジェクトのドキュメントに両方のコマンドを書いておけば OK

---

#### pyenv の Windows 対応

**問題点:**
- pyenv は Mac/Linux 専用
- Windows には **pyenv-win**（別プロジェクト）がある
- 設定方法が微妙に異なる

**結論:** Windows 開発者とチームを組む場合は、venv が共通言語！

---

### チーム開発での推奨構成

#### 推奨: 標準的なアプローチ

```
Mac開発者: pyenv + venv
Windows開発者: Python公式インストーラー + venv
Linux開発者: pyenv + venv

共通: venv + requirements.txt
```

**理由:**
- venv は全 OS で完全互換
- `requirements.txt` で依存関係を共有
- Python のバージョンは `.python-version` で指定

**プロジェクトに含めるファイル:**

```
project/
  ├── .python-version      # ⭐任意（pyenvを使う場合）
  ├── requirements.txt     # ✅必須（チーム開発では必須）
  ├── .gitignore          # ✅必須（Gitを使う場合は必須）
  └── README.md           # 🔶推奨（セットアップ手順）
```

---

## ✨ 推奨構成と理由

### 🎯 このガイドで構築する環境

```
✅ 必須: pyenv（Pythonバージョン管理）
  └── Python 3.12.x（最新安定版）
  └── Python 3.11.x（互換性重視版）
  └── 必要に応じて他のバージョンも

✅ 必須: プロジェクトごとにvenv（仮想環境）
  └── 独立したパッケージ群
```

### なぜ pyenv + venv？

**1. 柔軟性 🔄**
- お客様 A: Python 3.9 が必要 → pyenv で 3.9 をインストール
- お客様 B: Python 3.12 が必要 → pyenv で 3.12 をインストール
- 簡単に切り替え可能

**2. 分離性 🛡️**
- プロジェクト A: Django 4.2 を使用
- プロジェクト B: Django 5.0 を使用
- venv で完全に分離、干渉しない

**3. 標準的 📚**
- Python コミュニティで広く使われている
- ドキュメントが豊富
- 転職しても同じ方法が使える

**4. シンプル ⚡**
- 最小限のツール
- 理解しやすい
- トラブルが少ない

**5. AI 開発にも最適 🤖**
- TensorFlow、PyTorch などのバージョン指定が簡単
- CUDA バージョンに合わせた Python バージョンも選べる
- プロジェクトごとに異なる ML ライブラリバージョンを管理

**6. 初心者フレンドリー 👶**
- 段階的に学べる（まず pyenv、次に venv）
- 概念がシンプル
- トラブル時の情報が豊富

**7. Windows チームメンバーとの共存 🤝**
- venv は完全クロスプラットフォーム
- requirements.txt で簡単に環境を共有

---

## 🎯 このガイドで構築する環境

### 完成イメージ

```bash
# システム全体
/Users/あなた/
  ├── .pyenv/              # pyenvのホームディレクトリ
  │   └── versions/        # インストールしたPythonバージョン
  │       ├── 3.11.x/
  │       └── 3.12.x/
  │
  └── Projects/            # プロジェクトフォルダ
      ├── お客様A/
      │   └── project-a/
      │       └── .venv/   # プロジェクトAの仮想環境
      │
      └── お客様B/
          └── project-b/
              └── .venv/   # プロジェクトBの仮想環境
```

### 日常の使い方イメージ

```bash
# プロジェクトAで作業
cd ~/Projects/お客様A/project-a
source .venv/bin/activate      # 仮想環境を有効化
python --version               # Python 3.9.x（プロジェクトA用）
pip install django==4.2        # プロジェクトAにDjangoインストール

# プロジェクトBに切り替え
cd ~/Projects/お客様B/project-b
source .venv/bin/activate      # プロジェクトBの仮想環境を有効化
python --version               # Python 3.12.x（プロジェクトB用）
pip install django==5.0        # プロジェクトBにDjangoインストール
```

**🎉 それぞれのプロジェクトが完全に独立！お互いに影響しません！**

---

では、実際に構築していきましょう！

---

## ステップ 1: Homebrew のインストール 🍺

**✅ 必須ステップ**

### 1-1. Homebrew とは？

**Homebrew:**
- Mac 用のパッケージマネージャー
- Linux の apt-get や yum に相当
- ソフトウェアを簡単にインストール・管理できる

**💡 例えるなら:**
- App Store の CLI（コマンドライン）版
- `brew install 〇〇` で色々なツールをインストール

### 1-2. Homebrew が既にあるか確認

✅ **必須: 以下を実行**

ターミナルで以下を実行:

```bash
brew --version
```

**✅ バージョンが表示された場合:**

```
Homebrew 4.2.0
```

**→ 既にインストール済み！ステップ 1-4 へ進んでください**

**❌ 「command not found」と出た場合:**

```
-bash: brew: command not found
```

**→ インストールが必要です。ステップ 1-3 へ**

### 1-3. Homebrew をインストール

✅ **必須: 以下のコマンドを実行**

以下のコマンドを**そのまま**コピー＆ペーストして実行:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**💡 このコマンドの意味:**
- Homebrew の公式インストールスクリプトをダウンロードして実行
- 安全です（Homebrew 公式の方法）

**実行すると:**

1. **パスワードを求められる:**
   ```
   Password:
   ```
   **→ Mac のログインパスワードを入力**（画面には表示されません。見えなくても入力されています）

2. **Enter を押すように言われる:**
   ```
   Press RETURN to continue or any other key to abort:
   ```
   **→ Enter キーを押す**

3. **インストールが始まる**
   - 数分かかります（コーヒーでも飲みながら待ちましょう☕）

4. **完了メッセージ:**
   ```
   ==> Installation successful!
   ```

5. ✅ **重要！必須の追加設定:**
   ```
   ==> Next steps:
   - Run these two commands in your terminal to add Homebrew to your PATH:
     echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
     eval "$(/opt/homebrew/bin/brew shellenv)"
   ```

   **💡 M2 Mac の場合、この追加設定が必要です！**

   **表示されたコマンドを順番に実行:**

   ```bash
   echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
   eval "$(/opt/homebrew/bin/brew shellenv)"
   ```

**💡 どちらのシェルを使っているか確認:**

```bash
echo $SHELL
```

- `/bin/zsh` と表示 → `~/.zshrc` に追加（上記コマンド）
- `/bin/bash` と表示 → `~/.bash_profile` に追加

**M2 Mac では通常 zsh なので、`~/.zshrc` のパターンが多いです**

### 1-4. インストール確認

✅ **必須: 確認する**

ターミナルを**一度閉じて、再度開く**（重要！）

その後、以下を実行:

```bash
brew --version
```

**✅ 成功:**

```
Homebrew 4.2.0
（または他のバージョン）
```

**❌ まだ「command not found」の場合:**

1. ターミナルを完全に終了（`⌘ + Q`）
2. ターミナルを再起動
3. もう一度確認

それでもダメな場合は、ステップ 1-3 の「追加の設定」を再実行してください。

### 1-5. Homebrew を最新に更新

✅ **必須: 最新に更新**

```bash
brew update
```

**✅ 成功メッセージ:**

```
Already up-to-date.
```

または

```
Updated 1 tap (homebrew/core).
```

**🎉 Homebrew のインストール完了！**

---

## ステップ 2: pyenv のインストール 🔧

**✅ 必須ステップ**

### 2-1. pyenv とは？（復習）

**pyenv:**
- Python のバージョン管理ツール
- 複数の Python バージョンを簡単にインストール・切り替え
- Ruby の rbenv、Node.js の nvm に相当

**できること:**
- Python 3.9、3.10、3.11、3.12 などを全部インストール
- プロジェクトごとに使用バージョンを指定
- グローバルのデフォルトバージョンを設定

### 2-2. pyenv をインストール

✅ **必須: 以下を実行**

```bash
brew install pyenv
```

**📖 コマンドの詳細解説:**

```bash
brew install pyenv
└─┬─┘ └──┬──┘ └─┬─┘
  │      │       └─ インストールするパッケージの名前
  │      └─ Homebrewのインストールコマンド
  └─ Homebrewを実行
```

**実行すると:**
- ダウンロードとインストールが始まる
- 数分かかります

**✅ 成功メッセージ:**

```
==> Downloading https://...
==> Pouring pyenv--2.3.x.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pyenv/2.3.x: xxx files, xx.xMB
==> Running `brew cleanup pyenv`...
```

### 2-3. pyenv の PATH 設定（超重要！）

✅ **必須: PATH設定をしないとpyenvが動きません！**

**💡 この設定をしないと pyenv が動きません！**

以下のコマンドを実行:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

**📖 各コマンドの詳細解説:**

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
└┬─┘ └──────────┬──────────────────┘    └───┬────┘
 │               │                           └─ ファイルの末尾に追記
 │               └─ 追記する内容（pyenvのホームディレクトリを設定）
 └─ 画面に表示せずファイルに書き込む
```

**各行の意味:**
1. `export PYENV_ROOT="$HOME/.pyenv"` - pyenv のホームディレクトリを設定
2. `export PATH="$PYENV_ROOT/bin:$PATH"` - pyenv のコマンドを使えるようにする
3. `eval "$(pyenv init --path)"` - pyenv のパス初期化
4. `eval "$(pyenv init -)"` - pyenv の初期化

**💡 bash を使っている場合:**

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

**どちらを使うか確認:**

```bash
echo $SHELL
```

- `/bin/zsh` → 最初のコマンド（`.zshrc`）
- `/bin/bash` → 2 番目のコマンド（`.bash_profile`）

### 2-4. 設定を反映

✅ **必須: 設定を反映**

ターミナルを再起動するか、以下を実行:

```bash
source ~/.zshrc
```

**📖 コマンドの詳細解説:**

```bash
source ~/.zshrc
└──┬─┘ └───┬───┘
   │       └─ 読み込むファイル（シェルの設定ファイル）
   └─ ファイルを現在のシェルで実行する
```

または

```bash
source ~/.bash_profile
```

### 2-5. インストール確認

✅ **必須: 確認する**

```bash
pyenv --version
```

**✅ 成功:**

```
pyenv 2.3.36
（またはインストールされたバージョン）
```

**❌ 「command not found」の場合:**

1. ステップ 2-3 を再実行
2. ターミナルを完全に再起動（`⌘ + Q` で終了後、再起動）
3. もう一度確認

### 2-6. pyenv で利用可能な Python バージョンを確認

⭐ **任意: 確認したい場合**

```bash
pyenv install --list
```

**表示例:**

```
Available versions:
  2.7.18
  3.8.18
  3.9.18
  3.10.13
  3.11.7
  3.12.1
  3.13.0
  ...
```

**💡 この一覧から好きなバージョンをインストールできます！**

---

## ステップ 3: Python のインストール 🐍

**✅ 必須ステップ（最低1つのバージョン）**
**🔶 推奨: 2つのバージョンをインストール**

### 3-1. どのバージョンをインストールすべき？

**🔶 推奨: 2 つのバージョンをインストール**

1. **Python 3.12.x（最新安定版）** - 新規プロジェクト用
2. **Python 3.11.x（互換性重視版）** - 既存プロジェクト用

**💡 なぜ 2 つ？**

- **Python 3.12.x:**
  - 最新機能が使える
  - パフォーマンスが良い
  - 新規プロジェクトに最適

- **Python 3.11.x:**
  - 多くのライブラリが対応済み
  - 互換性が高い
  - お客様の既存プロジェクトで指定されることが多い

**💡 実際の現場では:**
- お客様のプロジェクトで「Python 3.9 を使ってください」と言われることもあります
- その場合は `pyenv install 3.9.18` で追加すれば OK！

### 3-2. 最新の安定バージョン番号を確認

⭐ **任意: 最新版を確認したい場合**

```bash
pyenv install --list | grep "^\s*3\.[0-9]*\.[0-9]*$"
```

**📖 コマンドの詳細解説:**

```bash
pyenv install --list | grep "^\s*3\.[0-9]*\.[0-9]*$"
└──────┬────────┘   └─────────┬──────────────────┘
       │                      └─ パターンマッチで3.x.xのバージョンだけ抽出
       └─ インストール可能なバージョン一覧を表示
```

**表示例:**

```
  3.9.18
  3.10.13
  3.11.7
  3.12.1
```

**💡 各メジャーバージョンの最後の番号が最新の安定版です**

例えば:
- 3.11 系の最新: `3.11.7`
- 3.12 系の最新: `3.12.1`

### 3-3. Python 3.12.x をインストール

✅ **必須: 以下を実行（バージョン番号は最新のものに変更）**

**最新の 3.12 系をインストール（例: 3.12.1）:**

```bash
pyenv install 3.12.1
```

**📖 コマンドの詳細解説:**

```bash
pyenv install 3.12.1
└─┬─┘ └──┬──┘ └──┬──┘
  │      │       └─ インストールするPythonのバージョン番号
  │      └─ インストールコマンド
  └─ pyenvを実行
```

**💡 最新バージョン番号は上記で確認した番号を使ってください**

**実行すると:**

```
Downloading Python-3.12.1.tar.xz...
Installing Python-3.12.1...
Installed Python-3.12.1 to /Users/あなた/.pyenv/versions/3.12.1
```

**⏰ 5-10 分かかります。気長に待ちましょう！**

**✅ 成功メッセージ:**

```
Installed Python-3.12.1 to /Users/あなた/.pyenv/versions/3.12.1
```

### 3-4. Python 3.11.x をインストール

🔶 **推奨: 互換性のために追加インストール**

**最新の 3.11 系をインストール（例: 3.11.7）:**

```bash
pyenv install 3.11.7
```

**同じように 5-10 分待ちます**

**✅ 成功メッセージ:**

```
Installed Python-3.11.7 to /Users/あなた/.pyenv/versions/3.11.7
```

### 3-5. インストールされたバージョンを確認

⭐ **任意: 確認したい場合**

```bash
pyenv versions
```

**📖 コマンドの詳細解説:**

```bash
pyenv versions
└─┬─┘ └───┬───┘
  │       └─ インストール済みバージョンを表示
  └─ pyenvを実行
```

**✅ 表示例:**

```
* system (set by /Users/あなた/.pyenv/version)
  3.11.7
  3.12.1
```

**💡 `*` がついているのが現在使用中のバージョン**
- `system` = Mac にプリインストールされている Python（使わない）

### 3-6. グローバルのデフォルトバージョンを設定

✅ **必須: デフォルトバージョンを設定**

**💡 重要な概念:**

- **グローバル:** システム全体で使うデフォルトの Python
- **ローカル:** 特定のプロジェクトで使う Python（後で設定）

**グローバルに 3.12.1 を設定:**

```bash
pyenv global 3.12.1
```

**📖 コマンドの詳細解説:**

```bash
pyenv global 3.12.1
└─┬─┘ └──┬─┘ └──┬──┘
  │      │      └─ 設定するPythonバージョン
  │      └─ グローバル設定コマンド
  └─ pyenvを実行
```

**何も表示されなければ OK**

### 3-7. 設定確認

✅ **必須: 確認する**

```bash
python --version
```

**✅ 正しい表示:**

```
Python 3.12.1
```

**❌ もし古いバージョンが表示されたら:**

```bash
# シェル設定を再読み込み
source ~/.zshrc

# もう一度確認
python --version
```

それでもダメな場合:

```bash
# pyenvのshim（シム）を再生成
pyenv rehash

# 確認
python --version
```

### 3-8. pip のバージョン確認

⭐ **任意: 確認したい場合**

```bash
pip --version
```

**✅ 表示例:**

```
pip 23.3.1 from /Users/あなた/.pyenv/versions/3.12.1/lib/python3.12/site-packages/pip (python 3.12)
```

**💡 ポイント:**
- pip は Python に標準で付属
- pyenv でインストールした Python のパスが表示される

### 3-9. pip を最新に更新

✅ **必須: pipを最新に**

```bash
pip install --upgrade pip
```

**📖 コマンドの詳細解説:**

```bash
pip install --upgrade pip
└┬┘ └──┬──┘ └───┬───┘ └┬┘
 │     │        │       └─ パッケージ名（pip自体）
 │     │        └─ アップグレードオプション
 │     └─ インストールコマンド
 └─ pipを実行
```

**✅ 成功メッセージ:**

```
Successfully installed pip-24.0
```

**🎉 Python のインストール完了！**

---

## ステップ 4: pip と仮想環境の基礎 📦

**✅ 必須: 仮想環境の概念を理解する**

### 4-1. pip とは？

**pip:**
- Python のパッケージマネージャー
- Python のライブラリ（パッケージ）をインストールするツール
- npm（Node.js）、gem（Ruby）に相当

**できること:**
- `pip install django` → Django をインストール
- `pip install requests` → Requests ライブラリをインストール
- `pip list` → インストール済みパッケージ一覧
- `pip uninstall パッケージ名` → パッケージをアンインストール

### 4-2. グローバル環境とローカル環境

**重要な概念:**

```
グローバル環境（使わない！）
  └── システム全体で共有
  └── プロジェクト間で干渉する
  └── バージョン競合が発生

ローカル環境 = 仮想環境（venv）（使う！）
  └── プロジェクトごとに独立
  └── 完全に分離
  └── 自由にパッケージをインストール
```

**❌ グローバルにインストールする問題:**

```bash
# グローバルにDjango 4.2をインストール
pip install django==4.2

# 別のプロジェクトでDjango 5.0が必要
pip install django==5.0  # ← 4.2が上書きされる！

# 最初のプロジェクトが動かなくなる！
```

**✅ 仮想環境を使う利点:**

```bash
# プロジェクトA
cd project-a
source .venv/bin/activate
pip install django==4.2  # ← プロジェクトAだけに影響

# プロジェクトB
cd project-b
source .venv/bin/activate
pip install django==5.0  # ← プロジェクトBだけに影響

# お互いに干渉しない！
```

### 4-3. venv とは？

**venv:**
- Python 標準の仮想環境作成ツール
- プロジェクトごとに独立した Python 環境を作成
- Python 3.3 以降に標準搭載（追加インストール不要）

**仕組み:**

```
project-a/
  └── .venv/           # プロジェクトAの仮想環境
      ├── bin/         # 実行ファイル
      ├── lib/         # インストールしたパッケージ
      └── ...

project-b/
  └── .venv/           # プロジェクトBの仮想環境（完全に独立）
      ├── bin/
      ├── lib/
      └── ...
```

### 4-4. 仮想環境の基本コマンド（まとめ）

#### 作成

✅ **必須: プロジェクトごとに1回実行**

```bash
python -m venv .venv
```

**📖 コマンドの超詳細解説:**

```bash
python -m venv .venv
└──┬─┘ └┬┘└┬┘ └─┬─┘
   │    │  │    └─ [4] 作成する仮想環境のフォルダ名
   │    │  └─ [3] 実行するモジュール名（Python標準の仮想環境モジュール）
   │    └─ [2] モジュールとして実行するオプション
   └─ [1] Pythonインタープリターを実行
```

**各部分の詳細説明:**

**[1] `python`**
- 意味: Python インタープリター（Python本体）を実行
- なぜ必要: venv はPythonの機能なので、Pythonで実行する

**[2] `-m`**
- 意味: "module"の略。Pythonモジュールを実行するオプション
- なぜ必要: venvはPython標準モジュールなので、-mで実行する

**[3] `venv`**
- 意味: 実行するモジュールの名前
- これは何: Python標準搭載の仮想環境作成モジュール
- ドット(`.`)なし: これはモジュール名だから

**[4] `.venv`**
- 意味: 作成する仮想環境フォルダの名前
- ドット(`.`)あり: これはフォルダ名だから（隠しフォルダにするため）
- 名前は自由: `venv`, `env`, `.env` など何でもOK
- 推奨: `.venv`（Python公式ドキュメントでも推奨）

**💡 なぜ2つのvenvがあるのか？**
- 1つ目の`venv`: モジュール名（ツールの名前）
- 2つ目の`.venv`: フォルダ名（作成するフォルダの名前）

**例: 他の名前でも作成可能**
```bash
python -m venv myenv       # myenvという名前で作成
python -m venv .env        # .envという名前で作成
python -m venv virtualenv  # virtualenvという名前で作成
```

---

#### 有効化

✅ **必須: 作業前に毎回実行**

```bash
# Mac/Linux
source .venv/bin/activate
```

**📖 コマンドの超詳細解説:**

```bash
source .venv/bin/activate
└──┬─┘ └─┬─┘└┬┘└───┬──┘
   │     │   │     └─ [4] 実行するスクリプトファイル名
   │     │   └─ [3] binフォルダ（実行ファイルが入っている）
   │     └─ [2] 仮想環境フォルダ名
   └─ [1] シェルコマンド（スクリプトを現在のシェルで実行）
```

**各部分の詳細説明:**

**[1] `source`**
- 意味: シェルのビルトインコマンド
- 何をする: ファイルを現在のシェルで実行する
- なぜ必要: 環境変数を現在のシェルに反映させるため
- 別名: `. `（ドットだけ）でも同じ意味

**[2] `.venv`**
- 意味: 仮想環境フォルダの名前
- ドット(`.`)の意味: 隠しフォルダを表す（Unixの慣習）
- なぜこの名前: ステップ4-4の作成で指定した名前

**[3] `/bin`**
- 意味: "binary"の略。実行ファイルが入っているフォルダ
- なぜ必要: activateスクリプトはbinフォルダの中にある

**[4] `activate`**
- 意味: 仮想環境を有効化するスクリプトファイル
- 拡張子なし: Linuxでは実行可能ファイルに拡張子は不要
- 実体: シェルスクリプト（環境変数を設定するコード）

**💡 パス全体の意味:**
`.venv/bin/activate` = 「.venvフォルダの中のbinフォルダの中のactivateファイル」

**Windows の場合:**
```bash
# Windows
.venv\Scripts\activate
└─┬─┘└───┬──┘└───┬──┘
  │      │       └─ 実行するスクリプト
  │      └─ Windowsでは"Scripts"フォルダ（binの代わり）
  └─ 仮想環境フォルダ
```

**💡 なぜ Windows と Mac/Linux で違う？**
- Unix系（Mac/Linux）: 実行ファイルは`bin/`に入れる慣習
- Windows: 実行ファイルは`Scripts/`に入れる慣習

---

#### 無効化

⭐ **任意: 作業終了時（しなくても問題なし）**

```bash
deactivate
```

**📖 コマンドの詳細解説:**

```bash
deactivate
└────┬───┘
     └─ 仮想環境を無効化する（activateで設定された環境変数を元に戻す）
```

---

#### 削除

⭐ **任意: やり直したい時**

```bash
# ただのフォルダなので、削除すればOK
rm -rf .venv
```

**📖 コマンドの詳細解説:**

```bash
rm -rf .venv
└┬┘└┬┘ └─┬─┘
 │  │    └─ 削除するフォルダ名
 │  └─ オプション（r=再帰的に、f=強制的に）
 └─ removeコマンド（削除）
```

**💡 覚えておくこと:**
1. ✅ **必須:** プロジェクトごとに仮想環境を作る
2. ✅ **必須:** 作業前に必ず有効化（activate）
3. ⭐ **任意:** 作業後は無効化（deactivate）してもしなくても OK

### 4-5. 実際に試してみる（練習）

⭐ **任意: 練習したい場合**

**練習用フォルダを作成:**

```bash
mkdir -p ~/python-practice
cd ~/python-practice
```

**仮想環境を作成:**

```bash
python -m venv .venv
```

**💡 何が起きた？**
- `.venv` フォルダが作成された
- この中に独立した Python 環境が入っている

**確認:**

```bash
ls -la
```

**表示:**

```
total 0
drwxr-xr-x   3 user  staff   96 Jan 15 10:00 .
drwxr-xr-x  45 user  staff 1440 Jan 15 10:00 ..
drwxr-xr-x   6 user  staff  192 Jan 15 10:00 .venv
```

**仮想環境を有効化:**

```bash
source .venv/bin/activate
```

**✅ 成功すると、プロンプトが変わる:**

```bash
(.venv) user@MacBook python-practice %
```

**💡 `(.venv)` が表示されていれば、仮想環境が有効です！**

**Python のバージョン確認:**

```bash
python --version
```

**pip のバージョン確認:**

```bash
pip --version
```

**インストール済みパッケージ確認:**

```bash
pip list
```

**表示:**

```
Package    Version
---------- -------
pip        23.3.1
setuptools 65.5.0
```

**💡 まっさらな状態！pip と setuptools しか入っていません**

**試しにパッケージをインストール:**

```bash
pip install requests
```

**確認:**

```bash
pip list
```

**表示:**

```
Package    Version
---------- ---------
certifi    2023.11.17
charset-normalizer 3.3.2
idna       3.6
pip        23.3.1
requests   2.31.0
setuptools 65.5.0
urllib3    2.1.0
```

**💡 requests とその依存パッケージがインストールされました！**

**仮想環境を無効化:**

```bash
deactivate
```

**✅ プロンプトが元に戻る:**

```bash
user@MacBook python-practice %
```

**もう一度 pip list を実行:**

```bash
pip list
```

**💡 グローバル環境のパッケージ一覧が表示される（requests は入っていない）**

**これが仮想環境の威力！完全に分離されています！**

**練習用フォルダを削除:**

```bash
cd ~
rm -rf ~/python-practice
```

**🎉 仮想環境の基礎を理解できました！**

---

## ステップ 5: VSCode の Python 設定 🎨

**🔶 推奨ステップ（VSCodeを使う場合は必須）**

### 5-1. VSCode の Python 拡張機能をインストール

✅ **必須: VSCodeでPython開発する場合**

1. VSCode を開く
2. 左サイドバーの「拡張機能」アイコン（四角が 4 つ）をクリック
3. 検索欄に `Python` と入力
4. **「Python」（Microsoft 製）** を選択
5. 「インストール」ボタンをクリック

**💡 正しい拡張機能:**
- 名前: Python
- 発行元: Microsoft
- アイコン: 青と黄色の Python ロゴ

**一緒にインストールされるもの:**
- Pylance（Python の言語サーバー）
- Python Debugger

### 5-2. VSCode でインタープリターを選択する方法

✅ **必須: プロジェクトごとに1回**

**インタープリター = 使用する Python のバージョン**

**方法 1: コマンドパレットから（推奨）**

1. `⌘ + Shift + P` を押す
2. `Python: Select Interpreter` と入力
3. リストから選択:
   - `Python 3.12.1 ('~/.pyenv/versions/3.12.1/bin/python')`
   - または
   - `Python 3.11.7 ('~/.pyenv/versions/3.11.7/bin/python')`

**方法 2: ステータスバーから**

1. VSCode の右下にある Python バージョン表示をクリック
2. リストから選択

### 5-3. 仮想環境を VSCode で認識させる

✅ **必須: プロジェクトで仮想環境を使う場合**

**自動認識:**
- VSCode は `.venv` フォルダを自動で検出
- プロジェクトフォルダを開くと、自動で仮想環境を認識

**手動選択:**

1. プロジェクトフォルダを開く
2. `⌘ + Shift + P` → `Python: Select Interpreter`
3. `.venv` の Python を選択
   - `Python 3.12.1 ('.venv': venv)`

**💡 仮想環境が選択されていることを確認:**
- 右下のステータスバーに `('.venv': venv)` と表示される

### 5-4. VSCode の統合ターミナルで自動的に仮想環境を有効化

🔶 **推奨: 自動化すると便利**

**設定方法:**

1. `⌘ + ,` で設定を開く
2. 検索欄に `terminal.integrated.env` と入力
3. または、`settings.json` に直接追加:

`⌘ + Shift + P` → `Preferences: Open User Settings (JSON)`

以下を追加:

```json
{
  "python.terminal.activateEnvironment": true
}
```

**これで、VSCode でターミナルを開くと自動的に仮想環境が有効化されます！**

### 5-5. おすすめの VSCode 設定

🔶 **推奨: より快適な開発のために**

`settings.json` に以下を追加:

```json
{
  "python.terminal.activateEnvironment": true,
  "python.defaultInterpreterPath": "python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": false,
  "python.formatting.provider": "none",
  "editor.formatOnSave": false,
  "python.analysis.typeCheckingMode": "basic",
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true
  }
}
```

**💡 この設定の意味:**
- 仮想環境を自動有効化
- `__pycache__` を非表示
- 基本的な型チェックを有効化

### 5-6. VSCode で Python ファイルを実行する方法

⭐ **任意: 好きな方法で**

**方法 1: 右上の実行ボタン（▶️）をクリック**

**方法 2: 右クリック → 「ターミナルで Python ファイルを実行」**

**方法 3: ターミナルで実行**

```bash
python ファイル名.py
```

**💡 仮想環境が有効化されている状態で実行されます**

---

## ステップ 6: プロジェクトでの実践 🚀

**✅ 必須: 実際にプロジェクトを作ってみる**

### 6-1. 新規プロジェクトの作成手順（完全版）

**シナリオ: Django で Web アプリを作る**

**ステップ 1: プロジェクトフォルダを作成**

✅ **必須**

```bash
mkdir -p ~/Projects/my-django-app
cd ~/Projects/my-django-app
```

**ステップ 2: 使用する Python バージョンを指定（ローカル設定）**

🔶 **推奨: pyenvを使う場合**

```bash
pyenv local 3.12.1
```

**📖 コマンドの詳細解説:**

```bash
pyenv local 3.12.1
└─┬─┘ └─┬─┘ └──┬──┘
  │     │      └─ 設定するPythonバージョン
  │     └─ このフォルダ専用の設定
  └─ pyenvを実行
```

**💡 何が起きた？**
- `.python-version` ファイルが作成される
- このフォルダでは常に Python 3.12.1 が使われる

**確認:**

```bash
cat .python-version
```

**表示:**

```
3.12.1
```

**ステップ 3: 仮想環境を作成**

✅ **必須**

```bash
python -m venv .venv
```

**ステップ 4: 仮想環境を有効化**

✅ **必須**

```bash
source .venv/bin/activate
```

**✅ プロンプトが変わる:**

```bash
(.venv) user@MacBook my-django-app %
```

**ステップ 5: pip を最新に更新**

✅ **必須**

```bash
pip install --upgrade pip
```

**ステップ 6: Django をインストール**

✅ **必須（このプロジェクトの場合）**

```bash
pip install django
```

**ステップ 7: Django プロジェクトを作成**

✅ **必須**

```bash
django-admin startproject config .
```

**📖 コマンドの詳細解説:**

```bash
django-admin startproject config .
└────┬────┘ └────┬───┘ └─┬─┘ └┬┘
     │           │       │    └─ [4] 作成場所（現在のフォルダ）
     │           │       └─ [3] プロジェクト名
     │           └─ [2] 新規プロジェクト作成コマンド
     └─ [1] Djangoの管理コマンド
```

**各部分の詳細:**

**[1] `django-admin`**
- Djangoの管理ツール
- Djangoをインストールすると使えるようになる

**[2] `startproject`**
- 新規プロジェクトを作成するコマンド

**[3] `config`**
- プロジェクト名（任意の名前でOK）
- 設定ファイルが入るフォルダ名になる

**[4] `.`**
- ドット = 現在のフォルダ
- **超重要:** これがないと余計なフォルダができる！

**💡 `.` がないとどうなる？**

```bash
# ドットなし
django-admin startproject config
# → config/config/ という二重フォルダができる（非推奨）

# ドットあり
django-admin startproject config .
# → config/ だけ（推奨）
```

**ステップ 8: 動作確認**

⭐ **任意: 動くか確認したい場合**

```bash
python manage.py runserver
```

**✅ 成功メッセージ:**

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

**ブラウザで http://127.0.0.1:8000/ を開く**

**Django の初期画面が表示されれば成功！🎉**

**サーバーを停止:**

```bash
Ctrl + C
```

**ステップ 9: VSCode で開く**

🔶 **推奨**

```bash
code .
```

**ステップ 10: VSCode でインタープリターを選択**

✅ **必須: VSCodeを使う場合**

1. `⌘ + Shift + P`
2. `Python: Select Interpreter`
3. `.venv` の Python を選択

**🎉 完璧なプロジェクト環境が完成しました！**

---

### 6-2. 既存プロジェクトをクローンして環境構築

**シナリオ: GitHub からクローンしたプロジェクトを動かす**

**ステップ 1: リポジトリをクローン**

✅ **必須**

```bash
cd ~/Projects
git clone git@github.com:user/existing-project.git
cd existing-project
```

**ステップ 2: README を確認**

✅ **必須**

```bash
cat README.md
```

**💡 Python のバージョン要件を確認:**
- "Python 3.11 以降が必要" などの記
