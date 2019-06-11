from django import forms
from WebApp.models import OnlineOp
class OnlineForm(forms.ModelForm):
    class Meta:
        model=OnlineOp
        fields="__all__"
