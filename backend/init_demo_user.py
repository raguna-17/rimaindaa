# backend/init_demo_user.py
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
