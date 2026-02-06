from django.contrib.auth.models import User

User.objects.get_or_create(
    username="raguna",
    defaults={"email":"demo@example.com", "password":"kaibasensei"}
)
