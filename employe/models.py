from django.db import models

class Employe(models.Model):
    utilisateur_id = models.IntegerField()
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)