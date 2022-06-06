from django import forms


MATERIAL_CHOICE = [
    ('concrete', 'concrete'),
    ('steel', 'steel'),
]

class Beam(forms.Form):
    beam_length = forms.IntegerField(label='Length (meters)')
    beam_material = forms.CharField(label='Material' ,widget=forms.Select(choices=MATERIAL_CHOICE))

'''
FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class BeamInput(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    age= forms.IntegerField()
    favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))
'''