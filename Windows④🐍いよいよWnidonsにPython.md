# 🐍 Python開発環境 完全構築ガイド 2025 - Windows版

**【Windows 11/10 (x64/ARM64) + VSCode + py launcher + venv - 絶対に失敗しない決定版】**

> **📌 このガイドの特徴**
> - ✅ 他の資料は一切不要！このガイドだけで100%完了
> - ✅ すべてのコマンドを実行結果付きで解説  
> - ✅ よくあるエラーと解決方法を完全網羅
> - ✅ 2025年1月時点の最新情報
> - ✅ AI/生成AI開発にも完全対応
> - ✅ **x64版・ARM64版Windows完全対応**
> - ✅ PowerShell & Command Prompt両対応

---

## 📑 クイックナビゲーション

### 🎯 あなたの状況に合わせて選択

**今すぐ環境構築したい →** [PART 2: 基本環境構築](#part-2-基本環境構築)

**理解してから進みたい →** [PART 1: 準備と理解](#part-1-準備と理解)

**複数バージョン管理したい →** [pyenv-winインストール](#ステップ7-pyenv-winインストール任意)

**エラーが出た →** [PART 6: トラブルシューティング](#part-6-トラブルシューティング)

**AI開発がしたい →** [PART 5: AI/生成AI開発](#part-5-ai生成ai開発)

**ARM64版Windowsの注意点 →** [ARM64特有の注意事項](#arm64特有の注意事項)

---

## 目次

### PART 1: 準備と理解
1. [Python環境の選択肢を完全理解](#1-python環境の選択肢を完全理解)
2. [なぜpy launcher + venvなのか？](#2-なぜpy-launcher--venvなのか)
3. [完成イメージ](#3-完成イメージ)
4. [表記ルール](#4-表記ルール)
5. [Windows版の特徴](#5-windows版の特徴)
6. [ARM64特有の注意事項](#6-arm64特有の注意事項)

### PART 2: 基本環境構築
7. [現在の状態確認](#7-現在の状態確認)
8. [Python公式インストール](#8-python公式インストール)
9. [py launcherの使い方](#9-py-launcherの使い方)
10. [venv使い方](#10-venv使い方)
11. [pyenv-winインストール（任意）](#11-pyenv-winインストール任意)

### PART 3: VSCode統合
12. [VSCode Python設定](#12-vscode-python設定)

### PART 4: 実践プロジェクト
13. [新規プロジェクト作成](#13-新規プロジェクト作成)
14. [既存プロジェクトクローン](#14-既存プロジェクトクローン)
15. [requirements.txt管理](#15-requirementstxt管理)

### PART 5: AI/生成AI開発
16. [AI開発環境](#16-ai開発環境)

### PART 6: トラブルシューティング
17. [エラー解決](#17-エラー解決)
18. [よくある質問](#18-よくある質問)

---

## PART 1: 準備と理解

### 1. Python環境の選択肢を完全理解

#### 8つの選択肢

| # | 選択肢 | 推奨度 | 対象 |
|---|--------|--------|------|
| 1 | Microsoft Store版 | ⚠️⚠️ | **初心者のみ・制限あり** |
| 2 | **python.org公式** | ⭐⭐⭐⭐⭐ | **Windows推奨** |
| 3 | **py launcher** | ⭐⭐⭐⭐⭐ | **全員必須** |
| 4 | **venv** | ⭐⭐⭐⭐⭐ | **全員必須** |
| 5 | pyenv-win | ⭐⭐⭐⭐ | 複数バージョン管理 |
| 6 | uv | ⭐⭐⭐⭐ | 上級者 |
| 7 | Anaconda | ⭐⭐⭐ | データサイエンス |
| 8 | Docker | ⭐⭐⭐⭐ | 本番環境 |

#### 詳細比較

**1. Microsoft Store版Python**

⚠️ **初心者のみ・制限あり:**
```powershell
# Microsoft Store版の確認
Get-Command python | Select-Object Source

# 表示例:
# C:\Users\あなた\AppData\Local\Microsoft\WindowsApps\python.exe
```

**問題点:**
- アクセス権限制限（一部フォルダに書き込めない）
- PATH設定が複雑
- 一部パッケージがインストールできない
- 本格開発には不向き

**向いている人:**
- プログラミング完全初心者
- とりあえず試したい
- 後で公式版に移行する予定

**本格開発するなら:**
❌ Microsoft Store版  
✅ python.org公式版

---

**2. python.org公式版** ⭐⭐⭐⭐⭐

✅ **Windows開発者はこれを使う！**

```
役割: Python本体のインストール

特徴:
- Windows公式推奨
- 完全な機能
- 制限なし
- py launcherが付属

ダウンロード:
https://www.python.org/downloads/

メリット:
✅ 最も安定
✅ 公式サポート
✅ 全機能利用可能
✅ py launcher自動インストール

デメリット:
⚠️ 複数バージョン管理は手動
⚠️ PATH設定に注意
```

---

**3. py launcher** ⭐⭐⭐⭐⭐

✅ **Windows最強ツール！**

```
役割: Pythonバージョンランチャー（Windows標準）

できること:
- 複数Pythonバージョンを自動管理
- py コマンドで簡単切り替え
- プロジェクトごとにバージョン指定

コマンド例:
py -3.12      # Python 3.12実行
py -3.11      # Python 3.11実行
py -0         # インストール済み一覧

メリット:
✅ Python公式インストーラーに付属（追加不要）
✅ 自動的に最適バージョン選択
✅ PATH汚染なし
✅ 完全クロスバージョン対応

Windowsの強み:
Macのpyenv相当が標準搭載！
```

**py launcher vs python コマンド:**

```
# ❌ pythonコマンド（非推奨）
python --version
# → 最初にPATHで見つかったPython（不確実）

# ✅ py launcher（推奨）
py --version
py -3.12 --version
# → 明示的にバージョン指定（確実）
```

---

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
py launcher: Pythonバージョン管理
venv: パッケージ管理
```

**py launcher vs venv の違い:**

```
┌─────────────────────────────────────┐
│     py launcher（バージョン管理）     │
│  ┌─────────────────────────────┐   │
│  │  Python 3.11                 │   │
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
- py launcher: Pythonバージョンを選ぶ
- venv: パッケージを分離する
```

---

**5. pyenv-win** ⭐⭐⭐⭐

⚡ **Mac pyenvのWindows版（任意）**

```
特徴:
- pyenvのWindows移植版
- CLI統一（Mac/Linux開発者向け）
- より高度なバージョン管理

推奨タイミング:
1. py launcher + venvマスター
2. Mac/Linuxとコマンド統一したい
3. より細かいバージョン管理

初心者は:
❌ まだ使わない
✅ py launcher + venvから始める

理由:
py launcherで十分！
Windows標準で簡単！
```

---

**6. uv** ⭐⭐⭐⭐

⚡ **次世代ツール（上級者向け）**

```
特徴:
- Rust製超高速ツール
- pip + venv + pyenv統合
- 10〜100倍速い
- Windows完全対応

推奨タイミング:
1. py launcher + venvマスター
2. 3〜6ヶ月Python開発経験
3. より高速な環境が欲しい時

初心者は:
❌ まだ使わない
✅ py launcher + venvから始める
```

---

**7. conda/Anaconda** ⭐⭐⭐

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
AI開発でもpy launcher + venvで十分
```

---

**8. Docker** ⭐⭐⭐⭐

🐳 **本番環境・チーム開発**

```
用途:
- 本番環境
- CI/CD
- チーム開発

推奨:
開発: py launcher + venv
本番: Docker

初心者は:
✅ ローカル開発はpy launcher + venv
✅ 慣れたらDockerも学ぶ
```

---

### 2. なぜpy launcher + venvなのか？

#### 結論

```
Windows開発者にとって:

py launcher + venv = 黄金の組み合わせ

理由:
1. ✅ 標準性: Windows公式標準
2. ✅ 簡単性: 追加インストール不要
3. ✅ 柔軟性: 複数バージョン自在
4. ✅ 分離性: プロジェクト完全独立
5. ✅ AI対応: ML/DL開発も最適
6. ✅ 互換性: Mac開発者と共存可能
```

#### 実例で理解

**シナリオ: 3つのプロジェクトを担当**

```powershell
# お客様A: Python 3.11 + Django 4.2
C:\Projects\客A\
  └─ project-a\
      ├─ .python-version (3.11)
      └─ .venv\ (Django==4.2)

# お客様B: Python 3.12 + Django 5.0
C:\Projects\客B\
  └─ project-b\
      ├─ .python-version (3.12)
      └─ .venv\ (Django==5.0)

# 自分: Python 3.12 + FastAPI
C:\Projects\my\
  └─ my-api\
      └─ .venv\ (FastAPI==0.109)

# 完全に独立！干渉ゼロ！
```

**日常の切り替え:**

```powershell
# 午前: お客様Aのプロジェクト
cd C:\Projects\客A\project-a
.venv\Scripts\activate
python --version
# → Python 3.11.x
pip list
# → Django 4.2

# 午後: お客様Bのプロジェクト  
cd C:\Projects\客B\project-b
.venv\Scripts\activate
python --version
# → Python 3.12.x
pip list
# → Django 5.0

# シームレス！
```

#### Mac開発者との共存

**チーム開発での共通言語:**

```
Mac開発者:
  pyenv + venv + requirements.txt

Windows開発者:
  py launcher + venv + requirements.txt

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

## Windows (PowerShell)
```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Windows (Command Prompt)
```cmd
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```
```

---

### 3. 完成イメージ

#### フォルダ構造

```
C:\Users\あなた\
├─ AppData\
│  └─ Local\
│     └─ Programs\
│        └─ Python\           # Pythonインストール先
│           ├─ Python311\
│           └─ Python312\
│
└─ Projects\                  # プロジェクト置き場
   ├─ 客A\
   │  └─ project-a\
   │     ├─ .python-version   # 3.11
   │     ├─ .venv\            # 仮想環境
   │     ├─ .gitignore
   │     ├─ requirements.txt
   │     └─ (ソースコード)
   │
   ├─ 客B\
   │  └─ project-b\
   │     ├─ .python-version   # 3.12
   │     ├─ .venv\
   │     ├─ requirements.txt
   │     └─ (ソースコード)
   │
   └─ my\
      └─ my-project\
          ├─ .venv\
          ├─ requirements.txt
          └─ (ソースコード)
```

#### 完成後にできること

```powershell
# ✅ 複数Pythonバージョン管理
py -0
# -V:3.11 *        Python 3.11.x (64-bit)
# -V:3.12          Python 3.12.x (64-bit)

# ✅ プロジェクトごとにバージョン切り替え
cd project-a
py --version
# Python 3.11.x

cd ..\project-b
py --version  
# Python 3.12.x

# ✅ パッケージ完全分離
cd project-a
.venv\Scripts\activate
pip list
# Django 4.2

cd ..\project-b
.venv\Scripts\activate
pip list
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
| 🌍 **どこでもOK** | 任意 | `py --version` |
| 📁 **プロジェクト内** | プロジェクトフォルダ | `.venv\Scripts\activate` |
| 🏠 **ホーム推奨** | `C:\Users\あなた\` | `mkdir Projects` |

#### 再実行影響

| マーク | 影響 | 例 |
|--------|------|-----|
| 🟢 **OK** | 何度でも | Pythonインストール |
| 🟡 **注意** | 重複 | PATH設定 |
| 🔴 **NG** | 1回のみ | `py -m venv .venv` |

#### シェル表記

```powershell
# PowerShell用コマンド
Get-Command python

# Command Prompt用コマンド
where python

# 両方で使えるコマンド
py --version
```

---

### 5. Windows版の特徴

#### Mac版との主な違い

| 項目 | Windows | Mac/Linux |
|------|---------|-----------|
| **標準ツール** | py launcher | pyenv |
| **インストール元** | python.org公式 | Homebrew |
| **venv有効化** | `.venv\Scripts\activate` | `source .venv/bin/activate` |
| **パス区切り** | `\` (バックスラッシュ) | `/` (スラッシュ) |
| **シェル** | PowerShell / Command Prompt | bash / zsh |
| **システムPython** | なし（自分でインストール） | プリインストール有 |

#### PowerShell vs Command Prompt

**推奨: PowerShell**

| 機能 | PowerShell | Command Prompt |
|------|-----------|----------------|
| **モダン度** | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **機能** | 豊富 | 基本的 |
| **スクリプト** | 強力 | 制限あり |
| **カラー出力** | ✅ | 限定的 |
| **推奨度** | ✅ | △ |

**このガイドでは:**
- メインコマンド: 両方で動作
- 特殊コマンド: PowerShell版とCmd版を併記

---

### 6. ARM64特有の注意事項

#### ARM64版Windowsとは？

```
ARM64版Windows:
- Windows 11 on ARM
- Surface Pro X
- Snapdragon搭載PC
- 一部の新型デバイス

特徴:
- 省電力
- 長時間バッテリー
- x64エミュレーション機能搭載
```

#### システムアーキテクチャの確認

```powershell
# PowerShell
$env:PROCESSOR_ARCHITECTURE
# ARM64 → ARM64版
# AMD64 → x64版

# または
systeminfo | findstr /C:"System Type"
# ARM64-based PC → ARM64版
# x64-based PC → x64版
```

#### Pythonのサポート状況

**✅ Python 3.11以降: ARM64ネイティブサポート**

| バージョン | ARM64サポート | 推奨度 |
|-----------|-------------|--------|
| Python 3.13 | ✅ ネイティブ | ⭐⭐⭐⭐⭐ |
| Python 3.12 | ✅ ネイティブ | ⭐⭐⭐⭐⭐ |
| Python 3.11 | ✅ ネイティブ | ⭐⭐⭐⭐⭐ |
| Python 3.10 | ⚠️ x64エミュレーション | ⭐⭐⭐ |
| Python 3.9以前 | ⚠️ x64エミュレーション | ⭐⭐ |

**推奨: Python 3.12以降**

#### インストーラーの選択（ARM64版Windows）

**python.orgダウンロードページ:**

```
ダウンロードページに表示:
- Windows installer (64-bit)  ← これはx64版
- Windows installer (ARM64)   ← ARM64版はこれ！

重要:
✅ Python 3.11以降: ARM64版を選択
⚠️ Python 3.10以前: x64版のみ（エミュレーションで動作）
```

**確認コマンド:**

```powershell
# インストール後、確認
py --version
python -c "import platform; print(platform.machine())"

# ARM64ネイティブの場合:
# ARM64

# x64エミュレーションの場合:
# AMD64
```

#### ARM64での制限事項

**1. 一部パッケージの互換性**

```
問題が出やすいパッケージ:
⚠️ numpy (古いバージョン)
⚠️ scipy
⚠️ TensorFlow (古いバージョン)
⚠️ PyTorch (古いバージョン)
⚠️ コンパイルが必要なパッケージ

解決策:
1. 最新バージョンを使う（ほとんど解決）
2. ホイール(.whl)が提供されているパッケージを選ぶ
3. x64版Pythonを使う（エミュレーション）
```

**2. パッケージインストール時の注意**

```powershell
# ARM64で問題が出た場合
pip install パッケージ名
# エラー: building wheel failed...

# 解決策1: 最新版を試す
pip install --upgrade パッケージ名

# 解決策2: プレリリース版を試す
pip install --pre パッケージ名

# 解決策3: 別のパッケージを使う
# 例: tensorflow → tensorflow-cpu
```

**3. x64版Pythonの併用（万が一の時）**

```powershell
# ARM64版Python 3.12 (メイン)
py -3.12-arm64 -m venv .venv

# x64版Python 3.12 (エミュレーション・互換性のため)
py -3.12-64 -m venv .venv-x64

# プロジェクトで使い分け
```

#### ARM64推奨パッケージバージョン

**2025年1月時点で安定:**

```txt
# 完全ARM64対応
numpy>=1.26.0
pandas>=2.1.0
matplotlib>=3.8.0
scikit-learn>=1.3.0

# AI/MLライブラリ
torch>=2.1.0         # PyTorch ARM64対応
tensorflow>=2.15.0   # TensorFlow ARM64対応

# Web開発
django>=5.0
fastapi>=0.109.0
flask>=3.0.0

# すべて問題なし！
```

#### パフォーマンス

```
ARM64ネイティブ実行:
✅ 省電力
✅ 発熱少ない
✅ バッテリー長持ち
⚠️ x64より少し遅い場合も（パッケージによる）

x64エミュレーション:
⚠️ 消費電力増
⚠️ 速度低下
✅ 互換性高い

推奨:
可能な限りARM64ネイティブ！
```

#### トラブルシューティングフローチャート（ARM64）

```
パッケージインストール失敗
        ↓
[Q1] ARM64ネイティブPython使用？
    NO → ARM64版Pythonをインストール
    YES ↓
        
[Q2] パッケージが最新版？
    NO → pip install --upgrade パッケージ名
    YES ↓
        
[Q3] ホイール(.whl)が提供されている？
    NO → ソースビルドが必要（別対処）
    YES ↓
        
[Q4] 代替パッケージがある？
    YES → 代替を試す
    NO ↓
        
[Q5] x64版Pythonで試す
    x64版Pythonインストール
    py -3.12-64 -m venv .venv
    → 成功？
    YES → x64版を使用（一時的）
    NO → [PART 6]へ
```

---

## PART 2: 基本環境構築

**⚠️ 重要な注意:**
この章では順番が重要です！
- 所要時間: 合計30分〜1時間
- ARM64版Windowsの方は[ARM64注意事項](#6-arm64特有の注意事項)を確認済みか確認

---

### 7. 現在の状態確認

#### チェックリスト

```powershell
# ✅ 前提条件確認

# 1. Windowsバージョン
winver
# Windows 11 または Windows 10 推奨

# 2. システムアーキテクチャ
$env:PROCESSOR_ARCHITECTURE
# AMD64 (x64版) または ARM64 (ARM64版)

# または
systeminfo | findstr /C:"System Type"

# 3. Git設定済みか？
git --version
git config --global user.name
git config --global user.email

# 4. VSCode設置済みか？
code --version

# 5. Docker設定済みか？（任意）
docker --version

# 6. GitHub SSH接続済みか？
ssh -T git@github.com
# Hi username! と表示されればOK
```

**すべてOK？ → 次へ進む**

**NGがある？ → 該当部分を先に設定**

---

### 8. Python公式インストール

#### ステップ8-1: ダウンロード

✅ **必須**  
📍 🌍 どこでもOK

**1. 公式サイトにアクセス:**

```
https://www.python.org/downloads/
```

**2. バージョン選択:**

**【x64版Windows】**
```
推奨バージョン:
✅ Python 3.12.x (最新安定版)
✅ Python 3.11.x (互換性重視)

クリック:
"Download Python 3.12.x" ボタン
→ Windows installer (64-bit) を選択
```

**【ARM64版Windows】🎯 重要！**
```
推奨バージョン:
✅ Python 3.12.x (最新・ARM64ネイティブ)
✅ Python 3.11.x (ARM64ネイティブ)

重要:
"Windows installer (ARM64)" を選択！
"Windows installer (64-bit)" はx64版です！

ダウンロードページの下部:
"Looking for a specific release?"
→ Python 3.12.x
→ Scroll down
→ "Windows installer (ARM64)" をダウンロード
```

**ファイル名例:**
```
x64版: python-3.12.1-amd64.exe
ARM64版: python-3.12.1-arm64.exe
```

---

#### ステップ8-2: Python 3.12インストール

✅ **必須**  
🔄 🟢 既にあれば上書き/追加

**インストーラー起動:**

**1. ダウンロードしたファイルをダブルクリック**

**2. ⚠️ 超重要チェックボックス（画面下部）:**
```
✅ Install launcher for all users (recommended)
✅ Add python.exe to PATH

この2つに必ずチェック！
```

**💡 なぜ重要？**
```
Install launcher for all users:
→ py launcherインストール（Windows最強ツール）

Add python.exe to PATH:
→ どこからでもpythonコマンド実行可能
```

**3. クリック: "Install Now"**

**4. UAC（ユーザーアカウント制御）:**
```
「このアプリがデバイスに変更を加えることを許可しますか？」
→ 「はい」をクリック
```

**5. インストール中:**
```
Setup Progress
Installing:
- pip
- pip documentation
- Python launcher
...
（2〜3分）
```

**6. 完了画面:**
```
Setup was successful

✅ "Disable path length limit" をクリック（推奨）

理由: Windowsのパス長制限（260文字）を解除
深い階層のプロジェクトでエラー防止
```

**7. "Close" をクリック**

**⏰ 所要時間: 3-5分**

---

#### ステップ8-3: Python 3.11インストール（任意）

🔶 **推奨**（複数バージョン管理のため）

**手順: ステップ8-2と同じ**

**ダウンロード:**
- **x64版:** python-3.11.x-amd64.exe
- **ARM64版:** python-3.11.x-arm64.exe

**インストール時のチェック:**
```
✅ Install launcher for all users
✅ Add python.exe to PATH

同じくチェック！
```

**💡 複数バージョンインストール可能:**
```
C:\Users\あなた\AppData\Local\Programs\Python\
├─ Python311\
└─ Python312\

すべて共存！py launcherが管理！
```

---

#### ステップ8-4: インストール確認

✅ **必須**

**新しいPowerShellを開く:**
```
重要: インストール前に開いていたPowerShellは閉じる
新しくPowerShellを起動
```

**確認コマンド:**

```powershell
# py launcher確認
py --version
# Python 3.12.x

# インストール済みPython一覧
py -0
# 表示例:
# -V:3.12 *        Python 3.12.1 (64-bit)
# -V:3.11          Python 3.11.7 (64-bit)
# * = デフォルト

# ARM64版の確認（ARM64 Windowsのみ）
python -c "import platform; print(platform.machine())"
# ARM64 → ネイティブ
# AMD64 → x64またはエミュレーション
```

**✅ 成功の表示:**
```
py --version
Python 3.12.1

py -0
 -V:3.12 *        Python 3.12.1 (64-bit)
 -V:3.11          Python 3.11.7 (64-bit)
```

**❌ エラーが出た場合:**

```powershell
# エラー: py is not recognized...

# 対処1: PowerShell再起動
# 完全に閉じて再起動

# 対処2: PATH確認
$env:PATH -split ';' | Select-String "Python"

# 対処3: 再インストール
# Python公式インストーラーを再実行
# ✅ Add python.exe to PATH に必ずチェック
```

---

#### ステップ8-5: pip確認・更新

✅ **必須**

```powershell
# pip確認
py -m pip --version
# pip 23.x.x from C:\Users\あなた\AppData\Local\Programs\Python\Python312\...

# pip更新（重要！）
py -m pip install --upgrade pip

# ✅ 成功:
# Successfully installed pip-24.0
```

**💡 なぜ `py -m pip`？**
```
python -m pip  ❌ どのPythonか不明確
py -m pip      ✅ py launcherが管理
py -3.12 -m pip ✅ バージョン明示
```

---

### 9. py launcherの使い方

#### 基本コマンド

**1. デフォルトPython実行:**
```powershell
py
# >>> (Pythonインタプリタ起動)
# exit() で終了
```

**2. バージョン指定実行:**
```powershell
# Python 3.12実行
py -3.12

# Python 3.11実行
py -3.11

# スクリプト実行
py -3.12 script.py
```

**3. インストール済み一覧:**
```powershell
py -0
# -V:3.12 *        Python 3.12.1 (64-bit)
# -V:3.11          Python 3.11.7 (64-bit)
```

**4. pip操作:**
```powershell
# デフォルトバージョンのpip
py -m pip list

# 特定バージョンのpip
py -3.12 -m pip list
py -3.11 -m pip list

# パッケージインストール
py -3.12 -m pip install requests
```

#### .python-versionファイル（任意）

**プロジェクトのデフォルトバージョン指定:**

```powershell
# プロジェクトフォルダで
cd C:\Projects\my-project

# .python-versionファイル作成
echo 3.12 > .python-version

# このフォルダでpyコマンド実行すると自動的に3.12を使用
py --version
# Python 3.12.x
```

**💡 Mac pyenvとの互換性:**
```
Mac:
pyenv local 3.12.1
→ .python-version作成

Windows:
echo 3.12 > .python-version
→ py launcherが自動認識

チーム開発で統一！
```

---

### 10. venv使い方

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
│ プロジェクトA: .venv\        │
│   └─ Django 4.2             │
│ プロジェクトB: .venv\        │
│   └─ Django 5.0             │
│ → 完全に独立！               │
└─────────────────────────────┘
```

#### 基本コマンド4つ

**1. 作成**

✅ **必須**  
📍 📁 プロジェクト内  
🔄 🔴 再実行で初期化（注意）

```powershell
# PowerShell / Command Prompt 共通
py -m venv .venv

# 特定バージョン指定
py -3.12 -m venv .venv
py -3.11 -m venv .venv
```

**コマンド詳細:**
```
py -m venv .venv
│  │  │    └─ フォルダ名（推奨: .venv）
│  │  └─ モジュール名
│  └─ モジュール実行オプション
└─ py launcher実行
```

**⚠️ 重要: 再実行すると？**
```powershell
# 初回
py -m venv .venv
pip install django
pip list
# Django表示

# 誤って再実行
py -m venv .venv
pip list
# Djangoが消えている！
```

**💡 だからrequirements.txt重要！**

---

**2. 有効化**

✅ **必須**  
📍 📁 `.venv`があるフォルダ  
🔄 🟢 何度でもOK

**【PowerShell】推奨**
```powershell
.venv\Scripts\Activate.ps1

# または
.\.venv\Scripts\Activate.ps1
```

**成功すると:**
```powershell
(.venv) PS C:\Projects\my-project>
└──┬──┘
   └─ 有効化されている印
```

**⚠️ 実行ポリシーエラーが出た場合:**

```powershell
# エラー: cannot be loaded because running scripts is disabled...

# 対処: 実行ポリシー変更（初回のみ）
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 確認
Get-ExecutionPolicy
# RemoteSigned

# 再度有効化
.venv\Scripts\Activate.ps1
```

**【Command Prompt】**
```cmd
.venv\Scripts\activate.bat

# または
.venv\Scripts\activate
```

**成功すると:**
```cmd
(.venv) C:\Projects\my-project>
```

---

**3. 無効化**

⭐ **任意**

```powershell
# PowerShell / Command Prompt 共通
deactivate
```

**プロンプトが元に戻る:**
```powershell
PS C:\Projects\my-project>
# (.venv) が消える
```

---

**4. 削除**

⭐ **任意**（やり直したい時）

```powershell
# 無効化
deactivate

# フォルダ削除
Remove-Item -Recurse -Force .venv

# または Explorerから削除

# 再作成
py -m venv .venv
```

---

#### 実践練習

```powershell
# 練習フォルダ作成
mkdir C:\Users\$env:USERNAME\python-test
cd C:\Users\$env:USERNAME\python-test

# 仮想環境作成
py -m venv .venv

# 確認
dir
# .venv ディレクトリ表示

# 有効化（PowerShell）
.venv\Scripts\Activate.ps1

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
cd ..
Remove-Item -Recurse -Force python-test
```

**🎉 venv理解完了！**

---

### 11. pyenv-winインストール（任意）

⭐ **任意** - Mac/Linux開発者とコマンド統一したい場合

#### pyenv-winとは？

```
pyenv-win:
- MacのpyenvのWindows移植版
- CLI統一
- より高度なバージョン管理

推奨する人:
✅ Mac/Linuxと環境を統一したい
✅ より細かいバージョン管理が必要
✅ チームでpyenvを使っている

推奨しない人:
❌ Windows初心者
❌ py launcherで十分
❌ シンプルが好き

結論:
ほとんどの人は py launcher で十分！
```

#### インストール手順（PowerShell）

```powershell
# 1. Git for Windowsが必要
git --version

# 2. pyenv-winインストール
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "$env:TEMP\install-pyenv-win.ps1"; &"$env:TEMP\install-pyenv-win.ps1"

# 3. PowerShell再起動

# 4. 確認
pyenv --version
# pyenv 3.x.x

# 5. Pythonインストール
pyenv install --list
pyenv install 3.12.1
pyenv install 3.11.7

# 6. グローバル設定
pyenv global 3.12.1

# 7. 確認
python --version
# Python 3.12.1
```

#### pyenv-win基本コマンド

```powershell
# インストール可能一覧
pyenv install --list

# Pythonインストール
pyenv install 3.12.1

# インストール済み一覧
pyenv versions

# グローバル設定
pyenv global 3.12.1

# ローカル設定（プロジェクト）
pyenv local 3.11.7

# 確認
python --version
```

**💡 py launcherとの併用も可能！**

---

## PART 3: VSCode統合

### 12. VSCode Python設定

#### ステップ12-1: 拡張機能インストール

✅ **必須**

**手順:**
1. VSCode起動
2. 左サイドバー「拡張機能」（`Ctrl + Shift + X`）
3. 検索: `Python`
4. **Python** (Microsoft) を選択
5. 「インストール」クリック

**同時インストール:**
- Pylance（言語サーバー）
- Python Debugger

---

#### ステップ12-2: インタープリター選択

✅ **必須**（プロジェクトごと）

**方法1: コマンドパレット**
```
Ctrl + Shift + P
→ "Python: Select Interpreter"
→ Python 3.12.x を選択
```

**方法2: ステータスバー**
```
右下のPythonバージョン表示クリック
→ リストから選択
```

**方法3: 仮想環境を認識**
```
プロジェクトで .venv\ 作成後
VSCodeが自動で検出
→ 右下に表示
```

---

#### ステップ12-3: 仮想環境自動認識

✅ **必須**

**settings.json:**
```
Ctrl + Shift + P
→ "Preferences: Open User Settings (JSON)"
```

**追加:**
```json
{
  "python.terminal.activateEnvironment": true,
  "python.defaultInterpreterPath": "py",
  "python.analysis.typeCheckingMode": "basic",
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.venv": false
  },
  "terminal.integrated.defaultProfile.windows": "PowerShell"
}
```

**💡 設定の意味:**
```json
"python.terminal.activateEnvironment": true
// → ターミナル開くと自動でvenv有効化

"python.defaultInterpreterPath": "py"
// → py launcherを使用

"terminal.integrated.defaultProfile.windows": "PowerShell"
// → PowerShellをデフォルトに
```

---

#### ステップ12-4: PowerShell実行ポリシー設定（重要）

✅ **必須**（初回のみ）

**VSCode統合ターミナルで:**

```powershell
# 実行ポリシー確認
Get-ExecutionPolicy

# Restricted の場合は変更
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 確認
Get-ExecutionPolicy
# RemoteSigned
```

**これで venv自動有効化が動作！**

---

#### ステップ12-5: 動作確認

⭐ **任意**

**test.py作成:**
```python
print("Hello, Python on Windows!")
import platform
print(f"Architecture: {platform.machine()}")
print(f"Python: {platform.python_version()}")
```

**実行方法:**
- **方法1:** 右上▶️ボタン
- **方法2:** 右クリック →「Run Python File」
- **方法3:** ターミナルで `python test.py`

**✅ 出力（x64版）:**
```
Hello, Python on Windows!
Architecture: AMD64
Python: 3.12.1
```

**✅ 出力（ARM64版）:**
```
Hello, Python on Windows!
Architecture: ARM64
Python: 3.12.1
```

**🎉 VSCode設定完了！**

---

## PART 4: 実践プロジェクト

### 13. 新規プロジェクト作成

#### シナリオ: Djangoブログアプリ

**完全手順:**

```powershell
# ステップ1: フォルダ作成
mkdir C:\Projects\my-blog
cd C:\Projects\my-blog

# ステップ2: Pythonバージョン指定（任意）
echo 3.12 > .python-version

# 確認
type .python-version
# 3.12

# ステップ3: 仮想環境作成
py -3.12 -m venv .venv

# ステップ4: 有効化
.venv\Scripts\Activate.ps1

# プロンプト確認
# (.venv) が表示される

# ステップ5: pip更新
python -m pip install --upgrade pip

# ステップ6: Django install
pip install django

# ステップ7: プロジェクト作成
django-admin startproject config .

# フォルダ構造確認
tree /F
# .
# ├── .python-version
# ├── .venv\
# ├── config\
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
@"
.venv\
__pycache__\
*.py[cod]
*.sqlite3
.DS_Store
"@ | Out-File -FilePath .gitignore -Encoding utf8

# ステップ13: Git初期化
git init
git add .
git commit -m "Initial commit"

# ステップ14: VSCodeで開く
code .
```

**完成！🎉**

---

### 14. 既存プロジェクトクローン

#### シナリオ: GitHubからクローン

```powershell
# ステップ1: クローン
cd C:\Projects
git clone git@github.com:client/project.git
cd project

# ステップ2: README確認
type README.md
# → Python 3.11必要と記載

# ステップ3: Python 3.11確認
py -3.11 --version
# なければインストール

# ステップ4: 仮想環境作成
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1

# ステップ5: 依存パッケージインストール
python -m pip install --upgrade pip
pip install -r requirements.txt

# ステップ6: 環境変数設定（必要なら）
copy .env.example .env
# .envを編集（Notepad++やVSCode）

# ステップ7: データベース設定
python manage.py migrate

# ステップ8: 起動
python manage.py runserver

# ステップ9: VSCodeで開く
code .
```

**完了！🎉**

---

### 15. requirements.txt管理

#### 作成

✅ **必須**（プロジェクト完成時）

```powershell
# 仮想環境有効化状態で
pip freeze > requirements.txt
```

**内容確認:**
```powershell
type requirements.txt
```

**例:**
```
asgiref==3.7.2
Django==5.0.1
sqlparse==0.4.4
```

---

#### インストール

✅ **必須**（新環境セットアップ時）

```powershell
pip install -r requirements.txt
```

---

#### 更新

✅ **必須**（新パッケージ追加時）

```powershell
# 1. パッケージインストール
pip install 新パッケージ

# 2. requirements.txt更新
pip freeze > requirements.txt

# 3. Git commit
git add requirements.txt
git commit -m "Add 新パッケージ"
git push
```

---

#### ベストプラクティス

**シンプル版（推奨）:**
```txt
Django==5.0.1
requests==2.31.0
python-dotenv==1.0.0
```

**完全版（本番環境）:**
```powershell
pip freeze > requirements.txt
```

**分割管理（大規模）:**
```
requirements\
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
```powershell
# 開発環境
pip install -r requirements\dev.txt

# 本番環境
pip install -r requirements\prod.txt
```

---

## PART 5: AI/生成AI開発

### 16. AI開発環境

#### 基本セットアップ

```powershell
# プロジェクト作成
mkdir C:\Projects\ai-project
cd C:\Projects\ai-project

# Python 3.12（最新推奨）
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1

# 基本ライブラリ
python -m pip install --upgrade pip
pip install numpy pandas matplotlib scikit-learn jupyter
```

---

#### Windows特有の注意事項

**1. ビルドツールが必要な場合**

一部のパッケージ（特に古いバージョン）はコンパイルが必要：

```powershell
# エラー例:
# error: Microsoft Visual C++ 14.0 or greater is required

# 解決策: Microsoft C++ Build Toolsインストール
# https://visualstudio.microsoft.com/visual-cpp-build-tools/

# または
# Visual Studio Installerで
# "C++によるデスクトップ開発" をインストール
```

**💡 2025年時点では、ほとんどのパッケージはホイール(.whl)提供**

---

#### ARM64での注意

**✅ 最新バージョン使用で問題なし:**

```powershell
# ARM64で推奨バージョン
pip install numpy>=1.26.0
pip install pandas>=2.1.0
pip install scikit-learn>=1.3.0

# すべてARM64ネイティブ対応！
```

**⚠️ 古いバージョンで問題が出る場合:**

```powershell
# 解決策1: 最新版に更新
pip install --upgrade パッケージ名

# 解決策2: ホイール版を指定
pip install パッケージ名 --only-binary :all:

# 解決策3: x64版Python使用（エミュレーション）
# Python x64版をインストール
py -3.12-64 -m venv .venv-x64
```

---

#### Jupyter Notebook

🔶 **推奨**

```powershell
# インストール
pip install jupyter

# 起動
jupyter notebook

# ブラウザが自動で開く
```

---

#### TensorFlow

⭐ **任意**（DL開発時）

**【x64版Windows】**

```powershell
# TensorFlow (GPU対応はCUDA/cuDNN必要)
pip install tensorflow

# CPU版のみ
pip install tensorflow-cpu
```

**【ARM64版Windows】🎯**

```powershell
# ARM64版はDirectML backend使用（推奨）
pip install tensorflow-cpu
pip install tensorflow-directml-plugin

# または最新版
pip install tensorflow>=2.15.0
```

**確認:**
```python
import tensorflow as tf
print(tf.__version__)
print("GPU:", tf.config.list_physical_devices('GPU'))
```

---

#### PyTorch

⭐ **任意**（DL開発時）

**【x64版Windows】**

```powershell
# PyTorch公式で最新コマンド確認
# https://pytorch.org/get-started/locally/

# CPU版
pip install torch torchvision torchaudio

# GPU版（CUDA 11.8）
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**【ARM64版Windows】🎯**

```powershell
# ARM64ネイティブサポート（PyTorch 2.0以降）
pip install torch torchvision torchaudio

# 確認
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'Architecture: {torch.__config__.show()}')"
```

**確認:**
```python
import torch
print(torch.__version__)
print("CUDA:", torch.cuda.is_available())
```

---

#### OpenAI API

⭐ **任意**（生成AI開発時）

```powershell
# インストール
pip install openai python-dotenv
```

**.env作成:**
```powershell
@"
OPENAI_API_KEY=your-api-key-here
"@ | Out-File -FilePath .env -Encoding utf8
```

**.gitignore追加:**
```powershell
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

---

#### LangChain

⭐ **任意**（LLMアプリ開発時）

```powershell
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

---

#### AI開発用requirements.txt例

**【x64版Windows】**
```txt
# データサイエンス
numpy==1.26.2
pandas==2.1.4
matplotlib==3.8.2
scikit-learn==1.3.2

# Jupyter
jupyter==1.0.0

# ディープラーニング（選択）
tensorflow==2.15.0
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

**【ARM64版Windows】**
```txt
# データサイエンス（ARM64ネイティブ）
numpy>=1.26.0
pandas>=2.1.0
matplotlib>=3.8.0
scikit-learn>=1.3.0

# Jupyter
jupyter>=1.0.0

# ディープラーニング（ARM64対応）
tensorflow>=2.15.0
tensorflow-directml-plugin>=0.4.0
# または
torch>=2.1.0
torchvision>=0.16.0
torchaudio>=2.1.0

# 生成AI
openai>=1.6.0
langchain>=0.1.0
langchain-openai>=0.0.2
python-dotenv>=1.0.0
```

---

## PART 6: トラブルシューティング

### 17. エラー解決

#### エラー1: py is not recognized

**症状:**
```powershell
py --version
# 'py' is not recognized as an internal or external command...
```

**解決策:**

**1. PowerShell再起動:**
```powershell
# 完全に閉じて再起動
```

**2. Python再インストール:**
```
✅ Install launcher for all users
✅ Add python.exe to PATH
両方チェック！
```

**3. PATH確認:**
```powershell
$env:PATH -split ';' | Select-String "Python"

# 表示されるべきパス:
# C:\Users\あなた\AppData\Local\Programs\Python\Python312\
# C:\Users\あなた\AppData\Local\Programs\Python\Python312\Scripts\
# C:\Users\あなた\AppData\Local\Programs\Python\Launcher\
```

**4. 手動PATH追加:**
```
Windows設定
→ システム
→ バージョン情報
→ システムの詳細設定
→ 環境変数
→ ユーザー環境変数 PATH に追加:
  C:\Users\あなた\AppData\Local\Programs\Python\Launcher\
```

---

#### エラー2: スクリプト実行が無効

**症状:**
```powershell
.venv\Scripts\Activate.ps1
# cannot be loaded because running scripts is disabled on this system
```

**解決策:**

```powershell
# 実行ポリシー確認
Get-ExecutionPolicy
# Restricted

# 変更（CurrentUserスコープ推奨）
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 確認
Get-ExecutionPolicy
# RemoteSigned

# 再度有効化
.venv\Scripts\Activate.ps1
```

**💡 セキュリティ:**
```
Restricted:   すべて禁止（デフォルト）
RemoteSigned: ローカルは許可、リモートは署名必要（推奨）
Unrestricted: すべて許可（非推奨）
```

---

#### エラー3: Permission denied (pip install)

**症状:**
```powershell
pip install django
# ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied
```

**原因と解決:**

**原因1: 管理者権限不要なのに使っている**
```powershell
# ❌ 管理者PowerShellで実行（非推奨）
# ✅ 通常PowerShellで実行

# 仮想環境使用
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install django
```

**原因2: グローバルにインストールしようとしている**
```powershell
# ❌ これは権限エラーになる
pip install django  # グローバル

# ✅ 仮想環境で
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install django
```

**原因3: ウイルス対策ソフトの干渉**
```
Windows Defenderが干渉している場合:
- 一時的に無効化
- または Python インストールフォルダを除外設定
```

---

#### エラー4: Microsoft Visual C++ 14.0 required

**症状:**
```powershell
pip install 古いパッケージ
# error: Microsoft Visual C++ 14.0 or greater is required
```

**解決策:**

**解決策1: ホイール版を使う（推奨）**
```powershell
# ホイール版(.whl)をインストール
pip install パッケージ名 --only-binary :all:

# 最新版に更新（ホイール提供される可能性）
pip install --upgrade パッケージ名
```

**解決策2: Build Toolsインストール**
```
1. ダウンロード:
   https://visualstudio.microsoft.com/visual-cpp-build-tools/

2. インストール
   "C++によるデスクトップ開発" を選択
   
3. 再起動後、pip install再試行
```

**⏰ 所要時間: 10-15分（Build Tools）**

---

#### エラー5: ModuleNotFoundError

**症状:**
```python
import requests
# ModuleNotFoundError: No module named 'requests'
```

**解決策:**

**1. 仮想環境が有効か確認:**
```powershell
# プロンプトに (.venv) があるか
(.venv) PS C:\Projects\my-project>

# なければ有効化
.venv\Scripts\Activate.ps1
```

**2. パッケージインストール:**
```powershell
pip install requests
```

**3. インタープリター確認（VSCode）:**
```
Ctrl + Shift + P
→ Python: Select Interpreter
→ .venv のPythonを選択
```

---

#### エラー6: VSCode仮想環境認識しない

**解決策:**

**1. Python拡張機能再インストール:**
- 拡張機能 → Python → アンインストール
- VSCode再起動
- Python再インストール

**2. VSCode完全再起動:**
```
Alt + F4 で終了
再起動
```

**3. .venv フォルダの場所確認:**
```powershell
# プロジェクトルートに .venv があるか
dir

# .venv
# ↑ これが表示されるか
```

**4. settings.json確認:**
```json
{
  "python.terminal.activateEnvironment": true
}
```

---

#### エラー7: ARM64パッケージインストール失敗

**症状（ARM64版Windows）:**
```powershell
pip install 古いパッケージ
# ERROR: Could not build wheels for パッケージ
# Building wheel for パッケージ (setup.py) ... error
```

**解決策:**

**解決策1: 最新版を試す**
```powershell
# 最新版に更新
pip install --upgrade パッケージ名

# プレリリース版を試す
pip install --pre パッケージ名
```

**解決策2: ホイール版を探す**
```powershell
# ホイール版のみインストール
pip install パッケージ名 --only-binary :all:
```

**解決策3: 代替パッケージを使う**
```powershell
# 例: TensorFlow
pip install tensorflow-cpu
pip install tensorflow-directml-plugin
```

**解決策4: x64版Python使用（エミュレーション）**
```powershell
# Python x64版をインストール
# （python.orgから x64版ダウンロード）

# x64版で仮想環境作成
py -3.12-64 -m venv .venv-x64
.venv-x64\Scripts\Activate.ps1
pip install パッケージ名
```

---

#### エラー8: Long Path対応

**症状:**
```
FileNotFoundError: [Errno 2] No such file or directory:
'C:\\Users\\...\\非常に長いパス...\\ファイル名'
```

**原因:** Windows 260文字パス制限

**解決策:**

**方法1: インストール時に解除（推奨）**
```
Pythonインストール完了画面:
✅ "Disable path length limit" をクリック
```

**方法2: レジストリ編集**
```
1. Win + R → regedit
2. 移動:
   HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
3. LongPathsEnabled を 1 に変更
4. PC再起動
```

**方法3: プロジェクトを浅い場所に**
```powershell
# ❌ 深すぎる
C:\Users\あなた\Documents\work\projects\2025\client-a\python\web-app\backend\api\v1\...

# ✅ 浅くする
C:\Projects\client-a-api\
```

---

### 18. よくある質問

#### Q1: py launcher vs python コマンド

**A:**

| コマンド | 説明 | 推奨度 |
|---------|------|--------|
| `py` | py launcherが管理 | ⭐⭐⭐⭐⭐ |
| `py -3.12` | バージョン明示 | ⭐⭐⭐⭐⭐ |
| `python` | PATH最初のPython | ⚠️ |

**推奨: py launcher使用**

---

#### Q2: PowerShell vs Command Prompt

**A:**

| 項目 | PowerShell | Command Prompt |
|------|-----------|----------------|
| **推奨度** | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **モダン** | ✅ | ❌ |
| **機能** | 豊富 | 基本 |

**推奨: PowerShell**

---

#### Q3: Microsoft Store版使うべき？

**A:**

```
Microsoft Store版:
✅ 超初心者のお試しのみ
❌ 本格開発

公式python.org版:
✅ 本格開発
✅ 制限なし
✅ 全機能
```

**推奨: python.org公式版**

---

#### Q4: .venv vs venv どっち？

**A:** ただの名前の違い

```powershell
py -m venv .venv  # 推奨（隠しフォルダ）
py -m venv venv   # OK
py -m venv env    # OK
```

**推奨: `.venv`**（Python公式推奨）

---

#### Q5: グローバルにインストールOK？

**A:** ❌基本NG

**例外的にOK:**
- `pip`自体
- `jupyter`などの汎用ツール

**基本ルール:**
すべてのパッケージは仮想環境に！

---

#### Q6: 複数バージョン同時使用OK？

**A:** ✅OK！それがpy launcherの目的

```powershell
# プロジェクトAは3.11
cd project-a
py -3.11 --version  # Python 3.11.x

# プロジェクトBは3.12
cd ..\project-b
py -3.12 --version  # Python 3.12.x
```

---

#### Q7: 仮想環境削除方法は？

**A:**

```powershell
# 無効化
deactivate

# フォルダ削除
Remove-Item -Recurse -Force .venv

# 再作成
py -m venv .venv
```

**💡 ただのフォルダ！気軽に作り直せる**

---

#### Q8: Mac開発者との共存は？

**A:**

**共通言語: venv + requirements.txt**

```
Mac: pyenv + venv
Windows: py launcher + venv

共通: requirements.txt
```

**README記載で解決！**

---

#### Q9: ARM64版Windowsで何が違う？

**A:**

```
Python 3.12以降:
✅ ARM64ネイティブ動作
✅ 問題なし

注意点:
⚠️ 古いパッケージは問題出る可能性
✅ 最新版使えば解決

パフォーマンス:
✅ 省電力
✅ バッテリー長持ち
△ 一部処理はx64より遅い場合も
```

---

#### Q10: Anaconda使うべき？

**A:**

**Anaconda向き:**
- データサイエンス専門
- GUI管理好き

**py launcher + venv向き:**
- Web開発も
- シンプル好き
- 容量節約

**初心者推奨:**
py launcher + venvから始める

---

#### Q11: .venvをGitにcommit？

**A:** ❌絶対ダメ！

**.gitignore必須:**
```gitignore
.venv/
venv/
env/
__pycache__/
*.py[cod]
*.sqlite3
```

**代わりに:**
requirements.txt をcommit

---

#### Q12: Windowsパス区切りは？

**A:**

```powershell
# Windows
C:\Projects\my-project\.venv\Scripts\activate

# Mac/Linux
/Users/you/Projects/my-project/.venv/bin/activate

# Python内部は / も使える
path = "C:/Projects/my-project"  # OK
```

---

#### Q13: VSCodeターミナルが文字化け

**A:**

**PowerShell文字コード設定:**

```powershell
# VSCode settings.json
{
  "terminal.integrated.defaultProfile.windows": "PowerShell",
  "terminal.integrated.profiles.windows": {
    "PowerShell": {
      "source": "PowerShell",
      "args": ["-NoExit", "-Command", "chcp 65001"]
    }
  }
}
```

---

#### Q14: pyenv-win使うべき？

**A:**

**pyenv-win推奨:**
✅ Mac/Linuxとコマンド統一
✅ チームがpyenv使用

**py launcher推奨:**
✅ Windows標準
✅ シンプル
✅ 初心者

**初心者は:**
py launcherで十分！

---

#### Q15: 管理者権限必要？

**A:**

```
Pythonインストール:
△ 初回のみ（UAC承認）

日常開発:
❌ 不要

pip install:
❌ 不要（仮想環境内）

権限が必要と言われたら:
→ 仮想環境使っていないサイン
```

---

## 完成チェックリスト

### 基本環境

- [ ] Python 3.12インストール済み（`py --version`）
- [ ] Python 3.11インストール済み（`py -3.11 --version`）
- [ ] py launcher動作確認（`py -0`）
- [ ] pip動作確認（`py -m pip --version`）
- [ ] 実行ポリシー設定済み（PowerShell）
- [ ] **ARM64版は正しいアーキテクチャか確認**（`python -c "import platform; print(platform.machine())"`）

### VSCode

- [ ] Python拡張機能インストール済み
- [ ] インタープリター選択可能
- [ ] 仮想環境自動認識設定済み
- [ ] PowerShellがデフォルトターミナル

### 実践

- [ ] 仮想環境作成できる
- [ ] 仮想環境有効化できる（PowerShell）
- [ ] パッケージインストールできる
- [ ] requirements.txt作成できる

**全部✅ → 完璧！🎉**

---

## 次のステップ

### 初心者

1. **Python基礎学習**
   - 変数、関数、クラス
   - 公式チュートリアル

2. **フレームワーク学習**
   - Django/Flask
   - FastAPI

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

**Windows版の強み:**
- ✅ py launcher標準搭載（Mac pyenv相当）
- ✅ VSCode完全統合
- ✅ ARM64版も完全対応
- ✅ Mac開発者との共存可能

**この先:**
- 楽しく学ぶ
- たくさん作る
- エラーを恐れない
- コミュニティに参加

**Happy Coding on Windows! 🐍✨**

---

## ドキュメント情報

**バージョン:** 1.0 (Windows ARM64対応完全版)  
**最終更新:** 2025年1月  
**対象:** Windows 11/10 (x64/ARM64) + VSCode  
**前提:** Git・VSCode・Docker・GitHub SSH完了（任意）

**特徴:**
- ✅ x64版・ARM64版Windows完全対応
- ✅ PowerShell & Command Prompt両対応
- ✅ py launcher完全活用
- ✅ ARM64特有の注意事項完備
- ✅ Mac版と対応したREADME例

**目標:**
このガイドだけで100%完了

**Mac版との違い:**
- pyenv → py launcher（Windows標準）
- Homebrew → python.org公式インストーラー
- bash/zsh → PowerShell/Command Prompt
- パス区切り: `/` → `\`
- venv有効化コマンドの違い

**ARM64対応:**
- Python 3.11以降ARM64ネイティブサポート
- パッケージ互換性情報
- x64エミュレーション方法
- トラブルシューティング

**フィードバック歓迎！**

---

*このガイドがあなたのPython開発の旅を最高のスタートにしますように！*
