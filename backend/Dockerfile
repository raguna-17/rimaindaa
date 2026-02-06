# -------------------------
# ベースイメージ
# -------------------------
FROM python:3.12-slim

# -------------------------
# 作業ディレクトリ
# -------------------------
WORKDIR /app

# -------------------------
# システム依存パッケージ
# -------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# -------------------------
# Pythonパッケージ
# -------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------
# アプリコピー
# -------------------------
COPY . .

# -------------------------
# 環境変数
# -------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -------------------------
# 本番用エントリーポイント
# -------------------------
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# -------------------------
# コンテナ起動コマンド
# -------------------------
ENTRYPOINT ["/app/entrypoint.sh"]
