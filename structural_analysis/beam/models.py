from cProfile import label
from distutils.command.config import LANG_EXT
from tkinter import Widget
from django.db import models

# Create your models here.
SUPPORT_CHOICES = (
    ("pin", "Pin/Hinge"),
    ("roller", "Roller"),
    ("fix", "Fixed"),
)

class BeamModel(models.Model):
    beam_length = models.FloatField()
    beam_E = models.FloatField()
    beam_Izz = models.FloatField()
    beam_left_support = models.CharField(
                        max_length=10,
                        choices=SUPPORT_CHOICES,
                        default='pin'
                        )
    beam_right_support = models.CharField(
                        max_length=10,
                        choices=SUPPORT_CHOICES,
                        default='roller'
                        )
    def __str__(self):
        return str(self.pk) + str(self.beam_left_support)+ '_SipleBeam_' + str(self.beam_right_support)
    

    #def 


