# Generated by Django 4.2.2 on 2024-02-07 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0005_score_is_wicket'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='championship.team'),
        ),
    ]