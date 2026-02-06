# MemoApp

Django + DRF + Docker で動作するメモ管理 API。
ユーザーごとのメモ・リマインダー・通知を管理し、JWT 認証対応。

## 環境構築（Docker 前提）
##### プロジェクトをクローン
git clone https://github.com/raguna-17/rimaindaa
cd backend

### 環境変数を設定 (.env)
cp .env.example .env
###### SECRET_KEY, DEBUG, DATABASE_URL を設定

# Docker コンテナ起動
docker-compose up --build


API は http://localhost:8000/api/ 配下で利用可能

Django 管理画面は http://localhost:8000/admin/

## 依存関係

Python >= 3.12

Django >= 5.2

djangorestframework / djangorestframework-simplejwt

psycopg2-binary / gunicorn / python-decouple / dj-database-url

whitenoise / django-cors-headers

テスト用:

pytest / pytest-django / pytest-cov

## API エンドポイント
機能	URL	メソッド
メモ一覧/作成	/api/memos/	GET / POST
リマインダー一覧/作成	/api/reminders/	GET / POST
通知一覧	/api/notifications/	GET
JWT トークン取得	/api/token/	POST
JWT リフレッシュ	/api/token/refresh/	POST
✅ テストとカバレッジ（Docker 内）

# カバレッジも自動測定（pytest.ini に設定済み）
docker-compose run backend pytest


カバレッジ率: 現状 97%

重要機能（ユーザー登録、メモ作成、リマインダー作成、通知生成）はすべてカバー済み

## CI / Lint

GitHub Actions で CI 構築済み

Push / Pull Request 時に自動でテスト + カバレッジ + Flake8 Lint 実行

