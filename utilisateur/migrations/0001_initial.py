# Generated by Django 5.2.3 on 2025-07-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mot_de_passe', models.CharField(max_length=128)),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('AGENT', 'Agent'), ('FINANCE', 'Finance')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
