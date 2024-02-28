from django.forms import ModelForm
from models import MovieInfo

class MovieInfo(ModelForm):
    class Meta:
        model=MovieInfo
        fields='__all__'
        