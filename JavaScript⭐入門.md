# JavaScript 世界一詳しい初心者ガイド

## JavaScriptとは? 💻

**JavaScript**（ジャバスクリプト）は、1995年にネットスケープコミュニケーションズのブレンダン・アイク（Brendan Eich）が開発した**プログラミング言語**です。

### 驚きの事実 😲

JavaScriptは**たった10日間**で作られました！

```
1995年5月
ブレンダン・アイク氏「Webページに動きをつける言語を作って！」
       ↓
   10日間で開発
       ↓
    JavaScript誕生
```

**当初の名前**: Mocha → LiveScript → JavaScript

### なぜ「Java」Script？Javaとは別物！🤔

**重要**: JavaとJavaScriptは**全く別の言語**です！

```
Java        ≠    JavaScript
コーヒーと   ≠    コーヒースクリプト
```

**名前の由来**:
1. 1995年当時、Java言語が大ブーム
2. マーケティング戦略で「Java」の名前を借りた
3. 実際には全く関係ない別の言語

**例え**: 
- 「ハムスター」と「ハム」が別物なのと同じ
- インド（India）とインドネシア（Indonesia）が別の国なのと同じ

## JavaScriptの特徴と歴史 📚

### 誕生当初（1995年）🌱

**目的**: Webページに簡単な動きを付ける

**できたこと**:
- フォームの入力チェック
- 画像のロールオーバー（マウスを乗せると変わる）
- ポップアップウィンドウ
- 簡単なアニメーション

**想定していなかったこと**:
- 大規模アプリケーション開発
- サーバーサイド開発
- モバイルアプリ開発
- ゲーム開発

### 進化の歴史 🚀

```
1995年 ━ JavaScript誕生
         「Webページをちょっと動かす」程度

1999年 ━ AJAX登場
         「ページ遷移なしでデータ取得」

2009年 ━ Node.js登場
         「サーバーサイドでも動く！」

2015年 ━ ES6（ES2015）
         「モダンな文法、クラス構文」

2025年 ━ 現在
         「フロント・バック・モバイル全てで使える万能言語」
```

### 現代のJavaScript（2025年）🌟

**できること**:
- ✅ Webサイト（フロントエンド）
- ✅ サーバー（Node.js、バックエンド）
- ✅ モバイルアプリ（React Native）
- ✅ デスクトップアプリ（Electron）
- ✅ ゲーム開発
- ✅ IoT（組み込み機器）
- ✅ 機械学習（TensorFlow.js）

**ほぼ何でもできる！**

## なぜJavaScriptを学ぶべき？🎯

### ✅ 圧倒的なメリット

#### 1. 唯一のブラウザ言語 🌐

```
ブラウザで動く言語 = JavaScript のみ
```

- Chrome、Firefox、Safari、Edge
- 全てのブラウザがJavaScriptを実行できる
- 他の選択肢がない（独占状態）

**なぜ他の言語じゃダメ？🤔**
- ブラウザのセキュリティの問題
- 標準化の難しさ
- 歴史的経緯

最近はWebAssemblyという選択肢もありますが、JavaScriptが主流です。

#### 2. 初心者に優しい 🌱

```javascript
// これだけで動く！
console.log("Hello, World!");
```

- コンパイル不要（書いたらすぐ実行）
- 環境構築が簡単（ブラウザがあればOK）
- エラーに寛容（途中で止まらない）
- 直感的な文法

#### 3. 就職・転職に強い 💼

**求人数**:
```
プログラミング言語別求人数（2025年）
1位: JavaScript  ████████████████ 
2位: Python      ███████████
3位: Java        ██████████
```

- Web開発では必須スキル
- フロントエンド、バックエンド両方で需要
- スタートアップから大企業まで使われている

#### 4. コミュニティが巨大 👥

- Stack Overflow（質問サイト）で最も質問が多い
- npm（パッケージ管理）には200万以上のライブラリ
- 日本語の情報も豊富

#### 5. 1つの言語で全部できる 🎯

```
JavaScript一択で全て開発可能

フロントエンド  → React、Vue、Angular
バックエンド    → Node.js、Express
モバイルアプリ   → React Native
デスクトップ    → Electron
```

**他の言語では**:
- フロント: JavaScript
- バック: Python、Ruby、Go...
- モバイル: Swift、Kotlin...

と、複数の言語を学ぶ必要がある

### ❌ デメリット（正直に）

1. **速度が遅い**
   - C言語などと比べると遅い
   - でも、Web開発では十分速い

2. **型がない（あいまい）**
   - バグが出やすい
   - 解決策: TypeScript を使う

3. **ブラウザ間の差異**
   - 昔は大問題（IEとの戦い）
   - 現在はほぼ解消

4. **歴史的な設計ミス**
   - 10日間で作られた影響
   - 互換性のため修正できない部分もある

**でも**: メリットの方が圧倒的に大きい！

## 環境構築 - 3つの方法 🛠️

JavaScriptは**環境構築が超簡単**！

### 方法1: ブラウザのコンソール（0秒で開始！）🌐

**最も簡単な方法**

#### Chromeの場合：

1. Chromeブラウザを開く
2. `F12`キー（Macは`Cmd + Option + I`）
3. 「Console」タブをクリック
4. コードを入力してEnter

```javascript
// 試してみよう！
console.log("Hello, JavaScript!");
// → Hello, JavaScript! と表示される

2 + 3
// → 5

"Hello" + " " + "World"
// → Hello World
```

**これだけでJavaScriptが動く！**

**なぜブラウザで動くの？🤔**
- ブラウザにはJavaScriptエンジンが組み込まれている
- Chrome → V8エンジン
- Firefox → SpiderMonkey
- Safari → JavaScriptCore

### 方法2: HTMLファイルで実行 📄

#### ステップ1: HTMLファイルを作成

**index.html**
```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>JavaScript練習</title>
</head>
<body>
  <h1>JavaScriptのテスト</h1>
  
  <!-- JavaScriptをここに書く -->
  <script>
    console.log("Hello from HTML!");
    alert("こんにちは！");
  </script>
</body>
</html>
```

#### ステップ2: ブラウザで開く

1. ファイルを保存
2. ダブルクリックでブラウザが開く
3. アラートが表示される
4. F12でコンソールを開くと「Hello from HTML!」

#### 外部ファイルに分離（推奨）

**index.html**
```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>JavaScript練習</title>
</head>
<body>
  <h1>JavaScriptのテスト</h1>
  
  <!-- 外部JavaScriptファイルを読み込む -->
  <script src="script.js"></script>
</body>
</html>
```

**script.js**
```javascript
console.log("Hello from external file!");
alert("外部ファイルから実行！");
```

**なぜ外部ファイルに分けるの？🤔**
- HTMLとJavaScriptの責任を分離
- 複数のHTMLで同じJavaScriptを使い回せる
- 読みやすい、管理しやすい

### 方法3: Node.js（サーバーサイド）⚙️

#### インストール

[https://nodejs.org/](https://nodejs.org/) から最新版をダウンロード

確認：
```bash
node --version
# v20.x.x など表示されればOK
```

#### 実行方法

**hello.js**
```javascript
console.log("Hello from Node.js!");
```

実行：
```bash
node hello.js
```

**ブラウザとNode.jsの違い🤔**

| 項目 | ブラウザ | Node.js |
|------|----------|---------|
| 実行環境 | クライアント（ユーザーのPC） | サーバー |
| DOM操作 | ✅ できる | ❌ できない |
| ファイル読み書き | ❌ できない（セキュリティ） | ✅ できる |
| 用途 | フロントエンド | バックエンド |

## 基本文法 - Syntax 📝

### コメント（メモ）💬

```javascript
// 1行コメント
// この行は実行されない

/* 
  複数行コメント
  ここも実行されない
  説明を書く場所
*/

/**
 * ドキュメンテーションコメント
 * 関数の説明などに使う
 */
```

**なぜコメントが必要？🤔**
- 自分のメモ
- 他の人への説明
- 一時的にコードを無効化

### 文の終わり - セミコロン 🔚

```javascript
// セミコロンあり（推奨）
console.log("Hello");
let x = 10;

// セミコロンなしでも動く
console.log("Hello")
let y = 20

// でも、たまに問題が起きる
let a = b
(function() {
  // これはエラーになる！
})()

// セミコロンがあれば明確
let a = b;
(function() {
  // OK
})();
```

**ベストプラクティス**: セミコロンは付ける！

### 変数宣言 - let, const, var 📦

#### let（レット）- 変更可能な変数

```javascript
let name = "太郎";
console.log(name);  // 太郎

name = "花子";  // 再代入OK
console.log(name);  // 花子
```

#### const（コンスト）- 変更不可能な定数

```javascript
const PI = 3.14159;
console.log(PI);  // 3.14159

PI = 3.14;  // エラー！再代入できない
```

**いつconst、いつlet？🤔**

基本ルール：
1. **最初はconst**を使う
2. 後で変更する必要があれば**let**に変更

```javascript
// ❌ 悪い例：何でもlet
let userName = "太郎";
let userAge = 25;
let MAX_USERS = 100;

// ✅ 良い例
const userName = "太郎";  // 変わらない
let userAge = 25;         // 年齢は変わる
const MAX_USERS = 100;    // 定数
```

#### var（古い書き方、使わない！）⚠️

```javascript
var oldStyle = "昔の書き方";
// 問題が多いので使わない！
```

**varの問題点**:
1. 再宣言できてしまう（バグの原因）
2. スコープの挙動が直感的でない
3. ES6（2015年）でlet/constが導入された

**結論**: let/constを使う、varは忘れる！

### 変数の命名規則 📛

```javascript
// ✅ 良い命名
let userName = "太郎";        // キャメルケース
let user_name = "太郎";       // スネークケース（Pythonスタイル）
const MAX_COUNT = 100;       // 定数は大文字

// ❌ ダメな命名
let 1user = "太郎";          // 数字から始まるのはNG
let user-name = "太郎";      // ハイフンはNG
let let = "太郎";            // 予約語はNG
```

**命名のベストプラクティス**:
- 意味のある名前を付ける
- `data`や`value`より`userName`や`totalPrice`
- 英語で書く（日本語も可能だが非推奨）
- キャメルケースが一般的（最初は小文字、以降は大文字開始）

## データ型 - Data Types 📊

JavaScriptには**8つの型**があります。

### プリミティブ型（基本型）🧱

#### 1. Number（数値）🔢

```javascript
let integer = 42;          // 整数
let float = 3.14;          // 小数
let negative = -10;        // 負の数
let big = 1_000_000;       // 区切り文字（読みやすい）

// 特殊な数値
let inf = Infinity;        // 無限大
let negInf = -Infinity;    // 負の無限大
let notNum = NaN;          // Not a Number（数値でない）

// NaNの例
console.log(0 / 0);        // NaN
console.log("abc" * 3);    // NaN
```

**なぜ整数と小数の区別がない？🤔**
- JavaScriptの設計思想：シンプルさ優先
- 内部的には全て浮動小数点数
- 他の言語（Java、C）には int、float、doubleなど複数ある

**注意: 浮動小数点の罠** ⚠️
```javascript
console.log(0.1 + 0.2);  // 0.30000000000000004
// !? なぜ？

// これはコンピュータの仕組み上の問題
// 2進数で0.1を正確に表現できない
```

**解決策**:
```javascript
// 整数に変換してから計算
let result = (0.1 * 10 + 0.2 * 10) / 10;
console.log(result);  // 0.3

// または、小数点以下を丸める
let result2 = (0.1 + 0.2).toFixed(1);
console.log(result2);  // "0.3"
```

#### 2. String（文字列）📝

```javascript
// 3種類の書き方
let single = 'シングルクォート';
let double = "ダブルクォート";
let backtick = `バッククォート`;

// どれも同じ意味、好みの問題
```

**テンプレートリテラル（超便利！）**
```javascript
let name = "太郎";
let age = 25;

// 古い書き方
let message1 = "私の名前は" + name + "で、" + age + "歳です";

// 新しい書き方（ES6）
let message2 = `私の名前は${name}で、${age}歳です`;

// 計算もできる
let total = `合計: ${100 + 200}円`;  // 合計: 300円

// 複数行も簡単
let multiLine = `
  1行目
  2行目
  3行目
`;
```

**エスケープシーケンス**
```javascript
let quote = "彼は\"こんにちは\"と言った";  // \"でダブルクォートを表示
let newline = "1行目\n2行目";              // \nで改行
let tab = "項目1\t項目2";                  // \tでタブ
let backslash = "C:\\Users\\Desktop";      // \\でバックスラッシュ
```

#### 3. Boolean（真偽値）✅❌

```javascript
let isAdult = true;
let isStudent = false;

// 比較演算の結果
let result = 5 > 3;  // true
let check = 10 === "10";  // false（型が違う）
```

**真偽値に変換される値（重要！）**
```javascript
// false扱いされる値（Falsy）
Boolean(false)       // false
Boolean(0)           // false
Boolean("")          // false（空文字列）
Boolean(null)        // false
Boolean(undefined)   // false
Boolean(NaN)         // false

// それ以外は全てtrue（Truthy）
Boolean(true)        // true
Boolean(1)           // true
Boolean("hello")     // true
Boolean([])          // true（空配列でもtrue！）
Boolean({})          // true（空オブジェクトでもtrue！）
```

**実用例**:
```javascript
let userName = "";

if (userName) {
  console.log("ユーザー名が入力されています");
} else {
  console.log("ユーザー名を入力してください");
  // 空文字列はfalse扱い
}
```

#### 4. Undefined（未定義）❓

```javascript
let x;
console.log(x);  // undefined

let obj = { name: "太郎" };
console.log(obj.age);  // undefined（存在しないプロパティ）

function test() {
  // returnがない
}
console.log(test());  // undefined
```

**意味**: 「値が設定されていない」

#### 5. Null（空）🕳️

```javascript
let empty = null;
console.log(empty);  // null

// 意図的に「空」を表現
let selectedUser = null;  // ユーザーが選択されていない
```

**undefinedとnullの違い🤔**
- `undefined`: JavaScriptが自動的に設定（意図しない空）
- `null`: プログラマーが明示的に設定（意図的な空）

```javascript
let a;           // undefined（自動）
let b = null;    // null（意図的）
```

#### 6. Symbol（シンボル）🔣

```javascript
// 一意な識別子を作る（高度な使い方）
let id1 = Symbol("id");
let id2 = Symbol("id");

console.log(id1 === id2);  // false（同じ説明でも別物）
```

**初心者は気にしなくてOK！**

#### 7. BigInt（巨大な整数）🔢

```javascript
// 通常のNumberでは扱えない大きな数
let bigNumber = 9007199254740991n;  // 末尾にn
let huge = BigInt("999999999999999999999");

console.log(bigNumber + 1n);  // 計算できる
```

**通常は使わない**（特殊な場合のみ）

### 参照型（オブジェクト型）📦

#### 8. Object（オブジェクト）

```javascript
// オブジェクト: プロパティの集まり
let person = {
  name: "太郎",
  age: 25,
  isStudent: false
};

console.log(person.name);  // "太郎"
console.log(person["age"]);  // 25（別の書き方）
```

**配列もオブジェクト**:
```javascript
let colors = ["red", "green", "blue"];
console.log(typeof colors);  // "object"
```

**関数もオブジェクト**:
```javascript
function greet() {
  console.log("Hello");
}
console.log(typeof greet);  // "function"（でもオブジェクトの一種）
```

### 型の確認 🔍

```javascript
// typeof演算子
console.log(typeof 42);           // "number"
console.log(typeof "hello");      // "string"
console.log(typeof true);         // "boolean"
console.log(typeof undefined);    // "undefined"
console.log(typeof null);         // "object" ← バグ！歴史的理由で修正できない
console.log(typeof {});           // "object"
console.log(typeof []);           // "object"
console.log(typeof function(){}); // "function"
```

**nullのバグ🐛**: 歴史的な理由で`typeof null`が`"object"`を返します。これはJavaScriptの有名なバグですが、互換性のため修正できません。

## 演算子 - Operators ➕➖✖️➗

### 算術演算子 🔢

```javascript
let a = 10;
let b = 3;

console.log(a + b);   // 13（足し算）
console.log(a - b);   // 7（引き算）
console.log(a * b);   // 30（掛け算）
console.log(a / b);   // 3.3333...（割り算）
console.log(a % b);   // 1（剰余、余り）
console.log(a ** b);  // 1000（べき乗、10の3乗）

// インクリメント・デクリメント
let count = 0;
count++;  // count = count + 1 と同じ
count--;  // count = count - 1 と同じ

// 前置と後置の違い
let x = 5;
console.log(x++);  // 5（表示してから+1）
console.log(x);    // 6

let y = 5;
console.log(++y);  // 6（+1してから表示）
```

**%（剰余）の使い道🤔**:
```javascript
// 偶数・奇数の判定
let num = 7;
if (num % 2 === 0) {
  console.log("偶数");
} else {
  console.log("奇数");  // これが実行される
}

// 3の倍数かチェック
if (num % 3 === 0) {
  console.log("3の倍数");
}
```

### 代入演算子 📥

```javascript
let x = 10;

x += 5;   // x = x + 5  →  15
x -= 3;   // x = x - 3  →  12
x *= 2;   // x = x * 2  →  24
x /= 4;   // x = x / 4  →  6
x %= 4;   // x = x % 4  →  2
```

### 比較演算子 ⚖️

```javascript
// 等価演算子（型変換あり）
console.log(5 == "5");   // true（文字列→数値に変換）
console.log(0 == false); // true（false→0に変換）

// 厳密等価演算子（型変換なし、推奨！）
console.log(5 === "5");   // false（型が違う）
console.log(0 === false); // false（型が違う）

// 不等価
console.log(5 != "5");    // false
console.log(5 !== "5");   // true（厳密、推奨！）

// 大小比較
console.log(5 > 3);   // true
console.log(5 < 3);   // false
console.log(5 >= 5);  // true
console.log(5 <= 4);  // false
```

**重要**: 常に`===`と`!==`を使う！`==`と`!=`は予期しない動作をすることがある。

**なぜ2種類あるの？🤔**:
- `==`: 型変換してから比較（緩い、バグの原因）
- `===`: 型も値も完全一致（厳密、安全）

```javascript
// ==の罠
console.log("" == false);  // true !?
console.log("0" == false); // true !?
console.log([] == false);  // true !?

// ===なら明確
console.log("" === false);  // false
console.log("0" === false); // false
console.log([] === false);  // false
```

### 論理演算子 🧠

```javascript
// AND（かつ）
console.log(true && true);    // true
console.log(true && false);   // false
console.log(false && true);   // false
console.log(false && false);  // false

// OR（または）
console.log(true || true);    // true
console.log(true || false);   // true
console.log(false || true);   // true
console.log(false || false);  // false

// NOT（否定）
console.log(!true);   // false
console.log(!false);  // true
console.log(!!true);  // true（2重否定）
```

**実用例**:
```javascript
let age = 20;
let hasLicense = true;

// 年齢が18以上かつ免許を持っている
if (age >= 18 && hasLicense) {
  console.log("運転できます");
}

// 学生または65歳以上
let isStudent = false;
if (isStudent || age >= 65) {
  console.log("割引適用");
}
```

**短絡評価（ショートサーキット）**:
```javascript
// ANDの場合、最初がfalseなら2番目を評価しない
let result = false && console.log("実行されない");

// ORの場合、最初がtrueなら2番目を評価しない
let result2 = true || console.log("実行されない");

// 実用例：デフォルト値の設定
let userName = inputName || "ゲスト";
// inputNameが空文字列なら"ゲスト"が使われる
```

### 三項演算子 🔀

```javascript
// 条件 ? 真の場合 : 偽の場合
let age = 20;
let message = age >= 18 ? "成人" : "未成年";
console.log(message);  // "成人"

// if文と同じ意味
let message2;
if (age >= 18) {
  message2 = "成人";
} else {
  message2 = "未成年";
}
```

**いつ使う？**:
- シンプルな条件分岐（1行で済む）
- 変数への代入

**使わない方がいい場合**:
- 複雑な条件（読みにくくなる）
- 処理が複数行（if文の方が明確）

## 制御構文 - Control Flow 🚦

### if文（もし〜なら）

```javascript
let age = 20;

if (age >= 18) {
  console.log("成人です");
}

// if-else
if (age >= 18) {
  console.log("成人です");
} else {
  console.log("未成年です");
}

// if-else if-else
if (age < 13) {
  console.log("子供");
} else if (age < 18) {
  console.log("ティーンエイジャー");
} else if (age < 65) {
  console.log("大人");
} else {
  console.log("シニア");
}

// ネスト（入れ子）
let hasTicket = true;
if (age >= 18) {
  if (hasTicket) {
    console.log("入場できます");
  } else {
    console.log("チケットが必要です");
  }
}
```

### switch文（場合分け）🔀

```javascript
let day = 3;

switch (day) {
  case 1:
    console.log("月曜日");
    break;
  case 2:
    console.log("火曜日");
    break;
  case 3:
    console.log("水曜日");
    break;
  case 4:
    console.log("木曜日");
    break;
  case 5:
    console.log("金曜日");
    break;
  case 6:
    console.log("土曜日");
    break;
  case 7:
    console.log("日曜日");
    break;
  default:
    console.log("不正な値");
}

// breakを忘れると...
let score = "B";
switch (score) {
  case "A":
    console.log("優秀");
    // breakがない！
  case "B":
    console.log("良好");  // これが実行される
    // breakがない！
  case "C":
    console.log("普通");  // これも実行される！
    break;
}
// 出力: 良好、普通（両方実行される）
```

**breakの重要性🚨**: 忘れると次のcaseも実行される（フォールスルー）

**いつswitch？いつif？**
- 複数の値を比較 → switch
- 範囲や複雑な条件 → if

### ループ - for文 🔄

```javascript
// 基本のfor文
for (let i = 0; i < 5; i++) {
  console.log(i);
}
// 0, 1, 2, 3, 4

// 仕組み
// 1. let i = 0（初期化）
// 2. i < 5?（条件チェック）
// 3. console.log(i)（処理実行）
// 4. i++（更新）
// 5. 2に戻る
```

**練習問題**:
```javascript
// 1から10までの合計
let sum = 0;
for (let i = 1; i <= 10; i++) {
  sum += i;
}
console.log(sum);  // 55

// 九九の表
for (let i = 1; i <= 9; i++) {
  for (let j = 1; j <= 9; j++) {
    console.log(`${i} × ${j} = ${i * j}`);
  }
}
```

### while文 🔁

```javascript
// 条件がtrueの間繰り返す
let count = 0;
while (count < 5) {
  console.log(count);
  count++;
}
// 0, 1, 2, 3, 4

// 無限ループに注意！
// while (true) {
//   console.log("止まらない！");
// }
```

### do-while文 🔂

```javascript
// 最低1回は実行される
let i = 0;
do {
  console.log(i);
  i++;
} while (i < 0);
// 0（条件がfalseでも1回は実行される）

// 通常のwhileとの違い
let j = 0;
while (j < 0) {
  console.log(j);  // 実行されない
  j++;
}
```

### for...of（配列のループ）📚

```javascript
let colors = ["red", "green", "blue"];

// 古い書き方
for (let i = 0; i < colors.length; i++) {
  console.log(colors[i]);
}

// 新しい書き方（ES6、おすすめ）
for (let color of colors) {
  console.log(color);
}
// red, green, blue
```

### for...in（オブジェクトのループ）🔑

```javascript
let person = {
  name: "太郎",
  age: 25,
  city: "東京"
};

for (let key in person) {
  console.log(`${key}: ${person[key]}`);
}
// name: 太郎
// age: 25
// city: 東京
```

### break と continue 🛑

```javascript
// break: ループを抜ける
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break;  // 5になったら終了
  }
  console.log(i);
}
// 0, 1, 2, 3, 4

// continue: 今回の反復をスキップ
for (let i = 0; i < 5; i++) {
  if (i === 2) {
    continue;  // 2の時だけスキップ
  }
  console.log(i);
}
// 0, 1, 3, 4（2がない）
```

## 関数 - Functions 🔧

### 関数宣言 📝

```javascript
// 基本の関数
function greet() {
  console.log("こんにちは！");
}

greet();  // 関数を呼び出す

// 引数あり
function greetUser(name) {
  console.log(`こんにちは、${name}さん！`);
}

greetUser("太郎");  // こんにちは、太郎さん！

// 複数の引数
function add(a, b) {
  return a + b;
}

let result = add(5, 3);
console.log(result);  // 8

// returnがない場合
function sayHello() {
  console.log("Hello");
  // returnがない
}

let value = sayHello();
console.log(value);  // undefined
```

**returnの重要性**:
- `return`で値を返す
- `return`がないと`undefined`を返す
- `return`以降のコードは実行されない

```javascript
function example() {
  console.log("実行される");
  return "終了";
  console.log("実行されない");  // デッドコード
}
```

### デフォルト引数 🎯

```javascript
// ES6以前
function greet(name) {
  name = name || "ゲスト";
  console.log(`こんにちは、${name}さん`);
}

// ES6以降（推奨）
function greet(name = "ゲスト") {
  console.log(`こんにちは、${name}さん`);
}

greet();        // こんにちは、ゲストさん
greet("太郎");  // こんにちは、太郎さん

// 複数のデフォルト引数
function createUser(name, age = 20, country = "日本") {
  return { name, age, country };
}

createUser("太郎");              // { name: "太郎", age: 20, country: "日本" }
createUser("花子", 25);          // { name: "花子", age: 25, country: "日本" }
createUser("John", 30, "USA");  // { name: "John", age: 30, country: "USA" }
```

### 関数式 📋

```javascript
// 関数式
const greet = function(name) {
  return `こんにちは、${name}さん`;
};

console.log(greet("太郎"));

// 関数宣言との違い
sayHello();  // OK（巻き上げがある）
function sayHello() {
  console.log("Hello");
}

sayHi();  // エラー！（巻き上げがない）
const sayHi = function() {
  console.log("Hi");
};
```

**巻き上げ（ホイスティング）🤔**:
- 関数宣言: ファイルの最初に移動される（どこからでも呼べる）
- 関数式: 移動されない（定義前に呼べない）

### アロー関数（超重要！）🏹

```javascript
// 従来の書き方
const add = function(a, b) {
  return a + b;
};

// アロー関数
const add = (a, b) => {
  return a + b;
};

// 1行なら{}とreturnを省略可能
const add = (a, b) => a + b;

// 引数が1つなら()も省略可能
const double = x => x * 2;

// 引数なし
const greet = () => "こんにちは";

// オブジェクトを返す場合は()で囲む
const createUser = (name, age) => ({ name, age });
// const createUser = (name, age) => { name, age };  // エラー！

console.log(add(5, 3));        // 8
console.log(double(7));        // 14
console.log(greet());          // こんにちは
console.log(createUser("太郎", 25));  // { name: "太郎", age: 25 }
```

**いつアロー関数？いつfunction？**
- 通常: アロー関数（簡潔）
- thisを使う場合: function（後述）
- メソッド定義: function

### 即時実行関数式（IIFE）⚡

```javascript
// 定義と同時に実行
(function() {
  console.log("すぐに実行される");
})();

// アロー関数版
(() => {
  console.log("これもすぐ実行");
})();

// 使い道：スコープを作る
(function() {
  let secret = "秘密の値";
  console.log(secret);
})();
console.log(secret);  // エラー！外からはアクセスできない
```

### 高階関数 🎭

関数を引数に取る、または関数を返す関数

```javascript
// 関数を引数に取る
function repeat(n, action) {
  for (let i = 0; i < n; i++) {
    action(i);
  }
}

repeat(3, (i) => {
  console.log(`${i}回目`);
});
// 0回目
// 1回目
// 2回目

// 関数を返す
function multiplier(factor) {
  return (x) => x * factor;
}

const double = multiplier(2);
const triple = multiplier(3);

console.log(double(5));  // 10
console.log(triple(5));  // 15
```

### コールバック関数 📞

```javascript
// タイマー
setTimeout(() => {
  console.log("3秒後に実行");
}, 3000);

// イベントリスナー（後述）
button.addEventListener("click", () => {
  console.log("ボタンがクリックされた");
});

// 配列メソッド
let numbers = [1, 2, 3, 4, 5];
numbers.forEach((num) => {
  console.log(num * 2);
});
// 2, 4, 6, 8, 10
```

## 配列 - Arrays 📚

### 配列の作成と基本操作

```javascript
// 配列の作成
let fruits = ["apple", "banana", "orange"];
let numbers = [1, 2, 3, 4, 5];
let mixed = [1, "two", true, null];  // 混在OK

// アクセス（インデックスは0から）
console.log(fruits[0]);  // "apple"
console.log(fruits[1]);  // "banana"
console.log(fruits[2]);  // "orange"

// 長さ
console.log(fruits.length);  // 3

// 変更
fruits[1] = "grape";
console.log(fruits);  // ["apple", "grape", "orange"]

// 存在しないインデックス
console.log(fruits[10]);  // undefined
```

### 配列の操作メソッド 🛠️

#### 追加・削除

```javascript
let fruits = ["apple", "banana"];

// 末尾に追加
fruits.push("orange");
console.log(fruits);  // ["apple", "banana", "orange"]

// 先頭に追加
fruits.unshift("grape");
console.log(fruits);  // ["grape", "apple", "banana", "orange"]

// 末尾を削除
let last = fruits.pop();
console.log(last);    // "orange"
console.log(fruits);  // ["grape", "apple", "banana"]

// 先頭を削除
let first = fruits.shift();
console.log(first);   // "grape"
console.log(fruits);  // ["apple", "banana"]
```

**図解**:
```
push/pop    →  配列の末尾
unshift/shift  →  配列の先頭

[先頭] ← shift/unshift | push/pop → [末尾]
```

#### splice（途中の要素を操作）

```javascript
let fruits = ["apple", "banana", "orange", "grape"];

// splice(開始位置, 削除数, 追加する要素...)

// 削除のみ
fruits.splice(1, 2);  // インデックス1から2つ削除
console.log(fruits);  // ["apple", "grape"]

// 追加のみ（削除数を0に）
fruits.splice(1, 0, "lemon", "melon");
console.log(fruits);  // ["apple", "lemon", "melon", "grape"]

// 置換（削除して追加）
fruits.splice(1, 2, "cherry");
console.log(fruits);  // ["apple", "cherry", "grape"]
```

#### slice（部分配列を取得）

```javascript
let fruits = ["apple", "banana", "orange", "grape", "melon"];

// slice(開始, 終了) ※終了は含まない
let some = fruits.slice(1, 3);
console.log(some);    // ["banana", "orange"]
console.log(fruits);  // 元の配列は変わらない

// 終了を省略（最後まで）
let from2 = fruits.slice(2);
console.log(from2);   // ["orange", "grape", "melon"]

// 負のインデックス（後ろから）
let last2 = fruits.slice(-2);
console.log(last2);   // ["grape", "melon"]

// コピー
let copy = fruits.slice();
```

### 配列の検索

```javascript
let fruits = ["apple", "banana", "orange", "banana"];

// indexOf: 最初の位置
console.log(fruits.indexOf("banana"));     // 1
console.log(fruits.indexOf("grape"));      // -1（見つからない）

// lastIndexOf: 最後の位置
console.log(fruits.lastIndexOf("banana")); // 3

// includes: 存在チェック（ES7）
console.log(fruits.includes("apple"));     // true
console.log(fruits.includes("grape"));     // false

// find: 条件に合う最初の要素
let numbers = [1, 5, 10, 15, 20];
let found = numbers.find(num => num > 10);
console.log(found);  // 15

// findIndex: 条件に合う最初のインデックス
let index = numbers.findIndex(num => num > 10);
console.log(index);  // 3
```

### 配列の反復処理（超重要！）🔄

#### forEach

```javascript
let fruits = ["apple", "banana", "orange"];

// 各要素に対して処理を実行
fruits.forEach((fruit, index) => {
  console.log(`${index}: ${fruit}`);
});
// 0: apple
// 1: banana
// 2: orange

// forループとの比較
// forループ
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

// forEach（簡潔！）
fruits.forEach(fruit => console.log(fruit));
```

#### map（変換）🗺️

```javascript
let numbers = [1, 2, 3, 4, 5];

// 各要素を2倍に
let doubled = numbers.map(num => num * 2);
console.log(doubled);  // [2, 4, 6, 8, 10]

// 元の配列は変わらない
console.log(numbers);  // [1, 2, 3, 4, 5]

// 実用例：ユーザー名の配列を作る
let users = [
  { name: "太郎", age: 25 },
  { name: "花子", age: 22 },
  { name: "次郎", age: 30 }
];

let names = users.map(user => user.name);
console.log(names);  // ["太郎", "花子", "次郎"]
```

#### filter（フィルタリング）🔍

```javascript
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// 偶数だけ
let evens = numbers.filter(num => num % 2 === 0);
console.log(evens);  // [2, 4, 6, 8, 10]

// 5より大きい
let over5 = numbers.filter(num => num > 5);
console.log(over5);  // [6, 7, 8, 9, 10]

// 実用例：成人だけ抽出
let users = [
  { name: "太郎", age: 25 },
  { name: "花子", age: 17 },
  { name: "次郎", age: 30 }
];

let adults = users.filter(user => user.age >= 18);
console.log(adults);
// [{ name: "太郎", age: 25 }, { name: "次郎", age: 30 }]
```

#### reduce（集約）📊

```javascript
let numbers = [1, 2, 3, 4, 5];

// 合計
let sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum);  // 15

// 仕組み
// 1回目: acc=0, num=1 → 0+1=1
// 2回目: acc=1, num=2 → 1+2=3
// 3回目: acc=3, num=3 → 3+3=6
// 4回目: acc=6, num=4 → 6+4=10
// 5回目: acc=10, num=5 → 10+5=15

// 最大値を見つける
let max = numbers.reduce((acc, num) => Math.max(acc, num));
console.log(max);  // 5

// 実用例：カートの合計金額
let cart = [
  { name: "本", price: 1000 },
  { name: "ペン", price: 200 },
  { name: "ノート", price: 300 }
];

let total = cart.reduce((sum, item) => sum + item.price, 0);
console.log(total);  // 1500
```

#### some / every

```javascript
let numbers = [1, 2, 3, 4, 5];

// some: 1つでも条件を満たすか
let hasEven = numbers.some(num => num % 2 === 0);
console.log(hasEven);  // true（2と4がある）

// every: 全てが条件を満たすか
let allPositive = numbers.every(num => num > 0);
console.log(allPositive);  // true（全て正の数）

let allEven = numbers.every(num => num % 2 === 0);
console.log(allEven);  // false（奇数がある）
```

### 配列の結合と変換

```javascript
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];

// concat: 結合
let combined = arr1.concat(arr2);
console.log(combined);  // [1, 2, 3, 4, 5, 6]

// スプレッド演算子（ES6、推奨）
let combined2 = [...arr1, ...arr2];
console.log(combined2);  // [1, 2, 3, 4, 5, 6]

// join: 文字列に変換
let fruits = ["apple", "banana", "orange"];
let str = fruits.join(", ");
console.log(str);  // "apple, banana, orange"

// split: 文字列から配列に（Stringメソッド）
let text = "apple,banana,orange";
let arr = text.split(",");
console.log(arr);  // ["apple", "banana", "orange"]

// reverse: 逆順（元の配列が変わる！）
let numbers = [1, 2, 3, 4, 5];
numbers.reverse();
console.log(numbers);  // [5, 4, 3, 2, 1]

// sort: ソート（元の配列が変わる！）
let fruits2 = ["orange", "apple", "banana"];
fruits2.sort();
console.log(fruits2);  // ["apple", "banana", "orange"]

// 数値のソート（注意！）
let nums = [1, 10, 2, 20, 3];
nums.sort();
console.log(nums);  // [1, 10, 2, 20, 3] !? 文字列としてソートされる

// 正しい数値ソート
nums.sort((a, b) => a - b);
console.log(nums);  // [1, 2, 3, 10, 20]
```

### 多次元配列

```javascript
// 2次元配列（配列の配列）
let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

console.log(matrix[0][0]);  // 1
console.log(matrix[1][2]);  // 6
console.log(matrix[2][1]);  // 8

// 実用例：座席表
let seats = [
  ["A1", "A2", "A3"],
  ["B1", "B2", "B3"],
  ["C1", "C2", "C3"]
];

// 全ての座席を表示
seats.forEach((row, i) => {
  row.forEach((seat, j) => {
    console.log(`行${i+1}列${j+1}: ${seat}`);
  });
});
```

## オブジェクト - Objects 📦

### オブジェクトの基本

```javascript
// オブジェクトの作成
let person = {
  name: "太郎",
  age: 25,
  isStudent: false,
  greet: function() {
    console.log("こんにちは！");
  }
};

// プロパティへのアクセス（ドット記法）
console.log(person.name);  // "太郎"
console.log(person.age);   // 25

// プロパティへのアクセス（ブラケット記法）
console.log(person["name"]);  // "太郎"

// メソッドの呼び出し
person.greet();  // こんにちは！

// プロパティの追加
person.email = "taro@example.com";
console.log(person.email);  // taro@example.com

// プロパティの削除
delete person.isStudent;
console.log(person.isStudent);  // undefined
```

**ドット記法 vs ブラケット記法🤔**:
```javascript
let obj = {
  name: "太郎",
  "user-age": 25,  // ハイフンを含む
  "full name": "山田太郎"  // スペースを含む
};

// ドット記法
console.log(obj.name);  // OK

// ブラケット記法が必要な場合
console.log(obj["user-age"]);  // ハイフンがある
console.log(obj["full name"]); // スペースがある

// 動的なプロパティアクセス
let key = "name";
console.log(obj[key]);  // "太郎"（変数を使える）
console.log(obj.key);   // undefined（"key"というプロパティを探す）
```

### メソッドの短縮記法（ES6）

```javascript
// 従来の書き方
let person = {
  name: "太郎",
  greet: function() {
    console.log("こんにちは");
  }
};

// 短縮記法（推奨）
let person2 = {
  name: "太郎",
  greet() {
    console.log("こんにちは");
  }
};
```

### thisキーワード

```javascript
let person = {
  name: "太郎",
  age: 25,
  greet() {
    console.log(`私は${this.name}です`);
  },
  introduce() {
    console.log(`${this.name}、${this.age}歳です`);
  }
};

person.greet();      // 私は太郎です
person.introduce();  // 太郎、25歳です

// thisは「このオブジェクト」を指す
```

**thisの罠（アロー関数）⚠️**:
```javascript
let person = {
  name: "太郎",
  // 通常の関数
  greet1() {
    console.log(this.name);  // OK
  },
  // アロー関数
  greet2: () => {
    console.log(this.name);  // undefined！
  }
};

person.greet1();  // 太郎
person.greet2();  // undefined

// アロー関数はthisを持たない
// メソッド定義には通常の関数を使う！
```

### オブジェクトのコピー

```javascript
let original = { name: "太郎", age: 25 };

// シャローコピー（浅いコピー）
let copy1 = Object.assign({}, original);
let copy2 = { ...original };  // スプレッド演算子（推奨）

copy2.name = "花子";
console.log(original.name);  // "太郎"（影響なし）

// ネストしたオブジェクトの問題
let user = {
  name: "太郎",
  address: {
    city: "東京",
    zip: "100-0001"
  }
};

let copy = { ...user };
copy.address.city = "大阪";
console.log(user.address.city);  // "大阪"（元も変わる！）

// ディープコピー（深いコピー）
let deepCopy = JSON.parse(JSON.stringify(user));
deepCopy.address.city = "福岡";
console.log(user.address.city);  // "大阪"（影響なし）
```

### オブジェクトの操作メソッド

```javascript
let person = {
  name: "太郎",
  age: 25,
  city: "東京"
};

// Object.keys(): キーの配列
let keys = Object.keys(person);
console.log(keys);  // ["name", "age", "city"]

// Object.values(): 値の配列
let values = Object.values(person);
console.log(values);  // ["太郎", 25, "東京"]

// Object.entries(): [キー, 値]の配列
let entries = Object.entries(person);
console.log(entries);
// [["name", "太郎"], ["age", 25], ["city", "東京"]]

// ループで使う
for (let [key, value] of Object.entries(person)) {
  console.log(`${key}: ${value}`);
}
// name: 太郎
// age: 25
// city: 東京

// プロパティの存在チェック
console.log("name" in person);     // true
console.log("email" in person);    // false
console.log(person.hasOwnProperty("name"));  // true
```

### 分割代入（Destructuring）💎

```javascript
// オブジェクトの分割代入
let person = { name: "太郎", age: 25, city: "東京" };

// 従来の書き方
let name = person.name;
let age = person.age;

// 分割代入（ES6、推奨）
let { name, age } = person;
console.log(name);  // "太郎"
console.log(age);   // 25

// 別名を付ける
let { name: userName, age: userAge } = person;
console.log(userName);  // "太郎"

// デフォルト値
let { name, age, email = "未設定" } = person;
console.log(email);  // "未設定"

// ネストしたオブジェクト
let user = {
  name: "太郎",
  address: {
    city: "東京",
    zip: "100-0001"
  }
};

let { name, address: { city } } = user;
console.log(city);  // "東京"

// 関数の引数で使う（超便利！）
function displayUser({ name, age }) {
  console.log(`${name}、${age}歳`);
}

displayUser(person);  // 太郎、25歳
```

### 配列の分割代入

```javascript
let colors = ["red", "green", "blue"];

// 従来の書き方
let first = colors[0];
let second = colors[1];

// 分割代入
let [first, second, third] = colors;
console.log(first);   // "red"
console.log(second);  // "green"
console.log(third);   // "blue"

// 一部だけ取得
let [primary, , tertiary] = colors;
console.log(primary);   // "red"
console.log(tertiary);  // "blue"（greenは飛ばす）

// 残りをまとめて取得
let [head, ...rest] = colors;
console.log(head);  // "red"
console.log(rest);  // ["green", "blue"]

// 値の交換（超便利！）
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a);  // 2
console.log(b);  // 1
```

## DOM操作 - Document Object Model 🌐

### DOMとは？

```
Webページ（HTML）
       ↓
   DOMツリー
       ↓
JavaScriptで操作可能
```

```html
<!DOCTYPE html>
<html>
  <head>
    <title>マイページ</title>
  </head>
  <body>
    <h1 id="title">こんにちは</h1>
    <p class="text">これは段落です</p>
    <button id="btn">クリック</button>
  </body>
</html>
```

このHTMLがDOMツリーに変換される：
```
document
  └─ html
      ├─ head
      │   └─ title
      └─ body
          ├─ h1 (id="title")
          ├─ p (class="text")
          └─ button (id="btn")
```

### 要素の取得

```javascript
// IDで取得（1つ）
let title = document.getElementById("title");
console.log(title);  // <h1 id="title">こんにちは</h1>

// クラス名で取得（複数）
let texts = document.getElementsByClassName("text");
console.log(texts);  // HTMLCollection

// タグ名で取得（複数）
let paragraphs = document.getElementsByTagName("p");

// CSSセレクタで取得（1つ、最初のもの）
let firstText = document.querySelector(".text");
let button = document.querySelector("#btn");

// CSSセレクタで取得（複数、全て）
let allTexts = document.querySelectorAll(".text");
console.log(allTexts);  // NodeList

// querySelector vs getElementById
// querySelector: 柔軟（CSSセレクタ）、少し遅い
// getElementById: シンプル、速い
```

**おすすめ**: `querySelector` と `querySelectorAll`（柔軟で統一感がある）

### 要素の内容を変更

```javascript
// テキストの変更
let title = document.querySelector("#title");
title.textContent = "新しいタイトル";
title.innerText = "別の書き方";  // ほぼ同じ

// HTMLの変更（⚠️ XSSに注意）
title.innerHTML = "<strong>太字のタイトル</strong>";

// 属性の取得・設定
let img = document.querySelector("img");
let src = img.getAttribute("src");
img.setAttribute("src", "new-image.jpg");
img.src = "another-way.jpg";  // 直接プロパティ

// クラスの操作
let element = document.querySelector(".box");
element.classList.add("active");      // クラスを追加
element.classList.remove("inactive"); // クラスを削除
element.classList.toggle("visible");  // トグル（あればなし、なければあり）
element.classList.contains("active");// 存在チェック

// スタイルの変更
element.style.color = "red";
element.style.backgroundColor = "yellow";
element.style.fontSize = "20px";

// 複数のスタイルを一度に
element.style.cssText = "color: red; background: yellow; font-size: 20px;";
```

### 要素の作成・追加・削除

```javascript
// 要素の作成
let newDiv = document.createElement("div");
newDiv.textContent = "新しい要素";
newDiv.className = "my-class";

// 要素の追加
let container = document.querySelector("#container");
container.appendChild(newDiv);  // 末尾に追加

// 別の追加方法
let newP = document.createElement("p");
newP.textContent = "別の要素";
container.insertBefore(newP, newDiv);  // newDivの前に挿入

// より柔軟な追加（ES6）
container.insertAdjacentHTML("beforeend", "<p>HTMLを直接挿入</p>");

// 要素の削除
let element = document.querySelector(".remove-me");
element.remove();  // 自分自身を削除（ES6）

// 古い書き方
element.parentNode.removeChild(element);

// 子要素を全削除
container.innerHTML = "";  // 簡単だがイベントも消える
// または
while (container.firstChild) {
  container.removeChild(container.firstChild);
}
```

### イベント処理 🎉

```javascript
// クリックイベント
let button = document.querySelector("#btn");

button.addEventListener("click", function() {
  console.log("ボタンがクリックされた！");
});

// アロー関数で
button.addEventListener("click", () => {
  alert("クリック！");
});

// イベントオブジェクト
button.addEventListener("click", (event) => {
  console.log(event.target);  // クリックされた要素
  console.log(event.type);    // "click"
  console.log(event.clientX); // マウスのX座標
  console.log(event.clientY); // マウスのY座標
});

// 複数のイベント
let input = document.querySelector("#input");

input.addEventListener("focus", () => {
  console.log("フォーカスされた");
});

input.addEventListener("blur", () => {
  console.log("フォーカスが外れた");
});

input.addEventListener("input", (e) => {
  console.log("入力値:", e.target.value);
});

// キーボードイベント
document.addEventListener("keydown", (e) => {
  console.log(`押されたキー: ${e.key}`);
  if (e.key === "Enter") {
    console.log("Enterキーが押された");
  }
});

// マウスイベント
let box = document.querySelector(".box");

box.addEventListener("mouseenter", () => {
  console.log("マウスが入った");
});

box.addEventListener("mouseleave", () => {
  console.log("マウスが出た");
});

// イベントの削除
function handleClick() {
  console.log("クリック");
}

button.addEventListener("click", handleClick);
button.removeEventListener("click", handleClick);

// イベントのデフォルト動作を防ぐ
let link = document.querySelector("a");
link.addEventListener("click", (e) => {
  e.preventDefault();  // リンク遷移を防ぐ
  console.log("リンクはクリックされたけど遷移しない");
});

// イベントの伝播を止める
button.addEventListener("click", (e) => {
  e.stopPropagation();  // 親要素にイベントが伝わらない
  console.log("ボタンのみ反応");
});
```

### 実用例：TODOリスト ✅

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>TODOリスト</title>
</head>
<body>
  <h1>TODOリスト</h1>
  <input type="text" id="todoInput" placeholder="やることを入力">
  <button id="addBtn">追加</button>
  <ul id="todoList"></ul>

  <script>
    const input = document.querySelector("#todoInput");
    const addBtn = document.querySelector("#addBtn");
    const todoList = document.querySelector("#todoList");

    // 追加ボタンをクリック
    addBtn.addEventListener("click", addTodo);

    // Enterキーでも追加
    input.addEventListener("keypress", (e) => {
      if (e.key === "Enter") {
        addTodo();
      }
    });

    function addTodo() {
      const text = input.value.trim();
      
      if (text === "") {
        alert("入力してください");
        return;
      }

      // li要素を作成
      const li = document.createElement("li");
      li.textContent = text;

      // 削除ボタンを作成
      const deleteBtn = document.createElement("button");
      deleteBtn.textContent = "削除";
      deleteBtn.addEventListener("click", () => {
        li.remove();
      });

      // liに削除ボタンを追加
      li.appendChild(deleteBtn);

      // リストに追加
      todoList.appendChild(li);

      // 入力欄をクリア
      input.value = "";
      input.focus();
    }
  </script>
</body>
</html>
```

## 非同期処理 - Asynchronous JavaScript ⏱️

### なぜ非同期処理が必要？🤔

```javascript
// 同期処理（順番に実行）
console.log("1");
console.log("2");
console.log("3");
// 出力: 1, 2, 3（順番通り）

// もし重い処理があったら...
console.log("開始");
// 3秒かかる処理（仮）
for (let i = 0; i < 3000000000; i++) {}
console.log("終了");
// 3秒間、画面が固まる！
```

**問題**:
- サーバーからのデータ取得（数秒かかる）
- ファイルの読み込み
- タイマー処理

これらを待っている間、**ブラウザが固まる**！

**解決策**: 非同期処理

### setTimeout / setInterval ⏰

```javascript
// setTimeout: 指定時間後に1回実行
console.log("開始");

setTimeout(() => {
  console.log("3秒後");
}, 3000);

console.log("終了");

// 出力:
// 開始
// 終了
// 3秒後

// setInterval: 繰り返し実行
let count = 0;
let intervalId = setInterval(() => {
  count++;
  console.log(`${count}秒経過`);
  
  if (count === 5) {
    clearInterval(intervalId);  // 停止
    console.log("タイマー終了");
  }
}, 1000);
```

### コールバック地獄 😱

```javascript
// 順番に処理したい場合（悪い例）
setTimeout(() => {
  console.log("1秒後");
  setTimeout(() => {
    console.log("2秒後");
    setTimeout(() => {
      console.log("3秒後");
      setTimeout(() => {
        console.log("4秒後");
        // ネストが深すぎて読めない！
      }, 1000);
    }, 1000);
  }, 1000);
}, 1000);

// これを「コールバック地獄」と呼ぶ
```

### Promise（約束）🤝

```javascript
// Promiseの基本
let promise = new Promise((resolve, reject) => {
  // 非同期処理
  let success = true;
  
  if (success) {
    resolve("成功！");  // 成功時
  } else {
    reject("失敗...");  // 失敗時
  }
});

// Promiseを使う
promise
  .then((result) => {
    console.log(result);  // "成功！"
  })
  .catch((error) => {
    console.log(error);   // "失敗..."
  });

// 実用例：非同期タイマー
function wait(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

wait(2000)
  .then(() => {
    console.log("2秒待った");
    return wait(1000);
  })
  .then(() => {
    console.log("さらに1秒待った");
  });
```

### async/await（最も読みやすい！）✨

```javascript
// asyncを付けると非同期関数になる
async function example() {
  console.log("開始");
  
  // awaitでPromiseの完了を待つ
  await wait(2000);
  console.log("2秒後");
  
  await wait(1000);
  console.log("さらに1秒後");
}

example();

// エラーハンドリング
async function fetchData() {
  try {
    let response = await fetch("https://api.example.com/data");
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.log("エラー:", error);
  }
}

// 複数の非同期処理を並列実行
async function parallel() {
  console.log("開始");
  
  // 並列実行（同時に開始）
  let [result1, result2, result3] = await Promise.all([
    fetch("url1"),
    fetch("url2"),
    fetch("url3")
  ]);
  
  console.log("全て完了");
}
```

**async/awaitのルール**:
- `async`関数の中でのみ`await`が使える
- `await`は必ずPromiseを返す関数の前に付ける
- `async`関数は自動的にPromiseを返す

### fetch API（データ取得）📡

```javascript
// GETリクエスト
fetch("https://api.example.com/users")
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error("エラー:", error);
  });

// async/await版（推奨）
async function getUsers() {
  try {
    const response = await fetch("https://api.example.com/users");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("エラー:", error);
  }
}

// POSTリクエスト
async function createUser(userData) {
  try {
    const response = await fetch("https://api.example.com/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(userData)
    });
    const data = await response.json();
    console.log("作成成功:", data);
  } catch (error) {
    console.error("エラー:", error);
  }
}

createUser({ name: "太郎", age: 25 });
```

## モダンJavaScript（ES6+）🚀

### let/const（既出）

```javascript
// varは使わない
let mutable = "変更可能";
const immutable = "変更不可";
```

### テンプレートリテラル（既出）

```javascript
const name = "太郎";
const message = `こんにちは、${name}さん`;
```

### アロー関数（既出）

```javascript
const add = (a, b) => a + b;
```

### 分割代入（既出）

```javascript
const { name, age } = person;
const [first, second] = array;
```

### スプレッド演算子 ...

```javascript
// 配列のコピー・結合
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];  // [1, 2, 3, 4, 5]

// オブジェクトのコピー・マージ
const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 };  // { a: 1, b: 2, c: 3 }

// 関数の引数として展開
const numbers = [1, 2, 3, 4, 5];
console.log(Math.max(...numbers));  // 5
```

### レスト引数 ...

```javascript
// 可変長引数
function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3));        // 6
console.log(sum(1, 2, 3, 4, 5));  // 15

// 最初の引数と残り
function example(first, ...rest) {
  console.log("最初:", first);  // 1
  console.log("残り:", rest);    // [2, 3, 4, 5]
}

example(1, 2, 3, 4, 5);
```

### デフォルト引数（既出）

```javascript
function greet(name = "ゲスト") {
  return `こんにちは、${name}さん`;
}
```

### プロパティの短縮記法

```javascript
const name = "太郎";
const age = 25;

// 従来
const person = { name: name, age: age };

// 短縮記法（ES6）
const person2 = { name, age };  // プロパティ名と変数名が同じなら省略可
```

### 計算されたプロパティ名

```javascript
const key = "name";
const person = {
  [key]: "太郎",  // プロパティ名を動的に設定
  [`${key}Upper`]: "TARO"
};

console.log(person.name);       // "太郎"
console.log(person.nameUpper);  // "TARO"
```

### オプショナルチェイニング ?.

```javascript
const user = {
  name: "太郎",
  address: {
    city: "東京"
  }
};

// 従来（エラー対策が必要）
const city = user && user.address && user.address.city;

// オプショナルチェイニング（ES2020）
const city2 = user?.address?.city;  // "東京"
const zip = user?.address?.zip;     // undefined（エラーにならない）

// メソッドの呼び出しにも使える
user.greet?.();  // greetがあれば実行、なければ何もしない
```

### Null合体演算子 ??

```javascript
// 従来（||の問題）
let count = 0;
let value = count || 10;
console.log(value);  // 10（0はfalsyなので10になる）

// Null合体演算子（ES2020）
let value2 = count ?? 10;
console.log(value2);  // 0（0は有効な値として扱われる）

// null/undefinedの時だけデフォルト値
let name = null;
let displayName = name ?? "名無し";  // "名無し"

let age = 0;
let displayAge = age ?? 18;  // 0（0は有効）
```

### クラス 🎓

```javascript
// クラスの定義
class Person {
  // コンストラクタ（初期化）
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  // メソッド
  greet() {
    return `こんにちは、${this.name}です`;
  }

  introduce() {
    return `${this.name}、${this.age}歳です`;
  }

  // getterメソッド
  get info() {
    return `${this.name} (${this.age}歳)`;
  }

  // setterメソッド
  set age(value) {
    if (value < 0) {
      throw new Error("年齢は0以上");
    }
    this._age = value;
  }
}

// インスタンスの作成
const person = new Person("太郎", 25);
console.log(person.greet());      // こんにちは、太郎です
console.log(person.info);         // 太郎 (25歳)

// 継承
class Student extends Person {
  constructor(name, age, grade) {
    super(name, age);  // 親クラスのコンストラクタを呼ぶ
    this.grade = grade;
  }

  // メソッドのオーバーライド
  introduce() {
    return `${super.introduce()}、${this.grade}年生です`;
  }

  study() {
    return `${this.name}は勉強中`;
  }
}

const student = new Student("花子", 20, 2);
console.log(student.introduce());  // 花子、20歳です、2年生です
console.log(student.study());      // 花子は勉強中
```

### モジュール（import/export）📦

**math.js**
```javascript
// 名前付きエクスポート
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

export const PI = 3.14159;
```

**utils.js**
```javascript
// デフォルトエクスポート（1ファイル1つ）
export default function multiply(a, b) {
  return a * b;
}
```

**main.js**
```javascript
// インポート
import { add, subtract, PI } from "./math.js";
import multiply from "./utils.js";

console.log(add(5, 3));       // 8
console.log(subtract(10, 4)); // 6
console.log(PI);              // 3.14159
console.log(multiply(3, 4));  // 12

// 全てをインポート
import * as Math from "./math.js";
console.log(Math.add(1, 2));  // 3

// 別名でインポート
import { add as sum } from "./math.js";
console.log(sum(1, 2));  // 3
```

**HTMLで使用**
```html
<script type="module" src="main.js"></script>
```

## よくあるエラーと解決法 🆘

### 1. Uncaught ReferenceError: X is not defined

```javascript
console.log(userName);  // エラー！userNameが定義されていない
```

**原因**:
- 変数を宣言していない
- タイプミス
- スコープ外

**解決法**:
```javascript
let userName = "太郎";  // 宣言する
console.log(userName);  // OK
```

### 2. Uncaught TypeError: X is not a function

```javascript
let add = 5;
add(3, 2);  // エラー！addは関数じゃない
```

**原因**:
- 関数でないものを関数として呼んでいる
- メソッド名のタイプミス

**解決法**:
```javascript
let add = (a, b) => a + b;  // 関数にする
add(3, 2);  // OK
```

### 3. Uncaught TypeError: Cannot read property 'X' of undefined

```javascript
let user;
console.log(user.name);  // エラー！userがundefined
```

**原因**:
- オブジェクトが`undefined`または`null`
- プロパティが存在しない

**解決法**:
```javascript
let user = { name: "太郎" };
console.log(user.name);  // OK

// またはオプショナルチェイニング
console.log(user?.name);  // undefinedでもエラーにならない
```

### 4. Unexpected token

```javascript
let obj = { name: "太郎" age: 25 };  // エラー！カンマがない
```

**原因**:
- 構文エラー（カンマ、括弧の不一致など）

**解決法**:
```javascript
let obj = { name: "太郎", age: 25 };  // カンマを追加
```

### 5. Cannot access 'X' before initialization

```javascript
console.log(name);  // エラー！
let name = "太郎";
```

**原因**:
- let/constは宣言前に使えない

**解決法**:
```javascript
let name = "太郎";
console.log(name);  // OK
```

## デバッグ方法 🐛

### console.log（基本）

```javascript
let name = "太郎";
console.log("name:", name);  // name: 太郎

let obj = { name: "太郎", age: 25 };
console.log(obj);  // オブジェクト全体を表示

// 複数の値
console.log("name:", name, "age:", 25);

// テーブル表示
let users = [
  { name: "太郎", age: 25 },
  { name: "花子", age: 22 }
];
console.table(users);  // 見やすい表形式
```

### その他のconsoleメソッド

```javascript
console.warn("警告メッセージ");    // 黄色で表示
console.error("エラーメッセージ");  // 赤色で表示

// 時間計測
console.time("処理時間");
// 重い処理
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("処理時間");  // 処理時間: 5.234ms

// グループ化
console.group("ユーザー情報");
console.log("名前: 太郎");
console.log("年齢: 25");
console.groupEnd();
```

### debugger文

```javascript
function calculate(a, b) {
  debugger;  // ここで実行が一時停止
  let result = a + b;
  return result;
}

calculate(5, 3);
// ブラウザのデベロッパーツールが開く
```

### try-catch（エラーハンドリング）

```javascript
try {
  // エラーが起きるかもしれない処理
  let result = riskyOperation();
  console.log(result);
} catch (error) {
  // エラーが起きた時の処理
  console.error("エラーが発生:", error.message);
} finally {
  // 必ず実行される処理
  console.log("処理終了");
}

// 自分でエラーを投げる
function divide(a, b) {
  if (b === 0) {
    throw new Error("0で割ることはできません");
  }
  return a / b;
}

try {
  divide(10, 0);
} catch (error) {
  console.error(error.message);  // 0で割ることはできません
}
```

## 学習ロードマップ 🗺️

### レベル1: 基礎（2週間）🌱

- [ ] 変数（let, const）
- [ ] データ型（string, number, boolean）
- [ ] 演算子
- [ ] if文、ループ
- [ ] 関数の基本
- [ ] 配列とオブジェクトの基本

**目標**: 簡単な計算プログラムが書ける

**練習問題**:
- 九九の表を作る
- FizzBuzz
- 配列の合計・平均を計算

### レベル2: 中級（1ヶ月）🌿

- [ ] アロー関数
- [ ] 配列メソッド（map, filter, reduce）
- [ ] オブジェクトの操作
- [ ] 分割代入
- [ ] DOM操作の基本
- [ ] イベント処理

**目標**: インタラクティブなWebページが作れる

**練習問題**:
- TODOリスト
- カウンター
- じゃんけんゲーム
- 電卓

### レベル3: 上級（2ヶ月）🌳

- [ ] 非同期処理（Promise, async/await）
- [ ] fetch API
- [ ] クラス
- [ ] モジュール
- [ ] エラーハンドリング
- [ ] LocalStorage

**目標**: 本格的なWebアプリが作れる

**練習問題**:
- 天気アプリ（API使用）
- メモアプリ（LocalStorage）
- クイズアプリ
- タイマーアプリ

### レベル4: エキスパート（継続）🚀

- [ ] フレームワーク（React, Vue, Angularなど）
- [ ] Node.js（バックエンド）
- [ ] TypeScript
- [ ] テスト（Jest）
- [ ] ビルドツール（Webpack, Vite）
- [ ] パフォーマンス最適化

## 学習リソース 📚

### 公式ドキュメント
- [MDN Web Docs](https://developer.mozilla.org/ja/) - 最高のリファレンス
- [JavaScript.info](https://ja.javascript.info/) - 詳しいチュートリアル

### オンライン学習
- freeCodeCamp
- Codecademy
- Udemy（有料）

### 書籍
- 「JavaScript本格入門」
- 「りあクト！」（React学習）

### 練習サイト
- LeetCode
- HackerRank
- Codewars

## まとめ 🎓

### JavaScriptの本質

```
JavaScript = Webを動かす言語
           = ブラウザで動く唯一の選択肢
           = フロント・バック・モバイル全てで使える
```

### 学習のコツ 💡

1. **毎日コードを書く**（5分でもOK）
2. **小さなプロジェクトを作る**（教科書だけでは身につかない）
3. **エラーを恐れない**（エラーは友達）
4. **他人のコードを読む**（GitHubなど）
5. **基礎を大切に**（応用は基礎の組み合わせ）

### 次のステップ 🚀

1. **フレームワークを学ぶ**
   - React（最も人気）
   - Vue（初心者に優しい）
   - Angular（大規模向け）

2. **バックエンドも学ぶ**
   - Node.js
   - Express.js

3. **TypeScriptに移行**
   - 型の安全性
   - 大規模開発に必須

### 最後に 🎉

JavaScriptは**最初は簡単、極めるのは難しい**言語です。

でも、**Web開発には絶対に必要**なスキルです。

焦らず、楽しみながら学んでいきましょう！

**Happy Coding! 🚀**

---

## チートシート（印刷用）📄

```javascript
// 変数
let name = "太郎";
const PI = 3.14;

// 関数
const add = (a, b) => a + b;

// 配列
let arr = [1, 2, 3];
arr.push(4);
arr.map(x => x * 2);
arr.filter(x => x > 2);

// オブジェクト
let obj = { name: "太郎", age: 25 };
obj.name;
obj["age"];

// 分割代入
let { name, age } = obj;
let [first, second] = arr;

// DOM
document.querySelector("#id");
element.textContent = "text";
element.addEventListener("click", () => {});

// 非同期
async function fetch() {
  const response = await fetch(url);
  const data = await response.json();
}

// エラーハンドリング
try {
  // code
} catch (error) {
  console.error(error);
}
```
