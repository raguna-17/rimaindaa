from django.contrib.auth.models import User

if not User.objects.filter(username="raguna").exists():
    User.objects.create_user("raguna", "demo@example.com", "raguna")