# 🐼 pandas DataFrame 完全マスター講座：初心者から実践レベルまで

> **対象者**: Python 未経験・エンジニア未経験の社会人  
> **期間**: 6 週間で初中級レベルまで  
> **重点分野**: pandas 基礎と DataFrame 操作（80%）+ 時系列データ基本（20%）

---

## 📋 学習ロードマップ

### 🎯 Week 1: pandas 超基礎 - DataFrame の作成と基本操作

### 🎯 Week 2: データ選択・抽出・フィルタリングの完全攻略

### 🎯 Week 3: データクリーニングと変換の実践

### 🎯 Week 4: 集計・グループ化・データ結合をマスター

### 🎯 Week 5: 時系列データの基本操作

### 🎯 Week 6: 可視化と実践プロジェクト

---

## Week 1: pandas 超基礎 - DataFrame の作成と基本操作

### 🎯 **この週のゴール**

- pandas ライブラリの基本を完全理解する
- DataFrame の構造を理解し、自在に作成できる
- 基本的なデータ操作を身につける

---

### **Day 1-2: pandas の世界へようこそ！**

```python
# pandasとは何か？
print("🐼 pandasの世界へようこそ！")
print("=" * 50)

import pandas as pd
import numpy as np
from datetime import datetime

print("📚 pandasとは？")
print("- Pythonのデータ分析ライブラリ")
print("- 表形式データ（Excel、CSV等）を簡単に扱える")
print("- 「Panel Data」の略")
print("- データサイエンティスト必須のツール")

# なぜpandasが重要なのか？
print("\n🌟 pandasが重要な理由:")
print("✅ Excelよりも高速で大量データを処理")
print("✅ 複雑な計算やデータ変換が簡単")
print("✅ グラフ作成との連携が簡単")
print("✅ 機械学習ライブラリとの相性抜群")

# 最初のDataFrame
print("\n📊 最初のDataFrameを作ってみよう！")

# 辞書からDataFrameを作成
student_data = {
    "名前": ["田中太郎", "佐藤花子", "鈴木次郎", "高橋美咲"],
    "年齢": [20, 22, 21, 23],
    "学年": [2, 4, 3, 4],
    "成績": [85, 92, 78, 88]
}

df = pd.DataFrame(student_data)
print("👨‍🎓 学生データ:")
print(df)

# DataFrameの基本情報を見る
print("\n🔍 DataFrameの基本情報:")
print(f"形状（行数、列数）: {df.shape}")
print(f"行数: {len(df)}")
print(f"列数: {len(df.columns)}")
print(f"列名: {list(df.columns)}")

# データ型を確認
print("\n📋 各列のデータ型:")
print(df.dtypes)

# 基本統計量
print("\n📈 数値列の基本統計量:")
print(df.describe())
```

### **Day 3-4: DataFrame の様々な作成方法**

```python
print("\n🛠️ DataFrameの様々な作成方法")
print("=" * 40)

# 1. 辞書から作成（最も基本）
print("1. 辞書からDataFrame作成")
sales_data = {
    "商品名": ["りんご", "バナナ", "オレンジ", "ぶどう"],
    "価格": [100, 80, 120, 200],
    "在庫": [50, 30, 25, 15]
}
sales_df = pd.DataFrame(sales_data)
print("🍎 商品データ:")
print(sales_df)

# 2. リストのリストから作成
print("\n2. リストのリストから作成")
employee_data = [
    ["田中", "営業", 350000],
    ["佐藤", "開発", 420000],
    ["鈴木", "人事", 380000],
    ["高橋", "営業", 360000]
]
employee_df = pd.DataFrame(employee_data, columns=["名前", "部署", "給与"])
print("👥 従業員データ:")
print(employee_df)

# 3. NumPy配列から作成
print("\n3. NumPy配列から作成")
np.random.seed(42)
random_data = np.random.randint(1, 100, size=(5, 3))
random_df = pd.DataFrame(random_data, columns=["A", "B", "C"])
print("🎲 ランダムデータ:")
print(random_df)

# 4. 空のDataFrameから作成
print("\n4. 空のDataFrameから開始")
empty_df = pd.DataFrame(columns=["日付", "売上", "利益"])
print("📄 空のDataFrame:")
print(empty_df)
print(f"形状: {empty_df.shape}")

# 空のDataFrameにデータを追加
new_row = {"日付": "2024-01-01", "売上": 150000, "利益": 45000}
empty_df = pd.concat([empty_df, pd.DataFrame([new_row])], ignore_index=True)
print("\n📄 データ追加後:")
print(empty_df)

# 5. 範囲データの作成
print("\n5. 連続データの作成")
range_df = pd.DataFrame({
    "番号": range(1, 6),
    "平方": [i**2 for i in range(1, 6)],
    "立方": [i**3 for i in range(1, 6)]
})
print("🔢 連続データ:")
print(range_df)

# 6. 重複データを含むDataFrame
print("\n6. 現実的なデータ（重複あり）")
customer_data = {
    "顧客ID": ["C001", "C002", "C001", "C003", "C002"],
    "商品": ["パン", "牛乳", "卵", "パン", "バター"],
    "金額": [200, 150, 180, 200, 300],
    "購入日": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02", "2024-01-03"]
}
customer_df = pd.DataFrame(customer_data)
print("🛒 顧客購入データ:")
print(customer_df)
```

### **Day 5-7: DataFrame の基本操作**

```python
print("\n🔧 DataFrameの基本操作をマスターしよう")
print("=" * 40)

# サンプルデータの作成
sample_data = {
    "商品名": ["ノートPC", "マウス", "キーボード", "モニター", "スピーカー", "ヘッドセット"],
    "カテゴリ": ["PC", "周辺機器", "周辺機器", "PC", "音響", "音響"],
    "価格": [80000, 2000, 5000, 30000, 15000, 8000],
    "在庫": [5, 50, 30, 8, 12, 20],
    "評価": [4.5, 4.2, 4.0, 4.8, 4.1, 4.3]
}
product_df = pd.DataFrame(sample_data)
print("💻 サンプル商品データ:")
print(product_df)

# 1. データの先頭・末尾を見る
print("\n1. データの先頭・末尾確認")
print("📋 先頭3行:")
print(product_df.head(3))
print("\n📋 末尾2行:")
print(product_df.tail(2))

# 2. インデックスとカラムの操作
print("\n2. インデックスとカラム")
print(f"インデックス: {product_df.index.tolist()}")
print(f"カラム名: {product_df.columns.tolist()}")

# カラム名の変更
product_df_renamed = product_df.copy()
product_df_renamed.columns = ["製品名", "分類", "値段", "個数", "点数"]
print("\n📋 カラム名変更後:")
print(product_df_renamed.head())

# 特定のカラム名だけ変更
product_df_partial = product_df.rename(columns={"商品名": "製品名", "価格": "値段"})
print("\n📋 一部カラム名変更:")
print(product_df_partial.head())

# 3. 新しい列の追加
print("\n3. 新しい列の追加")
# 計算による列追加
product_df["総在庫価値"] = product_df["価格"] * product_df["在庫"]
print("💰 総在庫価値を追加:")
print(product_df[["商品名", "価格", "在庫", "総在庫価値"]])

# 条件による列追加
product_df["価格帯"] = product_df["価格"].apply(
    lambda x: "高価格" if x > 20000 else "中価格" if x > 5000 else "低価格"
)
print("\n🏷️ 価格帯を追加:")
print(product_df[["商品名", "価格", "価格帯"]])

# 4. 行の追加
print("\n4. 行の追加")
new_product = {
    "商品名": "Webカメラ",
    "カテゴリ": "周辺機器",
    "価格": 12000,
    "在庫": 15,
    "評価": 4.4,
    "総在庫価値": 12000 * 15,
    "価格帯": "中価格"
}

# 辞書を一行のDataFrameに変換してから結合
product_df = pd.concat([product_df, pd.DataFrame([new_product])], ignore_index=True)
print("📦 新商品追加後:")
print(product_df.tail(3))

# 5. データの並び替え
print("\n5. データの並び替え")
# 価格の高い順
price_sorted = product_df.sort_values("価格", ascending=False)
print("💰 価格の高い順:")
print(price_sorted[["商品名", "価格"]])

# 複数列での並び替え（カテゴリ→価格）
multi_sorted = product_df.sort_values(["カテゴリ", "価格"], ascending=[True, False])
print("\n📂 カテゴリ別・価格順:")
print(multi_sorted[["商品名", "カテゴリ", "価格"]])

# 6. 基本的な統計操作
print("\n6. 基本統計")
print("📊 数値列の統計:")
print(product_df[["価格", "在庫", "評価"]].describe())

print("\n📈 個別統計:")
print(f"平均価格: {product_df['価格'].mean():,.0f}円")
print(f"最高価格: {product_df['価格'].max():,.0f}円")
print(f"最低価格: {product_df['価格'].min():,.0f}円")
print(f"価格の標準偏差: {product_df['価格'].std():,.0f}円")

# 7. ユニークな値の確認
print("\n7. ユニークな値")
print("🏷️ カテゴリの種類:")
print(product_df["カテゴリ"].unique())
print(f"カテゴリ数: {product_df['カテゴリ'].nunique()}種類")

print("\n📊 カテゴリ別商品数:")
print(product_df["カテゴリ"].value_counts())

# 8. 情報表示
print("\n8. DataFrame情報")
print("ℹ️ DataFrame情報:")
print(product_df.info())

print("\n🔍 欠損値チェック:")
print(product_df.isnull().sum())
```

**🛠 Week 1 の実習課題**

```python
print("\n📝 Week 1 実習課題")
print("=" * 50)

print("🏪 あなたの店舗データを作成しよう！")
print("""
課題: コンビニエンスストアの商品データベースを作成

【要件】
1. 以下の情報を含むDataFrameを作成
   - 商品名（10個以上）
   - カテゴリ（食品、飲料、雑貨、文具など）
   - 価格
   - 在庫数
   - 仕入先

2. 以下の操作を実行
   - 新しい列「利益率」を追加（価格の30%とする）
   - 「在庫金額」列を追加（価格×在庫数）
   - 価格の高い順に並び替え
   - カテゴリ別の商品数を集計
   - 基本統計量を表示

3. ボーナス課題
   - 在庫が10個以下の商品を「要発注」フラグで識別
   - 平均価格より高い商品を「高額商品」として分類
""")

# 解答例のヒント
print("\n💡 解答のヒント:")
print("""
# データ作成例
convenience_data = {
    "商品名": ["おにぎり", "ペットボトル茶", "チョコレート", ...],
    "カテゴリ": ["食品", "飲料", "菓子", ...],
    "価格": [120, 150, 200, ...],
    "在庫数": [30, 50, 15, ...],
    "仕入先": ["A社", "B社", "C社", ...]
}

df = pd.DataFrame(convenience_data)

# 利益率追加
df["利益率"] = df["価格"] * 0.3

# 並び替え
df_sorted = df.sort_values("価格", ascending=False)

# カテゴリ別集計
category_count = df["カテゴリ"].value_counts()
""")

# 実際に作ってみよう
sample_convenience = {
    "商品名": ["おにぎり梅", "お茶500ml", "チョコレート", "ボールペン", "弁当のり",
              "コーヒー缶", "ガム", "ノート", "サンドイッチ", "スポーツドリンク"],
    "カテゴリ": ["食品", "飲料", "菓子", "文具", "食品",
               "飲料", "菓子", "文具", "食品", "飲料"],
    "価格": [120, 150, 200, 100, 180, 130, 80, 150, 350, 180],
    "在庫数": [25, 40, 8, 50, 12, 30, 60, 20, 6, 35],
    "仕入先": ["A社", "B社", "C社", "D社", "A社", "B社", "C社", "D社", "A社", "B社"]
}

sample_df = pd.DataFrame(sample_convenience)
sample_df["利益率"] = sample_df["価格"] * 0.3
sample_df["在庫金額"] = sample_df["価格"] * sample_df["在庫数"]

print("\n📊 サンプル解答:")
print(sample_df)

print("\n📈 カテゴリ別商品数:")
print(sample_df["カテゴリ"].value_counts())

print("\n🏆 チャレンジしてみましょう！")
```

---

## Week 2: データ選択・抽出・フィルタリングの完全攻略

### 🎯 **この週のゴール**

- 列・行の選択方法を完全マスターする
- 条件によるフィルタリングを自在に操る
- 複雑な条件組み合わせができるようになる

---

### **Day 1-2: 列の選択と操作**

```python
print("📊 Week 2: データ選択・抽出・フィルタリング")
print("=" * 50)

import pandas as pd
import numpy as np

# 豊富なサンプルデータを作成
sales_data = {
    "日付": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05",
             "2024-01-06", "2024-01-07", "2024-01-08", "2024-01-09", "2024-01-10"],
    "商品名": ["ノートPC", "マウス", "キーボード", "モニター", "ノートPC",
              "ヘッドセット", "マウス", "キーボード", "モニター", "ヘッドセット"],
    "カテゴリ": ["PC", "周辺機器", "周辺機器", "PC", "PC",
               "音響", "周辺機器", "周辺機器", "PC", "音響"],
    "価格": [85000, 2500, 4800, 32000, 89000, 12000, 2200, 5200, 35000, 8500],
    "数量": [2, 5, 3, 1, 1, 2, 8, 4, 2, 3],
    "売上": [170000, 12500, 14400, 32000, 89000, 24000, 17600, 20800, 70000, 25500],
    "顧客年齢": [28, 45, 35, 52, 31, 26, 38, 29, 48, 33],
    "地域": ["東京", "大阪", "名古屋", "福岡", "東京", "大阪", "名古屋", "福岡", "東京", "大阪"]
}

df = pd.DataFrame(sales_data)
print("🛍️ 販売データ:")
print(df)

print("\n1. 列の選択方法")
print("=" * 30)

# 1つの列を選択
print("📋 1つの列を選択:")
product_names = df["商品名"]
print(product_names)
print(f"データ型: {type(product_names)}")  # Series

# 複数の列を選択
print("\n📋 複数の列を選択:")
basic_info = df[["商品名", "価格", "数量"]]
print(basic_info)
print(f"データ型: {type(basic_info)}")  # DataFrame

# 列を範囲で選択（位置ベース）
print("\n📋 列を範囲で選択:")
range_selection = df.loc[:, "商品名":"売上"]
print(range_selection.head())

# ドット記法での列選択（シンプルな列名の場合）
print("\n📋 ドット記法:")
print("価格の平均:", df.価格.mean())
print("数量の合計:", df.数量.sum())

# 列の存在確認
print("\n🔍 列の存在確認:")
print("'価格'列は存在するか:", "価格" in df.columns)
print("'利益'列は存在するか:", "利益" in df.columns)

# 列名のパターンマッチング
print("\n🔍 列名パターンマッチング:")
# 特定の文字を含む列
category_cols = [col for col in df.columns if "カテ" in col]
print("'カテ'を含む列:", category_cols)

# 数値列のみを選択
numeric_columns = df.select_dtypes(include=[np.number]).columns
print("数値列:", numeric_columns.tolist())

# 文字列列のみを選択
string_columns = df.select_dtypes(include=['object']).columns
print("文字列列:", string_columns.tolist())
```

### **Day 3-4: 行の選択と抽出**

```python
print("\n2. 行の選択方法")
print("=" * 30)

# インデックスによる行選択
print("📋 インデックスによる行選択:")
print("最初の行:")
print(df.iloc[0])

print("\n最初の3行:")
print(df.iloc[0:3])

print("\n最後の2行:")
print(df.iloc[-2:])

# 特定のインデックス
print("\nインデックス1, 3, 5の行:")
print(df.iloc[[1, 3, 5]])

# ラベルによる行選択
print("\n📋 ラベルによる行選択:")
print("インデックス0から4まで:")
print(df.loc[0:4, ["商品名", "価格"]])

# ブール索引による行選択
print("\n📋 条件による行選択:")

# 高額商品（価格50000円以上）
high_price = df[df["価格"] >= 50000]
print("🔥 高額商品:")
print(high_price[["商品名", "価格"]])

# 特定の商品
notebook_sales = df[df["商品名"] == "ノートPC"]
print("\n💻 ノートPCの売上:")
print(notebook_sales[["日付", "価格", "売上"]])

# 東京の売上
tokyo_sales = df[df["地域"] == "東京"]
print("\n🗼 東京の売上:")
print(tokyo_sales[["商品名", "売上"]])

# 複数条件の組み合わせ
print("\n📋 複数条件の組み合わせ:")

# AND条件（&）
tokyo_high = df[(df["地域"] == "東京") & (df["価格"] >= 30000)]
print("🗼💰 東京の高額商品:")
print(tokyo_high[["商品名", "価格", "売上"]])

# OR条件（|）
pc_or_monitor = df[(df["商品名"] == "ノートPC") | (df["商品名"] == "モニター")]
print("\n💻🖥️ PCまたはモニター:")
print(pc_or_monitor[["商品名", "価格"]])

# NOT条件（~）
not_tokyo = df[~(df["地域"] == "東京")]
print("\n🚫🗼 東京以外:")
print(not_tokyo[["地域", "売上"]].groupby("地域").sum())

# isin()メソッドの使用
target_products = ["ノートPC", "モニター", "ヘッドセット"]
target_sales = df[df["商品名"].isin(target_products)]
print("\n🎯 対象商品の売上:")
print(target_sales[["商品名", "売上"]])

# 範囲指定
age_range = df[(df["顧客年齢"] >= 30) & (df["顧客年齢"] <= 40)]
print("\n👥 30-40歳の顧客:")
print(age_range[["顧客年齢", "商品名", "売上"]])
```

### **Day 5-7: 高度なフィルタリングと条件操作**

```python
print("\n3. 高度なフィルタリング")
print("=" * 30)

# query()メソッド（SQLライクな条件指定）
print("📋 query()メソッド:")
query_result = df.query("価格 >= 30000 and 地域 == '東京'")
print("🔍 query()で高額&東京:")
print(query_result[["商品名", "価格", "地域"]])

# 複雑なquery条件
complex_query = df.query("価格 > 価格.mean() and 数量 >= 2")
print("\n🔍 平均価格以上&数量2個以上:")
print(complex_query[["商品名", "価格", "数量"]])

# 文字列メソッドを使った検索
print("\n📋 文字列メソッドでのフィルタリング:")

# 商品名に「ノート」を含む
contains_note = df[df["商品名"].str.contains("ノート")]
print("📔 'ノート'を含む商品:")
print(contains_note[["商品名", "価格"]])

# 商品名が「マ」で始まる
starts_with_ma = df[df["商品名"].str.startswith("マ")]
print("\n📔 'マ'で始まる商品:")
print(starts_with_ma[["商品名", "価格"]])

# 商品名が「ット」で終わる
ends_with_tto = df[df["商品名"].str.endswith("ット")]
print("\n📔 'ット'で終わる商品:")
print(ends_with_tto[["商品名", "価格"]])

# 正規表現を使った検索
import re
pattern_search = df[df["商品名"].str.contains(r"PC|モニター")]
print("\n🔍 正規表現でPC関連商品:")
print(pattern_search[["商品名", "カテゴリ"]])

# 4. null値、欠損値のフィルタリング
print("\n4. null値のフィルタリング")
print("=" * 30)

# 意図的にnull値を作成
df_with_nulls = df.copy()
df_with_nulls.loc[2, "価格"] = np.nan
df_with_nulls.loc[5, "地域"] = np.nan

print("📋 null値を含むデータ:")
print(df_with_nulls[["商品名", "価格", "地域"]])

# null値がある行
has_nulls = df_with_nulls[df_with_nulls.isnull().any(axis=1)]
print("\n❌ null値がある行:")
print(has_nulls)

# null値がない行
no_nulls = df_with_nulls[df_with_nulls.notnull().all(axis=1)]
print("\n✅ null値がない行:")
print(no_nulls[["商品名", "価格", "地域"]])

# 特定列にnull値がない行
price_not_null = df_with_nulls[df_with_nulls["価格"].notnull()]
print("\n💰 価格にnull値がない行:")
print(price_not_null[["商品名", "価格"]])

# 5. 条件に基づく値の更新
print("\n5. 条件に基づく値の更新")
print("=" * 30)

# コピーを作成して操作
df_update = df.copy()

# 条件に基づく値の置換
df_update.loc[df_update["価格"] >= 50000, "価格帯"] = "高額"
df_update.loc[df_update["価格"] < 50000, "価格帯"] = "標準"

print("🏷️ 価格帯を追加:")
print(df_update[["商品名", "価格", "価格帯"]])

# 複数条件での更新
df_update["売上ランク"] = "C"
df_update.loc[df_update["売上"] >= 50000, "売上ランク"] = "A"
df_update.loc[(df_update["売上"] >= 20000) & (df_update["売上"] < 50000), "売上ランク"] = "B"

print("\n🏆 売上ランクを追加:")
print(df_update[["商品名", "売上", "売上ランク"]])

# 6. サンプリング
print("\n6. データのサンプリング")
print("=" * 30)

# ランダムサンプリング
random_sample = df.sample(n=3, random_state=42)
print("🎲 ランダム3行:")
print(random_sample[["商品名", "価格"]])

# 割合でサンプリング
percent_sample = df.sample(frac=0.3, random_state=42)
print(f"\n📊 30%サンプリング ({len(percent_sample)}行):")
print(percent_sample[["商品名", "価格"]])

# 条件ごとのサンプリング
by_category = df.groupby("カテゴリ").apply(lambda x: x.sample(min(len(x), 2), random_state=42))
print("\n📂 カテゴリ別サンプリング:")
print(by_category.reset_index(drop=True)[["カテゴリ", "商品名", "価格"]])
```

**🛠 Week 2 の実習課題**

```python
print("\n📝 Week 2 実習課題")
print("=" * 50)

print("🏢 会社の従業員データ分析")

# 課題用データ
employee_data = {
    "従業員ID": ["E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008", "E009", "E010"],
    "名前": ["田中太郎", "佐藤花子", "鈴木次郎", "高橋美咲", "山田一郎",
           "渡辺美由紀", "中村健太", "小林美香", "加藤大輔", "吉田麻衣"],
    "部署": ["営業", "開発", "営業", "人事", "開発", "営業", "人事", "開発", "営業", "人事"],
    "年齢": [28, 32, 45, 29, 38, 26, 51, 35, 33, 27],
    "給与": [350000, 520000, 480000, 380000, 580000, 320000, 420000, 550000, 410000, 360000],
    "勤続年数": [3, 8, 15, 4, 12, 2, 20, 9, 7, 3],
    "評価": ["B", "A", "A", "B", "A", "C", "B", "A", "B", "B"],
    "地域": ["東京", "大阪", "東京", "名古屋", "大阪", "東京", "名古屋", "大阪", "東京", "名古屋"]
}

emp_df = pd.DataFrame(employee_data)

print("👥 従業員データ:")
print(emp_df)

print("""
📋 実習課題:

【基本課題】
1. 開発部の従業員だけを抽出
2. 年齢が30歳以上の従業員を抽出
3. 給与が400000円以上の従業員を抽出
4. 評価が'A'の従業員を抽出
5. 東京または大阪勤務の従業員を抽出

【応用課題】
6. 営業部で年齢が30歳以下の従業員
7. 勤続年数10年以上かつ評価が'A'または'B'の従業員
8. 給与が全体の平均以上の従業員
9. 名前に'田'が含まれる従業員
10. 各部署で最も給与の高い従業員

【チャレンジ課題】
11. 部署別の平均給与より高い給与をもらっている従業員
12. 年齢層別（20代、30代、40代、50代）の分析
13. 給与ランクの作成（S: 500000以上, A: 400000以上, B: 350000以上, C: それ以下）
""")

print("\n💡 解答例:")

# 基本課題の解答例
print("1. 開発部の従業員:")
dev_employees = emp_df[emp_df["部署"] == "開発"]
print(dev_employees[["名前", "部署", "給与"]])

print("\n6. 営業部で年齢30歳以下:")
young_sales = emp_df[(emp_df["部署"] == "営業") & (emp_df["年齢"] <= 30)]
print(young_sales[["名前", "部署", "年齢"]])

print("\n8. 平均給与以上の従業員:")
avg_salary = emp_df["給与"].mean()
above_avg = emp_df[emp_df["給与"] >= avg_salary]
print(f"平均給与: {avg_salary:,.0f}円")
print(above_avg[["名前", "給与"]])

print("\n🎯 全ての課題にチャレンジしてみましょう！")
```

---

## Week 3: データクリーニングと変換の実践

### 🎯 **この週のゴール**

- 欠損値の処理方法をマスターする
- データの変換・正規化を理解する
- 文字列データの操作を習得する

---

### **Day 1-2: 欠損値の検出と処理**

```python
print("🧹 Week 3: データクリーニングと変換")
print("=" * 50)

import pandas as pd
import numpy as np

print("1. 欠損値の検出と処理")
print("=" * 30)

# 現実的な問題のあるデータを作成
messy_data = {
    "顧客ID": ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010"],
    "名前": ["田中太郎", "佐藤花子", "", "高橋美咲", "山田一郎", None, "中村健太", "小林美香", "加藤大輔", ""],
    "年齢": [28, np.nan, 45, 29, np.nan, 26, 51, 35, 33, 27],
    "職業": ["会社員", "主婦", "会社員", "", "自営業", "学生", "会社員", np.nan, "会社員", "主婦"],
    "年収": [400, 0, 650, 450, np.nan, 200, 700, 520, np.nan, 300],
    "購入金額": [12000, 8500, np.nan, 15000, 22000, 3500, np.nan, 18000, 12500, 9800],
    "会員ランク": ["ゴールド", "シルバー", "ゴールド", "", "プラチナ", "ブロンズ", "ゴールド", "シルバー", "ゴールド", ""]
}

df = pd.DataFrame(messy_data)
print("📋 問題のあるデータ:")
print(df)

# 欠損値の確認
print("\n🔍 欠損値の確認:")
print("各列の欠損値数:")
print(df.isnull().sum())

print("\n欠損値の割合:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage.round(1))

# より詳細な欠損値確認
print("\n📊 詳細な欠損値情報:")
missing_info = pd.DataFrame({
    '欠損数': df.isnull().sum(),
    '欠損率(%)': (df.isnull().sum() / len(df)) * 100,
    'データ型': df.dtypes
})
print(missing_info)

# 欠損値がある行を特定
print("\n❌ 欠損値がある行:")
rows_with_missing = df[df.isnull().any(axis=1)]
print(rows_with_missing)

# 完全なデータがある行
print("\n✅ 完全なデータがある行:")
complete_rows = df[df.notnull().all(axis=1)]
print(complete_rows)

print("\n2. 欠損値の処理方法")
print("=" * 30)

# 処理用のコピーを作成
df_clean = df.copy()

# 方法1: 欠損値のある行を削除
print("方法1: 行削除")
df_drop_rows = df.dropna()
print(f"元データ: {len(df)}行 → 行削除後: {len(df_drop_rows)}行")

# 方法2: 欠損値のある列を削除
print("\n方法2: 列削除")
df_drop_cols = df.dropna(axis=1)
print(f"元データ: {len(df.columns)}列 → 列削除後: {len(df_drop_cols.columns)}列")
print("残った列:", df_drop_cols.columns.tolist())

# 方法3: 特定の列での欠損値削除
print("\n方法3: 特定列での削除")
df_drop_specific = df.dropna(subset=['年齢', '年収'])
print(f"年齢・年収で欠損削除後: {len(df_drop_specific)}行")

# 方法4: 欠損値の置換
print("\n方法4: 欠損値の置換")

# 数値データの欠損値を平均値で置換
df_clean['年齢'].fillna(df_clean['年齢'].mean(), inplace=True)
print("年齢の欠損値を平均値で置換:")
print(f"平均年齢: {df['年齢'].mean():.1f}歳")

# 中央値で置換
df_clean['年収'].fillna(df_clean['年収'].median(), inplace=True)
print(f"年収の欠損値を中央値({df['年収'].median()}万円)で置換")

# 文字列データの欠損値を最頻値で置換
mode_job = df['職業'].mode()[0] if not df['職業'].mode().empty else "不明"
df_clean['職業'].fillna(mode_job, inplace=True)
print(f"職業の欠損値を最頻値('{mode_job}')で置換")

# 固定値で置換
df_clean['会員ランク'].fillna("未設定", inplace=True)
df_clean['名前'].fillna("不明", inplace=True)

print("\n🛠️ クリーニング後のデータ:")
print(df_clean)

# 方法5: 前後の値で補間
print("\n方法5: 補間")
time_series_data = pd.DataFrame({
    '日付': pd.date_range('2024-01-01', periods=10, freq='D'),
    '売上': [100, 120, np.nan, 140, 135, np.nan, 160, 150, np.nan, 180]
})

print("補間前:")
print(time_series_data)

# 線形補間
time_series_data['売上_線形補間'] = time_series_data['売上'].interpolate()

# 前の値で埋める
time_series_data['売上_前埋め'] = time_series_data['売上'].fillna(method='ffill')

# 後の値で埋める
time_series_data['売上_後埋め'] = time_series_data['売上'].fillna(method='bfill')

print("\n補間後:")
print(time_series_data)
```

### **Day 3-4: データ型の変換と正規化**

```python
print("\n3. データ型の変換")
print("=" * 30)

# サンプルデータ
conversion_data = {
    "ID": ["1", "2", "3", "4", "5"],
    "売上": ["100000", "150000", "120000", "180000", "90000"],
    "日付": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "割引率": ["0.1", "0.15", "0.05", "0.2", "0.08"],
    "カテゴリ": ["A", "B", "A", "C", "B"]
}

df_convert = pd.DataFrame(conversion_data)
print("📋 変換前のデータ:")
print(df_convert)
print("\nデータ型:")
print(df_convert.dtypes)

# 文字列を数値に変換
df_convert['ID'] = pd.to_numeric(df_convert['ID'])
df_convert['売上'] = pd.to_numeric(df_convert['売上'])
df_convert['割引率'] = pd.to_numeric(df_convert['割引率'])

# 文字列を日付に変換
df_convert['日付'] = pd.to_datetime(df_convert['日付'])

# カテゴリ型に変換
df_convert['カテゴリ'] = df_convert['カテゴリ'].astype('category')

print("\n📋 変換後のデータ:")
print(df_convert)
print("\nデータ型:")
print(df_convert.dtypes)

# エラーが起きる可能性のある変換
problematic_data = pd.DataFrame({
    "数値": ["100", "200", "abc", "300", "def"]
})

print("\n⚠️ 問題のあるデータ:")
print(problematic_data)

# エラー時の処理方法
# errors='coerce': エラー値をNaNにする
numeric_coerce = pd.to_numeric(problematic_data['数値'], errors='coerce')
print("\nerrors='coerce':")
print(numeric_coerce)

# errors='ignore': エラー時は元のデータを保持
numeric_ignore = pd.to_numeric(problematic_data['数値'], errors='ignore')
print("\nerrors='ignore':")
print(numeric_ignore)

print("\n4. データの正規化・標準化")
print("=" * 30)

# サンプルデータ
normalization_data = {
    "商品": ["A", "B", "C", "D", "E"],
    "価格": [100, 500, 1000, 2000, 5000],
    "売上数": [1000, 800, 500, 200, 50],
    "評価": [4.2, 4.5, 4.8, 4.1, 4.6]
}

df_norm = pd.DataFrame(normalization_data)
print("📊 正規化前:")
print(df_norm)

# Min-Max正規化（0-1の範囲に変換）
df_norm['価格_正規化'] = (df_norm['価格'] - df_norm['価格'].min()) / (df_norm['価格'].max() - df_norm['価格'].min())

# Z-score標準化（平均0、標準偏差1）
df_norm['売上数_標準化'] = (df_norm['売上数'] - df_norm['売上数'].mean()) / df_norm['売上数'].std()

# ランクスコア（順位）
df_norm['評価_ランク'] = df_norm['評価'].rank()

print("\n📊 正規化後:")
print(df_norm)

# SKlearn使用版
from sklearn.preprocessing import MinMaxScaler, StandardScaler

scaler_minmax = MinMaxScaler()
scaler_standard = StandardScaler()

df_norm['価格_sklearn正規化'] = scaler_minmax.fit_transform(df_norm[['価格']])
df_norm['売上数_sklearn標準化'] = scaler_standard.fit_transform(df_norm[['売上数']])

print("\n📊 Sklearn使用版:")
print(df_norm[['価格', '価格_sklearn正規化', '売上数', '売上数_sklearn標準化']])
```

### **Day 5-7: 文字列データの操作と変換**

```python
print("\n5. 文字列データの操作")
print("=" * 30)

# 実際のデータでありそうな文字列問題
text_data = {
    "顧客名": ["  田中太郎  ", "佐藤 花子", "SUZUKI Jiro", "たかはし みさき", "山田　一郎"],
    "電話番号": ["090-1234-5678", "03(1234)5678", "0312345678", "090 1234 5678", ""],
    "メール": ["tanaka@email.com", "SATO@EMAIL.COM", "suzuki@", "takahashi@email", ""],
    "住所": ["東京都新宿区1-2-3", "大阪府大阪市北区４－５－６", "愛知県名古屋市", "", "福岡県福岡市博多区"],
    "商品コード": ["PC-001", "mouse-002", "KB_003", "monitor/004", "SP-005"]
}

df_text = pd.DataFrame(text_data)
print("📝 文字列データ:")
print(df_text)

# 基本的な文字列操作
print("\n🔧 基本的な文字列操作:")

# 前後の空白を削除
df_text['顧客名_trim'] = df_text['顧客名'].str.strip()

# 大文字・小文字変換
df_text['メール_小文字'] = df_text['メール'].str.lower()
df_text['メール_大文字'] = df_text['メール'].str.upper()

# 文字列の長さ
df_text['住所_長さ'] = df_text['住所'].str.len()

print("文字列処理結果:")
print(df_text[['顧客名', '顧客名_trim', 'メール', 'メール_小文字']])

# 文字列の分割
print("\n✂️ 文字列の分割:")
df_text['電話番号_clean'] = df_text['電話番号'].str.replace(r'[()-\s]', '', regex=True)
print("電話番号の正規化:")
print(df_text[['電話番号', '電話番号_clean']])

# 住所の分割
address_split = df_text['住所'].str.split('都|府|県', expand=True)
df_text['都道府県'] = address_split[0] + address_split[1].fillna('')
df_text['市区町村以下'] = address_split[2].fillna('')

print("\n🏠 住所の分割:")
print(df_text[['住所', '都道府県', '市区町村以下']])

# 文字列の置換
print("\n🔄 文字列の置換:")
df_text['商品コード_統一'] = df_text['商品コード'].str.replace(r'[-_/]', '-', regex=True)
print(df_text[['商品コード', '商品コード_統一']])

# パターンマッチング
print("\n🔍 パターンマッチング:")

# メールアドレスの検証
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
df_text['メール_有効'] = df_text['メール'].str.match(email_pattern)

print("メールアドレス検証:")
print(df_text[['メール', 'メール_有効']])

# 電話番号のパターン抽出
phone_pattern = r'(\d{2,4})-?(\d{4})-?(\d{4})'
phone_extract = df_text['電話番号'].str.extract(phone_pattern)
phone_extract.columns = ['市外局番', '局番', '番号']

print("\n📞 電話番号の分解:")
print(phone_extract)

# 文字列の検索
print("\n🔎 文字列の検索:")
tokyo_customers = df_text[df_text['住所'].str.contains('東京', na=False)]
print("東京在住の顧客:")
print(tokyo_customers[['顧客名_trim', '住所']])

# カタカナ・ひらがなの判定
def has_hiragana(text):
    if pd.isna(text):
        return False
    return bool(re.search(r'[ひらがな]', text))

def has_katakana(text):
    if pd.isna(text):
        return False
    return bool(re.search(r'[カタカナ]', text))

import re

df_text['ひらがな含む'] = df_text['顧客名'].apply(has_hiragana)
df_text['カタカナ含む'] = df_text['顧客名'].apply(has_katakana)

print("\n🇯🇵 日本語文字の判定:")
print(df_text[['顧客名', 'ひらがな含む', 'カタカナ含む']])

# 6. データの結合・連結
print("\n6. 文字列の結合")
print("=" * 30)

# 複数列の結合
df_text['フルネーム_住所'] = df_text['顧客名_trim'] + ' (' + df_text['住所'] + ')'

# 条件付き結合
df_text['連絡先'] = df_text['電話番号'].fillna('') + ' / ' + df_text['メール'].fillna('')

print("文字列結合結果:")
print(df_text[['顧客名_trim', '住所', 'フルネーム_住所']])
```

**🛠 Week 3 の実習課題**

```python
print("\n📝 Week 3 実習課題")
print("=" * 50)

print("🏥 病院の患者データクリーニング")

# 課題データ（現実的な問題を含む）
patient_data = {
    "患者ID": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008"],
    "氏名": ["  田中太郎  ", "佐藤花子", "", "高橋美咲", "山田一郎", None, "中村健太", "  小林美香"],
    "年齢": ["28", "45", "65", "", "38", "26", "51", "35"],
    "性別": ["男", "女", "Female", "女", "男", "M", "男", "女"],
    "血液型": ["A", "B", "O", "", "AB", "a", "B", "O"],
    "身長": ["170.5", "158.0", "", "162.5", "175.0", "168", "172.8", "155.5"],
    "体重": ["65.5", "52.0", "70.0", "55.5", "", "62.0", "80.5", "48.0"],
    "電話番号": ["090-1234-5678", "03(5678)1234", "0661234567", "090 9876 5432", "", "0312345678", "090-5555-4444", ""],
    "診療科": ["内科", "外科", "小児科", "内科", "整形外科", "眼科", "内科", "皮膚科"],
    "初診日": ["2024-01-15", "2024/01/20", "2024-1-25", "", "2024.02.01", "2024-02-05", "20240210", "2024-02-15"]
}

patient_df = pd.DataFrame(patient_data)
print("🏥 患者データ（クリーニング前）:")
print(patient_df)

print("""
📋 課題内容:

【データクリーニング課題】
1. 欠損値の確認と対処
   - 各列の欠損値数を表示
   - 氏名の空白を「不明」で置換
   - 年齢の空文字を中央値で置換
   - 身長・体重の欠損値を平均値で置換

2. データ型の変換
   - 年齢を数値型に変換
   - 身長・体重を小数型に変換
   - 初診日を日付型に変換

3. 文字列の正規化
   - 氏名の前後空白を削除
   - 性別を「男」「女」に統一
   - 血液型を大文字に統一
   - 電話番号の形式を統一（090-1234-5678形式）

4. データ検証
   - 年齢の妥当性チェック（0-150歳）
   - BMIの計算と追加
   - 電話番号の形式チェック
   - 初診日の妥当性チェック

【応用課題】
5. 年齢層の分類（小児、成人、高齢者）
6. BMIカテゴリの分類（低体重、普通、肥満など）
7. 診療科ごとの患者数集計
8. 月別初診患者数の集計
""")

print("\n💡 解答例（一部）:")

# 解答例の実装
patient_clean = patient_df.copy()

# 1. 欠損値対応
print("1. 欠損値確認:")
print(patient_clean.isnull().sum())

# 氏名の空白対応
patient_clean['氏名'] = patient_clean['氏名'].replace('', '不明').fillna('不明').str.strip()

# 2. データ型変換
patient_clean['年齢'] = pd.to_numeric(patient_clean['年齢'], errors='coerce')
patient_clean['身長'] = pd.to_numeric(patient_clean['身長'], errors='coerce')
patient_clean['体重'] = pd.to_numeric(patient_clean['体重'], errors='coerce')

# 欠損値を平均値で補完
patient_clean['年齢'].fillna(patient_clean['年齢'].median(), inplace=True)
patient_clean['身長'].fillna(patient_clean['身長'].mean(), inplace=True)
patient_clean['体重'].fillna(patient_clean['体重'].mean(), inplace=True)

# 3. 性別の統一
gender_map = {'M': '男', 'Female': '女'}
patient_clean['性別'] = patient_clean['性別'].replace(gender_map)

# BMI計算
patient_clean['BMI'] = patient_clean['体重'] / (patient_clean['身長'] / 100) ** 2

print("\n🛠️ クリーニング後（一部）:")
print(patient_clean[['氏名', '年齢', '性別', '身長', '体重', 'BMI']].round(2))

print("\n🎯 全ての課題にチャレンジしてみましょう！")
```

---

## Week 4: 集計・グループ化・データ結合をマスター

### 🎯 **この週のゴール**

- groupby 操作を完全にマスターする
- 複雑な集計処理ができるようになる
- データ結合（join, merge）を理解する

---

### **Day 1-3: groupby 操作の基本から応用**

```python
print("👥 Week 4: 集計・グループ化・データ結合")
print("=" * 50)

import pandas as pd
import numpy as np

print("1. groupby操作の基本")
print("=" * 30)

# 豊富な売上データを作成
sales_data = {
    "日付": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02", "2024-01-03",
             "2024-01-03", "2024-01-04", "2024-01-04", "2024-01-05", "2024-01-05"] * 3,
    "店舗": ["新宿店", "渋谷店", "新宿店", "渋谷店", "新宿店", "渋谷店", "新宿店", "渋谷店", "新宿店", "渋谷店"] * 3,
    "担当者": ["田中", "佐藤", "田中", "鈴木", "佐藤", "佐藤", "田中", "鈴木", "鈴木", "田中"] * 3,
    "商品カテゴリ": ["電子機器", "衣料品", "電子機器", "食品", "衣料品", "食品", "電子機器", "衣料品", "食品", "電子機器"] * 3,
    "売上金額": [50000, 30000, 45000, 15000, 25000, 20000, 60000, 35000, 18000, 55000] * 3,
    "利益": [15000, 9000, 13500, 4500, 7500, 6000, 18000, 10500, 5400, 16500] * 3,
    "顧客数": [3, 5, 2, 8, 4, 10, 4, 6, 12, 3] * 3
}

df = pd.DataFrame(sales_data)
print("🛍️ 売上データ:")
print(df.head(10))
print(f"総データ数: {len(df)}行")

# 基本的なgroupby
print("\n📊 基本的なgroupby操作:")

# 1つの列でグループ化
store_summary = df.groupby('店舗')['売上金額'].sum()
print("店舗別売上合計:")
print(store_summary)

# 複数の集計関数
store_detail = df.groupby('店舗')['売上金額'].agg(['sum', 'mean', 'count', 'std'])
print("\n店舗別詳細統計:")
print(store_detail.round(0))

# 複数列を同時に集計
multi_column_agg = df.groupby('店舗').agg({
    '売上金額': ['sum', 'mean'],
    '利益': ['sum', 'mean'],
    '顧客数': 'sum'
})
print("\n複数列集計:")
print(multi_column_agg.round(0))

# カラム名を整理
multi_column_agg.columns = ['売上合計', '売上平均', '利益合計', '利益平均', '総顧客数']
print("\nカラム名整理後:")
print(multi_column_agg)

print("\n2. 複数列でのグループ化")
print("=" * 30)

# 店舗×担当者でグループ化
store_staff = df.groupby(['店舗', '担当者'])['売上金額'].sum()
print("店舗×担当者別売上:")
print(store_staff)

# より複雑なグループ化
category_staff = df.groupby(['商品カテゴリ', '担当者']).agg({
    '売上金額': ['sum', 'count'],
    '利益': 'sum'
})
category_staff.columns = ['売上合計', '取引数', '利益合計']
print("\nカテゴリ×担当者別:")
print(category_staff)

# グループ化結果の並び替え
top_performers = category_staff.sort_values('売上合計', ascending=False)
print("\n売上上位:")
print(top_performers.head())

print("\n3. 高度なgroupby操作")
print("=" * 30)

# カスタム集計関数
def sales_analysis(group):
    """カスタム集計関数"""
    return pd.Series({
        '売上合計': group['売上金額'].sum(),
        '平均売上': group['売上金額'].mean(),
        '最大売上': group['売上金額'].max(),
        '売上件数': len(group),
        '利益率': (group['利益'].sum() / group['売上金額'].sum()) * 100,
        '顧客単価': group['売上金額'].sum() / group['顧客数'].sum()
    })

# カスタム関数適用
custom_analysis = df.groupby('店舗').apply(sales_analysis)
print("カスタム集計分析:")
print(custom_analysis.round(2))

# 条件付きグループ化
high_value_sales = df[df['売上金額'] >= 30000]
high_value_summary = high_value_sales.groupby('商品カテゴリ')['売上金額'].agg(['count', 'mean'])
high_value_summary.columns = ['高額取引数', '平均金額']
print("\n高額取引（3万円以上）:")
print(high_value_summary)

# ランキング機能
df['店舗内売上ランク'] = df.groupby('店舗')['売上金額'].rank(method='dense', ascending=False)
print("\n店舗内売上ランキング:")
print(df[['店舗', '担当者', '売上金額', '店舗内売上ランク']].head(10))

print("\n4. 時系列グループ化")
print("=" * 30)

# 日付でグループ化
daily_summary = df.groupby('日付').agg({
    '売上金額': 'sum',
    '利益': 'sum',
    '顧客数': 'sum'
})
print("日別売上:")
print(daily_summary)

# 前日比計算
daily_summary['売上前日比'] = daily_summary['売上金額'].pct_change() * 100
print("\n前日比付き:")
print(daily_summary.round(2))

# 累計計算
daily_summary['売上累計'] = daily_summary['売上金額'].cumsum()
print("\n累計付き:")
print(daily_summary)
```

### **Day 4-5: ピボットテーブルと集計**

```python
print("\n5. ピボットテーブル")
print("=" * 30)

# ピボットテーブルの基本
basic_pivot = df.pivot_table(
    values='売上金額',
    index='店舗',
    columns='商品カテゴリ',
    aggfunc='sum',
    fill_value=0
)
print("基本ピボットテーブル:")
print(basic_pivot)

# 複数の値を持つピボット
multi_value_pivot = df.pivot_table(
    values=['売上金額', '利益'],
    index='店舗',
    columns='商品カテゴリ',
    aggfunc='sum',
    fill_value=0
)
print("\n複数値ピボット:")
print(multi_value_pivot)

# 複数の集計関数
multi_func_pivot = df.pivot_table(
    values='売上金額',
    index='店舗',
    columns='商品カテゴリ',
    aggfunc=['sum', 'mean', 'count'],
    fill_value=0
)
print("\n複数関数ピボット:")
print(multi_func_pivot)

# 行・列の合計を追加
pivot_with_margins = df.pivot_table(
    values='売上金額',
    index='店舗',
    columns='商品カテゴリ',
    aggfunc='sum',
    fill_value=0,
    margins=True,
    margins_name='合計'
)
print("\n合計付きピボット:")
print(pivot_with_margins)

# パーセント計算
percent_pivot = df.pivot_table(
    values='売上金額',
    index='店舗',
    columns='商品カテゴリ',
    aggfunc='sum',
    fill_value=0
)

# 行の合計に対する割合
row_percent = percent_pivot.div(percent_pivot.sum(axis=1), axis=0) * 100
print("\n店舗別カテゴリ構成比(%):")
print(row_percent.round(1))

# 列の合計に対する割合
col_percent = percent_pivot.div(percent_pivot.sum(axis=0), axis=1) * 100
print("\nカテゴリ別店舗シェア(%):")
print(col_percent.round(1))

print("\n6. クロス集計")
print("=" * 30)

# 基本的なクロス集計
cross_tab = pd.crosstab(df['店舗'], df['商品カテゴリ'])
print("取引件数のクロス集計:")
print(cross_tab)

# 値を指定したクロス集計
cross_tab_values = pd.crosstab(
    df['店舗'],
    df['商品カテゴリ'],
    values=df['売上金額'],
    aggfunc='sum'
)
print("\n売上金額のクロス集計:")
print(cross_tab_values.fillna(0))

# 割合表示
cross_tab_percent = pd.crosstab(df['店舗'], df['商品カテゴリ'], normalize='index') * 100
print("\n割合クロス集計(%):")
print(cross_tab_percent.round(1))

# 複数次元クロス集計
multi_cross = pd.crosstab(
    [df['店舗'], df['担当者']],
    df['商品カテゴリ'],
    values=df['売上金額'],
    aggfunc='sum'
)
print("\n店舗×担当者×カテゴリ クロス集計:")
print(multi_cross.fillna(0))
```

### **Day 6-7: データ結合（join, merge）**

```python
print("\n7. データ結合")
print("=" * 30)

# 結合用のデータを準備
# 商品マスタ
product_master = pd.DataFrame({
    "商品コード": ["P001", "P002", "P003", "P004", "P005"],
    "商品名": ["ノートPC", "マウス", "キーボード", "モニター", "ヘッドセット"],
    "カテゴリ": ["PC", "周辺機器", "周辺機器", "PC", "音響機器"],
    "定価": [100000, 3000, 6000, 40000, 15000]
})

# 売上トランザクション
transaction_data = pd.DataFrame({
    "取引ID": ["T001", "T002", "T003", "T004", "T005", "T006"],
    "商品コード": ["P001", "P002", "P001", "P003", "P006", "P002"],  # P006は存在しない商品
    "数量": [2, 5, 1, 3, 2, 4],
    "売上日": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02", "2024-01-03", "2024-01-03"],
    "店舗": ["新宿店", "渋谷店", "新宿店", "渋谷店", "新宿店", "渋谷店"]
})

# 店舗マスタ
store_master = pd.DataFrame({
    "店舗": ["新宿店", "渋谷店", "池袋店"],  # 池袋店は取引がない
    "店舗コード": ["S001", "S002", "S003"],
    "住所": ["東京都新宿区", "東京都渋谷区", "東京都豊島区"],
    "開店日": ["2020-01-01", "2020-02-01", "2020-03-01"]
})

print("商品マスタ:")
print(product_master)
print("\n売上トランザクション:")
print(transaction_data)
print("\n店舗マスタ:")
print(store_master)

print("\n📍 内部結合（inner join）")
# 内部結合：両方のテーブルに存在するデータのみ
inner_join = pd.merge(transaction_data, product_master, on='商品コード', how='inner')
print("商品マスタとの内部結合:")
print(inner_join)

print("\n📍 左結合（left join）")
# 左結合：左のテーブルのデータを全て保持
left_join = pd.merge(transaction_data, product_master, on='商品コード', how='left')
print("商品マスタとの左結合:")
print(left_join)

print("\n📍 右結合（right join）")
# 右結合：右のテーブルのデータを全て保持
right_join = pd.merge(transaction_data, product_master, on='商品コード', how='right')
print("商品マスタとの右結合:")
print(right_join)

print("\n📍 外部結合（outer join）")
# 外部結合：両方のテーブルの全データを保持
outer_join = pd.merge(transaction_data, product_master, on='商品コード', how='outer')
print("商品マスタとの外部結合:")
print(outer_join)

print("\n📍 複数テーブルの結合")
# 段階的に結合
step1 = pd.merge(transaction_data, product_master, on='商品コード', how='left')
final_result = pd.merge(step1, store_master, on='店舗', how='left')

print("3テーブル結合結果:")
print(final_result[['取引ID', '商品名', 'カテゴリ', '数量', '店舗', '住所']])

print("\n📍 異なる列名での結合")
# 列名が異なる場合の結合
customer_data = pd.DataFrame({
    "顧客ID": ["C001", "C002", "C003"],
    "customer_name": ["田中", "佐藤", "鈴木"],
    "年齢": [30, 25, 35]
})

order_data = pd.DataFrame({
    "注文ID": ["O001", "O002", "O003"],
    "cust_id": ["C001", "C003", "C004"],  # 列名が異なる
    "商品": ["ノートPC", "マウス", "キーボード"],
    "金額": [100000, 3000, 6000]
})

# 異なる列名で結合
different_columns_join = pd.merge(
    order_data,
    customer_data,
    left_on='cust_id',
    right_on='顧客ID',
    how='left'
)
print("異なる列名での結合:")
print(different_columns_join)

print("\n📍 インデックスでの結合")
# インデックスを使った結合
df1 = pd.DataFrame({
    '売上': [100, 200, 300]
}, index=['A', 'B', 'C'])

df2 = pd.DataFrame({
    '利益': [30, 60, 90],
    '地域': ['東京', '大阪', '名古屋']
}, index=['A', 'B', 'D'])

index_join = df1.join(df2, how='outer')
print("インデックス結合:")
print(index_join)

print("\n📍 結合の検証")
# 結合結果の検証
print("元の取引データ数:", len(transaction_data))
print("内部結合後:", len(inner_join))
print("左結合後:", len(left_join))

# 結合できなかったデータの確認
missing_products = left_join[left_join['商品名'].isnull()]
if not missing_products.empty:
    print("\nマスタにない商品:")
    print(missing_products[['取引ID', '商品コード']])

print("\n8. concat（連結）")
print("=" * 30)

# データの縦連結
df1 = pd.DataFrame({
    '店舗': ['新宿店', '渋谷店'],
    '売上': [100000, 120000]
})

df2 = pd.DataFrame({
    '店舗': ['池袋店', '銀座店'],
    '売上': [90000, 150000]
})

vertical_concat = pd.concat([df1, df2], ignore_index=True)
print("縦連結:")
print(vertical_concat)

# データの横連結
df3 = pd.DataFrame({
    '利益': [30000, 36000, 27000, 45000]
})

horizontal_concat = pd.concat([vertical_concat, df3], axis=1)
print("\n横連結:")
print(horizontal_concat)

# キーによる連結
df4 = pd.DataFrame({
    '店舗': ['新宿店', '渋谷店', '池袋店'],
    '従業員数': [10, 12, 8]
})

df5 = pd.DataFrame({
    '店舗': ['新宿店', '渋谷店', '銀座店'],
    '面積': [100, 120, 80]
})

key_based_concat = pd.concat([df4.set_index('店舗'), df5.set_index('店舗')], axis=1, sort=True)
print("\nキーベース連結:")
print(key_based_concat)
```

**🛠 Week 4 の実習課題**

```python
print("\n📝 Week 4 実習課題")
print("=" * 50)

print("🏬 小売チェーンの売上分析プロジェクト")

# 課題用データセット
# 店舗マスタ
stores = pd.DataFrame({
    "店舗ID": ["S001", "S002", "S003", "S004", "S005"],
    "店舗名": ["新宿店", "渋谷店", "池袋店", "銀座店", "原宿店"],
    "地域": ["東京", "東京", "東京", "東京", "東京"],
    "開店年": [2018, 2019, 2020, 2015, 2021],
    "面積_㎡": [200, 150, 180, 250, 120]
})

# 商品マスタ
products = pd.DataFrame({
    "商品ID": ["P001", "P002", "P003", "P004", "P005", "P006"],
    "商品名": ["Tシャツ", "ジーンズ", "スニーカー", "バッグ", "帽子", "ベルト"],
    "カテゴリ": ["トップス", "ボトムス", "シューズ", "アクセサリー", "アクセサリー", "アクセサリー"],
    "原価": [1000, 3000, 4000, 2500, 800, 1200],
    "定価": [2000, 6000, 8000, 5000, 1600, 2400]
})

# 売上トランザクション
np.random.seed(42)
transactions = []
for i in range(200):
    transactions.append({
        "取引ID": f"T{i+1:03d}",
        "店舗ID": np.random.choice(stores["店舗ID"]),
        "商品ID": np.random.choice(products["商品ID"]),
        "数量": np.random.randint(1, 6),
        "売価": np.random.randint(1500, 8500),
        "売上日": np.random.choice(pd.date_range("2024-01-01", "2024-03-31")),
        "顧客年齢": np.random.randint(18, 65),
        "性別": np.random.choice(["男性", "女性"])
    })

sales_df = pd.DataFrame(transactions)

print("店舗マスタ:")
print(stores.head())
print("\n商品マスタ:")
print(products.head())
print("\n売上データ:")
print(sales_df.head())

print("""
📋 分析課題:

【基本集計課題】
1. 店舗別売上分析
   - 店舗別の売上合計、平均、取引数
   - 店舗別の利益計算（売価 - 原価）

2. 商品分析
   - 商品別売上ランキング
   - カテゴリ別売上分析
   - 商品別利益率分析

3. 時系列分析
   - 月別売上推移
   - 曜日別売上パターン
   - 売上トップ3の店舗の日別推移

【データ結合課題】
4. マスタとの結合
   - 売上データに店舗情報を結合
   - 売上データに商品情報を結合
   - 3テーブル結合で完全な売上明細作成

5. 顧客分析
   - 年齢層別購買分析（20代、30代、40代、50代以上）
   - 性別×カテゴリ別の売上分析
   - 店舗面積と売上の関係分析

【高度な分析課題】
6. ピボット分析
   - 店舗×カテゴリの売上ピボットテーブル
   - 月×店舗の売上推移ピボット
   - 年齢層×性別×カテゴリの3次元分析

7. パフォーマンス分析
   - 店舗面積あたりの売上効率
   - 商品回転率分析
   - 利益率の高い店舗×商品組み合わせ

8. 比較分析
   - 各店舗の売上構成比
   - 前月比分析
   - 同カテゴリ内での商品パフォーマンス比較
""")

print("\n💡 解答例（一部）:")

# 解答例
# 1. 基本的な店舗別分析
store_sales = sales_df.groupby('店舗ID').agg({
    '売価': ['sum', 'mean', 'count'],
    '数量': 'sum'
})
store_sales.columns = ['売上合計', '平均売価', '取引数', '総販売数']

# 店舗マスタと結合
store_analysis = pd.merge(store_sales.reset_index(), stores, on='店舗ID')
store_analysis['面積当売上'] = store_analysis['売上合計'] / store_analysis['面積_㎡']

print("店舗別分析:")
print(store_analysis[['店舗名', '売上合計', '取引数', '面積_㎡', '面積当売上']].round(2))

# 2. 商品カテゴリ分析用の結合
product_sales = pd.merge(sales_df, products, on='商品ID')
category_analysis = product_sales.groupby('カテゴリ').agg({
    '売価': 'sum',
    '数量': 'sum'
})

print("\nカテゴリ別売上:")
print(category_analysis)

print("\n🎯 全ての課題にチャレンジしてみましょう！")
```

---

## Week 5: 時系列データの基本操作

### 🎯 **この週のゴール**

- datetime 型の操作をマスターする
- 時系列データの基本的な分析ができる
- 日付・時間を使ったフィルタリングを習得する

---

### **Day 1-7: 時系列データの操作**

```python
print("📅 Week 5: 時系列データの基本操作")
print("=" * 50)

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

print("1. datetime型の基本")
print("=" * 30)

# 様々な日付データの作成
date_strings = [
    "2024-01-01",
    "01/15/2024",
    "2024年2月20日",
    "March 15, 2024",
    "2024-04-01 14:30:00"
]

print("📅 様々な日付形式:")
for date_str in date_strings[:4]:  # 日本語は除く
    try:
        converted = pd.to_datetime(date_str)
        print(f"{date_str} → {converted}")
    except:
        print(f"{date_str} → 変換失敗")

# 時系列データの作成
print("\n📊 時系列データの作成:")

# 日付範囲の生成
date_range = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
print(f"2024年の日付範囲: {len(date_range)}日")

# ビジネス日（平日のみ）
business_days = pd.date_range(start='2024-01-01', end='2024-12-31', freq='B')
print(f"2024年の営業日: {len(business_days)}日")

# 月末日
month_ends = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
print(f"月末日: {len(month_ends)}日")

# サンプル時系列データの作成
np.random.seed(42)
time_series_data = {
    "日付": pd.date_range('2024-01-01', periods=365, freq='D'),
    "売上": np.random.normal(100000, 20000, 365),
    "顧客数": np.random.poisson(50, 365),
    "気温": 15 + 10 * np.sin(2 * np.pi * np.arange(365) / 365) + np.random.normal(0, 3, 365)
}

# 売上に季節性を追加
for i, date in enumerate(time_series_data["日付"]):
    # 12月は売上UP
    if date.month == 12:
        time_series_data["売上"][i] *= 1.5
    # 週末効果
    if date.weekday() >= 5:
        time_series_data["売上"][i] *= 1.2

ts_df = pd.DataFrame(time_series_data)
ts_df.set_index('日付', inplace=True)

print("\n🔍 時系列データサンプル:")
print(ts_df.head())

print("\n2. 日付・時間の情報抽出")
print("=" * 30)

# 日付から情報を抽出
ts_df['年'] = ts_df.index.year
ts_df['月'] = ts_df.index.month
ts_df['日'] = ts_df.index.day
ts_df['曜日番号'] = ts_df.index.weekday  # 0=月曜日
ts_df['曜日名'] = ts_df.index.day_name()
ts_df['四半期'] = ts_df.index.quarter
ts_df['年間通算日'] = ts_df.index.dayofyear
ts_df['週番号'] = ts_df.index.isocalendar().week

print("📋 日付情報の抽出:")
print(ts_df[['売上', '年', '月', '曜日名', '四半期']].head(10))

# 平日・週末の判定
ts_df['平日フラグ'] = ts_df.index.weekday < 5
ts_df['週末フラグ'] = ts_df.index.weekday >= 5

print(f"\n平日: {ts_df['平日フラグ'].sum()}日")
print(f"週末: {ts_df['週末フラグ'].sum()}日")

print("\n3. 時系列データの選択・抽出")
print("=" * 30)

# 特定の月のデータ
january_data = ts_df[ts_df.index.month == 1]
print(f"1月のデータ: {len(january_data)}日")
print("1月の平均売上:", january_data['売上'].mean())

# 特定の期間
q1_data = ts_df['2024-01-01':'2024-03-31']
print(f"\n第1四半期: {len(q1_data)}日")

# 複数条件
summer_weekends = ts_df[
    (ts_df.index.month.isin([6, 7, 8])) &
    (ts_df['週末フラグ'] == True)
]
print(f"夏の週末: {len(summer_weekends)}日")

# 文字列による期間指定
july_data = ts_df.loc['2024-07']
print(f"\n7月のデータ: {len(july_data)}日")

print("\n4. 時系列集計")
print("=" * 30)

# 月別集計
monthly_summary = ts_df.groupby(ts_df.index.to_period('M')).agg({
    '売上': ['sum', 'mean'],
    '顧客数': 'sum',
    '気温': 'mean'
})
monthly_summary.columns = ['月間売上', '平均日売上', '月間顧客数', '平均気温']
print("月別サマリー:")
print(monthly_summary.head())

# 曜日別パターン
weekday_pattern = ts_df.groupby('曜日名')['売上'].mean()
# 曜日順に並び替え
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_pattern = weekday_pattern.reindex(weekday_order)
weekday_pattern.index = ['月', '火', '水', '木', '金', '土', '日']

print("\n📅 曜日別平均売上:")
print(weekday_pattern.round(0))

# 四半期別集計
quarterly_summary = ts_df.groupby('四半期').agg({
    '売上': ['sum', 'mean'],
    '顧客数': 'sum',
    '気温': 'mean'
})
quarterly_summary.columns = ['四半期売上', '平均日売上', '四半期顧客数', '平均気温']
print("四半期別サマリー:")
print(quarterly_summary.round(0))

# 週別集計
weekly_summary = ts_df.groupby('週番号')['売上'].sum()
print(f"\n週別売上（最初の5週）:")
print(weekly_summary.head())

print("\n5. 移動平均とトレンド分析")
print("=" * 30)

# 移動平均の計算
ts_df['売上_7日移動平均'] = ts_df['売上'].rolling(window=7).mean()
ts_df['売上_30日移動平均'] = ts_df['売上'].rolling(window=30).mean()

# 指数平滑移動平均
ts_df['売上_指数平滑'] = ts_df['売上'].ewm(span=7).mean()

print("📈 移動平均データ:")
print(ts_df[['売上', '売上_7日移動平均', '売上_30日移動平均']].head(10).round(0))

# 前日比、前年同月比
ts_df['前日比'] = ts_df['売上'].pct_change() * 100
ts_df['前週同曜日比'] = ts_df['売上'].pct_change(periods=7) * 100

print("\n📊 変化率分析:")
print(ts_df[['売上', '前日比', '前週同曜日比']].head(14).round(2))

print("\n6. 季節性分析")
print("=" * 30)

# 月別の季節性
seasonal_analysis = ts_df.groupby('月').agg({
    '売上': ['mean', 'std'],
    '顧客数': 'mean'
})
seasonal_analysis.columns = ['平均売上', '売上標準偏差', '平均顧客数']

# 全体平均との比較
overall_avg = ts_df['売上'].mean()
seasonal_analysis['季節指数'] = seasonal_analysis['平均売上'] / overall_avg

print("🌸 月別季節性:")
print(seasonal_analysis.round(2))

# 曜日効果の分析
weekday_effect = ts_df.groupby('曜日番号').agg({
    '売上': 'mean',
    '顧客数': 'mean'
})
weekday_effect.index = ['月', '火', '水', '木', '金', '土', '日']

# 平日平均との比較
weekday_avg = ts_df[ts_df['平日フラグ']]['売上'].mean()
weekday_effect['平日比'] = weekday_effect['売上'] / weekday_avg

print("\n📅 曜日効果:")
print(weekday_effect.round(2))

print("\n7. 欠損値の時系列補間")
print("=" * 30)

# 意図的に欠損値を作成
ts_sample = ts_df['売上'].copy()
missing_dates = pd.date_range('2024-02-10', '2024-02-15')
ts_sample.loc[missing_dates] = np.nan

print("📋 欠損値のある時系列:")
print(ts_sample['2024-02-08':'2024-02-18'])

# 様々な補間方法
interpolated_data = pd.DataFrame({
    '元データ': ts_sample,
    '線形補間': ts_sample.interpolate(method='linear'),
    '時間重み補間': ts_sample.interpolate(method='time'),
    '前方埋め': ts_sample.fillna(method='ffill'),
    '後方埋め': ts_sample.fillna(method='bfill')
})

print("\n🔧 各種補間結果:")
print(interpolated_data['2024-02-08':'2024-02-18'].round(0))

print("\n8. リサンプリング")
print("=" * 30)

# 週次リサンプリング
weekly_resample = ts_df['売上'].resample('W').agg(['sum', 'mean', 'std'])
weekly_resample.columns = ['週間売上', '週平均', '週標準偏差']
print("📊 週次リサンプリング:")
print(weekly_resample.head().round(0))

# 月次リサンプリング
monthly_resample = ts_df.resample('M').agg({
    '売上': ['sum', 'mean'],
    '顧客数': 'sum',
    '気温': 'mean'
})
monthly_resample.columns = ['月間売上', '日平均売上', '月間顧客数', '平均気温']
print("\n📅 月次リサンプリング:")
print(monthly_resample.head().round(0))

# カスタムリサンプリング（四半期の最初の月）
quarterly_first = ts_df['売上'].resample('QS').sum()
print("\n📈 四半期初月売上:")
print(quarterly_first)

print("\n9. 時差とタイムゾーン")
print("=" * 30)

# タイムゾーン付きデータ
tz_data = pd.date_range('2024-01-01 09:00', periods=24, freq='H', tz='Asia/Tokyo')
sales_hourly = pd.DataFrame({
    '時刻': tz_data,
    '売上': np.random.normal(10000, 2000, 24)
})

print("🌏 タイムゾーン付きデータ:")
print(sales_hourly.head())

# 異なるタイムゾーンに変換
sales_hourly['NY時刻'] = sales_hourly['時刻'].dt.tz_convert('America/New_York')
sales_hourly['UTC時刻'] = sales_hourly['時刻'].dt.tz_convert('UTC')

print("\n🌍 タイムゾーン変換:")
print(sales_hourly[['時刻', 'NY時刻', 'UTC時刻']].head(3))

print("\n10. 営業日計算")
print("=" * 30)

# 営業日の判定（土日祝日を除く）
import pandas.tseries.offsets as offsets

# カスタム営業日カレンダー（日本の祝日は簡略化）
holidays = ['2024-01-01', '2024-02-11', '2024-04-29', '2024-05-03', '2024-05-04', '2024-05-05']
holiday_dates = pd.to_datetime(holidays)

ts_df['営業日フラグ'] = (
    (ts_df.index.weekday < 5) &  # 平日
    (~ts_df.index.isin(holiday_dates))  # 祝日以外
)

business_days_count = ts_df['営業日フラグ'].sum()
print(f"2024年の営業日数: {business_days_count}日")

# 営業日のみの売上分析
business_only = ts_df[ts_df['営業日フラグ']]
print(f"営業日平均売上: {business_only['売上'].mean():,.0f}円")
print(f"休日平均売上: {ts_df[~ts_df['営業日フラグ']]['売上'].mean():,.0f}円")
```

**🛠 Week 5 の実習課題**

```python
print("\n📝 Week 5 実習課題")
print("=" * 50)

print("📊 ECサイトの時系列売上分析")

# 実際的な時系列データを作成
np.random.seed(42)
ecommerce_data = []

for i in range(365):
    date = pd.Timestamp('2024-01-01') + pd.Timedelta(days=i)

    # 基本売上（季節性を含む）
    base_sales = 50000 + 20000 * np.sin(2 * np.pi * i / 365)

    # 曜日効果
    if date.weekday() == 5:  # 土曜日
        base_sales *= 1.3
    elif date.weekday() == 6:  # 日曜日
        base_sales *= 1.1
    elif date.weekday() < 5:  # 平日
        base_sales *= 0.9

    # 特別イベント効果
    if date.month == 12:  # 12月（年末商戦）
        base_sales *= 1.8
    elif date.month in [3, 7]:  # 3月、7月（セール月）
        base_sales *= 1.4

    # ランダムノイズ
    base_sales += np.random.normal(0, 5000)

    ecommerce_data.append({
        '日付': date,
        '売上': max(0, base_sales),
        '注文数': np.random.poisson(base_sales / 5000),
        '新規顧客': np.random.poisson(10),
        'ページビュー': np.random.poisson(base_sales / 100)
    })

ecommerce_df = pd.DataFrame(ecommerce_data)
ecommerce_df.set_index('日付', inplace=True)

print("🛒 ECサイト売上データ:")
print(ecommerce_df.head())

print("""
📋 分析課題:

【基本分析】
1. 月別売上推移の分析
   - 月別売上合計とグラフ化
   - 前月比成長率の計算
   - 季節指数の算出

2. 曜日別パターン分析
   - 曜日別平均売上
   - 平日 vs 週末の比較
   - 最も売上の高い曜日の特定

3. 移動平均分析
   - 7日移動平均で短期トレンド把握
   - 30日移動平均で中期トレンド把握
   - トレンドの変化点の特定

【応用分析】
4. 季節性分解
   - トレンド、季節性、ノイズの分離
   - 年間売上サイクルの理解
   - 異常値の検出

5. 成長率分析
   - 前年同月比の計算（仮想）
   - 週次成長率の推移
   - 四半期別成長率

6. 相関分析
   - 売上と注文数の関係
   - ページビューと売上の関係
   - 新規顧客と売上の関係

【実践分析】
7. 売上予測の基礎
   - 過去30日の平均から翌日予測
   - 同曜日の平均から予測
   - 移動平均ベースの予測

8. ビジネス指標の計算
   - 平均注文単価（AOV）の推移
   - コンバージョン率の推移
   - 顧客当たり売上の推移

9. 異常検知
   - 売上の異常に高い/低い日の特定
   - 移動平均からの乖離分析
   - 統計的異常値の検出
""")

print("\n💡 解答例（一部）:")

# 1. 月別売上分析
monthly_sales = ecommerce_df.groupby(ecommerce_df.index.to_period('M')).agg({
    '売上': ['sum', 'mean'],
    '注文数': 'sum'
})
monthly_sales.columns = ['月間売上', '日平均売上', '月間注文数']
monthly_sales['前月比'] = monthly_sales['月間売上'].pct_change() * 100

print("📈 月別売上分析:")
print(monthly_sales.round(2))

# 2. 曜日別分析
weekday_analysis = ecommerce_df.groupby(ecommerce_df.index.dayofweek).agg({
    '売上': 'mean',
    '注文数': 'mean'
})
weekday_analysis.index = ['月', '火', '水', '木', '金', '土', '日']
weekday_analysis['売上指数'] = weekday_analysis['売上'] / weekday_analysis['売上'].mean()

print("\n📅 曜日別分析:")
print(weekday_analysis.round(2))

# 3. 移動平均
ecommerce_df['売上_7日MA'] = ecommerce_df['売上'].rolling(7).mean()
ecommerce_df['売上_30日MA'] = ecommerce_df['売上'].rolling(30).mean()

print("\n📊 移動平均サンプル:")
print(ecommerce_df[['売上', '売上_7日MA', '売上_30日MA']].tail().round(0))

# 4. 平均注文単価
ecommerce_df['AOV'] = ecommerce_df['売上'] / ecommerce_df['注文数']
monthly_aov = ecommerce_df.groupby(ecommerce_df.index.to_period('M'))['AOV'].mean()

print("\n💰 月別平均注文単価:")
print(monthly_aov.round(0))

print("\n🎯 全ての課題にチャレンジしてみましょう！")
```

---

## Week 6: 可視化と実践プロジェクト

### 🎯 **この週のゴール**

- pandas での基本的な可視化をマスターする
- 実際のビジネス課題を解決する
- 総合的なデータ分析プロジェクトを完成させる

---

### **Day 1-3: pandas での可視化**

```python
print("📊 Week 6: 可視化と実践プロジェクト")
print("=" * 50)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 日本語フォント設定
plt.rcParams['font.family'] = 'DejaVu Sans'
sns.set_style("whitegrid")

print("1. pandasでの基本的な可視化")
print("=" * 30)

# 可視化用のサンプルデータ作成
np.random.seed(42)
visualization_data = {
    "月": [f"{i}月" for i in range(1, 13)],
    "売上": [100, 120, 140, 135, 160, 180, 200, 190, 170, 150, 220, 250],
    "利益": [30, 36, 42, 40, 48, 54, 60, 57, 51, 45, 66, 75],
    "顧客数": [500, 600, 700, 675, 800, 900, 1000, 950, 850, 750, 1100, 1250]
}

viz_df = pd.DataFrame(visualization_data)
viz_df.set_index('月', inplace=True)

print("📋 可視化用データ:")
print(viz_df)

# 1. 線グラフ
print("\n📈 線グラフ:")
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 売上推移
viz_df['売上'].plot(kind='line', ax=axes[0,0], title='月別売上推移', color='blue', marker='o')
axes[0,0].set_ylabel('売上（万円）')

# 複数系列
viz_df[['売上', '利益']].plot(kind='line', ax=axes[0,1], title='売上・利益推移', marker='o')
axes[0,1].set_ylabel('金額（万円）')

# 棒グラフ
viz_df['顧客数'].plot(kind='bar', ax=axes[1,0], title='月別顧客数', color='green')
axes[1,0].set_ylabel('顧客数（人）')
axes[1,0].tick_params(axis='x', rotation=45)

# 散布図
viz_df.plot(kind='scatter', x='売上', y='利益', ax=axes[1,1], title='売上 vs 利益', alpha=0.7)

plt.tight_layout()
plt.show()

print("\n2. 様々なグラフ種類")
print("=" * 30)

# カテゴリ別データ
category_data = {
    "商品カテゴリ": ["電子機器", "衣料品", "食品", "書籍", "スポーツ", "美容"],
    "売上": [850, 620, 380, 240, 450, 310],
    "利益率": [25, 45, 15, 35, 30, 50]
}

cat_df = pd.DataFrame(category_data)
cat_df.set_index('商品カテゴリ', inplace=True)

fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# 棒グラフ（垂直）
cat_df['売上'].plot(kind='bar', ax=axes[0,0], title='カテゴリ別売上', color='skyblue')
axes[0,0].tick_params(axis='x', rotation=45)

# 棒グラフ（水平）
cat_df['売上'].plot(kind='barh', ax=axes[0,1], title='カテゴリ別売上（横）', color='lightcoral')

# 円グラフ
cat_df['売上'].plot(kind='pie', ax=axes[0,2], title='売上構成比', autopct='%1.1f%%')

# ヒストグラム
sales_dist = np.random.normal(100, 20, 1000)
pd.Series(sales_dist).plot(kind='hist', ax=axes[1,0], title='売上分布', bins=30, alpha=0.7)

# 箱ひげ図
box_data = pd.DataFrame({
    '店舗A': np.random.normal(100, 15, 100),
    '店舗B': np.random.normal(120, 20, 100),
    '店舗C': np.random.normal(90, 10, 100)
})
box_data.plot(kind='box', ax=axes[1,1], title='店舗別売上分布')

# 面グラフ
viz_df[['売上', '利益']].plot(kind='area', ax=axes[1,2], title='累積売上・利益', alpha=0.7)

plt.tight_layout()
plt.show()

print("\n3. 高度な可視化")
print("=" * 30)

# 時系列データの可視化
time_data = pd.DataFrame({
    '日付': pd.date_range('2024-01-01', periods=365, freq='D'),
    '売上': 50000 + 10000 * np.sin(2 * np.pi * np.arange(365) / 365) + np.random.normal(0, 5000, 365)
})
time_data.set_index('日付', inplace=True)

# 移動平均を追加
time_data['MA7'] = time_data['売上'].rolling(7).mean()
time_data['MA30'] = time_data['売上'].rolling(30).mean()

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 時系列プロット
time_data[['売上', 'MA7', 'MA30']].plot(ax=axes[0,0], title='売上推移と移動平均')
axes[0,0].legend(['売上', '7日移動平均', '30日移動平均'])

# 月別集計
monthly_sum = time_data.groupby(time_data.index.to_period('M'))['売上'].sum()
monthly_sum.plot(kind='bar', ax=axes[0,1], title='月別売上')
axes[0,1].tick_params(axis='x', rotation=45)

# ヒートマップ用データ
heatmap_data = time_data.copy()
heatmap_data['月'] = heatmap_data.index.month
heatmap_data['日'] = heatmap_data.index.day
pivot_data = heatmap_data.pivot_table(values='売上', index='月', columns='日', fill_value=0)

# ヒートマップ（簡易版）
im = axes[1,0].imshow(pivot_data.values, cmap='YlOrRd', aspect='auto')
axes[1,0].set_title('月別日別売上ヒートマップ')
axes[1,0].set_xlabel('日')
axes[1,0].set_ylabel('月')

# 散布図マトリックス（相関）
correlation_data = pd.DataFrame({
    '売上': np.random.normal(100, 20, 100),
    '広告費': np.random.normal(10, 3, 100),
    '気温': np.random.normal(20, 5, 100)
})
correlation_data['売上'] = correlation_data['売上'] + 0.7 * correlation_data['広告費'] + 0.3 * correlation_data['気温']

correlation_data.plot(kind='scatter', x='広告費', y='売上', ax=axes[1,1], title='広告費 vs 売上')

plt.tight_layout()
plt.show()

print("\n4. グラフのカスタマイズ")
print("=" * 30)

# 詳細なカスタマイズ例
fig, ax = plt.subplots(figsize=(10, 6))

# データプロット
viz_df['売上'].plot(kind='line', ax=ax, color='#2E86AB', linewidth=3, marker='o', markersize=8)

# カスタマイズ
ax.set_title('2024年月別売上推移', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('月', fontsize=12)
ax.set_ylabel('売上（万円）', fontsize=12)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#F8F9FA')

# 注釈追加
max_idx = viz_df['売上'].idxmax()
max_value = viz_df['売上'].max()
ax.annotate(f'最高売上: {max_value}万円',
           xy=(max_idx, max_value),
           xytext=(max_idx, max_value + 20),
           arrowprops=dict(arrowstyle='->', color='red'),
           fontsize=10, color='red')

plt.tight_layout()
plt.show()

print("✅ 可視化の基本をマスターしました！")
```

### **Day 4-7: 総合実践プロジェクト**

```python
print("\n🎯 総合実践プロジェクト: ECサイト売上分析")
print("=" * 50)

print("📋 プロジェクト概要:")
print("""
あなたはECサイトのデータアナリストです。
以下のデータを分析し、ビジネス改善案を提案してください。

【データセット】
1. 売上トランザクション（1年分）
2. 商品マスタ
3. 顧客マスタ
4. キャンペーン情報

【分析目標】
- 売上傾向の把握
- 商品・顧客セグメント分析
- 季節性・トレンド分析
- 改善提案の策定
""")

# 実践的なデータセット作成
np.random.seed(42)

# 1. 商品マスタ
products = pd.DataFrame({
    "商品ID": [f"P{i:03d}" for i in range(1, 51)],
    "商品名": [f"商品{i}" for i in range(1, 51)],
    "カテゴリ": np.random.choice(['電子機器', 'ファッション', '本・雑誌', 'スポーツ', '美容・健康'], 50),
    "価格": np.random.uniform(1000, 50000, 50).round(0),
    "原価": lambda x: x * np.random.uniform(0.4, 0.7, 50)
})
products['原価'] = (products['価格'] * np.random.uniform(0.4, 0.7, 50)).round(0)
products['利益率'] = ((products['価格'] - products['原価']) / products['価格'] * 100).round(1)

# 2. 顧客マスタ
customers = pd.DataFrame({
    "顧客ID": [f"C{i:04d}" for i in range(1, 501)],
    "年齢": np.random.randint(18, 70, 500),
    "性別": np.random.choice(['男性', '女性'], 500),
    "地域": np.random.choice(['関東', '関西', '中部', '九州', '東北'], 500),
    "会員ランク": np.random.choice(['ブロンズ', 'シルバー', 'ゴールド', 'プラチナ'], 500, p=[0.4, 0.3, 0.2, 0.1]),
    "登録日": pd.to_datetime(np.random.choice(pd.date_range('2023-01-01', '2024-12-31'), 500))
})

# 3. 売上トランザクション（1年分）
transactions = []
for i in range(3000):
    transaction_date = pd.Timestamp('2024-01-01') + pd.Timedelta(days=np.random.randint(0, 365))
    customer_id = np.random.choice(customers['顧客ID'])
    product_id = np.random.choice(products['商品ID'])
    quantity = np.random.randint(1, 5)

    # 価格に多少の変動を加える
    base_price = products[products['商品ID'] == product_id]['価格'].iloc[0]
    actual_price = base_price * np.random.uniform(0.8, 1.2)

    transactions.append({
        "取引ID": f"T{i+1:05d}",
        "日付": transaction_date,
        "顧客ID": customer_id,
        "商品ID": product_id,
        "数量": quantity,
        "単価": actual_price,
        "売上": actual_price * quantity
    })

sales_df = pd.DataFrame(transactions)

# 4. キャンペーン情報
campaigns = pd.DataFrame({
    "キャンペーン名": ["新春セール", "春のファッション祭", "夏のボーナスセール", "秋の読書キャンペーン", "年末大感謝祭"],
    "開始日": ["2024-01-01", "2024-03-01", "2024-07-01", "2024-09-01", "2024-12-01"],
    "終了日": ["2024-01-31", "2024-03-31", "2024-07-31", "2024-09-30", "2024-12-31"],
    "対象カテゴリ": ["全商品", "ファッション", "全商品", "本・雑誌", "全商品"],
    "割引率": [20, 30, 25, 15, 40]
})

print("\n📊 データセット概要:")
print(f"商品数: {len(products)}")
print(f"顧客数: {len(customers)}")
print(f"取引数: {len(sales_df)}")
print(f"キャンペーン数: {len(campaigns)}")

print("\n🔍 Step 1: データの結合と基本統計")
print("=" * 40)

# データ結合
sales_detail = sales_df.merge(products, on='商品ID', how='left')
sales_detail = sales_detail.merge(customers, on='顧客ID', how='left')

# 基本統計
print("📈 基本統計:")
print(f"総売上: {sales_detail['売上'].sum():,.0f}円")
print(f"平均注文単価: {sales_detail['売上'].mean():,.0f}円")
print(f"取引期間: {sales_detail['日付'].min().strftime('%Y-%m-%d')} 〜 {sales_detail['日付'].max().strftime('%Y-%m-%d')}")

# 月別売上
monthly_sales = sales_detail.groupby(sales_detail['日付'].dt.to_period('M')).agg({
    '売上': 'sum',
    '取引ID': 'count'
})
monthly_sales.columns = ['月間売上', '取引数']
monthly_sales['平均注文単価'] = monthly_sales['月間売上'] / monthly_sales['取引数']

print("\n📅 月別売上サマリー:")
print(monthly_sales.round(0))

print("\n🔍 Step 2: 商品分析")
print("=" * 40)

# 商品別売上
product_analysis = sales_detail.groupby(['商品ID', '商品名', 'カテゴリ']).agg({
    '売上': 'sum',
    '数量': 'sum',
    '取引ID': 'count'
}).round(0)
product_analysis.columns = ['総売上', '総販売数', '取引数']
product_analysis = product_analysis.sort_values('総売上', ascending=False)

print("🏆 売上TOP10商品:")
print(product_analysis.head(10))

# カテゴリ別分析
category_analysis = sales_detail.groupby('カテゴリ').agg({
    '売上': ['sum', 'mean'],
    '取引ID': 'count'
})
category_analysis.columns = ['総売上', '平均売上', '取引数']
category_analysis['売上構成比'] = (category_analysis['総売上'] / category_analysis['総売上'].sum() * 100).round(1)

print("\n📊 カテゴリ別分析:")
print(category_analysis.sort_values('総売上', ascending=False))

print("\n🔍 Step 3: 顧客分析")
print("=" * 40)

# 顧客別売上
customer_analysis = sales_detail.groupby(['顧客ID', '年齢', '性別', '会員ランク']).agg({
    '売上': 'sum',
    '取引ID': 'count'
})
customer_analysis.columns = ['総購入額', '購入回数']
customer_analysis['平均購入額'] = customer_analysis['総購入額'] / customer_analysis['購入回数']

# 顧客セグメント分析
print("👥 会員ランク別分析:")
rank_analysis = customer_analysis.groupby('会員ランク').agg({
    '総購入額': ['mean', 'sum'],
    '購入回数': 'mean'
})
rank_analysis.columns = ['平均購入額', '総売上', '平均購入回数']
print(rank_analysis.round(0))

print("\n👫 性別・年齢層別分析:")
# 年齢層の作成
customer_analysis['年齢層'] = pd.cut(customer_analysis['年齢'],
                                bins=[0, 30, 40, 50, 100],
                                labels=['20代', '30代', '40代', '50代以上'])

age_gender_analysis = customer_analysis.groupby(['性別', '年齢層'])['総購入額'].agg(['count', 'mean', 'sum'])
age_gender_analysis.columns = ['顧客数', '平均購入額', '総売上']
print(age_gender_analysis.round(0))

print("\n🔍 Step 4: 時系列分析")
print("=" * 40)

# 日別売上
daily_sales = sales_detail.groupby('日付')['売上'].sum()

# 曜日別パターン
sales_detail['曜日'] = sales_detail['日付'].dt.day_name()
weekday_pattern = sales_detail.groupby('曜日')['売上'].mean()
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_pattern = weekday_pattern.reindex(weekday_order)
weekday_pattern.index = ['月', '火', '水', '木', '金', '土', '日']

print("📅 曜日別売上パターン:")
print(weekday_pattern.round(0))

# 季節性分析
sales_detail['月'] = sales_detail['日付'].dt.month
seasonal_analysis = sales_detail.groupby('月')['売上'].sum()
seasonal_analysis.index = [f"{i}月" for i in seasonal_analysis.index]

print("\n🌸 月別売上（季節性）:")
print(seasonal_analysis)

print("\n🔍 Step 5: 改善提案")
print("=" * 40)

print("💡 分析結果に基づく改善提案:")
print("""
【売上向上施策】
1. 高収益商品の販促強化
   - 利益率の高い商品を優先的にプロモーション
   - 売上TOP10商品のクロスセル施策

2. 顧客セグメント別アプローチ
   - プラチナ会員向け限定商品の開発
   - 20-30代女性向けファッションカテゴリ強化

3. 季節性を活かした商品展開
   - 12月の年末需要に備えた在庫調整
   - 春・夏のキャンペーン時期最適化

【収益性改善】
4. 価格戦略の見直し
   - 低利益率商品の価格調整
   - 人気商品の値上げ検討

5. 在庫管理最適化
   - 売れ筋商品の欠品防止
   - 売れ行き不良商品の早期処分

【顧客満足度向上】
6. パーソナライゼーション
   - 顧客の購買履歴に基づくレコメンド
   - 会員ランク別の特典充実

7. 利便性向上
   - 週末の配送体制強化
   - モバイル購入体験の最適化
""")

print("\n📊 分析完了！")
print("🎯 この分析を参考に、データドリブンな意思決定を行いましょう！")
```

**🏆 最終課題: 完全オリジナル分析プロジェクト**

```python
print("\n🎓 卒業プロジェクト")
print("=" * 50)

print("""
🎯 最終課題: オリジナル分析プロジェクト

【課題内容】
これまで学んだpandasのスキルを総動員して、
以下のテーマから1つ選んで完全オリジナルの分析を行ってください。

【テーマ選択】
A. 架空のレストランチェーンの売上分析
B. オンライン学習プラットフォームの学習者行動分析
C. 不動産市場のトレンド分析
D. スポーツチームのパフォーマンス分析
E. 完全オリジナルテーマ

【必須要素】
✅ データ作成（現実的な問題設定）
✅ データクリーニング（欠損値・異常値処理）
✅ 基本統計と可視化
✅ groupby を使った集計分析
✅ 時系列分析（トレンド・季節性）
✅ データ結合（複数テーブル）
✅ ビジネス改善提案

【提出形式】
- Jupyter Notebook または Python スクリプト
- 分析結果のサマリー（1-2ページ）
- 改善提案（具体的なアクション含む）

【評価ポイント】
- pandas操作の正確性と効率性
- 分析の深さと洞察の質
- 可視化の分かりやすさ
- 実務に活かせる提案内容
""")

print("\n💪 頑張って取り組んでください！")
print("質問があれば、これまでのWeek 1-5の内容を参考にしてください。")

print("\n🎉 pandas DataFrame 完全マスター講座 完了！")
print("=" * 50)
print("""
おめでとうございます！🎊

あなたは以下のスキルを身につけました：
✅ DataFrameの作成と基本操作
✅ データの選択・抽出・フィルタリング
✅ データクリーニングと変換
✅ groupby による集計・分析
✅ 時系列データの操作
✅ データ可視化
✅ 実践的なビジネス分析

次のステップ：
🚀 より高度なライブラリ（scikit-learn、plotly等）の学習
🚀 機械学習への挑戦
🚀 実際のビジネス課題への適用

継続的な学習と実践で、データサイエンティストとしてのスキルを
さらに向上させていきましょう！

Happy Pandas! 🐼📊
""")
```

---

## 📚 参考資料と Next Steps

### **追加学習リソース**

1. **公式ドキュメント**

   - [pandas Documentation](https://pandas.pydata.org/docs/)
   - [pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

2. **実践的な学習**

   - Kaggle Learn の Pandas コース
   - 実際のオープンデータでの練習

3. **発展的なトピック**
   - pandas の性能最適化
   - Dask での大規模データ処理
   - pandas と SQL の連携

### **継続的な成長のために**

- **毎日の練習**: 小さなデータセットで毎日練習
- **コミュニティ参加**: Stack Overflow、pandas コミュニティ
- **プロジェクト作成**: 個人プロジェクトでスキル向上
- **最新情報**: pandas の新機能やベストプラクティス

**📈 データ分析の旅は始まったばかりです！**
**継続的な学習と実践で、より高いレベルを目指しましょう！ 🎯**
