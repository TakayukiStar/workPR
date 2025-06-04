# Mermaid記法 完全マスター教材 🚀
## 初級エンジニアから中上級レベルまで最速キャッチアップ - GitHub完全対応版

---

## 📚 目次
1. [基礎編：Mermaidの世界へようこそ](#基礎編)
2. [初級編：基本図表をマスター](#初級編)
3. [中級編：複雑な図表に挑戦](#中級編)
4. [上級編：プロレベルの技術](#上級編)
5. [実践編：現場で使える応用技術](#実践編)
6. [チートシート：いつでも使える早見表](#チートシート)
7. [トラブルシューティング：GitHub対応版](#トラブルシューティング)

---

## 🌟 基礎編：Mermaidの世界へようこそ

### Mermaidとは？
Mermaidは**テキストベースで図表を作成**できる革命的なツールです。コードを書くように図を描けるため、バージョン管理が可能で、ドキュメントと一緒に管理できます。

### 基本的な書き方
```
graph TD
    A[開始] --> B[処理]
    B --> C[終了]
```

```mermaid
graph TD
    A[開始] --> B[処理]
    B --> C[終了]
```

### 🎯 学習の進め方
各コードブロックを**そのままコピー&ペースト**して、Mermaid対応ツール（GitHub、GitLab、Notion、Mermaid Live Editor等）で試してください。

---

## 🚀 初級編：基本図表をマスター

### 1. フローチャート（基本中の基本）

#### ■ シンプルなフロー
```
flowchart TD
    Start([開始]) --> Input[データ入力]
    Input --> Process{処理が必要？}
    Process -->|Yes| Action[データ処理実行]
    Process -->|No| Skip[処理をスキップ]
    Action --> Output[結果出力]
    Skip --> Output
    Output --> End([終了])
```

```mermaid
flowchart TD
    Start([開始]) --> Input[データ入力]
    Input --> Process{処理が必要？}
    Process -->|Yes| Action[データ処理実行]
    Process -->|No| Skip[処理をスキップ]
    Action --> Output[結果出力]
    Skip --> Output
    Output --> End([終了])
```

#### ■ ノードの形状バリエーション
```
flowchart LR
    A[四角形] --> B(丸角四角形)
    B --> C([楕円形])
    C --> D{ダイヤモンド}
    D --> E["テキスト<br/>改行可能"]
    E --> F[("円形")]
    F --> G[["サブルーチン"]]
    G --> H[(データベース)]
```

```mermaid
flowchart LR
    A[四角形] --> B(丸角四角形)
    B --> C([楕円形])
    C --> D{ダイヤモンド}
    D --> E["テキスト<br/>改行可能"]
    E --> F[("円形")]
    F --> G[["サブルーチン"]]
    G --> H[(データベース)]
```

#### ■ 方向指定とサブグラフ
```
flowchart TB
    subgraph "フロー方向の例"
        direction TB
        A1[TB: 上から下] --> A2[デフォルト]
    end
    
    subgraph "左右方向"
        direction LR
        B1[LR: 左から右] --> B2[横並び]
    end
    
    A2 --> B1
```

```mermaid
flowchart TB
    subgraph "フロー方向の例"
        direction TB
        A1[TB: 上から下] --> A2[デフォルト]
    end
    
    subgraph "左右方向"
        direction LR
        B1[LR: 左から右] --> B2[横並び]
    end
    
    A2 --> B1
```

### 2. シーケンス図（システム間のやりとり）

#### ■ 基本的なシーケンス
```
sequenceDiagram
    participant U as ユーザー
    participant F as フロントエンド
    participant B as バックエンド
    participant D as データベース
    
    U->>F: ログイン要求
    F->>B: 認証API呼び出し
    B->>D: ユーザー情報取得
    D-->>B: ユーザーデータ返却
    B-->>F: 認証結果
    F-->>U: ログイン完了画面
```

```mermaid
sequenceDiagram
    participant U as ユーザー
    participant F as フロントエンド
    participant B as バックエンド
    participant D as データベース
    
    U->>F: ログイン要求
    F->>B: 認証API呼び出し
    B->>D: ユーザー情報取得
    D-->>B: ユーザーデータ返却
    B-->>F: 認証結果
    F-->>U: ログイン完了画面
```

#### ■ 条件分岐とループ
```
sequenceDiagram
    participant A as Client
    participant B as Server
    
    A->>B: データ送信
    
    alt 成功の場合
        B-->>A: 200 OK
    else エラーの場合
        B-->>A: 400 Bad Request
    end
    
    loop 3回まで再試行
        A->>B: リトライ
        B-->>A: レスポンス
    end
    
    Note over A,B: 処理完了
```

```mermaid
sequenceDiagram
    participant A as Client
    participant B as Server
    
    A->>B: データ送信
    
    alt 成功の場合
        B-->>A: 200 OK
    else エラーの場合
        B-->>A: 400 Bad Request
    end
    
    loop 3回まで再試行
        A->>B: リトライ
        B-->>A: レスポンス
    end
    
    Note over A,B: 処理完了
```

### 3. ガントチャート（プロジェクト管理）

```
gantt
    title プロジェクト進行表
    dateFormat  YYYY-MM-DD
    section 設計フェーズ
    要件定義          :a1, 2024-01-01, 30d
    基本設計          :a2, after a1, 20d
    詳細設計          :a3, after a2, 15d
    
    section 開発フェーズ
    フロントエンド開発    :b1, after a3, 40d
    バックエンド開発     :b2, after a3, 35d
    
    section テストフェーズ
    単体テスト        :c1, after b1, 10d
    結合テスト        :c2, after c1, 15d
```

```mermaid
gantt
    title プロジェクト進行表
    dateFormat  YYYY-MM-DD
    section 設計フェーズ
    要件定義          :a1, 2024-01-01, 30d
    基本設計          :a2, after a1, 20d
    詳細設計          :a3, after a2, 15d
    
    section 開発フェーズ
    フロントエンド開発    :b1, after a3, 40d
    バックエンド開発     :b2, after a3, 35d
    
    section テストフェーズ
    単体テスト        :c1, after b1, 10d
    結合テスト        :c2, after c1, 15d
```

---

## 🎓 中級編：複雑な図表に挑戦

### 1. ER図（データベース設計の必須技術）

#### ■ 基本的なER図
```
erDiagram
    USER {
        int user_id PK "ユーザーID"
        string username UK "ユーザー名"
        string email UK "メールアドレス"
        string password "パスワード"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
    }
    
    POST {
        int post_id PK "投稿ID"
        int user_id FK "ユーザーID"
        string title "タイトル"
        text content "本文"
        datetime published_at "公開日時"
        datetime created_at "作成日時"
    }
    
    COMMENT {
        int comment_id PK "コメントID"
        int post_id FK "投稿ID"
        int user_id FK "ユーザーID"
        text content "コメント内容"
        datetime created_at "作成日時"
    }
    
    USER ||--o{ POST : "投稿する"
    POST ||--o{ COMMENT : "コメントされる"
    USER ||--o{ COMMENT : "コメントする"
```

```mermaid
erDiagram
    USER {
        int user_id PK "ユーザーID"
        string username UK "ユーザー名"
        string email UK "メールアドレス"
        string password "パスワード"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
    }
    
    POST {
        int post_id PK "投稿ID"
        int user_id FK "ユーザーID"
        string title "タイトル"
        text content "本文"
        datetime published_at "公開日時"
        datetime created_at "作成日時"
    }
    
    COMMENT {
        int comment_id PK "コメントID"
        int post_id FK "投稿ID"
        int user_id FK "ユーザーID"
        text content "コメント内容"
        datetime created_at "作成日時"
    }
    
    USER ||--o{ POST : "投稿する"
    POST ||--o{ COMMENT : "コメントされる"
    USER ||--o{ COMMENT : "コメントする"
```

#### ■ ECサイトの複雑なER図
```
erDiagram
    USER {
        int user_id PK
        string username
        string email
        string phone
        datetime created_at
    }
    
    PRODUCT {
        int product_id PK
        string name
        text description
        decimal price
        int stock_quantity
        string category
    }
    
    ORDER {
        int order_id PK
        int user_id FK
        datetime order_date
        decimal total_amount
        string status
    }
    
    ORDER_ITEM {
        int order_item_id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal price
    }
    
    CART {
        int cart_id PK
        int user_id FK
        int product_id FK
        int quantity
        datetime added_at
    }
    
    USER ||--o{ ORDER : places
    USER ||--o{ CART : has
    ORDER ||--o{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : included_in
    PRODUCT ||--o{ CART : added_to
```

```mermaid
erDiagram
    USER {
        int user_id PK
        string username
        string email
        string phone
        datetime created_at
    }
    
    PRODUCT {
        int product_id PK
        string name
        text description
        decimal price
        int stock_quantity
        string category
    }
    
    ORDER {
        int order_id PK
        int user_id FK
        datetime order_date
        decimal total_amount
        string status
    }
    
    ORDER_ITEM {
        int order_item_id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal price
    }
    
    CART {
        int cart_id PK
        int user_id FK
        int product_id FK
        int quantity
        datetime added_at
    }
    
    USER ||--o{ ORDER : places
    USER ||--o{ CART : has
    ORDER ||--o{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : included_in
    PRODUCT ||--o{ CART : added_to
```

### 2. クラス図（オブジェクト指向設計）- GitHub対応版

```
classDiagram
    class User {
        -int userId
        -string username
        -string email
        -string passwordHash
        +login(password) boolean
        +updateProfile(data) void
        +getProfile() UserProfile
    }
    
    class Post {
        -int postId
        -int authorId
        -string title
        -string content
        -datetime createdAt
        +publish() void
        +edit(content) void
        +delete() void
    }
    
    class Comment {
        -int commentId
        -int postId
        -int authorId
        -string content
        +edit(content) void
        +delete() void
    }
    
    class UserRepository {
        <<interface>>
        +findById(id) User
        +save(user) void
        +delete(id) void
    }
    
    User --> Post : creates
    Post --> Comment : has
    User --> Comment : writes
    User --> UserRepository : uses
```

```mermaid
classDiagram
    class User {
        -int userId
        -string username
        -string email
        -string passwordHash
        +login(password) boolean
        +updateProfile(data) void
        +getProfile() UserProfile
    }
    
    class Post {
        -int postId
        -int authorId
        -string title
        -string content
        -datetime createdAt
        +publish() void
        +edit(content) void
        +delete() void
    }
    
    class Comment {
        -int commentId
        -int postId
        -int authorId
        -string content
        +edit(content) void
        +delete() void
    }
    
    class UserRepository {
        <<interface>>
        +findById(id) User
        +save(user) void
        +delete(id) void
    }
    
    User --> Post : creates
    Post --> Comment : has
    User --> Comment : writes
    User --> UserRepository : uses
```

### 3. 状態図（状態遷移の可視化）

```
stateDiagram-v2
    [*] --> 未ログイン
    
    未ログイン --> ログイン中 : ログイン試行
    ログイン中 --> ログイン済み : 認証成功
    ログイン中 --> 未ログイン : 認証失敗
    
    ログイン済み --> 編集中 : 投稿作成開始
    編集中 --> ログイン済み : 保存/キャンセル
    
    ログイン済み --> コメント中 : コメント入力
    コメント中 --> ログイン済み : コメント投稿
    
    ログイン済み --> 未ログイン : ログアウト
    
    note right of ログイン中
        認証処理中は
        他の操作を制限
    end note
```

```mermaid
stateDiagram-v2
    [*] --> 未ログイン
    
    未ログイン --> ログイン中 : ログイン試行
    ログイン中 --> ログイン済み : 認証成功
    ログイン中 --> 未ログイン : 認証失敗
    
    ログイン済み --> 編集中 : 投稿作成開始
    編集中 --> ログイン済み : 保存/キャンセル
    
    ログイン済み --> コメント中 : コメント入力
    コメント中 --> ログイン済み : コメント投稿
    
    ログイン済み --> 未ログイン : ログアウト
    
    note right of ログイン中
        認証処理中は
        他の操作を制限
    end note
```

### 4. マインドマップ（アイディア整理）

```
mindmap
  root((プロダクト開発))
    計画
      要件定義
      設計
      スケジュール
    開発
      フロントエンド
        React
        TypeScript
        Tailwind
      バックエンド
        Node.js
        Express
        PostgreSQL
    テスト
      単体テスト
      統合テスト
      E2Eテスト
    運用
      デプロイ
      監視
      保守
```

```mermaid
mindmap
  root((プロダクト開発))
    計画
      要件定義
      設計
      スケジュール
    開発
      フロントエンド
        React
        TypeScript
        Tailwind
      バックエンド
        Node.js
        Express
        PostgreSQL
    テスト
      単体テスト
      統合テスト
      E2Eテスト
    運用
      デプロイ
      監視
      保守
```

---

## 🏆 上級編：プロレベルの技術

### 1. 複雑なフローチャート（サブグラフとスタイリング）

```
flowchart TD
    subgraph "認証システム"
        A[ログイン要求] --> B{認証情報確認}
        B -->|有効| C[JWTトークン生成]
        B -->|無効| D[エラーレスポンス]
    end
    
    subgraph "API Gateway"
        E[API要求] --> F{トークン検証}
        F -->|有効| G[リクエスト転送]
        F -->|無効| H[401エラー]
    end
    
    subgraph "マイクロサービス"
        I[ユーザーサービス]
        J[注文サービス]
        K[商品サービス]
    end
    
    C --> E
    G --> I
    G --> J
    G --> K
    
    classDef authBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef apiBox fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef serviceBox fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    
    class A,B,C,D authBox
    class E,F,G,H apiBox
    class I,J,K serviceBox
```

```mermaid
flowchart TD
    subgraph "認証システム"
        A[ログイン要求] --> B{認証情報確認}
        B -->|有効| C[JWTトークン生成]
        B -->|無効| D[エラーレスポンス]
    end
    
    subgraph "API Gateway"
        E[API要求] --> F{トークン検証}
        F -->|有効| G[リクエスト転送]
        F -->|無効| H[401エラー]
    end
    
    subgraph "マイクロサービス"
        I[ユーザーサービス]
        J[注文サービス]
        K[商品サービス]
    end
    
    C --> E
    G --> I
    G --> J
    G --> K
    
    classDef authBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef apiBox fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef serviceBox fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    
    class A,B,C,D authBox
    class E,F,G,H apiBox
    class I,J,K serviceBox
```

### 2. アーキテクチャ図（システム全体像）

```
flowchart TB
    subgraph "フロントエンド層"
        ReactApp[React Application]
        MobileApp[Mobile App]
    end
    
    subgraph "API Gateway層"
        Gateway[API Gateway<br/>- 認証<br/>- レート制限<br/>- ロードバランシング]
    end
    
    subgraph "マイクロサービス層"
        UserService[User Service<br/>- ユーザー管理<br/>- 認証]
        OrderService[Order Service<br/>- 注文処理<br/>- 決済]
        ProductService[Product Service<br/>- 商品管理<br/>- 在庫]
        NotificationService[Notification Service<br/>- メール送信<br/>- プッシュ通知]
    end
    
    subgraph "データ層"
        UserDB[(User Database<br/>PostgreSQL)]
        OrderDB[(Order Database<br/>PostgreSQL)]
        ProductDB[(Product Database<br/>MongoDB)]
        Cache[(Redis Cache)]
    end
    
    subgraph "外部サービス"
        PaymentAPI[Payment API]
        EmailService[Email Service]
    end
    
    ReactApp --> Gateway
    MobileApp --> Gateway
    
    Gateway --> UserService
    Gateway --> OrderService
    Gateway --> ProductService
    Gateway --> NotificationService
    
    UserService --> UserDB
    OrderService --> OrderDB
    ProductService --> ProductDB
    
    UserService --> Cache
    OrderService --> Cache
    ProductService --> Cache
    
    OrderService --> PaymentAPI
    NotificationService --> EmailService
    
    classDef frontend fill:#e3f2fd,stroke:#1976d2
    classDef gateway fill:#fff3e0,stroke:#f57c00
    classDef service fill:#e8f5e8,stroke:#388e3c
    classDef database fill:#fce4ec,stroke:#c2185b
    classDef external fill:#f3e5f5,stroke:#7b1fa2
    
    class ReactApp,MobileApp frontend
    class Gateway gateway
    class UserService,OrderService,ProductService,NotificationService service
    class UserDB,OrderDB,ProductDB,Cache database
    class PaymentAPI,EmailService external
```

```mermaid
flowchart TB
    subgraph "フロントエンド層"
        ReactApp[React Application]
        MobileApp[Mobile App]
    end
    
    subgraph "API Gateway層"
        Gateway[API Gateway<br/>- 認証<br/>- レート制限<br/>- ロードバランシング]
    end
    
    subgraph "マイクロサービス層"
        UserService[User Service<br/>- ユーザー管理<br/>- 認証]
        OrderService[Order Service<br/>- 注文処理<br/>- 決済]
        ProductService[Product Service<br/>- 商品管理<br/>- 在庫]
        NotificationService[Notification Service<br/>- メール送信<br/>- プッシュ通知]
    end
    
    subgraph "データ層"
        UserDB[(User Database<br/>PostgreSQL)]
        OrderDB[(Order Database<br/>PostgreSQL)]
        ProductDB[(Product Database<br/>MongoDB)]
        Cache[(Redis Cache)]
    end
    
    subgraph "外部サービス"
        PaymentAPI[Payment API]
        EmailService[Email Service]
    end
    
    ReactApp --> Gateway
    MobileApp --> Gateway
    
    Gateway --> UserService
    Gateway --> OrderService
    Gateway --> ProductService
    Gateway --> NotificationService
    
    UserService --> UserDB
    OrderService --> OrderDB
    ProductService --> ProductDB
    
    UserService --> Cache
    OrderService --> Cache
    ProductService --> Cache
    
    OrderService --> PaymentAPI
    NotificationService --> EmailService
    
    classDef frontend fill:#e3f2fd,stroke:#1976d2
    classDef gateway fill:#fff3e0,stroke:#f57c00
    classDef service fill:#e8f5e8,stroke:#388e3c
    classDef database fill:#fce4ec,stroke:#c2185b
    classDef external fill:#f3e5f5,stroke:#7b1fa2
    
    class ReactApp,MobileApp frontend
    class Gateway gateway
    class UserService,OrderService,ProductService,NotificationService service
    class UserDB,OrderDB,ProductDB,Cache database
    class PaymentAPI,EmailService external
```

### 3. 詳細なシーケンス図（エラーハンドリング込み）

```
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant G as API Gateway
    participant A as Auth Service
    participant O as Order Service
    participant P as Payment Service
    participant D as Database
    
    U->>F: 商品購入ボタンクリック
    F->>G: 注文作成API呼び出し
    
    rect rgb(240, 248, 255)
        Note over G,A: 認証フェーズ
        G->>A: トークン検証
        A-->>G: 認証OK
    end
    
    rect rgb(248, 255, 240)
        Note over G,O: 注文処理フェーズ
        G->>O: 注文作成要求
        O->>D: 在庫確認
        D-->>O: 在庫あり
        O->>D: 注文データ保存
        D-->>O: 保存完了
    end
    
    rect rgb(255, 248, 240)
        Note over O,P: 決済フェーズ
        O->>P: 決済処理要求
        P->>P: 決済処理
        
        alt 決済成功
            P-->>O: 決済完了
            O->>D: 注文ステータス更新
            D-->>O: 更新完了
            O-->>G: 注文作成成功
            G-->>F: 200 OK
            F-->>U: 購入完了画面
        else 決済失敗
            P-->>O: 決済失敗
            O->>D: 注文キャンセル
            D-->>O: キャンセル完了
            O-->>G: 注文失敗
            G-->>F: 400 Bad Request
            F-->>U: エラーメッセージ
        end
    end
```

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant G as API Gateway
    participant A as Auth Service
    participant O as Order Service
    participant P as Payment Service
    participant D as Database
    
    U->>F: 商品購入ボタンクリック
    F->>G: 注文作成API呼び出し
    
    rect rgb(240, 248, 255)
        Note over G,A: 認証フェーズ
        G->>A: トークン検証
        A-->>G: 認証OK
    end
    
    rect rgb(248, 255, 240)
        Note over G,O: 注文処理フェーズ
        G->>O: 注文作成要求
        O->>D: 在庫確認
        D-->>O: 在庫あり
        O->>D: 注文データ保存
        D-->>O: 保存完了
    end
    
    rect rgb(255, 248, 240)
        Note over O,P: 決済フェーズ
        O->>P: 決済処理要求
        P->>P: 決済処理
        
        alt 決済成功
            P-->>O: 決済完了
            O->>D: 注文ステータス更新
            D-->>O: 更新完了
            O-->>G: 注文作成成功
            G-->>F: 200 OK
            F-->>U: 購入完了画面
        else 決済失敗
            P-->>O: 決済失敗
            O->>D: 注文キャンセル
            D-->>O: キャンセル完了
            O-->>G: 注文失敗
            G-->>F: 400 Bad Request
            F-->>U: エラーメッセージ
        end
    end
```

---

## 💼 実践編：現場で使える応用技術

### 1. リリースプロセスの可視化 - GitHub対応版

```
flowchart TD
    subgraph "開発ブランチ"
        develop[develop branch]
        feature1[feature/login]
        feature2[feature/payment]
        feature3[feature/ui-update]
    end
    
    subgraph "リリースプロセス"
        release[release/v1.0]
        hotfix[hotfix/urgent-fix]
    end
    
    subgraph "本番ブランチ"
        main[main branch]
        tag1[v1.0.0]
        tag2[v1.0.1]
    end
    
    feature1 --> develop
    feature2 --> develop
    feature3 --> develop
    
    develop --> release
    release --> main
    main --> tag1
    
    main --> hotfix
    hotfix --> main
    main --> tag2
    
    classDef devBranch fill:#e3f2fd,stroke:#1976d2
    classDef releaseBranch fill:#fff3e0,stroke:#f57c00
    classDef mainBranch fill:#e8f5e8,stroke:#388e3c
    classDef tagStyle fill:#fce4ec,stroke:#c2185b
    
    class develop,feature1,feature2,feature3 devBranch
    class release,hotfix releaseBranch
    class main mainBranch
    class tag1,tag2 tagStyle
```

```mermaid
flowchart TD
    subgraph "開発ブランチ"
        develop[develop branch]
        feature1[feature/login]
        feature2[feature/payment]
        feature3[feature/ui-update]
    end
    
    subgraph "リリースプロセス"
        release[release/v1.0]
        hotfix[hotfix/urgent-fix]
    end
    
    subgraph "本番ブランチ"
        main[main branch]
        tag1[v1.0.0]
        tag2[v1.0.1]
    end
    
    feature1 --> develop
    feature2 --> develop
    feature3 --> develop
    
    develop --> release
    release --> main
    main --> tag1
    
    main --> hotfix
    hotfix --> main
    main --> tag2
    
    classDef devBranch fill:#e3f2fd,stroke:#1976d2
    classDef releaseBranch fill:#fff3e0,stroke:#f57c00
    classDef mainBranch fill:#e8f5e8,stroke:#388e3c
    classDef tagStyle fill:#fce4ec,stroke:#c2185b
    
    class develop,feature1,feature2,feature3 devBranch
    class release,hotfix releaseBranch
    class main mainBranch
    class tag1,tag2 tagStyle
```

### 2. DevOpsパイプライン

```
flowchart LR
    subgraph "開発"
        Code[コード作成] --> Commit[Git Commit]
        Commit --> Push[Git Push]
    end
    
    subgraph "CI/CD Pipeline"
        Push --> Build[ビルド]
        Build --> Test[自動テスト]
        Test --> Security[セキュリティスキャン]
        Security --> Deploy[デプロイ]
    end
    
    subgraph "環境"
        Deploy --> Dev[開発環境]
        Dev --> Staging[ステージング環境]
        Staging --> Prod[本番環境]
    end
    
    subgraph "監視"
        Prod --> Monitor[監視]
        Monitor --> Alert[アラート]
        Alert --> Action[対応]
    end
    
    Test -->|失敗| Notification[開発者通知]
    Security -->|脆弱性発見| Block[デプロイ停止]
    Monitor -->|異常検知| Rollback[ロールバック]
    
    classDef dev fill:#e3f2fd,stroke:#1976d2
    classDef pipeline fill:#e8f5e8,stroke:#388e3c
    classDef env fill:#fff3e0,stroke:#f57c00
    classDef monitor fill:#fce4ec,stroke:#c2185b
    
    class Code,Commit,Push dev
    class Build,Test,Security,Deploy pipeline
    class Dev,Staging,Prod env
    class Monitor,Alert,Action monitor
```

```mermaid
flowchart LR
    subgraph "開発"
        Code[コード作成] --> Commit[Git Commit]
        Commit --> Push[Git Push]
    end
    
    subgraph "CI/CD Pipeline"
        Push --> Build[ビルド]
        Build --> Test[自動テスト]
        Test --> Security[セキュリティスキャン]
        Security --> Deploy[デプロイ]
    end
    
    subgraph "環境"
        Deploy --> Dev[開発環境]
        Dev --> Staging[ステージング環境]
        Staging --> Prod[本番環境]
    end
    
    subgraph "監視"
        Prod --> Monitor[監視]
        Monitor --> Alert[アラート]
        Alert --> Action[対応]
    end
    
    Test -->|失敗| Notification[開発者通知]
    Security -->|脆弱性発見| Block[デプロイ停止]
    Monitor -->|異常検知| Rollback[ロールバック]
    
    classDef dev fill:#e3f2fd,stroke:#1976d2
    classDef pipeline fill:#e8f5e8,stroke:#388e3c
    classDef env fill:#fff3e0,stroke:#f57c00
    classDef monitor fill:#fce4ec,stroke:#c2185b
    
    class Code,Commit,Push dev
    class Build,Test,Security,Deploy pipeline
    class Dev,Staging,Prod env
    class Monitor,Alert,Action monitor
```

### 3. ユーザージャーニーマップ

```
journey
    title ユーザーのオンラインショッピング体験
    section 発見
      Google検索: 3: User
      サイト訪問: 4: User
      商品閲覧: 5: User
    section 検討
      レビュー確認: 4: User
      価格比較: 3: User
      お気に入り追加: 4: User
    section 購入
      カート追加: 5: User
      会員登録: 2: User
      決済処理: 3: User
      注文確認: 4: User
    section フォロー
      配送追跡: 4: User
      商品受け取り: 5: User
      レビュー投稿: 3: User
```

```mermaid
journey
    title ユーザーのオンラインショッピング体験
    section 発見
      Google検索: 3: User
      サイト訪問: 4: User
      商品閲覧: 5: User
    section 検討
      レビュー確認: 4: User
      価格比較: 3: User
      お気に入り追加: 4: User
    section 購入
      カート追加: 5: User
      会員登録: 2: User
      決済処理: 3: User
      注文確認: 4: User
    section フォロー
      配送追跡: 4: User
      商品受け取り: 5: User
      レビュー投稿: 3: User
```

### 4. システム障害対応フロー

```
flowchart TD
    Alert[アラート発生] --> Triage{重要度判定}
    
    Triage -->|P1 Critical| Emergency[緊急対応チーム招集]
    Triage -->|P2 High| Urgent[当番エンジニア対応]
    Triage -->|P3 Medium| Normal[通常対応]
    Triage -->|P4 Low| Schedule[スケジュール対応]
    
    Emergency --> Investigate[原因調査]
    Urgent --> Investigate
    Normal --> Investigate
    
    Investigate --> Identify{原因特定？}
    Identify -->|Yes| Fix[修正実施]
    Identify -->|No| Escalate[エスカレーション]
    
    Fix --> Test[動作確認]
    Test --> Monitor[監視強化]
    
    Escalate --> Expert[専門家投入]
    Expert --> Fix
    
    Monitor --> PostMortem[ポストモーテム]
    PostMortem --> Improve[改善策実装]
    
    classDef critical fill:#ffebee,stroke:#d32f2f,stroke-width:3px
    classDef high fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef normal fill:#e8f5e8,stroke:#388e3c
    classDef process fill:#e3f2fd,stroke:#1976d2
    
    class Alert,Emergency critical
    class Urgent,Investigate high
    class Normal,Schedule normal
    class Fix,Test,Monitor,PostMortem,Improve process
```

```mermaid
flowchart TD
    Alert[アラート発生] --> Triage{重要度判定}
    
    Triage -->|P1 Critical| Emergency[緊急対応チーム招集]
    Triage -->|P2 High| Urgent[当番エンジニア対応]
    Triage -->|P3 Medium| Normal[通常対応]
    Triage -->|P4 Low| Schedule[スケジュール対応]
    
    Emergency --> Investigate[原因調査]
    Urgent --> Investigate
    Normal --> Investigate
    
    Investigate --> Identify{原因特定？}
    Identify -->|Yes| Fix[修正実施]
    Identify -->|No| Escalate[エスカレーション]
    
    Fix --> Test[動作確認]
    Test --> Monitor[監視強化]
    
    Escalate --> Expert[専門家投入]
    Expert --> Fix
    
    Monitor --> PostMortem[ポストモーテム]
    PostMortem --> Improve[改善策実装]
    
    classDef critical fill:#ffebee,stroke:#d32f2f,stroke-width:3px
    classDef high fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef normal fill:#e8f5e8,stroke:#388e3c
    classDef process fill:#e3f2fd,stroke:#1976d2
    
    class Alert,Emergency critical
    class Urgent,Investigate high
    class Normal,Schedule normal
    class Fix,Test,Monitor,PostMortem,Improve process
```

### 5. アジャイル開発プロセス

```
flowchart LR
    subgraph "スプリント1"
        Planning1[スプリント計画] --> Daily1[デイリースクラム]
        Daily1 --> Review1[スプリントレビュー]
        Review1 --> Retro1[レトロスペクティブ]
    end
    
    subgraph "スプリント2"
        Planning2[スプリント計画] --> Daily2[デイリースクラム]
        Daily2 --> Review2[スプリントレビュー]
        Review2 --> Retro2[レトロスペクティブ]
    end
    
    subgraph "スプリント3"
        Planning3[スプリント計画] --> Daily3[デイリースクラム]
        Daily3 --> Review3[スプリントレビュー]
        Review3 --> Retro3[レトロスペクティブ]
    end
    
    Retro1 --> Planning2
    Retro2 --> Planning3
    
    classDef planning fill:#e3f2fd,stroke:#1976d2
    classDef daily fill:#e8f5e8,stroke:#388e3c
    classDef review fill:#fff3e0,stroke:#f57c00
    classDef retro fill:#fce4ec,stroke:#c2185b
    
    class Planning1,Planning2,Planning3 planning
    class Daily1,Daily2,Daily3 daily
    class Review1,Review2,Review3 review
    class Retro1,Retro2,Retro3 retro
```

```mermaid
flowchart LR
    subgraph "スプリント1"
        Planning1[スプリント計画] --> Daily1[デイリースクラム]
        Daily1 --> Review1[スプリントレビュー]
        Review1 --> Retro1[レトロスペクティブ]
    end
    
    subgraph "スプリント2"
        Planning2[スプリント計画] --> Daily2[デイリースクラム]
        Daily2 --> Review2[スプリントレビュー]
        Review2 --> Retro2[レトロスペクティブ]
    end
    
    subgraph "スプリント3"
        Planning3[スプリント計画] --> Daily3[デイリースクラム]
        Daily3 --> Review3[スプリントレビュー]
        Review3 --> Retro3[レトロスペクティブ]
    end
    
    Retro1 --> Planning2
    Retro2 --> Planning3
    
    classDef planning fill:#e3f2fd,stroke:#1976d2
    classDef daily fill:#e8f5e8,stroke:#388e3c
    classDef review fill:#fff3e0,stroke:#f57c00
    classDef retro fill:#fce4ec,stroke:#c2185b
    
    class Planning1,Planning2,Planning3 planning
    class Daily1,Daily2,Daily3 daily
    class Review1,Review2,Review3 review
    class Retro1,Retro2,Retro3 retro
```

---

## 📋 チートシート：いつでも使える早見表

### 基本構文

| 図表タイプ | 開始コマンド | 用途 |
|----------|------------|------|
| フローチャート | `flowchart TD` | プロセスフロー |
| シーケンス図 | `sequenceDiagram` | システム間通信 |
| ER図 | `erDiagram` | データベース設計 |
| クラス図 | `classDiagram` | オブジェクト設計 |
| 状態図 | `stateDiagram-v2` | 状態遷移 |
| ガントチャート | `gantt` | プロジェクト管理 |
| マインドマップ | `mindmap` | アイディア整理 |
| ジャーニーマップ | `journey` | ユーザー体験 |

### よく使うノード形状

```
flowchart LR
    A[四角形] --> B(丸角四角形)
    B --> C([楕円])
    C --> D{ダイヤモンド}
    D --> E[["サブルーチン"]]
    E --> F[(データベース)]
    F --> G[("円形")]
    G --> H>"非対称"]
```

```mermaid
flowchart LR
    A[四角形] --> B(丸角四角形)
    B --> C([楕円])
    C --> D{ダイヤモンド}
    D --> E[["サブルーチン"]]
    E --> F[(データベース)]
    F --> G[("円形")]
    G --> H>"非対称"]
```

### 矢印の種類 - GitHub対応版

```
flowchart LR
    A -->|実線矢印| B
    C ---|実線| D
    E -.->|点線矢印| F
    G ==>|太矢印| H
```

```mermaid
flowchart LR
    A -->|実線矢印| B
    C ---|実線| D
    E -.->|点線矢印| F
    G ==>|太矢印| H
```

### スタイリング例

```
flowchart TD
    A[Normal] --> B[Styled]
    
    classDef redBox fill:#ff9999,stroke:#333,stroke-width:2px
    classDef blueBox fill:#9999ff,stroke:#333,stroke-width:2px
    
    class A redBox
    class B blueBox
```

```mermaid
flowchart TD
    A[Normal] --> B[Styled]
    
    classDef redBox fill:#ff9999,stroke:#333,stroke-width:2px
    classDef blueBox fill:#9999ff,stroke:#333,stroke-width:2px
    
    class A redBox
    class B blueBox
```

### 色パレット推奨

```
flowchart TD
    subgraph "推奨カラーパレット"
        A[プライマリ<br/>#1976d2] --> B[セカンダリ<br/>#388e3c]
        B --> C[アクセント<br/>#f57c00]
        C --> D[エラー<br/>#d32f2f]
        D --> E[警告<br/>#f9a825]
        E --> F[情報<br/>#0288d1]
    end
    
    classDef primary fill:#e3f2fd,stroke:#1976d2
    classDef secondary fill:#e8f5e8,stroke:#388e3c
    classDef accent fill:#fff3e0,stroke:#f57c00
    classDef error fill:#ffebee,stroke:#d32f2f
    classDef warning fill:#fff8e1,stroke:#f9a825
    classDef info fill:#e1f5fe,stroke:#0288d1
    
    class A primary
    class B secondary
    class C accent
    class D error
    class E warning
    class F info
```

```mermaid
flowchart TD
    subgraph "推奨カラーパレット"
        A[プライマリ<br/>#1976d2] --> B[セカンダリ<br/>#388e3c]
        B --> C[アクセント<br/>#f57c00]
        C --> D[エラー<br/>#d32f2f]
        D --> E[警告<br/>#f9a825]
        E --> F[情報<br/>#0288d1]
    end
    
    classDef primary fill:#e3f2fd,stroke:#1976d2
    classDef secondary fill:#e8f5e8,stroke:#388e3c
    classDef accent fill:#fff3e0,stroke:#f57c00
    classDef error fill:#ffebee,stroke:#d32f2f
    classDef warning fill:#fff8e1,stroke:#f9a825
    classDef info fill:#e1f5fe,stroke:#0288d1
    
    class A primary
    class B secondary
    class C accent
    class D error
    class E warning
    class F info
```

---

## 🔧 トラブルシューティング：GitHub対応版

### よくあるエラーと対処法

#### 1. クラス図でのメソッド記述エラー
**❌ NG例:**
```
+login(password: string): boolean
```

**✅ OK例:**
```
+login(password) boolean
```

#### 2. Gitgraphが表示されない
GitHubではgitgraphがサポートされていないため、フローチャートで代替：

**❌ NG例:**
```
gitgraph:
    commit id: "Initial"
```

**✅ OK例:**
```
flowchart TD
    A[Initial Commit] --> B[Feature Branch]
    B --> C[Merge to Main]
```

#### 3. 複雑な矢印が表示されない
一部の矢印記法はサポートされていません：

**❌ NG例:**
```
A -.-.-> B
A ====> B
```

**✅ OK例:**
```
A -.-> B
A ==> B
```

#### 4. 日本語フォントの問題
日本語を使用する際は、短い文章を心がけ、必要に応じて英語併記：

**✅ 推奨:**
```
A[ユーザー登録<br/>User Registration] --> B[認証<br/>Authentication]
```

---

## 🎯 実践課題

### 課題1：基本レベル
あなたの会社の「新入社員研修プロセス」をフローチャートで描いてください。

### 課題2：中級レベル
ECサイトのユーザー、商品、注文のER図を作成してください。

### 課題3：上級レベル
マイクロサービス間の商品注文処理をシーケンス図で表現してください。

### 課題4：実践レベル
CI/CDパイプラインの障害発生時の対応フローを状態図で表現してください。

---

## 📚 さらなる学習リソース

1. **Mermaid公式ドキュメント**: https://mermaid.js.org/
2. **Mermaid Live Editor**: https://mermaid.live/
3. **GitHubでのMermaid活用**: README.mdに直接埋め込み可能
4. **VS Code拡張**: Mermaid Preview
5. **Notion対応**: `/code` ブロックで `mermaid` を選択

---

## 💡 プロからのアドバイス

### ✅ Do（推奨）
- **シンプルに保つ**: 複雑すぎる図は理解が困難
- **一貫性を保つ**: 命名規則とスタイルを統一
- **段階的に作成**: 大きな図は小さなパーツから組み立て
- **定期的な更新**: システム変更時は図も更新
- **GitHubでテスト**: 本番投入前に必ずGitHubで表示確認

### ❌ Don't（非推奨）
- **情報の詰め込みすぎ**: 1つの図に多すぎる要素
- **不明確なラベル**: 略語だけの説明
- **古い図の放置**: 実装と乖離した図
- **未対応構文の使用**: GitHub未対応の記法は避ける

### 🚀 プロダクトマネージャー向け特別Tips

#### 1. ステークホルダー向け図表作成
```
flowchart TD
    subgraph "経営陣向け"
        A[高レベル概要図]
        B[ROI関連図]
    end
    
    subgraph "開発チーム向け"
        C[詳細技術図]
        D[実装フロー図]
    end
    
    subgraph "営業向け"
        E[機能概要図]
        F[競合比較図]
    end
    
    A --> C
    B --> E
    C --> D
    E --> F
```

```mermaid
flowchart TD
    subgraph "経営陣向け"
        A[高レベル概要図]
        B[ROI関連図]
    end
    
    subgraph "開発チーム向け"
        C[詳細技術図]
        D[実装フロー図]
    end
    
    subgraph "営業向け"
        E[機能概要図]
        F[競合比較図]
    end
    
    A --> C
    B --> E
    C --> D
    E --> F
```

#### 2. プロダクトロードマップ
```
gantt
    title プロダクトロードマップ 2024
    dateFormat  YYYY-MM-DD
    section Phase 1
    MVP開発           :active, mvp, 2024-01-01, 90d
    ユーザーテスト      :ut, after mvp, 30d
    
    section Phase 2
    機能拡張          :ext, after ut, 60d
    パフォーマンス改善   :perf, after ext, 30d
    
    section Phase 3
    新機能追加        :new, after perf, 90d
    スケール対応       :scale, after new, 60d
```

```mermaid
gantt
    title プロダクトロードマップ 2024
    dateFormat  YYYY-MM-DD
    section Phase 1
    MVP開発           :active, mvp, 2024-01-01, 90d
    ユーザーテスト      :ut, after mvp, 30d
    
    section Phase 2
    機能拡張          :ext, after ut, 60d
    パフォーマンス改善   :perf, after ext, 30d
    
    section Phase 3
    新機能追加        :new, after perf, 90d
    スケール対応       :scale, after new, 60d
```

#### 3. ユーザーフィードバックループ
```
flowchart LR
    subgraph "データ収集"
        A[ユーザーインタビュー]
        B[Analytics]
        C[サポート問い合わせ]
    end
    
    subgraph "分析"
        D[課題抽出]
        E[優先度付け]
    end
    
    subgraph "アクション"
        F[機能改善]
        G[新機能開発]
    end
    
    A --> D
    B --> D
    C --> D
    D --> E
    E --> F
    E --> G
    F --> A
    G --> A
```

```mermaid
flowchart LR
    subgraph "データ収集"
        A[ユーザーインタビュー]
        B[Analytics]
        C[サポート問い合わせ]
    end
    
    subgraph "分析"
        D[課題抽出]
        E[優先度付け]
    end
    
    subgraph "アクション"
        F[機能改善]
        G[新機能開発]
    end
    
    A --> D
    B --> D
    C --> D
    D --> E
    E --> F
    E --> G
    F --> A
    G --> A
```

---

## 🎊 まとめ

この教材を完了したあなたは、もう立派なMermaidエキスパートです！

### 習得したスキル
- ✅ 基本的な図表作成（フローチャート、シーケンス図）
- ✅ データベース設計（ER図）
- ✅ システム設計（クラス図、アーキテクチャ図）
- ✅ プロジェクト管理（ガントチャート、ジャーニーマップ）
- ✅ GitHub対応ベストプラクティス
- ✅ 実践的なスタイリングとレイアウト

### 次のステップ
1. **実際のプロジェクトで活用**: 日々の業務でMermaidを積極的に使用
2. **チーム展開**: 同僚にもMermaidの活用を推進
3. **継続学習**: 新機能やベストプラクティスを定期的にキャッチアップ
4. **コミュニティ参加**: Mermaidコミュニティで知見を共有

実際のプロジェクトで積極的に活用し、チーム全体のドキュメント品質向上に貢献してください！

**Perfect! 🚀**
