# Generated by Django 4.2 on 2023-04-26 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_servicos_ordemservico'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemservico',
            name='tipo',
            field=models.CharField(choices=[('MOTO', 'Moto'), ('PEQUENO', 'Pequeno'), ('MEDIO', 'Médio'), ('GRANDE', 'Grande')], default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='veiculo',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='core.clientes'),
        ),
    ]
