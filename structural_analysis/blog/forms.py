from django import forms


MATERIAL_CHOICE = [
    ('concrete', 'concrete'),
    ('steel', 'steel'),
]

class NameForm(forms.Form):
    beam_length = forms.FloatField(label='Length (meters)')
    beam_material = forms.CharField(label='Material' ,widget=forms.Select(choices=MATERIAL_CHOICE))
    beam_I = forms.FloatField(label='Izz')


