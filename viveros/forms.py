from django.forms import ModelForm
from viveros.models import Productor


# Create the form class.
class ProductorForm(ModelForm):
    class Meta:
        model = Productor
        fields = '__all__'