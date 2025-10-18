# React 世界一詳しい初心者ガイド

## Reactとは? ⚛️

**React**（リアクト）は、Facebookが2013年に開発した**UIを構築するためのJavaScriptライブラリ**です。

### 一言で言うと 🎯

**「再利用可能な部品（コンポーネント）でWebページを組み立てるライブラリ」**

```
従来のWeb開発       →    React
HTML全体を書く      →    部品を組み合わせる
手動でDOM操作       →    自動で画面更新
スパゲッティコード  →    整理された構造
```

## なぜReactが生まれたの？歴史的背景 📚

### Web開発の進化 🌍

#### 第1世代：静的HTML（1990年代）📄

```html
<html>
  <body>
    <h1>こんにちは</h1>
    <p>これは静的なページです</p>
  </body>
</html>
```

**特徴**:
- 変化しない
- サーバーから完成したHTMLが返ってくる
- クリックしたら別ページに遷移

#### 第2世代：jQuery（2006年〜）🔧

```javascript
// jQueryでのDOM操作
$("#button").click(function() {
  $("#content").html("新しい内容");
  $("#list").append("<li>新しい項目</li>");
});
```

**問題点が顕在化**:
```javascript
// 複雑になると...
let count = 0;

$("#increment").click(function() {
  count++;
  $("#count1").text(count);  // ここを更新
  $("#count2").text(count);  // ここも更新
  $("#count3").text(count);  // ここも更新
  // どこを更新したか分からなくなる！
  
  if (count > 10) {
    $("#message").show();
    $("#warning").addClass("active");
    // 条件分岐で複雑化
  }
});

// 別のボタンでも...
$("#decrement").click(function() {
  count--;
  $("#count1").text(count);  // また同じ更新
  $("#count2").text(count);  // コピペだらけ
  $("#count3").text(count);
  // バグの温床！
});
```

**大規模化すると地獄** 😱:
- どこでDOM操作しているか分からない
- データと表示が同期しない
- バグが頻発
- 保守が困難

### Facebook（現Meta）の課題 💭

2010年頃、Facebookのチャット機能で深刻な問題：

```
ユーザーがメッセージを送信
  ↓
画面の複数箇所を更新する必要
  ↓
- チャットウィンドウ
- 未読バッジ
- 通知アイコン
- タイムライン
  ↓
jQueryで手動更新すると...
  ↓
バグだらけ！更新漏れ！
```

**根本的な問題**: 
「データが変わったら、画面のどこを更新するか」を**人間が管理**していた

### React登場（2013年）✨

Facebook（現Meta）のジョーダン・ウォーク（Jordan Walke）が開発。

**革新的なアイデア**:

```
従来:
データが変わる → 手動でDOM操作 → 画面更新
         ↑
    人間が管理（大変！）

React:
データが変わる → Reactが自動判断 → 画面更新
         ↑
    自動で管理（楽！）
```

**コンセプト**:
1. **宣言的UI**: 「どう更新するか」ではなく「どう表示するか」だけ書く
2. **コンポーネント**: UIを再利用可能な部品に分割
3. **仮想DOM**: 効率的な画面更新

## Reactの3大特徴 🎯

### 1. コンポーネント指向 🧩

```jsx
// ボタンを部品化
function Button({ text, onClick }) {
  return <button onClick={onClick}>{text}</button>;
}

// 使い回せる！
<Button text="保存" onClick={save} />
<Button text="削除" onClick={remove} />
<Button text="キャンセル" onClick={cancel} />
```

**メリット**:
- 再利用可能
- テストしやすい
- 管理しやすい

### 2. 宣言的UI 📝

```jsx
// jQuery（命令的）
if (isLoading) {
  $("#spinner").show();
  $("#content").hide();
} else {
  $("#spinner").hide();
  $("#content").show();
}

// React（宣言的）
{isLoading ? <Spinner /> : <Content />}
// 「今この状態ならこう表示」と書くだけ
```

### 3. 仮想DOM（Virtual DOM）🎭

```
変更があった時:

従来:
DOMを直接操作（遅い）

React:
1. 仮想DOMで差分を計算（速い）
2. 必要な部分だけ更新（速い）
```

**なぜ仮想DOM？🤔**

DOMの操作は**非常に遅い**：
```javascript
// これは遅い
for (let i = 0; i < 1000; i++) {
  document.querySelector("#list").innerHTML += "<li>項目</li>";
}

// Reactは賢く最適化
```

## なぜReactを学ぶべき？🎯

### ✅ メリット

1. **圧倒的な人気** 🌟
   ```
   JavaScriptフレームワーク利用率（2025年）
   1位: React      ████████████████████ 40%
   2位: Vue        ████████ 16%
   3位: Angular    ████ 8%
   ```

2. **就職・転職に有利** 💼
   - フロントエンド求人の大半がReact
   - 高給与
   - リモートワーク案件多数

3. **学習リソースが豊富** 📚
   - 日本語の情報も多い
   - コミュニティが巨大
   - 質問すればすぐ回答

4. **エコシステムが充実** 🔧
   - Next.js（フルスタック）
   - React Native（モバイルアプリ）
   - 無数のライブラリ

5. **大企業が使用** 🏢
   - Meta（Facebook）
   - Instagram
   - Netflix
   - Airbnb
   - Uber
   - など多数

### ❌ デメリット（正直に）

1. **学習コストが高い**
   - JSXという独特の構文
   - Hooksの理解が必要
   - 周辺知識も必要

2. **変化が速い**
   - 頻繁にアップデート
   - ベストプラクティスが変わる

3. **JavaScript必須**
   - JSの知識がないと厳しい
   - ES6以降の文法は必須

**でも**: デメリットを補って余りあるメリット！

## 前提知識 📋

Reactを学ぶ前に必要な知識：

### 必須 ✅
- [ ] HTML基礎
- [ ] CSS基礎
- [ ] **JavaScript基礎**（超重要！）
  - 変数（let, const）
  - 関数（特にアロー関数）
  - 配列メソッド（map, filter）
  - オブジェクト
  - 分割代入
  - スプレッド演算子
  - ES6以降の文法

### あると良い 🔹
- [ ] TypeScript基礎
- [ ] npm/yarn
- [ ] モジュールシステム（import/export）

**JavaScriptが不安な方**: まずJavaScriptを固めましょう！（前のJavaScript入門書を参照）

## 環境構築 🛠️

### 方法1: オンラインエディタ（0秒で開始！）🌐

**最も簡単な方法**

#### CodeSandbox（推奨）

1. [https://codesandbox.io/](https://codesandbox.io/) にアクセス
2. 「Create Sandbox」→「React」を選択
3. すぐに開発開始！

**メリット**:
- インストール不要
- ブラウザだけでOK
- 共有も簡単

### 方法2: Create React App（本格的）💻

#### 前提条件

Node.jsのインストール（v14以上）:
```bash
node --version  # v18.x.x など表示されればOK
```

#### プロジェクト作成

```bash
# React アプリを作成
npx create-react-app my-app

# ディレクトリに移動
cd my-app

# 開発サーバー起動
npm start
```

ブラウザが開いて `http://localhost:3000` に接続される！

#### プロジェクト構造

```
my-app/
├── node_modules/     ← ライブラリ（触らない）
├── public/           ← 静的ファイル
│   └── index.html
├── src/              ← ここでコードを書く
│   ├── App.js        ← メインコンポーネント
│   ├── App.css
│   ├── index.js      ← エントリーポイント
│   └── ...
├── package.json      ← 依存関係
└── README.md
```

**なぜnpx？🤔**:
- `npm`: パッケージをインストール
- `npx`: パッケージを一時的に実行（インストール不要）

### 方法3: Vite（最速！）⚡

```bash
# Viteでプロジェクト作成
npm create vite@latest my-react-app

# テンプレートで「React」を選択

cd my-react-app
npm install
npm run dev
```

**Viteの利点**:
- 起動が超高速
- モダンなビルドツール
- Hot Module Replacement（変更が即座に反映）

**おすすめ**: 新規プロジェクトはVite！

## JSX - JavaScript + HTML 🎨

### JSXとは？

**J**ava**S**cript + **X**ML（HTML）

```jsx
// これがJSX
const element = <h1>こんにちは、世界！</h1>;

// 実は、これはJavaScriptに変換される
const element = React.createElement('h1', null, 'こんにちは、世界！');
```

**なぜJSX？🤔**:
- HTMLっぽく書ける（読みやすい）
- JavaScriptの機能が使える
- コンパイル時にエラーチェック

### JSXの基本ルール 📏

#### 1. 式を埋め込める {}

```jsx
const name = "太郎";
const age = 25;

// 変数を埋め込む
<h1>こんにちは、{name}さん</h1>

// 計算もできる
<p>{age}歳（来年は{age + 1}歳）</p>

// 関数呼び出しも
<p>{getName()}</p>

// 三項演算子
<p>{age >= 18 ? "成人" : "未成年"}</p>
```

#### 2. 1つの親要素が必要

```jsx
// ❌ エラー！複数の要素を並べられない
return (
  <h1>タイトル</h1>
  <p>本文</p>
);

// ✅ OK：1つの親で囲む
return (
  <div>
    <h1>タイトル</h1>
    <p>本文</p>
  </div>
);

// ✅ OK：Fragmentを使う（余計なdivが増えない）
return (
  <>
    <h1>タイトル</h1>
    <p>本文</p>
  </>
);
```

**なぜ1つだけ？🤔**:
- JavaScriptの関数は1つの値しか返せない
- `return a, b;` はできない
- だからJSXも1つの要素のみ

#### 3. className（classではない！）

```jsx
// ❌ エラー！classは予約語
<div class="container">

// ✅ OK
<div className="container">
```

**なぜclassName？🤔**:
- JavaScriptでは`class`は予約語（ES6のクラス構文）
- だから`className`を使う

#### 4. 閉じタグ必須

```jsx
// ❌ HTMLでは許されるが、JSXではエラー
<input type="text">
<img src="image.jpg">

// ✅ 自己閉じタグにする
<input type="text" />
<img src="image.jpg" />
```

#### 5. キャメルケース

```jsx
// ❌ HTML風（ケバブケース）
<button onclick="handleClick">

// ✅ JSX風（キャメルケース）
<button onClick={handleClick}>

// 他の例
<div tabindex="0">     ❌
<div tabIndex={0}>     ✅

<label for="name">     ❌
<label htmlFor="name"> ✅
```

### JSXの中でJavaScript 💻

```jsx
function Greeting() {
  const hour = new Date().getHours();
  
  // if文は{}の中では使えない
  // ❌ エラー
  return <h1>{if (hour < 12) "おはよう"}</h1>;
  
  // ✅ 三項演算子を使う
  return <h1>{hour < 12 ? "おはよう" : "こんにちは"}</h1>;
  
  // ✅ または事前に変数に入れる
  let greeting;
  if (hour < 12) {
    greeting = "おはよう";
  } else if (hour < 18) {
    greeting = "こんにちは";
  } else {
    greeting = "こんばんは";
  }
  
  return <h1>{greeting}</h1>;
}
```

## コンポーネント - 部品の作り方 🧩

### 関数コンポーネント（基本）

```jsx
// シンプルなコンポーネント
function Welcome() {
  return <h1>ようこそ！</h1>;
}

// アロー関数でも可
const Welcome = () => {
  return <h1>ようこそ！</h1>;
};

// 1行なら return 省略可
const Welcome = () => <h1>ようこそ！</h1>;

// 使い方
function App() {
  return (
    <div>
      <Welcome />
      <Welcome />
      <Welcome />
    </div>
  );
}
```

**コンポーネント名は大文字で始める！**

```jsx
// ❌ 小文字で始まると普通のHTMLタグと解釈される
<welcome />

// ✅ 大文字で始める
<Welcome />
```

### Props - データを渡す 📦

```jsx
// propsを受け取る
function Greeting(props) {
  return <h1>こんにちは、{props.name}さん！</h1>;
}

// 分割代入を使う（推奨）
function Greeting({ name }) {
  return <h1>こんにちは、{name}さん！</h1>;
}

// 複数のprops
function UserCard({ name, age, email }) {
  return (
    <div className="card">
      <h2>{name}</h2>
      <p>年齢: {age}</p>
      <p>メール: {email}</p>
    </div>
  );
}

// 使い方
function App() {
  return (
    <div>
      <Greeting name="太郎" />
      <Greeting name="花子" />
      
      <UserCard 
        name="太郎" 
        age={25} 
        email="taro@example.com" 
      />
    </div>
  );
}
```

**重要: Propsは読み取り専用！**

```jsx
function Greeting({ name }) {
  // ❌ エラー！propsは変更できない
  name = "花子";
  
  return <h1>こんにちは、{name}さん</h1>;
}
```

**なぜ読み取り専用？🤔**:
- データの流れを一方向に保つ（親→子）
- 予測可能な動作
- バグを防ぐ

### デフォルトProps

```jsx
function Greeting({ name = "ゲスト" }) {
  return <h1>こんにちは、{name}さん</h1>;
}

// nameを渡さなくても動く
<Greeting />  // こんにちは、ゲストさん
<Greeting name="太郎" />  // こんにちは、太郎さん
```

### children - 子要素を渡す 👶

```jsx
function Card({ children }) {
  return (
    <div className="card">
      {children}
    </div>
  );
}

// 使い方
<Card>
  <h2>タイトル</h2>
  <p>ここに好きな内容を書ける</p>
</Card>
```

**実用例**:
```jsx
function Button({ children, onClick }) {
  return (
    <button className="btn" onClick={onClick}>
      {children}
    </button>
  );
}

// 色々な内容を入れられる
<Button onClick={save}>
  <span>💾</span> 保存
</Button>

<Button onClick={remove}>
  <span>🗑️</span> 削除
</Button>
```

## State - 状態管理 🔄

### なぜStateが必要？🤔

```jsx
// これではボタンを押しても変わらない
function Counter() {
  let count = 0;
  
  const increment = () => {
    count++;  // 変数は変わるが...
    console.log(count);  // コンソールには出る
    // でも画面は更新されない！
  };
  
  return (
    <div>
      <p>カウント: {count}</p>
      <button onClick={increment}>+1</button>
    </div>
  );
}
```

**問題**: 変数が変わってもReactは気づかない → 再レンダリングされない

**解決**: `useState` フックを使う！

### useState - 状態を持つ 📊

```jsx
import { useState } from 'react';

function Counter() {
  // [現在の値, 更新関数] = useState(初期値)
  const [count, setCount] = useState(0);
  
  const increment = () => {
    setCount(count + 1);  // Reactが検知して再レンダリング
  };
  
  return (
    <div>
      <p>カウント: {count}</p>
      <button onClick={increment}>+1</button>
    </div>
  );
}
```

**仕組み**:
```
1. ボタンクリック
   ↓
2. setCount呼び出し
   ↓
3. Reactが変更を検知
   ↓
4. コンポーネントを再レンダリング
   ↓
5. 新しい値で画面更新
```

### useState の色々な使い方

```jsx
function Examples() {
  // 数値
  const [count, setCount] = useState(0);
  
  // 文字列
  const [name, setName] = useState("");
  
  // 真偽値
  const [isOpen, setIsOpen] = useState(false);
  
  // 配列
  const [items, setItems] = useState([]);
  
  // オブジェクト
  const [user, setUser] = useState({ name: "", age: 0 });
  
  // 更新方法
  setCount(count + 1);              // 直接値
  setCount(prev => prev + 1);       // 関数（推奨！）
  setIsOpen(!isOpen);               // 反転
  setItems([...items, "新しい"]);   // 配列に追加
  setUser({ ...user, age: 26 });    // オブジェクト更新
}
```

**なぜ関数形式？🤔**

```jsx
// 悪い例
const handleClick = () => {
  setCount(count + 1);
  setCount(count + 1);
  setCount(count + 1);
  // 全部同じ値を使うので、結果は+1だけ！
};

// 良い例
const handleClick = () => {
  setCount(prev => prev + 1);  // 0 → 1
  setCount(prev => prev + 1);  // 1 → 2
  setCount(prev => prev + 1);  // 2 → 3
  // ちゃんと+3される
};
```

### 実用例：TODOリスト ✅

```jsx
import { useState } from 'react';

function TodoApp() {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState("");
  
  const addTodo = () => {
    if (inputValue.trim() === "") return;
    
    const newTodo = {
      id: Date.now(),
      text: inputValue,
      completed: false
    };
    
    setTodos([...todos, newTodo]);
    setInputValue("");
  };
  
  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id 
        ? { ...todo, completed: !todo.completed }
        : todo
    ));
  };
  
  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };
  
  return (
    <div>
      <h1>TODOリスト</h1>
      <input
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyPress={(e) => e.key === 'Enter' && addTodo()}
        placeholder="やることを入力"
      />
      <button onClick={addTodo}>追加</button>
      
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
            />
            <span style={{ 
              textDecoration: todo.completed ? 'line-through' : 'none' 
            }}>
              {todo.text}
            </span>
            <button onClick={() => deleteTodo(todo.id)}>削除</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

## イベントハンドリング 🖱️

### 基本のイベント

```jsx
function EventExamples() {
  const [value, setValue] = useState("");
  
  // クリック
  const handleClick = () => {
    alert("クリックされた！");
  };
  
  // 入力
  const handleChange = (e) => {
    setValue(e.target.value);
  };
  
  // 送信
  const handleSubmit = (e) => {
    e.preventDefault();  // デフォルト動作を防ぐ
    console.log("送信:", value);
  };
  
  // キー押下
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      console.log("Enterが押された");
    }
  };
  
  return (
    <div>
      <button onClick={handleClick}>クリック</button>
      
      <input 
        value={value}
        onChange={handleChange}
        onKeyDown={handleKeyDown}
      />
      
      <form onSubmit={handleSubmit}>
        <button type="submit">送信</button>
      </form>
    </div>
  );
}
```

**注意: () を付けない！**

```jsx
// ❌ これだと即座に実行される
<button onClick={handleClick()}>

// ✅ 関数を渡す
<button onClick={handleClick}>

// ✅ 引数を渡したい場合はアロー関数
<button onClick={() => handleClick("引数")}>
```

### よくあるイベント一覧

```jsx
<button onClick={handle}>          {/* クリック */}
<button onDoubleClick={handle}>    {/* ダブルクリック */}

<input onChange={handle}>          {/* 入力変更 */}
<input onFocus={handle}>           {/* フォーカス */}
<input onBlur={handle}>            {/* フォーカス外れ */}

<input onKeyDown={handle}>         {/* キー押下 */}
<input onKeyUp={handle}>           {/* キー離す */}
<input onKeyPress={handle}>        {/* キー入力 */}

<div onMouseEnter={handle}>        {/* マウス入る */}
<div onMouseLeave={handle}>        {/* マウス出る */}
<div onMouseMove={handle}>         {/* マウス移動 */}

<form onSubmit={handle}>           {/* フォーム送信 */}
```

## 条件付きレンダリング 🔀

### if文を使う

```jsx
function Greeting({ isLoggedIn }) {
  if (isLoggedIn) {
    return <h1>おかえりなさい！</h1>;
  }
  return <h1>ログインしてください</h1>;
}
```

### 三項演算子（推奨）

```jsx
function Greeting({ isLoggedIn }) {
  return (
    <h1>
      {isLoggedIn ? "おかえりなさい！" : "ログインしてください"}
    </h1>
  );
}

// 複雑な場合
function UserStatus({ user }) {
  return (
    <div>
      {user.isAdmin ? (
        <AdminPanel />
      ) : (
        <UserPanel />
      )}
    </div>
  );
}
```

### 論理AND演算子 &&

```jsx
function Mailbox({ unreadMessages }) {
  return (
    <div>
      <h1>メールボックス</h1>
      {unreadMessages.length > 0 && (
        <p>未読メッセージが{unreadMessages.length}件あります</p>
      )}
    </div>
  );
}

// 仕組み
// true && <Component /> → <Component />が表示される
// false && <Component /> → 何も表示されない
```

**⚠️ 注意：数値0の罠**

```jsx
const count = 0;

// ❌ 0が表示される！
{count && <p>カウント: {count}</p>}

// ✅ 明示的に真偽値に
{count > 0 && <p>カウント: {count}</p>}
```

**なぜ0が表示される？🤔**:
- JavaScriptでは`0 && 何か`は`0`を返す
- Reactは`0`を表示する
- `false`、`null`、`undefined`は表示しない

## リストのレンダリング 📋

### map を使う

```jsx
function FruitList() {
  const fruits = ["りんご", "バナナ", "オレンジ"];
  
  return (
    <ul>
      {fruits.map((fruit, index) => (
        <li key={index}>{fruit}</li>
      ))}
    </ul>
  );
}
```

### key属性の重要性 🔑

```jsx
// ❌ 悪い例：keyがない
fruits.map(fruit => <li>{fruit}</li>)

// ⚠️ あまり良くない：indexをkeyに
fruits.map((fruit, index) => <li key={index}>{fruit}</li>)

// ✅ 良い例：一意なIDをkeyに
fruits.map(fruit => <li key={fruit.id}>{fruit.name}</li>)
```

**なぜkeyが必要？🤔**

Reactがどの要素が変更されたか識別するため：

```
変更前: [A, B, C]
変更後: [A, B, C, D]

keyがあると:
→ Dだけ追加すればいい（効率的）

keyがないと:
→ 全部作り直す（非効率）
```

**なぜindexはダメ？🤔**

```jsx
// 初期状態
["りんご", "バナナ", "オレンジ"]
// key: [0, 1, 2]

// 先頭に追加
["いちご", "りんご", "バナナ", "オレンジ"]
// key: [0, 1, 2, 3]

// keyが変わってしまう！
// いちご: 0（新しい）
// りんご: 1（0から変わった）
// バナナ: 2（1から変わった）
// オレンジ: 3（2から変わった）

// 結果: 全部再レンダリング
```

### 実用例：ユーザーリスト

```jsx
function UserList() {
  const users = [
    { id: 1, name: "太郎", age: 25 },
    { id: 2, name: "花子", age: 22 },
    { id: 3, name: "次郎", age: 30 }
  ];
  
  return (
    <div>
      {users.map(user => (
        <div key={user.id} className="user-card">
          <h3>{user.name}</h3>
          <p>年齢: {user.age}</p>
        </div>
      ))}
    </div>
  );
}
```

## useEffect - 副作用フック ⚡

### 副作用とは？

**副作用（Side Effect）**: コンポーネントの描画以外の処理

例：
- データ取得（API呼び出し）
- タイマー設定
- DOM操作
- ログ出力
- ローカルストレージへの保存

### 基本の使い方

```jsx
import { useEffect, useState } from 'react';

function Example() {
  const [count, setCount] = useState(0);
  
  // コンポーネントがマウントされた時 & 更新された時
  useEffect(() => {
    console.log("レンダリングされた");
    document.title = `${count}回クリック`;
  });
  
  return (
    <div>
      <p>カウント: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
    </div>
  );
}
```

### 依存配列 📦

```jsx
// パターン1: 毎回実行
useEffect(() => {
  console.log("毎レンダリング時");
});

// パターン2: 初回のみ実行
useEffect(() => {
  console.log("マウント時のみ");
}, []); // 空配列

// パターン3: 特定の値が変わった時のみ
useEffect(() => {
  console.log("countが変わった");
}, [count]); // countが変わった時だけ

// パターン4: 複数の依存
useEffect(() => {
  console.log("countまたはnameが変わった");
}, [count, name]);
```

**依存配列のルール**:
- `undefined`（なし）→ 毎回実行
- `[]`（空配列）→ 初回のみ
- `[a, b]`（値あり）→ a または b が変わった時

### クリーンアップ 🧹

```jsx
useEffect(() => {
  // セットアップ
  const timerId = setInterval(() => {
    console.log("1秒経過");
  }, 1000);
  
  // クリーンアップ（return で関数を返す）
  return () => {
    clearInterval(timerId);
    console.log("タイマー停止");
  };
}, []);
```

**いつクリーンアップ？**
- コンポーネントがアンマウントされる時
- 次のeffectが実行される前

### 実用例：データ取得 📡

```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    // データ取得
    const fetchUser = async () => {
      try {
        setLoading(true);
        const response = await fetch(`/api/users/${userId}`);
        const data = await response.json();
        setUser(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    
    fetchUser();
  }, [userId]); // userIdが変わったら再取得
  
  if (loading) return <div>読み込み中...</div>;
  if (error) return <div>エラー: {error}</div>;
  if (!user) return <div>ユーザーが見つかりません</div>;
  
  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </div>
  );
}
```

### よくある間違い ⚠️

```jsx
// ❌ 無限ループ
useEffect(() => {
  setCount(count + 1);  // countが変わる
}, [count]);  // countが変わったらeffect実行 → また変わる → ...

// ❌ 依存配列の指定漏れ
useEffect(() => {
  console.log(count);  // countを使っているのに
}, []);  // 依存配列に入れていない

// ✅ 正しい
useEffect(() => {
  console.log(count);
}, [count]);
```

## フォーム処理 📝

### 制御コンポーネント

```jsx
function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("送信:", { email, password });
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="メールアドレス"
      />
      
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="パスワード"
      />
      
      <button type="submit">ログイン</button>
    </form>
  );
}
```

**制御コンポーネントとは？**
- Reactのstateが唯一の情報源
- inputの値は常にstateと同期

### 複数の入力を扱う

```jsx
function UserForm() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    age: "",
    gender: "",
    agree: false
  });
  
  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value
    });
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("送信:", formData);
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input
        name="name"
        value={formData.name}
        onChange={handleChange}
        placeholder="名前"
      />
      
      <input
        name="email"
        type="email"
        value={formData.email}
        onChange={handleChange}
        placeholder="メール"
      />
      
      <input
        name="age"
        type="number"
        value={formData.age}
        onChange={handleChange}
        placeholder="年齢"
      />
      
      <select name="gender" value={formData.gender} onChange={handleChange}>
        <option value="">選択してください</option>
        <option value="male">男性</option>
        <option value="female">女性</option>
        <option value="other">その他</option>
      </select>
      
      <label>
        <input
          name="agree"
          type="checkbox"
          checked={formData.agree}
          onChange={handleChange}
        />
        利用規約に同意する
      </label>
      
      <button type="submit" disabled={!formData.agree}>
        送信
      </button>
    </form>
  );
}
```

### バリデーション

```jsx
function SignupForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  
  const validate = () => {
    const newErrors = {};
    
    if (!email) {
      newErrors.email = "メールアドレスは必須です";
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      newErrors.email = "有効なメールアドレスを入力してください";
    }
    
    if (!password) {
      newErrors.password = "パスワードは必須です";
    } else if (password.length < 8) {
      newErrors.password = "パスワードは8文字以上必要です";
    }
    
    return newErrors;
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    
    const validationErrors = validate();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }
    
    // 送信処理
    console.log("送信成功");
    setErrors({});
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <div>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="メールアドレス"
        />
        {errors.email && <p className="error">{errors.email}</p>}
      </div>
      
      <div>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="パスワード"
        />
        {errors.password && <p className="error">{errors.password}</p>}
      </div>
      
      <button type="submit">登録</button>
    </form>
  );
}
```

## コンポーネント間の通信 📡

### 親→子（Props）⬇️

```jsx
function Parent() {
  const message = "こんにちは";
  
  return <Child message={message} />;
}

function Child({ message }) {
  return <p>{message}</p>;
}
```

### 子→親（コールバック）⬆️

```jsx
function Parent() {
  const [count, setCount] = useState(0);
  
  const increment = () => {
    setCount(count + 1);
  };
  
  return (
    <div>
      <p>カウント: {count}</p>
      <Child onIncrement={increment} />
    </div>
  );
}

function Child({ onIncrement }) {
  return <button onClick={onIncrement}>+1</button>;
}
```

### 兄弟間の通信 ↔️

```jsx
// 共通の親でstateを管理
function Parent() {
  const [message, setMessage] = useState("");
  
  return (
    <div>
      <Sender onSend={setMessage} />
      <Receiver message={message} />
    </div>
  );
}

function Sender({ onSend }) {
  const [input, setInput] = useState("");
  
  const handleSend = () => {
    onSend(input);
    setInput("");
  };
  
  return (
    <div>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={handleSend}>送信</button>
    </div>
  );
}

function Receiver({ message }) {
  return <p>受信: {message}</p>;
}
```

**原則**: データは上から下へ流れる（単一方向データフロー）

## よくあるエラーと解決法 🆘

### 1. Cannot read property 'X' of undefined

```jsx
// ❌ エラー
function User({ user }) {
  return <div>{user.name}</div>;
}
// userがundefinedの場合エラー

// ✅ 解決法1: 条件分岐
function User({ user }) {
  if (!user) return <div>Loading...</div>;
  return <div>{user.name}</div>;
}

// ✅ 解決法2: オプショナルチェイニング
function User({ user }) {
  return <div>{user?.name}</div>;
}

// ✅ 解決法3: デフォルト値
function User({ user = {} }) {
  return <div>{user.name || "名無し"}</div>;
}
```

### 2. Maximum update depth exceeded

```jsx
// ❌ 無限ループ
function Counter() {
  const [count, setCount] = useState(0);
  
  setCount(count + 1);  // レンダリング中にstate更新
  
  return <div>{count}</div>;
}

// ✅ 解決法：イベントハンドラ内で更新
function Counter() {
  const [count, setCount] = useState(0);
  
  const increment = () => {
    setCount(count + 1);
  };
  
  return (
    <div>
      {count}
      <button onClick={increment}>+1</button>
    </div>
  );
}
```

### 3. Each child in a list should have a unique "key" prop

```jsx
// ❌ keyがない
{items.map(item => <li>{item}</li>)}

// ✅ keyを付ける
{items.map(item => <li key={item.id}>{item.name}</li>)}
```

### 4. Objects are not valid as a React child

```jsx
// ❌ オブジェクトを直接表示
const user = { name: "太郎", age: 25 };
return <div>{user}</div>;

// ✅ プロパティを表示
return <div>{user.name}</div>;

// ✅ JSON文字列化
return <div>{JSON.stringify(user)}</div>;
```

### 5. Cannot update during an existing state transition

```jsx
// ❌ 別のコンポーネントのstateを直接更新
function Child({ setParentState }) {
  setParentState(newValue);  // レンダリング中に実行
  return <div>...</div>;
}

// ✅ useEffectまたはイベントハンドラで更新
function Child({ setParentState }) {
  useEffect(() => {
    setParentState(newValue);
  }, []);
  
  return <div>...</div>;
}
```

## 実践プロジェクト：カウンターアプリ 🔢

完全に動作するカウンターアプリ：

```jsx
import { useState } from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(0);
  const [step, setStep] = useState(1);
  const [history, setHistory] = useState([0]);
  
  const increment = () => {
    const newCount = count + step;
    setCount(newCount);
    setHistory([...history, newCount]);
  };
  
  const decrement = () => {
    const newCount = count - step;
    setCount(newCount);
    setHistory([...history, newCount]);
  };
  
  const reset = () => {
    setCount(0);
    setHistory([0]);
  };
  
  const undo = () => {
    if (history.length > 1) {
      const newHistory = history.slice(0, -1);
      setHistory(newHistory);
      setCount(newHistory[newHistory.length - 1]);
    }
  };
  
  return (
    <div className="App">
      <h1>カウンターアプリ</h1>
      
      <div className="counter-display">
        <h2>{count}</h2>
      </div>
      
      <div className="controls">
        <button onClick={decrement} className="btn btn-danger">
          -{step}
        </button>
        <button onClick={reset} className="btn btn-secondary">
          リセット
        </button>
        <button onClick={increment} className="btn btn-success">
          +{step}
        </button>
      </div>
      
      <div className="step-control">
        <label>
          増減の幅:
          <input
            type="number"
            value={step}
            onChange={(e) => setStep(Number(e.target.value))}
            min="1"
          />
        </label>
      </div>
      
      <button 
        onClick={undo} 
        disabled={history.length <= 1}
        className="btn btn-warning"
      >
        元に戻す
      </button>
      
      <div className="history">
        <h3>履歴</h3>
        <p>{history.join(' → ')}</p>
      </div>
    </div>
  );
}

export default App;
```

**CSS（App.css）**:
```css
.App {
  text-align: center;
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  font-family: sans-serif;
}

.counter-display {
  font-size: 72px;
  font-weight: bold;
  margin: 30px 0;
  color: #2c3e50;
}

.controls {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin: 20px 0;
}

.btn {
  padding: 15px 30px;
  font-size: 18px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-success {
  background: #27ae60;
  color: white;
}

.btn-danger {
  background: #e74c3c;
  color: white;
}

.btn-secondary {
  background: #95a5a6;
  color: white;
}

.btn-warning {
  background: #f39c12;
  color: white;
}

.step-control {
  margin: 20px 0;
}

.step-control input {
  margin-left: 10px;
  padding: 8px;
  font-size: 16px;
  width: 80px;
}

.history {
  margin-top: 30px;
  padding: 20px;
  background: #ecf0f1;
  border-radius: 8px;
}
```

## 学習ロードマップ 🗺️

### レベル1: 基礎（2週間）🌱

- [ ] JSXの基本
- [ ] コンポーネントの作成
- [ ] Props
- [ ] useState
- [ ] イベントハンドリング
- [ ] 条件付きレンダリング
- [ ] リスト表示

**目標**: 簡単なカウンターやTODOリストが作れる

**練習問題**:
- カウンター
- TODOリスト
- じゃんけんゲーム

### レベル2: 中級（1ヶ月）🌿

- [ ] useEffect
- [ ] フォーム処理
- [ ] データ取得（fetch）
- [ ] コンポーネント設計
- [ ] カスタムフック
- [ ] useContext（状態管理）

**目標**: 実用的なアプリが作れる

**練習問題**:
- 天気アプリ（API使用）
- メモアプリ
- クイズアプリ
- ショッピングカート

### レベル3: 上級（2ヶ月）🌳

- [ ] useReducer
- [ ] useRef
- [ ] useMemo / useCallback（最適化）
- [ ] React Router（ページ遷移）
- [ ] 状態管理ライブラリ（Redux、Zustand）
- [ ] テスト（Jest、React Testing Library）

**目標**: 本格的なWebアプリが作れる

**練習問題**:
- ブログシステム
- SNSのクローン
- ダッシュボード
- Eコマースサイト

### レベル4: エキスパート（継続）🚀

- [ ] Next.js（SSR、SSG）
- [ ] TypeScript + React
- [ ] パフォーマンス最適化
- [ ] アクセシビリティ
- [ ] デザインシステム構築
- [ ] モノレポ管理

## Next.js へのステップアップ 🚀

Reactを習得したら**Next.js**がおすすめ！

### Next.jsとは？

Reactの**フレームワーク**（Reactを使いやすくしたもの）

**機能**:
- ファイルベースルーティング
- サーバーサイドレンダリング（SSR）
- 静的サイト生成（SSG）
- API Routes（バックエンド不要）
- 画像最適化
- TypeScript標準対応

### Create React App vs Next.js

| 特徴 | Create React App | Next.js |
|------|------------------|---------|
| 学習難易度 | 易しい | 中程度 |
| SEO | △ | ◎ |
| ルーティング | 別途必要 | 組み込み |
| 初期表示 | 遅い | 速い |
| おすすめ用途 | 学習、SPA | 本番アプリ |

**結論**: 
- 学習目的 → Create React App
- 本番アプリ → Next.js

## 学習リソース 📚

### 公式ドキュメント
- [React 公式](https://ja.react.dev/) - 最高のリソース
- [React Tutorial](https://ja.react.dev/learn/tutorial-tic-tac-toe) - 三目並べチュートリアル

### オンライン学習
- freeCodeCamp
- Scrimba（インタラクティブ）
- Udemy（有料）

### YouTube
- Codevolution（英語）
- プログラミングチュートリアル（日本語）

### 書籍
- 「りあクト！」
- 「React実践の教科書」

### 練習サイト
- Frontend Mentor
- Devchallenges.io

## まとめ 🎓

### Reactの本質

```
React = UIを部品化して組み立てる
      = 宣言的にUIを記述
      = データが変わったら自動で画面更新
```

### 学習のコツ 💡

1. **小さく始める**
   - 最初から大きなアプリを作らない
   - カウンター、TODOリストから

2. **公式ドキュメントを読む**
   - 最高の学習リソース
   - 日本語訳も充実

3. **毎日コードを書く**
   - 10分でもOK
   - 継続が大事

4. **エラーを恐れない**
   - エラーメッセージをよく読む
   - デベロッパーツールを活用

5. **他人のコードを読む**
   - GitHub
   - CodeSandbox

### 次のステップ 🚀

1. **基礎を固める**
   - Props、State、useEffectを完璧に

2. **小さなプロジェクトを作る**
   - TODOリスト
   - 天気アプリ
   - メモアプリ

3. **フレームワークを学ぶ**
   - Next.js（推奨）
   - Remix

4. **状態管理を学ぶ**
   - Context API
   - Zustand
   - Redux（必要なら）

5. **TypeScriptと組み合わせる**
   - 型安全性
   - 大規模開発に必須

### 最後に 🎉

Reactは**最初は難しいけど、慣れると最高に楽しい**！

**「なんでこんな面倒なの？」** と思うかもしれません。
でも、大規模アプリを作り始めると...

**「Reactなしでは無理！」** と気づきます。

焦らず、楽しみながら学んでいきましょう！

**Happy Reacting! ⚛️**

---

## チートシート（印刷用）📄

```jsx
// コンポーネント
function MyComponent() {
  return <div>Hello</div>;
}

// Props
function Greeting({ name }) {
  return <h1>Hello, {name}</h1>;
}

// State
const [count, setCount] = useState(0);
setCount(count + 1);

// Effect
useEffect(() => {
  // 処理
  return () => {/* クリーンアップ */};
}, [依存配列]);

// イベント
<button onClick={handleClick}>Click</button>

// 条件
{isTrue ? <A /> : <B />}
{isTrue && <Component />}

// リスト
{items.map(item => (
  <li key={item.id}>{item.name}</li>
))}

// フォーム
<input 
  value={value}
  onChange={(e) => setValue(e.target.value)}
/>

// 子要素
function Card({ children }) {
  return <div>{children}</div>;
}
```
