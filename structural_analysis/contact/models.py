from django.db import models

# Create your models here.
DEPT = [('civil', 'Civil Engineering'), ('mech','Mechanical Engineering'), ('ece','Electronics and Communication'), 
            ('cse','Computer Science and Engineering'), ('min','Mining Engineering'), 
            ('meta','Metalurgical Engineering'), ('chem','Chemical Engineering'),
            ('elec','Electrical Engineering')
        ]

DEGREE = [('btech','B.Tech'), ('mtech','M.Tech'), ('phd','PhD')]

class FeedbackModel(models.Model):
    name = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    dept = models.CharField(max_length=10,
                            choices=DEPT,
                            default='civil'
                            )
    degree = models.CharField(max_length=10,
                            choices=DEGREE,
                            default='btech'
                            )
    year_study = models.IntegerField()
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return str(self.pk) + "_" + str(self.name)
