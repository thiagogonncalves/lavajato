# Generated by Django 4.2 on 2023-04-26 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('valor_os', models.DecimalField(decimal_places=3, max_digits=6)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clientes')),
                ('servico', models.ManyToManyField(to='core.servicos')),
            ],
        ),
    ]