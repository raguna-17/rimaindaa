# backend/init_demo_user.py
import os
import django

# Django を初期化
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # ←自分の settings に置き換える
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# ユーザーがいなければ作る
User.objects.get_or_create(
    username="raguna",
    defaults={"email": "demo@example.com"}
)

user = User.objects.get(username="raguna")
if not user.has_usable_password():
    user.set_password("kaibasensei")
    user.save()
