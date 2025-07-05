from django.db import models

class TypePaiement(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField()

class Paiement(models.Model):
    employe_id = models.IntegerField()
    type_paiement = models.ForeignKey(TypePaiement, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)