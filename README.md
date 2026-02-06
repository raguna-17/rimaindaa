# Memo App

簡単なメモ管理アプリ。バックエンドは Django + DRF、フロントエンドは React + Vite。
デモURL：　https://rimaindaa.onrender.com
（ユーザー名：raguna　、　パスワード：kaibasensei）

## ディレクトリ構成
backend/   ← Django REST API
frontend/  ← React フロントエンド
README.md  ← このファイル

## 前提環境

Python 3.12 以上

Node.js 20 以上

Docker （任意だが推奨）

PostgreSQL（DATABASE_URL指定）

## インストール & 起動
## Backend
cd backend
pip install -r requirements.txt
##### 環境変数設定
export SECRET_KEY="任意のキー"
export DEBUG=True
export DATABASE_URL="postgres://user:pass@host:port/dbname"
##### マイグレーション & サーバ起動
python manage.py migrate
python manage.py runserver

###### Frontend
cd frontend
npm install
npm run dev


ブラウザで http://localhost:5173 にアクセス。

## Docker（任意）
docker-compose up --build


（backendとfrontendを同時に立ち上げる場合、docker-compose.ymlに設定必要）

## 使用例

ログイン → JWTで認証 → メモのCRUD

APIは /api/ 以下に存在

開発中は CORS を全許可

## 開発メモ

JWT 認証は SimpleJWT 使用

静的ファイルは STATIC_ROOT = staticfiles/ にまとめる

pytest でテスト可能

## デプロイ

Render で動作確認済み

環境変数を Render 側で設定