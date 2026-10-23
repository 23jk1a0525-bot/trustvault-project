

#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py migrate

python manage.py shell -c "
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ['DJANGO_SUPERUSER_USERNAME']
password = os.environ['DJANGO_SUPERUSER_PASSWORD']

user, created = User.objects.get_or_create(
    username=username,
    defaults={'is_staff': True, 'is_superuser': True}
)

if created:
    user.set_password(password)
    user.save()
elif not user.check_password(password):
    print('Existing account found; password was not changed.')
"

