from django.db import models

class Notification(models.Model):
    destinataire_id = models.IntegerField()
    titre = models.CharField(max_length=255)
    message = models.TextField()
    type_notification = models.CharField(max_length=50, choices=[('SYSTEME', 'Système'), ('PAIEMENT', 'Paiement'), ('SECURITE', 'Sécurité')])
    importance = models.CharField(max_length=10, choices=[('LOW', 'Faible'), ('MEDIUM', 'Moyenne'), ('HIGH', 'Haute')])
    objet_id = models.IntegerField(null=True, blank=True)
    read_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)