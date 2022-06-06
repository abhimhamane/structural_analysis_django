from cProfile import label
import email
from django import forms

DEPT = [('civil', 'Civil Engineering'), ('mech','Mechanical Engineering'), ('ece','Electronics and Communication'), 
            ('cse','Computer Science and Engineering'), ('min','Mining Engineering'), 
            ('meta','Metalurgical Engineering'), ('chem','Chemical Engineering'),
            ('elec','Electrical Engineering')
        ]


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    college = forms.CharField(label='College', max_length=150)
    dept = forms.ChoiceField(label='Department', choices= DEPT)
    degree = forms.ChoiceField(label='Degree', choices=[('btech','B.Tech'), ('mtech','M.Tech'), ('phd','PhD'), ('other','Other')])
    year = forms.ChoiceField(label='Year of College', choices=[('1','1'), ('2','2'), ('3','3'), ('4','4')])
    email = forms.EmailField(label='E-mail')
    feedback = forms.CharField(label='Feedback', widget=forms.Textarea)





