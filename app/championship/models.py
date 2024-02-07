from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

import os
import uuid


# Create your models here.

def championship_image_upload (instance, filename):
    """Generate filepath for championship image."""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{ext}"

    return os.path.join("uploads", 'championship', filename)

class Championship(models.Model):
    """Model of championship"""
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to=championship_image_upload, max_length=500)

    def __str__(self):
        return self.title

def event_image_upload (instance, filename):
    """Generate filepath for event image."""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{ext}"

    return os.path.join("uploads", 'event', filename)


class Event(models.Model):
    """Model of individual events, such as Cricket/Football Tournament"""
    championship = models.ForeignKey(Championship, blank=True, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    date_start = models.DateField(auto_now_add=False, null=True, blank=True)
    date_end = models.DateField(auto_now_add=False, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to=event_image_upload, max_length=500)
    category = models.CharField(max_length=255)

    teams = models.ManyToManyField("championship.Team", blank=True, related_name="events")

    def __str__(self):
        return self.title

def team_image_upload (instance, filename):
    """Generate filepath for team image."""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{ext}"

    return os.path.join("uploads", 'team', filename)

class Team(models.Model):
    """Model of Event Participant"""
    title = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(blank=True, null=True, upload_to=team_image_upload, max_length=500)
    members = models.ManyToManyField("championship.Member", blank=True, related_name="teams")

    def __str__(self):
        return self.title

def company_image_upload (instance, filename):
    """Generate filepath for company image."""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{ext}"

    return os.path.join("uploads", 'company', filename)


class Company(models.Model):
    """Model of Company"""
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to=company_image_upload, max_length=500)
    location = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "companies"
    

    def __str__(self):
        return self.name

class Member(models.Model):
    """Model of the Individual"""
    name = models.CharField(max_length=255, null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    designation = models.CharField(max_length=255, null=False, blank=False)
    # work email - for verification

    def __str__(self):
        return f"{self.name} : {self.company.name}"

class Score(models.Model):
    """Model of Score"""
    competition = models.ForeignKey('Competition', on_delete=models.CASCADE, related_name="scores")
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.CharField(max_length=255, blank=True, null=True)
    is_wicket = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.competition.title} : {self.team.title} : {self.points}"


class Competition(models.Model):
    """Model of Compentition"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False) # like "final", "semi-final", etc
    venue = models.CharField(max_length=255, null=False, blank=False)
    time = models.CharField(max_length=255, null=True, blank=True)
    competitors = models.ManyToManyField(Team, blank=True, related_name="competitions")
    is_finished = models.BooleanField(default=False, null=False, blank=False)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title

# Add default scores
@receiver(m2m_changed, sender=Competition.competitors.through)
def handle_m2m_change(sender, instance, action, **kwargs):
    if action == "post_add":
        for team in instance.competitors.all():
            exists = Score.objects.filter(team=team, competition=instance).exists()
            if not exists:
                Score.objects.create(team=team, competition=instance, points="0", is_wicket=False)
                Score.objects.create(team=team, competition=instance, points="0", is_wicket=True)

class ChampionshipHistory(models.Model):
    """Model of Championship History"""
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE, null=False, blank=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    entry_type = models.CharField(max_length=255, blank=False, null=False, default="timeline")
    time = models.DateTimeField(auto_now_add=True)

    # images
    # videos

    class Meta:
        verbose_name_plural = "championship history"

    def __str__(self):
        return f"{self.event.title} : {self.competition.title}"