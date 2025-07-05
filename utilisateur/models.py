from django.db import models
from django.contrib.auth.hashers import make_password

class Utilisateur(models.Model):
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)
    role = models.CharField(max_length=50, choices=[('ADMIN', 'Admin'), ('AGENT', 'Agent'), ('FINANCE', 'Finance')])
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.mot_de_passe.startswith('pbkdf2_'):
            self.mot_de_passe = make_password(self.mot_de_passe)
        super().save(*args, **kwargs)