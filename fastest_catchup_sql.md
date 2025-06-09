# SQL 超入門: 非エンジニア向け最速学習ガイド

このガイドは、全くの非エンジニアでも SQL を『最速』で使い始められるように作成した学習教材です。ブラウザ上で動く SQL エディタを使って、実際に手を動かしながら学んでいきましょう。

## 目次

1. [SQL とは？](#1-sqlとは)
2. [適したバージョン](#2-適したバージョン)
3. [実行環境の準備](#3-実行環境の準備)
4. [基本のデータ取得（SELECT 文）](#4-基本のデータ取得select文)
5. [条件による絞り込み（WHERE 句）](#5-条件による絞り込みwhere句)
6. [データの並べ替え（ORDER BY 句）](#6-データの並べ替えorder-by句)
7. [データのグループ化（GROUP BY 句）](#7-データのグループ化group-by句)
8. [複数テーブルの結合（JOIN）](#8-複数テーブルの結合join)
9. [データの集計関数](#9-データの集計関数)
10. [サブクエリ](#10-サブクエリ)
11. [データの追加・更新・削除](#11-データの追加更新削除)
12. [テーブルの作成と管理](#12-テーブルの作成と管理)
13. [インデックスとパフォーマンス](#13-インデックスとパフォーマンス)
14. [ビューの活用](#14-ビューの活用)
15. [実践的な SQL クエリ](#15-実践的なsqlクエリ)
16. [よくある質問と回答](#16-よくある質問と回答)
17. [次のステップ](#17-次のステップ)

---

## 1. SQL とは？

SQL (Structured Query Language) はデータベースを操作するための言語です。

### SQL の特徴

- **汎用性**: ほとんどのデータベースで使用される標準言語
- **宣言型言語**: 「何をするか」を指定し、「どのように行うか」はデータベースが決定
- **シンプルな文法**: 英語に近い自然な書き方ができる

### なぜ SQL を学ぶべきか

- ビジネスパーソンのデータ分析やレポート作成に最適
- 大量のデータを効率的に処理できる
- Excel では処理できない規模のデータを扱える
- データに基づく意思決定をサポートする強力なツール

---

## 2. 適したバージョン

SQL には複数の「方言」があります。主なものは以下の通りです：

- **MySQL**: オープンソースで人気、Web アプリケーションでよく使われる
- **PostgreSQL**: 高機能で拡張性が高い
- **SQLite**: 軽量で組み込み用途に適している
- **SQL Server**: Microsoft 製、企業向け
- **Oracle Database**: 大企業でよく使われる商用データベース

このガイドでは、標準 SQL に近い書き方を中心に解説します。ほとんどのデータベースで同様に動作します。

> 💡 **初心者向けヒント**：
> 最初は方言の違いを心配する必要はありません。基本的な文法はどのデータベースでもほぼ共通です。

---

## 3. 実行環境の準備

### おすすめ環境

1. **オンライン SQL 実行環境**（初心者向け）: インストール不要ですぐに始められる
2. **ローカルデータベース + GUI**（慣れてきたら）: より本格的な環境

### オンライン SQL 実行環境の使い方

1. ブラウザで [https://sqliteonline.com/](https://sqliteonline.com/) を開く
2. 左側のパネルでサンプルデータベースを選択または作成
3. 右側のエディタに SQL コマンドを入力し、実行ボタン（▶️）を押す

### SQL コマンドの入力と実行

- エディタに SQL コマンドを入力
- 実行ボタンを押すとコマンドが実行される
- 結果は下部のパネルに表示される

![SQLオンラインエディタ](https://i.imgur.com/example.png)

> 💡 **初心者向けヒント**：
> オンライン環境は無料で使えて、インストール不要なのでまずはこちらから始めるのがおすすめです。

---

## 4. 基本のデータ取得（SELECT 文）

データベースからデータを取得する最も基本的なコマンドは `SELECT` です。

### 基本構文

```sql
-- 全てのカラム（列）を取得
SELECT * FROM テーブル名;

-- 特定のカラムのみ取得
SELECT カラム1, カラム2 FROM テーブル名;
```

### 実践例

以下の「従業員」テーブルを例に考えてみましょう：

| id  | name | department | salary |
| --- | ---- | ---------- | ------ |
| 1   | 田中 | 営業       | 350000 |
| 2   | 佐藤 | 技術       | 400000 |
| 3   | 鈴木 | 営業       | 320000 |
| 4   | 高橋 | 人事       | 380000 |

```sql
-- 全ての従業員データを取得
SELECT * FROM employees;

-- 名前と部署だけを取得
SELECT name, department FROM employees;
```

### 別名（エイリアス）の使用

カラム名やテーブル名に別名をつけることができます。

```sql
-- カラムに別名をつける
SELECT
    name AS 氏名,
    department AS 部署,
    salary AS 給与
FROM employees;

-- テーブルに別名をつける
SELECT e.name, e.department
FROM employees AS e;
```

> 💡 **初心者向けヒント**：
> SQL コマンドは大文字でも小文字でも動作します。ただし、可読性のために予約語（SELECT, FROM など）は大文字で書くことが多いです。

---

## 5. 条件による絞り込み（WHERE 句）

WHERE 句を使うと、特定の条件に一致するデータだけを取得できます。

### 基本構文

```sql
SELECT カラム1, カラム2, ...
FROM テーブル名
WHERE 条件;
```

### 条件演算子

```sql
-- 等しい (=)
SELECT * FROM employees WHERE department = '営業';

-- 等しくない (<>, !=)
SELECT * FROM employees WHERE department != '技術';

-- より大きい (>)、より小さい (<)
SELECT * FROM employees WHERE salary > 350000;
SELECT * FROM employees WHERE salary < 400000;

-- 以上 (>=)、以下 (<=)
SELECT * FROM employees WHERE salary >= 350000;
SELECT * FROM employees WHERE salary <= 400000;

-- 複数条件（AND, OR）
SELECT * FROM employees WHERE department = '営業' AND salary >= 330000;
SELECT * FROM employees WHERE department = '営業' OR department = '技術';

-- 範囲指定 (BETWEEN)
SELECT * FROM employees WHERE salary BETWEEN 300000 AND 400000;

-- リスト内の値 (IN)
SELECT * FROM employees WHERE department IN ('営業', '技術');

-- 文字列部分一致 (LIKE)
SELECT * FROM employees WHERE name LIKE '佐%';  -- '佐'で始まる名前
SELECT * FROM employees WHERE name LIKE '%木';  -- '木'で終わる名前
SELECT * FROM employees WHERE name LIKE '%中%'; -- '中'を含む名前

-- NULL値の検索
SELECT * FROM employees WHERE department IS NULL;
SELECT * FROM employees WHERE department IS NOT NULL;
```

> 💡 **初心者向けヒント**：
> LIKE 演算子の「%」は任意の文字列を表すワイルドカードです。「\_」（アンダースコア）を使うと任意の 1 文字を表します。

---

## 6. データの並べ替え（ORDER BY 句）

ORDER BY 句を使うと、特定のカラムでデータを並べ替えることができます。

### 基本構文

```sql
SELECT カラム1, カラム2, ...
FROM テーブル名
ORDER BY カラム名 [ASC|DESC];
```

- ASC: 昇順（小さい値から大きい値へ）- デフォルト
- DESC: 降順（大きい値から小さい値へ）

### 実践例

```sql
-- 給与の高い順に並べ替え
SELECT * FROM employees ORDER BY salary DESC;

-- 部署でグループ化した後、給与の高い順に並べ替え
SELECT * FROM employees ORDER BY department, salary DESC;

-- 名前のアルファベット順に並べ替え
SELECT * FROM employees ORDER BY name ASC;
```

> 💡 **初心者向けヒント**：
> ORDER BY は複数のカラムで指定でき、最初のカラムで同じ値を持つ行は次のカラムで並べ替えられます。

---

## 7. データのグループ化（GROUP BY 句）

GROUP BY 句を使うと、特定のカラムの値でデータをグループ化し、集計できます。

### 基本構文

```sql
SELECT カラム1, 集計関数(カラム2)
FROM テーブル名
GROUP BY カラム1;
```

### 実践例

```sql
-- 部署ごとの平均給与を計算
SELECT
    department,
    AVG(salary) AS 平均給与
FROM employees
GROUP BY department;

-- 部署ごとの従業員数をカウント
SELECT
    department,
    COUNT(*) AS 従業員数
FROM employees
GROUP BY department;

-- 部署と性別でグループ化して平均給与を計算
SELECT
    department,
    gender,
    AVG(salary) AS 平均給与
FROM employees
GROUP BY department, gender;
```

### HAVING によるグループの絞り込み

WHERE はグループ化の前に条件を適用しますが、HAVING はグループ化の後に条件を適用します。

```sql
-- 平均給与が350000より高い部署を取得
SELECT
    department,
    AVG(salary) AS 平均給与
FROM employees
GROUP BY department
HAVING AVG(salary) > 350000;
```

> 💡 **初心者向けヒント**：
> GROUP BY と HAVING は集計関数（SUM, AVG, COUNT など）と一緒に使うことが多いです。

---

## 8. 複数テーブルの結合（JOIN）

JOIN 句を使うと、複数のテーブルを結合して一度に操作できます。

### テーブルの例

従業員テーブル（employees）:

| id  | name | department_id | salary |
| --- | ---- | ------------- | ------ |
| 1   | 田中 | 1             | 350000 |
| 2   | 佐藤 | 2             | 400000 |
| 3   | 鈴木 | 1             | 320000 |
| 4   | 高橋 | 3             | 380000 |

部署テーブル（departments）:

| id  | name | location |
| --- | ---- | -------- |
| 1   | 営業 | 東京     |
| 2   | 技術 | 大阪     |
| 3   | 人事 | 名古屋   |

### 主な JOIN の種類

1. **INNER JOIN**: 両方のテーブルで一致するレコードのみ取得
2. **LEFT JOIN**: 左テーブルの全レコードと、右テーブルの一致するレコード
3. **RIGHT JOIN**: 右テーブルの全レコードと、左テーブルの一致するレコード
4. **FULL JOIN**: 両方のテーブルの全レコード

### 実践例

```sql
-- INNER JOIN: 両方のテーブルに存在する従業員と部署情報を結合
SELECT
    e.name AS 従業員名,
    d.name AS 部署名,
    e.salary AS 給与,
    d.location AS 勤務地
FROM
    employees AS e
INNER JOIN
    departments AS d
ON
    e.department_id = d.id;

-- LEFT JOIN: 部署がない従業員も含めて取得
SELECT
    e.name AS 従業員名,
    d.name AS 部署名
FROM
    employees AS e
LEFT JOIN
    departments AS d
ON
    e.department_id = d.id;

-- 複数テーブルの結合
SELECT
    e.name AS 従業員名,
    d.name AS 部署名,
    p.title AS プロジェクト名
FROM
    employees AS e
JOIN
    departments AS d ON e.department_id = d.id
JOIN
    projects AS p ON e.project_id = p.id;
```

> 💡 **初心者向けヒント**：
> JOIN 操作は最初は混乱しやすいですが、実務では非常によく使います。図で描いてイメージすると理解しやすくなります。

---

## 9. データの集計関数

SQL には様々な集計関数があり、データの分析に役立ちます。

### 主な集計関数

```sql
-- COUNT: レコード数をカウント
SELECT COUNT(*) FROM employees;                      -- 全レコード数
SELECT COUNT(department) FROM employees;             -- NULLでないdepartmentの数
SELECT COUNT(DISTINCT department) FROM employees;    -- 異なるdepartmentの数

-- SUM: 合計を計算
SELECT SUM(salary) FROM employees;                   -- 給与の合計
SELECT SUM(salary) FROM employees WHERE department = '営業';  -- 営業部の給与合計

-- AVG: 平均を計算
SELECT AVG(salary) FROM employees;                   -- 給与の平均
SELECT AVG(salary) FROM employees WHERE gender = '女性';  -- 女性従業員の給与平均

-- MAX/MIN: 最大値/最小値を取得
SELECT MAX(salary) FROM employees;                   -- 最高給与
SELECT MIN(salary) FROM employees;                   -- 最低給与
```

### 集計関数と GROUP BY の組み合わせ

```sql
-- 部署ごとの給与統計
SELECT
    department,
    COUNT(*) AS 従業員数,
    AVG(salary) AS 平均給与,
    MAX(salary) AS 最高給与,
    MIN(salary) AS 最低給与,
    SUM(salary) AS 給与総額
FROM employees
GROUP BY department;
```

> 💡 **初心者向けヒント**：
> 集計関数は NULL 値を無視します（COUNT(\*)を除く）。データに欠損がある場合は注意が必要です。

---

## 10. サブクエリ

サブクエリとは、別の SQL クエリ内に含まれる SQL クエリのことです。複雑な条件や計算を行う際に便利です。

### サブクエリの基本

```sql
-- 平均給与より高い給与をもらっている従業員を取得
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 特定の部署に所属する従業員を取得
SELECT name
FROM employees
WHERE department_id IN (
    SELECT id
    FROM departments
    WHERE location = '東京'
);
```

### 相関サブクエリ

メインクエリの値を参照するサブクエリを相関サブクエリと呼びます。

```sql
-- 各部署の平均給与より高い給与をもらっている従業員を取得
SELECT e1.name, e1.department, e1.salary
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department = e1.department
);
```

> 💡 **初心者向けヒント**：
> サブクエリは強力ですが、複雑になりすぎると可読性と性能が低下することがあります。JOIN や CTE（Common Table Expression）で代替できる場合も多いです。

---

## 11. データの追加・更新・削除

SQL はデータの取得だけでなく、データの追加・更新・削除も行えます。

### データの追加（INSERT）

```sql
-- 基本的なINSERT
INSERT INTO employees (name, department, salary)
VALUES ('山田', '営業', 360000);

-- 複数レコードの一括挿入
INSERT INTO employees (name, department, salary)
VALUES
    ('小林', '技術', 420000),
    ('吉田', '人事', 370000);

-- SELECT結果からのデータ挿入
INSERT INTO employees_backup
SELECT * FROM employees WHERE department = '営業';
```

### データの更新（UPDATE）

```sql
-- 全レコードの更新
UPDATE employees
SET salary = salary * 1.05;  -- 全従業員の給与を5%アップ

-- 条件付き更新
UPDATE employees
SET salary = salary * 1.1
WHERE department = '営業';  -- 営業部のみ10%アップ

-- 複数カラムの更新
UPDATE employees
SET salary = salary * 1.05,
    department = '営業管理'
WHERE department = '営業' AND salary > 400000;
```

### データの削除（DELETE）

```sql
-- 条件付き削除
DELETE FROM employees
WHERE salary < 300000;

-- すべてのデータを削除
DELETE FROM employees;  -- または TRUNCATE TABLE employees;
```

> 💡 **初心者向けヒント**：
> UPDATE や DELETE を実行する前に、同じ WHERE 条件で SELECT を実行して、意図したレコードが対象になっているか確認するのが良い習慣です。

---

## 12. テーブルの作成と管理

### テーブルの作成（CREATE TABLE）

```sql
-- 基本的なテーブル作成
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 0),
    registration_date DATE DEFAULT CURRENT_DATE
);

-- 既存テーブルからテーブルを作成
CREATE TABLE vip_customers AS
SELECT * FROM customers WHERE total_purchase > 1000000;
```

### テーブルの変更（ALTER TABLE）

```sql
-- カラムの追加
ALTER TABLE customers
ADD phone VARCHAR(20);

-- カラムの変更
ALTER TABLE customers
ALTER COLUMN name VARCHAR(150);  -- または MODIFY COLUMN (データベースによって異なる)

-- カラムの削除
ALTER TABLE customers
DROP COLUMN phone;

-- カラム名の変更
ALTER TABLE customers
RENAME COLUMN email TO contact_email;  -- データベースによって構文が異なることがある
```

### テーブルの削除（DROP TABLE）

```sql
-- テーブルの削除
DROP TABLE customers;

-- テーブルが存在する場合のみ削除
DROP TABLE IF EXISTS customers;
```

> 💡 **初心者向けヒント**：
> テーブル設計は重要です。後から変更するのは難しい場合があるので、最初に適切なデータ型と制約を選びましょう。

---

## 13. インデックスとパフォーマンス

インデックスは検索を高速化するための仕組みです。大規模なデータベースでは特に重要です。

### インデックスの作成と削除

```sql
-- 基本的なインデックスの作成
CREATE INDEX idx_employee_name
ON employees (name);

-- 複合インデックスの作成（複数のカラムに対するインデックス）
CREATE INDEX idx_dept_salary
ON employees (department, salary);

-- 一意インデックスの作成（重複を許さない）
CREATE UNIQUE INDEX idx_employee_email
ON employees (email);

-- インデックスの削除
DROP INDEX idx_employee_name;
```

### パフォーマンスのヒント

1. 検索条件でよく使用されるカラムにインデックスを作成する
2. 不要なカラムは SELECT に含めない（特に大きなテキストデータなど）
3. LIKE '%文字列%' のような前方一致でない検索はインデックスを使えない
4. 実行計画（EXPLAIN）を使ってクエリのパフォーマンスを分析する

```sql
-- 実行計画の表示（データベースによって構文が異なる場合がある）
EXPLAIN SELECT * FROM employees WHERE department = '営業';
```

> 💡 **初心者向けヒント**：
> インデックスは検索を高速化しますが、INSERT/UPDATE/DELETE 操作は遅くなります。必要なところだけにインデックスを作成しましょう。

---

## 14. ビューの活用

ビュー（View）は保存されたクエリで、実際のテーブルのように扱えます。複雑なクエリを簡略化できます。

### ビューの作成と使用

```sql
-- ビューの作成
CREATE VIEW employee_details AS
SELECT
    e.id,
    e.name,
    d.name AS department,
    e.salary,
    d.location
FROM
    employees e
JOIN
    departments d ON e.department_id = d.id;

-- ビューの使用（通常のテーブルのように扱える）
SELECT * FROM employee_details WHERE department = '営業';

-- ビューの更新
CREATE OR REPLACE VIEW employee_details AS
SELECT
    e.id,
    e.name,
    d.name AS department,
    e.salary,
    d.location,
    YEAR(CURRENT_DATE) - YEAR(e.birth_date) AS age
FROM
    employees e
JOIN
    departments d ON e.department_id = d.id;

-- ビューの削除
DROP VIEW employee_details;
```

### ビューのメリット

1. 複雑なクエリを簡略化できる
2. セキュリティ管理が容易（特定のカラムだけ公開する）
3. データの一貫性を保つ（同じクエリを複数の場所で使用する場合）

> 💡 **初心者向けヒント**：
> ビューは実際のデータを保存しているわけではなく、クエリの定義だけを保存しています。ビューを参照するたびに元のクエリが実行されます。

---

## 15. 実践的な SQL クエリ

実際のビジネスシーンで使える SQL クエリの例を見てみましょう。

### 例 1: 売上レポート

```sql
-- 月別・製品カテゴリ別の売上集計
SELECT
    EXTRACT(YEAR FROM order_date) AS 年,
    EXTRACT(MONTH FROM order_date) AS 月,
    p.category AS 製品カテゴリ,
    SUM(o.quantity * o.unit_price) AS 売上合計,
    COUNT(DISTINCT o.order_id) AS 注文数,
    COUNT(DISTINCT o.customer_id) AS 顧客数
FROM
    order_items o
JOIN
    products p ON o.product_id = p.id
WHERE
    order_date BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date),
    p.category
ORDER BY
    年, 月, 売上合計 DESC;
```

### 例 2: 顧客セグメンテーション

```sql
-- RFM分析（最新購入日、購入頻度、購入金額）
SELECT
    customer_id,
    MAX(order_date) AS 最新購入日,
    COUNT(DISTINCT order_id) AS 購入回数,
    SUM(total_amount) AS 累計購入金額,
    CASE
        WHEN MAX(order_date) >= CURRENT_DATE - INTERVAL '90 days' THEN 'アクティブ'
        WHEN MAX(order_date) >= CURRENT_DATE - INTERVAL '180 days' THEN '要フォロー'
        ELSE '休眠'
    END AS 顧客ステータス
FROM
    orders
GROUP BY
    customer_id
ORDER BY
    累計購入金額 DESC;
```

### 例 3: 在庫管理レポート

```sql
-- 商品別在庫状況と発注推奨
SELECT
    p.id AS 製品ID,
    p.name AS 製品名,
    p.current_stock AS 現在庫,
    p.minimum_stock AS 最小在庫,
    p.reorder_level AS 発注閾値,
    CASE
        WHEN p.current_stock <= p.reorder_level THEN '発注推奨'
        WHEN p.current_stock <= p.minimum_stock * 1.2 THEN '注意'
        ELSE '適正'
    END AS 在庫状況,
    COALESCE(s.avg_monthly_sales, 0) AS 月平均販売数,
    CASE
        WHEN p.current_stock <= p.reorder_level
        THEN GREATEST(p.minimum_stock * 2 - p.current_stock, 0)
        ELSE 0
    END AS 推奨発注数量
FROM
    products p
LEFT JOIN (
    SELECT
        product_id,
        SUM(quantity) / 3 AS avg_monthly_sales
    FROM
        sales
    WHERE
        sale_date >= CURRENT_DATE - INTERVAL '90 days'
    GROUP BY
        product_id
) s ON p.id = s.product_id
ORDER BY
    在庫状況,
    p.category;
```

> 💡 **初心者向けヒント**：
> 実践的なクエリは複雑に見えますが、基本的な SQL コマンドの組み合わせです。少しずつ理解していきましょう。

---

## 16. よくある質問と回答

### Q1: SQL と Excel の違いは何ですか？

A1: Excel は表計算ソフトで、主に小〜中規模のデータ処理に適しています。SQL はデータベース言語で、大規模なデータセットの操作、複雑なクエリ、複数テーブルの結合に優れています。SQL はプログラムから自動実行できる点も大きな違いです。

### Q2: どのデータベースを選べばいいですか？

A2: 初心者なら、SQLite か MySQL がおすすめです。SQLite は設定不要で手軽に始められ、MySQL は多機能で将来的なスケーリングも可能です。職場や既存システムとの連携がある場合は、既に使われているデータベースを選ぶと良いでしょう。

### Q3: SQL でできることの限界は何ですか？

A3: SQL は優れたデータ検索・操作ツールですが、複雑な計算や条件分岐、繰り返し処理には不向きです。また、グラフなどの視覚化は別のツールと組み合わせる必要があります。

### Q4: パフォーマンスが悪いクエリを改善するには？

A4: インデックスの追加、不要な JOIN やサブクエリの削減、必要なカラムだけを選択する、適切な WHERE 条件を使う、などの方法があります。また、EXPLAIN 文でクエリの実行計画を確認することも重要です。

### Q5: SQL インジェクションとは何ですか？

A5: SQL インジェクションは、悪意のある SQL コードをアプリケーションに挿入して、データベースを不正に操作する攻撃手法です。プリペアドステートメントやパラメータ化クエリを使用することで防ぐことができます。

> 💡 **初心者向けヒント**：
> SQL の学習
