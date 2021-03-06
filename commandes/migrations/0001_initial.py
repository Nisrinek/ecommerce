# Generated by Django 2.0.7 on 2019-01-31 01:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='commande',
            fields=[
                ('id_commande', models.AutoField(primary_key=True, serialize=False)),
                ('type_paiement', models.CharField(choices=[('cb', 'carte_bancaire'), ('espece', 'espece'), ('en_ligne', 'en_ligne')], default='espece', max_length=30)),
                ('etat_paiement', models.BooleanField(default=False)),
                ('date_paiement', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='produit',
            fields=[
                ('categorie', models.CharField(max_length=100)),
                ('cout', models.IntegerField()),
                ('desc_produit', models.TextField()),
                ('id_produit', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('vendu', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='utilisateur',
            fields=[
                ('id_utilisateur', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=45)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='commande',
            name='produi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commandes.produit'),
        ),
        migrations.AddField(
            model_name='commande',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commandes.utilisateur'),
        ),
    ]
