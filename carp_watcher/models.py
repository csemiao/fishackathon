from django.db import models

# Create your models here.

"""
Fish model
"""
class Fish (models.Model):
    name = models.CharField(max_length=50)
    coefficient = models.DecimalField(max_digits=10, decimal_places=2)
    exponent = models.DecimalField(max_digits=10, decimal_places=8)

    def __unicode__(self):
        return self.name

"""
Stream model
"""
class Stream (models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=12, decimal_places=9)
    long = models.DecimalField(max_digits=12, decimal_places=9)
    length = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

"""
Daily stream data for all streams
"""
class Data_Stream(models.Model):
    stream = models.ForeignKey(Stream)
    velocity = models.DecimalField(max_digits=7, decimal_places=4)
    day = models.DateTimeField()
    temp = models.IntegerField()
    spike = models.BooleanField(default=False)

    class Meta:
        ordering = ('stream', 'day')
        unique_together = ('stream', 'day')

    def __unicode__(self):
        return str(self.stream) + " " + str(self.day)

