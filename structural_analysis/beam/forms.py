from django import forms

from .models import BeamModel


class BeamInput(forms.ModelForm):
    class Meta:
        model = BeamModel
        fields = "__all__"

