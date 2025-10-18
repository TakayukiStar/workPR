# TypeScript 世界一詳しい初心者ガイド

## TypeScriptとは? 💻

**TypeScript**（タイプスクリプト）は、Microsoftが2012年に開発した**プログラミング言語**です。正確には、JavaScriptに**型システム**を追加した言語です。

### 一言で言うと 🎯

**「JavaScriptに型のチェック機能を付けた言語」**

```
JavaScript       →    TypeScript
自由だけど       →    型でガードレール付き
バグが出やすい   →    バグを事前に防げる
```

## なぜTypeScriptが生まれたの？歴史的背景 📚

### JavaScript誕生（1995年）🌟

JavaScriptは元々**10日間**で作られた言語です（本当です！）

**当時の目的**: 
- Webページに簡単な動きを付ける
- フォームの入力チェック程度

**想定していなかったこと**:
- 大規模なアプリケーション開発
- 何千行、何万行ものコード
- チーム開発

### JavaScriptの問題点 😰

```javascript
// JavaScript: 実行するまでエラーに気づかない
function add(a, b) {
  return a + b;
}

add(5, 3);        // 8 ← OK
add("5", 3);      // "53" ← !? 文字列になった！
add(5);           // NaN ← !? bがundefinedなので計算できない
add(5, 3, 7, 9);  // 8 ← 余分な引数は無視される
```

**問題**:
- 型の間違いを実行するまで検出できない
- 存在しないプロパティにアクセスしても実行時まで分からない
- リファクタリング（コード整理）が怖い
- 大規模開発でバグが増える

### TypeScript登場（2012年）✨

Microsoftのアンダース・ヘルスバーグ（C#の設計者でもある）が開発。

**コンセプト**:
- JavaScriptの自由さを保ちつつ
- 型チェックでバグを防ぐ
- 大規模開発を可能にする

```typescript
// TypeScript: コードを書いている時点でエラーを教えてくれる
function add(a: number, b: number): number {
  return a + b;
}

add(5, 3);        // 8 ← OK
add("5", 3);      // エラー！数値を渡してください
add(5);           // エラー！引数が足りません
add(5, 3, 7, 9);  // エラー！引数が多すぎます
```

## JavaScriptとTypeScriptの関係 🔄

### 重要な関係性

```
┌─────────────────────┐
│   TypeScript        │ ← あなたが書くコード
│ (型付きJavaScript)  │
└──────────┬──────────┘
           │
           │ コンパイル（変換）
           │ tsc コマンド
           ↓
┌─────────────────────┐
│   JavaScript        │ ← ブラウザで実行されるコード
│ (型情報は削除される)│
└─────────────────────┘
           │
           │ 実行
           ↓
    ブラウザ/Node.js
```

**重要ポイント**:
1. TypeScriptは**JavaScriptの上位互換**（JavaScriptのコードはそのままTypeScriptとして使える）
2. TypeScriptは**直接実行できない**（必ずJavaScriptに変換が必要）
3. 型チェックは**開発時のみ**（実行時には型情報は消える）

### なぜこんな仕組み？🤔

**A**: ブラウザはJavaScriptしか理解できないから！

- ブラウザの開発者たち全員が「TypeScriptも実行できるようにしよう」と合意するのは不可能
- 既存のJavaScriptの資産（ライブラリ、フレームワーク）をそのまま使いたい
- だから「TypeScript → JavaScript」に変換する方式を採用

**メリット**:
- どんなブラウザでも動く
- 既存のJavaScriptライブラリが使える
- JavaScriptの知識がそのまま活きる

## TypeScriptを学ぶべき理由 🎯

### ✅ メリット

1. **バグを事前に防げる** 🛡️
   - タイプミス、型の間違いをすぐに発見
   - 実行前にエラーを教えてくれる

2. **コードが読みやすい** 📖
   ```typescript
   // 関数を見ただけで、何を受け取って何を返すか分かる
   function getUserName(id: number): string {
     // ...
   }
   ```

3. **エディタの補完が優秀** 💡
   - VSCodeなどで自動補完が効く
   - 存在しないメソッドを打つと即座に警告

4. **リファクタリングが安全** 🔧
   - 名前変更が一括でできる
   - 影響範囲が分かる

5. **チーム開発に最適** 👥
   - コードの意図が明確
   - ドキュメント代わりになる

6. **就職・転職に有利** 💼
   - 現代のWeb開発では必須スキル
   - React、Angular、Vue.jsなどで採用

### ❌ デメリット（正直に言います）

1. **学習コストがある**
   - JavaScriptに加えて型システムを学ぶ必要

2. **コンパイル（変換）が必要**
   - 書いたコードをすぐ実行できない（1秒もかからないが）

3. **型定義を書く手間**
   - JavaScriptより少しコード量が増える

**でも**: デメリットよりメリットの方が圧倒的に大きいです！

## 環境構築 🛠️

### 最小限の環境構築（5分でできる！）

#### 1. Node.jsのインストール

[https://nodejs.org/](https://nodejs.org/) から最新版をインストール

確認：
```bash
node --version  # v18.0.0 など表示されればOK
```

#### 2. TypeScriptのインストール

```bash
npm install -g typescript
```

確認：
```bash
tsc --version  # Version 5.x.x など表示されればOK
```

**npm（エヌピーエム）って何？🤔**
- Node Package Manager の略
- JavaScriptのライブラリをインストールするツール
- Node.jsをインストールすると自動的に入る

**tsc（ティーエスシー）って何？🤔**
- TypeScript Compiler の略
- TypeScriptをJavaScriptに変換するコマンド

#### 3. 最初のTypeScriptファイルを作る

```bash
# ディレクトリを作成
mkdir typescript-practice
cd typescript-practice

# ファイルを作成（エディタで開く）
code hello.ts  # VS Codeの場合
```

**hello.ts** に以下を書く：
```typescript
function greet(name: string): string {
  return `こんにちは、${name}さん！`;
}

console.log(greet("太郎"));
```

#### 4. コンパイルして実行

```bash
# TypeScriptをJavaScriptに変換
tsc hello.ts

# hello.js が生成される

# 実行
node hello.js
```

出力：
```
こんにちは、太郎さん！
```

### より実践的な環境構築

プロジェクトを作る：
```bash
# package.jsonを作成
npm init -y

# TypeScriptをプロジェクトにインストール
npm install --save-dev typescript

# TypeScriptの設定ファイルを生成
npx tsc --init
```

**tsconfig.json** が生成されます（TypeScriptの設定ファイル）

おすすめの初期設定：
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "outDir": "./dist"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

ディレクトリ構造：
```
typescript-practice/
├── src/           ← TypeScriptファイルを置く
│   └── index.ts
├── dist/          ← コンパイルされたJSファイルが出力される
├── tsconfig.json  ← TypeScriptの設定
└── package.json   ← プロジェクトの情報
```

## 基本の型 - Type Basics 📦

### プリミティブ型（基本的な型）

#### 1. string（文字列） 📝

```typescript
let name: string = "太郎";
let message: string = 'こんにちは';
let template: string = `私の名前は${name}です`;

// エラー例
name = 123;  // エラー！数値は代入できません
```

**なぜstringなの？sは小文字？🤔**
- JavaScriptの`typeof`演算子が`"string"`を返すため
- TypeScriptはJavaScriptの慣習に従っている
- `String`（大文字）は別物（オブジェクト型）

#### 2. number（数値） 🔢

```typescript
let age: number = 25;
let price: number = 3.14;
let hex: number = 0xff;  // 16進数
let binary: number = 0b1010;  // 2進数

// JavaScriptと同じく整数と小数の区別なし
```

**なぜintやfloatがないの？🤔**
- JavaScriptには整数と小数の区別がない
- 全て「number」という1つの型
- 内部的にはIEEE 754倍精度浮動小数点数

#### 3. boolean（真偽値） ✅❌

```typescript
let isActive: boolean = true;
let isCompleted: boolean = false;

// エラー例
isActive = "true";  // エラー！文字列"true"と真偽値trueは別物
isActive = 1;       // エラー！数値1と真偽値trueは別物
```

**なぜ0や1じゃダメ？🤔**
- TypeScriptは厳密な型チェック
- JavaScriptでは`if (1)`がOKだが、TypeScriptでは明示的に`boolean`が必要

#### 4. null と undefined 🕳️

```typescript
let nothing: null = null;
let notDefined: undefined = undefined;

// 実際にはあまり単独では使わない
let maybeNumber: number | null = null;  // 「数値 または null」
```

**nullとundefinedの違いは？🤔**
- `undefined`: 「値が設定されていない」（変数を宣言しただけの状態）
- `null`: 「意図的に空であることを示す」

```javascript
let a;           // undefined（値を設定していない）
let b = null;    // null（意図的に空を代入）
```

### 配列 - Array 📚

```typescript
// 書き方1: Type[]
let numbers: number[] = [1, 2, 3, 4, 5];
let names: string[] = ["太郎", "花子", "次郎"];

// 書き方2: Array<Type>（同じ意味）
let scores: Array<number> = [90, 85, 92];

// 混在はエラー
let mixed: number[] = [1, "two", 3];  // エラー！
```

**なぜ2つの書き方があるの？🤔**
- `number[]`の方がシンプルで読みやすい（おすすめ）
- `Array<number>`はジェネリクスという機能を使っている（後述）
- 好みの問題だが、`number[]`の方が一般的

### オブジェクト - Object 📦

```typescript
// 書き方1: インラインで型定義
let person: { name: string; age: number } = {
  name: "太郎",
  age: 25
};

// 書き方2: 型エイリアス（Type Alias）
type Person = {
  name: string;
  age: number;
};

let taro: Person = {
  name: "太郎",
  age: 25
};

// プロパティが足りない、または余分だとエラー
let hanako: Person = {
  name: "花子"
  // エラー！ageが足りない
};
```

### オプショナルプロパティ（省略可能）🔀

```typescript
type User = {
  name: string;
  age: number;
  email?: string;  // ?を付けると省略可能
};

let user1: User = {
  name: "太郎",
  age: 25
  // emailは省略してもOK
};

let user2: User = {
  name: "花子",
  age: 22,
  email: "hanako@example.com"
  // emailを付けてもOK
};
```

**?（クエスチョンマーク）の意味は？🤔**
- 「このプロパティは無くてもいいよ」という意味
- 型的には`string | undefined`と同じ意味

### any型 - 型チェックを無効化 🚨

```typescript
let anything: any = "文字列";
anything = 123;        // OK
anything = true;       // OK
anything = [];         // OK

// 危険：型チェックが効かない
anything.doSomething();  // 実行時エラーになる可能性
```

**⚠️ 警告**: 
- `any`は型チェックを完全に無効化する
- TypeScriptを使う意味がなくなる
- **なるべく使わない！**

**どうしても使う場合**:
- 外部ライブラリの型定義がない
- 一時的な回避策として

**代替案**: `unknown`型（後述）

## 型推論 - Type Inference 🔮

TypeScriptの**超重要機能**！

```typescript
// 型を書かなくても自動で推論される
let message = "こんにちは";  // 自動的に string 型
let count = 42;              // 自動的に number 型
let isActive = true;         // 自動的に boolean 型

// 推論された型通りに動作
message = "さようなら";  // OK
message = 123;          // エラー！messageはstring型
```

### なぜ型推論があるの？🤔

**理由1: 冗長さの排除**
```typescript
// 型を書くと冗長
let name: string = "太郎";

// 型推論を使うとシンプル
let name = "太郎";  // どうせstring型だと分かる
```

**理由2: JavaScriptからの移行を容易に**
- 既存のJavaScriptコードに少しずつ型を追加できる
- 全部に型を書く必要がない

### 型推論が効かない場合 🤔

```typescript
// 初期値がない場合は推論できない
let value;  // any型になってしまう（危険！）

// 明示的に型を書く
let value: number;  // OK
```

### 関数の戻り値も推論される 🎯

```typescript
function add(a: number, b: number) {
  return a + b;  // 戻り値は自動的に number 型
}

function greet(name: string) {
  return `こんにちは、${name}さん`;  // 自動的に string 型
}
```

**ベストプラクティス**:
- 変数の型は基本的に書かない（推論に任せる）
- 関数の引数の型は必ず書く
- 関数の戻り値の型は書いても書かなくてもOK（チーム規約による）

## ユニオン型 - Union Types 🔀

「AまたはB」を表現する型

```typescript
// 文字列 または 数値
let id: string | number;

id = "abc123";  // OK
id = 123;       // OK
id = true;      // エラー！booleanは許可していない

// 関数の引数でも使える
function printId(id: string | number) {
  console.log(`IDは: ${id}`);
}

printId("abc");  // OK
printId(123);    // OK
```

### 実用例：エラーハンドリング ⚠️

```typescript
type Result = 
  | { success: true; data: string }
  | { success: false; error: string };

function fetchData(): Result {
  if (Math.random() > 0.5) {
    return { success: true, data: "データ取得成功" };
  } else {
    return { success: false, error: "エラーが発生" };
  }
}

const result = fetchData();
if (result.success) {
  console.log(result.data);  // TypeScriptはここでdataがあることを理解
} else {
  console.log(result.error);  // TypeScriptはここでerrorがあることを理解
}
```

**これを型ガード（Type Guard）と呼びます** 🛡️

## インターフェース - Interface 📋

オブジェクトの形を定義する

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  age?: number;  // オプショナル
}

// Userインターフェースに従ったオブジェクト
const user: User = {
  id: 1,
  name: "太郎",
  email: "taro@example.com"
  // ageは省略可能
};

// 関数の引数として使う
function displayUser(user: User) {
  console.log(`${user.name} (${user.email})`);
}
```

### InterfaceとType Aliasの違い 🤔

```typescript
// Interface
interface Animal {
  name: string;
}

// Type Alias
type Animal = {
  name: string;
};
```

**どちらを使うべき？**

両方ほぼ同じですが、微妙な違い：

| 特徴 | Interface | Type Alias |
|------|-----------|------------|
| オブジェクト定義 | ✅ 得意 | ✅ できる |
| ユニオン型 | ❌ できない | ✅ できる |
| 拡張 | extends で拡張可能 | & で結合可能 |
| 同名で宣言 | マージされる | エラー |

**おすすめ**:
- オブジェクトの形を定義 → `interface`
- ユニオン型など複雑な型 → `type`
- 迷ったら`interface`でOK

### Interfaceの拡張（継承） 🌳

```typescript
interface Person {
  name: string;
  age: number;
}

// Personを拡張してStudentを作る
interface Student extends Person {
  studentId: string;
  grade: number;
}

const student: Student = {
  name: "太郎",
  age: 20,
  studentId: "S12345",
  grade: 2
};
```

## 関数の型付け - Function Types 🔧

### 基本の関数

```typescript
// 引数と戻り値に型を付ける
function add(a: number, b: number): number {
  return a + b;
}

// アロー関数でも同じ
const multiply = (a: number, b: number): number => {
  return a * b;
};

// 省略形
const subtract = (a: number, b: number): number => a - b;
```

### オプショナル引数 🔀

```typescript
function greet(name: string, greeting?: string): string {
  if (greeting) {
    return `${greeting}、${name}さん`;
  }
  return `こんにちは、${name}さん`;
}

greet("太郎");              // "こんにちは、太郎さん"
greet("太郎", "おはよう");  // "おはよう、太郎さん"
```

### デフォルト引数 🎯

```typescript
function createUser(name: string, age: number = 20): User {
  return { name, age };
}

createUser("太郎");      // age は 20 になる
createUser("花子", 25);  // age は 25 になる
```

### void型 - 戻り値なし 🚫

```typescript
function logMessage(message: string): void {
  console.log(message);
  // return文がない、またはreturnだけ
}

// エラー例
function wrong(): void {
  return "something";  // エラー！void型なのに値を返している
}
```

**なぜvoid？🤔**
- 「空虚な、何もない」という意味
- C言語など他の言語でも使われている用語
- 「戻り値を使わない関数」を明示

### never型 - 決して返らない 🔚

```typescript
// エラーを投げる関数（正常終了しない）
function throwError(message: string): never {
  throw new Error(message);
}

// 無限ループ（終わらない）
function infiniteLoop(): never {
  while (true) {
    // ...
  }
}
```

**voidとneverの違いは？🤔**
- `void`: 戻り値がない（でも関数は終了する）
- `never`: 関数が終了しない（エラーまたは無限ループ）

### 関数型を定義 📝

```typescript
// 関数の型を定義
type MathOperation = (a: number, b: number) => number;

const add: MathOperation = (a, b) => a + b;
const subtract: MathOperation = (a, b) => a - b;
const multiply: MathOperation = (a, b) => a * b;

// 関数を引数として受け取る（高階関数）
function calculate(
  a: number, 
  b: number, 
  operation: MathOperation
): number {
  return operation(a, b);
}

calculate(10, 5, add);       // 15
calculate(10, 5, subtract);  // 5
calculate(10, 5, multiply);  // 50
```

## ジェネリクス - Generics 🎁

**最も強力で、最も難しい機能の1つ**

### なぜジェネリクスが必要？🤔

問題：配列の最初の要素を返す関数を作りたい

```typescript
// 文字列配列用
function firstString(arr: string[]): string {
  return arr[0];
}

// 数値配列用
function firstNumber(arr: number[]): number {
  return arr[0];
}

// ...型ごとに関数を作る必要がある！😱
```

**解決策：ジェネリクス**

```typescript
// Tは「型の変数」（Type Variable）
function first<T>(arr: T[]): T {
  return arr[0];
}

// 使用時に型が決まる
const num = first([1, 2, 3]);        // T = number
const str = first(["a", "b", "c"]);  // T = string
const bool = first([true, false]);   // T = boolean
```

### ジェネリクスの仕組み 🔍

```
1. 関数を呼ぶ
   first([1, 2, 3])
   
2. TypeScriptが型を推論
   「配列の中身はnumberだな」
   → T = number
   
3. 関数内のTがすべてnumberに置き換わる
   function first<number>(arr: number[]): number {
     return arr[0];
   }
```

**まるで型の関数！**
- 普通の関数: 値を受け取って値を返す
- ジェネリクス: 型を受け取って型を返す

### 実用例：レスポンス型 📡

```typescript
interface ApiResponse<T> {
  success: boolean;
  data: T;
  error?: string;
}

// ユーザー情報のレスポンス
type UserResponse = ApiResponse<User>;
// 展開すると：
// {
//   success: boolean;
//   data: User;
//   error?: string;
// }

// 商品一覧のレスポンス
type ProductListResponse = ApiResponse<Product[]>;
```

### 複数の型パラメータ 🎭

```typescript
function pair<T, U>(first: T, second: U): [T, U] {
  return [first, second];
}

const p1 = pair("name", 25);        // [string, number]
const p2 = pair(true, "success");   // [boolean, string]
```

**T, U, K, V...って何？🤔**
- 型パラメータの慣習的な名前
- T = Type
- U = 2番目の型（Type の次の文字）
- K = Key（キー）
- V = Value（値）
- 好きな名前を付けてOKだが、大文字1文字が一般的

### 制約付きジェネリクス 🚧

```typescript
// Tは「nameプロパティを持つ型」に限定
function printName<T extends { name: string }>(obj: T): void {
  console.log(obj.name);
}

printName({ name: "太郎", age: 25 });  // OK
printName({ age: 25 });                // エラー！nameがない
```

## よくあるエラーと解決法 🆘

### 1. Type 'X' is not assignable to type 'Y' 😰

```typescript
let num: number = "123";
// エラー: Type 'string' is not assignable to type 'number'
```

**意味**: 「文字列型を数値型に代入できません」

**解決法**:
```typescript
// パターン1: 型を合わせる
let num: number = 123;

// パターン2: 変換する
let num: number = Number("123");  // 文字列→数値に変換

// パターン3: 型を変更する
let num: string = "123";  // そもそも文字列として扱う
```

### 2. Object is possibly 'undefined' 😰

```typescript
function findUser(id: number): User | undefined {
  // ユーザーが見つからない場合はundefinedを返す
  return undefined;
}

const user = findUser(1);
console.log(user.name);  // エラー！userがundefinedかもしれない
```

**解決法1: if文でチェック**
```typescript
const user = findUser(1);
if (user) {
  console.log(user.name);  // OK
}
```

**解決法2: オプショナルチェイニング（?.）**
```typescript
const user = findUser(1);
console.log(user?.name);  // userがundefinedなら全体もundefinedになる
```

**解決法3: Null合体演算子（??）**
```typescript
const user = findUser(1);
const name = user?.name ?? "名無し";  // undefinedなら"名無し"
```

### 3. Property 'X' does not exist on type 'Y' 😰

```typescript
interface User {
  name: string;
  age: number;
}

const user: User = { name: "太郎", age: 25 };
console.log(user.email);  // エラー！emailプロパティは存在しない
```

**原因**:
- タイプミス
- インターフェース定義に含めるのを忘れた

**解決法**:
```typescript
// パターン1: インターフェースに追加
interface User {
  name: string;
  age: number;
  email?: string;  // 追加
}

// パターン2: 正しいプロパティ名を使う
console.log(user.name);  // OK
```

### 4. 'X' is declared but its value is never read 😰

```typescript
function calculate(a: number, b: number): number {
  const result = a + b;
  return a + b;  // resultを使っていない
}
```

**解決法**:
```typescript
function calculate(a: number, b: number): number {
  const result = a + b;
  return result;  // resultを使う
}

// または、変数を作らない
function calculate(a: number, b: number): number {
  return a + b;  // シンプル
}
```

### 5. Cannot find name 'X' 😰

```typescript
console.log(message);  // エラー！messageが定義されていない
```

**原因**:
- 変数の宣言を忘れた
- スコープが違う
- インポートを忘れた

**解決法**:
```typescript
const message = "Hello";
console.log(message);  // OK
```

## 型アサーション - Type Assertion 🎯

「この値の型は私が保証する」という宣言

```typescript
// HTMLElementは抽象的すぎる
const input = document.getElementById("username");
input.value = "太郎";  // エラー！HTMLElementにはvalueプロパティがない

// 型アサーション：「これはHTMLInputElementだ」と明示
const input = document.getElementById("username") as HTMLInputElement;
input.value = "太郎";  // OK
```

**⚠️ 警告**:
- 型アサーションは「TypeScriptに嘘をつく」行為
- 実行時エラーの可能性がある
- 確信がある場合のみ使う

### asとangle-bracket構文 🔀

```typescript
// 書き方1: as（推奨）
const input = document.getElementById("username") as HTMLInputElement;

// 書き方2: <> （JSXと紛らわしいので非推奨）
const input = <HTMLInputElement>document.getElementById("username");
```

**Reactを使う場合は必ずasを使う！**（JSXと混同するため）

### const アサーション 🔒

```typescript
// 通常
const colors = ["red", "green", "blue"];
// 型: string[]（変更可能な文字列配列）

// const アサーション
const colors = ["red", "green", "blue"] as const;
// 型: readonly ["red", "green", "blue"]（変更不可、具体的な値）

colors[0] = "yellow";  // エラー！読み取り専用
```

**使い所**:
- 定数として扱いたい配列・オブジェクト
- より厳密な型チェックが欲しい時

## unknown型 - 安全なany ✅

```typescript
let value: unknown;

value = "文字列";  // OK
value = 123;       // OK
value = true;      // OK

// でも、使う前にチェックが必要
console.log(value.toUpperCase());  // エラー！valueの型が不明

// 型ガードでチェック
if (typeof value === "string") {
  console.log(value.toUpperCase());  // OK
}
```

**anyとunknownの違い**:
- `any`: 何でもOK、型チェックなし（危険）
- `unknown`: 何でも入るが、使う前にチェックが必要（安全）

**ベストプラクティス**: `any`の代わりに`unknown`を使う！

## 列挙型 - Enum 🎨

定数に名前を付けてグループ化

```typescript
enum Direction {
  Up,
  Down,
  Left,
  Right
}

// 使用例
function move(direction: Direction) {
  switch (direction) {
    case Direction.Up:
      console.log("上に移動");
      break;
    case Direction.Down:
      console.log("下に移動");
      break;
    // ...
  }
}

move(Direction.Up);
```

**値は自動で割り当てられる**:
```typescript
enum Direction {
  Up,    // 0
  Down,  // 1
  Left,  // 2
  Right  // 3
}
```

### 文字列Enum（推奨）📝

```typescript
enum Direction {
  Up = "UP",
  Down = "DOWN",
  Left = "LEFT",
  Right = "RIGHT"
}

// デバッグしやすい
console.log(Direction.Up);  // "UP"（数字の0より分かりやすい）
```

### Enumの代替：Union型 🔄

```typescript
// Enumの代わりにUnion型を使う（モダンなアプローチ）
type Direction = "UP" | "DOWN" | "LEFT" | "RIGHT";

function move(direction: Direction) {
  // ...
}

move("UP");  // OK
move("INVALID");  // エラー
```

**どちらを使うべき？**
- Enum: 値が増えない、名前空間が欲しい
- Union型: シンプル、型推論が効く（推奨）

## 実践例：TODO アプリ 📝

全ての知識を使った実用例：

```typescript
// 型定義
type TodoId = number;

interface Todo {
  id: TodoId;
  title: string;
  completed: boolean;
  createdAt: Date;
}

type TodoInput = Omit<Todo, "id" | "createdAt">;

// クラス定義
class TodoManager {
  private todos: Todo[] = [];
  private nextId: TodoId = 1;

  // TODOを追加
  addTodo(input: TodoInput): Todo {
    const todo: Todo = {
      id: this.nextId++,
      title: input.title,
      completed: input.completed,
      createdAt: new Date()
    };
    this.todos.push(todo);
    return todo;
  }

  // TODOを取得
  getTodo(id: TodoId): Todo | undefined {
    return this.todos.find(todo => todo.id === id);
  }

  // 全TODO取得
  getAllTodos(): readonly Todo[] {
    return this.todos;
  }

  // TODOを完了にする
  completeTodo(id: TodoId): boolean {
    const todo = this.getTodo(id);
    if (todo) {
      todo.completed = true;
      return true;
    }
    return false;
  }

  // TODOを削除
  deleteTodo(id: TodoId): boolean {
    const index = this.todos.findIndex(todo => todo.id === id);
    if (index !== -1) {
      this.todos.splice(index, 1);
      return true;
    }
    return false;
  }

  // 完了済みTODOをフィルタ
  getCompletedTodos(): Todo[] {
    return this.todos.filter(todo => todo.completed);
  }

  // 未完了TODOをフィルタ
  getIncompleteTodos(): Todo[] {
    return this.todos.filter(todo => !todo.completed);
  }
}

// 使用例
const manager = new TodoManager();

// 追加
const todo1 = manager.addTodo({
  title: "TypeScriptを学ぶ",
  completed: false
});

const todo2 = manager.addTodo({
  title: "買い物に行く",
  completed: false
});

// 完了にする
manager.completeTodo(todo1.id);

// 一覧表示
console.log("全TODO:", manager.getAllTodos());
console.log("完了済み:", manager.getCompletedTodos());
console.log("未完了:", manager.getIncompleteTodos());
```

**このコードで使っている機能**:
- ✅ Type Alias（`TodoId`）
- ✅ Interface（`Todo`）
- ✅ ユーティリティ型（`Omit`）
- ✅ Class
- ✅ Private修飾子
- ✅ Union型（`Todo | undefined`）
- ✅ 配列メソッドの型推論
- ✅ Readonly型

## ユーティリティ型 - Utility Types 🛠️

TypeScript組み込みの便利な型変換ツール

### Partial<T> - 全プロパティをオプショナルに

```typescript
interface User {
  name: string;
  age: number;
  email: string;
}

// 一部だけ更新したい時
function updateUser(user: User, updates: Partial<User>): User {
  return { ...user, ...updates };
}

const user: User = { name: "太郎", age: 25, email: "taro@example.com" };
updateUser(user, { age: 26 });  // ageだけ更新
```

### Required<T> - 全プロパティを必須に

```typescript
interface Config {
  host?: string;
  port?: number;
  timeout?: number;
}

// すべて必須にする
type RequiredConfig = Required<Config>;
// = { host: string; port: number; timeout: number }
```

### Readonly<T> - 全プロパティを読み取り専用に

```typescript
interface User {
  name: string;
  age: number;
}

const user: Readonly<User> = { name: "太郎", age: 25 };
user.age = 26;  // エラー！読み取り専用
```

### Pick<T, K> - 特定のプロパティだけ選ぶ

```typescript
interface User {
  id: number;
  name: string;
  age: number;
  email: string;
  password: string;
}

// idとnameだけ欲しい
type UserPreview = Pick<User, "id" | "name">;
// = { id: number; name: string }
```

### Omit<T, K> - 特定のプロパティを除外

```typescript
interface User {
  id: number;
  name: string;
  age: number;
  email: string;
  password: string;
}

// passwordを除いたユーザー情報（外部に公開用）
type PublicUser = Omit<User, "password">;
// = { id: number; name: string; age: number; email: string }
```

### Record<K, T> - キーと値の型を指定

```typescript
// キーが文字列、値が数値の辞書
type ScoreMap = Record<string, number>;

const scores: ScoreMap = {
  "太郎": 90,
  "花子": 85,
  "次郎": 92
};

// より具体的に
type UserRole = "admin" | "user" | "guest";
type RolePermissions = Record<UserRole, string[]>;

const permissions: RolePermissions = {
  admin: ["read", "write", "delete"],
  user: ["read", "write"],
  guest: ["read"]
};
```

## strictモード - 厳格な型チェック 🔒

`tsconfig.json`で設定：

```json
{
  "compilerOptions": {
    "strict": true
  }
}
```

**strict: true が有効にする項目**:
- `strictNullChecks`: null/undefinedを厳密にチェック
- `strictFunctionTypes`: 関数の型を厳密に
- `strictBindCallApply`: bind/call/applyを厳密に
- `strictPropertyInitialization`: クラスプロパティの初期化チェック
- など

**推奨**: 新規プロジェクトでは必ず`strict: true`に！

## 学習ロードマップ 🗺️

### レベル1: 基礎（1週間） 🌱

- [ ] TypeScriptとは何か理解
- [ ] 環境構築
- [ ] 基本の型（string, number, boolean, array）
- [ ] 関数の型付け
- [ ] 型推論の理解

**目標**: 簡単な関数に型を付けられる

### レベル2: 中級（2週間） 🌿

- [ ] Interface/Type Alias
- [ ] Union型
- [ ] オプショナルとnull許容
- [ ] ユーティリティ型（Partial, Pick, Omit）
- [ ] 型ガード

**目標**: 実用的なアプリケーションに型を付けられる

### レベル3: 上級（1ヶ月） 🌳

- [ ] ジェネリクス
- [ ] 高度なユーティリティ型
- [ ] Conditional Types
- [ ] Mapped Types
- [ ] デコレータ（experimentalFeatures）

**目標**: 型安全なライブラリを設計できる

### レベル4: エキスパート（3ヶ月〜） 🚀

- [ ] Template Literal Types
- [ ] Intrinsic String Manipulation Types
- [ ] 型レベルプログラミング
- [ ] パフォーマンスチューニング

**目標**: TypeScriptの型システムを自在に操れる

## 実践的なTips 💡

### 1. 型定義ファイル（.d.ts）📄

外部JavaScriptライブラリを使う時：

```bash
# React の型定義をインストール
npm install --save-dev @types/react
```

DefinitelyTyped（@types）から型定義を入手できる

### 2. JSDocコメント 📝

```typescript
/**
 * ユーザー名を取得する
 * @param id - ユーザーID
 * @returns ユーザー名、見つからない場合はundefined
 */
function getUserName(id: number): string | undefined {
  // ...
}
```

VSCodeでホバーすると説明が表示される！

### 3. non-null assertion operator（!）⚠️

```typescript
// 「絶対にnullじゃない」と断言
const element = document.getElementById("app")!;
element.innerHTML = "Hello";

// 危険！elementがnullの場合は実行時エラー
```

**使用は慎重に！** できればif文で チェック

### 4. 型の絞り込み（Narrowing）🔍

```typescript
function processValue(value: string | number) {
  if (typeof value === "string") {
    // この中ではvalueはstring型
    console.log(value.toUpperCase());
  } else {
    // この中ではvalueはnumber型
    console.log(value.toFixed(2));
  }
}
```

TypeScriptが自動で型を絞り込んでくれる！

### 5. 型エイリアスに説明を付ける 📝

```typescript
/** ユーザーID（1以上の整数） */
type UserId = number;

/** メールアドレス（例: user@example.com） */
type Email = string;

// 使う側で説明が表示される
function sendEmail(to: Email, userId: UserId) {
  // ...
}
```

## よくある質問 FAQ ❓

### Q1: TypeScriptは必須？JavaScriptじゃダメ？

**A**: JavaScriptでも開発できますが：
- 小規模プロジェクト → JavaScriptでもOK
- チーム開発、大規模 → TypeScript強く推奨
- 新規プロジェクト → TypeScript一択

### Q2: 学習コストに見合う？

**A**: 絶対に見合います！
- バグが減る → デバッグ時間削減
- リファクタリングが安全 → 保守性向上
- エディタの補完 → 開発速度向上

初期投資（学習時間）は1〜2週間、その後ずっとメリット！

### Q3: 既存のJavaScriptプロジェクトに導入できる？

**A**: できます！段階的に移行可能：
1. `.js` → `.ts` にリネーム（1ファイルずつ）
2. `any`型でいったん動かす
3. 徐々に型を付けていく

### Q4: パフォーマンスは？

**A**: 影響なし！
- 型チェックは開発時のみ
- コンパイル後のJavaScriptは普通のJavaScript
- 実行時のオーバーヘッドゼロ

### Q5: どのエディタがおすすめ？

**A**: **VS Code 一択！**
- TypeScript開発者が同じMicrosoft
- 最高の補完・型チェック
- 無料

## まとめ 🎓

### TypeScriptの本質

```
TypeScript = JavaScript + 型システム
           = バグを減らす仕組み
           = 開発者体験の向上
```

### 覚えておくべきポイント ⭐

1. **型は味方** 🛡️
   - エラーを教えてくれる親切な友達
   - 恐れず、活用する

2. **段階的に学ぶ** 🐢
   - 最初から完璧を目指さない
   - よく使う機能から覚える

3. **型推論を信じる** 🔮
   - 過度に型を書かない
   - TypeScriptに任せる

4. **strictモードON** 🔒
   - 厳格な方が結果的に楽
   - バグを早期発見

5. **公式ドキュメント** 📖
   - [https://www.typescriptlang.org/docs/](https://www.typescriptlang.org/docs/)
   - 最高の学習リソース

### 次のステップ 🚀

1. **小さなプロジェクトで実践**
   - TODO アプリ
   - 計算機
   - 簡単なゲーム

2. **フレームワークと組み合わせ**
   - React + TypeScript
   - Vue + TypeScript
   - Next.js（TypeScript標準）

3. **コードを読む**
   - GitHubのTypeScriptプロジェクト
   - 有名ライブラリのソースコード

4. **型パズルを解く**
   - [Type Challenges](https://github.com/type-challenges/type-challenges)
   - 楽しく学べる！

## 最後に 🎉

TypeScriptは**投資**です。

- 学習時間という投資
- その後ずっとリターンがある
- バグの少ない、保守しやすいコード

最初は難しく感じても、2週間使えば自然になります。
そして気づくでしょう...

**「もうTypeScriptなしでは書けない！」**

頑張ってください！**Happy TypeScripting! 🚀**

---

**チートシート（印刷用）📄**

```typescript
// 基本の型
let str: string = "文字列";
let num: number = 123;
let bool: boolean = true;
let arr: number[] = [1, 2, 3];
let obj: { name: string; age: number } = { name: "太郎", age: 25 };

// Union型
let id: string | number = "abc123";

// 関数
function greet(name: string): string {
  return `Hello, ${name}`;
}

// Interface
interface User {
  name: string;
  age: number;
  email?: string;  // オプショナル
}

// Type Alias
type ID = string | number;

// ジェネリクス
function identity<T>(value: T): T {
  return value;
}

// ユーティリティ型
Partial<T>     // 全プロパティをオプショナルに
Required<T>    // 全プロパティを必須に
Readonly<T>    // 全プロパティを読み取り専用に
Pick<T, K>     // 特定プロパティを選択
Omit<T, K>     // 特定プロパティを除外
Record<K, T>   // キー・値の型を指定

// 型ガード
if (typeof value === "string") { }
if (value !== null) { }
if ("name" in obj) { }

// 型アサーション
const input = document.getElementById("id") as HTMLInputElement;

// オプショナルチェイニング
user?.name?.toUpperCase();

// Null合体演算子
const name = user?.name ?? "名無し";
```
