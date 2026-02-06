# Memo App

Django REST Framework を用いたバックエンド API と、React + Vite によるフロントエンドで構成されたメモ管理アプリです。
JWT 認証を採用し、ユーザーごとにメモを安全に管理できます。

デモURL
https://rimaindaa-1.onrender.com/


## 主な機能

ユーザー認証（JWT）

メモの作成 / 取得 / 更新 / 削除（CRUD）

認証ユーザーごとのデータ分離

フロントエンドとバックエンドの完全分離構成

Docker を用いた開発・デプロイ対応

## 技術スタック
### Backend

Python 3.12

Django

Django REST Framework

SimpleJWT

Gunicorn

PostgreSQL

Docker

### Frontend

React

Vite

TypeScript

Docker

### Infrastructure

Render

Docker Compose（ローカル開発用）



## 環境変数
Backend（例）
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:pass@host:port/dbname

Frontend（例）
VITE_API_URL=https://<backend-service>.onrender.com


※ 実際の値は .env.example を参照してください。

## ローカル起動（Docker 不使用）
### Backend
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### Frontend
cd frontend
npm install
npm run dev


ブラウザで http://localhost:5173 にアクセス。

## Docker を使った起動（推奨）
docker-compose up --build


backend / frontend を同時に起動します。

## API 概要

エンドポイントは /api/ 配下

JWT による認証必須

開発環境では CORS を全許可

## テスト

pytest によるテスト実行可能

docker-compose exec web pytest

## デプロイ

Render にデプロイ済み

Backend / Frontend を別サービスとして構成

環境変数は Render 側で設定

## 補足

静的ファイルは STATIC_ROOT=staticfiles/ に集約

エントリーポイントで migrate / collectstatic を実行