# Generated by Django 4.2 on 2023-04-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('endereco', models.CharField(max_length=200)),
                ('veiculo', models.CharField(max_length=15)),
                ('placa', models.CharField(max_length=7)),
            ],
        ),
    ]