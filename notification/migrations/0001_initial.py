# Generated by Django 5.2.3 on 2025-07-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinataire_id', models.IntegerField()),
                ('titre', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('type_notification', models.CharField(choices=[('SYSTEME', 'Système'), ('PAIEMENT', 'Paiement'), ('SECURITE', 'Sécurité')], max_length=50)),
                ('importance', models.CharField(choices=[('LOW', 'Faible'), ('MEDIUM', 'Moyenne'), ('HIGH', 'Haute')], max_length=10)),
                ('objet_id', models.IntegerField(blank=True, null=True)),
                ('read_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
