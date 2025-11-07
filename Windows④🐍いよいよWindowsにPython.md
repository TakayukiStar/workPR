# 🐍 Windows Python環境構築ガイド 2025 - 生成AI開発版

**【Windows 10/11 対応 - VSCode + venv + Google AI Studio - 20分で完了】**

> **📌 このガイドの特徴**
> - ✅ シンプル！pyenv不要、venvだけでOK
> - ✅ VSCode統合で快適開発
> - ✅ Google AI Studioで生成AI開発
> - ✅ 20分で動くデモまで完成
> - ✅ x64とARM64の両方に対応
> - ✅ 2025年1月時点の最新情報

---

## 📑 クイックナビゲーション

### 🎯 あなたの状況に合わせて選択

**今すぐ環境構築したい →** [STEP 2: Python公式インストール](#step-2-python公式インストール)

**ARM64 Windows（Surface Pro X等）→** [STEP 1: アーキテクチャ確認](#step-1-アーキテクチャ確認)

**生成AIデモを見たい →** [STEP 6: 生成AIデモ](#step-6-生成aiデモ)

---

## 目次

1. [アーキテクチャ確認](#step-1-アーキテクチャ確認)
2. [Python公式インストール](#step-2-python公式インストール)
3. [VSCode設定](#step-3-vscode設定)
4. [venv（仮想環境）の使い方](#step-4-venv仮想環境の使い方)
5. [Google AI Studio設定](#step-5-google-ai-studio設定)
6. [生成AIデモ](#step-6-生成aiデモ)
7. [プロジェクト実践](#step-7-プロジェクト実践)

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

**アーキテクチャ確認（ARM64の場合のみ）:**

```powershell
python -c "import platform; print(platform.machine())"
```

**✅ 表示:**
- **x64 Windows**: `AMD64`
- **ARM64 Windows**: `ARM64` または `AMD64`（エミュレーション）

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

それでもダメなら → [トラブルシューティング](#トラブルシューティング)

---

**エラー2: Microsoft Store が起動する**
```
python と入力するとMicrosoft Storeが開く
```

**解決策:**
→ [トラブルシューティング](#トラブルシューティング)

---

## STEP 3: VSCode設定

#### ステップ3-1: VSCodeインストール

✅ **必須**

**1. ダウンロード:**

```
https://code.visualstudio.com/
```

**2. インストール:**
```
1. ダウンロードしたインストーラを起動
2. 利用規約に同意
3. 以下をチェック:
   ☑ PATHへの追加（必須）
   ☑ エクスプローラーのコンテキストメニューに追加（推奨）
   ☑ サポートされているファイルの種類のエディターとして、Codeを登録する（推奨）
4. インストール実行
```

**⏰ 所要時間: 3-5分**

---

#### ステップ3-2: Python拡張機能インストール

✅ **必須**

**VSCodeを起動してから:**

```
1. 左サイドバーの「拡張機能」アイコンをクリック
   または Ctrl + Shift + X

2. 検索ボックスに「Python」と入力

3. 「Python」（発行元: Microsoft）を選択

4. 「インストール」ボタンをクリック
```

**自動でインストールされる拡張機能:**
- Python (Microsoft)
- Pylance（言語サーバー）
- Python Debugger

**⏰ 所要時間: 1-2分**

---

#### ステップ3-3: VSCode設定

🔶 **推奨**

**settings.jsonを開く:**

```
1. Ctrl + Shift + P でコマンドパレットを開く
2. 「Preferences: Open User Settings (JSON)」と入力
3. Enterキー
```

**以下を追加:**

```json
{
  "python.terminal.activateEnvironment": true,
  "python.defaultInterpreterPath": "python",
  "python.analysis.typeCheckingMode": "basic",
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true
  },
  "terminal.integrated.defaultProfile.windows": "PowerShell"
}
```

**💡 これで仮想環境が自動で認識されます！**

---

#### ステップ3-4: PowerShell実行ポリシー設定

✅ **必須**（VSCodeで仮想環境を使う場合）

**VSCodeのターミナルで実行:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**確認メッセージで `Y` を入力**

**💡 これをしないと、VSCodeで仮想環境が有効化できません！**

---

## STEP 4: venv（仮想環境）の使い方

#### venvとは？

```
venv = 仮想環境作成ツール（Python標準）

役割:
プロジェクトごとに独立した環境を作る

なぜ必要?
プロジェクトA: google-generativeai 0.8.3
プロジェクトB: google-generativeai 0.7.0
→ 完全に独立！干渉なし！
```

---

#### 基本コマンド4つ

**1. 作成**

✅ **必須**  
📍 プロジェクトフォルダ内

```powershell
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

**💡 `.venv` は推奨フォルダ名（Python公式推奨）**

**⏰ 所要時間: 10-20秒**

---

**2. 有効化**

✅ **必須**  
📍 `.venv`があるフォルダ

**PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

**CMD:**
```cmd
.venv\Scripts\activate.bat
```

**VSCode:**
```
VSCodeでフォルダを開くと自動で有効化されます
（settings.jsonを設定している場合）
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

**4. 削除**

⭐ **任意**（やり直したい時）

```powershell
# 無効化
deactivate

# フォルダ削除
Remove-Item -Recurse -Force .venv

# 再作成
python -m venv .venv
```

---

#### パッケージ管理

```powershell
# 有効化した状態で

# pipアップデート（最初に1回）
python -m pip install --upgrade pip

# パッケージインストール
pip install google-generativeai python-dotenv

# 確認
pip list

# requirements.txt作成
pip freeze > requirements.txt

# requirements.txtからインストール
pip install -r requirements.txt
```

---

## STEP 5: Google AI Studio設定

#### ステップ5-1: Google AI Studioにアクセス

✅ **必須**

**1. ブラウザでアクセス:**

```
https://aistudio.google.com/
```

**2. Googleアカウントでログイン**

**3. 利用規約に同意**

---

#### ステップ5-2: APIキー取得

✅ **必須**

**画面の流れ:**

```
1. 左サイドバーの「Get API key」をクリック

2. 「Create API key」ボタンをクリック

3. プロジェクトを選択:
   - 既存のプロジェクトを選択
   - または「Create new project」で新規作成

4. APIキーが表示される:
   ┌─────────────────────────────────────┐
   │ Your API key                        │
   │ AIzaSy...（40文字くらい）           │
   │ [Copy] ボタン                       │
   └─────────────────────────────────────┘

5. 「Copy」ボタンをクリックしてコピー
```

**⚠️ 重要: APIキーは外部に公開しないでください！**

---

#### ステップ5-3: APIキー保存

✅ **必須**

**プロジェクトフォルダに`.env`ファイルを作成:**

**VSCodeで:**
```
1. プロジェクトフォルダを開く
2. 新規ファイル作成: .env
3. 以下を記述:
```

**.env ファイルの内容:**
```
GOOGLE_API_KEY=あなたのAPIキー
```

**💡 例:**
```
GOOGLE_API_KEY=AIzaSyABCDEFGHIJKLMNOPQRSTUVWXYZ1234567
```

---

#### ステップ5-4: .gitignore設定

✅ **必須**（Git使用時）

**プロジェクトフォルダに`.gitignore`ファイルを作成:**

**.gitignore ファイルの内容:**
```gitignore
# 仮想環境
.venv/
venv/
env/

# APIキー
.env

# Python
__pycache__/
*.py[cod]
*.pyc

# その他
.DS_Store
```

**💡 これで`.env`ファイルがGitにアップロードされるのを防げます！**

---

## STEP 6: 生成AIデモ

#### プロジェクト作成

**完全手順:**

```powershell
# 1. プロジェクトフォルダ作成
mkdir gemini-demo
cd gemini-demo

# 2. 仮想環境作成
python -m venv .venv

# 3. 仮想環境有効化
.venv\Scripts\Activate.ps1

# 4. pipアップデート
python -m pip install --upgrade pip

# 5. 必要なパッケージインストール
pip install google-generativeai python-dotenv

# 6. VSCodeで開く
code .
```

---

#### .envファイル作成

**VSCodeで新規ファイル作成: `.env`**

```
GOOGLE_API_KEY=あなたのAPIキー
```

---

#### デモコード作成

**VSCodeで新規ファイル作成: `demo.py`**

```python
"""
Google Gemini API デモ
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルから環境変数を読み込み
load_dotenv()

# APIキーを設定
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# モデルを初期化
model = genai.GenerativeModel('gemini-pro')

def chat():
    """シンプルなチャット機能"""
    print("=" * 50)
    print("Google Gemini チャットデモ")
    print("終了するには 'quit' または 'exit' と入力")
    print("=" * 50)
    print()
    
    while True:
        # ユーザー入力
        user_input = input("あなた: ")
        
        # 終了チェック
        if user_input.lower() in ['quit', 'exit', '終了']:
            print("チャットを終了します。")
            break
        
        # 空入力チェック
        if not user_input.strip():
            continue
        
        try:
            # Geminiに送信
            response = model.generate_content(user_input)
            
            # レスポンス表示
            print(f"\nGemini: {response.text}\n")
            
        except Exception as e:
            print(f"\nエラーが発生しました: {e}\n")

if __name__ == "__main__":
    chat()
```

---

#### 実行

**VSCodeのターミナルで:**

```powershell
python demo.py
```

**✅ 成功すると:**
```
==================================================
Google Gemini チャットデモ
終了するには 'quit' または 'exit' と入力
==================================================

あなた: こんにちは！
Gemini: こんにちは！何かお手伝いできることはありますか？

あなた: Pythonで素数を判定する関数を書いて
Gemini: 以下はPythonで素数を判定する関数です：
...（コード例が表示される）

あなた: quit
チャットを終了します。
```

**🎉 生成AIデモ完成！**

---

#### 応用例

**1. チャット履歴を保存**

```python
"""
チャット履歴を保存するバージョン
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

# チャット履歴
chat_history = []

def chat_with_history():
    """チャット履歴を保持するチャット"""
    print("=" * 50)
    print("Google Gemini チャットデモ（履歴付き）")
    print("終了するには 'quit' または 'exit' と入力")
    print("=" * 50)
    print()
    
    # チャットセッション開始
    chat = model.start_chat(history=[])
    
    while True:
        user_input = input("あなた: ")
        
        if user_input.lower() in ['quit', 'exit', '終了']:
            print("チャットを終了します。")
            break
        
        if not user_input.strip():
            continue
        
        try:
            # チャットで送信（履歴を保持）
            response = chat.send_message(user_input)
            print(f"\nGemini: {response.text}\n")
            
        except Exception as e:
            print(f"\nエラーが発生しました: {e}\n")

if __name__ == "__main__":
    chat_with_history()
```

---

**2. ストリーミングレスポンス**

```python
"""
ストリーミングでレスポンスを表示
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def chat_streaming():
    """ストリーミングでチャット"""
    print("=" * 50)
    print("Google Gemini チャットデモ（ストリーミング）")
    print("終了するには 'quit' または 'exit' と入力")
    print("=" * 50)
    print()
    
    while True:
        user_input = input("あなた: ")
        
        if user_input.lower() in ['quit', 'exit', '終了']:
            print("チャットを終了します。")
            break
        
        if not user_input.strip():
            continue
        
        try:
            print("\nGemini: ", end="", flush=True)
            
            # ストリーミングで生成
            response = model.generate_content(user_input, stream=True)
            
            for chunk in response:
                print(chunk.text, end="", flush=True)
            
            print("\n")
            
        except Exception as e:
            print(f"\nエラーが発生しました: {e}\n")

if __name__ == "__main__":
    chat_streaming()
```

---

**3. 画像を含む質問**

```python
"""
画像を含む質問（Gemini Pro Vision）
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Visionモデル
model = genai.GenerativeModel('gemini-pro-vision')

def analyze_image(image_path: str, prompt: str):
    """画像を分析"""
    try:
        # 画像を読み込み
        img = Image.open(image_path)
        
        # 画像とプロンプトを送信
        response = model.generate_content([prompt, img])
        
        print(f"質問: {prompt}")
        print(f"回答: {response.text}")
        
    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    # 使い方
    analyze_image(
        image_path="sample.jpg",
        prompt="この画像に何が写っていますか？"
    )
```

---

## STEP 7: プロジェクト実践

#### フォルダ構成

**推奨構成:**

```
gemini-project\
├── .venv\              # 仮想環境（Gitに含めない）
├── .env                # APIキー（Gitに含めない）
├── .gitignore          # Git除外設定
├── requirements.txt    # 依存関係
├── README.md          # プロジェクト説明
├── main.py            # メインスクリプト
└── utils\             # ユーティリティ
    ├── __init__.py
    └── ai_helper.py   # AI関連の関数
```

---

#### requirements.txt

**作成コマンド:**

```powershell
pip freeze > requirements.txt
```

**内容例:**

```txt
google-generativeai==0.8.3
python-dotenv==1.0.1
Pillow==10.2.0
```

---

#### README.md

**テンプレート:**

```markdown
# Gemini AI プロジェクト

Google Gemini APIを使用したAIアプリケーション

## セットアップ

```bash
# 仮想環境作成
python -m venv .venv

# 有効化（PowerShell）
.venv\Scripts\Activate.ps1

# 依存関係インストール
pip install -r requirements.txt

# .envファイル作成
# GOOGLE_API_KEY=your-api-key-here
```

## 使い方

```bash
python main.py
```

## 必要な環境変数

- `GOOGLE_API_KEY`: Google AI StudioのAPIキー
```

---

#### プロジェクトテンプレート

**完全なプロジェクト作成手順:**

```powershell
# プロジェクト作成
mkdir my-ai-project
cd my-ai-project

# 仮想環境
python -m venv .venv
.venv\Scripts\Activate.ps1

# パッケージインストール
python -m pip install --upgrade pip
pip install google-generativeai python-dotenv

# .gitignore作成
@"
.venv/
.env
__pycache__/
*.py[cod]
"@ | Out-File -FilePath .gitignore -Encoding utf8

# .env作成（後でAPIキーを記入）
@"
GOOGLE_API_KEY=your-api-key-here
"@ | Out-File -FilePath .env -Encoding utf8

# requirements.txt作成
pip freeze > requirements.txt

# README.md作成
@"
# My AI Project
"@ | Out-File -FilePath README.md -Encoding utf8

# main.py作成
@"
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')

if __name__ == '__main__':
    response = model.generate_content('Hello, Gemini!')
    print(response.text)
"@ | Out-File -FilePath main.py -Encoding utf8

# VSCodeで開く
code .
```

---

## よく使うコマンド一覧

```powershell
# ========================================
# Python
# ========================================
python -V                  # バージョン確認
python -c "コード"          # コマンドライン実行
python script.py          # スクリプト実行

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
python -m pip install --upgrade pip         # pipアップデート
pip install パッケージ名                     # インストール
pip install パッケージ名==1.2.3              # バージョン指定
pip uninstall パッケージ名                   # アンインストール
pip list                                   # インストール済み一覧
pip show パッケージ名                        # パッケージ詳細
pip freeze > requirements.txt              # 依存関係保存
pip install -r requirements.txt            # 依存関係インストール

# ========================================
# VSCode
# ========================================
code .                    # 現在のフォルダをVSCodeで開く
code ファイル名            # ファイルをVSCodeで開く
```

---

## トラブルシューティング

### エラー1: `python` コマンドが見つからない

**症状:**
```powershell
python --version
# 'python' は、内部コマンドまたは外部コマンド...
```

**解決策:**

```powershell
# 1. PowerShell/CMD再起動
# 完全に閉じる → 再起動

# 2. 確認
python -V
```

**それでもダメな場合:**

**手動でPATH設定:**
```
1. Windowsキー → 「環境変数」で検索
2. 「環境変数を編集」をクリック
3. ユーザー環境変数の「Path」を選択 → 「編集」
4. 「新規」をクリック
5. 以下を追加:
   C:\Users\あなた\AppData\Local\Programs\Python\Python313\
   C:\Users\あなた\AppData\Local\Programs\Python\Python313\Scripts\
6. 「OK」で保存
7. PowerShell/CMD再起動
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

### エラー4: APIキーエラー

**症状:**
```
google.api_core.exceptions.PermissionDenied: 403 API key not valid
```

**原因:**
- APIキーが間違っている
- .envファイルが読み込まれていない

**解決策:**

```powershell
# .envファイル確認
type .env
# GOOGLE_API_KEY=... が正しいか確認

# python-dotenvがインストールされているか確認
pip show python-dotenv

# なければインストール
pip install python-dotenv
```

---

### エラー5: パッケージがインストールできない（ARM64）

**症状:**
```powershell
pip install パッケージ名
# error: Microsoft Visual C++ 14.0 or greater is required
```

**解決策:**

**Visual Studio Build Toolsをインストール:**
```
1. https://visualstudio.microsoft.com/downloads/
2. Build Tools for Visual Studio 2022 をダウンロード
3. インストール時に「C++によるデスクトップ開発」を選択
4. インストール完了後、再試行
```

---

## 完成チェックリスト

### 基本環境

- [ ] アーキテクチャ確認済み（x64 or ARM64）
- [ ] Python 3.13インストール済み（`python -V`）
- [ ] VSCodeインストール済み
- [ ] Python拡張機能インストール済み
- [ ] PowerShell実行ポリシー設定済み

### 仮想環境

- [ ] 仮想環境作成できる（`python -m venv .venv`）
- [ ] 仮想環境有効化できる（`.venv\Scripts\Activate.ps1`）
- [ ] パッケージインストールできる（`pip install`）
- [ ] requirements.txt作成できる（`pip freeze`）

### Google AI Studio

- [ ] Google AI Studioアカウント作成済み
- [ ] APIキー取得済み
- [ ] .envファイル作成済み
- [ ] .gitignore設定済み

### 生成AIデモ

- [ ] google-generativeaiインストール済み
- [ ] デモコード実行成功
- [ ] Geminiとチャットできた

**全部✅ → 完璧！🎉**

---

## 次のステップ

### 初心者

1. **Pythonの基礎学習**
   - 変数、関数、クラス
   - 公式チュートリアル

2. **生成AIの基礎**
   - プロンプトエンジニアリング
   - Google AI Studioのプレイグラウンド

3. **簡単なアプリ作成**
   - コマンドラインチャットボット
   - テキスト要約ツール
   - 翻訳アプリ

### 中級者

1. **LangChain導入**
   - RAG（検索拡張生成）
   - チェーン構築

2. **Streamlit導入**
   - Webアプリ化
   - ユーザーインターフェース

3. **データベース連携**
   - チャット履歴保存
   - ユーザー管理

### 上級者

1. **本格的なWebアプリ**
   - FastAPI + React
   - 認証機能

2. **Fine-tuning**
   - カスタムモデル作成
   - 専門分野特化

3. **デプロイ**
   - Google Cloud Run
   - Vercel

---

## ドキュメント情報

**バージョン:** 3.0 (生成AI開発特化版)  
**最終更新:** 2025年1月  
**対象:** Windows 10/11 (x64/ARM64)  
**所要時間:** 20分

**対応環境:**
- ✅ Windows 10 (20H2以降) x64/ARM64
- ✅ Windows 11 x64/ARM64
- ✅ Surface Pro X
- ✅ Snapdragon搭載PC
- ✅ 一般的なx64 PC

**使用技術:**
- Python 3.13.x
- VSCode
- venv（標準ライブラリ）
- Google Gemini API
- python-dotenv

---

**🎉 以上で完了！**

このガイドだけで、Windows（x64/ARM64）での生成AI開発をすぐに始められます。

**💡 ポイント:**
- ✅ シンプル - pyenv不要、venvだけ
- ✅ VSCode統合 - 快適な開発環境
- ✅ 実践的 - すぐに動くデモ付き
- ✅ 拡張可能 - LangChain、Streamlitへ展開

**Happy Coding! 🐍✨ Happy AI Development! 🤖✨**
