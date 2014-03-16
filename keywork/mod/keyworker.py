import os
from django.contrib.auth.models import User

class Keyworker(User):
    class Meta:
        app_label = os.path.basename(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
