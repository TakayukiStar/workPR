# 🐍 Windows Python環境構築ガイド 2025

**【Windows 10/11 対応 - x64/ARM64完全サポート - 30分で完了】**

> **📌 このガイドの特徴**
> - ✅ シンプルで分かりやすい！30分で完了
> - ✅ すぐに実行できるコマンド形式
> - ✅ x64とARM64の両方に対応
> - ✅ トラブルシューティング完備
> - ✅ 2025年1月時点の最新情報

---

## 📑 クイックナビゲーション

## 📑 クイックナビゲーション

### 🎯 あなたの状況に合わせて選択

**今すぐ環境構築したい →** [STEP 2: Python公式インストール](#step-2-python公式インストール)

**ARM64 Windows（Surface Pro X等）→** [STEP 1: アーキテクチャ確認](#step-1-アーキテクチャ確認)

**エラーが出た →** [トラブルシューティング](#トラブルシューティング)

---

## 目次

1. [アーキテクチャ確認](#step-1-アーキテクチャ確認)
2. [Python公式インストール](#step-2-python公式インストール)
3. [pyenv-winインストール](#step-3-pyenv-winインストール)
4. [Pythonバージョン管理](#step-4-pythonバージョン管理)
5. [仮想環境（venv）の使い方](#step-5-仮想環境venvの使い方)
6. [プロジェクト実践](#step-6-プロジェクト実践)
7. [よく使うコマンド一覧](#よく使うコマンド一覧)
8. [トラブルシューティング](#トラブルシューティング)

---

## STEP 1: アーキテクチャ確認

#### 🎯 まず最初に！あなたのWindowsを確認

**なぜ重要？**
```
Windowsには2種類のアーキテクチャがあります:
1. x64 (AMD64) - 一般的なPC
2. ARM64 - Surface Pro X、Snapdragon搭載PC

ARM64の場合、Pythonインストール時に注意が必要です！
```

---

#### あなたのPCを確認

✅ **必須**  
📍 PowerShell / CMD / VSCodeターミナル

**実行場所の選択肢:**

**方法A: PowerShell（推奨）**
```
1. Windowsキー + X
2. 「Windows PowerShell」または「ターミナル」をクリック
```

**方法B: コマンドプロンプト（CMD）**
```
1. Windowsキー + R
2. 「cmd」と入力してEnter
```

**方法C: VSCode ターミナル**
```
1. VSCodeを起動
2. Ctrl + ` (バッククォート)
```

**方法D: 検索から**
```
1. Windowsキー
2. 「powershell」または「cmd」と入力
3. Enterキー
```

---

**コマンド実行:**

```powershell
$env:PROCESSOR_ARCHITECTURE
```

**✅ 表示パターン:**

**パターンA: x64（一般的なPC）**
```
AMD64
```

**パターンB: ARM64（Surface Pro X等）**
```
ARM64
```

---

#### 📊 判定結果

| 表示 | アーキテクチャ | 対応 | 備考 |
|------|-------------|------|------|
| **AMD64** | x64 | ✅完全対応 | 標準手順でOK |
| **ARM64** | ARM64 | ✅完全対応 | **Pythonインストール時に注意** |

**💡 この先の手順でアーキテクチャ別の指示があります！**

---

## STEP 2: Python公式インストール

#### ステップ2-1: ダウンロード

✅ **必須**

**1. ブラウザでアクセス:**
```
https://www.python.org/downloads/
```

**2. バージョン選択:**

2025年1月現在、以下のバージョンが推奨されます：

| バージョン | 推奨度 | 理由 |
|-----------|--------|------|
| **Python 3.13.x** | ⭐⭐⭐⭐⭐ | 最新の安定版・サポート期間長い |
| Python 3.14.x | ⭐⭐⭐ | 最新機能・まだ新しい |

**💡 このガイドでは Python 3.13.x を推奨します**

**3. ダウンロード:**

**ページ上部の大きな黄色いボタン:**
```
Download Python 3.13.x
```
をクリック

**💡 自動で Windows用のインストーラ（.exe）がダウンロードされます**

**ダウンロード先:**
```
通常: C:\Users\あなたのユーザー名\Downloads\
ファイル名: python-3.13.x-amd64.exe（x64の場合）
          python-3.13.x-arm64.exe（ARM64の場合）
```

---

#### ステップ2-2: インストール

✅ **必須**

**1. インストーラを起動:**

**方法A: エクスプローラーから**
```
1. Windowsキー + E でエクスプローラーを開く
2. 左側の「ダウンロード」をクリック
3. python-3.13.x-amd64.exe を探す
4. ダブルクリック
```

**方法B: ブラウザのダウンロードバーから**
```
1. ダウンロード完了後、ブラウザ下部に表示される
2. ファイル名をクリック
```

**方法C: 通知から**
```
1. ダウンロード完了後、Windows通知が表示される
2. 通知をクリック → 「開く」
```

---

**2. ⚠️ 超重要: チェックボックス設定**

インストーラが起動すると、以下の画面が表示されます：

```
┌─────────────────────────────────────┐
│ Install Python 3.13.x               │
├─────────────────────────────────────┤
│                                     │
│  ☐ Install launcher for all users  │
│  ☑ Add python.exe to PATH ← 必須！ │
│                                     │
│  ┌──────────────────────────────┐  │
│  │  Install Now                 │  │
│  │  (推奨) すべてのユーザー     │  │
│  └──────────────────────────────┘  │
│                                     │
│  Customize installation             │
│                                     │
└─────────────────────────────────────┘
```

**✅ 必ずチェック:**
```
☑ Add python.exe to PATH
```

**💡 このチェックを忘れると、後で手動でPATH設定が必要になります！**

---

**3. インストール実行:**

```
1. 画面下部の「Install Now」をクリック
2. ユーザーアカウント制御（UAC）が表示されたら「はい」をクリック
3. インストール進行中...
   - Setup Progress
   - Installing...
   - (青いプログレスバー)
4. 「Setup was successful」と表示されたら完了
5. 「Close」をクリック
```

**⏰ 所要時間: 3-5分**

---

#### ステップ2-3: 確認

✅ **必須**  
📍 PowerShell / CMD / VSCode ターミナル

**実行場所の選択肢:**

**方法A: PowerShell（推奨）**
```
1. Windowsキー + X
2. 「Windows PowerShell」または「ターミナル」をクリック
```

**方法B: コマンドプロンプト（CMD）**
```
1. Windowsキー + R
2. 「cmd」と入力してEnter
```

**方法C: VSCode ターミナル**
```
1. VSCodeを起動
2. Ctrl + ` (バッククォート)
3. または メニュー → ターミナル → 新しいターミナル
```

**方法D: 検索から**
```
1. Windowsキー
2. 「powershell」または「cmd」と入力
3. Enterキー
```

---

**確認コマンド実行:**

```powershell
python -V
```

**✅ 成功:**
```
Python 3.13.x
```

**詳細確認:**

```powershell
python -c "import sys; print(sys.executable)"
```

**✅ 表示例:**
```
C:\Users\あなた\AppData\Local\Programs\Python\Python313\python.exe
```

**💡 公式Pythonが正しくインストールされました！**

---

**❌ エラーが出た場合:**

**エラー1: `python` が認識されない**
```
'python' は、内部コマンドまたは外部コマンド...
```

**原因:**
- PATH にチェックを入れ忘れた
- PowerShell/CMDを再起動していない

**解決策:**
```
1. PowerShell/CMDを完全に閉じる
2. 新しくPowerShell/CMDを起動
3. 再度 python -V を実行
```

それでもダメなら → [トラブルシューティング](#エラー1-python-コマンドが見つからない)

---

**エラー2: Microsoft Store が起動する**
```
python と入力するとMicrosoft Storeが開く
```

**解決策:**
→ [トラブルシューティング](#エラー3-microsoft-store版pythonが邪魔)

---

## STEP 3: pyenv-winインストール

#### ステップ3-1: インストール

✅ **必須**  
📍 PowerShell / CMD / VSCodeターミナル

**実行場所:**
- **PowerShell** - Windowsキー + X → 「Windows PowerShell」
- **CMD** - Windowsキー + R → 「cmd」
- **VSCodeターミナル** - VSCode内で Ctrl + `
- **どこでもOK** - 上記のいずれかを開けばOK

**PowerShellで実行:**

```powershell
pip install pyenv-win --target %USERPROFILE%\.pyenv
```

**✅ 成功時の表示:**
```
Collecting pyenv-win
  Downloading pyenv_win-...
Installing collected packages: pyenv-win
Successfully installed pyenv-win
```

**⏰ 所要時間: 1-2分**

**💡 このコマンドの意味:**
```
pip install pyenv-win
└─ pipでpyenv-winをインストール

--target %USERPROFILE%\.pyenv
└─ C:\Users\あなた\.pyenv\ にインストール
```

---

#### ステップ3-2: 環境変数設定

✅ **必須**

**Windowsの環境変数設定画面を開く方法:**

**方法A: キーボードショートカット（最速）**
```
1. Windowsキー
2. 「環境変数」と入力
3. 「環境変数を編集」をクリック
4. または「システム環境変数の編集」をクリック
```

**方法B: 設定から**
```
1. Windowsキー + I（設定を開く）
2. 検索ボックスに「環境変数」と入力
3. 「環境変数を編集」をクリック
```

**方法C: コントロールパネルから**
```
1. Windowsキー + R
2. 「sysdm.cpl」と入力してEnter
3. 「詳細設定」タブ
4. 「環境変数」ボタンをクリック
```

---

**環境変数の設定手順:**

**画面構成:**
```
┌─────────────────────────────────────┐
│ 環境変数                            │
├─────────────────────────────────────┤
│ ユーザー環境変数 ← ここを設定      │
│ ┌─────────────────────────────────┐ │
│ │ 変数          値                │ │
│ │ PATH          C:\...            │ │
│ │ TEMP          ...               │ │
│ └─────────────────────────────────┘ │
│   [新規] [編集] [削除]              │
│                                     │
│ システム環境変数                    │
│ ┌─────────────────────────────────┐ │
│ │ （触らない）                    │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

**💡 上半分の「ユーザー環境変数」だけを編集します**

---

**1. PYENV 変数を追加:**

```
1. 「ユーザー環境変数」の「新規」ボタンをクリック
2. 以下を入力:
   変数名: PYENV
   変数値: %USERPROFILE%\.pyenv\pyenv-win
3. 「OK」をクリック
```

**2. PYENV_ROOT 変数を追加:**

```
1. 「ユーザー環境変数」の「新規」ボタンをクリック
2. 以下を入力:
   変数名: PYENV_ROOT
   変数値: %USERPROFILE%\.pyenv\pyenv-win
3. 「OK」をクリック
```

**3. PYENV_HOME 変数を追加:**

```
1. 「ユーザー環境変数」の「新規」ボタンをクリック
2. 以下を入力:
   変数名: PYENV_HOME
   変数値: %USERPROFILE%\.pyenv\pyenv-win
3. 「OK」をクリック
```

**💡 まとめ:**

| 変数名 | 変数値 |
|--------|--------|
| `PYENV` | `%USERPROFILE%\.pyenv\pyenv-win` |
| `PYENV_ROOT` | `%USERPROFILE%\.pyenv\pyenv-win` |
| `PYENV_HOME` | `%USERPROFILE%\.pyenv\pyenv-win` |

---

**4. PATH 変数を編集:**

**⚠️ 重要: PATHは「新規」ではなく「編集」です！**

```
1. 「ユーザー環境変数」で「Path」を探す
2. 「Path」を選択（クリック）
3. 「編集」ボタンをクリック
```

**新しいウィンドウが開きます:**

```
┌─────────────────────────────────────┐
│ 環境変数名の編集                    │
├─────────────────────────────────────┤
│ C:\...                              │
│ C:\...                              │
│ ...                                 │
│                                     │
│ [新規] [編集] [削除] [上へ] [下へ] │
└─────────────────────────────────────┘
```

```
5. 「新規」ボタンをクリック
6. 以下を追加（1行目）:
   %USERPROFILE%\.pyenv\pyenv-win\bin
   
7. もう一度「新規」ボタンをクリック
8. 以下を追加（2行目）:
   %USERPROFILE%\.pyenv\pyenv-win\shims
   
9. 追加した2行を一番上に移動:
   - 追加した行を選択
   - 「上へ」ボタンを何度もクリック
   - 一番上まで移動
   
10. 「OK」をクリック
```

**💡 重要: 既存のPythonより優先するため、先頭に配置！**

---

**5. すべて保存:**

```
1. 環境変数ウィンドウで「OK」をクリック
2. システムのプロパティウィンドウで「OK」をクリック
```

---

#### ステップ3-3: 確認

✅ **必須**

**PowerShellを再起動してから:**

```powershell
pyenv --version
```

**✅ 成功:**
```
pyenv 3.1.1
```

**🎉 pyenv-win完了！**

---

## STEP 4: Pythonバージョン管理

#### 利用可能なバージョン確認

⭐ **任意**  
📍 PowerShell / CMD / VSCodeターミナル

**実行場所:**
- **PowerShell** - Windowsキー + X → 「Windows PowerShell」
- **CMD** - Windowsキー + R → 「cmd」
- **VSCodeターミナル** - VSCode内で Ctrl + `

```powershell
pyenv install -l
```

**特定バージョンのみ表示:**
```powershell
pyenv install -l | findstr 3.11
```

**💡 2025年1月時点の推奨:**
- **x64 Windows**: Python 3.13.0
- **ARM64 Windows**: Python 3.13.0-arm64

---

#### Pythonインストール

✅ **必須**  
📍 PowerShell / CMD / VSCodeターミナル

**実行場所:**
- **PowerShell** - Windowsキー + X → 「Windows PowerShell」
- **CMD** - Windowsキー + R → 「cmd」
- **VSCodeターミナル** - VSCode内で Ctrl + `

**【x64 Windows】一般的なPC:**

```powershell
pyenv install 3.11.7
pyenv install 3.13.0
```

**✅ 実行結果:**
```
Downloading Python-3.13.0-amd64.exe...
Installing Python-3.13.0...
python-3.13.0 installed successfully!
```

**⏰ 所要時間: 5-10分**

---

**【ARM64 Windows】Surface Pro X等:**

```powershell
# ARM64ネイティブ版（推奨・高速）
pyenv install 3.11.7-arm64
pyenv install 3.13.0-arm64

# またはx64版（互換性重視、TensorFlow/PyTorch開発時）
pyenv install 3.11.7
pyenv install 3.13.0
```

**✅ 実行結果（ARM64版）:**
```
Downloading Python-3.13.0-arm64.exe...
Installing Python-3.13.0-arm64...
python-3.13.0 installed successfully!
```

**💡 ARM64の場合の選び方:**
```
Web開発・データ分析 → 3.13.0-arm64（推奨・高速）
ディープラーニング → 3.13.0（x64版、互換性重視）
```

**⏰ 所要時間: 5-10分**

---

#### インストール済みバージョン確認

✅ **必須**

```powershell
pyenv versions
```

**✅ 表示（x64の場合）:**
```
* 3.11.7
  3.13.0
```

**✅ 表示（ARM64の場合、ARM64版をインストールした場合）:**
```
* 3.11.7-arm64
  3.13.0-arm64
```

**💡 `*` = 現在使用中**

---

#### デフォルトバージョン設定

✅ **必須**

**【x64 Windows】:**

```powershell
pyenv global 3.13.0
```

**【ARM64 Windows】:**

```powershell
# ARM64版をインストールした場合
pyenv global 3.13.0-arm64

# x64版をインストールした場合
pyenv global 3.13.0
```

**何も表示されなければOK**

---

#### 確認

✅ **必須**

```powershell
python -V
```

**✅ 成功:**
```
Python 3.13.x
```

**アーキテクチャ確認（ARM64の場合）:**

```powershell
python -c "import platform; print(platform.machine())"
```

**✅ 表示:**
- **x64 Windows**: `AMD64`
- **ARM64 Windows（ARM64版Python）**: `ARM64`
- **ARM64 Windows（x64版Python）**: `AMD64`（エミュレーション）

**🎉 Python環境完成！**

---

## STEP 5: 仮想環境（venv）の使い方

#### venvとは？

```
venv = 仮想環境作成ツール（Python標準）

役割:
プロジェクトごとに独立した環境を作る

なぜ必要?
プロジェクトA: Django 4.2
プロジェクトB: Django 5.0
→ 完全に独立！干渉なし！
```

---

#### 基本コマンド

**1. 作成**

✅ **必須**  
📍 📁 プロジェクト内

```powershell
python -m venv .venv
```

**💡 `.venv` は推奨フォルダ名（Python公式推奨）**

---

**2. 有効化**

✅ **必須**  
📍 📁 `.venv`があるフォルダ

**PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

**CMD:**
```cmd
.venv\Scripts\activate.bat
```

**✅ 成功すると:**
```powershell
(.venv) PS C:\Projects\my-project>
└──┬──┘
   └─ 有効化されている印
```

---

**3. 無効化**

⭐ **任意**

```powershell
deactivate
```

**プロンプトが元に戻る:**
```powershell
PS C:\Projects\my-project>
# (.venv) が消える
```

---

#### PowerShell実行エラーが出たら

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

#### パッケージ管理

```powershell
# 有効化した状態で

# インストール
pip install numpy pandas matplotlib

# 確認
pip list

# requirements.txt作成
pip freeze > requirements.txt

# requirements.txtからインストール
pip install -r requirements.txt
```

---

## STEP 6: プロジェクト実践

#### シナリオ1: 新規プロジェクト（Djangoアプリ）

**完全手順:**

```powershell
# プロジェクトフォルダ作成
mkdir my-project
cd my-project

# Pythonバージョン指定（プロジェクト専用）
# x64の場合
pyenv local 3.11.7
# ARM64の場合
pyenv local 3.11.7-arm64

# 確認
type .python-version
# 3.11.7 または 3.11.7-arm64

# 仮想環境作成
python -m venv .venv

# 有効化
.venv\Scripts\Activate.ps1

# プロンプト確認
# (.venv) が表示される

# pipアップデート
python -m pip install --upgrade pip

# Djangoインストール
pip install django

# Djangoプロジェクト作成
django-admin startproject config .

# データベース初期化
python manage.py migrate

# 開発サーバー起動
python manage.py runserver
```

**✅ ブラウザで http://127.0.0.1:8000/ を確認**

**🎉 完成！**

---

#### シナリオ2: 既存プロジェクト（GitHubからクローン）

```powershell
# クローン
git clone <URL>
cd project

# Pythonバージョン確認（.python-versionがあれば自動）
type .python-version
# 3.11.7

# 仮想環境作成
python -m venv .venv
.venv\Scripts\Activate.ps1

# 依存関係インストール
pip install -r requirements.txt

# 起動
python manage.py runserver
```

**🎉 完了！**

---

## よく使うコマンド一覧

```powershell
# ========================================
# pyenv
# ========================================
pyenv versions              # インストール済みPython一覧
pyenv install -l           # インストール可能なバージョン一覧

# x64 Windows
pyenv install 3.13.0       # Pythonインストール
pyenv global 3.13.0        # グローバル設定
pyenv local 3.11.7         # プロジェクト専用設定

# ARM64 Windows
pyenv install 3.13.0-arm64 # ARM64版Pythonインストール
pyenv global 3.13.0-arm64  # ARM64版をグローバル設定
pyenv local 3.11.7-arm64   # ARM64版をプロジェクト専用設定

# ========================================
# venv
# ========================================
python -m venv .venv       # 仮想環境作成
.venv\Scripts\Activate.ps1 # 有効化（PowerShell）
.venv\Scripts\activate.bat # 有効化（CMD）
deactivate                 # 無効化

# ========================================
# pip
# ========================================
pip install パッケージ名         # インストール
pip install パッケージ名==1.2.3  # バージョン指定
pip uninstall パッケージ名       # アンインストール
pip list                      # インストール済み一覧
pip freeze > requirements.txt # 依存関係保存
pip install -r requirements.txt # 依存関係インストール
python -m pip install --upgrade pip # pipアップデート
```

---

## ⚠️ トラブルシューティング

### エラー1: `python` コマンドが見つからない

**症状:**
```powershell
python --version
# 'python' は、内部コマンドまたは外部コマンド...
```

**解決策:**

```powershell
# 1. PowerShell再起動
# 完全に閉じる → 再起動

# 2. pyenv rehash
pyenv rehash

# 3. 確認
python -V
```

---

### エラー2: 仮想環境が有効化できない

**症状:**
```powershell
.venv\Scripts\Activate.ps1
# スクリプトの実行が無効...
```

**解決策:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**または、CMD使用:**
```cmd
.venv\Scripts\activate.bat
```

---

### エラー3: Microsoft Store版Pythonが邪魔

**症状:**
```powershell
python --version
# Microsoft Store版のPythonが起動する
```

**解決策:**

1. **アンインストール:**
   ```
   設定 → アプリ → Python → アンインストール
   ```

2. **アプリ実行エイリアスを無効化:**
   ```
   設定 → アプリ → アプリ実行エイリアス
   → Python関連を全てオフ
   ```

3. **PowerShell再起動**

---

### エラー4: ARM64でパッケージがインストールできない

**症状:**
```powershell
pip install パッケージ名
# error: Microsoft Visual C++ 14.0 or greater is required
```

**原因:**
```
パッケージがARM64ネイティブ版を提供していない
C拡張のコンパイルが必要
```

**解決策1: x64版Pythonを使う（最も簡単）**

```powershell
# x64版Pythonに切り替え
pyenv local 3.11.7  # ARM64なし = x64版

# 仮想環境再作成
Remove-Item -Recurse -Force .venv
python -m venv .venv
.venv\Scripts\Activate.ps1

# 再インストール
pip install パッケージ名
```

**💡 エミュレーションで互換性向上！**

---

**解決策2: ビルドツールインストール**

1. Visual Studio Build Toolsをダウンロード
   - https://visualstudio.microsoft.com/downloads/
   - Build Tools for Visual Studio 2022

2. インストール後、再試行
   ```powershell
   pip install パッケージ名
   ```

---

### エラー5: Permission denied

**症状:**
```powershell
pip install django
# Permission denied
```

**原因:**
グローバル環境にインストールしようとしている

**解決策:**

```powershell
# 仮想環境作成
python -m venv .venv
.venv\Scripts\Activate.ps1

# 再度インストール
pip install django
```

**❌ 絶対NG:**
```powershell
# 管理者権限でpip install  # これは絶対ダメ！
```

---

## 🎯 完成形

```
C:\Projects\
└── my-project\
    ├── .python-version    # pyenv local で自動作成
    ├── .venv\            # 仮想環境
    ├── requirements.txt  # 依存関係
    ├── .gitignore
    └── (ソースコード)
```

**.gitignore**
```gitignore
.venv/
__pycache__/
*.py[cod]
*.sqlite3
.DS_Store
```

---

## 完成チェックリスト

### 基本環境

- [ ] アーキテクチャ確認済み（x64 or ARM64）
- [ ] Python公式インストール済み（`python -V`）
- [ ] pyenv-win動作確認（`pyenv --version`）
- [ ] Python 3.13インストール済み（適切なアーキテクチャ）
- [ ] Python 3.11インストール済み（適切なアーキテクチャ）
- [ ] グローバルバージョン設定済み（`python --version`）
- [ ] Pythonアーキテクチャ確認済み（ARM64の場合）

### 実践

- [ ] 仮想環境作成できる
- [ ] 仮想環境有効化できる
- [ ] パッケージインストールできる
- [ ] requirements.txt作成できる
- [ ] Djangoプロジェクト作成できる

**全部✅ → 完璧！🎉**

---

## ドキュメント情報

**バージョン:** 2.0 (Windows版 - ARM64完全対応・シンプル版)  
**最終更新:** 2025年1月  
**対象:** Windows 10/11 (x64/ARM64)  
**所要時間:** 30分

**対応環境:**
- ✅ Windows 10 (20H2以降) x64/ARM64
- ✅ Windows 11 x64/ARM64
- ✅ Surface Pro X
- ✅ Snapdragon搭載PC
- ✅ 一般的なx64 PC

---

**🎉 以上で完了！**

このガイドだけで、Windows（x64/ARM64）でのPython開発をすぐに始められます。

**💡 ARM64 Windows（Surface Pro X等）の方へ:**
- Web開発・データ分析: ARM64版Python（`-arm64`）が最速
- ディープラーニング: x64版Pythonで互換性確保
- プロジェクトごとに使い分け可能

**Happy Coding! 🐍✨**
