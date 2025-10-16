# Python 開発環境 完全構築ガイド 🐍

**【Mac M2 + VSCode + pyenv + venv - このガイドだけで絶対できる！】**

Git・VSCode・Docker・GitHub SSH 接続が完了した状態から、プロフェッショナルな Python 開発環境を構築します。実際の初心者の方が遭遇するエラーをすべて網羅しています。

**📌 このガイドの表記ルール:**
- ✅ **必須** - 必ず実行・作成する
- 🔶 **推奨** - 強く推奨（なくても動くが、あるべき）
- ⭐ **任意** - あると便利（プロジェクトによる）

**📍 実行場所の表記:**
- 🌍 **どこでもOK** - 任意のフォルダで実行可能
- 📁 **プロジェクト内** - プロジェクトフォルダ内で実行必須
- 🏠 **ホーム推奨** - ホームディレクトリ推奨（`~/`）

**🔄 再実行について:**
- 🟢 **再実行OK** - 何度実行しても問題なし
- 🟡 **注意** - 再実行すると設定が上書きされる
- 🔴 **再実行NG** - 一度だけ実行（再実行するとエラーまたは無駄）

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

## 📍 コマンド実行場所 早見表

**よくある質問: 「このコマンドはどこで実行するの？」**

以下の表で一目でわかります！

| コマンド | 実行場所 | 理由 |
|---------|---------|------|
| `brew --version` | 🌍 どこでもOK | システム全体のツール |
| `brew install pyenv` | 🌍 どこでもOK | システム全体のツール |
| `pyenv --version` | 🌍 どこでもOK | システム全体のツール |
| `pyenv install 3.12.1` | 🌍 どこでもOK | システム全体にインストール |
| `pyenv global 3.12.1` | 🌍 どこでもOK | システム全体の設定 |
| `pyenv local 3.12.1` | 📁 プロジェクト内 | そのフォルダ専用の設定 |
| `python -m venv .venv` | 📁 プロジェクト内 | そのフォルダに仮想環境を作成 |
| `source .venv/bin/activate` | 📁 プロジェクト内 | `.venv`があるフォルダ |
| `pip install パッケージ` | 📁 プロジェクト内 | 仮想環境が有効な状態で |
| `pip freeze > requirements.txt` | 📁 プロジェクト内 | プロジェクトのファイルを作成 |
| `git clone ...` | 🏠 ホーム推奨 | 保存先フォルダで実行 |

**💡 簡単な見分け方:**

**🌍 どこでもOK（システム全体のツール）:**
- `brew` で始まるコマンド
- `pyenv install`, `pyenv global`（システム全体のPython管理）

**📁 プロジェクト内必須:**
- `pyenv local`（そのフォルダ専用）
- `python -m venv`（仮想環境作成）
- `source .venv/bin/activate`（仮想環境有効化）
- `pip install`（パッケージインストール）
- プロジェクトファイル作成系（`django-admin`, `touch`, `cat >`など）

---

## ⚠️ 再実行して問題が起こるコマンド一覧

| コマンド | 再実行の影響 | 対処法 |
|---------|------------|--------|
| `python -m venv .venv` | 🔴 既存の仮想環境が消える | 先に`rm -rf .venv`で削除してから作り直す |
| `echo '...' >> ~/.zshrc` | 🟡 設定が重複する | ファイルを開いて重複を削除 |
| `django-admin startproject` | 🔴 エラーまたは上書き | 既にある場合は実行しない |
| その他のインストール系 | 🟢 問題なし | 「既にあります」と表示されるだけ |

**💡 覚えておくポイント:**
- **インストール系**（brew install, pyenv installなど）→ 🟢 再実行OK
- **作成系**（venv作成, プロジェクト作成など）→ 🔴 再実行注意
- **設定追加系**（echo >> など）→ 🟡 重複するが動作はする

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
📍 **実行場所:** 🌍 どこでもOK（任意のフォルダ）
🔄 **再実行:** 🟢 何度でもOK

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

**💡 もし既にインストール済みなのに、もう一度ステップ1-3を実行したら？**

**答え: 問題ありません！** Homebrewのインストールスクリプトは賢いので：

```bash
# 既にインストールされている状態で実行すると...
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 以下のようなメッセージが表示されて終了
It appears Homebrew is already installed. If your intent is to reinstall you
should do the following before running this installer again:
    rm -rf /opt/homebrew
```

**結果:**
- ✅ システムは壊れない
- ✅ 既存のHomebrewに影響なし
- ⚠️ ただし時間の無駄（5分くらい）

**推奨:** まず `brew --version` で確認してから、必要な場合のみインストール

### 1-3. Homebrew をインストール

✅ **必須: 以下のコマンドを実行**
📍 **実行場所:** 🌍 どこでもOK（任意のフォルダ）
🔄 **再実行:** 🟡 注意（既にある場合は不要）

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
📍 **実行場所:** 🌍 どこでもOK（任意のフォルダ）
🔄 **再実行:** 🟢 何度でもOK（最新版に更新される）

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
📍 **実行場所:** 🌍 どこでもOK（任意のフォルダ）
🔄 **再実行:** 🟡 注意（設定が重複する可能性）

**💡 この設定をしないと pyenv が動きません！**

以下のコマンドを実行:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

**⚠️ 重要: このコマンドを何度も実行すると？**

**結果:**
- 🟡 `.zshrc`に同じ設定が複数行追加される
- 🟡 動作には問題ないが、ファイルが汚れる
- ✅ システムは壊れない

**確認方法:**

```bash
# 設定が何回書かれているか確認
grep -c "PYENV_ROOT" ~/.zshrc
```

**表示:**
```
1  ← 正常（1回だけ）
2  ← 2回実行してしまった
3  ← 3回実行してしまった
```

**もし重複してしまったら（修正方法）:**

```bash
# .zshrcを開く
open -e ~/.zshrc

# 重複している以下の4行を削除（1セットだけ残す）
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# 保存してターミナルを再起動
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
📍 **実行場所:** 🌍 どこでもOK（任意のフォルダ）
🔄 **再実行:** 🟢 何度でもOK（同じバージョンなら「Already installed」と表示される）

**最新の 3.12 系をインストール（例: 3.12.1）:**

```bash
pyenv install 3.12.1
```

**⚠️ もし既にインストール済みのバージョンを再度実行すると？**

```bash
pyenv install 3.12.1
# 既にインストール済みの場合...

# 表示:
python-build: definition not found: 3.12.1

The following versions contain `3.12.1' in the name:
  3.12.1

See all available versions with `pyenv install --list'.

If the version you need is missing, try upgrading pyenv:
  brew update && brew upgrade pyenv
```

または

```
pyenv: version `3.12.1' already installed
```

**結果:**
- ✅ システムは壊れない
- ✅ 既存のPythonに影響なし
- ⚠️ 時間の無駄（5-10分）

**確認方法:**

```bash
# インストール済みバージョンを確認
pyenv versions
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
📍 **実行場所:** 📁 プロジェクトフォルダ内（重要！）
🔄 **再実行:** 🔴 注意（既存の仮想環境が上書きされる）

```bash
python -m venv .venv
```

**⚠️ 既に `.venv` がある状態で再度実行すると？**

**結果:**
- 🔴 既存の `.venv` フォルダが上書きされる
- 🔴 インストールしたパッケージが全て消える
- ✅ システムは壊れない

**例:**

```bash
# 初回: 仮想環境を作成
cd ~/Projects/my-project
python -m venv .venv
source .venv/bin/activate
pip install django requests  # パッケージをインストール

# 誤って再度実行
python -m venv .venv  # ← これを実行すると...
# → djangoとrequestsが消える！

# 確認
pip list
# → pipとsetuptoolsだけ（まっさらな状態に戻る）
```

**もし誤って再実行してしまったら:**

```bash
# requirements.txtがあれば復元可能
pip install -r requirements.txt

# requirements.txtがない場合
# → 再度パッケージをインストールするしかない
```

**💡 だからrequirements.txtが重要！**

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
📍 **実行場所:** 📁 プロジェクトフォルダ内（`.venv`があるフォルダ）
🔄 **再実行:** 🟢 何度でもOK

```bash
# Mac/Linux
source .venv/bin/activate
```

**⚠️ 既に有効化された状態で再度実行すると？**

**結果:**
- ✅ 問題なし
- ✅ 同じ仮想環境が再度有効化されるだけ

**💡 重要: 必ず `.venv` があるフォルダで実行！**

```bash
# ❌ 間違った場所で実行
cd ~
source .venv/bin/activate
# → エラー: No such file or directory

# ✅ 正しい場所で実行
cd ~/Projects/my-project  # .venvがあるフォルダ
source .venv/bin/activate
# → 成功: (.venv) がプロンプトに表示される
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
📍 **実行場所:** 🏠 ホームディレクトリ推奨（または任意の場所）

```bash
mkdir -p ~/Projects/my-django-app
cd ~/Projects/my-django-app
```

**📖 説明:**
- `~/Projects/` = あなたのプロジェクトをまとめるフォルダ
- 場所は自由（デスクトップでもDocumentsでもOK）
- 推奨: `~/Projects/` で統一すると管理しやすい

**ステップ 2: 使用する Python バージョンを指定（ローカル設定）**

🔶 **推奨: pyenvを使う場合**
📍 **実行場所:** 📁 プロジェクトフォルダ内（`~/Projects/my-django-app`）

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
📍 **実行場所:** 📁 プロジェクトフォルダ内（`~/Projects/my-django-app`）
🔄 **再実行:** 🔴 注意（既存が消える）

```bash
python -m venv .venv
```

**💡 確認: 現在のフォルダが正しいか？**

```bash
pwd
# 表示: /Users/あなた/Projects/my-django-app

# ここで実行すれば、
# /Users/あなた/Projects/my-django-app/.venv が作られる
```

**ステップ 4: 仮想環境を有効化**

✅ **必須**
📍 **実行場所:** 📁 プロジェクトフォルダ内（`.venv`があるフォルダ）

```bash
source .venv/bin/activate
```

**✅ プロンプトが変わる:**

```bash
(.venv) user@MacBook my-django-app %
```

**ステップ 5: pip を最新に更新**

✅ **必須**
📍 **実行場所:** 📁 プロジェクトフォルダ内（仮想環境が有効な状態）

```bash
pip install --upgrade pip
```

**💡 確認: 仮想環境が有効か？**

プロンプトに `(.venv)` が表示されているはず:

```bash
(.venv) user@MacBook my-django-app %
```

**ステップ 6: Django をインストール**

✅ **必須（このプロジェクトの場合）**
📍 **実行場所:** 📁 プロジェクトフォルダ内（仮想環境が有効な状態）

```bash
pip install django
```

**ステップ 7: Django プロジェクトを作成**

✅ **必須**
📍 **実行場所:** 📁 プロジェクトフォルダ内
🔄 **再実行:** 🔴 エラーまたは上書き（既にある場合は実行しない）

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
- "Python 3.11 以降が必要" などの記載を探す

**ステップ 3: 必要な Python バージョンをインストール（必要に応じて）**

⭐ **任意: 指定されたバージョンがない場合のみ**

```bash
# 例: Python 3.11が必要な場合
pyenv install 3.11.7
pyenv local 3.11.7
```

**ステップ 4: 仮想環境を作成**

✅ **必須**

```bash
python -m venv .venv
source .venv/bin/activate
```

**ステップ 5: 依存パッケージをインストール**

✅ **必須**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**💡 `requirements.txt` = プロジェクトに必要なパッケージ一覧**

**ステップ 6: 動作確認**

⭐ **任意: 動くか確認したい場合**

```bash
# プロジェクトによって異なる
python manage.py runserver  # Djangoの場合
# または
python app.py              # Flaskの場合
# または
python main.py             # その他
```

**ステップ 7: VSCode で開く**

🔶 **推奨**

```bash
code .
```

**🎉 既存プロジェクトの環境構築完了！**

---

### 6-3. .gitignore の設定（重要！）

**✅ 必須: Gitを使う場合**

**💡 仮想環境はGitにコミットしない！**

`.gitignore` ファイルを作成:

```bash
touch .gitignore
```

以下を記入:

```gitignore
# 仮想環境（必須）
.venv/
venv/
env/
ENV/

# Python関連（必須）
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# IDE関連（推奨）
.vscode/
.idea/
*.swp
*.swo

# OS関連（推奨）
.DS_Store
Thumbs.db

# 環境変数（必須）
.env
.env.local

# データベース（推奨）
*.sqlite3
db.sqlite3
```

**💡 なぜ .venv をコミットしない？**
- 容量が大きい（数百 MB）
- 環境依存（Mac 用の venv は Windows で動かない）
- `requirements.txt` があれば誰でも再現できる

---

## ステップ 7: お客様のプロジェクトで使う 🤝

**✅ 必須: 実務で使う場合**

### 7-1. お客様から Python バージョンを指定された場合

**シナリオ: 「Python 3.9 を使ってください」と言われた**

**ステップ 1: Python 3.9 をインストール**

✅ **必須**

```bash
# 最新の3.9系を確認
pyenv install --list | grep "^\s*3\.9\."

# インストール（例: 3.9.18）
pyenv install 3.9.18
```

**ステップ 2: プロジェクトフォルダで設定**

✅ **必須**

```bash
cd ~/Projects/お客様A/project-a
pyenv local 3.9.18
```

**ステップ 3: 確認**

✅ **必須**

```bash
python --version
```

**✅ 表示:**

```
Python 3.9.18
```

**ステップ 4: 仮想環境を作成**

✅ **必須**

```bash
python -m venv .venv
source .venv/bin/activate
```

**🎉 お客様の指定バージョンで環境構築完了！**

---

### 7-2. 複数のお客様プロジェクトを管理

**フォルダ構成例:**

```
~/Projects/
  ├── お客様A/
  │   └── project-a/
  │       ├── .python-version    # ⭐任意: 3.9.18
  │       ├── .venv/             # ✅必須
  │       └── requirements.txt   # ✅必須
  │
  ├── お客様B/
  │   └── project-b/
  │       ├── .python-version    # ⭐任意: 3.11.7
  │       ├── .venv/             # ✅必須
  │       └── requirements.txt   # ✅必須
  │
  └── 自分/
      └── my-project/
          ├── .python-version    # ⭐任意: 3.12.1
          ├── .venv/             # ✅必須
          └── requirements.txt   # ✅必須
```

**切り替え方法:**

```bash
# お客様Aのプロジェクト
cd ~/Projects/お客様A/project-a
source .venv/bin/activate
python --version  # → 3.9.18

# お客様Bのプロジェクト
cd ~/Projects/お客様B/project-b
source .venv/bin/activate
python --version  # → 3.11.7
```

**💡 `.python-version` があれば、自動的に切り替わる！**

---

### 7-3. お客様のプロジェクトでの日常作業フロー

**1. 作業開始時:**

✅ **必須**

```bash
cd ~/Projects/お客様A/project-a
source .venv/bin/activate
git pull origin main
```

**2. 開発作業:**

✅ **必須**

```bash
# コードを編集
# ...

# 動作確認
python manage.py runserver
```

**3. 新しいパッケージが必要になった:**

✅ **必須**

```bash
# 仮想環境が有効化されていることを確認
pip install 新しいパッケージ名

# requirements.txtを更新
pip freeze > requirements.txt

# Git にコミット
git add requirements.txt
git commit -m "Add 新しいパッケージ名"
git push origin feature/新機能
```

**4. 作業終了時:**

⭐ **任意**

```bash
deactivate
```

---

## ステップ 8: requirements.txt の使い方 📝

**✅ 必須: チーム開発の場合**
**🔶 推奨: 個人開発でも使うべき**

### 8-1. requirements.txt とは？

**requirements.txt:**
- プロジェクトに必要なパッケージの一覧
- バージョンも含めて記録
- これがあれば、誰でも同じ環境を再現できる

**例:**

```txt
Django==5.0
requests==2.31.0
pytest==7.4.3
```

### 8-2. requirements.txt の作成

✅ **必須: プロジェクト完成時**

**現在インストールされているパッケージを出力:**

```bash
pip freeze > requirements.txt
```

**📖 コマンドの詳細解説:**

```bash
pip freeze > requirements.txt
└┬┘ └─┬──┘ └┬┘└──────┬────────┘
 │     │     │         └─ 出力先ファイル名
 │     │     └─ リダイレクト（出力をファイルに書き込む）
 │     └─ インストール済みパッケージをrequirements.txt形式で表示
 └─ pipを実行
```

**内容を確認:**

```bash
cat requirements.txt
```

**表示例:**

```txt
asgiref==3.7.2
Django==5.0
sqlparse==0.4.4
```

**💡 依存関係も含めて全て出力される**

### 8-3. requirements.txt からインストール

✅ **必須: 新しい環境でセットアップする時**

**新しい環境でプロジェクトをセットアップ:**

```bash
# 仮想環境を作成・有効化
python -m venv .venv
source .venv/bin/activate

# requirements.txtからインストール
pip install -r requirements.txt
```

**📖 コマンドの詳細解説:**

```bash
pip install -r requirements.txt
└┬┘ └──┬──┘ └┬┘└──────┬────────┘
 │     │     │         └─ 読み込むファイル名
 │     │     └─ ファイルから読み込むオプション
 │     └─ インストールコマンド
 └─ pipを実行
```

**✅ 成功メッセージ:**

```
Successfully installed Django-5.0 asgiref-3.7.2 sqlparse-0.4.4
```

### 8-4. requirements.txt の管理ベストプラクティス

**パターン 1: シンプル（推奨・初心者向け）**

```txt
Django==5.0
requests==2.31.0
```

**メリット:**
- シンプルで読みやすい
- 最小限のパッケージだけ記載

**デメリット:**
- 依存パッケージのバージョンが固定されない

---

**パターン 2: 完全版（本番環境向け）**

```bash
pip freeze > requirements.txt
```

**メリット:**
- 完全に同じ環境を再現できる
- バージョンが完全に固定される

**デメリット:**
- ファイルが長くなる
- 不要なパッケージも含まれることがある

---

**パターン 3: 分割管理（大規模プロジェクト向け）**

⭐ **任意: 大規模プロジェクトの場合**

```
requirements/
  ├── base.txt        # 共通パッケージ
  ├── dev.txt         # 開発環境用
  └── prod.txt        # 本番環境用
```

**base.txt:**
```txt
Django==5.0
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

### 8-5. バージョン指定の書き方

⭐ **任意: 知識として**

```txt
# 完全一致（推奨）
Django==5.0

# 以上
Django>=5.0

# 以下
Django<=5.0

# 範囲指定
Django>=4.2,<6.0

# 最新版（非推奨）
Django
```

**💡 推奨: `==` で完全一致を指定（再現性が高い）**

### 8-6. requirements.txt を更新する手順

✅ **必須: 新しいパッケージを追加した時**

**新しいパッケージをインストールした後:**

```bash
# パッケージをインストール
pip install 新しいパッケージ

# requirements.txtを更新
pip freeze > requirements.txt

# Gitにコミット
git add requirements.txt
git commit -m "Add 新しいパッケージ"
git push
```

**💡 チーム開発では、必ず requirements.txt を最新に保つ！**

---

## ステップ 9: AI 開発の追加設定 🤖

**⭐ 任意: AI/機械学習開発をする場合のみ**

### 9-1. AI/機械学習でよく使うライブラリ

**基本ライブラリ:**
- NumPy: 数値計算
- Pandas: データ分析
- Matplotlib: グラフ描画
- Scikit-learn: 機械学習

**ディープラーニング:**
- TensorFlow: Google 製
- PyTorch: Meta（Facebook）製
- Keras: TensorFlow の高レベル API

**生成 AI:**
- OpenAI: GPT API
- LangChain: LLM アプリ開発フレームワーク
- Transformers: Hugging Face のライブラリ

### 9-2. AI 開発用の環境構築

⭐ **任意**

**基本構成:**

```bash
# プロジェクトフォルダ作成
mkdir -p ~/Projects/ai-project
cd ~/Projects/ai-project

# Python 3.11を使用（AI開発では3.11が安定）
pyenv local 3.11.7

# 仮想環境作成
python -m venv .venv
source .venv/bin/activate

# 基本ライブラリをインストール
pip install --upgrade pip
pip install numpy pandas matplotlib scikit-learn jupyter
```

**Jupyter Notebook のインストール（推奨）:**

```bash
pip install jupyter
```

**起動:**

```bash
jupyter notebook
```

**💡 ブラウザで Jupyter Notebook が開きます**

### 9-3. TensorFlow のインストール（M2 Mac 用）

⭐ **任意**

**M2 Mac では特別な方法が必要:**

```bash
# 必要なライブラリ
pip install tensorflow-macos tensorflow-metal
```

**確認:**

```python
import tensorflow as tf
print(tf.__version__)
print("GPU available:", tf.config.list_physical_devices('GPU'))
```

**💡 M2 Mac の GPU（Metal）を活用できます！**

### 9-4. PyTorch のインストール

⭐ **任意**

**公式サイトで最適なコマンドを確認:**
https://pytorch.org/get-started/locally/

**M2 Mac の場合:**

```bash
pip install torch torchvision torchaudio
```

**確認:**

```python
import torch
print(torch.__version__)
print("MPS available:", torch.backends.mps.is_available())
```

### 9-5. OpenAI API の使用

⭐ **任意**

**インストール:**

```bash
pip install openai
```

**使用例:**

```python
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

**💡 API キーは環境変数で管理:**

```bash
export OPENAI_API_KEY="your-api-key"
```

または `.env` ファイルを作成:

```bash
pip install python-dotenv
```

`.env`:
```
OPENAI_API_KEY=your-api-key
```

**Python で読み込み:**

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

### 9-6. LangChain のインストール

⭐ **任意**

```bash
pip install langchain langchain-openai
```

**簡単な例:**

```python
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model="gpt-4")
messages = [HumanMessage(content="こんにちは！")]
response = llm.invoke(messages)
print(response.content)
```

### 9-7. AI 開発用の requirements.txt 例

⭐ **任意**

**基本構成:**

```txt
# データサイエンス基本
numpy==1.26.2
pandas==2.1.4
matplotlib==3.8.2
scikit-learn==1.3.2

# Jupyter
jupyter==1.0.0

# ディープラーニング（どちらか）
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

## 🔧 トラブルシューティング

### エラー 1: pyenv がインストールできない

**症状:**

```bash
brew install pyenv
# エラーが出る
```

**解決方法 1: Homebrew を更新**

```bash
brew update
brew upgrade
brew install pyenv
```

**解決方法 2: Xcode Command Line Tools を再インストール**

```bash
xcode-select --install
```

### エラー 2: Python のインストールが失敗する

**症状:**

```bash
pyenv install 3.12.1
# BUILD FAILED エラー
```

**解決方法 1: 必要な依存関係をインストール**

```bash
brew install openssl readline sqlite3 xz zlib
```

**解決方法 2: 環境変数を設定してインストール**

```bash
CFLAGS="-I$(brew --prefix openssl)/include" \
LDFLAGS="-L$(brew --prefix openssl)/lib" \
pyenv install 3.12.1
```

### エラー 3: python コマンドが見つからない

**症状:**

```bash
python --version
# command not found
```

**解決方法 1: python3 を使う**

```bash
python3 --version
```

**解決方法 2: pyenv の設定を確認**

```bash
# シェル設定を再読み込み
source ~/.zshrc

# pyenv のパスを確認
echo $PATH | grep pyenv
```

**解決方法 3: pyenv rehash**

```bash
pyenv rehash
python --version
```

### エラー 4: 仮想環境が有効化されない

**症状:**

```bash
source .venv/bin/activate
# プロンプトが変わらない
```

**解決方法 1: 仮想環境を再作成**

```bash
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
```

**解決方法 2: フルパスで指定**

```bash
source /Users/あなた/Projects/project-a/.venv/bin/activate
```

### エラー 5: pip install が Permission denied

**症状:**

```bash
pip install django
# Permission denied
```

**原因:** グローバル環境にインストールしようとしている

**解決方法: 仮想環境を使う**

```bash
# 仮想環境を作成
python -m venv .venv
source .venv/bin/activate

# 再度インストール
pip install django
```

**❌ 絶対にやってはいけないこと:**

```bash
sudo pip install  # これは絶対ダメ！システムを壊す可能性
```

### エラー 6: VSCode でインタープリターが表示されない

**症状:**
- `Python: Select Interpreter` で何も表示されない

**解決方法 1: Python 拡張機能を再インストール**

1. 拡張機能から Python をアンインストール
2. VSCode を再起動
3. Python 拡張機能を再インストール

**解決方法 2: VSCode を再起動**

```bash
# 完全に終了
⌘ + Q

# 再起動
```

**解決方法 3: インタープリターのパスを手動で指定**

1. `⌘ + Shift + P`
2. `Python: Select Interpreter`
3. `Enter interpreter path...` を選択
4. `/Users/あなた/.pyenv/versions/3.12.1/bin/python` を入力

### エラー 7: requirements.txt からインストールできない

**症状:**

```bash
pip install -r requirements.txt
# エラーが出る
```

**解決方法 1: pip を最新に更新**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**解決方法 2: 1 つずつインストール**

```bash
# requirements.txtの各行を1つずつ実行
pip install Django==5.0
pip install requests==2.31.0
```

**解決方法 3: バージョン指定を緩くする**

requirements.txt:
```txt
# 完全一致から範囲指定に変更
Django>=5.0,<6.0
requests>=2.31.0
```

### エラー 8: M2 Mac で特定のパッケージがインストールできない

**症状:**
- `pip install` でエラー
- `Building wheel for xxx ... error`

**解決方法: Rosetta 2 で実行**

```bash
# Rosetta 2をインストール（初回のみ）
softwareupdate --install-rosetta

# x86_64版のPythonをインストール
arch -x86_64 pyenv install 3.11.7

# プロジェクトで使用
arch -x86_64 pyenv local 3.11.7
```

**💡 ほとんどのパッケージは M2 ネイティブで動作します。これは最終手段！**

---

## 📚 よくある質問

### Q1: pyenv と venv の違いは？

**A:**

| 機能 | pyenv | venv |
|------|-------|------|
| **役割** | Python のバージョン管理 | プロジェクトごとの環境分離 |
| **管理対象** | Python 本体（3.9、3.10 など） | パッケージ（Django、requests など） |
| **使うタイミング** | 最初に 1 回 | プロジェクトごと |
| **必須度** | ✅ 必須 | ✅ 必須 |
| **例** | `pyenv install 3.12.1` | `python -m venv .venv` |

**両方使う！**
- pyenv で Python バージョンをインストール
- venv でプロジェクトごとに環境を分離

### Q2: .venv と venv の違いは？

**A:** ただの名前の違いです！

```bash
# どちらもOK
python -m venv .venv  # ドットで始まる（隠しフォルダ）
python -m venv venv   # ドットなし

# env や .env も使える
python -m venv env
python -m venv .env
```

**💡 推奨: `.venv`**
- ドットで始まるので隠しフォルダ
- プロジェクトフォルダがすっきり見える
- Python 公式ドキュメントでも推奨

### Q3: グローバル環境にパッケージをインストールしても良い？

**A:** ❌ 推奨しません

**理由:**
- プロジェクト間で干渉する
- バージョン競合が発生する
- プロジェクトの依存関係が不明確になる

**例外的に OK なもの:**
- `pip` 自体のアップグレード
- `jupyter` などの汎用ツール

**基本: すべてのパッケージは仮想環境に！**

### Q4: pyenv global と pyenv local の違いは？

**A:**

**pyenv global: ✅ 必須**
- システム全体のデフォルト Python
- どこでも使われる

```bash
pyenv global 3.12.1
```

**pyenv local: 🔶 推奨**
- 特定のプロジェクトフォルダ専用
- `.python-version` ファイルが作成される
- そのフォルダでは優先的に使われる

```bash
cd ~/Projects/project-a
pyenv local 3.11.7  # project-aだけで3.11.7を使う
```

**優先順位:**
1. `pyenv local`（カレントディレクトリ）
2. `pyenv global`（システムデフォルト）

### Q5: 複数の Python バージョンを同時に使える？

**A:** ✅ はい！それが pyenv の目的です

```bash
# バージョン一覧
pyenv versions

# プロジェクトA: Python 3.9
cd ~/Projects/project-a
pyenv local 3.9.18
python --version  # → 3.9.18

# プロジェクトB: Python 3.12
cd ~/Projects/project-b
pyenv local 3.12.1
python --version  # → 3.12.1
```

### Q6: 仮想環境を削除するには？

**A:** フォルダを削除するだけ

```bash
# 仮想環境を無効化（有効化している場合）
deactivate

# フォルダを削除
rm -rf .venv

# 再作成
python -m venv .venv
```

**💡 仮想環境はただのフォルダ。気軽に作り直せます！**

### Q7: pip freeze と pip list の違いは？

**A:**

**pip list:**
- インストール済みパッケージの一覧表示
- 人間が読みやすい形式

```bash
pip list
```

```
Package    Version
---------- -------
Django     5.0
requests   2.31.0
```

**pip freeze:**
- requirements.txt 用の形式
- そのままファイルに保存できる

```bash
pip freeze
```

```
Django==5.0
requests==2.31.0
```

**使い分け:**
- 確認: `pip list`
- requirements.txt 作成: `pip freeze > requirements.txt`

### Q8: Python 2 と Python 3 の違いは？

**A:**

**Python 2:**
- 2020 年にサポート終了
- 古いコード・レガシーシステムで使用

**Python 3:**
- 現在の標準
- すべての新規プロジェクトで使用

**💡 Python 3 だけ覚えれば OK！Python 2 は無視してください**

### Q9: Anaconda を使うべき？

**A:** 初心者には pyenv + venv を推奨

**Anaconda が向いている人:**
- データサイエンス専門
- GUI で管理したい
- 科学計算ライブラリを頻繁に使う

**pyenv + venv が向いている人:**
- Web 開発もする
- シンプルな環境が好き
- ディスク容量を節約したい

**💡 まずは pyenv + venv を使って、必要になったら Anaconda を検討**

### Q10: VSCode の Python 拡張機能は必須？

**A:** ✅ VSCodeを使うなら必須

**拡張機能なし:**
- Python ファイルは編集できる
- シンタックスハイライトだけ

**拡張機能あり:**
- 自動補完
- エラー表示
- デバッガー
- インタープリター選択
- テスト実行

**💡 必ずインストールしましょう！開発効率が 10 倍違います**

### Q11: 仮想環境を Git にコミットすべき？

**A:** ❌ 絶対にダメ！

**理由:**
- 容量が大きい（数百 MB）
- 環境依存（Mac 用の venv は Windows で動かない）
- 不要（requirements.txt で再現可能）

**.gitignore に必ず追加:**

```gitignore
.venv/
venv/
env/
```

**代わりに requirements.txt をコミット！**

### Q12: プロジェクトを別の PC に移動するには？

**A:**

**元の PC:**

```bash
# requirements.txtを作成
pip freeze > requirements.txt

# Gitにコミット
git add requirements.txt .python-version
git commit -m "Add requirements"
git push
```

**新しい PC:**

```bash
# クローン
git clone git@github.com:user/repo.git
cd repo

# Pythonバージョンを確認（.python-versionがあれば自動）
python --version

# 仮想環境を作成
python -m venv .venv
source .venv/bin/activate

# パッケージをインストール
pip install -r requirements.txt
```

**🎉 完全に同じ環境が再現できます！**

### Q13: Mac にプリインストールされている Python はどうすれば？

**A:** 無視してください！触らないでください！

**理由:**
- macOS システムが使っている
- 勝手に触るとシステムが壊れる
- pyenv でインストールした Python を使う

**確認:**

```bash
which python3
# /usr/bin/python3 ← これはシステム用（使わない）

which python
# /Users/あなた/.pyenv/shims/python ← これを使う！
```

### Q14: AI 開発で TensorFlow と PyTorch、どちらを使うべき？

**A:** プロジェクトによって異なります

**TensorFlow:**
- Google 製
- 本番環境向け
- TensorFlow Lite でモバイル対応

**PyTorch:**
- Meta（Facebook）製
- 研究・プロトタイピング向け
- 直感的で初心者に優しい

**💡 初心者には PyTorch を推奨！**

両方インストールしても問題ありません（仮想環境が別なら）。

### Q15: OpenAI API の料金は？

**A:**

**GPT-4:**
- 入力: $0.01 / 1K トークン
- 出力: $0.03 / 1K トークン

**GPT-3.5 Turbo:**
- 入力: $0.0005 / 1K トークン
- 出力: $0.0015 / 1K トークン

**💡 1000 トークン ≈ 750 単語（英語）≈ 500 文字（日本語）**

**開発時の注意:**
- API キーを `.env` で管理
- `.env` を `.gitignore` に追加
- 使用量制限を設定

### Q16: uv は使うべき？

**A:** 初心者はまず pyenv + venv から！

**段階的なアプローチ:**

```
ステップ1: pyenv + venv をマスター（本ガイド）
    ↓（3〜6ヶ月）
ステップ2: Python開発に慣れる
    ↓（必要に応じて）
ステップ3: uvを試す
```

**uv を試すタイミング:**
- pyenv + venv が完璧に使える
- Python の基礎を理解している
- より高速な開発環境が欲しい
- 新しいツールに興味がある

**💡 焦る必要はありません！pyenv + venv でも十分プロフェッショナルです**

### Q17: Windows 開発者とチームを組む場合、どうすれば良い？

**A:** venv が最強の共通言語！

**推奨構成:**
- **Mac/Linux:** pyenv + venv
- **Windows:** Python 公式インストーラー + venv
- **共通:** requirements.txt

**理由:**
- venv は全 OS で完全互換
- requirements.txt で環境を共有
- Python のインストール方法だけが異なる

**プロジェクトの README に両 OS のコマンドを記載:**

````markdown
# Mac/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
````

**💡 詳細は「Windows 開発者との共存性」セクションを参照！**

### Q18: プロジェクトに必須のファイルは？

**A:**

```
project/
  ├── .python-version      # ⭐任意（pyenvを使う場合に便利）
  ├── requirements.txt     # ✅必須（チーム開発では絶対必要）
  ├── .gitignore          # ✅必須（Gitを使う場合）
  └── README.md           # 🔶推奨（セットアップ手順を書く）
```

**各ファイルの説明:**

**.python-version** ⭐任意
- pyenvで自動的にバージョンを切り替えるためのファイル
- なくても動くが、あると便利
- 内容例: `3.12.1`

**requirements.txt** ✅必須（チーム開発）
- プロジェクトに必要なパッケージ一覧
- チーム開発では絶対に必要
- 内容例: `Django==5.0`

**.gitignore** ✅必須（Gitを使う場合）
- Gitにコミットしないファイルを指定
- `.venv/` は必ず含める
- 内容例: `.venv/`、`__pycache__/`

**README.md** 🔶推奨
- セットアップ手順を書く
- チームメンバーや未来の自分のため
- 内容例: Python バージョン、インストール手順

### Q19: コマンドを間違ったフォルダで実行してしまった！

**A:** コマンドによって対処法が違います

**ケース1: `python -m venv .venv` を間違った場所で実行**

```bash
# 例: ホームディレクトリで実行してしまった
cd ~
python -m venv .venv  # ← 間違い！

# 結果: ~/.venv が作られる
```

**対処法:**

```bash
# 1. 間違って作った仮想環境を削除
cd ~
rm -rf .venv

# 2. 正しい場所で作り直す
cd ~/Projects/my-project
python -m venv .venv
```

**ケース2: `source .venv/bin/activate` を間違った場所で実行**

```bash
cd ~
source .venv/bin/activate
# エラー: -bash: .venv/bin/activate: No such file or directory
```

**対処法:**

```bash
# 正しい場所に移動してから実行
cd ~/Projects/my-project
source .venv/bin/activate
```

**ケース3: システム全体のコマンド（brew, pyenvなど）**

```bash
# どこで実行してもOK
cd ~/Desktop
brew install pyenv  # ← どこで実行しても同じ結果
```

**💡 まとめ:**
- システム全体のツール → どこでもOK
- プロジェクト固有のコマンド → 必ずプロジェクトフォルダで！

### Q20: 同じコマンドを2回実行してしまった場合の影響は？

**A:** コマンドによって異なります

| コマンド | 2回目の影響 | 対処 |
|---------|-----------|------|
| `brew install pyenv` | 🟢 問題なし | 「既にあります」と表示 |
| `pyenv install 3.12.1` | 🟢 問題なし | 「既にあります」と表示 |
| `python -m venv .venv` | 🔴 仮想環境が初期化される | requirements.txtから復元 |
| `echo '...' >> ~/.zshrc` | 🟡 設定が重複 | ファイルを編集して削除 |
| `django-admin startproject` | 🔴 エラーまたは上書き | 実行しない |
| `source .venv/bin/activate` | 🟢 問題なし | 再度有効化されるだけ |
| `pip install パッケージ` | 🟢 問題なし | 「既にあります」と表示 |

**💡 基本ルール:**
- **インストール・有効化系** → 🟢 何度でもOK
- **作成・追記系** → 🔴🟡 注意が必要

---

## 🎓 実践シナリオ集

### シナリオ 1: Django で Web アプリを作る

```bash
# プロジェクト作成
mkdir -p ~/Projects/my-webapp
cd ~/Projects/my-webapp
pyenv local 3.12.1
python -m venv .venv
source .venv/bin/activate

# Django インストール
pip install --upgrade pip
pip install django

# Django プロジェクト作成
django-admin startproject config .
python manage.py migrate
python manage.py createsuperuser

# 開発サーバー起動
python manage.py runserver

# requirements.txt 作成
pip freeze > requirements.txt

# Git 管理
git init
echo ".venv/" >> .gitignore
git add .
git commit -m "Initial commit"
```

### シナリオ 2: Flask で REST API を作る

```bash
# プロジェクト作成
mkdir -p ~/Projects/my-api
cd ~/Projects/my-api
pyenv local 3.11.7
python -m venv .venv
source .venv/bin/activate

# Flask インストール
pip install --upgrade pip
pip install flask flask-cors

# app.py 作成
cat > app.py << 'EOF'
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)
EOF

# 実行
python app.py

# requirements.txt 作成
pip freeze > requirements.txt
```

### シナリオ 3: 機械学習プロジェクト

```bash
# プロジェクト作成
mkdir -p ~/Projects/ml-project
cd ~/Projects/ml-project
pyenv local 3.11.7
python -m venv .venv
source .venv/bin/activate

# 必要なパッケージをインストール
pip install --upgrade pip
pip install numpy pandas matplotlib scikit-learn jupyter

# Jupyter Notebook 起動
jupyter notebook

# プロジェクト構造
mkdir -p data notebooks models

# .gitignore 作成
cat > .gitignore << 'EOF'
.venv/
.ipynb_checkpoints/
__pycache__/
data/
*.pyc
EOF

# requirements.txt 作成
pip freeze > requirements.txt
```

### シナリオ 4: OpenAI API を使ったチャットボット

```bash
# プロジェクト作成
mkdir -p ~/Projects/chatbot
cd ~/Projects/chatbot
pyenv local 3.12.1
python -m venv .venv
source .venv/bin/activate

# パッケージインストール
pip install --upgrade pip
pip install openai python-dotenv

# .env ファイル作成
cat > .env << 'EOF'
OPENAI_API_KEY=your-api-key-here
EOF

# .gitignore 作成
cat > .gitignore << 'EOF'
.venv/
.env
__pycache__/
EOF

# main.py 作成
cat > main.py << 'EOF'
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat(message):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("チャットボット起動！（'quit'で終了）")
    while True:
        user_input = input("あなた: ")
        if user_input.lower() == 'quit':
            break
        response = chat(user_input)
        print(f"AI: {response}")
EOF

# 実行
python main.py

# requirements.txt 作成
pip freeze > requirements.txt
```

### シナリオ 5: お客様のプロジェクトに参加

```bash
# リポジトリをクローン
cd ~/Projects/お客様A
git clone git@github.com:client/project.git
cd project

# READMEで要件を確認
cat README.md
# "Python 3.9以降が必要"

# Python 3.9をインストール（なければ）
pyenv install 3.9.18
pyenv local 3.9.18

# 仮想環境作成
python -m venv .venv
source .venv/bin/activate

# 依存パッケージをインストール
pip install --upgrade pip
pip install -r requirements.txt

# データベースのマイグレーション
python manage.py migrate

# 開発サーバー起動
python manage.py runserver

# VSCodeで開く
code .
```

### シナリオ 6: 複数プロジェクトの切り替え

```bash
# 朝: お客様Aのプロジェクト
cd ~/Projects/お客様A/project-a
source .venv/bin/activate
python --version  # 3.9.18
git pull origin main
python manage.py runserver

# 午後: お客様Bのプロジェクト
deactivate
cd ~/Projects/お客様B/project-b
source .venv/bin/activate
python --version  # 3.12.1
git pull origin develop
python app.py

# 夕方: 自分のプロジェクト
deactivate
cd ~/Projects/my-project
source .venv/bin/activate
python --version  # 3.11.7
jupyter notebook
```

---

## 💪 完璧にできたかチェックリスト

### 基本セットアップ

- [ ] ✅ Homebrew がインストールされている（`brew --version`）
- [ ] ✅ pyenv がインストールされている（`pyenv --version`）
- [ ] ✅ Python 3.12.x がインストールされている（`pyenv versions`）
- [ ] 🔶 Python 3.11.x がインストールされている（`pyenv versions`）
- [ ] ✅ グローバルのデフォルトが 3.12.x（`python --version`）

### VSCode 設定

- [ ] ✅ Python 拡張機能がインストールされている
- [ ] ✅ インタープリターを選択できる（`⌘ + Shift + P` → Python: Select Interpreter）
- [ ] ✅ `.venv` が自動認識される

### プロジェクト管理

- [ ] ✅ 仮想環境を作成できる（`python -m venv .venv`）
- [ ] ✅ 仮想環境を有効化できる（`source .venv/bin/activate`）
- [ ] ✅ パッケージをインストールできる（`pip install パッケージ名`）
- [ ] ✅ requirements.txt を作成できる（`pip freeze > requirements.txt`）
- [ ] ✅ requirements.txt からインストールできる（`pip install -r requirements.txt`）

### 実践

- [ ] ✅ Django プロジェクトを作成できる
- [ ] ✅ VSCode でコードを実行できる
- [ ] ✅ 複数のプロジェクトで異なる Python バージョンを使える
- [ ] ✅ GitHub のプロジェクトをクローンして環境構築できる

**全部チェックできたら完璧です！🎉**

---

## 🎉 完成！

**おめでとうございます！**

あなたは今、プロの Python エンジニアと同じ環境を手に入れました！

### 次のステップ

**1. 基礎を固める**
- Python の文法を学ぶ
- Django や Flask のチュートリアル
- Git の使い方を習得

**2. 実践プロジェクトを作る**
- Web アプリを作る
- API を作る
- データ分析をする

**3. AI/機械学習に挑戦**
- Kaggle のチュートリアル
- Hugging Face のモデルを試す
- 自分のデータで ML モデルを作る

**4. オープンソースに貢献**
- GitHub で興味あるプロジェクトを探す
- Issue を解決する
- プルリクエストを送る

**5. モダンツールに挑戦（慣れてから）**
- uv を試してみる
- Poetry でプロジェクト管理
- Docker でコンテナ化

### 継続的な学習

**公式ドキュメント:**
- Python 公式: https://docs.python.org/ja/3/
- Django 公式: https://docs.djangoproject.com/ja/
- Flask 公式: https://flask.palletsprojects.com/

**コミュニティ:**
- Stack Overflow: 質問と回答
- Qiita: 日本語の技術記事
- Reddit r/Python: 海外のコミュニティ

**学習リソース:**
- Real Python: https://realpython.com/
- Python チュートリアル: 公式ドキュメント
- Udemy: オンラインコース

---

## 🙏 最後に

このガイドは、実際の初心者エンジニアの方々の質問とエラーを基に作成されています。

**あなたがつまずいたポイントは、他の人も同じようにつまずきます。**

もし新しいエラーや疑問が出てきたら、それを記録して共有してください。それが次の人の助けになります！

**Happy Coding! 🐍✨**

---

## 📝 このガイドについて

**バージョン:** 2.0  
**最終更新:** 2025 年 1 月  
**対象:** Mac M2 + VSCode ユーザー  
**前提:** Git・VSCode・Docker・GitHub SSH 接続が完了している状態

**改訂内容:**
- コマンドの単語レベルでの詳細解説を追加
- 必須/推奨/任意の明確化
- Windows開発者との共存性について詳細追加

**フィードバック大歓迎！**
- わかりにくい部分
- 新しいエラー
- 改善提案

**このガイドの目標:**  
他の資料を一切見なくても、このガイドだけで 100%完了できること

その目標に向けて、常にアップデートしていきます！🚀
