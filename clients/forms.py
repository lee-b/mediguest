from django.forms import ModelForm
from models import Client
from admin_image_widget import AdminImageWidget

class ClientForm(ModelForm):
    class Meta:
        model = Client
        widgets = {
            'photo':     AdminImageWidget(),
        }

