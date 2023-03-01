from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateField()
    matn = models.TextField()
    rasm = models.FileField()
    def __str__(self):
        return self.sarlavha

class Intervyu(models.Model):
    sana = models.DateField()
    sarlavha = models.CharField(max_length=50)
    video = models.CharField(max_length=100)
    def __str__(self):
        return self.sarlavha
