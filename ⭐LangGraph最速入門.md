# LangGraph完全マスターガイド 2025

**初心者から実務レベルまで - この一冊で完結する決定版ガイド**

---

## 📖 本書の使い方

### このガイドで達成できること

✅ LangGraphの基礎から実践まで完全習得  
✅ Google AI Studio (Gemini) との統合をマスター  
✅ Tavily検索APIを活用した実用的なAIエージェント構築  
✅ 実サービスで使える本格的なワークフロー実装  
✅ エラー処理、並列実行、複雑な分岐の実装

### 対象読者

- LangGraph未経験者
- Python基礎知識がある方
- 実務でAIエージェントを構築したい方

### 学習の進め方

1. **第1章は必読** - 全ての基礎となります
2. **コードは必ず実行** - 読むだけでなく動かして理解
3. **APIキーを事前準備** - 後述の手順で取得してください

---

## 🎯 目次

### 第0章: 環境準備とAPIキー取得
- [0-1. 必要なパッケージのインストール](#0-1-必要なパッケージのインストール)
- [0-2. APIキーの取得方法](#0-2-apiキーの取得方法)
- [0-3. APIキーの設定方法](#0-3-apiキーの設定方法)

### 第1章: LangGraphの基本概念
- [1-1. LangGraphとは何か](#1-1-langgraphとは何か)
- [1-2. 必須要素 vs オプション要素](#1-2-必須要素-vs-オプション要素)
- [1-3. StateGraphの仕組み](#1-3-stategraphの仕組み)
- [1-4. START/ENDの真実](#1-4-startendの真実)

### 第2章: 最小構成の実装
- [2-1. 17行で動く最小コード](#2-1-17行で動く最小コード)
- [2-2. 実践的な基本実装](#2-2-実践的な基本実装)
- [2-3. グラフ可視化の実装](#2-3-グラフ可視化の実装)
- [2-4. よくある質問30選](#2-4-よくある質問30選)

### 第3章: 条件分岐とルーティング
- [3-1. 条件分岐の基本](#3-1-条件分岐の基本)
- [3-2. 複数ルートの実装](#3-2-複数ルートの実装)
- [3-3. 動的ルーティング](#3-3-動的ルーティング)
- [3-4. 第3章完全実装例](#3-4-第3章完全実装例)

### 第4章: ツール統合 - Tavily検索
- [4-1. Tavily検索の基本](#4-1-tavily検索の基本)
- [4-2. LLMとツールの連携](#4-2-llmとツールの連携)
- [4-3. 実用的な検索エージェント](#4-3-実用的な検索エージェント)
- [4-4. ストリーミング実行](#4-4-ストリーミング実行)
- [4-5. 複数ツールの統合](#4-5-複数ツールの統合)

### 第5章: ループ処理とエラーハンドリング
- [5-1. ループ処理の基本](#5-1-ループ処理の基本)
- [5-2. 最大試行回数の制御](#5-2-最大試行回数の制御)
- [5-3. エラーハンドリング戦略](#5-3-エラーハンドリング戦略)
- [5-4. リトライロジックの実装](#5-4-リトライロジックの実装)
- [5-5. 第5章完全実装例](#5-5-第5章完全実装例)

### 第6章: 並列処理と非同期実行
- [6-1. 並列ノードの実装](#6-1-並列ノードの実装)
- [6-2. 非同期処理のパターン](#6-2-非同期処理のパターン)
- [6-3. パフォーマンス最適化](#6-3-パフォーマンス最適化)
- [6-4. 第6章完全実装例](#6-4-第6章完全実装例)

### 第7章: 実践的なシステム構築
- [7-1. マルチエージェントシステム](#7-1-マルチエージェントシステム)
- [7-2. 複雑な分岐フロー](#7-2-複雑な分岐フロー)
- [7-3. 本番環境への展開](#7-3-本番環境への展開)
- [7-4. 第7章完全実装例](#7-4-第7章完全実装例)

### 付録
- [A. トラブルシューティング完全版](#付録a-トラブルシューティング完全版)
- [B. パフォーマンスチューニング](#付録b-パフォーマンスチューニング)
- [C. ベストプラクティス集](#付録c-ベストプラクティス集)
- [3-4. 第3章完全実装例](#3-4-第3章完全実装例)

---

# 第0章: 環境準備とAPIキー取得

## 0-1. 必要なパッケージのインストール

### すべて一括インストール（推奨）

```bash
# 基本パッケージ + 可視化 + 検索 + 非同期
pip install langgraph langchain-google-genai langchain-community \
            tavily-python pillow aiohttp tenacity

# 可視化用（どちらか一方でOK）
pip install pygraphviz  # 推奨
# または
pip install grandalf    # pygraphvizが動かない場合
```

### 個別インストール（必要に応じて）

```bash
# コア機能（必須）
pip install langgraph
pip install langchain-google-genai
pip install langchain-community

# 検索機能（第4章以降）
pip install tavily-python

# 可視化（オプション、強く推奨）
pip install pillow
pip install pygraphviz  # または grandalf

# 非同期処理（第6章以降）
pip install aiohttp

# エラーハンドリング（第5章以降）
pip install tenacity
```

### インストール確認

```python
# 以下を実行してエラーが出なければOK
import langgraph
import langchain_google_genai
import tavily
print("✅ すべてのパッケージが正しくインストールされています")
```

---

## 0-2. APIキーの取得方法

### Google AI Studio APIキー取得

**所要時間: 約2分**

1. **Google AI Studioにアクセス**
   - URL: https://aistudio.google.com/apikey
   - Googleアカウントでログイン

2. **APIキーを作成**
   - 「Create API Key」ボタンをクリック
   - プロジェクトを選択（または新規作成）
   - APIキーが生成される（`AIza...` で始まる文字列）

3. **APIキーをコピー**
   - 表示されたAPIキー全体をコピー
   - **重要**: このキーは再表示できないため、安全な場所に保存

**注意事項:**
- APIキーは他人に見せない
- GitHubなどに公開しない
- 環境変数または設定ファイルで管理

### Tavily Search APIキー取得

**所要時間: 約3分**

1. **Tavilyにアカウント登録**
   - URL: https://tavily.com/
   - 「Sign Up」からアカウント作成

2. **APIキーを取得**
   - ダッシュボードにログイン
   - 「API Keys」セクションに移動
   - デフォルトで1つのAPIキーが発行済み

3. **無料プランの制限確認**
   - 月間1,000リクエストまで無料
   - それ以上は有料プラン

---

## 0-3. APIキーの設定方法

### 方法1: コード内で直接設定（学習用）

```python
import os

# Gemini APIキー（環境変数名は自由ですが、統一推奨）
os.environ["GEMINI_API_KEY"] = "AIza..."  # ここに実際のキーを貼り付け

# Tavily APIキー（第4章以降で使用）
os.environ["TAVILY_API_KEY"] = "tvly-..."  # ここに実際のキーを貼り付け
```

**⚠️ この方法の注意点:**
- コードをGitHubにプッシュしないこと
- 学習・テスト目的のみで使用
- 本番環境では方法2を推奨

### 方法2: .envファイルで管理（推奨）

#### ステップ1: python-dotenvをインストール

```bash
pip install python-dotenv
```

#### ステップ2: .envファイルを作成

プロジェクトのルートディレクトリに `.env` ファイルを作成:

```bash
# .env
GEMINI_API_KEY=AIza...
TAVILY_API_KEY=tvly-...
```

#### ステップ3: .gitignoreに追加

```bash
# .gitignore
.env
```

#### ステップ4: コードで読み込み

```python
import os
from dotenv import load_dotenv

# .envファイルを読み込み
load_dotenv()

# 環境変数として利用可能
gemini_api_key = os.environ["GEMINI_API_KEY"]
tavily_api_key = os.environ["TAVILY_API_KEY"]

# 確認
if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY が設定されていません")
print("✅ APIキーの読み込み成功")
```

### APIキー設定の確認スクリプト

```python
import os

def check_api_keys():
    """APIキーが正しく設定されているか確認"""
    
    issues = []
    
    # Gemini APIキーの確認
    gemini_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_key:
        issues.append("❌ GEMINI_API_KEY が設定されていません")
    elif gemini_key == "your-gemini-api-key-here":
        issues.append("❌ GEMINI_API_KEY がプレースホルダーのままです")
    else:
        print(f"✅ GEMINI_API_KEY: {gemini_key[:10]}...")
    
    # Tavily APIキーの確認
    tavily_key = os.environ.get("TAVILY_API_KEY")
    if not tavily_key:
        print("ℹ️ TAVILY_API_KEY が設定されていません（第4章以降で必要）")
    elif tavily_key == "your-tavily-api-key-here":
        print("ℹ️ TAVILY_API_KEY がプレースホルダーのままです")
    else:
        print(f"✅ TAVILY_API_KEY: {tavily_key[:10]}...")
    
    if issues:
        print("\n".join(issues))
        raise ValueError("APIキーの設定を確認してください")
    
    print("\n✅ すべてのAPIキーが正しく設定されています")

# 実行
check_api_keys()
```

---

# 第1章: LangGraphの基本概念

## 1-1. LangGraphとは何か

### LangGraphの本質

LangGraphは**ステートフルなAIワークフローを構築するためのフレームワーク**です。

**従来のチェーン型AIとの違い:**

```python
# ❌ 従来のチェーン型（シンプルだが柔軟性に欠ける）
chain = prompt | llm | output_parser
result = chain.invoke({"input": "質問"})

# ✅ LangGraph（複雑なフローを表現可能）
graph = StateGraph(State)
graph.add_node("analyze", analyze_input)
graph.add_node("search", search_web)
graph.add_node("summarize", summarize_results)
graph.add_conditional_edges("analyze", route_decision)
# ... 柔軟な制御フロー
```

### LangGraphが得意なこと

1. **複雑な条件分岐**
   - ユーザー入力に応じて異なる処理ルートを選択
   - LLMの判断で次のアクションを決定

2. **ループ処理**
   - 満足いく結果が得られるまで繰り返し
   - エージェント的な振る舞い

3. **並列実行**
   - 複数のタスクを同時実行
   - 結果を統合

4. **ステート管理**
   - ノード間でデータを共有
   - 実行履歴の追跡

### 実際のユースケース

```
# カスタマーサポートボット
User Input → Intent分類 → 
    ├─ FAQ検索 → 回答生成
    ├─ チケット作成 → 担当者アサイン
    └─ エスカレーション → 人間に転送

# リサーチエージェント
Query → Web検索 → 結果評価 →
    └─ 不十分 → 追加検索（ループ）
    └─ 十分 → レポート生成

# コンテンツ生成パイプライン
Topic → アウトライン生成 →
    ├─ セクション1執筆（並列）
    ├─ セクション2執筆（並列）
    └─ セクション3執筆（並列）
    → 統合 → 校正 → 完成
```

---

## 1-2. 必須要素 vs オプション要素

### 🔴 絶対に必要な5つの要素

#### 1. StateGraph

```python
from langgraph.graph import StateGraph

workflow = StateGraph(State)  # これがないと何も始まらない
```

**役割**: ワークフローの設計図を作成

#### 2. State (TypedDict)

```python
from typing import TypedDict

class State(TypedDict):
    input: str
    output: str
```

**役割**: ノード間で共有するデータの型を定義

**なぜ必須?**
- ノード間でデータを受け渡すため
- 型安全性を確保するため

#### 3. add_node()

```python
workflow.add_node("process", process_function)
```

**役割**: 実行する処理（ノード）を追加

#### 4. add_edge()

```python
workflow.add_edge(START, "process")
workflow.add_edge("process", END)
```

**役割**: ノード同士を接続

#### 5. compile()

```python
app = workflow.compile()
```

**役割**: 実行可能な形式に変換

**なぜ必須?**
- `workflow`は設計図（実行不可）
- `app`は実行可能なアプリケーション

---

### 🟡 自動で用意されるもの（暗黙的）

#### START / END

```python
from langgraph.graph import START, END

# これらは自動的に利用可能
workflow.add_edge(START, "first_node")
workflow.add_edge("last_node", END)
```

**真実:**
- `START`と`END`は**定数**として提供される
- 内部的には`__start__`と`__end__`という名前に変換される
- 書かなくてもグラフは動くが、**99%のケースで使う**

#### __start__ / __end__

```python
# ❌ コードで書かない
workflow.add_edge("__start__", "node")

# ✅ 代わりにSTARTを使う
workflow.add_edge(START, "node")
```

**真実:**
- これらは**内部名**
- グラフ可視化時に表示される
- **直接使うことは絶対にない**

---

### 🟢 あると便利なもの（オプション）

#### set_entry_point() / set_finish_point()

```python
# 古い書き方（非推奨）
workflow.set_entry_point("start_node")
workflow.set_finish_point("end_node")

# ✅ 推奨される書き方
workflow.add_edge(START, "start_node")
workflow.add_edge("end_node", END)
```

**なぜ非推奨?**
- `add_edge(START, ...)`の方が一貫性がある
- 公式ドキュメントでも`START`/`END`を推奨

#### グラフ可視化

```python
# なくても動くが、あると超便利
png_data = app.get_graph().draw_mermaid_png()
```

**推奨度**: ⭐⭐⭐⭐⭐（複雑なグラフでは必須レベル）

---

## 1-3. StateGraphの仕組み

### Stateの役割

**Stateはワークフロー全体で共有される「メモリ」**

```python
from typing import TypedDict

class State(TypedDict):
    input: str       # ユーザー入力
    output: str      # 最終結果
    intermediate: str  # 中間結果
    count: int       # 処理回数
```

### ノード関数のルール

#### 絶対に守るべき2つのルール

**ルール1: 引数は必ず `state`**

```python
# ✅ 正しい
def my_node(state: State) -> dict:
    user_input = state["input"]
    return {"output": "処理済み"}

# ❌ 間違い - 引数名が違う
def my_node(data: State) -> dict:
    return {"output": "処理済み"}

# ❌ 間違い - 型ヒントなし（動くが非推奨）
def my_node(state):
    return {"output": "処理済み"}
```

**ルール2: 戻り値は必ず `dict`**

```python
# ✅ 正しい
def my_node(state: State) -> dict:
    return {"output": "結果"}

# ❌ 間違い - strを返す
def my_node(state: State) -> str:
    return "結果"

# ❌ 間違い - Stateオブジェクトを返す
def my_node(state: State) -> State:
    return state
```

### Stateの更新メカニズム

**重要: 戻り値の`dict`は自動的にマージされる**

```python
from typing import TypedDict

class State(TypedDict):
    input: str
    output: str
    count: int

def increment_node(state: State) -> dict:
    # 現在の state
    # {"input": "test", "output": "", "count": 0}
    
    # countだけ更新して返す
    return {"count": state["count"] + 1}
    
    # 自動マージ後の state
    # {"input": "test", "output": "", "count": 1}
    # ↑ inputとoutputはそのまま残る！
```

**マージのルール:**

```python
# 実行前
state = {"input": "Hello", "output": "", "count": 0}

# ノードが返す
return {"output": "Processed", "count": 1}

# 自動マージ後
state = {"input": "Hello", "output": "Processed", "count": 1}
#        ↑ そのまま    ↑ 更新          ↑ 更新
```

### 複数フィールドの更新

```python
def process_node(state: State) -> dict:
    # 複数フィールドを同時更新
    return {
        "output": "完了",
        "count": state["count"] + 1,
        "intermediate": "中間データ"
    }
```

### よくある疑問: 全フィールドを返す必要は?

**A: ありません！更新したいフィールドだけ返せばOK**

```python
# ✅ これでOK（outputだけ更新）
def node1(state: State) -> dict:
    return {"output": "結果"}

# ✅ これもOK（countだけ更新）
def node2(state: State) -> dict:
    return {"count": state["count"] + 1}

# ❌ これは冗長（不要）
def node3(state: State) -> dict:
    return {
        "input": state["input"],    # 更新してないのに返している
        "output": "結果",
        "count": state["count"]     # 更新してないのに返している
    }
```

---

## 1-4. START/ENDの真実

### よくある誤解を解消

#### 誤解1: "STARTとENDは書かないといけない"

**真実: 書かなくても動く、でも99%書く**

```python
# ❌ 理論上は動くが、実践では使わない
workflow = StateGraph(State)
workflow.add_node("node1", func1)
workflow.add_node("node2", func2)
workflow.add_edge("node1", "node2")
app = workflow.compile()

# ✅ 実践ではこう書く
workflow = StateGraph(State)
workflow.add_node("node1", func1)
workflow.add_node("node2", func2)
workflow.add_edge(START, "node1")  # 明示的な開始点
workflow.add_edge("node2", END)     # 明示的な終了点
app = workflow.compile()
```

#### 誤解2: "__start__を使うべき"

**真実: 絶対に使わない**

```python
# ❌ 絶対にこう書かない
workflow.add_edge("__start__", "node1")

# ✅ 必ずこう書く
workflow.add_edge(START, "node1")
```

**なぜ?**

| 項目 | `START` | `__start__` |
|------|---------|-------------|
| 用途 | コードで使う | グラフ表示のみ |
| 公開API | ✅ はい | ❌ いいえ |
| 推奨 | ✅ 推奨 | ❌ 非推奨 |

#### 誤解3: "STARTとENDは特別なノード"

**真実: ただのマーカー（定数）**

```python
from langgraph.graph import START, END

# 実際の実装（簡略版）
START = "__start__"  # 単なる文字列定数
END = "__end__"      # 単なる文字列定数

# だからこう使える
workflow.add_edge(START, "first")  # "__start__" → "first"
workflow.add_edge("last", END)     # "last" → "__end__"
```

### グラフ可視化での表示

**コードとグラフ表示の対応表**

| コードで書く | グラフで表示 |
|------------|-------------|
| `START` | `__start__` |
| `"my_node"` | `my_node` |
| `"処理1"` | `処理1` |
| `END` | `__end__` |

**例:**

```python
workflow.add_edge(START, "analyze")
workflow.add_edge("analyze", "process")
workflow.add_edge("process", END)
```

**グラフ表示:**
```
__start__ → analyze → process → __end__
```

### 実践的な使い方

```python
import os
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

# APIキー設定
os.environ["GEMINI_API_KEY"] = "your-api-key"

class State(TypedDict):
    data: str

def node_a(state: State) -> dict:
    return {"data": state["data"] + " → A"}

def node_b(state: State) -> dict:
    return {"data": state["data"] + " → B"}

# ✅ 推奨パターン
workflow = StateGraph(State)
workflow.add_node("a", node_a)
workflow.add_node("b", node_b)

# 明示的な開始と終了
workflow.add_edge(START, "a")
workflow.add_edge("a", "b")
workflow.add_edge("b", END)

app = workflow.compile()

result = app.invoke({"data": "開始"})
print(result["data"])  # "開始 → A → B"
```

---

# 第2章: 最小構成の実装

## 2-1. 17行で動く最小コード

### 絶対最小限のコード

```python
import os
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

os.environ["GEMINI_API_KEY"] = "your-actual-api-key-here"

class State(TypedDict):
    output: str

llm = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp"
)

workflow = StateGraph(State)
workflow.add_node("llm", lambda s: {"output": llm.invoke([HumanMessage("こんにちは")]).content})
workflow.add_edge(START, "llm")
workflow.add_edge("llm", END)
app = workflow.compile()

print(app.invoke({"output": ""})["output"])
```

**これが動く最小単位です。以降はこれを読みやすく展開していきます。**

---

## 2-2. 実践的な基本実装

### ステップ1: インポート

```python
import os
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
```

**各インポートの役割:**

| モジュール | 必須? | 役割 |
|-----------|------|------|
| `os` | 🔴必須 | 環境変数の設定・取得 |
| `TypedDict` | 🔴 | Stateの型定義 |
| `StateGraph` | 🔴 | ワークフローの作成 |
| `START, END` | 🟡推奨 | 開始・終了マーカー |
| `ChatGoogleGenerativeAI` | 🔴 | Gemini LLMクライアント |
| `HumanMessage` | 🔴 | LLMへのメッセージ形式 |

### ステップ2: APIキー設定

```python
import os

# APIキー設定（必須）
os.environ["GEMINI_API_KEY"] = "AIza..."

# 検証
if not os.environ.get("GEMINI_API_KEY"):
    raise ValueError("❌ APIキーが設定されていません")

print(f"✅ APIキー設定OK: {os.environ['GEMINI_API_KEY'][:10]}...")
```

### ステップ3: State定義

```python
class State(TypedDict):
    input: str   # ユーザー入力
    output: str  # LLM出力
```

**Stateのベストプラクティス:**

```python
# ✅ 明確なフィールド名
class State(TypedDict):
    user_query: str
    llm_response: str
    search_results: str
    final_answer: str

# ❌ 曖昧なフィールド名
class State(TypedDict):
    data: str
    result: str
    info: str
```

### ステップ4: LLM初期化

```python
llm = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],  # APIキー明示
    model="gemini-2.0-flash-exp",                 # モデル指定
    temperature=0.7,                              # 創造性（0〜1）
    max_tokens=1024                               # 最大トークン数
)
```

**パラメータ解説:**

| パラメータ | デフォルト | 説明 | 推奨値 |
|-----------|----------|------|-------|
| `google_api_key` | 環境変数 | APIキー | 明示推奨 |
| `model` | - | 使用モデル | `gemini-2.0-flash-exp` |
| `temperature` | 1.0 | ランダム性 | 0.7（バランス型） |
| `max_tokens` | - | 出力上限 | 1024〜2048 |

**temperatureの選び方:**

```python
# 事実ベースの回答
llm_factual = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0.1  # ほぼ決定的
)

# バランス型
llm_balanced = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0.7
)

# 創造的な出力
llm_creative = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0.9
)
```

### ステップ5: ノード関数定義

```python
def call_gemini(state: State) -> dict:
    """
    Gemini APIを呼び出すノード
    
    Args:
        state: 現在のワークフロー状態
        
    Returns:
        dict: 更新するフィールド
    """
    # 1. 入力取得
    user_input = state["input"]
    
    # 2. LLM呼び出し
    response = llm.invoke([HumanMessage(content=user_input)])
    
    # 3. 結果を返す
    return {"output": response.content}
```

**HumanMessageの使い方:**

```python
# 基本形
message = HumanMessage(content="こんにちは")

# 複数メッセージ
from langchain_core.messages import SystemMessage

messages = [
    SystemMessage(content="あなたは親切なアシスタントです"),
    HumanMessage(content="LangGraphについて教えて")
]
response = llm.invoke(messages)
```

### ステップ6: グラフ構築

```python
# 1. グラフ作成
workflow = StateGraph(State)

# 2. ノード追加
workflow.add_node("gemini", call_gemini)

# 3. エッジ追加（フロー定義）
workflow.add_edge(START, "gemini")  # 開始 → gemini
workflow.add_edge("gemini", END)     # gemini → 終了

# 4. コンパイル
app = workflow.compile()
```

**add_nodeの柔軟性:**

```python
# パターン1: 関数を渡す
def my_func(state: State) -> dict:
    return {"output": "結果"}
workflow.add_node("node1", my_func)

# パターン2: ラムダ式
workflow.add_node("node2", lambda s: {"output": "結果"})

# パターン3: クラスメソッド
class MyProcessor:
    def process(self, state: State) -> dict:
        return {"output": "結果"}

processor = MyProcessor()
workflow.add_node("node3", processor.process)
```

### ステップ7: 実行

```python
# 最小実行
result = app.invoke({"input": "こんにちは", "output": ""})
print(result["output"])

# 実践的な実行関数
def run_workflow(app, user_input: str, verbose: bool = True):
    """ワークフローを実行"""
    if verbose:
        print(f"📝 入力: {user_input}")
    
    result = app.invoke({"input": user_input, "output": ""})
    
    if verbose:
        print(f"✅ 出力: {result['output']}")
    
    return result

# 使用例
run_workflow(app, "LangGraphの特徴を教えてください")
```

---

## 2-3. グラフ可視化の実装

### 可視化関数（汎用版）

```python
def visualize_graph(app, filename: str = "workflow.png", show_ascii: bool = False):
    """
    ワークフローグラフを可視化
    
    Args:
        app: コンパイル済みアプリ
        filename: 保存ファイル名
        show_ascii: PNG失敗時にASCII版を表示
    """
    print(f"\n📊 グラフを可視化中...")
    
    try:
        # PNG生成
        png_data = app.get_graph().draw_mermaid_png()
        
        # ファイル保存
        with open(filename, "wb") as f:
            f.write(png_data)
        
        print(f"✅ '{filename}' に保存しました")
        
    except Exception as e:
        print(f"⚠️ PNG保存失敗: {e}")
        
        if show_ascii:
            print("\n📝 ASCII版グラフ:")
            print(app.get_graph().draw_ascii())
```

### 使用例

```python
# 基本使用
visualize_graph(app)

# カスタムファイル名
visualize_graph(app, filename="my_workflow.png")

# ASCII版も表示
visualize_graph(app, show_ascii=True)
```

### グラフ構造の理解

```python
import os
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

os.environ["GEMINI_API_KEY"] = "your-api-key"

class State(TypedDict):
    data: str

workflow = StateGraph(State)
workflow.add_node("process", lambda s: {"data": "処理済み"})
workflow.add_edge(START, "process")
workflow.add_edge("process", END)
app = workflow.compile()
```

**生成されるグラフ:**

```
__start__ → process → __end__
```

**重要ポイント:**
- `START` → グラフでは `__start__`
- `"process"` → グラフでも `process`
- `END` → グラフでは `__end__`

---

## 2-4. よくある質問41選

---

## 基本概念（Q1-Q10）

### Q1: LangGraphとLangChainの違いは？

**簡潔な回答**:
- **LangChain**: 線形の処理チェーン（A → B → C）
- **LangGraph**: グラフ構造のワークフロー（条件分岐、ループ、並列実行が可能）

**詳細**:

LangChainは線形処理に最適ですが、複雑な制御フローには向いていません。

```python
# ❌ LangChainでは条件分岐が困難
chain = prompt | llm | output_parser
result = chain.invoke({"input": "質問"})
# 常に同じフローを実行

# ✅ LangGraphなら条件分岐が簡単
workflow.add_conditional_edges("classify", router, {
    "route_a": "handler_a",
    "route_b": "handler_b"
})
```

**いつLangGraphを選ぶべきか**:
- ✅ ユーザー入力で処理を変える
- ✅ 満足するまでループしたい
- ✅ 複数タスクを並列実行したい
- ✅ 複雑な状態管理が必要

---

### Q2: StateGraphは必須？

**回答**: **はい、絶対必須です。**

```python
# ❌ エラー（StateGraphなし）
workflow.add_node("process", func)  # NameError

# ✅ 必ずStateGraphから始める
from langgraph.graph import StateGraph

workflow = StateGraph(State)
workflow.add_node("process", func)
app = workflow.compile()
```

**StateGraphの役割**:
1. ノードとエッジの管理
2. 実行順序の決定
3. State更新の自動処理
4. グラフの可視化

---

### Q3: TypedDictは必須？

**回答**: 技術的には不要ですが、**99.9%使うべき**です。

**TypedDictを使わない場合の問題**:
- 型安全性がない
- IDEの補完が効かない
- バグの早期発見が困難

**推奨：TypedDict使用**:
```python
from typing import TypedDict

class State(TypedDict):
    user_input: str
    llm_response: str
    confidence: float

def my_node(state: State) -> dict:
    user_text = state["user_input"]  # ✅ IDEが補完
    return {"llm_response": "回答"}
```

---

### Q4: Stateのフィールド数に制限は？

**回答**: **制限はありません。** 1個でも100個でもOKです。

```python
# ✅ ミニマム
class MinimalState(TypedDict):
    input: str
    output: str

# ✅ 複雑
class ComplexState(TypedDict):
    user_id: str
    query: str
    intent: str
    search_results: list
    final_response: str
    # ... 好きなだけ追加可能
```

**ベストプラクティス**: 関連フィールドをグループ化

---

### Q5: STARTとENDは省略できる？

**回答**: 技術的には可能ですが、**実用上は必ず使います。**

```python
# ✅ 明確で実用的
from langgraph.graph import START, END

workflow.add_edge(START, "node1")  # 開始点が明確
workflow.add_edge("node2", END)    # 終了点が明確
```

**使う理由**:
- 開始点・終了点が明確
- 可読性が高い
- デバッグしやすい

---

### Q6: __start__と__end__を直接使える？

**回答**: 技術的には可能ですが、**絶対に使わないでください。**

```python
# ❌ 動くが非推奨
workflow.add_edge("__start__", "node1")

# ✅ 必ずこう書く
from langgraph.graph import START, END
workflow.add_edge(START, "node1")
```

**理由**: 可読性、公式ドキュメントとの一貫性、将来の互換性

---

### Q7: ノード名として__start__や__end__は使える？

**回答**: **使えません（予約語）**。

```python
# ❌ エラー
workflow.add_node("__start__", func)  # ValueError

# ✅ OK
workflow.add_node("start_process", func)
workflow.add_node("initialize", func)
```

---

### Q8: ノード名は日本語でもOK？

**回答**: **完全にOKです！**

```python
# ✅ 日本語ノード名
workflow.add_node("質問受付", receive)
workflow.add_node("LLM処理", process)
workflow.add_node("結果整形", format)
```

**推奨**: 英語 + コメントが国際的
```python
workflow.add_node("classify_intent", classify)  # 意図分類
```

---

### Q9: ノードの追加順序は重要？

**回答**: **いいえ、無関係です。** 実行順序はエッジで決まります。

```python
# ✅ これらは全て同じ動作
# パターン1: 順番通り
workflow.add_node("step1", func1)
workflow.add_node("step2", func2)

# パターン2: 逆順
workflow.add_node("step2", func2)
workflow.add_node("step1", func1)

# 実行順序はエッジで決まる
workflow.add_edge(START, "step1")
workflow.add_edge("step1", "step2")
```

---

### Q10: エッジの追加順序は？

**回答**: **無関係です。** グラフの接続関係のみが重要。

---

## ノード関数（Q11-Q20）

### Q11: ノード関数の引数名はstate固定？

**回答**: **いいえ、任意の名前でOK**（慣例は`state`）。

```python
# ✅ すべて有効
def node1(state: State) -> dict: ...
def node2(s: State) -> dict: ...
def node3(data: State) -> dict: ...
```

**重要**: 型ヒント（`: State`）は必須

---

### Q12: 戻り値は必ずdict？

**回答**: **はい、必ずdict**です。

```python
# ✅ OK
def node(state: State) -> dict:
    return {"output": "結果"}

# ❌ NG
def bad_node(state: State) -> str:
    return "結果"  # エラー
```

---

### Q13: 空のdictを返してもいい？

**回答**: **はい、OKです。** Stateを更新しない場合に使います。

```python
def log_only(state: State) -> dict:
    print(f"ログ: {state}")
    return {}  # 何も更新しない
```

---

### Q14: すべてのフィールドを返す必要は？

**回答**: **いいえ、更新分だけ**返せばOKです。

```python
class State(TypedDict):
    a: str
    b: str
    c: str

# ✅ 良い例: aだけ更新
def node(state: State) -> dict:
    return {"a": "新値"}
# b・cはそのまま保持される
```

---

### Q15: lambda式とdef関数の使い分けは？

**回答**: **1行ならlambda、それ以外はdef関数**。

```python
# ✅ lambda向き
workflow.add_node("inc", lambda s: {"count": s["count"] + 1})

# ✅ def向き
def process(state: State) -> dict:
    result = complex_logic(state["input"])
    return {"output": result}
```

---

### Q16: lambda式で複数行はできる？

**回答**: 技術的には可能ですが、**絶対に推奨しません。**

可読性が最悪になるため、複数行なら必ずdef関数を使いましょう。

---

### Q17: ノード関数内でエラーが起きたら？

**回答**: **ワークフロー全体が停止**します。

**対策**: try-exceptでキャッチ
```python
def safe_node(state: State) -> dict:
    try:
        result = risky_operation(state["input"])
        return {"output": result, "error": None}
    except Exception as e:
        return {"output": None, "error": str(e)}
```

---

### Q18: ノード関数でprintデバッグはできる？

**回答**: **はい、完全にできます。**

```python
def debug_node(state: State) -> dict:
    print(f"入力: {state['input']}")
    result = process(state["input"])
    print(f"出力: {result}")
    return {"output": result}
```

---

### Q19: ノード関数は非同期（async）にできる？

**回答**: **はい、できます。**

```python
async def async_node(state: State) -> dict:
    result = await async_api_call(state["input"])
    return {"output": result}

# 非同期実行
result = await app.ainvoke({"input": "test"})
```

---

### Q20: 同じノードを複数回追加できる？

**回答**: **いいえ、エラー**になります。ノード名は一意。

```python
# ❌ エラー
workflow.add_node("process", func)
workflow.add_node("process", func)  # ValueError

# ✅ 異なる名前で
workflow.add_node("process_1", func)
workflow.add_node("process_2", func)
```

---

## 実行とデバッグ（Q21-Q30）

### Q21: invoke()の引数は？

**回答**: **Stateの初期値をdictで渡します。**

```python
# ✅ 最小限
result = app.invoke({"input": "質問"})

# ✅ 詳細
result = app.invoke({
    "input": "質問",
    "output": "",
    "count": 0
})
```

---

### Q22: 実行結果は何が返る？

**回答**: **最終的なState全体がdict**として返ります。

```python
result = app.invoke({"input": "テスト"})

print(type(result))  # 
print(result)
# {
#     "input": "テスト",
#     "output": "処理済み: テスト",
#     "count": 1
# }
```

---

### Q23: 途中経過を取得できる？

**回答**: **はい、stream()で可能**です。

```python
for chunk in app.stream({"input": "テスト"}):
    print(chunk)
# 各ノードの実行ごとに出力
```

---

### Q24: 実行時間を計測したい

**回答**: `time`モジュールで計測できます。

```python
import time

start = time.time()
result = app.invoke({"input": "質問"})
print(f"実行時間: {time.time() - start:.2f}秒")
```

---

### Q25: エラーハンドリングは？

**回答**: **try-exceptでラップ**します。

```python
try:
    result = app.invoke({"input": "データ"})
    print(f"成功: {result['output']}")
except Exception as e:
    print(f"エラー: {e}")
```

---

### Q26: グラフの実行順序を確認したい

**回答**: **stream()で確認**できます。

```python
for i, chunk in enumerate(app.stream({"input": "データ"}), 1):
    node_name = list(chunk.keys())[0]
    print(f"{i}. {node_name}")
```

---

### Q27: 特定のノードだけ実行できる？

**回答**: **できません。** 常にSTARTからENDまで実行されます。

**代替案**: 条件分岐でスキップ、または最小限のグラフを作る

---

### Q28: 実行をキャンセルできる？

**回答**: **困難**です。タイムアウト設定や最大ステップ数制限で対応。

```python
# 最大ステップ数を制限
result = app.invoke(
    {"input": "データ"},
    config={"recursion_limit": 10}
)
```

---

### Q29: 並列実行は可能？

**回答**: **はい、可能です！**

```python
# 並列開始
workflow.add_edge(START, "task1")
workflow.add_edge(START, "task2")
workflow.add_edge(START, "task3")

# 結合
workflow.add_edge("task1", "merge")
workflow.add_edge("task2", "merge")
workflow.add_edge("task3", "merge")
```

---

### Q30: ストリーミング実行とは？

**回答**: **結果を逐次取得**する実行方法です。

```python
# invoke: 全て完了後に返す
result = app.invoke({"input": "質問"})

# stream: 各ノードごとに返す
for chunk in app.stream({"input": "質問"}):
    print(chunk)  # リアルタイム表示
```

---

## メッセージの使い方（Q31）

### Q31: HumanMessageとSystemMessageの違いは？

**回答**: **役割を定義する重要な要素**です。LangGraphで頻繁に使います。

**基本**:
```python
from langchain_core.messages import SystemMessage, HumanMessage

# SystemMessage: LLMに役割を指示
system = SystemMessage(content="あなたは親切なアシスタントです")

# HumanMessage: ユーザー入力
human = HumanMessage(content="こんにちは")
```

**LangGraphのノード内で使用**:
```python
def process_node(state: State) -> dict:
    messages = [
        SystemMessage(content="簡潔に回答してください。"),
        HumanMessage(content=state["user_input"])
    ]
    response = llm.invoke(messages)
    return {"output": response.content}
```

**SystemMessageの効果**:
```python
# SystemMessageなし → 長い説明
response1 = llm.invoke([HumanMessage("LangGraphとは？")])

# SystemMessageあり → 1文で回答
response2 = llm.invoke([
    SystemMessage(content="1文で答えて"),
    HumanMessage(content="LangGraphとは？")
])
```

---

## グラフ構造（Q32-Q41）

### Q32: グラフに循環（ループ）を作れる？

**回答**: **はい、できます。**

```python
workflow.add_edge("node1", "node2")
workflow.add_edge("node2", "node1")  # ループ

# 注意: 無限ループにならないよう条件分岐が必要
workflow.add_conditional_edges("node2", should_continue, {
    "continue": "node1",
    "end": END
})
```

---

### Q33: 1つのノードから複数のノードに接続できる？

**回答**: **はい、条件分岐で可能**です。

```python
workflow.add_conditional_edges("classify", route, {
    "route_a": "node_a",
    "route_b": "node_b",
    "route_c": "node_c"
})
```

---

### Q34: 複数のノードから1つのノードに接続できる？

**回答**: **はい、できます。**

```python
workflow.add_edge("node1", "merge")
workflow.add_edge("node2", "merge")
workflow.add_edge("node3", "merge")
```

---

### Q35: グラフを動的に変更できる？

**回答**: **compile()前なら可能、compile()後は不可**。

```python
workflow.add_node("node1", func1)
workflow.add_node("node2", func2)  # ここまでOK

app = workflow.compile()  # この後は変更不可
```

---

### Q36: グラフの深さに制限は？

**回答**: **実質的な制限はありません**が、深すぎると実行時間が長くなります。

---

### Q37: 並列ノードは作れる？

**回答**: **はい、できます。**

```python
# 並列開始
workflow.add_edge(START, "parallel1")
workflow.add_edge(START, "parallel2")
workflow.add_edge(START, "parallel3")

# 統合
workflow.add_edge("parallel1", "merge")
workflow.add_edge("parallel2", "merge")
workflow.add_edge("parallel3", "merge")
```

---

### Q38: グラフ可視化は必須？

**回答**: **いいえ、オプション**ですが、複雑なグラフでは強く推奨します。

```python
# PNG保存
png_data = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png_data)

# ASCII版
print(app.get_graph().draw_ascii())
```

---

### Q39: PNGが生成できない場合は？

**回答**: **ASCII版で表示**できます。

```python
print(app.get_graph().draw_ascii())
```

---

### Q40: グラフをJupyter Notebookで表示したい

**回答**: IPythonのImage機能を使います。

```python
from IPython.display import Image, display

png_data = app.get_graph().draw_mermaid_png()
display(Image(png_data))
```

---

### Q41: グラフの実行順序はどう決まる？

**回答**: **エッジで定義した接続順序**に従います。

STARTから辿れるノードを探し、エッジに従って次のノードへ進み、ENDに到達するまで続けます。

```python
# この接続
workflow.add_edge(START, "a")
workflow.add_edge("a", "b")
workflow.add_edge("b", "c")
workflow.add_edge("c", END)

# この実行順序
# START → a → b → c → END
```

```

---

### 完全な実装例（第2章）

```python
"""
第2章完全実装 - コピー&ペーストで動きます
"""

import os
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# ============================================
# APIキー設定
# ============================================

os.environ["GEMINI_API_KEY"] = "your-actual-api-key"  # ← 実際のキーに変更

if os.environ.get("GEMINI_API_KEY") == "your-actual-api-key":
    raise ValueError("❌ APIキーを設定してください")

# ============================================
# State定義
# ============================================

class State(TypedDict):
    input: str
    output: str

# ============================================
# LLM初期化
# ============================================

llm = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0.7,
    max_tokens=1024
)

# ============================================
# ノード関数
# ============================================

def call_gemini(state: State) -> dict:
    """Gemini APIを呼び出す"""
    print(f"📝 入力: {state['input']}")
    
    response = llm.invoke([HumanMessage(content=state["input"])])
    
    print(f"✅ 応答受信完了")
    return {"output": response.content}

# ============================================
# グラフ構築
# ============================================

workflow = StateGraph(State)
workflow.add_node("gemini", call_gemini)
workflow.add_edge(START, "gemini")
workflow.add_edge("gemini", END)

app = workflow.compile()

print("✅ ワークフロー構築完了")

# ============================================
# グラフ可視化
# ============================================

def visualize_graph(app, filename="workflow.png"):
    """グラフをPNG保存"""
    try:
        png_data = app.get_graph().draw_mermaid_png()
        with open(filename, "wb") as f:
            f.write(png_data)
        print(f"✅ グラフを '{filename}' に保存")
    except Exception as e:
        print(f"⚠️ PNG保存失敗: {e}")
        print(app.get_graph().draw_ascii())

visualize_graph(app, "ch2_workflow.png")

# ============================================
# 実行関数
# ============================================

def run_workflow(app, user_input: str):
    """ワークフローを実行"""
    print("\n" + "=" * 60)
    print("🚀 実行開始")
    print("=" * 60)
    
    result = app.invoke({"input": user_input, "output": ""})
    
    print("=" * 60)
    print("✅ 完了")
    print("=" * 60)
    print(f"\n📤 結果:\n{result['output']}\n")
    
    return result

# ============================================
# 実行
# ============================================

if __name__ == "__main__":
    run_workflow(app, "LangGraphの主な特徴を3つ教えてください")
```

---

## 第3章: 条件分岐の実装【完全解説】

### 3-1. 条件分岐の基本概念

#### なぜ条件分岐が必要なのか

実際のアプリケーションでは、**入力内容によって処理を変える必要**があります。

**例: カスタマーサポートボット**
```
ユーザー入力「パスワードを忘れました」
  ↓
意図分類「パスワードリセット」
  ↓
FAQ検索 → 自動回答

ユーザー入力「商品が壊れています！」
  ↓
意図分類「クレーム」
  ↓
緊急チケット作成 → 人間にエスカレーション
```

**線形フローでは不可能**
```python
# ❌ これではすべて同じ処理になってしまう
workflow.add_edge(START, "process")
workflow.add_edge("process", END)
```

**条件分岐で実現**
```python
# ✅ 入力に応じて処理を変える
workflow.add_conditional_edges("classify", router, {
    "password_reset": "faq_node",
    "complaint": "escalate_node",
    "question": "answer_node"
})
```

---

#### add_conditional_edges() の完全理解

**構文の分解**
```python
workflow.add_conditional_edges(
    source="判定を行うノード名",        # ①
    path=ルーティング関数,              # ②
    path_map={                         # ③
        "ルート名A": "遷移先ノードA",
        "ルート名B": "遷移先ノードB",
        "ルート名C": END
    }
)
```

**① source（判定を行うノード）**
- このノードの**実行後**に条件分岐が発生
- 文字列でノード名を指定

**② path（ルーティング関数）**
- Stateを受け取り、**次に進むルート名を返す関数**
- 必ず文字列を返す
- この戻り値がpath_mapのキーと一致する必要がある

**③ path_map（ルートマッピング）**
- キー: ルーティング関数が返す文字列
- 値: 次に実行するノード名（またはEND）

---

### 3-2. 最小の条件分岐実装（ステップバイステップ）

#### ステップ1: 要件定義

**目標**: ユーザー入力を「挨拶」「質問」「その他」に分類して、それぞれ異なる処理を行う

**フロー設計**
```
START
  ↓
classify（分類ノード）
  ↓
条件分岐
  ├─ "greeting" → greeting_node → END
  ├─ "question" → question_node → END
  └─ "other" → other_node → END
```

---

#### ステップ2: State設計

```python
from typing import TypedDict

class State(TypedDict):
    input: str       # ユーザー入力
    category: str    # 分類結果（greeting/question/other）
    output: str      # 最終的な応答
```

**重要ポイント**:
- `category`は分岐判定に使用
- ノード関数で`category`を更新し、ルーティング関数で読み取る

---

#### ステップ3: 分類ノード実装

```python
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

os.environ["GEMINI_API_KEY"] = "your-api-key"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0.0  # 分類は決定的にする
)

def classify(state: State) -> dict:
    """ユーザー入力を分類する"""
    
    # LLMに分類を依頼
    messages = [
        SystemMessage(content="""
あなたは入力分類の専門家です。
以下のルールに従って分類してください:

- 「こんにちは」「おはよう」など → greeting
- 疑問文や説明を求める内容 → question  
- 上記以外 → other

必ず「greeting」「question」「other」のいずれか1つだけを返してください。
余計な説明は不要です。
        """),
        HumanMessage(content=f"分類対象: {state['input']}")
    ]
    
    response = llm.invoke(messages)
    category = response.content.strip().lower()
    
    # 予期しない値の場合はotherにフォールバック
    if category not in ["greeting", "question", "other"]:
        category = "other"
    
    return {"category": category}
```

**ポイント解説**:
1. **temperature=0.0**: 分類は一貫性が重要なので決定的にする
2. **SystemMessage**: LLMに明確な指示を与える
3. **フォールバック処理**: 予期しない値への対策（重要！）

---

#### ステップ4: ルーティング関数の実装

```python
from typing import Literal

def route_by_category(state: State) -> Literal["greeting", "question", "other"]:
    """分類結果に基づいてルートを決定"""
    return state["category"]
```

**重要な理解**:
- この関数は**シンプルでOK**
- 複雑なロジックは分類ノードで実装済み
- ルーティング関数は単に結果を返すだけ

**Literalの役割**:
```python
# ✅ 型安全（IDEが補完してくれる）
def route(state: State) -> Literal["greeting", "question", "other"]:
    return state["category"]

# ❌ 型ヒントなし（動くが推奨しない）
def route(state: State):
    return state["category"]
```

---

#### ステップ5: 各ルートの処理ノード実装

```python
def handle_greeting(state: State) -> dict:
    """挨拶への応答"""
    return {
        "output": "こんにちは！何かお手伝いできることはありますか？"
    }

def handle_question(state: State) -> dict:
    """質問への応答"""
    # LLMを使って質問に回答
    response = llm.invoke([
        SystemMessage(content="親切で分かりやすく回答してください。"),
        HumanMessage(content=state["input"])
    ])
    return {"output": response.content}

def handle_other(state: State) -> dict:
    """その他への応答"""
    return {
        "output": "申し訳ございません、理解できませんでした。もう一度お願いします。"
    }
```

**設計のポイント**:
- `handle_greeting`: シンプルな定型応答（LLM不要）
- `handle_question`: LLMで動的に回答生成
- `handle_other`: フォールバック処理

---

#### ステップ6: グラフの組み立て

```python
from langgraph.graph import StateGraph, START, END

# グラフ作成
workflow = StateGraph(State)

# ノード追加
workflow.add_node("classify", classify)
workflow.add_node("greeting", handle_greeting)
workflow.add_node("question", handle_question)
workflow.add_node("other", handle_other)

# エッジ追加
workflow.add_edge(START, "classify")  # 開始点

# 条件分岐（重要！）
workflow.add_conditional_edges(
    source="classify",          # 分類ノードの後で分岐
    path=route_by_category,     # ルーティング関数
    path_map={                  # ルートマッピング
        "greeting": "greeting",  # キー=関数の戻り値, 値=ノード名
        "question": "question",
        "other": "other"
    }
)

# 各ルートの終了
workflow.add_edge("greeting", END)
workflow.add_edge("question", END)
workflow.add_edge("other", END)

# コンパイル
app = workflow.compile()
```

**グラフ構造の可視化**:
```
__start__
    ↓
classify
    ↓
  [条件分岐]
    ├─ greeting → __end__
    ├─ question → __end__
    └─ other → __end__
```

---

#### ステップ7: テストと実行

```python
# テストケース
test_inputs = [
    "こんにちは",
    "LangGraphとは何ですか？",
    "あいうえお12345",
    "おはようございます",
    "条件分岐の仕組みを教えて"
]

for user_input in test_inputs:
    result = app.invoke({
        "input": user_input,
        "category": "",  # 初期値
        "output": ""     # 初期値
    })
    
    print(f"入力: {user_input}")
    print(f"分類: {result['category']}")
    print(f"応答: {result['output']}")
    print("-" * 60)
```

**実行結果例**:
```
入力: こんにちは
分類: greeting
応答: こんにちは！何かお手伝いできることはありますか？
------------------------------------------------------------
入力: LangGraphとは何ですか？
分類: question
応答: LangGraphは、LangChainの上に構築された...（LLMの回答）
------------------------------------------------------------
入力: あいうえお12345
分類: other
応答: 申し訳ございません、理解できませんでした。もう一度お願いします。
------------------------------------------------------------
```

---

#### 完全なコード（コピペ可能）

```python
import os
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# APIキー設定
os.environ["GEMINI_API_KEY"] = "your-api-key"

# State定義
class State(TypedDict):
    input: str
    category: str
    output: str

# LLM初期化
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.0)

# ノード1: 分類
def classify(state: State) -> dict:
    messages = [
        SystemMessage(content="""
入力を分類してください:
- greeting: 挨拶
- question: 質問
- other: その他
1単語のみ返してください。
        """),
        HumanMessage(content=state["input"])
    ]
    response = llm.invoke(messages)
    category = response.content.strip().lower()
    if category not in ["greeting", "question", "other"]:
        category = "other"
    return {"category": category}

# ルーティング関数
def route_by_category(state: State) -> Literal["greeting", "question", "other"]:
    return state["category"]

# ノード2a: 挨拶処理
def handle_greeting(state: State) -> dict:
    return {"output": "こんにちは！何かお手伝いできることはありますか？"}

# ノード2b: 質問処理
def handle_question(state: State) -> dict:
    response = llm.invoke([
        SystemMessage(content="親切に回答してください。"),
        HumanMessage(content=state["input"])
    ])
    return {"output": response.content}

# ノード2c: その他
def handle_other(state: State) -> dict:
    return {"output": "申し訳ございません、理解できませんでした。"}

# グラフ構築
workflow = StateGraph(State)
workflow.add_node("classify", classify)
workflow.add_node("greeting", handle_greeting)
workflow.add_node("question", handle_question)
workflow.add_node("other", handle_other)

workflow.add_edge(START, "classify")
workflow.add_conditional_edges("classify", route_by_category, {
    "greeting": "greeting",
    "question": "question",
    "other": "other"
})
workflow.add_edge("greeting", END)
workflow.add_edge("question", END)
workflow.add_edge("other", END)

app = workflow.compile()

# テスト
test_inputs = ["こんにちは", "LangGraphとは?", "12345"]
for text in test_inputs:
    result = app.invoke({"input": text, "category": "", "output": ""})
    print(f"入力: {text} | 分類: {result['category']} | 応答: {result['output'][:50]}...")
```

---

### 3-3. よくある間違いとデバッグ

#### 間違い1: ルートマッピングの不一致

```python
# ❌ エラー例
def route(state: State) -> Literal["greet", "quest", "other"]:
    if state["category"] == "greeting":
        return "greet"  # ここで"greet"を返す
    elif state["category"] == "question":
        return "quest"
    return "other"

workflow.add_conditional_edges("classify", route, {
    "greeting": "greeting_node",  # キーが"greeting"だがルーティング関数は"greet"を返す
    "question": "question_node",  # キーが"question"だがルーティング関数は"quest"を返す
    "other": "other_node"
})
# → KeyError: 'greet' が発生
```

**修正方法**:
```python
# ✅ 正しい実装
def route(state: State) -> Literal["greeting", "question", "other"]:
    return state["category"]  # Stateのcategoryをそのまま返す

workflow.add_conditional_edges("classify", route, {
    "greeting": "greeting_node",  # キーと戻り値が一致
    "question": "question_node",
    "other": "other_node"
})
```

---

#### 間違い2: すべてのケースをカバーしていない

```python
# ❌ エラー例
def route(state: State) -> Literal["greeting", "question", "other"]:
    return state["category"]

workflow.add_conditional_edges("classify", route, {
    "greeting": "greeting_node",
    "question": "question_node"
    # "other"のケースが抜けている
})
# → state["category"]が"other"のときKeyError
```

**修正方法**:
```python
# ✅ すべてのケースをカバー
workflow.add_conditional_edges("classify", route, {
    "greeting": "greeting_node",
    "question": "question_node",
    "other": "other_node"  # 忘れずに追加
})
```

---

#### 間違い3: ルーティング関数で直接分岐ロジックを書く

```python
# ❌ アンチパターン（動くが保守性が悪い）
def route(state: State) -> Literal["route_a", "route_b"]:
    user_input = state["input"]
    
    # ルーティング関数内で複雑なロジック
    if "こんにちは" in user_input or "おはよう" in user_input:
        return "route_a"
    elif "？" in user_input or "教えて" in user_input:
        return "route_b"
    else:
        return "route_a"
```

**推奨パターン**:
```python
# ✅ ベストプラクティス
# 1. 分類ノードで判定
def classify(state: State) -> dict:
    # ここで複雑なロジックを実装
    category = complex_classification_logic(state["input"])
    return {"category": category}

# 2. ルーティング関数はシンプルに
def route(state: State) -> Literal["route_a", "route_b"]:
    return state["category"]
```

**理由**:
- 分類ロジックの再利用が容易
- テストがしやすい
- コードの可読性が高い

---

### 3-4. 複数条件での高度なルーティング

#### スコアベースの分岐

**ユースケース**: 信頼度スコアに応じて処理を変える

```python
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
import os

os.environ["GEMINI_API_KEY"] = "your-api-key"

class State(TypedDict):
    query: str
    confidence_score: float  # 0.0〜1.0
    answer: str

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.3)

# ステップ1: 信頼度を評価
def evaluate_confidence(state: State) -> dict:
    """質問の難易度を評価してスコアを算出"""
    
    messages = [
        SystemMessage(content="""
あなたは質問の難易度評価の専門家です。
以下の基準でスコアを0.0〜1.0で評価してください:

0.0-0.3: 簡単（一般常識で答えられる）
  例: "こんにちは", "今日の天気は?"
  
0.4-0.7: 中程度（ある程度の知識が必要）
  例: "LangGraphの基本的な使い方は?", "Pythonでリストをソートする方法は?"
  
0.8-1.0: 難しい（専門知識が必要）
  例: "量子コンピューティングの原理を説明して", "transformerモデルのattention機構の数式を導出して"

必ず0.0〜1.0の数値のみを返してください。説明は不要です。
        """),
        HumanMessage(content=f"評価対象: {state['query']}")
    ]
    
    response = llm.invoke(messages)
    
    try:
        score = float(response.content.strip())
        # 範囲チェック
        score = max(0.0, min(1.0, score))
    except ValueError:
        # パースに失敗した場合は中間値
        score = 0.5
    
    return {"confidence_score": score}

# ステップ2: スコアに基づいてルーティング
def route_by_confidence(state: State) -> Literal["simple", "moderate", "complex"]:
    """信頼度スコアに基づいてルートを決定"""
    score = state["confidence_score"]
    
    if score < 0.4:
        return "simple"
    elif score < 0.8:
        return "moderate"
    else:
        return "complex"

# ステップ3: 各難易度に応じた処理
def handle_simple(state: State) -> dict:
    """簡単な質問への応答"""
    llm_simple = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # 軽量モデル
        temperature=0.7,
        max_tokens=256  # 短い応答
    )
    
    response = llm_simple.invoke([
        SystemMessage(content="簡潔に1-2文で回答してください。"),
        HumanMessage(content=state["query"])
    ])
    
    return {"answer": f"[簡易回答] {response.content}"}

def handle_moderate(state: State) -> dict:
    """中程度の質問への応答"""
    response = llm.invoke([
        SystemMessage(content="分かりやすく、適度な詳しさで説明してください。"),
        HumanMessage(content=state["query"])
    ])
    
    return {"answer": f"[標準回答] {response.content}"}

def handle_complex(state: State) -> dict:
    """難しい質問への応答"""
    llm_advanced = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",  # 高性能モデル
        temperature=0.3,
        max_tokens=2048  # 詳細な応答
    )
    
    response = llm_advanced.invoke([
        SystemMessage(content="""
専門的かつ包括的に説明してください。
必要に応じて以下を含めてください:
- 背景知識
- 詳細な説明
- 具体例
- 関連する概念
        """),
        HumanMessage(content=state["query"])
    ])
    
    return {"answer": f"[詳細回答] {response.content}"}

# グラフ構築
workflow = StateGraph(State)

workflow.add_node("evaluate", evaluate_confidence)
workflow.add_node("simple", handle_simple)
workflow.add_node("moderate", handle_moderate)
workflow.add_node("complex", handle_complex)

workflow.add_edge(START, "evaluate")

workflow.add_conditional_edges(
    source="evaluate",
    path=route_by_confidence,
    path_map={
        "simple": "simple",
        "moderate": "moderate",
        "complex": "complex"
    }
)

workflow.add_edge("simple", END)
workflow.add_edge("moderate", END)
workflow.add_edge("complex", END)

app = workflow.compile()

# テスト
test_queries = [
    "こんにちは",
    "LangGraphの基本的な使い方を教えて",
    "量子もつれの数学的定式化とベル不等式の導出過程を説明してください"
]

for query in test_queries:
    result = app.invoke({
        "query": query,
        "confidence_score": 0.0,
        "answer": ""
    })
    
    print(f"\n{'='*70}")
    print(f"質問: {query}")
    print(f"難易度スコア: {result['confidence_score']:.2f}")
    print(f"回答: {result['answer'][:100]}...")
```

**実行結果例**:
```
======================================================================
質問: こんにちは
難易度スコア: 0.15
回答: [簡易回答] こんにちは！何かお手伝いできることはありますか？
======================================================================
質問: LangGraphの基本的な使い方を教えて
難易度スコア: 0.55
回答: [標準回答] LangGraphは、複雑なAIワークフローをグラフ構造で表現するフレームワークです...
======================================================================
質問: 量子もつれの数学的定式化とベル不等式の導出過程を説明してください
難易度スコア: 0.95
回答: [詳細回答] 量子もつれ(quantum entanglement)は、2つ以上の量子系が分離不可能な状態...
```

---

### 3-5. 実践例: カスタマーサポートボット（完全実装）

#### 要件定義

**機能要件**:
1. ユーザーメッセージの意図を分類（問い合わせ/クレーム/要望/フィードバック）
2. 感情分析（ポジティブ/ニュートラル/ネガティブ）
3. 優先度判定（高/中/低）
4. 優先度に応じた応答生成

**フロー設計**:
```
START → analyze → 
  ├─ high priority → urgent_response → END
  ├─ medium priority → standard_response → END
  └─ low priority → basic_response → END
```

---

#### 完全実装

```python
import os
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

os.environ["GEMINI_API_KEY"] = "your-api-key"

# State定義
class SupportState(TypedDict):
    message: str        # ユーザーメッセージ
    intent: str         # 意図（inquiry/complaint/request/feedback）
    sentiment: str      # 感情（positive/neutral/negative）
    priority: str       # 優先度（high/medium/low）
    response: str       # 最終応答
    analysis_detail: str  # 分析の詳細（デバッグ用）

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.3)

# ノード1: メッセージ分析
def analyze_message(state: SupportState) -> dict:
    """ユーザーメッセージを多角的に分析"""
    
    message = state["message"]
    
    # 意図分類
    intent_prompt = """
以下のカテゴリに分類してください:
- inquiry: 製品やサービスについての問い合わせ
- complaint: 不満やクレーム
- request: 新機能や改善の要望
- feedback: 一般的なフィードバック

入力: {message}

必ず上記4つのうち1つだけを返してください。
    """.format(message=message)
    
    intent_response = llm.invoke([HumanMessage(content=intent_prompt)])
    intent = intent_response.content.strip().lower()
    
    # バリデーション
    valid_intents = ["inquiry", "complaint", "request", "feedback"]
    if intent not in valid_intents:
        intent = "inquiry"  # デフォルト
    
    # 感情分析
    sentiment_prompt = """
以下のメッセージの感情を分析してください:
- positive: ポジティブな内容
- neutral: 中立的な内容
- negative: ネガティブな内容

入力: {message}

必ず上記3つのうち1つだけを返してください。
    """.format(message=message)
    
    sentiment_response = llm.invoke([HumanMessage(content=sentiment_prompt)])
    sentiment = sentiment_response.content.strip().lower()
    
    # バリデーション
    valid_sentiments = ["positive", "neutral", "negative"]
    if sentiment not in valid_sentiments:
        sentiment = "neutral"
    
    # 優先度判定ロジック
    if intent == "complaint" or sentiment == "negative":
        priority = "high"
    elif intent == "inquiry":
        priority = "medium"
    else:
        priority = "low"
    
    # 分析詳細を記録（デバッグ用）
    analysis_detail = f"意図={intent}, 感情={sentiment}, 優先度={priority}"
    
    return {
        "intent": intent,
        "sentiment": sentiment,
        "priority": priority,
        "analysis_detail": analysis_detail
    }

# ルーティング関数
def route_by_priority(state: SupportState) -> Literal["high", "medium", "low"]:
    """優先度に基づいてルーティング"""
    return state["priority"]

# 高優先度対応
def handle_high_priority(state: SupportState) -> dict:
    """緊急対応が必要なケース"""
    
    messages = [
        SystemMessage(content="""
あなたは経験豊富なカスタマーサポートのシニアスタッフです。
クレームや緊急の問い合わせに対応しています。

以下の点に注意して応答してください:
1. 誠実な謝罪から始める
2. 問題を理解していることを示す
3. 具体的な解決策を提示
4. 迅速な対応を約束
5. エスカレーションの手順を案内
        """),
        HumanMessage(content=state["message"])
    ]
    
    response = llm.invoke(messages)
    
    return {
        "response": f"【緊急対応】\n{response.content}\n\n※このメッセージは優先的に処理され、担当者に即座にエスカレーションされました。"
    }

# 中優先度対応
def handle_medium_priority(state: SupportState) -> dict:
    """標準的な問い合わせ対応"""
    
    messages = [
        SystemMessage(content="""
あなたは親切で知識豊富なカスタマーサポートスタッフです。
一般的な問い合わせに対応しています。

以下の点に注意して応答してください:
1. 親しみやすく丁寧な口調
2. 質問に正確に回答
3. 必要に応じて追加情報を提供
4. さらなる質問を促す
        """),
        HumanMessage(content=state["message"])
    ]
    
    response = llm.invoke(messages)
    
    return {
        "response": f"【標準対応】\n{response.content}\n\nさらにご不明な点がございましたら、お気軽にお問い合わせください。"
    }

# 低優先度対応
def handle_low_priority(state: SupportState) -> dict:
    """フィードバックや要望への対応"""
    
    messages = [
        SystemMessage(content="""
あなたはフレンドリーなカスタマーサポートスタッフです。
フィードバックや要望に対応しています。

以下の点に注意して応答してください:
1. 感謝の言葉から始める
2. フィードバックを真摯に受け止める姿勢
3. 簡潔かつポジティブな応答
        """),
        HumanMessage(content=state["message"])
    ]
    
    response = llm.invoke(messages)
    
    return {
        "response": f"【フィードバック対応】\n{response.content}\n\n貴重なご意見をありがとうございます！"
    }

# グラフ構築
workflow = StateGraph(SupportState)

# ノード登録
workflow.add_node("analyze", analyze_message)
workflow.add_node("high", handle_high_priority)
workflow.add_node("medium", handle_medium_priority)
workflow.add_node("low", handle_low_priority)

# フロー定義
workflow.add_edge(START, "analyze")

workflow.add_conditional_edges(
    source="analyze",
    path=route_by_priority,
    path_map={
        "high": "high",
        "medium": "medium",
        "low": "low"
    }
)

workflow.add_edge("high", END)
workflow.add_edge("medium", END)
workflow.add_edge("low", END)

app = workflow.compile()

# グラフ可視化
try:
    png_data = app.get_graph().draw_mermaid_png()
    with open("support_bot_graph.png", "wb") as f:
        f.write(png_data)
    print("✅ グラフを 'support_bot_graph.png' に保存しました")
except Exception as e:
    print(f"⚠️ PNG保存失敗: {e}")
    print("\nASCII版グラフ:")
    print(app.get_graph().draw_ascii())

# テストケース
test_messages = [
    "商品が2週間経っても届きません！注文番号12345です。すぐに確認してください！",
    "製品Aの設定方法について教えてください。",
    "このサービス、本当に便利です！いつもありがとうございます。",
    "ダークモード機能を追加してほしいです。",
    "パスワードリセットの方法がわかりません。"
]

print("\n" + "="*80)
print("カスタマーサポートボット - テスト実行")
print("="*80)

for i, msg in enumerate(test_messages, 1):
    result = app.invoke({
        "message": msg,
        "intent": "",
        "sentiment": "",
        "priority": "",
        "response": "",
        "analysis_detail": ""
    })
    
    print(f"\n【テストケース {i}】")
    print(f"メッセージ: {msg}")
    print(f"分析結果: {result['analysis_detail']}")
    print(f"\n応答:\n{result['response']}")
    print("-" * 80)
```

**実行結果例**:
```
================================================================================
カスタマーサポートボット - テスト実行
================================================================================

【テストケース 1】
メッセージ: 商品が2週間経っても届きません！注文番号12345です。すぐに確認してください！
分析結果: 意図=complaint, 感情=negative, 優先度=high

応答:
【緊急対応】
大変申し訳ございません。ご注文の商品がまだお手元に届いていないとのこと、心よりお詫び申し上げます。

注文番号12345について、直ちに配送状況を確認させていただきます...
（省略）

※このメッセージは優先的に処理され、担当者に即座にエスカレーションされました。
--------------------------------------------------------------------------------

【テストケース 2】
メッセージ: 製品Aの設定方法について教えてください。
分析結果: 意図=inquiry, 感情=neutral, 優先度=medium

応答:
【標準対応】
製品Aの設定方法についてご案内いたします...
（省略）

さらにご不明な点がございましたら、お気軽にお問い合わせください。
--------------------------------------------------------------------------------
```

---

### 3-6. 条件分岐のベストプラクティス

#### ✅ DO（推奨）

**1. ルーティング関数はシンプルに**
```python
# ✅ 良い例
def route(state: State) -> Literal["a", "b", "c"]:
    return state["category"]  # Stateから読み取るだけ
```

**2. 型ヒントを必ず使う**
```python
# ✅ 良い例
def route(state: State) -> Literal["route_a", "route_b"]:
    return state["route"]

# ❌ 悪い例
def route(state):  # 型ヒントなし
    return state["route"]
```

**3. すべてのケースをカバー**
```python
# ✅ 良い例
workflow.add_conditional_edges("node", route, {
    "case_a": "handler_a",
    "case_b": "handler_b",
    "case_c": "handler_c"  # すべてのケース
})
```

**4. フォールバック処理を実装**
```python
# ✅ 良い例
def classify(state: State) -> dict:
    response = llm.invoke([...])
    category = response.content.strip().lower()
    
    # 予期しない値への対策
    if category not in ["a", "b", "c"]:
        category = "default"
    
    return {"category": category}
```

---

#### ❌ DON'T（非推奨）

**1. ルーティング関数で複雑なロジック**
```python
# ❌ 悪い例
def route(state: State) -> Literal["a", "b"]:
    # ルーティング関数内で複雑な処理
    result = complex_analysis(state["input"])
    if result > 0.5:
        return "a"
    return "b"
```

**2. マッピングキーと戻り値の不一致**
```python
# ❌ 悪い例
def route(state: State) -> Literal["yes", "no"]:
    return "yes" if state["flag"] else "no"

workflow.add_conditional_edges("node", route, {
    "true": "node_a",   # キーが合わない
    "false": "node_b"
})
```

**3. 一部のケースが抜けている**
```python
# ❌ 悪い例
def route(state: State) -> Literal["a", "b", "c"]:
    return state["category"]

workflow.add_conditional_edges("node", route, {
    "a": "handler_a",
    "b": "handler_b"
    # "c"が抜けている → 実行時エラー
})
```

---

## 第4章: ツール統合【完全解説】

### 4-1. Tavily検索APIの完全理解

#### Tavily検索とは何か

**公式説明**:
Tavilyは、AI向けに最適化された検索APIです。通常の検索エンジンと異なり、LLMが理解しやすいクリーンで構造化されたデータを返します。

**特徴**:
- 🚀 高速: レスポンス時間が短い（通常1-2秒）
- 🎯 正確: AI向けに最適化された関連性の高い結果
- 💰 無料枠: 月間1,000リクエストまで無料
- 🔧 簡単: LangChainと完全統合

**他の検索APIとの比較**:
| 項目 | Tavily | Google Search API | Bing Search API |
|------|--------|-------------------|-----------------|
| 無料枠 | 1,000req/月 | なし | なし |
| AI最適化 | ⭐⭐⭐ | ⭐ | ⭐ |
| LangChain統合 | ネイティブ | 要カスタム | 要カスタム |

---

#### Tavily APIキーの取得（詳細手順）

**ステップ1**: https://tavily.com/ にアクセス

**ステップ2**: 「Get Started」または「Sign Up」をクリック

**ステップ3**: Googleアカウントまたはメールアドレスで登録

**ステップ4**: ダッシュボードで自動生成されたAPIキーをコピー
- キーは `tvly-` で始まる文字列
- 例: `tvly-Abc123XyZ789...`

**ステップ5**: APIキーを環境変数に設定
```python
import os
os.environ["TAVILY_API_KEY"] = "tvly-your-actual-key"
```

または`.env`ファイルに:
```
TAVILY_API_KEY=tvly-your-actual-key
```

---

#### Tavily検索の基本的な使い方

**最小実装**:
```python
import os
from langchain_community.tools.tavily_search import TavilySearchResults

# APIキー設定
os.environ["TAVILY_API_KEY"] = "tvly-your-key"

# 検索ツール初期化
search = TavilySearchResults(
    max_results=3  # 取得する結果の数
)

# 検索実行
results = search.invoke("LangGraphとは")

# 結果表示
for i, result in enumerate(results, 1):
    print(f"\n結果 {i}:")
    print(f"URL: {result['url']}")
    print(f"内容: {result['content'][:100]}...")
    print(f"スコア: {result.get('score', 'N/A')}")
```

**実行結果の構造**:
```python
[
    {
        'url': 'https://example.com/langgraph-intro',
        'content': 'LangGraphは、LangChainの上に構築されたフレームワークで...',
        'score': 0.95  # 関連性スコア（0.0〜1.0）
    },
    {
        'url': 'https://another-site.com/tutorial',
        'content': 'LangGraphを使うことで、複雑なAIワークフロー...',
        'score': 0.87
    },
    ...
]
```

---

#### パラメータの詳細解説

```python
search = TavilySearchResults(
    max_results=5,           # 結果数（1〜10推奨）
    search_depth="basic",    # "basic" or "advanced"
    include_domains=[],      # 特定ドメインのみ（オプション）
    exclude_domains=[],      # 除外ドメイン（オプション）
    include_answer=False,    # 要約を含めるか
    include_raw_content=False  # 生のHTMLを含めるか
)
```

**パラメータ詳細**:

1. **max_results**:
   - 取得する検索結果の数
   - 推奨: 3〜5（バランス重視）
   - 多すぎるとLLMのコンテキストを圧迫

2. **search_depth**:
   - `"basic"`: 高速、表面的な情報
   - `"advanced"`: 詳細、深い分析（遅い）
   - 推奨: 通常は`"basic"`で十分

3. **include_domains** (例):
   ```python
   search = TavilySearchResults(
       max_results=3,
       include_domains=["wikipedia.org", "github.com"]
   )
   ```

4. **exclude_domains** (例):
   ```python
   search = TavilySearchResults(
       max_results=3,
       exclude_domains=["ads-site.com", "spam.com"]
   )
   ```

---

### 4-2. LLMとツールの統合（bind_tools）

#### bind_toolsの仕組み

**概念**:
`bind_tools()`は、LLMに「このツールが使えますよ」と教える機能です。LLMは必要に応じてツールの使用を判断します。

**フロー**:
```
ユーザー「2024年のノーベル賞受賞者は？」
  ↓
LLM「これは最新情報なので検索ツールを使おう」
  ↓
tool_calls を生成
  ↓
ツール実行（Tavily検索）
  ↓
結果をLLMに渡す
  ↓
LLM「検索結果をもとに回答を生成」
```

---

#### 基本的なbind_toolsの使い方

```python
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage

# APIキー設定
os.environ["GEMINI_API_KEY"] = "your-key"
os.environ["TAVILY_API_KEY"] = "your-key"

# LLM初期化
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0
)

# ツール初期化
search_tool = TavilySearchResults(max_results=3)

# ツールをLLMにバインド
llm_with_tools = llm.bind_tools([search_tool])

# 実行
response = llm_with_tools.invoke([
    HumanMessage(content="2024年のノーベル物理学賞受賞者は？")
])

# ツール使用判定
if hasattr(response, "tool_calls") and response.tool_calls:
    print("✅ LLMがツール使用を決定しました")
    print(f"ツール名: {response.tool_calls[0]['name']}")
    print(f"引数: {response.tool_calls[0]['args']}")
else:
    print("❌ LLMはツールを使用しませんでした")
    print(f"直接回答: {response.content}")
```

**重要な理解**:
- `bind_tools()`は**リストを受け取る**（複数ツール対応）
- LLMが自動的にツールの使用を判断
- `tool_calls`属性の有無でツール使用を確認

---

#### tool_callsの詳細

```python
# tool_callsの構造
response.tool_calls = [
    {
        'name': 'tavily_search_results_json',
        'args': {'query': '2024 ノーベル物理学賞'},
        'id': 'call_abc123'
    }
]
```

**フィールド解説**:
- `name`: 使用するツールの名前
- `args`: ツールに渡す引数（dict形式）
- `id`: ツール呼び出しの一意ID

---

### 4-3. エージェントループの完全実装

#### エージェントループとは

**定義**:
LLMとツールが**協調動作**して、タスクを完遂するパターンです。

**フロー図**:
```
START
  ↓
agent (LLMがツール使用を判断)
  ↓
ツール必要? 
  ├─ YES → tools (検索実行) → agent (結果で再評価) → ...
  └─ NO  → END (最終回答)
```

**重要な概念**:
- **ループ**: `tools → agent` の繰り返し
- **終了条件**: `tool_calls`がない = タスク完了

---

#### messagesベースのState設計

**なぜmessagesベース?**
エージェントでは、LLMとツールの往復が発生します。会話履歴を保持するために`messages`をStateに持ちます。

```python
from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
```

**Annotatedの意味**:
```python
messages: Annotated[list, operator.add]
#         ^^^^^^^^^^^^^^^^^^^^^^^^
#         型ヒント + マージ方法の指定
```

- `list`: メッセージのリスト
- `operator.add`: 新しいメッセージを**追加**（上書きではない）

**動作例**:
```python
# 初期State
{"messages": [HumanMessage("質問")]}

# ノードAが実行
return {"messages": [AIMessage("回答A")]}

# マージ後（addなので追加）
{"messages": [HumanMessage("質問"), AIMessage("回答A")]}

# ノードBが実行
return {"messages": [ToolMessage("検索結果")]}

# マージ後
{"messages": [HumanMessage("質問"), AIMessage("回答A"), ToolMessage("検索結果")]}
```

---

#### ToolNodeの理解

**ToolNodeとは**:
LangGraphが提供する**組み込みノード**で、ツール実行を自動処理します。

```python
from langgraph.prebuilt import ToolNode

tools = [search_tool]
tool_node = ToolNode(tools)
```

**ToolNodeの動作**:
1. `messages`から最新の`tool_calls`を取得
2. 該当するツールを実行
3. 結果を`ToolMessage`として返す

**利点**:
- 手動でツール実行コードを書く必要がない
- エラーハンドリングが自動
- 複数ツールに対応

---

#### 完全なエージェント実装（コピペ可能）

```python
import os
from typing import TypedDict, Annotated, Literal
import operator
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import ToolNode

# APIキー設定
os.environ["GEMINI_API_KEY"] = "your-key"
os.environ["TAVILY_API_KEY"] = "your-key"

# State定義
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

# ツール初期化
search_tool = TavilySearchResults(
    max_results=3,
    search_depth="advanced"  # 詳細な検索
)

tools = [search_tool]

# LLM初期化とツールバインド
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0  # 検索エージェントは決定的に
)
llm_with_tools = llm.bind_tools(tools)

# エージェントノード
def agent_node(state: AgentState) -> dict:
    """LLMがツール使用を判断"""
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

# ルーティング関数
def should_continue(state: AgentState) -> Literal["tools", "end"]:
    """ツール使用が必要か判定"""
    last_message = state["messages"][-1]
    
    # tool_callsがあればツールノードへ
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    
    # なければ終了
    return "end"

# グラフ構築
workflow = StateGraph(AgentState)

# ノード追加
workflow.add_node("agent", agent_node)
workflow.add_node("tools", ToolNode(tools))

# エッジ追加
workflow.add_edge(START, "agent")

# 条件分岐
workflow.add_conditional_edges(
    source="agent",
    path=should_continue,
    path_map={
        "tools": "tools",
        "end": END
    }
)

# ツール → エージェントのループ
workflow.add_edge("tools", "agent")

# コンパイル
app = workflow.compile()

# グラフ可視化
try:
    png_data = app.get_graph().draw_mermaid_png()
    with open("search_agent_graph.png", "wb") as f:
        f.write(png_data)
    print("✅ グラフを 'search_agent_graph.png' に保存しました")
except:
    print("ASCII版グラフ:")
    print(app.get_graph().draw_ascii())

# テスト実行
print("\n" + "="*80)
print("検索エージェント - テスト実行")
print("="*80)

test_queries = [
    "2024年のノーベル物理学賞受賞者を教えて",
    "LangGraphの最新バージョンは？",
    "こんにちは"  # 検索不要のケース
]

for query in test_queries:
    print(f"\n【質問】 {query}")
    
    result = app.invoke({
        "messages": [HumanMessage(content=query)]
    })
    
    # 最終回答を取得
    final_message = result["messages"][-1]
    print(f"【回答】 {final_message.content[:200]}...")
    
    # ツール使用状況を確認
    tool_used = any(
        hasattr(msg, "tool_calls") and msg.tool_calls
        for msg in result["messages"]
    )
    print(f"【ツール使用】 {'あり' if tool_used else 'なし'}")
    print("-" * 80)
```

**実行結果例**:
```
================================================================================
検索エージェント - テスト実行
================================================================================

【質問】 2024年のノーベル物理学賞受賞者を教えて
【回答】 2024年のノーベル物理学賞は、John J. HopfieldとGeoffrey E. Hintonが受賞しました。彼らは人工ニューラルネットワークを用いた機械学習の基礎的な発見と発明により受賞しました...
【ツール使用】 あり
--------------------------------------------------------------------------------

【質問】 LangGraphの最新バージョンは？
【回答】 検索結果によると、LangGraphの最新バージョンは0.2.xシリーズです...
【ツール使用】 あり
--------------------------------------------------------------------------------

【質問】 こんにちは
【回答】 こんにちは！何かお手伝いできることはありますか？
【ツール使用】 なし
--------------------------------------------------------------------------------
```

---

#### エージェントループのデバッグ

**ループの進行を確認**:
```python
# stream()で各ステップを観察
for step in app.stream({"messages": [HumanMessage("質問")]}):
    print(step)
```

**出力例**:
```python
{'agent': {'messages': [AIMessage(content='', tool_calls=[...])]}}
{'tools': {'messages': [ToolMessage(content='検索結果...')]}}
{'agent': {'messages': [AIMessage(content='最終回答...')]}}
```

**ループ回数の制限**（無限ループ防止）:
```python
# 最大5ステップで強制終了
result = app.invoke(
    {"messages": [HumanMessage("質問")]},
    config={"recursion_limit": 5}
)
```

---

### 4-4. 複数ツールの統合

#### カスタムツールの作成

LangChainの`@tool`デコレータで簡単に作成できます。

```python
from langchain_core.tools import tool

@tool
def calculate(expression: str) -> str:
    """数式を計算します。
    
    Args:
        expression: 計算する数式（例: "2 + 2", "10 * 5"）
    
    Returns:
        計算結果の文字列
    """
    try:
        # 注意: eval()は実運用では危険。ここではデモのみ
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"計算エラー: {e}"

@tool
def get_current_time() -> str:
    """現在の日時を取得します。
    
    Returns:
        現在の日時（日本時間）
    """
    from datetime import datetime
    import pytz
    
    jst = pytz.timezone('Asia/Tokyo')
    now = datetime.now(jst)
    return now.strftime("%Y年%m月%d日 %H時%M分%S秒")
```

**重要ポイント**:
1. **docstring必須**: LLMがツールの用途を理解するため
2. **型ヒント必須**: 引数と戻り値の型を明示
3. **戻り値は文字列**: LLMが解釈しやすい形式

---

#### 複数ツールを持つエージェント

```python
import os
from typing import TypedDict, Annotated, Literal
import operator
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode

os.environ["GEMINI_API_KEY"] = "your-key"
os.environ["TAVILY_API_KEY"] = "your-key"

# State定義
class MultiToolState(TypedDict):
    messages: Annotated[list, operator.add]

# ツール定義
search_tool = TavilySearchResults(max_results=3)

@tool
def calculate(expression: str) -> str:
    """数式を計算"""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"エラー: {e}"

@tool
def get_weather(city: str) -> str:
    """天気情報を取得（デモ用のダミー実装）"""
    # 実際はAPI呼び出しなど
    return f"{city}の天気: 晴れ、気温23度"

# すべてのツールをリスト化
tools = [search_tool, calculate, get_weather]

# LLM初期化
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0)
llm_with_tools = llm.bind_tools(tools)

# エージェントノード
def agent(state: MultiToolState) -> dict:
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

# ルーティング
def should_continue(state: MultiToolState) -> Literal["tools", "end"]:
    last_msg = state["messages"][-1]
    if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
        return "tools"
    return "end"

# グラフ構築
workflow = StateGraph(MultiToolState)
workflow.add_node("agent", agent)
workflow.add_node("tools", ToolNode(tools))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", should_continue, {
    "tools": "tools",
    "end": END
})
workflow.add_edge("tools", "agent")

app = workflow.compile()

# テスト
test_queries = [
    "東京の天気は？",
    "125 × 48の計算をして",
    "Pythonの最新バージョンを調べて",
    "大阪の天気を調べて、その気温を華氏に変換して"  # 複数ツール使用
]

print("="*80)
print("マルチツールエージェント - テスト")
print("="*80)

for query in test_queries:
    print(f"\n【質問】 {query}")
    
    result = app.invoke({"messages": [HumanMessage(content=query)]})
    
    # 使用されたツールを確認
    tools_used = []
    for msg in result["messages"]:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            for tc in msg.tool_calls:
                tools_used.append(tc["name"])
    
    print(f"【使用ツール】 {', '.join(set(tools_used)) if tools_used else 'なし'}")
    print(f"【回答】 {result['messages'][-1].content[:150]}...")
    print("-" * 80)
```

**実行結果例**:
```
【質問】 東京の天気は？
【使用ツール】 get_weather
【回答】 東京の天気: 晴れ、気温23度

【質問】 125 × 48の計算をして
【使用ツール】 calculate
【回答】 125 × 48 = 6000です。

【質問】 Pythonの最新バージョンを調べて
【使用ツール】 tavily_search_results_json
【回答】 検索結果によると、Pythonの最新バージョンは3.12.xです...

【質問】 大阪の天気を調べて、その気温を華氏に変換して
【使用ツール】 get_weather, calculate
【回答】 大阪の天気は晴れで、気温は23度（摂氏）です。これを華氏に変換すると73.4度になります。
```

---

## 第5章: 高度なパターン【完全解説】

### 5-1. ループと再試行パターン

#### なぜループが必要か

**ユースケース**:
1. **品質チェック**: 結果が満足いくまで繰り返す
2. **リトライ**: エラー発生時に再試行
3. **段階的改善**: 前回の結果をフィードバックして改善

**例: コード生成の品質チェック**
```
generate_code → check_quality →
  ├─ 合格 → END
  └─ 不合格 → improve_code → check_quality → ...
```

---

#### 基本的なループパターン

```python
import os
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

os.environ["GEMINI_API_KEY"] = "your-key"

class LoopState(TypedDict):
    task: str
    result: str
    quality_score: float
    attempts: int

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.7)

# ステップ1: タスク実行
def execute_task(state: LoopState) -> dict:
    """タスクを実行"""
    messages = [
        SystemMessage(content="簡潔なPython関数を生成してください。"),
        HumanMessage(content=state["task"])
    ]
    response = llm.invoke(messages)
    
    return {
        "result": response.content,
        "attempts": state["attempts"] + 1
    }

# ステップ2: 品質評価
def evaluate_quality(state: LoopState) -> dict:
    """生成結果の品質を評価"""
    messages = [
        SystemMessage(content="""
以下のコードの品質を0.0〜1.0で評価してください。
基準:
- 0.8以上: 優秀
- 0.5〜0.8: 普通
- 0.5未満: 改善必要

数値のみ返してください。
        """),
        HumanMessage(content=state["result"])
    ]
    
    response = llm.invoke(messages)
    
    try:
        score = float(response.content.strip())
        score = max(0.0, min(1.0, score))
    except:
        score = 0.5
    
    return {"quality_score": score}

# ステップ3: ループ判定
def should_retry(state: LoopState) -> Literal["retry", "end"]:
    """再試行が必要か判定"""
    
    # 品質基準を満たした
    if state["quality_score"] >= 0.8:
        return "end"
    
    # 最大試行回数に到達
    if state["attempts"] >= 3:
        return "end"
    
    # 再試行
    return "retry"

# ステップ4: 改善
def improve_result(state: LoopState) -> dict:
    """前回の結果を改善"""
    messages = [
        SystemMessage(content=f"""
前回生成したコードを改善してください。
品質スコア: {state['quality_score']}

改善点:
- より明確な変数名
- エッジケースの処理
- ドキュメントの追加
        """),
        HumanMessage(content=state["result"])
    ]
    
    response = llm.invoke(messages)
    return {"result": response.content}

# グラフ構築
workflow = StateGraph(LoopState)

workflow.add_node("execute", execute_task)
workflow.add_node("evaluate", evaluate_quality)
workflow.add_node("improve", improve_result)

workflow.add_edge(START, "execute")
workflow.add_edge("execute", "evaluate")

workflow.add_conditional_edges(
    source="evaluate",
    path=should_retry,
    path_map={
        "retry": "improve",
        "end": END
    }
)

# ループの要: improve → execute
workflow.add_edge("improve", "execute")

app = workflow.compile()

# テスト
result = app.invoke({
    "task": "リストの重複を削除する関数を作成",
    "result": "",
    "quality_score": 0.0,
    "attempts": 0
})

print(f"試行回数: {result['attempts']}")
print(f"最終スコア: {result['quality_score']:.2f}")
print(f"\n生成コード:\n{result['result']}")
```

**グラフ構造**:
```
START → execute → evaluate →
          ↑         ↓
          |       retry?
          |         ↓
        improve ←─ yes
          
        no → END
```

---

#### 再試行の実践例: API呼び出しのリトライ

```python
import os
import time
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END

class RetryState(TypedDict):
    url: str
    response: str
    error: str
    attempts: int

def call_api(state: RetryState) -> dict:
    """API呼び出し（失敗する可能性あり）"""
    try:
        # ダミーAPI呼び出し
        # 実際はrequests.get(state["url"])など
        import random
        if random.random() < 0.5:  # 50%の確率で失敗
            raise Exception("API接続エラー")
        
        return {
            "response": "API呼び出し成功",
            "error": "",
            "attempts": state["attempts"] + 1
        }
    except Exception as e:
        return {
            "response": "",
            "error": str(e),
            "attempts": state["attempts"] + 1
        }

def should_retry(state: RetryState) -> Literal["retry", "end"]:
    """リトライすべきか判定"""
    
    # 成功した
    if state["response"]:
        return "end"
    
    # 最大リトライ回数に到達
    if state["attempts"] >= 5:
        return "end"
    
    # リトライ
    return "retry"

def wait_before_retry(state: RetryState) -> dict:
    """リトライ前に待機（エクスポネンシャルバックオフ）"""
    wait_time = 2 ** state["attempts"]  # 2, 4, 8, 16秒...
    print(f"リトライ {state['attempts']}回目まで {wait_time}秒待機...")
    time.sleep(wait_time)
    return {}

# グラフ構築
workflow = StateGraph(RetryState)
workflow.add_node("call_api", call_api)
workflow.add_node("wait", wait_before_retry)

workflow.add_edge(START, "call_api")
workflow.add_conditional_edges("call_api", should_retry, {
    "retry": "wait",
    "end": END
})
workflow.add_edge("wait", "call_api")

app = workflow.compile()

# テスト
result = app.invoke({
    "url": "https://api.example.com/data",
    "response": "",
    "error": "",
    "attempts": 0
})

if result["response"]:
    print(f"✅ 成功（{result['attempts']}回目の試行）")
else:
    print(f"❌ 失敗（{result['attempts']}回試行後）: {result['error']}")
```

---

### 5-2. エラーハンドリングの完全ガイド

#### 基本的なエラーハンドリング

```python
def safe_node(state: State) -> dict:
    """エラーをキャッチして安全に処理"""
    try:
        result = risky_operation(state["input"])
        return {
            "output": result,
            "error": None,
            "success": True
        }
    except ValueError as e:
        return {
            "output": None,
            "error": f"入力エラー: {e}",
            "success": False
        }
    except Exception as e:
        return {
            "output": None,
            "error": f"予期しないエラー: {e}",
            "success": False
        }
```

---

#### エラー時の分岐処理

```python
import os
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

os.environ["GEMINI_API_KEY"] = "your-key"

class ErrorHandlingState(TypedDict):
    input: str
    output: str
    error: str
    error_type: str

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

def process_with_error_handling(state: ErrorHandlingState) -> dict:
    """処理を実行してエラーをハンドリング"""
    try:
        # ダミー処理: JSONパース
        import json
        data = json.loads(state["input"])
        
        response = llm.invoke([
            HumanMessage(content=f"このデータを説明: {data}")
        ])
        
        return {
            "output": response.content,
            "error": "",
            "error_type": "none"
        }
    
    except json.JSONDecodeError as e:
        return {
            "output": "",
            "error": str(e),
            "error_type": "json_error"
        }
    
    except Exception as e:
        return {
            "output": "",
            "error": str(e),
            "error_type": "unknown_error"
        }

def route_by_error(state: ErrorHandlingState) -> Literal["success", "json_error", "unknown_error"]:
    """エラータイプで分岐"""
    return state["error_type"]

def handle_json_error(state: ErrorHandlingState) -> dict:
    """JSON解析エラーへの対応"""
    return {
        "output": f"入力形式エラー: {state['error']}\n正しいJSON形式で入力してください。"
    }

def handle_unknown_error(state: ErrorHandlingState) -> dict:
    """未知のエラーへの対応"""
    return {
        "output": f"システムエラーが発生しました: {state['error']}\n管理者に連絡してください。"
    }

def format_success(state: ErrorHandlingState) -> dict:
    """成功時の処理"""
    return {"output": f"✅ 処理成功\n{state['output']}"}

# グラフ構築
workflow = StateGraph(ErrorHandlingState)

workflow.add_node("process", process_with_error_handling)
workflow.add_node("json_error_handler", handle_json_error)
workflow.add_node("unknown_error_handler", handle_unknown_error)
workflow.add_node("success_handler", format_success)

workflow.add_edge(START, "process")

workflow.add_conditional_edges(
    source="process",
    path=route_by_error,
    path_map={
        "none": "success_handler",
        "json_error": "json_error_handler",
        "unknown_error": "unknown_error_handler"
    }
)

workflow.add_edge("success_handler", END)
workflow.add_edge("json_error_handler", END)
workflow.add_edge("unknown_error_handler", END)

app = workflow.compile()

# テスト
test_inputs = [
    '{"name": "Alice", "age": 30}',  # 正常
    '{"invalid json',                 # JSON解析エラー
    None                              # その他のエラー
]

for inp in test_inputs:
    print(f"\n入力: {inp}")
    try:
        result = app.invoke({
            "input": str(inp),
            "output": "",
            "error": "",
            "error_type": ""
        })
        print(f"出力: {result['output']}")
    except Exception as e:
        print(f"実行エラー: {e}")
    print("-" * 60)
```

---

### 5-3. 並列実行パターン

#### 並列実行の基本概念

**直列実行（通常）**:
```
task1 → task2 → task3  （所要時間: 6秒）
2秒    2秒    2秒
```

**並列実行**:
```
task1 ─┐
task2 ─┼→ merge  （所要時間: 2秒）
task3 ─┘
2秒
```

---

#### 並列ノードの実装

```python
import os
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

os.environ["GEMINI_API_KEY"] = "your-key"

class ParallelState(TypedDict):
    topic: str
    summary: str
    pros: str
    cons: str
    final_report: str

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.7)

# 並列タスク1: 要約生成
def generate_summary(state: ParallelState) -> dict:
    """トピックの要約を生成"""
    response = llm.invoke([
        SystemMessage(content="トピックを3文で要約してください。"),
        HumanMessage(content=state["topic"])
    ])
    return {"summary": response.content}

# 並列タスク2: メリット抽出
def extract_pros(state: ParallelState) -> dict:
    """メリットを列挙"""
    response = llm.invoke([
        SystemMessage(content="3つの主要なメリットを箇条書きで。"),
        HumanMessage(content=state["topic"])
    ])
    return {"pros": response.content}

# 並列タスク3: デメリット抽出
def extract_cons(state: ParallelState) -> dict:
    """デメリットを列挙"""
    response = llm.invoke([
        SystemMessage(content="3つの主要なデメリットを箇条書きで。"),
        HumanMessage(content=state["topic"])
    ])
    return {"cons": response.content}

# 統合タスク
def merge_results(state: ParallelState) -> dict:
    """並列処理結果を統合"""
    report = f"""
=== 分析レポート: {state['topic']} ===

【要約】
{state['summary']}

【メリット】
{state['pros']}

【デメリット】
{state['cons']}
    """
    return {"final_report": report.strip()}

# グラフ構築
workflow = StateGraph(ParallelState)

# ノード登録
workflow.add_node("summary", generate_summary)
workflow.add_node("pros", extract_pros)
workflow.add_node("cons", extract_cons)
workflow.add_node("merge", merge_results)

# 並列開始
workflow.add_edge(START, "summary")
workflow.add_edge(START, "pros")
workflow.add_edge(START, "cons")

# 統合ノードへ集約
workflow.add_edge("summary", "merge")
workflow.add_edge("pros", "merge")
workflow.add_edge("cons", "merge")

workflow.add_edge("merge", END)

app = workflow.compile()

# グラフ確認
print("グラフ構造:")
print(app.get_graph().draw_ascii())

# テスト
import time
start = time.time()

result = app.invoke({
    "topic": "リモートワークの導入",
    "summary": "",
    "pros": "",
    "cons": "",
    "final_report": ""
})

elapsed = time.time() - start

print(f"\n実行時間: {elapsed:.2f}秒")
print(result["final_report"])
```

**重要なポイント**:
- `add_edge(START, "node")` を複数回呼ぶことで並列開始
- すべての並列ノードが完了してから`merge`が実行される
- 実行順序は保証されない（非同期実行）

---

### 5-4. ストリーミング実行

#### stream()の基本

**通常のinvoke()**:
```python
result = app.invoke({"input": "質問"})
print(result)  # 全て完了後に一度だけ表示
```

**stream()を使用**:
```python
for chunk in app.stream({"input": "質問"}):
    print(chunk)  # 各ノードの実行ごとに表示
```

---

#### 実践例: プログレス表示

```python
import os
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import time

os.environ["GEMINI_API_KEY"] = "your-key"

class StreamState(TypedDict):
    input: str
    step1_result: str
    step2_result: str
    final_output: str

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

def step1_process(state: StreamState) -> dict:
    """ステップ1: 入力を分析"""
    print("  [ステップ1] 入力を分析中...")
    time.sleep(1)  # シミュレーション
    
    response = llm.invoke([
        HumanMessage(content=f"次の文を分析: {state['input']}")
    ])
    
    return {"step1_result": response.content}

def step2_process(state: StreamState) -> dict:
    """ステップ2: 詳細分析"""
    print("  [ステップ2] 詳細分析中...")
    time.sleep(1)
    
    response = llm.invoke([
        HumanMessage(content=f"次の分析を深める: {state['step1_result']}")
    ])
    
    return {"step2_result": response.content}

def finalize(state: StreamState) -> dict:
    """ステップ3: 最終レポート"""
    print("  [ステップ3] レポート生成中...")
    time.sleep(1)
    
    final = f"""
分析結果:
- 初期分析: {state['step1_result'][:50]}...
- 詳細分析: {state['step2_result'][:50]}...
    """
    return {"final_output": final}

# グラフ構築
workflow = StateGraph(StreamState)
workflow.add_node("step1", step1_process)
workflow.add_node("step2", step2_process)
workflow.add_node("finalize", finalize)

workflow.add_edge(START, "step1")
workflow.add_edge("step1", "step2")
workflow.add_edge("step2", "finalize")
workflow.add_edge("finalize", END)

app = workflow.compile()

# ストリーミング実行
print("="*60)
print("ストリーミング実行開始")
print("="*60)

for i, chunk in enumerate(app.stream({
    "input": "AIの未来について",
    "step1_result": "",
    "step2_result": "",
    "final_output": ""
}), 1):
    node_name = list(chunk.keys())[0]
    print(f"\n[チャンク {i}] ノード '{node_name}' 完了")
    # print(f"  結果: {chunk}")  # 詳細表示

print("\n" + "="*60)
print("✅ すべての処理が完了しました")
print("="*60)
```

**出力例**:
```
============================================================
ストリーミング実行開始
============================================================
  [ステップ1] 入力を分析中...

[チャンク 1] ノード 'step1' 完了
  [ステップ2] 詳細分析中...

[チャンク 2] ノード 'step2' 完了
  [ステップ3] レポート生成中...

[チャンク 3] ノード 'finalize' 完了

============================================================
✅ すべての処理が完了しました
============================================================
```

---

## 付録A: トラブルシューティング完全ガイド

### よくあるエラーと解決法

#### エラー1: KeyError: 'route_name'

**エラーメッセージ**:
```
KeyError: 'high_priority'
```

**原因**:
ルーティング関数が返す値がpath_mapに存在しない

**解決法**:
```python
# ❌ 問題のあるコード
def route(state):
    return "high_priority"  # この値が

workflow.add_conditional_edges("node", route, {
    "high": "handler",  # ここにない
    "low": "handler2"
})

# ✅ 修正版
def route(state):
    return "high"  # 値を一致させる

workflow.add_conditional_edges("node", route, {
    "high": "handler",
    "low": "handler2"
})
```

---

#### エラー2: "Node '__start__' already exists"

**エラーメッセージ**:
```
ValueError: Node '__start__' already exists
```

**原因**:
予約語`__start__`や`__end__`をノード名として使用

**解決法**:
```python
# ❌ 問題のあるコード
workflow.add_node("__start__", func)

# ✅ 修正版
workflow.add_node("start_process", func)
```

---

#### エラー3: API認証エラー

**エラーメッセージ**:
```
AuthenticationError: Invalid API key
```

**原因**:
- APIキーが正しく設定されていない
- APIキーが無効

**解決法**:
```python
import os

# デバッグ: キーが設定されているか確認
print(os.environ.get("GEMINI_API_KEY"))
print(os.environ.get("TAVILY_API_KEY"))

# 正しく設定
os.environ["GEMINI_API_KEY"] = "AIza..."  # 実際のキー
os.environ["TAVILY_API_KEY"] = "tvly-..."  # 実際のキー
```

---

#### エラー4: RecursionError

**エラーメッセージ**:
```
RecursionError: maximum recursion depth exceeded
```

**原因**:
無限ループ（終了条件がない）

**解決法**:
```python
# ❌ 問題のあるコード（終了条件なし）
def route(state):
    return "retry"  # 常にretry

workflow.add_conditional_edges("node", route, {
    "retry": "node"  # 無限ループ
})

# ✅ 修正版（終了条件を追加）
def route(state):
    if state["attempts"] >= 5:
        return "end"
    return "retry"

workflow.add_conditional_edges("node", route, {
    "retry": "node",
    "end": END
})
```

**または最大ステップ数を制限**:
```python
result = app.invoke(
    {"input": "質問"},
    config={"recursion_limit": 10}  # 最大10ステップ
)
```

---

## 付録B: ベストプラクティス集

### 1. State設計のベストプラクティス

#### ✅ 良い設計

```python
from typing import TypedDict

class State(TypedDict):
    # 明確で具体的な名前
    user_query: str
    search_results: list
    final_answer: str
    confidence_score: float
    error_message: str
```

#### ❌ 悪い設計

```python
class State(TypedDict):
    # 曖昧な名前
    data: str
    result: str
    value: float
    msg: str
```

---

### 2. ノード関数のベストプラクティス

#### ✅ 良い実装

```python
def process_node(state: State) -> dict:
    """
    ユーザークエリを処理してLLMで回答を生成
    
    Args:
        state: 現在のワークフロー状態
    
    Returns:
        更新するStateフィールド
    """
    try:
        # 明確なロジック
        user_input = state["user_query"]
        response = llm.invoke([HumanMessage(content=user_input)])
        
        return {
            "final_answer": response.content,
            "error_message": ""
        }
    
    except Exception as e:
        # エラーハンドリング
        return {
            "final_answer": "",
            "error_message": str(e)
        }
```

#### ❌ 悪い実装

```python
def process_node(state):  # 型ヒントなし
    # ドキュメントなし
    # エラーハンドリングなし
    return {"result": llm.invoke([HumanMessage(state["input"])]).content}
```

---

### 3. グラフ構造のベストプラクティス

#### ✅ 良い構造

```python
# 明確な命名
workflow.add_node("classify_intent", classify)
workflow.add_node("search_knowledge_base", search)
workflow.add_node("generate_response", generate)

# 論理的なフロー
workflow.add_edge(START, "classify_intent")
workflow.add_conditional_edges("classify_intent", route, {
    "needs_search": "search_knowledge_base",
    "direct_answer": "generate_response"
})
```

#### ❌ 悪い構造

```python
# 曖昧な命名
workflow.add_node("node1", func1)
workflow.add_node("node2", func2)
workflow.add_node("process", func3)

# 複雑すぎるフロー（可読性が低い）
```

---

## 付録C: 実装パターンライブラリ

### パターン1: シンプルQ&A

```python
import os
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

os.environ["GEMINI_API_KEY"] = "your-key"

class QAState(TypedDict):
    question: str
    answer: str

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

workflow = StateGraph(QAState)
workflow.add_node("answer", lambda s: {
    "answer": llm.invoke([HumanMessage(s["question"])]).content
})
workflow.add_edge(START, "answer")
workflow.add_edge("answer", END)

app = workflow.compile()

result = app.invoke({"question": "LangGraphとは？", "answer": ""})
print(result["answer"])
```

---

### パターン2: 検索付きQ&A

```python
# 第4章のエージェントループを参照
```

---

### パターン3: 多段階処理

```python
workflow.add_edge(START, "analyze")
workflow.add_edge("analyze", "transform")
workflow.add_edge("transform", "validate")
workflow.add_edge("validate", "format")
workflow.add_edge("format", END)
```

---

### パターン4: 条件分岐 + ループ

```python
workflow.add_edge(START, "process")
workflow.add_conditional_edges("process", check_quality, {
    "good": END,
    "retry": "improve"
})
workflow.add_edge("improve", "process")  # ループ
```

---

## 🎉 完走おめでとうございます！

この第3章以降の資料で、あなたは以下をマスターしました:

✅ **条件分岐**: 複雑なルーティングロジックの実装
✅ **ツール統合**: Tavily検索とカスタムツールの統合
✅ **エージェントループ**: LLMとツールの協調動作
✅ **高度なパターン**: ループ、並列実行、ストリーミング
✅ **エラーハンドリング**: 堅牢なワークフロー設計
✅ **ベストプラクティス**: プロダクション品質のコード

---

## 次のステップ

1. **実践プロジェクトに挑戦**:
   - カスタマーサポートボットを構築
   - リサーチエージェントを作成
   - データ分析パイプラインを実装

2. **公式ドキュメントで深掘り**:
   - [LangGraph公式](https://langchain-ai.github.io/langgraph/)
   - [LangChain統合](https://python.langchain.com/)

3. **コミュニティ参加**:
   - GitHub Discussionsで質問
   - 自分の実装を共有

---

## 参考リンク

- 📚 [LangGraph公式ドキュメント](https://langchain-ai.github.io/langgraph/)
- 🔑 [Google AI Studio](https://aistudio.google.com/)
- 🔍 [Tavily Search API](https://tavily.com/)
- 💬 [LangChain Discord](https://discord.gg/langchain)

**Happy Coding! 🚀**

あなたは今、LangGraphのエキスパートです。実際のサービスを構築する準備が整いました！

