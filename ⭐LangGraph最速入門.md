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

## 2-4. よくある質問30選

### 基本概念

#### Q1: LangGraphとLangChainの違いは?

**A:** LangChainは**線形的なチェーン**、LangGraphは**グラフ構造**のワークフローを扱います。

```python
# LangChain - シンプルだが柔軟性に欠ける
chain = prompt | llm | output_parser
result = chain.invoke({"input": "質問"})

# LangGraph - 複雑だが柔軟
graph = StateGraph(State)
graph.add_conditional_edges(...)  # 条件分岐
graph.add_edge(..., ..., condition=...)  # ループ
```

#### Q2: StateGraphは必須?

**A:** はい、**絶対必須**です。これがないとワークフローを作れません。

#### Q3: Stateのフィールドは何個まで?

**A:** **制限なし**。1個でも100個でもOKです。

```python
# ✅ 最小（1フィールド）
class MinimalState(TypedDict):
    data: str

# ✅ 実用的（複数フィールド）
class RealState(TypedDict):
    query: str
    search_results: list
    summary: str
    final_answer: str
    metadata: dict
```

#### Q4: TypedDictは必須?

**A:** 技術的には`dict`でも動きますが、**TypedDictを強く推奨**します。

```python
# ❌ 動くが非推奨
class State(dict):
    pass

# ✅ 推奨
from typing import TypedDict
class State(TypedDict):
    input: str
    output: str
```

**理由:**
- 型安全性
- IDEの補完
- タイポ防止

#### Q5: STARTとENDは省略できる?

**A:** 技術的には可能ですが、**99%のケースで使います**。

```python
# ❌ 動くが実践的でない
workflow.add_edge("node1", "node2")

# ✅ 推奨
workflow.add_edge(START, "node1")
workflow.add_edge("node2", END)
```

---

### ノード関数

#### Q6: ノード関数の引数名は`state`固定?

**A:** いいえ、**任意の名前でOK**ですが、`state`が慣例です。

```python
# ✅ すべて有効
def node1(state: State) -> dict:
    return {"output": "OK"}

def node2(data: State) -> dict:
    return {"output": "OK"}

def node3(s: State) -> dict:
    return {"output": "OK"}
```

#### Q7: 戻り値は必ずdict?

**A:** はい、**必ずdict**です。

```python
# ✅ 正しい
def correct_node(state: State) -> dict:
    return {"output": "結果"}

# ❌ エラー
def wrong_node(state: State) -> str:
    return "結果"
```

#### Q8: 空のdictを返してもいい?

**A:** はい、**OK**です（何も更新しない場合）。

```python
def no_update_node(state: State) -> dict:
    # 何か処理はするが、Stateは更新しない
    print("処理中...")
    return {}  # ✅ OK
```

#### Q9: すべてのフィールドを返す必要は?

**A:** いいえ、**更新するフィールドだけ**返せばOKです。

```python
class State(TypedDict):
    a: str
    b: str
    c: str

def node(state: State) -> dict:
    # aだけ更新
    return {"a": "新しい値"}  # ✅ bとcはそのまま
```

#### Q10: ノード関数内でエラーが起きたら?

**A:** **ワークフロー全体が停止**します（第5章で対策を学びます）。

```python
def risky_node(state: State) -> dict:
    result = 10 / 0  # ZeroDivisionError
    return {"output": result}

# → ワークフロー停止、エラーが伝播
```

---

### グラフ構造

#### Q11: ノードの追加順序は重要?

**A:** いいえ、**順序は無関係**です。

```python
# どちらも同じ結果
# パターン1
workflow.add_node("a", func_a)
workflow.add_node("b", func_b)

# パターン2
workflow.add_node("b", func_b)
workflow.add_node("a", func_a)
```

#### Q12: エッジの追加順序は?

**A:** いいえ、**順序は無関係**です。

```python
# どちらも同じ
# パターン1
workflow.add_edge(START, "a")
workflow.add_edge("a", END)

# パターン2
workflow.add_edge("a", END)
workflow.add_edge(START, "a")
```

#### Q13: 同じノードを複数回追加できる?

**A:** いいえ、**エラー**になります。

```python
workflow.add_node("process", func)
workflow.add_node("process", func)  # ❌ エラー
```

#### Q14: ノード名は日本語OK?

**A:** はい、**完全にOK**です。

```python
workflow.add_node("処理1", func1)
workflow.add_node("検索", func2)
workflow.add_node("要約生成", func3)
# ✅ すべて有効
```

#### Q15: ノード名の制限は?

**A:** `__start__`と`__end__`は**予約語**なので使えません。

```python
workflow.add_node("__start__", func)  # ❌ エラー
workflow.add_node("__end__", func)    # ❌ エラー
workflow.add_node("my_node", func)    # ✅ OK
```

---

### 実行とデバッグ

#### Q16: invoke()の引数は?

**A:** **Stateの初期値**を辞書で渡します。

```python
class State(TypedDict):
    input: str
    output: str

# すべてのフィールドを渡す必要はない
result = app.invoke({"input": "質問"})  # ✅ OK
result = app.invoke({"input": "質問", "output": ""})  # ✅ これもOK
```

#### Q17: 実行結果は何が返る?

**A:** **最終的なState全体**が返ります。

```python
result = app.invoke({"input": "こんにちは"})
print(type(result))  # <class 'dict'>
print(result)  # {"input": "こんにちは", "output": "こんにちは！..."}
```

#### Q18: 途中経過は取得できる?

**A:** `stream()`メソッドで可能です。

```python
for chunk in app.stream({"input": "質問"}):
    print(chunk)  # 各ノードの実行結果
```

#### Q19: 実行時間を計測したい

**A:** Pythonの`time`モジュールを使います。

```python
import time

start_time = time.time()
result = app.invoke({"input": "質問"})
end_time = time.time()

print(f"実行時間: {end_time - start_time:.2f}秒")
```

#### Q20: デバッグ方法は?

**A:** ノード関数内で`print()`を使います。

```python
def debug_node(state: State) -> dict:
    print(f"現在のstate: {state}")  # デバッグ出力
    result = some_processing(state)
    print(f"処理結果: {result}")
    return {"output": result}
```

---

### APIとLLM

#### Q21: Gemini以外のLLMは使える?

**A:** はい、**LangChain対応LLMならすべて使えます**。

```python
# OpenAI
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    model="gpt-4"
)

# Anthropic Claude
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"],
    model="claude-3-opus"
)

# ローカルLLM (Ollama)
from langchain_community.llms import Ollama
llm = Ollama(model="llama2")
```

#### Q22: APIキーをハードコードしたくない

**A:** 環境変数または`.env`ファイルを使います（0-3章参照）。

```python
# .envファイルから読み込み
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp"
)
```

#### Q23: APIエラーが起きたらどうなる?

**A:** **例外が発生し、ワークフロー停止**します。

```python
# エラーハンドリング例
def safe_llm_call(state: State) -> dict:
    try:
        response = llm.invoke([HumanMessage(content=state["input"])])
        return {"output": response.content}
    except Exception as e:
        return {"output": f"エラー: {str(e)}"}
```

#### Q24: LLM呼び出しをキャッシュできる?

**A:** LangChainのキャッシュ機能を使います。

```python
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache

set_llm_cache(InMemoryCache())

# 同じ質問は2回目以降キャッシュから返る
```

#### Q25: 複数のLLMを同時に使える?

**A:** はい、**ノードごとに異なるLLMを使えます**。

```python
llm_fast = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-1.5-flash"
)

llm_smart = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp"
)

def fast_node(state: State) -> dict:
    response = llm_fast.invoke([HumanMessage(content=state["input"])])
    return {"output": response.content}

def smart_node(state: State) -> dict:
    response = llm_smart.invoke([HumanMessage(content=state["input"])])
    return {"output": response.content}
```

---

### グラフ可視化

#### Q26: 可視化は必須?

**A:** いいえ、**オプション**ですが、複雑なグラフでは強く推奨します。

#### Q27: PNGが生成できない場合は?

**A:** ASCII版で表示できます。

```python
try:
    png_data = app.get_graph().draw_mermaid_png()
except Exception:
    print(app.get_graph().draw_ascii())
```

#### Q28: グラフをJupyter Notebookで表示したい

**A:** `IPython.display`を使います。

```python
from IPython.display import Image, display

png_data = app.get_graph().draw_mermaid_png()
display(Image(png_data))
```

#### Q29: グラフの色を変えられる?

**A:** Mermaidの設定で可能ですが、高度なトピックです。

#### Q30: グラフをHTML出力できる?

**A:** はい、可能です。

```python
# Mermaid形式で取得
mermaid_code = app.get_graph().draw_mermaid()
print(mermaid_code)

# HTMLに埋め込み可能
html = f"""
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<div class="mermaid">
{mermaid_code}
</div>
"""
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

# 第3章: 条件分岐とルーティング

## 3-1. 条件分岐の基本

### なぜ条件分岐が必要?

**単純な直線フロー:**
```
入力 → 処理 → 出力
```

**条件分岐フロー:**
```
入力 → 判定 → 
    ├─ ルートA → 処理A
    ├─ ルートB → 処理B
    └─ ルートC → 処理C
```

### 条件分岐の実装方法

LangGraphでは`add_conditional_edges()`を使います。

```python
workflow.add_conditional_edges(
    "判定ノード",           # どのノードの後に分岐?
    routing_function,      # どう分岐するか判断?
    {                      # 各ルートの接続先
        "route_a": "node_a",
        "route_b": "node_b",
        "route_c": END
    }
)
```

### 最小の条件分岐例

```python
import os
from typing import TypedDict, Literal, NotRequired
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

os.environ["GEMINI_API_KEY"] = "your-api-key"

# State定義
class State(TypedDict):
    input: str                     # 必須（ユーザーが渡す）
    category: NotRequired[str]     # オプショナル（ノードが追加）
    # output: str は定義不要（最終出力のみで使用）

# LLM初期化
llm = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0.3
)

# ノード1: カテゴリ分類
def classify_input(state: State) -> dict:
    """入力をカテゴリ分類"""
    user_input = state["input"]
    
    prompt = f"""
    以下の質問を分類してください。
    - 挨拶なら「greeting」
    - 質問なら「question」
    - その他なら「other」
    
    質問: {user_input}
    
    カテゴリ名のみを返してください。
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    category = response.content.strip().lower()
    
    return {"category": category}

# ルーティング関数
def route_by_category(state: State) -> Literal["greeting", "question", "other"]:
    """カテゴリに応じてルーティング"""
    return state["category"]

# ノード2: 挨拶処理
def handle_greeting(state: State) -> dict:
    return {"output": "こんにちは！何かお手伝いできることはありますか？"}

# ノード3: 質問処理
def handle_question(state: State) -> dict:
    response = llm.invoke([HumanMessage(content=state["input"])])
    return {"output": response.content}

# ノード4: その他処理
def handle_other(state: State) -> dict:
    return {"output": "申し訳ございません、理解できませんでした。"}

# グラフ構築
workflow = StateGraph(State)

# ノード追加
workflow.add_node("classify", classify_input)
workflow.add_node("greeting", handle_greeting)
workflow.add_node("question", handle_question)
workflow.add_node("other", handle_other)

# エッジ追加
workflow.add_edge(START, "classify")

# 条件分岐
workflow.add_conditional_edges(
    "classify",
    route_by_category,
    {
        "greeting": "greeting",
        "question": "question",
        "other": "other"
    }
)

# 各ルートから終了
workflow.add_edge("greeting", END)
workflow.add_edge("question", END)
workflow.add_edge("other", END)

app = workflow.compile()

# 実行（categoryは不要！）
test_inputs = [
    "こんにちは",
    "LangGraphとは何ですか？",
    "あいうえお"
]

for test_input in test_inputs:
    print(f"\n{'='*60}")
    print(f"入力: {test_input}")
    result = app.invoke({"input": test_input})  # ← categoryは渡さない
    print(f"カテゴリ: {result['category']}")
    print(f"出力: {result['output']}")
```

### ルーティング関数の重要ポイント

**ルール1: 戻り値は文字列**

```python
# ✅ 正しい
def route_func(state: State) -> str:
    return "route_a"

# ✅ 型ヒント付き（推奨）
def route_func(state: State) -> Literal["route_a", "route_b"]:
    if state["score"] > 0.8:
        return "route_a"
    return "route_b"
```

**ルール2: 戻り値はマッピングのキーと一致**

```python
# ルーティング関数
def route_func(state: State) -> Literal["high", "low"]:
    return "high" if state["score"] > 0.5 else "low"

# マッピング（キーが一致）
workflow.add_conditional_edges(
    "classify",
    route_func,
    {
        "high": "premium_process",  # ← "high"と一致
        "low": "basic_process"      # ← "low"と一致
    }
)
```

### 🔑 Stateの設計ポイント（重要）

```python
from typing import TypedDict, NotRequired

class State(TypedDict):
    # ✅ 必須フィールド：ユーザーが渡すもの
    input: str
    
    # ✅ オプショナル：ノードが追加するもの（他のノードで使う）
    category: NotRequired[str]
    sentiment: NotRequired[str]
    
    # ❌ 最終出力のみで使うフィールドは定義不要
    # output: str  ← これは不要
```

**理由:**
- `category`や`sentiment`は**複数のノード**で参照される → 定義すべき
- `output`は**最終結果として1回だけ**使われる → 定義不要

---

## 3-2. 複数ルートの実装

### 実用的な例: 質問応答システム

```python
import os
from typing import TypedDict, Literal, NotRequired
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

os.environ["GEMINI_API_KEY"] = "your-api-key"

# State定義
class State(TypedDict):
    question: str                  # 必須（ユーザーが渡す）
    intent: NotRequired[str]       # オプショナル（他のノードで参照）
    # answer: str は定義不要（最終出力のみ）

# LLM初期化
llm = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0.3
)

# ノード1: Intent分類
def classify_intent(state: State) -> dict:
    """質問の意図を分類"""
    question = state["question"]
    
    messages = [
        SystemMessage(content="""
        質問を以下のカテゴリに分類してください:
        - factual: 事実確認の質問
        - opinion: 意見を求める質問
        - howto: 手順を尋ねる質問
        - other: その他
        
        カテゴリ名のみを返してください。
        """),
        HumanMessage(content=question)
    ]
    
    response = llm.invoke(messages)
    intent = response.content.strip().lower()
    
    return {"intent": intent}

# ルーティング関数
def route_by_intent(state: State) -> Literal["factual", "opinion", "howto", "other"]:
    """意図に基づいてルーティング"""
    return state["intent"]

# ノード2a: 事実確認処理
def handle_factual(state: State) -> dict:
    """事実確認の質問に回答"""
    messages = [
        SystemMessage(content="事実に基づいて正確に回答してください。"),
        HumanMessage(content=state["question"])
    ]
    
    response = llm.invoke(messages)
    return {"answer": response.content}

# ノード2b: 意見処理
def handle_opinion(state: State) -> dict:
    """意見を求める質問に回答"""
    messages = [
        SystemMessage(content="バランスの取れた視点を提供してください。"),
        HumanMessage(content=state["question"])
    ]
    
    response = llm.invoke(messages)
    return {"answer": response.content}

# ノード2c: 手順説明処理
def handle_howto(state: State) -> dict:
    """手順を段階的に説明"""
    messages = [
        SystemMessage(content="ステップバイステップで説明してください。"),
        HumanMessage(content=state["question"])
    ]
    
    response = llm.invoke(messages)
    return {"answer": response.content}

# ノード2d: その他処理
def handle_other(state: State) -> dict:
    """その他の質問に対応"""
    return {"answer": "申し訳ございませんが、もう少し具体的にお聞かせいただけますか？"}

# グラフ構築
workflow = StateGraph(State)

# ノード追加
workflow.add_node("classify", classify_intent)
workflow.add_node("factual", handle_factual)
workflow.add_node("opinion", handle_opinion)
workflow.add_node("howto", handle_howto)
workflow.add_node("other", handle_other)

# エッジ追加
workflow.add_edge(START, "classify")

# 条件分岐
workflow.add_conditional_edges(
    "classify",
    route_by_intent,
    {
        "factual": "factual",
        "opinion": "opinion",
        "howto": "howto",
        "other": "other"
    }
)

# 各ルートから終了
workflow.add_edge("factual", END)
workflow.add_edge("opinion", END)
workflow.add_edge("howto", END)
workflow.add_edge("other", END)

app = workflow.compile()

# テスト実行（intentは渡さない）
test_questions = [
    "東京の人口は何人ですか？",
    "AIの未来についてどう思いますか？",
    "Pythonで環境構築する方法を教えてください",
    "あいうえお"
]

for question in test_questions:
    print(f"\n{'='*60}")
    print(f"質問: {question}")
    result = app.invoke({"question": question})  # ← intentは不要
    print(f"意図: {result['intent']}")
    print(f"回答: {result['answer']}")
```

---

## 3-3. 動的ルーティング

### スコアベースのルーティング

信頼度スコアに基づいて処理を分岐する実用的なパターンです。

```python
import os
from typing import TypedDict, Literal, NotRequired
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
import json

os.environ["GEMINI_API_KEY"] = "your-api-key"

# State定義
class State(TypedDict):
    query: str                      # 必須
    confidence: NotRequired[float]  # 他のノードで参照
    # answer: str は定義不要

# LLM初期化
llm = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0.3
)

# ノード1: 信頼度評価
def evaluate_confidence(state: State) -> dict:
    """質問の難易度を評価して信頼度スコアを返す"""
    query = state["query"]
    
    messages = [
        SystemMessage(content="""
        以下の質問の難易度を0.0〜1.0で評価してください。
        - 0.0〜0.3: 簡単な質問（挨拶、基本的な事実）
        - 0.4〜0.7: 中程度の質問（説明が必要）
        - 0.8〜1.0: 難しい質問（専門知識、複雑な推論）
        
        数値のみを返してください。例: 0.7
        """),
        HumanMessage(content=query)
    ]
    
    response = llm.invoke(messages)
    
    try:
        confidence = float(response.content.strip())
    except ValueError:
        confidence = 0.5  # デフォルト値
    
    return {"confidence": confidence}

# ルーティング関数
def route_by_confidence(state: State) -> Literal["simple", "moderate", "complex"]:
    """信頼度スコアに基づいてルーティング"""
    score = state["confidence"]
    
    if score < 0.4:
        return "simple"
    elif score < 0.8:
        return "moderate"
    else:
        return "complex"

# ノード2a: シンプル処理
def handle_simple(state: State) -> dict:
    """簡単な質問に素早く回答"""
    messages = [
        SystemMessage(content="簡潔に回答してください。"),
        HumanMessage(content=state["query"])
    ]
    
    response = llm.invoke(messages)
    return {"answer": response.content}

# ノード2b: 標準処理
def handle_moderate(state: State) -> dict:
    """中程度の質問に詳しく回答"""
    messages = [
        SystemMessage(content="詳しく説明してください。"),
        HumanMessage(content=state["query"])
    ]
    
    response = llm.invoke(messages)
    return {"answer": response.content}

# ノード2c: 複雑処理
def handle_complex(state: State) -> dict:
    """難しい質問に専門的に回答"""
    messages = [
        SystemMessage(content="専門的かつ包括的に説明してください。"),
        HumanMessage(content=state["query"])
    ]
    
    response = llm.invoke(messages)
    return {"answer": response.content}

# グラフ構築
workflow = StateGraph(State)

workflow.add_node("evaluate", evaluate_confidence)
workflow.add_node("simple", handle_simple)
workflow.add_node("moderate", handle_moderate)
workflow.add_node("complex", handle_complex)

workflow.add_edge(START, "evaluate")

workflow.add_conditional_edges(
    "evaluate",
    route_by_confidence,
    {
        "simple": "simple",
        "moderate": "moderate",
        "complex": "complex"
    }
)

workflow.add_edge("simple", END)
workflow.add_edge("moderate", END)
workflow.add_edge("complex", END)

app = workflow.compile()

# テスト実行
test_queries = [
    "こんにちは",
    "LangGraphの基本的な使い方を教えてください",
    "量子コンピューティングと機械学習の理論的な関係性について説明してください"
]

for query in test_queries:
    print(f"\n{'='*60}")
    print(f"質問: {query}")
    result = app.invoke({"query": query})
    print(f"信頼度: {result['confidence']:.2f}")
    print(f"ルート: {route_by_confidence(result)}")
    print(f"回答: {result['answer'][:100]}...")
```

### 複数条件による複雑なルーティング

```python
import os
from typing import TypedDict, Literal, NotRequired
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

os.environ["GEMINI_API_KEY"] = "your-api-key"

# State定義
class State(TypedDict):
    query: str                    # 必須
    language: NotRequired[str]    # 他のノードで参照
    priority: NotRequired[str]    # 他のノードで参照
    # response: str は定義不要

llm = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0.3
)

# ノード1: 分析
def analyze_query(state: State) -> dict:
    """クエリを分析"""
    query = state["query"]
    
    # 言語検出（簡易版）
    if any(c >= '\u4e00' and c <= '\u9fff' for c in query):
        language = "ja"
    elif any(c >= '\uac00' and c <= '\ud7a3' for c in query):
        language = "ko"
    else:
        language = "en"
    
    # 優先度判定（キーワードベース）
    urgent_keywords = ["urgent", "emergency", "至急", "緊急"]
    priority = "high" if any(kw in query.lower() for kw in urgent_keywords) else "normal"
    
    return {
        "language": language,
        "priority": priority
    }

# ルーティング関数
def route_by_analysis(state: State) -> Literal["urgent_ja", "urgent_en", "normal_ja", "normal_en"]:
    """言語と優先度で複合ルーティング"""
    lang = state["language"]
    priority = state["priority"]
    
    if priority == "high" and lang == "ja":
        return "urgent_ja"
    elif priority == "high" and lang == "en":
        return "urgent_en"
    elif lang == "ja":
        return "normal_ja"
    else:
        return "normal_en"

# ノード2a: 緊急・日本語
def handle_urgent_ja(state: State) -> dict:
    response = llm.invoke([HumanMessage(
        content=f"緊急対応として迅速に回答してください: {state['query']}"
    )])
    return {"response": f"【緊急対応】{response.content}"}

# ノード2b: 緊急・英語
def handle_urgent_en(state: State) -> dict:
    response = llm.invoke([HumanMessage(
        content=f"Urgent response required: {state['query']}"
    )])
    return {"response": f"[URGENT] {response.content}"}

# ノード2c: 通常・日本語
def handle_normal_ja(state: State) -> dict:
    response = llm.invoke([HumanMessage(content=state['query'])])
    return {"response": response.content}

# ノード2d: 通常・英語
def handle_normal_en(state: State) -> dict:
    response = llm.invoke([HumanMessage(content=state['query'])])
    return {"response": response.content}

# グラフ構築
workflow = StateGraph(State)

workflow.add_node("analyze", analyze_query)
workflow.add_node("urgent_ja", handle_urgent_ja)
workflow.add_node("urgent_en", handle_urgent_en)
workflow.add_node("normal_ja", handle_normal_ja)
workflow.add_node("normal_en", handle_normal_en)

workflow.add_edge(START, "analyze")

workflow.add_conditional_edges(
    "analyze",
    route_by_analysis,
    {
        "urgent_ja": "urgent_ja",
        "urgent_en": "urgent_en",
        "normal_ja": "normal_ja",
        "normal_en": "normal_en"
    }
)

workflow.add_edge("urgent_ja", END)
workflow.add_edge("urgent_en", END)
workflow.add_edge("normal_ja", END)
workflow.add_edge("normal_en", END)

app = workflow.compile()

# テスト実行
test_queries = [
    "こんにちは、LangGraphについて教えてください",
    "至急：システムエラーの対処法を教えてください",
    "Hello, please explain LangGraph",
    "Urgent: How to fix the system error?"
]

for query in test_queries:
    print(f"\n{'='*60}")
    print(f"クエリ: {query}")
    result = app.invoke({"query": query})
    print(f"言語: {result['language']}, 優先度: {result['priority']}")
    print(f"応答: {result['response'][:100]}...")
```

---

## 3-4. 第3章完全実装例

### 実践的なカスタマーサポートボット

```python
"""
第3章完全実装: カスタマーサポートボット
- 意図分類
- 優先度判定
- 複数ルートの条件分岐
"""

import os
from typing import TypedDict, Literal, NotRequired
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# ============================================
# APIキー設定
# ============================================

os.environ["GEMINI_API_KEY"] = "your-actual-api-key"

if os.environ.get("GEMINI_API_KEY") == "your-actual-api-key":
    raise ValueError("❌ APIキーを設定してください")

# ============================================
# State定義
# ============================================

class State(TypedDict):
    # 必須（ユーザーが渡す）
    customer_message: str
    
    # オプショナル（ノード間で共有）
    intent: NotRequired[str]
    priority: NotRequired[str]
    sentiment: NotRequired[str]
    
    # 最終出力は定義不要
    # response: str

# ============================================
# LLM初期化
# ============================================

llm = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0.3,
    max_tokens=1024
)

print("✅ LLM初期化完了")

# ============================================
# ノード関数定義
# ============================================

def analyze_message(state: State) -> dict:
    """顧客メッセージを分析"""
    message = state["customer_message"]
    
    # 意図分類
    intent_prompt = f"""
    以下の顧客メッセージを分類してください:
    - inquiry: 問い合わせ
    - complaint: クレーム
    - request: 要望
    - feedback: フィードバック
    
    メッセージ: {message}
    カテゴリ名のみを返してください。
    """
    
    intent_response = llm.invoke([HumanMessage(content=intent_prompt)])
    intent = intent_response.content.strip().lower()
    
    # 感情分析
    sentiment_prompt = f"""
    以下のメッセージの感情を分析してください:
    - positive: ポジティブ
    - neutral: 中立
    - negative: ネガティブ
    
    メッセージ: {message}
    感情のみを返してください。
    """
    
    sentiment_response = llm.invoke([HumanMessage(content=sentiment_prompt)])
    sentiment = sentiment_response.content.strip().lower()
    
    # 優先度判定
    if intent == "complaint" or sentiment == "negative":
        priority = "high"
    elif intent == "inquiry":
        priority = "medium"
    else:
        priority = "low"
    
    return {
        "intent": intent,
        "sentiment": sentiment,
        "priority": priority
    }

def route_message(state: State) -> Literal["high_priority", "standard", "low_priority"]:
    """優先度に基づいてルーティング"""
    return {
        "high": "high_priority",
        "medium": "standard",
        "low": "low_priority"
    }[state["priority"]]

def handle_high_priority(state: State) -> dict:
    """高優先度の対応"""
    messages = [
        SystemMessage(content="""
        あなたは経験豊富なカスタマーサポート担当者です。
        顧客の問題を最優先で解決してください。
        丁寧かつ迅速に対応してください。
        """),
        HumanMessage(content=f"""
        顧客メッセージ: {state['customer_message']}
        意図: {state['intent']}
        感情: {state['sentiment']}
        
        上記を考慮して適切に対応してください。
        """)
    ]
    
    response = llm.invoke(messages)
    return {"response": f"【優先対応】{response.content}"}

def handle_standard(state: State) -> dict:
    """標準的な対応"""
    messages = [
        SystemMessage(content="親切かつ丁寧に対応してください。"),
        HumanMessage(content=state["customer_message"])
    ]
    
    response = llm.invoke(messages)
    return {"response": response.content}

def handle_low_priority(state: State) -> dict:
    """低優先度の対応"""
    messages = [
        SystemMessage(content="簡潔に対応してください。"),
        HumanMessage(content=state["customer_message"])
    ]
    
    response = llm.invoke(messages)
    return {"response": response.content}

# ============================================
# グラフ構築
# ============================================

print("\n🏗️ ワークフローグラフを構築中...")

workflow = StateGraph(State)

# ノード追加
workflow.add_node("analyze", analyze_message)
workflow.add_node("high_priority", handle_high_priority)
workflow.add_node("standard", handle_standard)
workflow.add_node("low_priority", handle_low_priority)

# エッジ追加
workflow.add_edge(START, "analyze")

# 条件分岐
workflow.add_conditional_edges(
    "analyze",
    route_message,
    {
        "high_priority": "high_priority",
        "standard": "standard",
        "low_priority": "low_priority"
    }
)

# 終了
workflow.add_edge("high_priority", END)
workflow.add_edge("standard", END)
workflow.add_edge("low_priority", END)

app = workflow.compile()

print("✅ グラフ構築完了")

# ============================================
# グラフ可視化
# ============================================

def visualize_graph(app, filename="ch3_customer_support.png"):
    """グラフをPNG保存"""
    print(f"\n📊 グラフを可視化中...")
    try:
        png_data = app.get_graph().draw_mermaid_png()
        with open(filename, "wb") as f:
            f.write(png_data)
        print(f"✅ グラフを '{filename}' に保存")
    except Exception as e:
        print(f"⚠️ PNG保存失敗: {e}")
        print("\n📝 ASCII版グラフ:")
        print(app.get_graph().draw_ascii())

visualize_graph(app)

# ============================================
# 実行関数
# ============================================

def run_support_bot(app, message: str):
    """サポートボットを実行"""
    print("\n" + "=" * 60)
    print("🤖 カスタマーサポートボット")
    print("=" * 60)
    print(f"📥 顧客メッセージ: {message}")
    
    result = app.invoke({"customer_message": message})
    
    print(f"\n📊 分析結果:")
    print(f"  意図: {result['intent']}")
    print(f"  感情: {result['sentiment']}")
    print(f"  優先度: {result['priority']}")
    print(f"\n📤 応答:\n{result['response']}")
    print("=" * 60)
    
    return result

# ============================================
# 実行
# ============================================

if __name__ == "__main__":
    test_messages = [
        "商品が届いていません。至急確認してください。",
        "製品の使い方について教えてください。",
        "とても良い製品でした。ありがとうございます！",
        "新機能の追加を検討していただけますか？"
    ]
    
    for message in test_messages:
        run_support_bot(app, message)
```

---

## 🎯 第3章のまとめ

### 学んだこと

1. **条件分岐の基本**
   - `add_conditional_edges()`の使い方
   - ルーティング関数の実装
   - マッピング辞書の定義

2. **Stateの設計原則**
   - 必須フィールド: ユーザーが渡すもの
   - オプショナルフィールド: ノード間で共有するもの
   - 最終出力のみで使うフィールドは定義不要

3. **複雑なルーティング**
   - スコアベースの分岐
   - 複数条件の組み合わせ
   - 動的なルート選択

### 重要なポイント

```python
# ✅ 良いState設計
class State(TypedDict):
    input: str                    # 必須（ユーザー提供）
    category: NotRequired[str]    # 他のノードで使用
    sentiment: NotRequired[str]   # 他のノードで使用
    # output: str                 # 定義不要（最終出力のみ）

# ✅ 良いルーティング関数
def route_func(state: State) -> Literal["a", "b", "c"]:
    """明確な型ヒント付き"""
    if state["score"] > 0.8:
        return "a"
    elif state["score"] > 0.5:
        return "b"
    return "c"

# ✅ 良いノード関数
def process_node(state: State) -> dict:
    """必要なフィールドだけ返す"""
    result = some_processing(state["input"])
    return {"category": result}  # 更新するフィールドのみ
```

### 次のステップ

第4章では、**Tavily検索APIとの統合**を学び、外部ツールを使った実用的なエージェントを構築します。

---

これで第3章は完了です！ 🎉

---

# 第4章: ツール統合 - Tavily検索

## 4-1. Tavily検索の基本

### Tavily検索とは

Tavilyは**AI向けに最適化された検索API**です。通常のGoogle検索と違い、LLMが理解しやすい形式で結果を返します。

**特徴:**
- AI向けに最適化された検索結果
- ノイズの少ないクリーンなデータ
- 無料枠: 月間1,000リクエスト
- 高速なレスポンス

### 基本的な使い方

```python
import os
from langchain_community.tools.tavily_search import TavilySearchResults

os.environ["TAVILY_API_KEY"] = "tvly-..."

# 検索ツールの初期化
search_tool = TavilySearchResults(
    tavily_api_key=os.environ["TAVILY_API_KEY"],  # ← 正しい引数名
    max_results=3,
    search_depth="basic"  # "basic" or "advanced"
)

# 検索実行
results = search_tool.invoke("LangGraphとは")
print(results)
```

### 検索結果の構造

```python
# 返り値の例
[
    {
        'url': 'https://example.com/page1',
        'content': '検索結果の要約...',
        'score': 0.95  # 関連性スコア
    },
    {
        'url': 'https://example.com/page2',
        'content': '別の検索結果...',
        'score': 0.87
    }
]
```

---

## 4-2. LLMとツールの連携

### ツールバインディングの仕組み

LangGraphでは、LLMに「ツールを使える能力」を与えます。

```python
import os
from typing import TypedDict, Annotated, Literal, NotRequired
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, AIMessage
import operator

os.environ["GEMINI_API_KEY"] = "your-gemini-key"
os.environ["TAVILY_API_KEY"] = "your-tavily-key"

# State定義（messagesベース）
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]  # メッセージリストを蓄積

# 検索ツール初期化
search_tool = TavilySearchResults(
    tavily_api_key=os.environ["TAVILY_API_KEY"],
    max_results=3,
    search_depth="basic"
)

tools = [search_tool]

# LLMにツールをバインド
llm_with_tools = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0
).bind_tools(tools)

# エージェントノード
def agent_node(state: AgentState) -> dict:
    """LLMがツール使用を判断"""
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

# 条件分岐関数
def should_continue(state: AgentState) -> Literal["tools", "end"]:
    """ツール実行が必要か判断"""
    last_message = state["messages"][-1]
    
    # ツール呼び出しがあるか確認
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    
    return "end"

# ツールノード（自動実行）
from langgraph.prebuilt import ToolNode
tool_node = ToolNode(tools)

# グラフ構築
workflow = StateGraph(AgentState)

workflow.add_node("agent", agent_node)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "agent")

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": END
    }
)

# ツール実行後、再びエージェントへ
workflow.add_edge("tools", "agent")

app = workflow.compile()

# 実行
result = app.invoke({
    "messages": [HumanMessage(content="2024年のノーベル物理学賞受賞者は誰ですか？")]
})

# 最終メッセージを表示
print(result["messages"][-1].content)
```

### 実行フロー

```
START → agent (LLMが判断) →
    ├─ ツール不要 → END
    └─ ツール必要 → tools (検索実行) → agent (結果を使って回答) → END
```

---

## 4-3. 実用的な検索エージェント

### 完全な実装例

```python
"""
第4章完全実装: Tavily検索エージェント
- LLMとツールの連携
- 検索結果を使った回答生成
- エラーハンドリング
"""

import os
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.prebuilt import ToolNode
import operator

# ============================================
# APIキー設定
# ============================================

os.environ["GEMINI_API_KEY"] = "your-gemini-key"
os.environ["TAVILY_API_KEY"] = "your-tavily-key"

if os.environ.get("GEMINI_API_KEY") == "your-gemini-key":
    raise ValueError("❌ GEMINI_API_KEYを設定してください")

if os.environ.get("TAVILY_API_KEY") == "your-tavily-key":
    raise ValueError("❌ TAVILY_API_KEYを設定してください")

# ============================================
# State定義
# ============================================

class AgentState(TypedDict):
    """エージェントの状態
    
    messagesにAnnotated[list, operator.add]を使うことで、
    新しいメッセージが自動的にリストに追加される
    """
    messages: Annotated[list, operator.add]

# ============================================
# ツールとLLMの初期化
# ============================================

# Tavily検索ツール
search_tool = TavilySearchResults(
    tavily_api_key=os.environ["TAVILY_API_KEY"],
    max_results=3,
    search_depth="advanced",  # より詳細な検索
    include_answer=True,      # 要約された回答を含める
    include_raw_content=False # 生のHTMLは除外
)

tools = [search_tool]

# LLMにツールをバインド
llm_with_tools = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0
).bind_tools(tools)

print("✅ ツールとLLMの初期化完了")

# ============================================
# ノード関数
# ============================================

def agent_node(state: AgentState) -> dict:
    """
    エージェントノード: LLMが次のアクションを決定
    
    - ツールを使うべきか判断
    - 使う場合はtool_callsを含むメッセージを返す
    - 使わない場合は直接回答を返す
    """
    messages = state["messages"]
    
    # システムメッセージを追加（初回のみ）
    if len(messages) == 1:
        system_message = SystemMessage(content="""
        あなたは親切なアシスタントです。
        最新の情報が必要な質問には、検索ツールを使ってください。
        検索結果を基に、正確で分かりやすい回答を提供してください。
        """)
        messages = [system_message] + messages
    
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

def should_continue(state: AgentState) -> Literal["tools", "end"]:
    """
    条件分岐: ツール実行が必要か判断
    
    Returns:
        "tools": ツールを実行する
        "end": 処理を終了する
    """
    last_message = state["messages"][-1]
    
    # tool_callsがあればツール実行
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    
    return "end"

# ============================================
# グラフ構築
# ============================================

print("\n🏗️ ワークフローグラフを構築中...")

workflow = StateGraph(AgentState)

# ノード追加
workflow.add_node("agent", agent_node)
workflow.add_node("tools", ToolNode(tools))

# エッジ追加
workflow.add_edge(START, "agent")

# 条件分岐
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": END
    }
)

# ツール実行後、再びエージェントへ
workflow.add_edge("tools", "agent")

app = workflow.compile()

print("✅ グラフ構築完了")

# ============================================
# グラフ可視化
# ============================================

def visualize_graph(app, filename="ch4_search_agent.png"):
    """グラフをPNG保存"""
    print(f"\n📊 グラフを可視化中...")
    try:
        png_data = app.get_graph().draw_mermaid_png()
        with open(filename, "wb") as f:
            f.write(png_data)
        print(f"✅ グラフを '{filename}' に保存")
    except Exception as e:
        print(f"⚠️ PNG保存失敗: {e}")
        print("\n📝 ASCII版グラフ:")
        print(app.get_graph().draw_ascii())

visualize_graph(app)

# ============================================
# 実行関数
# ============================================

def run_search_agent(app, query: str, verbose: bool = True):
    """検索エージェントを実行"""
    if verbose:
        print("\n" + "=" * 60)
        print("🔍 検索エージェント")
        print("=" * 60)
        print(f"📥 質問: {query}")
    
    result = app.invoke({
        "messages": [HumanMessage(content=query)]
    })
    
    if verbose:
        print("\n📊 実行ログ:")
        for i, msg in enumerate(result["messages"], 1):
            msg_type = type(msg).__name__
            print(f"  {i}. {msg_type}")
            
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                print(f"     → ツール呼び出し: {len(msg.tool_calls)}件")
        
        print("\n📤 最終回答:")
        print(result["messages"][-1].content)
        print("=" * 60)
    
    return result

# ============================================
# 実行
# ============================================

if __name__ == "__main__":
    # テストクエリ
    test_queries = [
        "2024年のノーベル物理学賞受賞者は誰ですか？",
        "最新のGPT-4の特徴を教えてください",
        "こんにちは"  # 検索不要なクエリ
    ]
    
    for query in test_queries:
        run_search_agent(app, query)
        print("\n")
```

---

## 4-4. ストリーミング実行

### リアルタイムで進捗を表示

```python
def run_search_agent_stream(app, query: str):
    """ストリーミング実行で進捗を表示"""
    print(f"\n🔍 質問: {query}\n")
    
    for event in app.stream(
        {"messages": [HumanMessage(content=query)]},
        stream_mode="values"
    ):
        # 最新のメッセージを取得
        last_msg = event["messages"][-1]
        
        if isinstance(last_msg, AIMessage):
            if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
                print("🔧 ツールを実行中...")
            else:
                print(f"💬 回答: {last_msg.content}")

# 使用例
run_search_agent_stream(app, "最新のAI技術トレンドは？")
```

---

## 4-5. 複数ツールの統合

### 検索 + 計算ツール

```python
import os
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import ToolNode
import operator

os.environ["GEMINI_API_KEY"] = "your-key"
os.environ["TAVILY_API_KEY"] = "your-key"

# カスタムツール定義
@tool
def calculate(expression: str) -> str:
    """数式を計算します。例: "2 + 2" → "4" """
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"計算エラー: {str(e)}"

# ツールリスト
search_tool = TavilySearchResults(
    tavily_api_key=os.environ["TAVILY_API_KEY"],
    max_results=3
)

tools = [search_tool, calculate]

# State定義
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

# LLMにツールをバインド
llm_with_tools = ChatGoogleGenerativeAI(
    google_api_key=os.environ["GEMINI_API_KEY"],
    model="gemini-2.0-flash-exp",
    temperature=0
).bind_tools(tools)

# ノード定義
def agent_node(state: AgentState) -> dict:
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

def should_continue(state: AgentState) -> Literal["tools", "end"]:
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return "end"

# グラフ構築
workflow = StateGraph(AgentState)
workflow.add_node("agent", agent_node)
workflow.add_node("tools", ToolNode(tools))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": END
    }
)
workflow.add_edge("tools", "agent")

app = workflow.compile()

# 実行
test_queries = [
    "最新のビットコイン価格を調べて、1000ドル投資したら何BTC買えるか計算してください",
    "15 * 234 + 567 を計算してください",
    "LangGraphの最新情報を教えてください"
]

for query in test_queries:
    print(f"\n{'='*60}")
    print(f"質問: {query}")
    result = app.invoke({"messages": [HumanMessage(content=query)]})
    print(f"回答: {result['messages'][-1].content}")
```

---

## 🎯 第4章のまとめ

### 学んだこと

1. **Tavily検索の基本**
   - 正しい引数名: `tavily_api_key`（`api_key`ではない）
   - `search_depth`: "basic" or "advanced"
   - `max_results`: 返す結果の数

2. **ツールバインディング**
   - `bind_tools()`でLLMにツールを渡す
   - LLMが自動的にツール使用を判断
   - `tool_calls`でツール実行要求を確認

3. **messagesベースのState**
   - `Annotated[list, operator.add]`で自動蓄積
   - 会話履歴を保持
   - ツール実行結果も含まれる

4. **ループ構造**
   - agent → tools → agent のループ
   - ツールが不要になるまで繰り返し

### 重要なポイント

```python
# ✅ 正しいTavily初期化
search_tool = TavilySearchResults(
    tavily_api_key=os.environ["TAVILY_API_KEY"],  # ← 正しい引数名
    max_results=3
)

# ✅ 正しいState定義（messagesベース）
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

# ✅ 正しい条件分岐
def should_continue(state: AgentState) -> Literal["tools", "end"]:
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return "end"
```

### 次のステップ

第5章では、**ループ処理とエラーハンドリング**を学び、より堅牢なエージェントを構築します。

---

これで第4章は完了です！ 🎉
from

