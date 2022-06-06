from django.db import models

# Create your models here.
class BeamModel(models.Model):
    beam_length = models.FloatField()
    beam_E = models.FloatField()
    beam_Izz = models.FloatField()

class SupportModel(models.Model):
    pass

class UDLModel(models.Model):
    
    pass

class PointLoadModel(models.Model):

    pass

class PointMomentModel(models.Model):

    pass

