# 🐼 pandas DataFrame 実務完全マスター講座：Advanced 版

> **対象者**: Python 基礎知識あり・実務でデータ分析を行いたい方  
> **期間**: 8 週間で実務レベルまで  
> **重点分野**: 実務データ処理（70%）+ 高度な分析手法（30%）

---

## 📋 学習ロードマップ

### 🎯 Week 1: pandas 基礎と DataFrame 完全理解

### 🎯 Week 2: インデックス操作とデータ選択の極意

### 🎯 Week 3: データクリーニングと前処理の実践

### 🎯 Week 4: 特徴量エンジニアリング（apply/lambda 活用）

### 🎯 Week 5: データ結合マスター（concat/merge 完全攻略）

### 🎯 Week 6: 集計・グループ化・時系列分析

### 🎯 Week 7: 高度な可視化と統計分析

### 🎯 Week 8: 実務プロジェクト総合演習

---

## Week 1: pandas 基礎と DataFrame 完全理解

### 🎯 **この週のゴール**

- DataFrame の内部構造を完全理解する
- メモリ効率とパフォーマンスを意識できる
- 実務レベルのデータ作成・読み込みをマスターする

---

### **Day 1-2: DataFrame の内部構造と効率的な作成**

```python
print("🏗️ pandas DataFrame 実務完全マスター講座 - Advanced版")
print("=" * 60)

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("1. DataFrameの内部構造を理解する")
print("=" * 40)

# DataFrameの基本構造
sample_data = {
    "ID": [1, 2, 3, 4, 5],
    "名前": ["田中", "佐藤", "鈴木", "高橋", "山田"],
    "年齢": [25, 30, 35, 28, 32],
    "給与": [400000, 550000, 600000, 480000, 520000],
    "部署": ["営業", "開発", "営業", "人事", "開発"]
}

df = pd.DataFrame(sample_data)
print("📊 サンプルDataFrame:")
print(df)

print("\n🔍 DataFrameの内部構造:")
print(f"形状（shape）: {df.shape}")
print(f"次元数（ndim）: {df.ndim}")
print(f"要素数（size）: {df.size}")
print(f"メモリ使用量: {df.memory_usage(deep=True).sum()} bytes")

print("\n📋 詳細な情報:")
df.info(memory_usage='deep')

print("\n💾 メモリ最適化:")
# データ型最適化前
print("最適化前のメモリ使用量:")
print(df.memory_usage(deep=True))

# 数値データの最適化
df_optimized = df.copy()
df_optimized['ID'] = df_optimized['ID'].astype('int8')  # 1-255の範囲なら
df_optimized['年齢'] = df_optimized['年齢'].astype('int8')  # 0-127の範囲なら
df_optimized['給与'] = df_optimized['給与'].astype('int32')  # 大きな数値

# カテゴリ型の活用
df_optimized['部署'] = df_optimized['部署'].astype('category')

print("\n最適化後のメモリ使用量:")
print(df_optimized.memory_usage(deep=True))

print("\nデータ型の変化:")
print(pd.DataFrame({
    '元のデータ型': df.dtypes,
    '最適化後': df_optimized.dtypes,
    '元のメモリ': df.memory_usage(deep=True),
    '最適化後メモリ': df_optimized.memory_usage(deep=True)
}))

print("\n2. 効率的なDataFrame作成方法")
print("=" * 40)

# 方法1: 大量データの効率的作成
print("📈 大量データの効率的作成:")

# 非効率な方法（避けるべき）
import time
start_time = time.time()
df_inefficient = pd.DataFrame()
for i in range(1000):
    new_row = pd.DataFrame({'値': [i]})
    df_inefficient = pd.concat([df_inefficient, new_row], ignore_index=True)
inefficient_time = time.time() - start_time

# 効率的な方法
start_time = time.time()
data_list = [{'値': i} for i in range(1000)]
df_efficient = pd.DataFrame(data_list)
efficient_time = time.time() - start_time

print(f"非効率な方法: {inefficient_time:.4f}秒")
print(f"効率的な方法: {efficient_time:.4f}秒")
print(f"速度改善: {inefficient_time/efficient_time:.1f}倍高速")

# 方法2: NumPy配列からの作成（最速）
print("\n⚡ NumPy配列からの作成:")
np.random.seed(42)

start_time = time.time()
# 100万行のデータ
large_data = {
    'A': np.random.randint(1, 100, 1000000),
    'B': np.random.normal(50, 15, 1000000),
    'C': np.random.choice(['X', 'Y', 'Z'], 1000000)
}
df_large = pd.DataFrame(large_data)
numpy_time = time.time() - start_time

print(f"100万行データ作成時間: {numpy_time:.4f}秒")
print(f"メモリ使用量: {df_large.memory_usage(deep=True).sum() / 1024**2:.1f} MB")

print("\n3. 実務的なデータ読み込み")
print("=" * 40)

# CSV読み込みの最適化
print("📁 CSV読み込みの最適化:")

# サンプルCSVデータを作成
sample_csv_data = {
    'date': pd.date_range('2024-01-01', periods=10000, freq='H'),
    'value1': np.random.normal(100, 20, 10000),
    'value2': np.random.randint(1, 1000, 10000),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 10000),
    'flag': np.random.choice([True, False], 10000)
}
sample_df = pd.DataFrame(sample_csv_data)

# CSV保存
sample_df.to_csv('sample_data.csv', index=False)

print("🔧 読み込み最適化のテクニック:")

# 基本的な読み込み
basic_df = pd.read_csv('sample_data.csv')
print(f"基本読み込み: {basic_df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")

# 最適化された読み込み
optimized_df = pd.read_csv(
    'sample_data.csv',
    dtype={
        'value2': 'int16',  # データ型を指定
        'category': 'category',  # カテゴリ型で読み込み
        'flag': 'bool'
    },
    parse_dates=['date'],  # 日付型として解析
    chunksize=None  # チャンク読み込みも可能
)
print(f"最適化読み込み: {optimized_df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")

# 必要な列のみ読み込み
selected_df = pd.read_csv('sample_data.csv', usecols=['date', 'value1', 'category'])
print(f"選択読み込み: {selected_df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")

print("\n4. 高度なDataFrame操作")
print("=" * 40)

# チェーンメソッド（Method Chaining）
print("🔗 メソッドチェーンの活用:")

result = (df
    .assign(
        年齢カテゴリ=lambda x: pd.cut(x['年齢'], bins=[0, 30, 40, 100],
                               labels=['若手', '中堅', 'ベテラン']),
        給与レベル=lambda x: pd.qcut(x['給与'], q=3, labels=['低', '中', '高'])
    )
    .query('年齢 >= 25')
    .sort_values('給与', ascending=False)
    .reset_index(drop=True)
)

print("メソッドチェーン結果:")
print(result)

# パイプライン処理
print("\n🔀 パイプライン処理:")

def add_bonus(df):
    """ボーナス列を追加"""
    df = df.copy()
    df['ボーナス'] = df['給与'] * 2.5
    return df

def add_total_compensation(df):
    """年収を計算"""
    df = df.copy()
    df['年収'] = (df['給与'] * 12) + df['ボーナス']
    return df

pipeline_result = (df
    .pipe(add_bonus)
    .pipe(add_total_compensation)
    .round(0)
)

print("パイプライン処理結果:")
print(pipeline_result[['名前', '給与', 'ボーナス', '年収']])

print("\n5. エラーハンドリングとデバッグ")
print("=" * 40)

# 一般的なエラーと対処法
print("⚠️ よくあるエラーと対処法:")

# KeyError対策
try:
    value = df['存在しない列']
except KeyError as e:
    print(f"KeyError発生: {e}")
    print("対処法: 列の存在確認")
    if '存在しない列' in df.columns:
        value = df['存在しない列']
    else:
        print("列が存在しません。利用可能な列:", df.columns.tolist())

# データ型エラー対策
try:
    result = df['名前'] + df['年齢']  # 文字列 + 数値
except TypeError as e:
    print(f"\nTypeError発生: 文字列と数値を結合しようとしました")
    print("対処法: データ型を統一")
    result = df['名前'] + df['年齢'].astype(str) + "歳"
    print("修正結果:", result.tolist())

# 欠損値エラー対策
df_with_na = df.copy()
df_with_na.loc[2, '年齢'] = np.nan

print(f"\n欠損値を含むデータでの計算:")
print(f"平均年齢: {df_with_na['年齢'].mean():.1f}")  # 欠損値は自動で除外
print(f"欠損値の個数: {df_with_na['年齢'].isna().sum()}")

print("\n✅ Week 1 完了：DataFrameの基礎を完全理解しました！")
```

---

## Week 2: インデックス操作とデータ選択の極意

### 🎯 **この週のゴール**

- インデックスの概念を完全理解する
- 階層インデックスを自在に操る
- 高速なデータ選択テクニックをマスターする

---

### **Day 1-3: インデックスの完全理解**

```python
print("\n📇 Week 2: インデックス操作とデータ選択の極意")
print("=" * 50)

print("1. インデックスとは何か？")
print("=" * 30)

# インデックスの基本概念
df = pd.DataFrame({
    '商品名': ['りんご', 'バナナ', 'オレンジ', 'ぶどう'],
    '価格': [100, 80, 120, 200],
    '在庫': [50, 30, 25, 15]
})

print("📊 デフォルトインデックス:")
print(df)
print(f"\nインデックス: {df.index}")
print(f"インデックスの型: {type(df.index)}")
print(f"インデックスの名前: {df.index.name}")

print("\n🔍 インデックスの詳細:")
print(f"インデックスの値: {df.index.tolist()}")
print(f"インデックスのデータ型: {df.index.dtype}")
print(f"インデックスの長さ: {len(df.index)}")
print(f"インデックスは一意か: {df.index.is_unique}")

print("\n📋 カラムについて:")
print(f"カラム: {df.columns}")
print(f"カラムの型: {type(df.columns)}")
print(f"カラム数: {len(df.columns)}")

print("\n2. インデックスの設定と操作")
print("=" * 30)

# インデックスの設定
print("🔧 インデックスの設定方法:")

# 方法1: set_indexで既存列をインデックスに
df_indexed = df.set_index('商品名')
print("商品名をインデックスに設定:")
print(df_indexed)
print(f"新しいインデックス: {df_indexed.index}")

# 方法2: インデックスを直接指定
df_custom = df.copy()
df_custom.index = ['果物1', '果物2', '果物3', '果物4']
print("\nカスタムインデックス:")
print(df_custom)

# 方法3: 作成時にインデックス指定
df_with_index = pd.DataFrame({
    '価格': [100, 80, 120, 200],
    '在庫': [50, 30, 25, 15]
}, index=['りんご', 'バナナ', 'オレンジ', 'ぶどう'])
print("\n作成時にインデックス指定:")
print(df_with_index)

print("\n🔄 インデックスの操作:")

# インデックスのリセット
df_reset = df_indexed.reset_index()
print("インデックスをリセット:")
print(df_reset)

# インデックス名の設定
df_named = df_indexed.copy()
df_named.index.name = '商品'
print("\nインデックスに名前を設定:")
print(df_named)

# インデックスの変更
df_renamed = df_indexed.rename(index={'りんご': 'アップル', 'バナナ': 'バナーナ'})
print("\nインデックスの名前変更:")
print(df_renamed)

print("\n3. 階層インデックス（MultiIndex）")
print("=" * 30)

# 階層インデックスの作成
print("🏗️ 階層インデックスの作成:")

# 売上データで階層インデックス
sales_data = {
    '売上': [100, 120, 80, 90, 150, 130, 110, 140],
    '利益': [30, 36, 24, 27, 45, 39, 33, 42]
}

# 2階層のインデックス
multi_index = pd.MultiIndex.from_tuples([
    ('東京', '新宿店'),
    ('東京', '渋谷店'),
    ('東京', '池袋店'),
    ('大阪', '梅田店'),
    ('大阪', '難波店'),
    ('大阪', '天王寺店'),
    ('名古屋', '栄店'),
    ('名古屋', '名駅店')
], names=['地域', '店舗'])

df_multi = pd.DataFrame(sales_data, index=multi_index)
print("階層インデックスデータ:")
print(df_multi)

print(f"\nインデックスレベル数: {df_multi.index.nlevels}")
print(f"レベル名: {df_multi.index.names}")
print(f"レベル0の値: {df_multi.index.get_level_values(0).unique()}")
print(f"レベル1の値: {df_multi.index.get_level_values(1).unique()}")

print("\n🎯 階層インデックスでの選択:")

# レベル0での選択
print("東京の店舗:")
print(df_multi.loc['東京'])

# 特定の店舗
print("\n新宿店のデータ:")
print(df_multi.loc[('東京', '新宿店')])

# レベルごとの集計
print("\n地域別合計:")
print(df_multi.groupby(level=0).sum())

# 階層の入れ替え
df_swapped = df_multi.swaplevel()
print("\n階層を入れ替え:")
print(df_swapped.head())

# インデックスの並び替え
df_sorted = df_multi.sort_index()
print("\nインデックスで並び替え:")
print(df_sorted)

print("\n4. 高速なデータ選択テクニック")
print("=" * 30)

# 大きなデータセットで性能比較
print("⚡ 性能比較（大きなデータセット）:")

# 大きなデータセット作成
np.random.seed(42)
large_df = pd.DataFrame({
    'A': np.random.randint(1, 1000, 100000),
    'B': np.random.normal(0, 1, 100000),
    'C': np.random.choice(['X', 'Y', 'Z'], 100000)
})

import time

# 方法1: boolean indexing
start = time.time()
result1 = large_df[large_df['A'] > 500]
time1 = time.time() - start

# 方法2: query method
start = time.time()
result2 = large_df.query('A > 500')
time2 = time.time() - start

print(f"Boolean indexing: {time1:.4f}秒")
print(f"Query method: {time2:.4f}秒")

# インデックス設定後の高速選択
large_df_indexed = large_df.set_index('A').sort_index()

start = time.time()
result3 = large_df_indexed.loc[500:1000]  # インデックス範囲選択
time3 = time.time() - start

print(f"インデックス範囲選択: {time3:.4f}秒")

print("\n🔎 高度な選択方法:")

# isin を使った効率的な選択
categories = ['X', 'Y']
start = time.time()
result_isin = large_df[large_df['C'].isin(categories)]
time_isin = time.time() - start

# 複数条件での選択（効率的）
start = time.time()
result_multiple = large_df.query('A > 500 and C in @categories')
time_multiple = time.time() - start

print(f"isin選択: {time_isin:.4f}秒")
print(f"複数条件query: {time_multiple:.4f}秒")

print("\n5. インデックスのベストプラクティス")
print("=" * 30)

print("💡 インデックス活用のベストプラクティス:")

# 1. 検索が多い列をインデックスに
print("1. よく検索する列をインデックスに設定")
customer_df = pd.DataFrame({
    'customer_id': range(1000, 2000),
    'name': [f'Customer{i}' for i in range(1000)],
    'purchase_amount': np.random.randint(100, 10000, 1000)
})

# customer_idでよく検索する場合
customer_indexed = customer_df.set_index('customer_id')
print("顧客ID1500の情報:", customer_indexed.loc[1500, 'name'])

# 2. 日付データは必ずDatetimeIndexに
print("\n2. 日付データはDatetimeIndexを使用")
date_df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=365, freq='D'),
    'sales': np.random.randint(10000, 50000, 365)
})
date_df = date_df.set_index('date')

# 日付範囲での高速選択
q1_sales = date_df.loc['2024-01':'2024-03']
print(f"Q1の売上データ: {len(q1_sales)}日分")

# 3. カテゴリデータでの効率的な処理
print("\n3. カテゴリデータの効率的処理")
category_df = pd.DataFrame({
    'product_category': pd.Categorical(['Electronics', 'Clothing', 'Books'] * 1000),
    'sales': np.random.randint(100, 1000, 3000)
})

# カテゴリごとの集計（高速）
category_summary = category_df.groupby('product_category').agg({
    'sales': ['sum', 'mean', 'count']
})
print("カテゴリ別売上サマリー:")
print(category_summary)

print("\n✅ Week 2 完了：インデックス操作をマスターしました！")
```

### **Day 4-7: 高度なデータ選択とフィルタリング**

```python
print("\n6. 高度なフィルタリングテクニック")
print("=" * 30)

# 複雑な条件でのフィルタリング
sales_df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=1000, freq='D'),
    'product': np.random.choice(['A', 'B', 'C', 'D'], 1000),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 1000),
    'sales': np.random.normal(1000, 300, 1000),
    'profit': np.random.normal(200, 100, 1000)
})

print("🎯 複雑な条件フィルタリング:")

# 1. 統計的条件
print("1. 統計的フィルタリング:")
high_sales = sales_df[sales_df['sales'] > sales_df['sales'].quantile(0.9)]
print(f"上位10%の売上: {len(high_sales)}件")

# 2. 複数列の条件組み合わせ
print("\n2. 複数列条件組み合わせ:")
complex_filter = sales_df[
    (sales_df['sales'] > 1200) &
    (sales_df['profit'] > 150) &
    (sales_df['region'].isin(['North', 'East']))
]
print(f"複合条件に合致: {len(complex_filter)}件")

# 3. 文字列パターンマッチング
print("\n3. 高度な文字列マッチング:")
product_df = pd.DataFrame({
    'product_name': ['iPhone_14', 'Samsung_Galaxy', 'iPad_Pro', 'MacBook_Air', 'Surface_Pro'],
    'brand': ['Apple', 'Samsung', 'Apple', 'Apple', 'Microsoft'],
    'price': [80000, 70000, 90000, 120000, 110000]
})

# 正規表現を使った選択
apple_products = product_df[product_df['product_name'].str.contains(r'iPhone|iPad|MacBook')]
print("Apple製品:")
print(apple_products)

# 価格範囲での選択
mid_range = product_df[product_df['price'].between(70000, 100000)]
print("\n価格70,000-100,000円の商品:")
print(mid_range)

print("\n7. 動的なデータ選択")
print("=" * 30)

# 動的フィルタリング関数
def dynamic_filter(df, conditions):
    """
    動的にフィルタリング条件を適用

    Parameters:
    df: DataFrame
    conditions: dict of conditions
    """
    result = df.copy()

    for column, condition in conditions.items():
        if isinstance(condition, dict):
            if 'min' in condition:
                result = result[result[column] >= condition['min']]
            if 'max' in condition:
                result = result[result[column] <= condition['max']]
            if 'values' in condition:
                result = result[result[column].isin(condition['values'])]
        else:
            result = result[result[column] == condition]

    return result

# 使用例
filter_conditions = {
    'sales': {'min': 800, 'max': 1500},
    'region': {'values': ['North', 'South']},
    'product': 'A'
}

filtered_data = dynamic_filter(sales_df, filter_conditions)
print(f"動的フィルタ結果: {len(filtered_data)}件")

print("\n8. パフォーマンス最適化テクニック")
print("=" * 30)

# データ型最適化による高速化
print("⚡ データ型最適化:")

# 最適化前
large_sales = pd.DataFrame({
    'product_id': np.random.randint(1, 1000, 100000),
    'quantity': np.random.randint(1, 100, 100000),
    'price': np.random.uniform(10, 1000, 100000),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 100000)
})

print(f"最適化前メモリ: {large_sales.memory_usage(deep=True).sum() / 1024**2:.1f}MB")

# 最適化後
large_sales_opt = large_sales.copy()
large_sales_opt['product_id'] = large_sales_opt['product_id'].astype('int16')
large_sales_opt['quantity'] = large_sales_opt['quantity'].astype('int8')
large_sales_opt['price'] = large_sales_opt['price'].astype('float32')
large_sales_opt['category'] = large_sales_opt['category'].astype('category')

print(f"最適化後メモリ: {large_sales_opt.memory_usage(deep=True).sum() / 1024**2:.1f}MB")

# フィルタリング速度比較
start = time.time()
result_orig = large_sales[large_sales['category'] == 'A']
time_orig = time.time() - start

start = time.time()
result_opt = large_sales_opt[large_sales_opt['category'] == 'A']
time_opt = time.time() - start

print(f"フィルタリング時間 - 最適化前: {time_orig:.4f}秒")
print(f"フィルタリング時間 - 最適化後: {time_opt:.4f}秒")

print("\n✅ Week 2 完了：高度なデータ選択をマスターしました！")
```

---

## Week 3: データクリーニングと前処理の実践

### 🎯 **この週のゴール**

- 実務レベルのデータクリーニングをマスターする
- 様々なデータ品質問題に対処できる
- 自動化されたクリーニングパイプラインを構築する

---

### **Day 1-3: 欠損値処理の完全攻略**

```python
print("\n🧹 Week 3: データクリーニングと前処理の実践")
print("=" * 50)

print("1. 実務における欠損値パターンの理解")
print("=" * 40)

# 実際のビジネスデータを模擬
np.random.seed(42)

# 複雑な欠損パターンを持つデータ作成
customer_data = []
for i in range(1000):
    # 基本情報
    customer_id = f"C{i+1:04d}"
    age = np.random.randint(18, 80)

    # 年収（高齢者は退職で未回答多い）
    if age > 65:
        income = np.nan if np.random.random() > 0.3 else np.random.randint(0, 300)
    else:
        income = np.random.randint(200, 1000) if np.random.random() > 0.1 else np.nan

    # 電話番号（若い世代は固定電話なし）
    if age < 30:
        phone = "" if np.random.random() > 0.2 else f"03-{np.random.randint(1000,9999)}-{np.random.randint(1000,9999)}"
    else:
        phone = f"03-{np.random.randint(1000,9999)}-{np.random.randint(1000,9999)}" if np.random.random() > 0.05 else ""

    # 購入履歴（新規顧客は購入履歴なし）
    days_since_reg = np.random.randint(1, 1000)
    if days_since_reg < 30:
        last_purchase = np.nan
        total_purchases = 0
    else:
        last_purchase = pd.Timestamp('2024-01-01') - pd.Timedelta(days=np.random.randint(1, days_since_reg))
        total_purchases = np.random.randint(1, 50)

    customer_data.append({
        'customer_id': customer_id,
        'age': age,
        'income': income,
        'phone': phone,
        'registration_date': pd.Timestamp('2024-01-01') - pd.Timedelta(days=days_since_reg),
        'last_purchase_date': last_purchase,
        'total_purchases': total_purchases,
        'preferred_category': np.random.choice(['Fashion', 'Electronics', 'Books', '', 'Sports'],
                                            p=[0.25, 0.25, 0.15, 0.1, 0.25])
    })

df_customers = pd.DataFrame(customer_data)

print("📊 実務データの欠損値パターン:")
print(df_customers.head())

print("\n🔍 欠損値の詳細分析:")
missing_analysis = pd.DataFrame({
    '欠損数': df_customers.isnull().sum(),
    '欠損率(%)': (df_customers.isnull().sum() / len(df_customers) * 100).round(2),
    'データ型': df_customers.dtypes
})
print(missing_analysis)

# 欠損値のパターン分析
print("\n📈 欠損値パターンの可視化:")
import matplotlib.pyplot as plt

# 欠損値の組み合わせパターン
missing_patterns = df_customers.isnull()
pattern_counts = missing_patterns.groupby(list(missing_patterns.columns)).size().sort_values(ascending=False)
print("主要な欠損パターン（上位5）:")
print(pattern_counts.head())

print("\n2. 欠損値の種類と対処法")
print("=" * 40)

print("💡 欠損値の分類と戦略:")

# MCAR (Missing Completely At Random) - 完全にランダム
print("1. MCAR（完全ランダム欠損）:")
# 例：システムエラーで一部データが欠損
mcar_example = df_customers.copy()
random_missing = np.random.choice(df_customers.index, 50, replace=False)
mcar_example.loc[random_missing, 'total_purchases'] = np.nan
print(f"ランダム欠損を追加: {mcar_example['total_purchases'].isnull().sum()}件")

# MAR (Missing At Random) - 他の変数に依存した欠損
print("\n2. MAR（他変数依存欠損）:")
# 例：高齢者の年収未回答（年齢に依存）
mar_analysis = df_customers.groupby(pd.cut(df_customers['age'], bins=[0, 30, 50, 65, 100]))['income'].apply(
    lambda x: x.isnull().sum() / len(x) * 100
)
print("年齢層別年収欠損率:")
print(mar_analysis.round(2))

# MNAR (Missing Not At Random) - 欠損値自体に意味がある
print("\n3. MNAR（非ランダム欠損）:")
# 例：高収入者の年収未回答（プライバシー重視）
high_income_mask = df_customers['income'] > 800
print(f"高収入者の年収回答率: {((~df_customers.loc[high_income_mask, 'income'].isnull()).sum() / high_income_mask.sum() * 100):.1f}%")

print("\n3. 高度な欠損値補完手法")
print("=" * 40)

# 準備：作業用データフレーム
df_impute = df_customers.copy()

print("🔧 補完手法の実装:")

# 1. 基本統計による補完
print("1. 基本統計補完:")
# 年齢層別の年収中央値で補完
age_groups = pd.cut(df_impute['age'], bins=[0, 30, 50, 65, 100], labels=['20代', '30-40代', '50-60代', '60代以上'])
income_by_age = df_impute.groupby(age_groups)['income'].median()

def fill_income_by_age(row):
    if pd.isna(row['income']):
        age_group = pd.cut([row['age']], bins=[0, 30, 50, 65, 100], labels=['20代', '30-40代', '50-60代', '60代以上'])[0]
        return income_by_age[age_group]
    return row['income']

df_impute['income_filled'] = df_impute.apply(fill_income_by_age, axis=1)
print("年齢層別年収中央値で補完完了")

# 2. 前方・後方補完（時系列データ）
print("\n2. 時系列補完:")
df_sorted = df_impute.sort_values('registration_date')
df_sorted['income_ffill'] = df_sorted['income'].fillna(method='ffill')
df_sorted['income_bfill'] = df_sorted['income'].fillna(method='bfill')
print("前方・後方補完完了")

# 3. 補間法
print("\n3. 補間法:")
df_sorted['income_interpolate'] = df_sorted['income'].interpolate(method='linear')
print("線形補間完了")

# 4. 機械学習による補完（簡易版）
print("\n4. 予測モデル補完:")
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# 年収予測のための特徴量準備
features_df = df_impute[['age', 'total_purchases']].copy()
features_df['days_since_reg'] = (pd.Timestamp('2024-01-01') - df_impute['registration_date']).dt.days

# 年収データがある行で学習
complete_mask = ~df_impute['income'].isnull()
X_train = features_df[complete_mask]
y_train = df_impute.loc[complete_mask, 'income']

# モデル学習
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 欠損値予測
missing_mask = df_impute['income'].isnull()
X_missing = features_df[missing_mask]
predicted_income = rf_model.predict(X_missing)

df_impute.loc[missing_mask, 'income_predicted'] = predicted_income
print("ランダムフォレストによる予測補完完了")

# 補完結果の比較
print("\n📊 補完手法の比較:")
comparison_df = pd.DataFrame({
    '元データ': df_impute['income'],
    '年齢層別中央値': df_impute['income_filled'],
    'RF予測': df_impute.get('income_predicted', np.nan)
}).fillna('欠損')

print(comparison_df.head(10))

print("\n4. データ品質評価")
print("=" * 40)

def data_quality_report(df, target_col):
    """データ品質レポート作成"""
    report = {}

    # 基本統計
    report['total_records'] = len(df)
    report['missing_count'] = df[target_col].isnull().sum()
    report['missing_rate'] = report['missing_count'] / report['total_records'] * 100

    # 有効データの統計
    valid_data = df[target_col].dropna()
    if len(valid_data) > 0:
        report['mean'] = valid_data.mean()
        report['median'] = valid_data.median()
        report['std'] = valid_data.std()
        report['min'] = valid_data.min()
        report['max'] = valid_data.max()

    return report

# 各補完手法の品質評価
original_quality = data_quality_report(df_impute, 'income')
filled_quality = data_quality_report(df_impute, 'income_filled')

print("📋 品質レポート:")
print(f"元データ欠損率: {original_quality['missing_rate']:.2f}%")
print(f"補完後欠損率: {filled_quality['missing_rate']:.2f}%")
print(f"元データ平均: {original_quality.get('mean', 'N/A')}")
print(f"補完後平均: {filled_quality.get('mean', 'N/A')}")

print("\n✅ Week 3 Day 1-3 完了：欠損値処理をマスターしました！")
```

### **Day 4-7: データ異常値検出と文字列クリーニング**

```python
print("\n5. 異常値検出と処理")
print("=" * 40)

# 異常値を含むデータセット作成
np.random.seed(42)
sales_data = []

for i in range(1000):
    # 通常の売上データ
    if np.random.random() > 0.05:  # 95%は正常データ
        sales = np.random.normal(10000, 2000)
        if sales < 0:
            sales = abs(sales)  # 負の売上は絶対値に
    else:  # 5%は異常値
        if np.random.random() > 0.5:
            sales = np.random.normal(50000, 5000)  # 異常に高い売上
        else:
            sales = np.random.uniform(0, 100)  # 異常に低い売上

    sales_data.append({
        'date': pd.Timestamp('2024-01-01') + pd.Timedelta(days=np.random.randint(0, 365)),
        'store_id': np.random.choice(['S001', 'S002', 'S003', 'S004'], p=[0.4, 0.3, 0.2, 0.1]),
        'sales': sales,
        'customer_count': max(1, int(sales / 500 + np.random.normal(0, 5)))
    })

sales_df = pd.DataFrame(sales_data)

print("📊 売上データ（異常値含む）:")
print(sales_df.describe())

print("\n🔍 異常値検出手法:")

# 1. 統計的手法（IQR法）
def detect_outliers_iqr(df, column):
    """IQR法による異常値検出"""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers, (lower_bound, upper_bound)

outliers_iqr, bounds_iqr = detect_outliers_iqr(sales_df, 'sales')
print(f"1. IQR法検出異常値: {len(outliers_iqr)}件")
print(f"   正常範囲: {bounds_iqr[0]:.0f} - {bounds_iqr[1]:.0f}")

# 2. Z-score法
def detect_outliers_zscore(df, column, threshold=3):
    """Z-score法による異常値検出"""
    z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
    outliers = df[z_scores > threshold]
    return outliers

outliers_zscore = detect_outliers_zscore(sales_df, 'sales')
print(f"2. Z-score法検出異常値: {len(outliers_zscore)}件")

# 3. 修正Z-score法（MAD使用）
def detect_outliers_modified_zscore(df, column, threshold=3.5):
    """修正Z-score法（MAD使用）"""
    median = df[column].median()
    mad = np.median(np.abs(df[column] - median))
    modified_z_scores = 0.6745 * (df[column] - median) / mad
    outliers = df[np.abs(modified_z_scores) > threshold]
    return outliers

outliers_mad = detect_outliers_modified_zscore(sales_df, 'sales')
print(f"3. 修正Z-score法検出異常値: {len(outliers_mad)}件")

# 4. 機械学習手法（Isolation Forest）
from sklearn.ensemble import IsolationForest

isolation_forest = IsolationForest(contamination=0.1, random_state=42)
outlier_labels = isolation_forest.fit_predict(sales_df[['sales', 'customer_count']])
outliers_if = sales_df[outlier_labels == -1]
print(f"4. Isolation Forest検出異常値: {len(outliers_if)}件")

print("\n🛠️ 異常値の処理方法:")

# 処理方法1: 削除
sales_cleaned_drop = sales_df[~sales_df.index.isin(outliers_iqr.index)]
print(f"削除処理後: {len(sales_cleaned_drop)}件（{len(sales_df) - len(sales_cleaned_drop)}件削除）")

# 処理方法2: キャッピング（上下限値で置換）
sales_cleaned_cap = sales_df.copy()
sales_cleaned_cap['sales'] = sales_cleaned_cap['sales'].clip(lower=bounds_iqr[0], upper=bounds_iqr[1])
print(f"キャッピング処理: 下限{bounds_iqr[0]:.0f}, 上限{bounds_iqr[1]:.0f}")

# 処理方法3: 変換（対数変換）
sales_cleaned_log = sales_df.copy()
sales_cleaned_log['sales_log'] = np.log1p(sales_cleaned_log['sales'])  # log1p = log(1+x)
print("対数変換処理完了")

print("\n6. 高度な文字列クリーニング")
print("=" * 40)

# 実務的な汚れた文字列データ
messy_data = {
    'customer_name': [
        '田中　太郎', '  佐藤花子  ', 'SUZUKI Jiro', 'たかはし　みさき',
        '山田一郎　　', '中村　健太', 'Tanaka Hanako', '鈴木　次郎',
        '', None, '田中（太郎）', '佐藤-花子'
    ],
    'email': [
        'tanaka@email.com', 'SATO@EMAIL.COM', 'suzuki@gmail', 'takahashi@',
        '', 'yamada@@email.com', 'nakamura@email.com.', 'tanaka@email',
        'hanako.tanaka@company.co.jp', None, 'invalid-email', 'test@test.test'
    ],
    'phone': [
        '090-1234-5678', '03(1234)5678', '0312345678', '090 1234 5678',
        '090-1234-567', '090-1234-56789', '', '03-1234-5678',
        '81-90-1234-5678', '+81-90-1234-5678', 'invalid', None
    ],
    'address': [
        '東京都新宿区1-2-3', '大阪府大阪市北区４－５－６', '愛知県名古屋市',
        '〒100-0001 東京都千代田区', '神奈川県横浜市港北区新横浜２－５－８',
        '', '福岡県福岡市博多区', '北海道札幌市中央区',
        '沖縄県那覇市', '東京都　新宿区　　１－２－３', None, '無効な住所'
    ]
}

messy_df = pd.DataFrame(messy_data)
print("📋 汚れた文字列データ:")
print(messy_df)

print("\n🧽 文字列クリーニング処理:")

# 1. 基本的なクリーニング
def clean_name(name):
    """名前のクリーニング"""
    if pd.isna(name) or name == '':
        return None

    # 前後の空白削除
    name = str(name).strip()

    # 全角空白を半角に
    name = name.replace('　', ' ')

    # 複数の空白を1つに
    import re
    name = re.sub(r'\s+', ' ', name)

    # 括弧などの除去
    name = re.sub(r'[（）()【】\[\]－-]', '', name)

    return name if name else None

messy_df['customer_name_clean'] = messy_df['customer_name'].apply(clean_name)

# 2. メールアドレスの検証とクリーニング
def clean_email(email):
    """メールアドレスのクリーニングと検証"""
    if pd.isna(email) or email == '':
        return None

    email = str(email).strip().lower()

    # 基本的なメールアドレス形式チェック
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # 一般的な修正
    email = email.replace('@@', '@')  # 重複@の修正
    email = re.sub(r'\.+$', '', email)  # 末尾のピリオド削除

    if re.match(pattern, email):
        return email
    else:
        return None

messy_df['email_clean'] = messy_df['email'].apply(clean_email)

# 3. 電話番号の正規化
def clean_phone(phone):
    """電話番号のクリーニングと正規化"""
    if pd.isna(phone) or phone == '':
        return None

    phone = str(phone).strip()

    # 数字のみ抽出
    import re
    digits = re.sub(r'[^\d]', '', phone)

    # 国際番号の処理
    if digits.startswith('81'):
        digits = digits[2:]

    # 長さチェック
    if len(digits) == 10:  # 固定電話
        return f"{digits[:2]}-{digits[2:6]}-{digits[6:]}"
    elif len(digits) == 11:  # 携帯電話
        return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
    else:
        return None

messy_df['phone_clean'] = messy_df['phone'].apply(clean_phone)

# 4. 住所のクリーニング
def clean_address(address):
    """住所のクリーニング"""
    if pd.isna(address) or address == '':
        return None

    address = str(address).strip()

    # 郵便番号の除去
    import re
    address = re.sub(r'〒?\d{3}-?\d{4}\s*', '', address)

    # 全角数字を半角に
    address = address.translate(str.maketrans('０１２３４５６７８９', '0123456789'))

    # 空白の正規化
    address = re.sub(r'\s+', '', address)

    # 基本的な住所形式チェック
    if any(pref in address for pref in ['都', '府', '県']) and any(city in address for city in ['市', '区', '町', '村']):
        return address
    else:
        return None

messy_df['address_clean'] = messy_df['address'].apply(clean_address)

print("🔍 クリーニング結果:")
comparison_cols = ['customer_name', 'customer_name_clean', 'email', 'email_clean']
print(messy_df[comparison_cols].head())

print("\n📊 クリーニング効果:")
for col in ['customer_name', 'email', 'phone', 'address']:
    original_valid = messy_df[col].notna().sum()
    clean_valid = messy_df[f'{col}_clean'].notna().sum()
    print(f"{col}: {original_valid} → {clean_valid} (有効率: {clean_valid/len(messy_df)*100:.1f}%)")

print("\n7. 自動クリーニングパイプライン")
print("=" * 40)

class DataCleaner:
    """自動データクリーニングパイプライン"""

    def __init__(self):
        self.cleaning_log = []

    def clean_dataframe(self, df):
        """DataFrameの自動クリーニング"""
        df_clean = df.copy()

        for column in df_clean.columns:
            if df_clean[column].dtype == 'object':
                df_clean[column] = self._clean_text_column(df_clean[column], column)
            elif df_clean[column].dtype in ['int64', 'float64']:
                df_clean[column] = self._clean_numeric_column(df_clean[column], column)

        return df_clean

    def _clean_text_column(self, series, column_name):
        """テキスト列のクリーニング"""
        original_nulls = series.isnull().sum()

        # 基本的なクリーニング
        cleaned = series.str.strip()
        cleaned = cleaned.replace('', np.nan)

        # 空白の正規化
        cleaned = cleaned.str.replace(r'\s+', ' ', regex=True)

        new_nulls = cleaned.isnull().sum()
        self.cleaning_log.append(f"{column_name}: {original_nulls} → {new_nulls} null値")

        return cleaned

    def _clean_numeric_column(self, series, column_name):
        """数値列のクリーニング"""
        original_nulls = series.isnull().sum()

        # 異常値検出（IQR法）
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # 異常値をNaNに
        cleaned = series.copy()
        outlier_mask = (series < lower_bound) | (series > upper_bound)
        cleaned[outlier_mask] = np.nan

        outlier_count = outlier_mask.sum()
        new_nulls = cleaned.isnull().sum()

        self.cleaning_log.append(f"{column_name}: {outlier_count}個の異常値を検出, {original_nulls} → {new_nulls} null値")

        return cleaned

    def get_cleaning_report(self):
        """クリーニングレポートを取得"""
        return "\n".join(self.cleaning_log)

# パイプライン使用例
cleaner = DataCleaner()
sales_cleaned = cleaner.clean_dataframe(sales_df)

print("🤖 自動クリーニング結果:")
print(cleaner.get_cleaning_report())

print("\n✅ Week 3 完了：データクリーニングをマスターしました！")
```

---

## Week 4: 特徴量エンジニアリング（apply/lambda 活用）

### 🎯 **この週のゴール**

- apply()と lambda 式を完全理解する
- 実務的な特徴量作成テクニックをマスターする
- 高度な変換処理を効率的に実装する

---

### **Day 1-4: apply()と lambda 式の完全攻略**

```python
print("\n🔧 Week 4: 特徴量エンジニアリング（apply/lambda活用）")
print("=" * 50)

print("1. apply()とlambda式の基本概念")
print("=" * 40)

# サンプルデータの準備
customer_data = pd.DataFrame({
    'customer_id': range(1, 1001),
    'age': np.random.randint(18, 80, 1000),
    'income': np.random.normal(50000, 20000, 1000),
    'purchase_amount': np.random.exponential(1000, 1000),
    'purchase_frequency': np.random.poisson(5, 1000),
    'registration_date': pd.date_range('2020-01-01', periods=1000, freq='D'),
    'last_login': pd.date_range('2024-01-01', periods=1000, freq='H'),
    'product_category': np.random.choice(['Electronics', 'Fashion', 'Books', 'Sports'], 1000)
})

print("📊 顧客データサンプル:")
print(customer_data.head())

print("\n🎯 apply()の基本パターン:")

# 1. 単一列に対するapply（Series.apply）
print("1. Series.apply() - 単一列変換:")

# シンプルなlambda式
customer_data['age_category'] = customer_data['age'].apply(lambda x: 'Young' if x < 30 else 'Middle' if x < 50 else 'Senior')
print("年齢カテゴリ作成:")
print(customer_data[['age', 'age_category']].head())

# より複雑な関数
def income_level(income):
    """収入レベルの分類"""
    if income < 30000:
        return 'Low'
    elif income < 70000:
        return 'Medium'
    else:
        return 'High'

customer_data['income_level'] = customer_data['income'].apply(income_level)
print("\n収入レベル分類:")
print(customer_data[['income', 'income_level']].head())

# 2. 複数列に対するapply（DataFrame.apply）
print("\n2. DataFrame.apply() - 複数列使用:")

# axis=1で行方向に適用
def customer_score(row):
    """顧客スコア計算"""
    age_score = 100 - row['age']  # 若いほど高スコア
    income_score = row['income'] / 1000  # 収入を1000で割る
    frequency_score = row['purchase_frequency'] * 10
    return age_score + income_score + frequency_score

customer_data['customer_score'] = customer_data.apply(customer_score, axis=1)
print("顧客スコア計算:")
print(customer_data[['age', 'income', 'purchase_frequency', 'customer_score']].head())

# lambda式での複数列使用
customer_data['purchase_per_freq'] = customer_data.apply(
    lambda row: row['purchase_amount'] / max(row['purchase_frequency'], 1), axis=1
)
print("\n購入頻度あたりの金額:")
print(customer_data[['purchase_amount', 'purchase_frequency', 'purchase_per_freq']].head())

print("\n3. 高度なapply()活用パターン")
print("=" * 40)

# 3. 条件分岐を含む複雑な処理
def customer_segment(row):
    """顧客セグメント分類"""
    age = row['age']
    income = row['income']
    frequency = row['purchase_frequency']

    if age < 30:
        if income > 50000:
            return 'Young_HighIncome'
        else:
            return 'Young_LowIncome'
    elif age < 50:
        if frequency > 5:
            return 'Middle_HighFreq'
        else:
            return 'Middle_LowFreq'
    else:
        if income > 60000:
            return 'Senior_Wealthy'
        else:
            return 'Senior_Standard'

customer_data['segment'] = customer_data.apply(customer_segment, axis=1)
print("顧客セグメント分析:")
segment_summary = customer_data['segment'].value_counts()
print(segment_summary)

# 4. 日付計算を含む処理
print("\n📅 日付関連の特徴量:")

# 登録からの経過日数
customer_data['days_since_registration'] = customer_data.apply(
    lambda row: (pd.Timestamp('2024-01-01') - row['registration_date']).days, axis=1
)

# 最終ログインからの経過時間
customer_data['hours_since_last_login'] = customer_data.apply(
    lambda row: (pd.Timestamp('2024-01-01 12:00:00') - row['last_login']).total_seconds() / 3600, axis=1
)

print("日付関連特徴量:")
print(customer_data[['registration_date', 'days_since_registration', 'last_login', 'hours_since_last_login']].head())

# 5. 文字列処理を含む特徴量
print("\n📝 文字列処理特徴量:")

# カテゴリから特徴量作成
def category_features(category):
    """カテゴリから複数特徴量を作成"""
    features = {}
    features['is_tech'] = 1 if category == 'Electronics' else 0
    features['is_fashion'] = 1 if category == 'Fashion' else 0
    features['category_length'] = len(category)
    return pd.Series(features)

category_features_df = customer_data['product_category'].apply(category_features)
customer_data = pd.concat([customer_data, category_features_df], axis=1)

print("カテゴリ特徴量:")
print(customer_data[['product_category', 'is_tech', 'is_fashion', 'category_length']].head())

print("\n4. パフォーマンス最適化")
print("=" * 40)

# apply vs ベクトル化操作の比較
print("⚡ パフォーマンス比較:")

large_df = pd.DataFrame({
    'value1': np.random.random(100000),
    'value2': np.random.random(100000)
})

import time

# apply使用
start = time.time()
result_apply = large_df.apply(lambda row: row['value1'] * row['value2'], axis=1)
time_apply = time.time() - start

# ベクトル化操作
start = time.time()
result_vectorized = large_df['value1'] * large_df['value2']
time_vectorized = time.time() - start

print(f"apply使用: {time_apply:.4f}秒")
print(f"ベクトル化: {time_vectorized:.4f}秒")
print(f"速度改善: {time_apply/time_vectorized:.1f}倍")

# NumPy関数の活用
print("\n🚀 NumPy関数活用:")

def optimize_conditional(df):
    """条件分岐の最適化"""
    # 非効率なapply
    start = time.time()
    result_slow = df['value1'].apply(lambda x: 'High' if x > 0.5 else 'Low')
    time_slow = time.time() - start

    # 効率的なnp.where
    start = time.time()
    result_fast = np.where(df['value1'] > 0.5, 'High', 'Low')
    time_fast = time.time() - start

    print(f"apply条件分岐: {time_slow:.4f}秒")
    print(f"np.where: {time_fast:.4f}秒")
    print(f"速度改善: {time_slow/time_fast:.1f}倍")

optimize_conditional(large_df.head(10000))

print("\n5. 実務特徴量エンジニアリング例")
print("=" * 40)

# ECサイトの実務的な特徴量作成
ecommerce_data = pd.DataFrame({
    'user_id': range(1, 5001),
    'signup_date': pd.date_range('2023-01-01', periods=5000, freq='D'),
    'last_purchase_date': pd.date_range('2024-01-01', periods=5000, freq='H'),
    'total_orders': np.random.poisson(10, 5000),
    'total_amount': np.random.exponential(5000, 5000),
    'avg_order_value': np.random.normal(500, 200, 5000),
    'favorite_category': np.random.choice(['Electronics', 'Fashion', 'Books', 'Home'], 5000),
    'payment_method': np.random.choice(['Credit', 'Debit', 'Digital'], 5000),
    'location_tier': np.random.choice(['Tier1', 'Tier2', 'Tier3'], 5000)
})

print("🛒 ECサイトデータ:")
print(ecommerce_data.head())

print("\n🎯 実務特徴量の作成:")

# 1. RFM分析の基礎特徴量
def calculate_rfm_features(row):
    """RFM分析用特徴量"""
    current_date = pd.Timestamp('2024-01-01')

    # Recency（最終購入からの日数）
    recency = (current_date - row['last_purchase_date']).days

    # Frequency（注文頻度）
    frequency = row['total_orders']

    # Monetary（総購入金額）
    monetary = row['total_amount']

    return pd.Series({
        'recency': recency,
        'frequency': frequency,
        'monetary': monetary,
        'rfm_score': (1/max(recency, 1)) * frequency * (monetary/1000)
    })

rfm_features = ecommerce_data.apply(calculate_rfm_features, axis=1)
ecommerce_data = pd.concat([ecommerce_data, rfm_features], axis=1)

# 2. 顧客ライフサイクル特徴量
def customer_lifecycle(row):
    """顧客ライフサイクル段階"""
    days_since_signup = (pd.Timestamp('2024-01-01') - row['signup_date']).days
    orders_per_day = row['total_orders'] / max(days_since_signup, 1)

    if days_since_signup < 30:
        if row['total_orders'] > 2:
            return 'New_Active'
        else:
            return 'New_Inactive'
    elif days_since_signup < 365:
        if orders_per_day > 0.1:
            return 'Growing'
        else:
            return 'Declining'
    else:
        if orders_per_day > 0.05:
            return 'Loyal'
        else:
            return 'AtRisk'

ecommerce_data['lifecycle_stage'] = ecommerce_data.apply(customer_lifecycle, axis=1)

# 3. 行動パターン特徴量
ecommerce_data['orders_per_month'] = ecommerce_data.apply(
    lambda row: row['total_orders'] / max((pd.Timestamp('2024-01-01') - row['signup_date']).days / 30, 1), axis=1
)

ecommerce_data['is_high_value'] = ecommerce_data.apply(
    lambda row: 1 if row['avg_order_value'] > row['avg_order_value'].quantile(0.8) else 0, axis=1
)

# 4. カテゴリ別特徴量（ワンホットエンコーディング）
category_dummies = pd.get_dummies(ecommerce_data['favorite_category'], prefix='cat')
payment_dummies = pd.get_dummies(ecommerce_data['payment_method'], prefix='pay')
tier_dummies = pd.get_dummies(ecommerce_data['location_tier'], prefix='tier')

ecommerce_data = pd.concat([ecommerce_data, category_dummies, payment_dummies, tier_dummies], axis=1)

print("📊 作成された特徴量:")
feature_columns = ['recency', 'frequency', 'monetary', 'rfm_score', 'lifecycle_stage',
                  'orders_per_month', 'is_high_value']
print(ecommerce_data[feature_columns].head())

print("\n📈 特徴量の統計:")
print(ecommerce_data[['rfm_score', 'orders_per_month']].describe())

print("\n6. 高度な変換テクニック")
print("=" * 40)

# カスタム変換器クラス
class FeatureTransformer:
    """カスタム特徴量変換器"""

    def __init__(self):
        self.transformations = []

    def add_transformation(self, name, func):
        """変換処理を追加"""
        self.transformations.append((name, func))

    def fit_transform(self, df):
        """すべての変換を適用"""
        result_df = df.copy()

        for name, func in self.transformations:
            try:
                if hasattr(func, '__call__'):
                    if 'axis' in func.__code__.co_varnames:
                        result_df[name] = df.apply(func, axis=1)
                    else:
                        result_df[name] = df.apply(func)
                else:
                    result_df[name] = func
                print(f"✅ {name} 変換完了")
            except Exception as e:
                print(f"❌ {name} 変換失敗: {e}")

        return result_df

# 変換器の使用例
transformer = FeatureTransformer()

# 複数の変換を登録
transformer.add_transformation(
    'customer_tenure_months',
    lambda row: (pd.Timestamp('2024-01-01') - row['signup_date']).days / 30
)

transformer.add_transformation(
    'purchase_intensity',
    lambda row: row['total_orders'] / max((pd.Timestamp('2024-01-01') - row['signup_date']).days, 1) * 365
)

transformer.add_transformation(
    'value_segment',
    lambda row: 'Premium' if row['total_amount'] > 10000 else 'Standard' if row['total_amount'] > 2000 else 'Basic'
)

# 変換実行
sample_df = ecommerce_data.head(100)
transformed_df = transformer.fit_transform(sample_df)

print("\n🔄 変換器による特徴量作成:")
new_features = ['customer_tenure_months', 'purchase_intensity', 'value_segment']
print(transformed_df[new_features].head())

print("\n✅ Week 4 完了：特徴量エンジニアリングをマスターしました！")
```

### **Day 5-7: 高度な特徴量作成テクニック**

```python
print("\n7. 時系列特徴量エンジニアリング")
print("=" * 40)

# 時系列データの準備
dates = pd.date_range('2023-01-01', '2024-12-31', freq='D')
time_series_data = pd.DataFrame({
    'date': dates,
    'sales': np.random.normal(1000, 200, len(dates)) + 500 * np.sin(2 * np.pi * np.arange(len(dates)) / 365),
    'customers': np.random.poisson(50, len(dates)),
    'marketing_spend': np.random.exponential(100, len(dates))
})

# 基本的な時系列特徴量
time_series_data['year'] = time_series_data['date'].dt.year
time_series_data['month'] = time_series_data['date'].dt.month
time_series_data['day_of_week'] = time_series_data['date'].dt.dayofweek
time_series_data['is_weekend'] = time_series_data['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)

print("📅 基本時系列特徴量:")
print(time_series_data.head())

# ラグ特徴量（過去の値）
for lag in [1, 7, 30]:
    time_series_data[f'sales_lag_{lag}'] = time_series_data['sales'].shift(lag)

# 移動平均特徴量
for window in [7, 30]:
    time_series_data[f'sales_ma_{window}'] = time_series_data['sales'].rolling(window=window).mean()

# 変化率特徴量
time_series_data['sales_pct_change'] = time_series_data['sales'].pct_change()
time_series_data['sales_diff'] = time_series_data['sales'].diff()

print("\n📊 時系列特徴量サンプル:")
ts_features = ['sales', 'sales_lag_1', 'sales_lag_7', 'sales_ma_7', 'sales_pct_change']
print(time_series_data[ts_features].head(10))

print("\n8. 統計的特徴量の作成")
print("=" * 40)

# 集約統計量の特徴量
def create_statistical_features(df, target_col, group_col):
    """統計的特徴量の作成"""
    grouped = df.groupby(group_col)[target_col]

    stats_df = grouped.agg([
        'mean', 'median', 'std', 'min', 'max', 'count'
    ]).reset_index()

    # 列名の変更
    stats_df.columns = [group_col] + [f'{target_col}_{stat}' for stat in ['mean', 'median', 'std', 'min', 'max', 'count']]

    return stats_df

# 月別統計特徴量
monthly_stats = create_statistical_features(time_series_data, 'sales', 'month')
print("月別売上統計:")
print(monthly_stats)

# 顧客セグメント別統計
customer_stats = ecommerce_data.groupby('lifecycle_stage').agg({
    'total_amount': ['mean', 'std'],
    'total_orders': ['mean', 'median'],
    'avg_order_value': ['mean', 'std']
}).round(2)

print("\n顧客ライフサイクル別統計:")
print(customer_stats)

print("\n9. 相互作用特徴量")
print("=" * 40)

# 数値変数同士の相互作用
interaction_df = ecommerce_data.copy()

# 乗算による相互作用
interaction_df['amount_frequency_interaction'] = interaction_df['total_amount'] * interaction_df['total_orders']

# 比率による相互作用
interaction_df['amount_per_order'] = interaction_df['total_amount'] / (interaction_df['total_orders'] + 1)

# 条件付き相互作用
def conditional_interaction(row):
    """条件付き相互作用特徴量"""
    if row['favorite_category'] == 'Electronics':
        return row['total_amount'] * 1.2  # Electronics顧客は高価値重み
    elif row['favorite_category'] == 'Fashion':
        return row['total_orders'] * 1.5  # Fashion顧客は頻度重み
    else:
        return row['avg_order_value']

interaction_df['category_weighted_value'] = interaction_df.apply(conditional_interaction, axis=1)

print("🔄 相互作用特徴量:")
interaction_features = ['total_amount', 'total_orders', 'amount_frequency_interaction', 'amount_per_order']
print(interaction_df[interaction_features].head())

print("\n10. 次元削減と特徴量選択")
print("=" * 40)

# 主成分分析による特徴量作成
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 数値特徴量のみ選択
numeric_features = ['total_orders', 'total_amount', 'avg_order_value', 'recency', 'frequency', 'monetary']
X_numeric = ecommerce_data[numeric_features].fillna(0)

# 標準化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_numeric)

# PCA適用
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

# PCA結果をDataFrameに追加
pca_df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2', 'PCA3'])
ecommerce_data = pd.concat([ecommerce_data.reset_index(drop=True), pca_df], axis=1)

print("📉 PCA特徴量:")
print(f"第1主成分の寄与率: {pca.explained_variance_ratio_[0]:.3f}")
print(f"第2主成分の寄与率: {pca.explained_variance_ratio_[1]:.3f}")
print(f"第3主成分の寄与率: {pca.explained_variance_ratio_[2]:.3f}")
print(f"累積寄与率: {pca.explained_variance_ratio_.cumsum()}")

print("\n11. 特徴量評価と選択")
print("=" * 40)

# 特徴量の重要度評価
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, f_regression

# ターゲット変数の作成（例：総購入金額を予測）
target = ecommerce_data['total_amount'].fillna(0)

# 特徴量準備
feature_cols = ['total_orders', 'avg_order_value', 'recency', 'frequency', 'monetary',
               'orders_per_month', 'PCA1', 'PCA2', 'PCA3']
X_features = ecommerce_data[feature_cols].fillna(0)

# Random Forestによる特徴量重要度
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_features, target)

feature_importance = pd.DataFrame({
    'feature': feature_cols,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

print("🌳 Random Forest特徴量重要度:")
print(feature_importance)

# 統計的特徴量選択
selector = SelectKBest(score_func=f_regression, k=5)
X_selected = selector.fit_transform(X_features, target)
selected_features = np.array(feature_cols)[selector.get_support()]

print(f"\n📊 統計的選択された特徴量: {selected_features}")

print("\n12. 特徴量パイプライン統合")
print("=" * 40)

class ComprehensiveFeatureEngine:
    """包括的特徴量エンジニアリングエンジン"""

    def __init__(self):
        self.feature_log = []
        self.transformers = {}

    def create_basic_features(self, df):
        """基本特徴量の作成"""
        df = df.copy()

        # 日付特徴量
        if 'signup_date' in df.columns:
            df['days_since_signup'] = (pd.Timestamp('2024-01-01') - df['signup_date']).dt.days
            df['signup_year'] = df['signup_date'].dt.year
            df['signup_month'] = df['signup_date'].dt.month
            self.feature_log.append("日付特徴量作成完了")

        return df

    def create_ratio_features(self, df):
        """比率特徴量の作成"""
        df = df.copy()

        if 'total_amount' in df.columns and 'total_orders' in df.columns:
            df['amount_per_order'] = df['total_amount'] / (df['total_orders'] + 1)
            self.feature_log.append("比率特徴量作成完了")

        return df

    def create_categorical_features(self, df):
        """カテゴリ特徴量の作成"""
        df = df.copy()

        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            if df[col].nunique() < 10:  # カテゴリ数が少ない場合のみワンホット
                dummies = pd.get_dummies(df[col], prefix=col)
                df = pd.concat([df, dummies], axis=1)

        self.feature_log.append(f"カテゴリ特徴量作成完了: {categorical_cols.tolist()}")
        return df

    def create_statistical_features(self, df, group_cols, target_cols):
        """統計特徴量の作成"""
        df = df.copy()

        for group_col in group_cols:
            for target_col in target_cols:
                if group_col in df.columns and target_col in df.columns:
                    grouped = df.groupby(group_col)[target_col]
                    df[f'{target_col}_mean_by_{group_col}'] = grouped.transform('mean')
                    df[f'{target_col}_std_by_{group_col}'] = grouped.transform('std')

        self.feature_log.append("統計特徴量作成完了")
        return df

    def fit_transform(self, df, group_cols=None, target_cols=None):
        """全ての特徴量エンジニアリングを実行"""
        df = self.create_basic_features(df)
        df = self.create_ratio_features(df)
        df = self.create_categorical_features(df)

        if group_cols and target_cols:
            df = self.create_statistical_features(df, group_cols, target_cols)

        return df

    def get_log(self):
        """処理ログを取得"""
        return "\n".join(self.feature_log)

# 特徴量エンジン使用例
engine = ComprehensiveFeatureEngine()
sample_data = ecommerce_data.head(100).copy()

enhanced_data = engine.fit_transform(
    sample_data,
    group_cols=['favorite_category', 'payment_method'],
    target_cols=['total_amount', 'total_orders']
)

print("🚀 包括的特徴量エンジニアリング:")
print(engine.get_log())
print(f"\n元の特徴量数: {sample_data.shape[1]}")
print(f"拡張後特徴量数: {enhanced_data.shape[1]}")

print("\n✅ Week 4 完了：高度な特徴量エンジニアリングをマスターしました！")
```

---

## Week 5: データ結合マスター（concat/merge 完全攻略）

### 🎯 **この週のゴール**

- merge()と concat()を完全理解する
- 複雑な結合パターンを自在に操る
- 実務でよくある結合エラーを回避する
- 大規模データの効率的な結合をマスターする

---

### **Day 1-3: merge()の完全攻略**

```python
print("🔗 Week 5: データ結合マスター（concat/merge完全攻略）")
print("=" * 50)

import pandas as pd
import numpy as np
import time
from functools import reduce

print("1. merge()の基本概念と内部動作")
print("=" * 40)

# 実務的なサンプルデータ作成
# 顧客マスタ
customers = pd.DataFrame({
    'customer_id': ['C001', 'C002', 'C003', 'C004', 'C005'],
    'customer_name': ['田中商事', '佐藤建設', '鈴木製作所', '高橋電機', '山田運輸'],
    'industry': ['商社', '建設', '製造', '電機', '運輸'],
    'credit_score': [750, 680, 820, 720, 690],
    'registration_date': pd.to_datetime(['2020-01-01', '2020-03-15', '2019-06-20', '2021-02-10', '2020-11-05'])
})

# 売上トランザクション
transactions = pd.DataFrame({
    'transaction_id': ['T001', 'T002', 'T003', 'T004', 'T005', 'T006', 'T007'],
    'customer_id': ['C001', 'C002', 'C001', 'C003', 'C006', 'C002', 'C004'],  # C006は存在しない顧客
    'amount': [100000, 250000, 150000, 300000, 50000, 200000, 180000],
    'transaction_date': pd.to_datetime(['2024-01-15', '2024-01-20', '2024-02-01', '2024-02-05', '2024-02-10', '2024-02-15', '2024-02-20']),
    'product_category': ['A', 'B', 'A', 'C', 'A', 'B', 'C']
})

# 商品マスタ
products = pd.DataFrame({
    'product_category': ['A', 'B', 'C', 'D'],  # Dは取引がないカテゴリ
    'category_name': ['電子部品', '機械部品', '材料', '工具'],
    'unit_price': [1000, 5000, 2000, 3000],
    'supplier': ['サプライヤー1', 'サプライヤー2', 'サプライヤー3', 'サプライヤー4']
})

print("📊 基本データセット:")
print("顧客マスタ:")
print(customers)
print("\n売上トランザクション:")
print(transactions)
print("\n商品マスタ:")
print(products)

print("\n🔍 merge()の基本パターン:")

# 1. 内部結合（inner join）
print("1. 内部結合（INNER JOIN）:")
inner_result = pd.merge(transactions, customers, on='customer_id', how='inner')
print(f"トランザクション{len(transactions)}件 × 顧客{len(customers)}件 → 結果{len(inner_result)}件")
print(inner_result[['transaction_id', 'customer_name', 'amount']])

# 2. 左結合（left join）
print("\n2. 左結合（LEFT JOIN）:")
left_result = pd.merge(transactions, customers, on='customer_id', how='left')
print(f"結果{len(left_result)}件（トランザクション件数を維持）")
print("顧客マスタにない取引:")
print(left_result[left_result['customer_name'].isnull()][['transaction_id', 'customer_id', 'amount']])

# 3. 右結合（right join）
print("\n3. 右結合（RIGHT JOIN）:")
right_result = pd.merge(transactions, customers, on='customer_id', how='right')
print(f"結果{len(right_result)}件（顧客数を維持）")
print("取引がない顧客:")
print(right_result[right_result['transaction_id'].isnull()][['customer_id', 'customer_name']])

# 4. 外部結合（outer join）
print("\n4. 外部結合（OUTER JOIN）:")
outer_result = pd.merge(transactions, customers, on='customer_id', how='outer')
print(f"結果{len(outer_result)}件（全データを維持）")
print("データの完全性:")
print(f"- 有効な取引: {outer_result['transaction_id'].notna().sum()}件")
print(f"- 有効な顧客: {outer_result['customer_name'].notna().sum()}件")

print("\n2. 複雑な結合条件")
print("=" * 40)

# 複数列による結合
detailed_transactions = pd.DataFrame({
    'customer_id': ['C001', 'C001', 'C002', 'C002'],
    'product_category': ['A', 'B', 'A', 'C'],
    'quantity': [10, 5, 20, 15],
    'transaction_date': pd.to_datetime(['2024-01-15', '2024-01-16', '2024-01-20', '2024-01-25'])
})

print("📋 複数列結合の例:")
print("詳細トランザクション:")
print(detailed_transactions)

# 複数列での結合
multi_column_merge = pd.merge(
    detailed_transactions,
    products,
    on='product_category',
    how='left'
)
print("\n商品マスタとの結合:")
print(multi_column_merge)

# 異なる列名での結合
customer_info = pd.DataFrame({
    'cust_id': ['C001', 'C002', 'C003'],  # 列名が異なる
    'region': ['関東', '関西', '中部'],
    'sales_rep': ['営業A', '営業B', '営業C']
})

different_name_merge = pd.merge(
    transactions,
    customer_info,
    left_on='customer_id',
    right_on='cust_id',
    how='left'
)
print("\n異なる列名での結合:")
print(different_name_merge[['customer_id', 'cust_id', 'region', 'sales_rep']].head())

print("\n3. 結合のパフォーマンス最適化")
print("=" * 40)

# 大規模データでのパフォーマンステスト
print("⚡ パフォーマンス比較:")

# 大きなデータセット作成
np.random.seed(42)
large_left = pd.DataFrame({
    'key': np.random.choice(range(10000), 100000),
    'value1': np.random.random(100000)
})

large_right = pd.DataFrame({
    'key': range(10000),
    'value2': np.random.random(10000)
})

print(f"左テーブル: {len(large_left):,}行")
print(f"右テーブル: {len(large_right):,}行")

# パフォーマンス測定
start_time = time.time()
result_normal = pd.merge(large_left, large_right, on='key', how='left')
normal_time = time.time() - start_time

# インデックス設定による高速化
large_right_indexed = large_right.set_index('key')
start_time = time.time()
result_indexed = large_left.set_index('key').join(large_right_indexed, how='left')
indexed_time = time.time() - start_time

print(f"通常のmerge: {normal_time:.3f}秒")
print(f"インデックス利用: {indexed_time:.3f}秒")
print(f"速度改善: {normal_time/indexed_time:.1f}倍")

# ソート済みデータでの最適化
large_left_sorted = large_left.sort_values('key')
large_right_sorted = large_right.sort_values('key')

start_time = time.time()
result_sorted = pd.merge(large_left_sorted, large_right_sorted, on='key', how='left')
sorted_time = time.time() - start_time

print(f"ソート済みmerge: {sorted_time:.3f}秒")

print("\n4. 結合時のエラーハンドリング")
print("=" * 40)

print("🚨 よくある結合エラーと対処法:")

# 1. キー列のデータ型不一致
problematic_df1 = pd.DataFrame({
    'id': [1, 2, 3],  # 数値型
    'name': ['A', 'B', 'C']
})

problematic_df2 = pd.DataFrame({
    'id': ['1', '2', '4'],  # 文字列型
    'value': [100, 200, 300]
})

print("1. データ型不一致の問題:")
print(f"df1のid型: {problematic_df1['id'].dtype}")
print(f"df2のid型: {problematic_df2['id'].dtype}")

# 修正方法
problematic_df2['id'] = problematic_df2['id'].astype(int)
fixed_merge = pd.merge(problematic_df1, problematic_df2, on='id', how='left')
print("修正後の結合:")
print(fixed_merge)

# 2. 重複キーの問題
duplicate_customers = pd.DataFrame({
    'customer_id': ['C001', 'C001', 'C002'],  # C001が重複
    'customer_name': ['田中商事', '田中商事(新)', '佐藤建設'],
    'status': ['active', 'inactive', 'active']
})

print("\n2. 重複キーの問題:")
duplicate_merge = pd.merge(transactions.head(3), duplicate_customers, on='customer_id', how='left')
print(f"元トランザクション: {len(transactions.head(3))}件")
print(f"結合後: {len(duplicate_merge)}件（重複により増加）")

# 重複除去の方法
cleaned_customers = duplicate_customers.drop_duplicates(subset=['customer_id'], keep='first')
clean_merge = pd.merge(transactions.head(3), cleaned_customers, on='customer_id', how='left')
print(f"重複除去後: {len(clean_merge)}件")

print("\n5. 高度な結合テクニック")
print("=" * 40)

# 条件付き結合（範囲結合）
print("📅 範囲結合の例:")

# 価格帯マスタ
price_tiers = pd.DataFrame({
    'tier_name': ['低価格', '中価格', '高価格'],
    'min_amount': [0, 100000, 200000],
    'max_amount': [99999, 199999, float('inf'))]
})

print("価格帯マスタ:")
print(price_tiers)

# 条件付き結合を実現する関数
def conditional_merge(transactions_df, price_tiers_df):
    """条件付き結合：取引金額に基づく価格帯分類"""
    result_list = []

    for _, trans in transactions_df.iterrows():
        amount = trans['amount']
        matched_tier = price_tiers_df[
            (price_tiers_df['min_amount'] <= amount) &
            (price_tiers_df['max_amount'] >= amount)
        ]

        if not matched_tier.empty:
            trans_with_tier = trans.to_dict()
            trans_with_tier.update(matched_tier.iloc[0].to_dict())
            result_list.append(trans_with_tier)

    return pd.DataFrame(result_list)

conditional_result = conditional_merge(transactions, price_tiers)
print("\n条件付き結合結果:")
print(conditional_result[['transaction_id', 'amount', 'tier_name']])

# より効率的な範囲結合（pd.cut使用）
transactions['price_tier'] = pd.cut(
    transactions['amount'],
    bins=[0, 100000, 200000, float('inf')],
    labels=['低価格', '中価格', '高価格'],
    include_lowest=True
)
print("\npd.cutを使用した価格帯分類:")
print(transactions[['transaction_id', 'amount', 'price_tier']])

print("\n6. 複数テーブルの連鎖結合")
print("=" * 40)

# 営業担当マスタ
sales_reps = pd.DataFrame({
    'rep_id': ['R001', 'R002', 'R003'],
    'rep_name': ['田中営業', '佐藤営業', '鈴木営業'],
    'region': ['関東', '関西', '中部']
})

# 顧客-営業担当マッピング
customer_rep_mapping = pd.DataFrame({
    'customer_id': ['C001', 'C002', 'C003', 'C004', 'C005'],
    'rep_id': ['R001', 'R002', 'R001', 'R003', 'R002']
})

print("📊 多段階結合:")
print("営業担当マスタ:")
print(sales_reps)
print("\n顧客-営業担当マッピング:")
print(customer_rep_mapping)

# 方法1: 段階的結合
step1 = pd.merge(transactions, customers, on='customer_id', how='left')
step2 = pd.merge(step1, customer_rep_mapping, on='customer_id', how='left')
step3 = pd.merge(step2, sales_reps, on='rep_id', how='left')

print("\n段階的結合結果:")
print(step3[['transaction_id', 'customer_name', 'rep_name', 'amount']])

# 方法2: 関数型結合（reduce使用）
def chain_merge(dfs_and_keys):
    """複数DataFrameの連鎖結合"""
    return reduce(
        lambda left, right_info: pd.merge(left, right_info[0], on=right_info[1], how='left'),
        dfs_and_keys[1:],
        dfs_and_keys[0][0]
    )

merge_chain = [
    (transactions, 'customer_id'),
    (customers, 'customer_id'),
    (customer_rep_mapping, 'customer_id'),
    (sales_reps, 'rep_id')
]

chained_result = chain_merge(merge_chain)
print("\n関数型連鎖結合結果:")
print(chained_result[['transaction_id', 'customer_name', 'rep_name', 'amount']])

print("\n✅ Week 5 Day 1-3 完了：merge()を完全マスターしました！")
```

### **Day 4-7: concat()完全攻略と高度な結合パターン**

```python
print("\n7. concat()の完全理解")
print("=" * 40)

print("📚 concat()の基本概念:")

# 基本的なconcat操作
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

df2 = pd.DataFrame({
    'A': [10, 11, 12],
    'B': [13, 14, 15],
    'C': [16, 17, 18]
})

df3 = pd.DataFrame({
    'D': [19, 20, 21],
    'E': [22, 23, 24]
})

print("基本DataFrame:")
print("df1:")
print(df1)
print("\ndf2:")
print(df2)
print("\ndf3:")
print(df3)

# 縦方向の連結
vertical_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
print("\n📈 縦方向連結（axis=0）:")
print(vertical_concat)

# 横方向の連結
horizontal_concat = pd.concat([df1, df3], axis=1)
print("\n📊 横方向連結（axis=1）:")
print(horizontal_concat)

# インデックスを保持した連結
indexed_concat = pd.concat([df1, df2], axis=0, keys=['データ1', 'データ2'])
print("\n🏷️ 階層インデックス付き連結:")
print(indexed_concat)

print("\n8. 実務的なconcat活用パターン")
print("=" * 40)

# 時系列データの結合
print("📅 時系列データの結合:")

# 月別売上データ
jan_sales = pd.DataFrame({
    'date': pd.date_range('2024-01-01', '2024-01-31', freq='D'),
    'sales': np.random.normal(1000, 100, 31),
    'month': '2024-01'
})

feb_sales = pd.DataFrame({
    'date': pd.date_range('2024-02-01', '2024-02-29', freq='D'),
    'sales': np.random.normal(1100, 120, 29),
    'month': '2024-02'
})

mar_sales = pd.DataFrame({
    'date': pd.date_range('2024-03-01', '2024-03-31', freq='D'),
    'sales': np.random.normal(1200, 150, 31),
    'month': '2024-03'
})

# 四半期データの結合
q1_sales = pd.concat([jan_sales, feb_sales, mar_sales], ignore_index=True)
print(f"Q1売上データ: {len(q1_sales)}日分")
print("月別売上サマリー:")
print(q1_sales.groupby('month')['sales'].agg(['sum', 'mean']).round(2))

# 複数ファイルの読み込みと結合シミュレーション
print("\n📁 複数ファイル結合パターン:")

def simulate_file_concat():
    """複数ファイルの読み込みと結合をシミュレート"""
    file_data = []

    for i in range(1, 6):  # 5つのファイルをシミュレート
        df = pd.DataFrame({
            'customer_id': [f'C{j:03d}' for j in range(i*100, (i+1)*100)],
            'value': np.random.normal(1000, 200, 100),
            'source_file': f'file_{i}.csv'
        })
        file_data.append(df)

    # 全ファイルを結合
    combined_data = pd.concat(file_data, ignore_index=True)
    return combined_data

combined_files = simulate_file_concat()
print(f"結合されたデータ: {len(combined_files)}行")
print("ファイル別データ数:")
print(combined_files['source_file'].value_counts())

print("\n9. 異なる構造のDataFrame結合")
print("=" * 40)

# 列が異なるDataFrameの結合
print("🔀 列構造が異なるDataFrame:")

sales_2023 = pd.DataFrame({
    'date': pd.date_range('2023-01-01', periods=5, freq='D'),
    'product_a': [100, 110, 105, 120, 115],
    'product_b': [200, 210, 205, 220, 215]
})

sales_2024 = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=5, freq='D'),
    'product_a': [130, 140, 135, 150, 145],
    'product_c': [300, 310, 305, 320, 315]  # product_bがなく、product_cが新規
})

print("2023年データ:")
print(sales_2023)
print("\n2024年データ:")
print(sales_2024)

# 外部結合で全列を保持
mixed_columns_concat = pd.concat([sales_2023, sales_2024], sort=False)
print("\n混合列結合結果:")
print(mixed_columns_concat)

# 共通列のみ結合
common_columns = list(set(sales_2023.columns) & set(sales_2024.columns))
print(f"\n共通列: {common_columns}")
common_only_concat = pd.concat([
    sales_2023[common_columns],
    sales_2024[common_columns]
])
print("共通列のみ結合:")
print(common_only_concat)

print("\n10. 大規模データの効率的結合")
print("=" * 40)

print("⚡ 大規模データ結合の最適化:")

# メモリ効率的な結合方法
def efficient_large_concat(dataframes, chunk_size=1000):
    """メモリ効率的な大規模データ結合"""

    # チャンク単位で処理
    result_chunks = []
    current_chunk = []
    current_size = 0

    for df in dataframes:
        current_chunk.append(df)
        current_size += len(df)

        if current_size >= chunk_size:
            # チャンクを結合
            chunk_result = pd.concat(current_chunk, ignore_index=True)
            result_chunks.append(chunk_result)

            # チャンクをリセット
            current_chunk = []
            current_size = 0

    # 残りのデータを処理
    if current_chunk:
        chunk_result = pd.concat(current_chunk, ignore_index=True)
        result_chunks.append(chunk_result)

    # 最終結合
    return pd.concat(result_chunks, ignore_index=True)

# テスト用の大きなデータセット
large_dataframes = []
for i in range(10):
    df = pd.DataFrame({
        'id': range(i*1000, (i+1)*1000),
        'value': np.random.random(1000),
        'category': np.random.choice(['A', 'B', 'C'], 1000)
    })
    large_dataframes.append(df)

# 効率的結合のテスト
start_time = time.time()
efficient_result = efficient_large_concat(large_dataframes, chunk_size=2000)
efficient_time = time.time() - start_time

# 通常結合との比較
start_time = time.time()
normal_result = pd.concat(large_dataframes, ignore_index=True)
normal_time = time.time() - start_time

print(f"効率的結合: {efficient_time:.3f}秒")
print(f"通常結合: {normal_time:.3f}秒")
print(f"結果データ: {len(efficient_result)}行")

print("\n11. データ品質チェック付き結合")
print("=" * 40)

class QualityCheckedMerge:
    """データ品質チェック機能付きマージ"""

    def __init__(self):
        self.merge_log = []
        self.quality_issues = []

    def safe_merge(self, left, right, on=None, how='inner', **kwargs):
        """安全なマージ実行"""

        # 事前チェック
        self._pre_merge_checks(left, right, on)

        # マージ実行
        try:
            result = pd.merge(left, right, on=on, how=how, **kwargs)
            self._post_merge_checks(left, right, result, how)

            self.merge_log.append(f"✅ マージ成功: {len(left)} × {len(right)} → {len(result)}")
            return result

        except Exception as e:
            self.quality_issues.append(f"❌ マージエラー: {str(e)}")
            raise

    def _pre_merge_checks(self, left, right, on):
        """マージ前品質チェック"""

        if on:
            # キー列の存在チェック
            if on not in left.columns:
                self.quality_issues.append(f"⚠️ 左テーブルにキー列'{on}'が存在しません")
            if on not in right.columns:
                self.quality_issues.append(f"⚠️ 右テーブルにキー列'{on}'が存在しません")

            # データ型チェック
            if on in left.columns and on in right.columns:
                if left[on].dtype != right[on].dtype:
                    self.quality_issues.append(f"⚠️ キー列'{on}'のデータ型が異なります: {left[on].dtype} vs {right[on].dtype}")

            # 重複チェック
            left_duplicates = left[on].duplicated().sum()
            right_duplicates = right[on].duplicated().sum()

            if left_duplicates > 0:
                self.quality_issues.append(f"⚠️ 左テーブルにキー重複: {left_duplicates}件")
            if right_duplicates > 0:
                self.quality_issues.append(f"⚠️ 右テーブルにキー重複: {right_duplicates}件")

    def _post_merge_checks(self, left, right, result, how):
        """マージ後品質チェック"""

        # 行数チェック
        if how == 'inner':
            if len(result) > len(left) or len(result) > len(right):
                self.quality_issues.append("⚠️ 内部結合で行数が増加（重複キーの可能性）")

        elif how == 'left':
            if len(result) != len(left):
                self.quality_issues.append(f"⚠️ 左結合で行数が変化: {len(left)} → {len(result)}")

        # null値チェック
        new_nulls = result.isnull().sum().sum() - left.isnull().sum().sum()
        if new_nulls > 0:
            self.quality_issues.append(f"⚠️ マージにより{new_nulls}個のnull値が発生")

    def get_quality_report(self):
        """品質レポートを取得"""
        report = "=== データ品質レポート ===\n"
        report += "\n".join(self.merge_log)
        if self.quality_issues:
            report += "\n\n=== 品質問題 ===\n"
            report += "\n".join(self.quality_issues)
        return report

# 品質チェック付きマージの使用例
quality_merger = QualityCheckedMerge()

# 問題のあるデータでテスト
problematic_left = pd.DataFrame({
    'id': [1, 1, 2, 3],  # 重複あり
    'value': ['A', 'B', 'C', 'D']
})

problematic_right = pd.DataFrame({
    'id': ['1', '2', '4'],  # 文字列型
    'info': ['X', 'Y', 'Z']
})

print("🔍 品質チェック付きマージテスト:")
try:
    # データ型を修正してからマージ
    problematic_right['id'] = problematic_right['id'].astype(int)
    safe_result = quality_merger.safe_merge(problematic_left, problematic_right, on='id', how='left')
    print("マージ結果:")
    print(safe_result)
except Exception as e:
    print(f"マージエラー: {e}")

print("\n品質レポート:")
print(quality_merger.get_quality_report())

print("\n12. 実務統合パイプライン")
print("=" * 40)

class DataIntegrationPipeline:
    """データ統合パイプライン"""

    def __init__(self):
        self.steps = []
        self.results = {}
        self.performance_log = {}

    def add_merge_step(self, name, left_key, right_key, join_type='left', validation=True):
        """マージステップを追加"""
        self.steps.append({
            'type': 'merge',
            'name': name,
            'left_key': left_key,
            'right_key': right_key,
            'join_type': join_type,
            'validation': validation
        })

    def add_concat_step(self, name, dataframes, axis=0):
        """結合ステップを追加"""
        self.steps.append({
            'type': 'concat',
            'name': name,
            'dataframes': dataframes,
            'axis': axis
        })

    def execute_pipeline(self, initial_data):
        """パイプライン実行"""
        current_data = initial_data.copy()

        for step in self.steps:
            start_time = time.time()

            if step['type'] == 'merge':
                current_data = self._execute_merge_step(current_data, step)
            elif step['type'] == 'concat':
                current_data = self._execute_concat_step(current_data, step)

            execution_time = time.time() - start_time
            self.performance_log[step['name']] = execution_time
            self.results[step['name']] = current_data.copy()

            print(f"✅ {step['name']} 完了: {execution_time:.3f}秒, {len(current_data)}行")

        return current_data

    def _execute_merge_step(self, data, step):
        """マージステップ実行"""
        # 実装は簡略化
        return data

    def _execute_concat_step(self, data, step):
        """結合ステップ実行"""
        return pd.concat([data] + step['dataframes'], axis=step['axis'], ignore_index=True)

    def get_performance_report(self):
        """パフォーマンスレポート"""
        total_time = sum(self.performance_log.values())
        report = f"総実行時間: {total_time:.3f}秒\n"
        for step, time_taken in self.performance_log.items():
            percentage = (time_taken / total_time) * 100
            report += f"- {step}: {time_taken:.3f}秒 ({percentage:.1f}%)\n"
        return report

# パイプライン使用例
pipeline = DataIntegrationPipeline()

# 追加データの結合ステップ
additional_transactions = pd.DataFrame({
    'transaction_id': ['T008', 'T009'],
    'customer_id': ['C001', 'C003'],
    'amount': [75000, 125000],
    'transaction_date': pd.to_datetime(['2024-03-01', '2024-03-05']),
    'product_category': ['B', 'A']
})

pipeline.add_concat_step('追加取引結合', [additional_transactions], axis=0)

# パイプライン実行
print("🚀 データ統合パイプライン実行:")
final_result = pipeline.execute_pipeline(transactions)

print(f"\n最終結果: {len(final_result)}行")
print("\nパフォーマンスレポート:")
print(pipeline.get_performance_report())

print("\n✅ Week 5 完了：データ結合を完全マスターしました！")
```

---

## Week 6: 集計・グループ化・時系列分析

### 🎯 **この週のゴール**

- groupby 操作の高度なテクニックをマスターする
- 複雑な集計処理を効率的に実装する
- 時系列データの分析手法を習得する
- ビジネス指標の計算方法を理解する

---

### **Day 1-4: 高度な groupby 操作**

```python
print("\n📊 Week 6: 集計・グループ化・時系列分析")
print("=" * 50)

print("1. groupbyの内部動作と最適化")
print("=" * 40)

# 大規模な売上データセットの作成
np.random.seed(42)
sales_data = []

# 2年分の日次売上データ
for i in range(730):  # 2年 = 730日
    date = pd.Timestamp('2023-01-01') + pd.Timedelta(days=i)

    # 複数店舗の売上
    for store in ['東京店', '大阪店', '名古屋店', '福岡店', '札幌店']:
        # 複数商品カテゴリ
        for category in ['Electronics', 'Fashion', 'Food', 'Books']:
            # 季節性を加味した売上
            base_sales = 10000
            seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * i / 365)
            weekend_factor = 1.2 if date.weekday() >= 5 else 1.0

            sales = base_sales * seasonal_factor * weekend_factor * np.random.uniform(0.7, 1.3)

            sales_data.append({
                'date': date,
                'store': store,
                'category': category,
                'sales': sales,
                'units_sold': int(sales / np.random.uniform(50, 200)),
                'year': date.year,
                'month': date.month,
                'quarter': date.quarter,
                'weekday': date.day_name()
            })

sales_df = pd.DataFrame(sales_data)
print(f"📈 売上データ: {len(sales_df):,}行")
print("データサンプル:")
print(sales_df.head())

print("\n⚡ groupby パフォーマンス最適化:")

# 1. カテゴリ型による最適化
start_time = time.time()
result1 = sales_df.groupby('store')['sales'].sum()
time1 = time.time() - start_time

# カテゴリ型に変換
sales_df_opt = sales_df.copy()
sales_df_opt['store'] = sales_df_opt['store'].astype('category')
sales_df_opt['category'] = sales_df_opt['category'].astype('category')

start_time = time.time()
result2 = sales_df_opt.groupby('store')['sales'].sum()
time2 = time.time() - start_time

print(f"通常型: {time1:.4f}秒")
print(f"カテゴリ型: {time2:.4f}秒")
print(f"速度改善: {time1/time2:.1f}倍")

# 2. ソート済みデータでの最適化
sales_df_sorted = sales_df.sort_values(['store', 'category'])

start_time = time.time()
result3 = sales_df_sorted.groupby(['store', 'category'])['sales'].sum()
time3 = time.time() - start_time

print(f"ソート済み複数キー: {time3:.4f}秒")

print("\n2. 高度な集計関数")
print("=" * 40)

# カスタム集計関数
def sales_metrics(group):
    """カスタム売上指標計算"""
    return pd.Series({
        '売上合計': group['sales'].sum(),
        '売上平均': group['sales'].mean(),
        '売上中央値': group['sales'].median(),
        '売上標準偏差': group['sales'].std(),
        '最大売上': group['sales'].max(),
        '最小売上': group['sales'].min(),
        '売上範囲': group['sales'].max() - group['sales'].min(),
        '変動係数': group['sales'].std() / group['sales'].mean(),
        '売上成長率': group['sales'].pct_change().mean() * 100,
        '取引日数': len(group),
        'アクティブ率': (group['sales'] > 0).sum() / len(group)
    })

# 店舗別詳細分析
store_analysis = sales_df.groupby('store').apply(sales_metrics)
print("🏪 店舗別詳細分析:")
print(store_analysis.round(2))

# パーセンタイル計算
def percentile_analysis(group):
    """パーセンタイル分析"""
    return pd.Series({
        'P10': group['sales'].quantile(0.1),
        'P25': group['sales'].quantile(0.25),
        'P50': group['sales'].quantile(0.5),
        'P75': group['sales'].quantile(0.75),
        'P90': group['sales'].quantile(0.9),
        'P95': group['sales'].quantile(0.95),
        'P99': group['sales'].quantile(0.99)
    })

category_percentiles = sales_df.groupby('category').apply(percentile_analysis)
print("\n📊 カテゴリ別パーセンタイル分析:")
print(category_percentiles.round(0))

print("\n3. 複雑な集計パターン")
print("=" * 40)

# 複数レベルの集計
print("🔄 多段階集計:")

# レベル1: 店舗×カテゴリ別日次平均
daily_avg = sales_df.groupby(['store', 'category', 'date'])['sales'].mean().reset_index()

# レベル2: 店舗×カテゴリ別月次統計
monthly_stats = daily_avg.groupby([
    daily_avg['store'],
    daily_avg['category'],
    daily_avg['date'].dt.to_period('M')
]).agg({
    'sales': ['mean', 'std', 'count']
})

monthly_stats.columns = ['月平均売上', '月売上標準偏差', '営業日数']
print("月次統計サンプル:")
print(monthly_stats.head(10))

# 条件付き集計
print("\n🎯 条件付き集計:")

def conditional_aggregation(group):
    """条件に基づく集計"""
    high_sales = group[group['sales'] > group['sales'].quantile(0.8)]
    low_sales = group[group['sales'] < group['sales'].quantile(0.2)]

    return pd.Series({
        '高売上日数': len(high_sales),
        '高売上平均': high_sales['sales'].mean() if len(high_sales) > 0 else 0,
        '低売上日数': len(low_sales),
        '低売上平均': low_sales['sales'].mean() if len(low_sales) > 0 else 0,
        '安定度': 1 - (group['sales'].std() / group['sales'].mean())
    })

store_performance = sales_df.groupby('store').apply(conditional_aggregation)
print("店舗パフォーマンス分析:")
print(store_performance.round(3))

print("\n4. ウィンドウ関数と移動計算")
print("=" * 40)

# 売上データを日付順にソート
sales_daily = sales_df.groupby(['store', 'date'])['sales'].sum().reset_index()
sales_daily = sales_daily.sort_values(['store', 'date'])

print("📈 移動平均・累積計算:")

# 店舗別の移動平均
sales_daily['MA_7'] = sales_daily.groupby('store')['sales'].rolling(window=7).mean().reset_index(0, drop=True)
sales_daily['MA_30'] = sales_daily.groupby('store')['sales'].rolling(window=30).mean().reset_index(0, drop=True)

# 累積売上
sales_daily['cumulative_sales'] = sales_daily.groupby('store')['sales'].cumsum()

# 前年同月比
sales_daily['year'] = sales_daily['date'].dt.year
sales_daily['month'] = sales_daily['date'].dt.month
sales_daily['yoy_change'] = sales_daily.groupby(['store', 'month'])['sales'].pct_change(periods=365) * 100

print("移動平均サンプル:")
print(sales_daily[['store', 'date', 'sales', 'MA_7', 'MA_30']].head(10))

# ランキング計算
sales_daily['daily_rank'] = sales_daily.groupby('date')['sales'].rank(ascending=False)
sales_daily['monthly_rank'] = sales_daily.groupby([sales_daily['date'].dt.to_period('M')])['sales'].rank(ascending=False)

print("\n🏆 ランキング分析:")
top_performers = sales_daily[sales_daily['daily_rank'] <= 2].groupby('store').size().sort_values(ascending=False)
print("トップ2入り回数:")
print(top_performers)

print("\n5. 時系列特徴量の生成")
print("=" * 40)

print("📅 時系列特徴量エンジニアリング:")

# ラグ特徴量
for lag in [1, 7, 30]:
    sales_daily[f'sales_lag_{lag}'] = sales_daily.groupby('store')['sales'].shift(lag)

# 変化率特徴量
sales_daily['sales_pct_change_1d'] = sales_daily.groupby('store')['sales'].pct_change()
sales_daily['sales_pct_change_7d'] = sales_daily.groupby('store')['sales'].pct_change(periods=7)

# 季節性特徴量
sales_daily['day_of_year'] = sales_daily['date'].dt.dayofyear
sales_daily['week_of_year'] = sales_daily['date'].dt.isocalendar().week
sales_daily['is_weekend'] = sales_daily['date'].dt.weekday >= 5

# 周期性検出
def seasonal_decompose_simple(group):
    """簡易季節性分解"""
    if len(group) < 365:  # 1年未満のデータは季節性分析をスキップ
        return group

    # トレンド（365日移動平均）
    group['trend'] = group['sales'].rolling(window=365, center=True).mean()

    # 季節性（週次パターン）
    group['seasonal'] = group.groupby(group['date'].dt.dayofweek)['sales'].transform('mean')

    # 残差
    group['residual'] = group['sales'] - group['trend'].fillna(group['sales'].mean()) - group['seasonal']

    return group

# 店舗別季節性分解
sales_with_decomp = sales_daily.groupby('store').apply(seasonal_decompose_simple).reset_index(drop=True)

print("季節性分解サンプル:")
sample_store = sales_with_decomp[sales_with_decomp['store'] == '東京店'].head(10)
print(sample_store[['date', 'sales', 'trend', 'seasonal', 'residual']])

print("\n6. ビジネス指標の計算")
print("=" * 40)

print("💼 KPI計算:")

# 売上成長率
def calculate_growth_metrics(df):
    """成長指標の計算"""
    df = df.sort_values('date')

    # 前日比
    df['sales_growth_1d'] = df['sales'].pct_change() * 100

    # 前週比
    df['sales_growth_7d'] = df['sales'].pct_change(periods=7) * 100

    # 前月比（約30日）
    df['sales_growth_30d'] = df['sales'].pct_change(periods=30) * 100

    # 年初来成長率
    df['ytd_growth'] = (df['sales'] / df.groupby(df['date'].dt.year)['sales'].cumsum().shift().fillna(df['sales'])) - 1

    return df

# 店舗別成長指標
growth_metrics = sales_daily.groupby('store').apply(calculate_growth_metrics).reset_index(drop=True)

# 成長率サマリー
growth_summary = growth_metrics.groupby('store').agg({
    'sales_growth_1d': ['mean', 'std'],
    'sales_growth_7d': ['mean', 'std'],
    'sales_growth_30d': ['mean', 'std']
}).round(2)

print("成長率サマリー:")
print(growth_summary)

# 売上の安定性指標
stability_metrics = sales_daily.groupby('store').agg({
    'sales': [
        lambda x: x.std() / x.mean(),  # 変動係数
        lambda x: (x.max() - x.min()) / x.mean(),  # 正規化範囲
        lambda x: (x > x.quantile(0.9)).sum() / len(x),  # 高売上日の比率
        lambda x: (x < x.quantile(0.1)).sum() / len(x)   # 低売上日の比率
    ]
})

stability_metrics.columns = ['変動係数', '正規化範囲', '高売上日比率', '低売上日比率']
print("\n📊 売上安定性指標:")
print(stability_metrics.round(3))

print("\n✅ Week 6 Day 1-4 完了：高度な集計をマスターしました！")
```

### **Day 5-7: 時系列分析の実践**

```python
print("\n7. 高度な時系列分析")
print("=" * 40)

# 詳細な時系列データセットの作成
print("📊 時系列データの準備:")

# より複雑な時系列パターン
def generate_complex_timeseries(start_date, periods, freq='D'):
    """複雑なパターンを持つ時系列データ生成"""
    dates = pd.date_range(start_date, periods=periods, freq=freq)

    data = []
    for i, date in enumerate(dates):
        # 基本トレンド（成長）
        trend = 1000 + i * 2

        # 年次季節性
        yearly_seasonal = 200 * np.sin(2 * np.pi * i / 365)

        # 週次季節性
        weekly_seasonal = 100 * np.sin(2 * np.pi * i / 7)

        # 月末効果
        month_end_effect = 150 if date.day >= 25 else 0

        # 祝日効果（簡略化）
        holiday_effect = -200 if date.month == 1 and date.day == 1 else 0

        # ランダムノイズ
        noise = np.random.normal(0, 100)

        # 外部イベント（例：キャンペーン）
        campaign_effect = 500 if (i % 90 == 0 and i > 0) else 0

        value = trend + yearly_seasonal + weekly_seasonal + month_end_effect + holiday_effect + noise + campaign_effect

        data.append({
            'date': date,
            'value': max(0, value),  # 負の値は0に
            'trend': trend,
            'yearly_seasonal': yearly_seasonal,
            'weekly_seasonal': weekly_seasonal,
            'month_end_effect': month_end_effect,
            'campaign_effect': campaign_effect,
            'noise': noise
        })

    return pd.DataFrame(data)

# 3年分のデータ生成
ts_data = generate_complex_timeseries('2021-01-01', 1095)  # 3年 = 1095日
ts_data.set_index('date', inplace=True)

print(f"時系列データ: {len(ts_data)}日分")
print("データサンプル:")
print(ts_data.head())

print("\n📈 トレンド分析:")

# 移動平均によるトレンド抽出
ts_data['MA_30'] = ts_data['value'].rolling(window=30).mean()
ts_data['MA_90'] = ts_data['value'].rolling(window=90).mean()
ts_data['MA_365'] = ts_data['value'].rolling(window=365).mean()

# トレンドの方向性
ts_data['trend_direction'] = np.sign(ts_data['MA_30'].diff())

# トレンド強度
ts_data['trend_strength'] = abs(ts_data['MA_30'].pct_change())

print("トレンド分析結果:")
trend_summary = ts_data.groupby('trend_direction')['trend_strength'].agg(['count', 'mean'])
trend_summary.index = ['下降', '変化なし', '上昇']
print(trend_summary)

print("\n🔄 季節性分析:")

# 季節性の定量化
seasonal_patterns = {}

# 月別パターン
monthly_pattern = ts_data.groupby(ts_data.index.month)['value'].agg(['mean', 'std'])
monthly_pattern.index = [f'{i}月' for i in monthly_pattern.index]
seasonal_patterns['月別'] = monthly_pattern

# 曜日別パターン
weekday_pattern = ts_data.groupby(ts_data.index.dayofweek)['value'].agg(['mean', 'std'])
weekday_pattern.index = ['月', '火', '水', '木', '金', '土', '日']
seasonal_patterns['曜日別'] = weekday_pattern

# 四半期別パターン
quarterly_pattern = ts_data.groupby(ts_data.index.quarter)['value'].agg(['mean', 'std'])
quarterly_pattern.index = [f'Q{i}' for i in quarterly_pattern.index]
seasonal_patterns['四半期別'] = quarterly_pattern

print("季節性パターン:")
for pattern_name, pattern_data in seasonal_patterns.items():
    print(f"\n{pattern_name}:")
    print(pattern_data.round(2))

# 季節性指数の計算
def calculate_seasonal_index(series, period):
    """季節性指数の計算"""
    # 移動平均
    ma = series.rolling(window=period, center=True).mean()

    # 季節性成分
    seasonal_component = series / ma

    # 期間別平均季節性指数
    if period == 12:  # 月次
        seasonal_index = seasonal_component.groupby(seasonal_component.index.month).mean()
    elif period == 7:  # 週次
        seasonal_index = seasonal_component.groupby(seasonal_component.index.dayofweek).mean()
    else:
        seasonal_index = seasonal_component.groupby(seasonal_component.index.dayofyear % period).mean()

    return seasonal_index

# 月別季節性指数
monthly_seasonal_index = calculate_seasonal_index(ts_data['value'], 12)
print(f"\n📊 月別季節性指数:")
for month, index in monthly_seasonal_index.items():
    print(f"{month}月: {index:.3f}")

print("\n8. 異常値検出と外れ値分析")
print("=" * 40)

# 時系列異常値検出
def detect_timeseries_outliers(series, method='iqr', window=30):
    """時系列データの異常値検出"""

    if method == 'iqr':
        # IQR法
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = (series < lower_bound) | (series > upper_bound)

    elif method == 'rolling_iqr':
        # 移動窓IQR法
        rolling_q1 = series.rolling(window=window).quantile(0.25)
        rolling_q3 = series.rolling(window=window).quantile(0.75)
        rolling_iqr = rolling_q3 - rolling_q1
        lower_bound = rolling_q1 - 1.5 * rolling_iqr
        upper_bound = rolling_q3 + 1.5 * rolling_iqr
        outliers = (series < lower_bound) | (series > upper_bound)

    elif method == 'std':
        # 標準偏差法
        mean = series.mean()
        std = series.std()
        outliers = abs(series - mean) > 3 * std

    elif method == 'rolling_std':
        # 移動窓標準偏差法
        rolling_mean = series.rolling(window=window).mean()
        rolling_std = series.rolling(window=window).std()
        outliers = abs(series - rolling_mean) > 3 * rolling_std

    return outliers

# 各種異常値検出の実行
outlier_methods = ['iqr', 'rolling_iqr', 'std', 'rolling_std']
outlier_results = {}

for method in outlier_methods:
    outliers = detect_timeseries_outliers(ts_data['value'], method=method)
    outlier_results[method] = outliers
    print(f"{method}法: {outliers.sum()}個の異常値を検出")

# 異常値の詳細分析
print("\n🔍 異常値の詳細分析:")

# rolling_iqr法の結果を使用
outliers = outlier_results['rolling_iqr']
outlier_data = ts_data[outliers].copy()

if len(outlier_data) > 0:
    print(f"異常値発生日数: {len(outlier_data)}日")
    print(f"異常値の平均値: {outlier_data['value'].mean():.0f}")
    print(f"正常値の平均値: {ts_data[~outliers]['value'].mean():.0f}")

    # 異常値の月別分布
    outlier_monthly = outlier_data.groupby(outlier_data.index.month).size()
    print("\n月別異常値発生数:")
    for month, count in outlier_monthly.items():
        print(f"{month}月: {count}回")

print("\n9. 予測モデリングの基礎")
print("=" * 40)

print("🔮 簡易予測モデル:")

# 単純移動平均予測
def simple_moving_average_forecast(series, window=30, periods=7):
    """単純移動平均による予測"""
    last_values = series.tail(window)
    forecast = [last_values.mean()] * periods
    return forecast

# 指数平滑化予測
def exponential_smoothing_forecast(series, alpha=0.3, periods=7):
    """指数平滑化による予測"""
    # 初期値
    s = [series.iloc[0]]

    # 指数平滑化計算
    for i in range(1, len(series)):
        s.append(alpha * series.iloc[i] + (1 - alpha) * s[i-1])

    # 予測
    forecast = [s[-1]] * periods
    return forecast

# 線形トレンド予測
def linear_trend_forecast(series, periods=7):
    """線形トレンド予測"""
    from sklearn.linear_model import LinearRegression

    # データ準備
    X = np.arange(len(series)).reshape(-1, 1)
    y = series.values

    # モデル学習
    model = LinearRegression()
    model.fit(X, y)

    # 予測
    future_X = np.arange(len(series), len(series) + periods).reshape(-1, 1)
    forecast = model.predict(future_X)

    return forecast

# 各予測手法の実行
forecast_methods = {
    '移動平均': simple_moving_average_forecast,
    '指数平滑化': exponential_smoothing_forecast,
    '線形トレンド': linear_trend_forecast
}

forecast_results = {}
train_data = ts_data['value'].iloc[:-7]  # 最後の7日を除いて学習
actual_values = ts_data['value'].iloc[-7:].values  # 実際の値

print("📊 予測結果:")
for method_name, method_func in forecast_methods.items():
    try:
        if method_name == '指数平滑化':
            forecast = method_func(train_data, alpha=0.3, periods=7)
        else:
            forecast = method_func(train_data, periods=7)

        forecast_results[method_name] = forecast

        # 予測精度（MAPE）
        mape = np.mean(np.abs((actual_values - forecast) / actual_values)) * 100
        print(f"{method_name}: MAPE = {mape:.2f}%")

    except Exception as e:
        print(f"{method_name}: エラー - {e}")

print("\n10. 時系列データの可視化分析")
print("=" * 40)

# 統計的サマリー
print("📈 時系列統計サマリー:")

def timeseries_summary(series):
    """時系列データの統計サマリー"""
    summary = {
        '観測数': len(series),
        '平均': series.mean(),
        '中央値': series.median(),
        '標準偏差': series.std(),
        '最小値': series.min(),
        '最大値': series.max(),
        '範囲': series.max() - series.min(),
        '変動係数': series.std() / series.mean(),
        '歪度': series.skew(),
        '尖度': series.kurtosis()
    }
    return pd.Series(summary)

ts_summary = timeseries_summary(ts_data['value'])
print(ts_summary.round(3))

# 自己相関分析（簡易版）
def calculate_autocorrelation(series, max_lags=30):
    """自己相関の計算"""
    autocorr = {}
    for lag in range(1, max_lags + 1):
        lagged_series = series.shift(lag)
        correlation = series.corr(lagged_series)
        autocorr[lag] = correlation
    return pd.Series(autocorr)

autocorr_result = calculate_autocorrelation(ts_data['value'])
print(f"\n🔄 自己相関分析（上位5ラグ）:")
top_autocorr = autocorr_result.abs().nlargest(5)
for lag, corr in top_autocorr.items():
    print(f"ラグ{lag}: {corr:.3f}")

print("\n11. 実務時系列分析パイプライン")
print("=" * 40)

class TimeSeriesAnalyzer:
    """時系列分析総合クラス"""

    def __init__(self):
        self.data = None
        self.analysis_results = {}

    def load_data(self, data, date_column=None, value_column=None):
        """データの読み込み"""
        if date_column and value_column:
            self.data = data.set_index(date_column)[value_column]
        else:
            self.data = data

        print(f"データ読み込み完了: {len(self.data)}観測値")

    def basic_analysis(self):
        """基本分析"""
        if self.data is None:
            raise ValueError("データが読み込まれていません")

        # 基本統計
        self.analysis_results['basic_stats'] = {
            '観測数': len(self.data),
            '平均': self.data.mean(),
            '標準偏差': self.data.std(),
            '最小値': self.data.min(),
            '最大値': self.data.max()
        }

        # トレンド分析
        ma_short = self.data.rolling(window=7).mean()
        ma_long = self.data.rolling(window=30).mean()

        trend_up = (ma_short > ma_long).sum()
        trend_down = (ma_short < ma_long).sum()

        self.analysis_results['trend'] = {
            '上昇トレンド日数': trend_up,
            '下降トレンド日数': trend_down,
            'トレンド強度': abs(ma_short.diff()).mean()
        }

        return self.analysis_results

    def seasonal_analysis(self):
        """季節性分析"""
        if self.data is None:
            raise ValueError("データが読み込まれていません")

        # 月別パターン
        monthly = self.data.groupby(self.data.index.month).agg(['mean', 'std'])

        # 曜日別パターン
        weekly = self.data.groupby(self.data.index.dayofweek).agg(['mean', 'std'])

        self.analysis_results['seasonality'] = {
            'monthly_pattern': monthly,
            'weekly_pattern': weekly,
            'monthly_volatility': monthly['std'].mean(),
            'weekly_volatility': weekly['std'].mean()
        }

        return self.analysis_results['seasonality']

    def anomaly_detection(self, method='rolling_iqr', window=30):
        """異常値検出"""
        if self.data is None:
            raise ValueError("データが読み込まれていません")

        outliers = detect_timeseries_outliers(self.data, method=method, window=window)

        self.analysis_results['anomalies'] = {
            'outlier_count': outliers.sum(),
            'outlier_ratio': outliers.sum() / len(self.data),
            'outlier_dates': self.data[outliers].index.tolist(),
            'outlier_values': self.data[outliers].values.tolist()
        }

        return self.analysis_results['anomalies']

    def generate_report(self):
        """総合レポート生成"""
        report = "=== 時系列分析レポート ===\n\n"

        if 'basic_stats' in self.analysis_results:
            report += "【基本統計】\n"
            for key, value in self.analysis_results['basic_stats'].items():
                report += f"- {key}: {value:.2f}\n"
            report += "\n"

        if 'trend' in self.analysis_results:
            report += "【トレンド分析】\n"
            for key, value in self.analysis_results['trend'].items():
                report += f"- {key}: {value:.2f}\n"
            report += "\n"

        if 'anomalies' in self.analysis_results:
            report += "【異常値分析】\n"
            anomalies = self.analysis_results['anomalies']
            report += f"- 異常値数: {anomalies['outlier_count']}\n"
            report += f"- 異常値率: {anomalies['outlier_ratio']:.2%}\n"
            report += "\n"

        return report

# 分析器の使用例
analyzer = TimeSeriesAnalyzer()
analyzer.load_data(ts_data['value'])

# 分析実行
basic_results = analyzer.basic_analysis()
seasonal_results = analyzer.seasonal_analysis()
anomaly_results = analyzer.anomaly_detection()

# レポート生成
print("📋 時系列分析レポート:")
print(analyzer.generate_report())

print("\n✅ Week 6 完了：集計・時系列分析をマスターしました！")
```

---

## Week 7: 高度な可視化と統計分析

### 🎯 **この週のゴール**

- pandas と可視化ライブラリの連携をマスターする
- 統計的分析手法を習得する
- ビジネスダッシュボードを構築する
- データストーリーテリングのスキルを身につける

---

### **Day 1-4: 高度な可視化テクニック**

```python
print("\n📊 Week 7: 高度な可視化と統計分析")
print("=" * 50)

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
import matplotlib.patches as mpatches
from scipy import stats
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 日本語フォント設定
plt.rcParams['font.family'] = 'DejaVu Sans'
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

print("1. pandasと可視化ライブラリの統合")
print("=" * 40)

# 可視化用のリッチなデータセット作成
np.random.seed(42)
visualization_data = []

for i in range(1000):
    date = pd.Timestamp('2023-01-01') + pd.Timedelta(days=np.random.randint(0, 365))
    customer_type = np.random.choice(['新規', 'リピート', 'VIP'], p=[0.3, 0.5, 0.2])

    # 顧客タイプによる購入行動の違い
    if customer_type == '新規':
        purchase_amount = np.random.exponential(500)
        satisfaction = np.random.normal(3.5, 0.8)
    elif customer_type == 'リピート':
        purchase_amount = np.random.exponential(800)
        satisfaction = np.random.normal(4.0, 0.6)
    else:  # VIP
        purchase_amount = np.random.exponential(1500)
        satisfaction = np.random.normal(4.5, 0.4)

    visualization_data.append({
        'date': date,
        'customer_type': customer_type,
        'purchase_amount': purchase_amount,
        'satisfaction': max(1, min(5, satisfaction)),
        'age': np.random.randint(18, 70),
        'region': np.random.choice(['関東', '関西', '中部', '九州']),
        'product_category': np.random.choice(['Electronics', 'Fashion', 'Books', 'Sports']),
        'marketing_channel': np.random.choice(['Web', '店舗', 'SNS', 'メール'])
    })

viz_df = pd.DataFrame(visualization_data)

print("📊 可視化用データセット:")
print(viz_df.head())
print(f"\nデータ形状: {viz_df.shape}")

print("\n🎨 高度な matplotlib 可視化:")

# 1. 複合グラフ（売上トレンド + 満足度）
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 12))

# 日次売上トレンド
daily_sales = viz_df.groupby('date').agg({
    'purchase_amount': 'sum',
    'satisfaction': 'mean'
}).reset_index()

ax1.plot(daily_sales['date'], daily_sales['purchase_amount'],
         color='blue', linewidth=2, alpha=0.7, label='日次売上')
ax1.fill_between(daily_sales['date'], daily_sales['purchase_amount'],
                alpha=0.3, color='blue')
ax1.set_title('日次売上推移', fontsize=14, fontweight='bold')
ax1.set_ylabel('売上金額')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 顧客タイプ別購入金額分布
viz_df.boxplot(column='purchase_amount', by='customer_type', ax=ax2)
ax2.set_title('顧客タイプ別購入金額分布', fontsize=14, fontweight='bold')
ax2.set_xlabel('顧客タイプ')
ax2.set_ylabel('購入金額')

# 地域別売上構成
region_sales = viz_df.groupby('region')['purchase_amount'].sum()
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
wedges, texts, autotexts = ax3.pie(region_sales.values, labels=region_sales.index,
                                  autopct='%1.1f%%', colors=colors, startangle=90)
ax3.set_title('地域別売上構成比', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

print("\n🔥 seaborn による高度な統計可視化:")

# 2. 相関ヒートマップ
plt.figure(figsize=(10, 8))
numeric_cols = ['purchase_amount', 'satisfaction', 'age']
correlation_matrix = viz_df[numeric_cols].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, fmt='.3f', cbar_kws={'label': '相関係数'})
plt.title('変数間相関ヒートマップ', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# 3. ペアプロット（散布図マトリックス）
g = sns.pairplot(viz_df[numeric_cols + ['customer_type']],
                hue='customer_type', diag_kind='kde',
                plot_kws={'alpha': 0.6})
g.fig.suptitle('変数間関係性分析', y=1.02, fontsize=16, fontweight='bold')
plt.show()

# 4. ファセットグリッド
g = sns.FacetGrid(viz_df, col='region', row='customer_type',
                 height=4, aspect=1.2)
g.map(plt.scatter, 'age', 'purchase_amount', alpha=0.6)
g.add_legend()
g.fig.suptitle('地域×顧客タイプ別 年齢vs購入金額', y=1.02, fontsize=16)
plt.show()

print("\n⚡ Plotly による インタラクティブ可視化:")

# 5. インタラクティブ散布図
fig = px.scatter(viz_df, x='age', y='purchase_amount',
                color='customer_type', size='satisfaction',
                hover_data=['region', 'product_category'],
                title='年齢 vs 購入金額（インタラクティブ）')
fig.show()

# 6. 時系列インタラクティブグラフ
monthly_trend = viz_df.groupby([viz_df['date'].dt.to_period('M'), 'customer_type']).agg({
    'purchase_amount': 'sum'
}).reset_index()
monthly_trend['date'] = monthly_trend['date'].astype(str)

fig = px.line(monthly_trend, x='date', y='purchase_amount',
             color='customer_type', title='月次売上推移（顧客タイプ別）')
fig.update_layout(xaxis_title='月', yaxis_title='売上金額')
fig.show()

print("\n2. 統計的分析の実装")
print("=" * 40)

print("📊 記述統計学:")

# 基本統計量の拡張計算
def enhanced_describe(df, column):
    """拡張記述統計"""
    series = df[column]

    basic_stats = series.describe()

    # 追加統計量
    additional_stats = pd.Series({
        '範囲': series.max() - series.min(),
        '四分位範囲': series.quantile(0.75) - series.quantile(0.25),
        '変動係数': series.std() / series.mean(),
        '歪度': stats.skew(series),
        '尖度': stats.kurtosis(series),
        '5%パーセンタイル': series.quantile(0.05),
        '95%パーセンタイル': series.quantile(0.95)
    })

    return pd.concat([basic_stats, additional_stats])

purchase_stats = enhanced_describe(viz_df, 'purchase_amount')
print("購入金額の拡張統計:")
print(purchase_stats.round(3))

print("\n🔬 推定統計学:")

# 信頼区間の計算
def confidence_interval(data, confidence=0.95):
    """信頼区間の計算"""
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)
    margin_error = std_err * stats.t.ppf((1 + confidence) / 2, n - 1)

    return mean - margin_error, mean + margin_error

# 顧客タイプ別の信頼区間
print("顧客タイプ別購入金額の95%信頼区間:")
for customer_type in viz_df['customer_type'].unique():
    data = viz_df[viz_df['customer_type'] == customer_type]['purchase_amount']
    ci_lower, ci_upper = confidence_interval(data)
    print(f"{customer_type}: [{ci_lower:.2f}, {ci_upper:.2f}]")

print("\n🧪 仮説検定:")

# 1. 顧客タイプ間の平均購入金額の差の検定（ANOVA）
groups = [group['purchase_amount'].values for name, group in viz_df.groupby('customer_type')]
f_stat, p_value = stats.f_oneway(*groups)

print(f"ANOVA検定結果:")
print(f"F統計量: {f_stat:.4f}")
print(f"p値: {p_value:.4f}")
print(f"結果: {'有意差あり' if p_value < 0.05 else '有意差なし'}")

# 2. 二群間の平均の差の検定（t検定）
new_customers = viz_df[viz_df['customer_type'] == '新規']['purchase_amount']
vip_customers = viz_df[viz_df['customer_type'] == 'VIP']['purchase_amount']

t_stat, p_value = stats.ttest_ind(new_customers, vip_customers)
print(f"\n新規 vs VIP顧客のt検定:")
print(f"t統計量: {t_stat:.4f}")
print(f"p値: {p_value:.4f}")

# 3. 相関係数の有意性検定
corr_coef, p_value = stats.pearsonr(viz_df['age'], viz_df['purchase_amount'])
print(f"\n年齢と購入金額の相関:")
print(f"相関係数: {corr_coef:.4f}")
print(f"p値: {p_value:.4f}")

print("\n📈 回帰分析:")

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# 特徴量エンジニアリング
viz_df_encoded = viz_df.copy()

# カテゴリ変数のエンコーディング
label_encoders = {}
categorical_cols = ['customer_type', 'region', 'product_category', 'marketing_channel']

for col in categorical_cols:
    le = LabelEncoder()
    viz_df_encoded[col + '_encoded'] = le.fit_transform(viz_df_encoded[col])
    label_encoders[col] = le

# 特徴量とターゲット変数の準備
feature_cols = ['age', 'satisfaction'] + [col + '_encoded' for col in categorical_cols]
X = viz_df_encoded[feature_cols]
y = viz_df_encoded['purchase_amount']

# 訓練・テストデータ分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 線形回帰モデル
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# 予測と評価
y_pred = lr_model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"線形回帰モデル性能:")
print(f"R²スコア: {r2:.4f}")
print(f"RMSE: {rmse:.2f}")

# 特徴量重要度
feature_importance = pd.DataFrame({
    'feature': feature_cols,
    'coefficient': lr_model.coef_,
    'abs_coefficient': np.abs(lr_model.coef_)
}).sort_values('abs_coefficient', ascending=False)

print(f"\n特徴量重要度（上位5）:")
print(feature_importance.head())

print("\n3. ビジネスダッシュボード構築")
print("=" * 40)

class BusinessDashboard:
    """ビジネスダッシュボードクラス"""

    def __init__(self, data):
        self.data = data
        self.kpis = {}
        self.charts = {}

    def calculate_kpis(self):
        """主要指標の計算"""
        self.kpis = {
            '総売上': self.data['purchase_amount'].sum(),
            '総顧客数': self.data.shape[0],
            '平均購入金額': self.data['purchase_amount'].mean(),
            '平均満足度': self.data['satisfaction'].mean(),
            'VIP顧客比率': (self.data['customer_type'] == 'VIP').mean() * 100,
            '新規顧客比率': (self.data['customer_type'] == '新規').mean() * 100
        }
        return self.kpis

    def create_summary_dashboard(self):
        """サマリーダッシュボード作成"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

        # 1. 売上トレンド
        daily_sales = self.data.groupby('date')['purchase_amount'].sum().reset_index()
        ax1.plot(daily_sales['date'], daily_sales['purchase_amount'],
                color='#2E86AB', linewidth=2)
        ax1.fill_between(daily_sales['date'], daily_sales['purchase_amount'],
                        alpha=0.3, color='#2E86AB')
        ax1.set_title('日次売上推移', fontsize=14, fontweight='bold')
        ax1.set_ylabel('売上金額')
        ax1.grid(True, alpha=0.3)

        # 2. 顧客タイプ別構成比
        customer_counts = self.data['customer_type'].value_counts()
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
        ax2.pie(customer_counts.values, labels=customer_counts.index,
               autopct='%1.1f%%', colors=colors)
        ax2.set_title('顧客タイプ別構成比', fontsize=14, fontweight='bold')

        # 3. 地域別売上
        region_sales = self.data.groupby('region')['purchase_amount'].sum().sort_values(ascending=True)
        bars = ax3.barh(region_sales.index, region_sales.values, color='#96CEB4')
        ax3.set_title('地域別売上', fontsize=14, fontweight='bold')
        ax3.set_xlabel('売上金額')

        # バーに値を表示
        for i, (bar, value) in enumerate(zip(bars, region_sales.values)):
            ax3.text(value + max(region_sales.values) * 0.01, i,
                    f'{value:,.0f}', va='center', fontsize=10)

        # 4. 満足度分布
        ax4.hist(self.data['satisfaction'], bins=20, color='#FFEAA7',
                alpha=0.7, edgecolor='black')
        ax4.axvline(self.data['satisfaction'].mean(), color='red',
                   linestyle='--', linewidth=2, label=f'平均: {self.data["satisfaction"].mean():.2f}')
        ax4.set_title('顧客満足度分布', fontsize=14, fontweight='bold')
        ax4.set_xlabel('満足度')
        ax4.set_ylabel('頻度')
        ax4.legend()

        plt.tight_layout()
        plt.show()

        return fig

    def create_kpi_summary(self):
        """KPIサマリー表示"""
        print("=" * 50)
        print("          📊 KPI ダッシュボード 📊")
        print("=" * 50)

        for kpi_name, kpi_value in self.kpis.items():
            if 'ratio' in kpi_name.lower() or '比率' in kpi_name:
                print(f"{kpi_name:12}: {kpi_value:6.1f}%")
            elif '金額' in kpi_name or '売上' in kpi_name:
                print(f"{kpi_name:12}: ¥{kpi_value:10,.0f}")
            elif '顧客数' in kpi_name:
                print(f"{kpi_name:12}: {kpi_value:7,.0f}人")
            else:
                print(f"{kpi_name:12}: {kpi_value:10.2f}")

        print("=" * 50)

    def create_advanced_analysis(self):
        """高度な分析レポート"""
        print("\n📈 高度な分析レポート")
        print("-" * 30)

        # 顧客セグメント分析
        segment_analysis = self.data.groupby('customer_type').agg({
            'purchase_amount': ['count', 'mean', 'sum'],
            'satisfaction': 'mean',
            'age': 'mean'
        }).round(2)

        print("顧客セグメント分析:")
        print(segment_analysis)

        # チャネル効果分析
        channel_analysis = self.data.groupby('marketing_channel').agg({
            'purchase_amount': ['count', 'mean'],
            'satisfaction': 'mean'
        }).round(2)

        print("\nマーケティングチャネル分析:")
        print(channel_analysis)

        # 地域別パフォーマンス
        region_performance = self.data.groupby('region').agg({
            'purchase_amount': ['sum', 'mean'],
            'satisfaction': 'mean'
        }).round(2)

        print("\n地域別パフォーマンス:")
        print(region_performance)

# ダッシュボード使用例
dashboard = BusinessDashboard(viz_df)
kpis = dashboard.calculate_kpis()

dashboard.create_kpi_summary()
dashboard_fig = dashboard.create_summary_dashboard()
dashboard.create_advanced_analysis()

print("\n✅ Week 7 Day 1-4 完了：高度な可視化をマスターしました！")
```

### **Day 5-7: データストーリーテリングと実践分析**

````python
print("\n4. データストーリーテリング")
print("=" * 40)

print("📖 効果的なデータストーリーの構築:")

class DataStoryTeller:
    """データストーリーテリングクラス"""

    def __init__(self, data):
        self.data = data
        self.story_elements = {}
        self.insights = []
        self.recommendations = []

    def analyze_business_context(self):
        """ビジネス文脈の分析"""
        print("🎯 ビジネス課題の特定:")

        # 売上の時系列パターン分析
        daily_sales = self.data.groupby('date')['purchase_amount'].sum()

        # トレンド分析
        sales_trend = daily_sales.rolling(window=30).mean()
        trend_direction = 'increasing' if sales_trend.iloc[-1] > sales_trend.iloc[0] else 'decreasing'

        # 季節性分析
        monthly_sales = self.data.groupby(self.data['date'].dt.month)['purchase_amount'].mean()
        seasonal_variance = monthly_sales.std() / monthly_sales.mean()

        # 顧客セグメント分析
        segment_revenue = self.data.groupby('customer_type')['purchase_amount'].sum()
        top_segment = segment_revenue.idxmax()

        self.story_elements['context'] = {
            'trend_direction': trend_direction,
            'seasonal_variance': seasonal_variance,
            'top_segment': top_segment,
            'total_revenue': self.data['purchase_amount'].sum(),
            'customer_count': len(self.data)
        }

        print(f"📊 売上トレンド: {trend_direction}")
        print(f"📅 季節変動係数: {seasonal_variance:.3f}")
        print(f"👑 最高収益セグメント: {top_segment}")

        return self.story_elements['context']

    def identify_key_insights(self):
        """主要インサイトの特定"""
        print("\n💡 主要インサイト:")

        insights = []

        # インサイト1: 顧客タイプ別の収益性
        revenue_by_type = self.data.groupby('customer_type').agg({
            'purchase_amount': ['sum', 'mean', 'count']
        })

        vip_avg = revenue_by_type.loc['VIP', ('purchase_amount', 'mean')]
        new_avg = revenue_by_type.loc['新規', ('purchase_amount', 'mean')]
        vip_premium = (vip_avg / new_avg - 1) * 100

        insights.append({
            'type': 'revenue_gap',
            'message': f"VIP顧客の平均購入金額は新規顧客の{vip_premium:.0f}%高い",
            'impact': 'high',
            'data': {'vip_avg': vip_avg, 'new_avg': new_avg}
        })

        # インサイト2: 地域格差
        region_performance = self.data.groupby('region')['purchase_amount'].agg(['sum', 'mean'])
        top_region = region_performance['sum'].idxmax()
        bottom_region = region_performance['sum'].idxmin()
        region_gap = region_performance.loc[top_region, 'sum'] / region_performance.loc[bottom_region, 'sum']

        insights.append({
            'type': 'regional_disparity',
            'message': f"{top_region}の売上は{bottom_region}の{region_gap:.1f}倍",
            'impact': 'medium',
            'data': {'top_region': top_region, 'bottom_region': bottom_region, 'gap': region_gap}
        })

        # インサイト3: 満足度と購入金額の関係
        high_satisfaction = self.data[self.data['satisfaction'] >= 4.5]
        low_satisfaction = self.data[self.data['satisfaction'] < 3.5]

        if len(high_satisfaction) > 0 and len(low_satisfaction) > 0:
            satisfaction_impact = (high_satisfaction['purchase_amount'].mean() /
                                 low_satisfaction['purchase_amount'].mean() - 1) * 100

            insights.append({
                'type': 'satisfaction_correlation',
                'message': f"高満足度顧客は低満足度顧客より{satisfaction_impact:.0f}%多く購入",
                'impact': 'high',
                'data': {'satisfaction_impact': satisfaction_impact}
            })

        # インサイト4: チャネル効果
        channel_performance = self.data.groupby('marketing_channel').agg({
            'purchase_amount': ['mean', 'count']
        })

        best_channel = channel_performance[('purchase_amount', 'mean')].idxmax()
        worst_channel = channel_performance[('purchase_amount', 'mean')].idxmin()
        channel_diff = (channel_performance.loc[best_channel, ('purchase_amount', 'mean')] /
                       channel_performance.loc[worst_channel, ('purchase_amount', 'mean')] - 1) * 100

        insights.append({
            'type': 'channel_effectiveness',
            'message': f"{best_channel}チャネルは{worst_channel}より{channel_diff:.0f}%効果的",
            'impact': 'medium',
            'data': {'best_channel': best_channel, 'worst_channel': worst_channel}
        })

        self.insights = insights

        # インサイトを表示
        for i, insight in enumerate(insights, 1):
            impact_icon = "🔥" if insight['impact'] == 'high' else "⚡" if insight['impact'] == 'medium' else "💡"
            print(f"{impact_icon} インサイト{i}: {insight['message']}")

        return insights

    def generate_recommendations(self):
        """推奨アクションの生成"""
        print("\n🎯 推奨アクション:")

        recommendations = []

        # インサイトベースの推奨事項
        for insight in self.insights:
            if insight['type'] == 'revenue_gap':
                recommendations.append({
                    'priority': 'high',
                    'action': 'VIP顧客向けプレミアムサービス拡充',
                    'reasoning': 'VIP顧客の高い購買力を活かす',
                    'expected_impact': '売上15-20%向上'
                })

                recommendations.append({
                    'priority': 'medium',
                    'action': '新規顧客のVIP転換プログラム開発',
                    'reasoning': '新規顧客を高価値顧客に育成',
                    'expected_impact': '顧客生涯価値30%向上'
                })

            elif insight['type'] == 'regional_disparity':
                recommendations.append({
                    'priority': 'medium',
                    'action': '低パフォーマンス地域のマーケティング強化',
                    'reasoning': '地域格差の解消により全体売上底上げ',
                    'expected_impact': '地域売上10-15%向上'
                })

            elif insight['type'] == 'satisfaction_correlation':
                recommendations.append({
                    'priority': 'high',
                    'action': '顧客満足度向上プログラム実施',
                    'reasoning': '満足度向上が直接的に売上向上につながる',
                    'expected_impact': '平均購入金額10-12%向上'
                })

            elif insight['type'] == 'channel_effectiveness':
                recommendations.append({
                    'priority': 'medium',
                    'action': '効果的チャネルへの予算配分見直し',
                    'reasoning': 'ROIの高いチャネルに集中投資',
                    'expected_impact': 'マーケティングROI20%向上'
                })

        self.recommendations = recommendations

        # 推奨事項を表示
        for i, rec in enumerate(recommendations, 1):
            priority_icon = "🚨" if rec['priority'] == 'high' else "⚠️" if rec['priority'] == 'medium' else "💭"
            print(f"{priority_icon} 推奨{i}: {rec['action']}")
            print(f"   理由: {rec['reasoning']}")
            print(f"   期待効果: {rec['expected_impact']}")
            print()

        return recommendations

    def create_executive_summary(self):
        """エグゼクティブサマリー作成"""
        context = self.story_elements['context']

        summary = f"""
=== エグゼクティブサマリー ===

【現状】
• 総売上: ¥{context['total_revenue']:,.0f}
• 総顧客数: {context['customer_count']:,}人
• 売上トレンド: {context['trend_direction']}
• 主力セグメント: {context['top_segment']}顧客

【主要課題】
"""

        # 高インパクトインサイトを追加
        high_impact_insights = [i for i in self.insights if i['impact'] == 'high']
        for insight in high_impact_insights:
            summary += f"• {insight['message']}\n"

        summary += "\n【推奨アクション】\n"

        # 高優先度推奨事項を追加
        high_priority_recs = [r for r in self.recommendations if r['priority'] == 'high']
        for rec in high_priority_recs:
            summary += f"• {rec['action']}\n"

        summary += f"\n【期待効果】\n• 総合的な売上向上: 20-30%\n• 顧客満足度向上: 15-20%\n"

        return summary

# データストーリーテリング実行
storyteller = DataStoryTeller(viz_df)

# ストーリー構築
context = storyteller.analyze_business_context()
insights = storyteller.identify_key_insights()
recommendations = storyteller.generate_recommendations()

# エグゼクティブサマリー
executive_summary = storyteller.create_executive_summary()
print(executive_summary)

print("\n5. A/Bテスト分析")
print("=" * 40)

# A/Bテストデータの生成
print("🧪 A/Bテスト分析:")

np.random.seed(42)
ab_test_data = []

for i in range(2000):
    # テストグループの割り当て
    test_group = np.random.choice(['A', 'B'], p=[0.5, 0.5])

    # グループAとBで異なる効果
    if test_group == 'A':
        conversion_rate = 0.15  # ベースライン
        purchase_amount = np.random.exponential(800)
    else:
        conversion_rate = 0.18  # 3%ポイント向上
        purchase_amount = np.random.exponential(850)  # 平均金額も向上

    # コンバージョンの決定
    converted = np.random.random() < conversion_rate

    ab_test_data.append({
        'user_id': f'U{i+1:04d}',
        'test_group': test_group,
        'converted': converted,
        'purchase_amount': purchase_amount if converted else 0,
        'days_active': np.random.randint(1, 30)
    })

ab_df = pd.DataFrame(ab_test_data)

print("A/Bテストデータ:")
print(ab_df.head())

# A/Bテスト分析関数
def ab_test_analysis(df, group_col, metric_col, alpha=0.05):
    """A/Bテスト統計分析"""

    results = {}

    # グループ別基本統計
    group_stats = df.groupby(group_col)[metric_col].agg(['count', 'mean', 'std'])
    results['group_stats'] = group_stats

    # 統計的検定
    group_a = df[df[group_col] == 'A'][metric_col]
    group_b = df[df[group_col] == 'B'][metric_col]

    # t検定
    t_stat, p_value = stats.ttest_ind(group_a, group_b)

    # 効果サイズ（Cohen's d）
    pooled_std = np.sqrt(((len(group_a) - 1) * group_a.std()**2 +
                         (len(group_b) - 1) * group_b.std()**2) /
                        (len(group_a) + len(group_b) - 2))
    effect_size = (group_b.mean() - group_a.mean()) / pooled_std

    # 信頼区間
    ci_a = confidence_interval(group_a)
    ci_b = confidence_interval(group_b)

    results['statistical_test'] = {
        't_statistic': t_stat,
        'p_value': p_value,
        'effect_size': effect_size,
        'significant': p_value < alpha,
        'confidence_interval_a': ci_a,
        'confidence_interval_b': ci_b
    }

    return results

# コンバージョン率のA/Bテスト
conversion_results = ab_test_analysis(ab_df, 'test_group', 'converted')

print("\n📊 コンバージョン率A/Bテスト結果:")
print("グループ別統計:")
print(conversion_results['group_stats'])

test_results = conversion_results['statistical_test']
print(f"\n統計的検定:")
print(f"t統計量: {test_results['t_statistic']:.4f}")
print(f"p値: {test_results['p_value']:.4f}")
print(f"効果サイズ: {test_results['effect_size']:.4f}")
print(f"統計的有意性: {'あり' if test_results['significant'] else 'なし'}")

# 購入金額のA/Bテスト（コンバージョンした顧客のみ）
converted_users = ab_df[ab_df['converted'] == True]
if len(converted_users) > 0:
    purchase_results = ab_test_analysis(converted_users, 'test_group', 'purchase_amount')

    print("\n💰 購入金額A/Bテスト結果（コンバージョン顧客のみ）:")
    print("グループ別統計:")
    print(purchase_results['group_stats'])

print("\n6. コホート分析")
print("=" * 40)

print("👥 コホート分析:")

# コホート分析データの生成
cohort_data = []
np.random.seed(42)

start_date = pd.Timestamp('2023-01-01')
for cohort_month in range(12):  # 12ヶ月のコホート
    cohort_start = start_date + pd.DateOffset(months=cohort_month)
    initial_users = np.random.randint(100, 500)  # 初期ユーザー数

    for period in range(12 - cohort_month):  # 観測期間
        # リテンション率（時間とともに減少）
        retention_rate = 1.0 * (0.85 ** period)  # 月15%ずつ減少
        retained_users = int(initial_users * retention_rate)

        # 1人あたりの売上（時間とともに増加傾向）
        revenue_per_user = 100 + period * 10 + np.random.normal(0, 20)
        total_revenue = retained_users * max(0, revenue_per_user)

        cohort_data.append({
            'cohort_month': cohort_start.strftime('%Y-%m'),
            'period': period,
            'initial_users': initial_users,
            'retained_users': retained_users,
            'retention_rate': retained_users / initial_users,
            'revenue_per_user': revenue_per_user,
            'total_revenue': total_revenue
        })

cohort_df = pd.DataFrame(cohort_data)

print("コホートデータサンプル:")
print(cohort_df.head(10))

# コホートテーブルの作成
def create_cohort_table(df, cohort_col, period_col, metric_col):
    """コホートテーブル作成"""
    cohort_table = df.pivot_table(
        index=cohort_col,
        columns=period_col,
        values=metric_col,
        fill_value=0
    )
    return cohort_table

# リテンション率のコホートテーブル
retention_cohort = create_cohort_table(cohort_df, 'cohort_month', 'period', 'retention_rate')

print("\n📊 リテンション率コホートテーブル:")
print(retention_cohort.round(3))

# ユーザーあたり売上のコホートテーブル
revenue_cohort = create_cohort_table(cohort_df, 'cohort_month', 'period', 'revenue_per_user')

print("\n💰 ユーザーあたり売上コホートテーブル:")
print(revenue_cohort.round(0))

# コホート分析の可視化
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# リテンション率ヒートマップ
sns.heatmap(retention_cohort, annot=True, fmt='.2f', cmap='YlOrRd', ax=ax1)
ax1.set_title('リテンション率コホート分析')
ax1.set_xlabel('期間（月）')
ax1.set_ylabel('コホート月')

# 売上ヒートマップ
sns.heatmap(revenue_cohort, annot=True, fmt='.0f', cmap='YlGnBu', ax=ax2)
ax2.set_title('ユーザーあたり売上コホート分析')
ax2.set_xlabel('期間（月）')
ax2.set_ylabel('コホート月')

plt.tight_layout()
plt.show()

print("\n✅ Week 7 完了：高度な可視化と統計分析をマスターしました！")

---

## Week 8: 実務プロジェクト総合演習

### 🎯 **この週のゴール**
- これまでの学習内容を統合する
- 実際のビジネス課題を解決する
- 完全なデータ分析パイプラインを構築する
- プロフェッショナルレベルの分析レポートを作成する

---

### **Day 1-7: 総合実務プロジェクト**

```python
print("\n🚀 Week 8: 実務プロジェクト総合演習")
print("=" * 50)

print("プロジェクト概要: ECサイトの売上最適化")
print("""
【背景】
あなたはECサイト運営会社のデータアナリストとして、
売上低迷の原因分析と改善策の提案を求められました。

【データセット】
- 顧客データ（50,000件）
- 商品データ（1,000件）
- 取引データ（200,000件）
- マーケティングデータ（キャンペーン、広告）
- レビューデータ（100,000件）

【目標】
1. 売上低迷の原因特定
2. 顧客セグメンテーション
3. 商品推奨システムの基礎分析
4. マーケティング効果測定
5. 具体的な改善提案

【期待成果物】
- データ分析レポート
- エグゼクティブサマリー
- アクションプラン
- ダッシュボード
""")

import warnings
warnings.filterwarnings('ignore')

print("\n1. データ準備と探索的データ分析")
print("=" * 40)

# 実際のビジネスデータを模擬した大規模データセット生成
class EcommerceDataGenerator:
    """ECサイトデータ生成器"""

    def __init__(self, seed=42):
        np.random.seed(seed)
        self.customers = None
        self.products = None
        self.transactions = None
        self.reviews = None
        self.campaigns = None

    def generate_customers(self, n_customers=50000):
        """顧客データ生成"""
        customers = []

        for i in range(n_customers):
            # 顧客基本情報
            age = np.random.normal(40, 15)
            age = max(18, min(80, age))

            # 年齢に基づく行動パターン
            if age < 30:
                income = np.random.normal(35000, 10000)
                tech_savvy = np.random.uniform(0.7, 1.0)
                price_sensitive = np.random.uniform(0.6, 0.9)
            elif age < 50:
                income = np.random.normal(55000, 20000)
                tech_savvy = np.random.uniform(0.5, 0.8)
                price_sensitive = np.random.uniform(0.4, 0.7)
            else:
                income = np.random.normal(45000, 15000)
                tech_savvy = np.random.uniform(0.3, 0.6)
                price_sensitive = np.random.uniform(0.3, 0.6)

            income = max(15000, income)

            customers.append({
                'customer_id': f'C{i+1:05d}',
                'age': int(age),
                'gender': np.random.choice(['M', 'F']),
                'income': income,
                'registration_date': pd.Timestamp('2022-01-01') + pd.Timedelta(days=np.random.randint(0, 730)),
                'city': np.random.choice(['Tokyo', 'Osaka', 'Nagoya', 'Fukuoka', 'Sapporo'],
                                       p=[0.3, 0.2, 0.15, 0.15, 0.2]),
                'tech_savvy': tech_savvy,
                'price_sensitive': price_sensitive,
                'customer_segment': None  # 後で計算
            })

        self.customers = pd.DataFrame(customers)

        # 顧客セグメント計算
        self.customers['customer_segment'] = self.customers.apply(
            lambda row: self._calculate_segment(row), axis=1
        )

        return self.customers

    def _calculate_segment(self, customer):
        """顧客セグメント計算"""
        if customer['income'] > 60000 and customer['tech_savvy'] > 0.7:
            return 'Premium Tech'
        elif customer['income'] > 50000:
            return 'High Value'
        elif customer['age'] < 35 and customer['tech_savvy'] > 0.6:
            return 'Young Digital'
        elif customer['price_sensitive'] > 0.7:
            return 'Price Conscious'
        else:
            return 'Standard'

    def generate_products(self, n_products=1000):
        """商品データ生成"""
        categories = ['Electronics', 'Fashion', 'Home', 'Books', 'Sports', 'Beauty']
        brands = ['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE']

        products = []

        for i in range(n_products):
            category = np.random.choice(categories)

            # カテゴリ別価格設定
            if category == 'Electronics':
                base_price = np.random.lognormal(6, 1)  # 高価格帯
            elif category == 'Fashion':
                base_price = np.random.lognormal(4, 0.8)
            elif category == 'Home':
                base_price = np.random.lognormal(4.5, 0.9)
            elif category == 'Books':
                base_price = np.random.lognormal(2.5, 0.5)  # 低価格帯
            elif category == 'Sports':
                base_price = np.random.lognormal(4.2, 0.7)
            else:  # Beauty
                base_price = np.random.lognormal(3.5, 0.6)

            products.append({
                'product_id': f'P{i+1:04d}',
                'category': category,
                'brand': np.random.choice(brands),
                'price': round(base_price, 2),
                'cost': round(base_price * np.random.uniform(0.4, 0.7), 2),
                'launch_date': pd.Timestamp('2020-01-01') + pd.Timedelta(days=np.random.randint(0, 1460)),
                'avg_rating': np.random.normal(4.0, 0.8),
                'review_count': np.random.poisson(50),
                'inventory': np.random.randint(0, 1000)
            })

        self.products = pd.DataFrame(products)
        self.products['avg_rating'] = self.products['avg_rating'].clip(1, 5)
        self.products['profit_margin'] = (self.products['price'] - self.products['cost']) / self.products['price']

        return self.products

    def generate_transactions(self, n_transactions=200000):
        """取引データ生成"""
        if self.customers is None or self.products is None:
            raise ValueError("顧客データと商品データを先に生成してください")

        transactions = []

        for i in range(n_transactions):
            # 顧客選択（アクティブ顧客ほど取引確率高）
            customer = self.customers.sample(1).iloc[0]

            # 商品選択（顧客セグメントに基づく選好）
            if customer['customer_segment'] == 'Premium Tech':
                preferred_categories = ['Electronics', 'Beauty']
                price_factor = 1.5
            elif customer['customer_segment'] == 'High Value':
                preferred_categories = ['Fashion', 'Home']
                price_factor = 1.2
            elif customer['customer_segment'] == 'Young Digital':
                preferred_categories = ['Electronics', 'Fashion', 'Sports']
                price_factor = 0.8
            elif customer['customer_segment'] == 'Price Conscious':
                preferred_categories = ['Books', 'Home']
                price_factor = 0.6
            else:
                preferred_categories = list(self.products['category'].unique())
                price_factor = 1.0

            # 商品フィルタリング
            available_products = self.products[
                (self.products['category'].isin(preferred_categories)) &
                (self.products['price'] <= customer['income'] * price_factor / 1000)
            ]

            if len(available_products) == 0:
                available_products = self.products.sample(10)

            product = available_products.sample(1).iloc[0]

            # 取引詳細
            quantity = np.random.randint(1, 5)

            # 季節性効果
            transaction_date = pd.Timestamp('2023-01-01') + pd.Timedelta(days=np.random.randint(0, 365))
            seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * transaction_date.dayofyear / 365)

            # 割引適用
            discount = np.random.uniform(0, 0.3) if np.random.random() < 0.2 else 0

            final_price = product['price'] * (1 - discount) * seasonal_factor

            transactions.append({
                'transaction_id': f'T{i+1:06d}',
                'customer_id': customer['customer_id'],
                'product_id': product['product_id'],
                'transaction_date': transaction_date,
                'quantity': quantity,
                'unit_price': round(final_price, 2),
                'total_amount': round(final_price * quantity, 2),
                'discount': discount,
                'channel': np.random.choice(['Web', 'Mobile', 'Store'], p=[0.5, 0.4, 0.1])
            })

        self.transactions = pd.DataFrame(transactions)
        return self.transactions

    def generate_reviews(self, n_reviews=100000):
        """レビューデータ生成"""
        if self.transactions is None:
            raise ValueError("取引データを先に生成してください")

        # 取引の一部にレビューを付与
        review_transactions = self.transactions.sample(n_reviews, replace=True)

        reviews = []

        for _, transaction in review_transactions.iterrows():
            customer = self.customers[self.customers['customer_id'] == transaction['customer_id']].iloc[0]
            product = self.products[self.products['product_id'] == transaction['product_id']].iloc[0]

            # 顧客セグメントと商品評価に基づくレビュー
            base_rating = product['avg_rating']

            if customer['customer_segment'] == 'Premium Tech':
                rating_adjustment = np.random.normal(0.5, 0.3)
            elif customer['customer_segment'] == 'Price Conscious':
                rating_adjustment = np.random.normal(-0.3, 0.4)
            else:
                rating_adjustment = np.random.normal(0, 0.3)

            final_rating = max(1, min(5, base_rating + rating_adjustment))

            reviews.append({
                'review_id': f'R{len(reviews)+1:06d}',
                'customer_id': transaction['customer_id'],
                'product_id': transaction['product_id'],
                'transaction_id': transaction['transaction_id'],
                'rating': round(final_rating),
                'review_date': transaction['transaction_date'] + pd.Timedelta(days=np.random.randint(1, 30)),
                'helpful_votes': np.random.poisson(3)
            })

        self.reviews = pd.DataFrame(reviews)
        return self.reviews

# データ生成実行
print("📊 大規模データセット生成中...")
data_generator = EcommerceDataGenerator()

customers = data_generator.generate_customers(50000)
products = data_generator.generate_products(1000)
transactions = data_generator.generate_transactions(200000)
reviews = data_generator.generate_reviews(100000)

print("✅ データ生成完了")
print(f"顧客データ: {len(customers):,}件")
print(f"商品データ: {len(products):,}件")
print(f"取引データ: {len(transactions):,}件")
print(f"レビューデータ: {len(reviews):,}件")

print("\n📊 基本的な探索的データ分析:")

# データ概観
print("【顧客データ概要】")
print(customers.describe(include='all'))

print("\n【商品データ概要】")
print(products.describe(include='all'))

print("\n【取引データ概要】")
print(transactions.describe(include='all'))

print("\n2. データ統合と特徴量エンジニアリング")
print("=" * 40)

class EcommerceAnalyzer:
    """ECサイト分析総合クラス"""

    def __init__(self, customers, products, transactions, reviews):
        self.customers = customers
        self.products = products
        self.transactions = transactions
        self.reviews = reviews
        self.integrated_data = None
        self.customer_features = None
        self.product_features = None

    def integrate_data(self):
        """データ統合"""
        print("🔗 データ統合実行中...")

        # 取引データに商品情報を結合
        trans_product = pd.merge(self.transactions, self.products, on='product_id', how='left')

        # 顧客情報を結合
        integrated = pd.merge(trans_product, self.customers, on='customer_id', how='left')

        # レビュー情報を集計して結合
        review_agg = self.reviews.groupby('transaction_id').agg({
            'rating': 'mean',
            'helpful_votes': 'sum'
        }).reset_index()

        integrated = pd.merge(integrated, review_agg, on='transaction_id', how='left')

        self.integrated_data = integrated
        print(f"✅ 統合データ作成完了: {len(integrated):,}行")

        return integrated

    def create_customer_features(self):
        """顧客特徴量作成"""
        print("👥 顧客特徴量エンジニアリング...")

        # 基本的な取引統計
        customer_stats = self.integrated_data.groupby('customer_id').agg({
            'total_amount': ['sum', 'mean', 'count', 'std'],
            'quantity': 'sum',
            'discount': 'mean',
            'rating': 'mean',
            'transaction_date': ['min', 'max']
        }).reset_index()

        # 列名を平坦化
        customer_stats.columns = ['customer_id', 'total_spent', 'avg_order_value', 'order_count',
                                'spend_volatility', 'total_quantity', 'avg_discount', 'avg_rating',
                                'first_purchase', 'last_purchase']

        # 追加特徴量計算
        customer_stats['days_as_customer'] = (customer_stats['last_purchase'] - customer_stats['first_purchase']).dt.days
        customer_stats['purchase_frequency'] = customer_stats['order_count'] / (customer_stats['days_as_customer'] + 1) * 365
        customer_stats['spend_volatility'] = customer_stats['spend_volatility'].fillna(0)

        # RFM分析
        reference_date = self.integrated_data['transaction_date'].max()
        customer_stats['recency'] = (reference_date - customer_stats['last_purchase']).dt.days
        customer_stats['frequency'] = customer_stats['order_count']
        customer_stats['monetary'] = customer_stats['total_spent']

        # RFMスコア計算
        customer_stats['R_score'] = pd.qcut(customer_stats['recency'], 5, labels=[5,4,3,2,1])
        customer_stats['F_score'] = pd.qcut(customer_stats['frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
        customer_stats['M_score'] = pd.qcut(customer_stats['monetary'], 5, labels=[1,2,3,4,5])

        # 総合RFMスコア
        customer_stats['RFM_score'] = (customer_stats['R_score'].astype(int) +
                                     customer_stats['F_score'].astype(int) +
                                     customer_stats['M_score'].astype(int))

        # 顧客基本情報とマージ
        customer_features = pd.merge(customer_stats, self.customers, on='customer_id', how='left')

        # 顧客価値セグメント
        def customer_value_segment(row):
            if row['RFM_score'] >= 12:
                return 'Champions'
            elif row['RFM_score'] >= 10:
                return 'Loyal Customers'
            elif row['RFM_score'] >= 8:
                return 'Potential Loyalists'
            elif row['RFM_score'] >= 6:
                return 'At Risk'
            else:
                return 'Lost'

        customer_features['value_segment'] = customer_features.apply(customer_value_segment, axis=1)

        self.customer_features = customer_features
        print(f"✅ 顧客特徴量作成完了: {len(customer_features):,}顧客")

        return customer_features

    def create_product_features(self):
        """商品特徴量作成"""
        print("📦 商品特徴量エンジニアリング...")

        # 基本的な売上統計
        product_stats = self.integrated_data.groupby('product_id').agg({
            'total_amount': ['sum', 'mean', 'count'],
            'quantity': 'sum',
            'discount': 'mean',
            'rating': ['mean', 'count'],
            'transaction_date': ['min', 'max']
        }).reset_index()

        # 列名を平坦化
        product_stats.columns = ['product_id', 'total_revenue', 'avg_price_paid', 'sale_count',
                               'total_units_sold', 'avg_discount_given', 'avg_customer_rating',
                               'rating_count', 'first_sale', 'last_sale']

        # 追加特徴量
        product_stats['days_on_market'] = (product_stats['last_sale'] - product_stats['first_sale']).dt.days
        product_stats['sales_velocity'] = product_stats['sale_count'] / (product_stats['days_on_market'] + 1) * 365

        # 商品基本情報とマージ
        product_features = pd.merge(product_stats, self.products, on='product_id', how='left')

        # 商品パフォーマンスセグメント
        def product_performance_segment(row):
            if row['total_revenue'] > product_features['total_revenue'].quantile(0.8):
                return 'Star'
            elif row['total_revenue'] > product_features['total_revenue'].quantile(0.6):
                return 'Rising'
            elif row['total_revenue'] > product_features['total_revenue'].quantile(0.4):
                return 'Steady'
            elif row['total_revenue'] > product_features['total_revenue'].quantile(0.2):
                return 'Declining'
            else:
                return 'Dog'

        product_features['performance_segment'] = product_features.apply(product_performance_segment, axis=1)

        self.product_features = product_features
        print(f"✅ 商品特徴量作成完了: {len(product_features):,}商品")

        return product_features

    def analyze_sales_trends(self):
        """売上トレンド分析"""
        print("📈 売上トレンド分析...")

        # 日次売上
        daily_sales = self.integrated_data.groupby('transaction_date').agg({
            'total_amount': 'sum',
            'transaction_id': 'count'
        }).reset_index()
        daily_sales.columns = ['date', 'revenue', 'transaction_count']

        # 移動平均
        daily_sales['revenue_ma7'] = daily_sales['revenue'].rolling(window=7).mean()
        daily_sales['revenue_ma30'] = daily_sales['revenue'].rolling(window=30).mean()

        # 成長率
        daily_sales['revenue_growth'] = daily_sales['revenue'].pct_change() * 100

        # 月次集計
        monthly_sales = self.integrated_data.groupby(self.integrated_data['transaction_date'].dt.to_period('M')).agg({
            'total_amount': 'sum',
            'customer_id': 'nunique',
            'transaction_id': 'count'
        }).reset_index()
        monthly_sales.columns = ['month', 'revenue', 'unique_customers', 'transactions']
        monthly_sales['avg_order_value'] = monthly_sales['revenue'] / monthly_sales['transactions']
        monthly_sales['revenue_per_customer'] = monthly_sales['revenue'] / monthly_sales['unique_customers']

        return daily_sales, monthly_sales

    def segment_analysis(self):
        """セグメント分析"""
        print("🎯 顧客セグメント分析...")

        if self.customer_features is None:
            self.create_customer_features()

        # 価値セグメント別分析
        segment_analysis = self.customer_features.groupby('value_segment').agg({
            'customer_id': 'count',
            'total_spent': ['mean', 'sum'],
            'avg_order_value': 'mean',
            'order_count': 'mean',
            'purchase_frequency': 'mean',
            'recency': 'mean'
        }).round(2)

        # カテゴリ別セグメント購買行動
        category_segment = self.integrated_data.merge(
            self.customer_features[['customer_id', 'value_segment']],
            on='customer_id'
        ).groupby(['value_segment', 'category'])['total_amount'].sum().unstack(fill_value=0)

        return segment_analysis, category_segment

    def product_recommendation_analysis(self):
        """商品推奨分析"""
        print("🛒 商品推奨分析...")

        # 顧客-商品マトリックス
        customer_product_matrix = self.integrated_data.groupby(['customer_id', 'product_id'])['total_amount'].sum().unstack(fill_value=0)

        # 商品間相関（シンプルな協調フィルタリング）
        product_correlation = customer_product_matrix.corr()

        # 人気商品（購入回数順）
        popular_products = self.integrated_data.groupby('product_id').agg({
            'customer_id': 'nunique',
            'total_amount': 'sum',
            'quantity': 'sum'
        }).sort_values('customer_id', ascending=False)

        return product_correlation, popular_products

# 分析実行
analyzer = EcommerceAnalyzer(customers, products, transactions, reviews)

# データ統合
integrated_data = analyzer.integrate_data()

# 特徴量エンジニアリング
customer_features = analyzer.create_customer_features()
product_features = analyzer.create_product_features()

# 分析実行
daily_sales, monthly_sales = analyzer.analyze_sales_trends()
segment_analysis, category_segment = analyzer.segment_analysis()
product_correlation, popular_products = analyzer.product_recommendation_analysis()

print("\n3. 主要分析結果")
print("=" * 40)

print("📊 売上サマリー:")
print(f"総売上: ¥{integrated_data['total_amount'].sum():,.0f}")
print(f"総取引数: {len(integrated_data):,}")
print(f"ユニーク顧客数: {integrated_data['customer_id'].nunique():,}")
print(f"平均注文金額: ¥{integrated_data['total_amount'].mean():.0f}")

print("\n👥 顧客セグメント分析:")
print(segment_analysis)

print("\n📦 商品パフォーマンス:")
print("カテゴリ別売上:")
category_revenue = integrated_data.groupby('category')['total_amount'].sum().sort_values(ascending=False)
print(category_revenue)

print("\n🎯 人気商品TOP10:")
top_products = product_features.nlargest(10, 'total_revenue')[['product_id', 'category', 'brand', 'total_revenue', 'sale_count']]
print(top_products)

print("\n4. ビジネスインサイトと改善提案")
print("=" * 40)

class BusinessInsightEngine:
    """ビジネスインサイト分析エンジン"""

    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.insights = []
        self.recommendations = []

    def identify_revenue_issues(self):
        """売上課題の特定"""
        print("💡 売上課題の特定:")

        # 月次売上トレンド分析
        monthly_data = self.analyzer.integrated_data.groupby(
            self.analyzer.integrated_data['transaction_date'].dt.to_period('M')
        )['total_amount'].sum()

        # 売上成長率
        growth_rate = monthly_data.pct_change().mean() * 100

        if growth_rate < 0:
            self.insights.append({
                'type': 'revenue_decline',
                'severity': 'high',
                'message': f'月次売上成長率がマイナス ({growth_rate:.1f}%)',
                'data': growth_rate
            })

        # 顧客獲得コスト vs LTV分析
        customer_ltv = self.analyzer.customer_features['total_spent'].mean()
        avg_orders = self.analyzer.customer_features['order_count'].mean()

        if customer_ltv < avg_orders * 50:  # 仮の基準
            self.insights.append({
                'type': 'low_ltv',
                'severity': 'medium',
                'message': f'顧客生涯価値が低い (平均¥{customer_ltv:.0f})',
                'data': customer_ltv
            })

        # セグメント別課題
        champions = self.analyzer.customer_features[
            self.analyzer.customer_features['value_segment'] == 'Champions'
        ]

        if len(champions) / len(self.analyzer.customer_features) < 0.1:
            self.insights.append({
                'type': 'low_champions',
                'severity': 'high',
                'message': f'Champions顧客の割合が低い ({len(champions)/len(self.analyzer.customer_features)*100:.1f}%)',
                'data': len(champions) / len(self.analyzer.customer_features)
            })

        return self.insights

    def analyze_customer_behavior(self):
        """顧客行動分析"""
        print("👥 顧客行動分析:")

        # チャーン分析
        recent_customers = self.analyzer.customer_features[
            self.analyzer.customer_features['recency'] <= 30
        ]
        at_risk_customers = self.analyzer.customer_features[
            self.analyzer.customer_features['recency'] > 90
        ]

        churn_rate = len(at_risk_customers) / len(self.analyzer.customer_features)

        if churn_rate > 0.3:
            self.insights.append({
                'type': 'high_churn_risk',
                'severity': 'high',
                'message': f'チャーンリスク顧客が多い ({churn_rate*100:.1f}%)',
                'data': churn_rate
            })

        # 購入頻度分析
        low_frequency = self.analyzer.customer_features[
            self.analyzer.customer_features['purchase_frequency'] < 2
        ]

        if len(low_frequency) / len(self.analyzer.customer_features) > 0.5:
            self.insights.append({
                'type': 'low_purchase_frequency',
                'severity': 'medium',
                'message': f'購入頻度の低い顧客が多い ({len(low_frequency)/len(self.analyzer.customer_features)*100:.1f}%)',
                'data': len(low_frequency) / len(self.analyzer.customer_features)
            })

        return self.insights

    def generate_recommendations(self):
        """改善提案生成"""
        print("🎯 改善提案:")

        recommendations = []

        for insight in self.insights:
            if insight['type'] == 'revenue_decline':
                recommendations.extend([
                    {
                        'priority': 'P1',
                        'category': '売上改善',
                        'action': 'Champions顧客向けプレミアムプログラム開発',
                        'rationale': '高価値顧客からの売上を最大化',
                        'expected_impact': '売上15-20%向上',
                        'timeline': '3ヶ月'
                    },
                    {
                        'priority': 'P1',
                        'category': '売上改善',
                        'action': 'クロスセル・アップセル施策強化',
                        'rationale': '既存顧客の購入単価向上',
                        'expected_impact': 'AOV 10-15%向上',
                        'timeline': '2ヶ月'
                    }
                ])

            elif insight['type'] == 'high_churn_risk':
                recommendations.append({
                    'priority': 'P1',
                    'category': '顧客維持',
                    'action': 'チャーン予防キャンペーン実施',
                    'rationale': '90日以上非購入顧客の呼び戻し',
                    'expected_impact': 'チャーン率20%削減',
                    'timeline': '1ヶ月'
                })

            elif insight['type'] == 'low_purchase_frequency':
                recommendations.append({
                    'priority': 'P2',
                    'category': 'エンゲージメント',
                    'action': 'パーソナライズドメール配信強化',
                    'rationale': '顧客との接触頻度向上',
                    'expected_impact': '購入頻度30%向上',
                    'timeline': '2ヶ月'
                })

            elif insight['type'] == 'low_champions':
                recommendations.append({
                    'priority': 'P2',
                    'category': '顧客育成',
                    'action': 'ロイヤルティプログラム改善',
                    'rationale': '中価値顧客のChampions転換促進',
                    'expected_impact': 'Champions比率2倍',
                    'timeline': '6ヶ月'
                })

        # 商品関連の推奨事項
        top_categories = self.analyzer.integrated_data.groupby('category')['total_amount'].sum().nlargest(3)

        recommendations.append({
            'priority': 'P2',
            'category': '商品戦略',
            'action': f'主力カテゴリ({", ".join(top_categories.index)})の商品拡充',
            'rationale': '売上の多いカテゴリでのシェア拡大',
            'expected_impact': 'カテゴリ売上10%向上',
            'timeline': '4ヶ月'
        })

        self.recommendations = recommendations
        return recommendations

# インサイト分析実行
insight_engine = BusinessInsightEngine(analyzer)
insights = insight_engine.identify_revenue_issues()
behavior_insights = insight_engine.analyze_customer_behavior()
recommendations = insight_engine.generate_recommendations()

print("\n💡 主要インサイト:")
for i, insight in enumerate(insights, 1):
    severity_icon = "🚨" if insight['severity'] == 'high' else "⚠️"
    print(f"{severity_icon} {i}. {insight['message']}")

print("\n🎯 改善提案:")
for i, rec in enumerate(recommendations, 1):
    priority_icon = "🔥" if rec['priority'] == 'P1' else "⚡"
    print(f"{priority_icon} {rec['priority']} {rec['action']}")
    print(f"   カテゴリ: {rec['category']}")
    print(f"   根拠: {rec['rationale']}")
    print(f"   期待効果: {rec['expected_impact']}")
    print(f"   実施期間: {rec['timeline']}")
    print()

print("\n5. エグゼクティブサマリー")
print("=" * 40)

def create_executive_summary():
    """エグゼクティブサマリー作成"""

    # KPI計算
    total_revenue = integrated_data['total_amount'].sum()
    total_customers = integrated_data['customer_id'].nunique()
    avg_order_value = integrated_data['total_amount'].mean()

    champions_count = len(customer_features[customer_features['value_segment'] == 'Champions'])
    champions_ratio = champions_count / len(customer_features) * 100

    at_risk_count = len(customer_features[customer_features['value_segment'] == 'At Risk'])
    at_risk_ratio = at_risk_count / len(customer_features) * 100

    summary = f"""
=== ECサイト売上最適化 エグゼクティブサマリー ===

【現状分析】
📊 ビジネス概況
• 総売上: ¥{total_revenue:,.0f}
• 総顧客数: {total_customers:,}人
• 平均注文金額: ¥{avg_order_value:.0f}
• Champions顧客比率: {champions_ratio:.1f}%
• リスク顧客比率: {at_risk_ratio:.1f}%

【主要課題】
"""

    # 高優先度の課題を追加
    high_severity_insights = [i for i in insights if i['severity'] == 'high']
    for insight in high_severity_insights:
        summary += f"🚨 {insight['message']}\n"

    summary += f"""
【改善機会】
💰 収益向上ポテンシャル
• Champions顧客拡充により売上20%向上可能
• クロスセル強化でAOV 15%向上可能
• チャーン防止で年間売上10%保護可能

【推奨アクション】
"""

    # P1優先度の推奨事項
    p1_recommendations = [r for r in recommendations if r['priority'] == 'P1']
    for rec in p1_recommendations:
        summary += f"🔥 {rec['action']} ({rec['timeline']})\n"

    summary += f"""
【期待成果】
📈 実施による期待効果
• 短期（3ヶ月）: 売上15%向上
• 中期（6ヶ月）: 顧客生涯価値25%向上
• 長期（12ヶ月）: 持続的成長基盤確立

【次のステップ】
1. P1施策の即座実行
2. 週次KPIモニタリング体制構築
3. 月次効果測定とPDCA実施
"""

    return summary

executive_summary = create_executive_summary()
print(executive_summary)

print("\n6. 最終成果物とネクストステップ")
print("=" * 40)

print("📋 プロジェクト成果物:")
print("""
✅ 完成した成果物:
1. 包括的データ分析レポート
2. 顧客セグメンテーション結果
3. 商品パフォーマンス分析
4. ビジネスインサイト特定
5. 具体的改善提案
6. エグゼクティブサマリー

📊 分析で使用した手法:
• データクリーニングと前処理
• 特徴量エンジニアリング (apply/lambda活用)
• データ結合 (merge/concat)
• 高度な集計とgroupby操作
• 時系列分析
• 統計的分析
• 可視化とダッシュボード作成
• RFM分析
• コホート分析
• 協調フィルタリング基礎

🛠️ 実装したスキル:
• pandas操作の完全習得
• ビジネス課題解決アプローチ
• データストーリーテリング
• エグゼクティブ向けレポート作成
""")

print("\n🚀 ネクストステップ:")
print("""
【即座に実行可能】
1. 特定した改善施策の実装
2. KPIダッシュボードの日次運用
3. A/Bテストによる施策効果検証

【スキル発展】
1. 機械学習モデルによる高度な予測分析
2. リアルタイムデータパイプライン構築
3. より高度な推奨システム開発
4.因果推論による施策効果測定

【ビジネスインパクト】
1. データドリブンな意思決定文化の構築
2. 継続的な改善プロセスの確立
3. 競合優位性の確保
""")

print("\n🎓 おめでとうございます！")
print("=" * 50)
print("""
pandas DataFrame 実務完全マスター講座 Advanced版を完走しました！

あなたは以下を習得しました:

🏆 Technical Skills:
✅ pandas操作の完全習得
✅ 大規模データの効率的処理
✅ 複雑なデータ結合・変換
✅ 高度な特徴量エンジニアリング
✅ 統計分析と可視化
✅ 実務レベルのデータパイプライン構築

🎯 Business Skills:
✅ ビジネス課題の構造化
✅ データからのインサイト抽出
✅ エグゼクティブ向けレポート作成
✅ アクショナブルな改善提案
✅ データストーリーテリング

🚀 Next Level:
あなたは今や実務で即戦力となるデータアナリストです。
継続的な学習と実践で、さらなる高みを目指しましょう！

Keep analyzing, keep growing! 📊✨
""")

print("\n✅ Week 8 完了：実務プロジェクトを完遂しました！")
print("✅ 全8週間の学習プログラム完了！")

---

## 📚 総合まとめと今後の学習パス

### **習得したスキルの総棋譜**

```python
print("\n📊 習得スキル総まとめ")
print("=" * 50)

skills_mastered = {
    'Week 1: pandas基礎': [
        'DataFrameの内部構造理解',
        'メモリ効率的なデータ作成',
        'データ型最適化',
        'エラーハンドリング',
        'パフォーマンス最適化'
    ],

    'Week 2: インデックス操作': [
        'インデックスの完全理解',
        '階層インデックス（MultiIndex）',
        '高速データ選択テクニック',
        '動的フィルタリング',
        'パフォーマンス比較と最適化'
    ],

    'Week 3: データクリーニング': [
        '欠損値の種類と対処法',
        '機械学習による欠損値補完',
        '異常値検出手法',
        '文字列クリーニング',
        '自動クリーニングパイプライン'
    ],

    'Week 4: 特徴量エンジニアリング': [
        'apply()とlambda式の完全活用',
        '時系列特徴量作成',
        '統計的特徴量生成',
        '相互作用特徴量',
        'カスタム変換器の実装'
    ],

    'Week 5: データ結合': [
        'merge()とconcat()の完全攻略',
        '複雑な結合パターン',
        '結合エラーハンドリング',
        '大規模データの効率的結合',
        '品質チェック付き結合'
    ],

    'Week 6: 集計・時系列分析': [
        '高度なgroupby操作',
        'カスタム集計関数',
        '時系列特徴量エンジニアリング',
        '季節性分解',
        'ビジネス指標計算'
    ],

    'Week 7: 可視化・統計分析': [
        '高度な可視化テクニック',
        '統計的仮説検定',
        '回帰分析',
        'A/Bテスト分析',
        'コホート分析'
    ],

    'Week 8: 実務プロジェクト': [
        '大規模データセット生成',
        '包括的データ分析',
        'ビジネスインサイト抽出',
        'エグゼクティブレポート作成',
        '改善提案の具体化'
    ]
}

for week, skills in skills_mastered.items():
    print(f"\n🎯 {week}")
    for skill in skills:
        print(f"  ✅ {skill}")
````

### **推奨学習パス**

```python
print("\n🗺️ 今後の学習パス")
print("=" * 50)

learning_paths = {
    '機械学習スペシャリスト': [
        'scikit-learn完全マスター',
        'XGBoost, LightGBM活用',
        'ディープラーニング (TensorFlow/PyTorch)',
        'AutoML (H2O.ai, AutoGluon)',
        'MLOps (MLflow, Kubeflow)'
    ],

    'データエンジニア': [
        'Apache Spark / PySpark',
        'データパイプライン構築 (Airflow)',
        'クラウドサービス (AWS, GCP, Azure)',
        'ストリーミング処理 (Kafka, Flink)',
        'データウェアハウス設計'
    ],

    'ビジネスアナリスト': [
        'Tableau / Power BI 上級',
        '統計学・実験設計',
        'ビジネス戦略分析',
        'プロダクト分析',
        'マーケティング分析'
    ],

    'データサイエンティスト': [
        '高度な統計手法',
        '因果推論 (causal inference)',
        '時系列予測 (Prophet, ARIMA)',
        '自然言語処理 (NLP)',
        '推奨システム構築'
    ]
}

for path, skills in learning_paths.items():
    print(f"\n🎯 {path}")
    for skill in skills:
        print(f"  📚 {skill}")
```

### **継続的成長のための提案**

```python
print("\n💪 継続的成長のために")
print("=" * 50)

print("""
🔄 定期的な実践:
• 週1回：新しいデータセットでの分析実践
• 月1回：過去のコードのリファクタリング
• 四半期1回：新しい手法・ライブラリの学習

🤝 コミュニティ参加:
• Kaggle競技への参加
• データサイエンスコミュニティ活動
• オープンソースプロジェクト貢献
• 勉強会・カンファレンス参加

📖 継続学習:
• 最新のpandas機能追跡
• 新しい分析手法の習得
• ビジネス領域知識の拡充
• 技術ブログ・論文の定期的な読書

🎯 プロジェクト実践:
• 個人プロジェクトの継続
• 実務課題への積極的適用
• ポートフォリオの充実
• 成果の定量的測定
""")

print("\n🌟 最後に")
print("=" * 50)
print("""
この8週間で、あなたはpandasの真のマスターになりました。
しかし、これは新たなスタートラインに立ったに過ぎません。

データの世界は日々進化しています。
学び続け、実践し続け、価値を創造し続けてください。

あなたのデータ分析スキルが、
ビジネスの成功と社会の発展に貢献することを期待しています。

Happy Data Analysis! 🐼📊✨
""")
```

---

**🎉 pandas DataFrame 実務完全マスター講座 Advanced 版 完了！**

これで 8 週間にわたる包括的な学習プログラムが完成しました。実務で即座に活用できる高度な pandas スキルを習得し、データサイエンティストとしての基盤を築き上げました！
