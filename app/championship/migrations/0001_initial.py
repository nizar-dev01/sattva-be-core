# Generated by Django 4.2.2 on 2024-01-24 19:36

import championship.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to=championship.models.championship_image_upload)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to=championship.models.company_image_upload)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('venue', models.CharField(max_length=255)),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='championship.company')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to=championship.models.team_image_upload)),
                ('members', models.ManyToManyField(blank=True, related_name='teams', to='championship.member')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.CharField(blank=True, max_length=255, null=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='championship.competition')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='championship.competition')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_start', models.DateField(blank=True, null=True)),
                ('date_end', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to=championship.models.event_image_upload)),
                ('category', models.CharField(max_length=255)),
                ('championship', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='championship.championship')),
                ('teams', models.ManyToManyField(related_name='events', to='championship.team')),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='competitors',
            field=models.ManyToManyField(blank=True, null=True, related_name='competitions', to='championship.team'),
        ),
        migrations.AddField(
            model_name='competition',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='championship.event'),
        ),
        migrations.AddField(
            model_name='company',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='championship.team'),
        ),
        migrations.CreateModel(
            name='ChampionshipHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(blank=True, null=True)),
                ('entry_type', models.CharField(default='timeline', max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('championship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='championship.championship')),
                ('competition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='championship.competition')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='championship.event')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='championship.team')),
            ],
        ),
    ]
