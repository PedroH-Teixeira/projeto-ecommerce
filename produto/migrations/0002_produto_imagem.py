# Generated by Django 4.1.2 on 2022-10-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m/'),
        ),
    ]