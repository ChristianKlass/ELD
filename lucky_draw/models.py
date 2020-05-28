from django.db import models
import random
from datetime import datetime


# Create your models here.
class Event(models.Model):
    """Event"""
    name = models.CharField(max_length=100)
    total_number_of_winners = models.IntegerField(default=random.randint(30, 100))

    """To print human readable name when you refer to yourself (Apocalypse instead of Event 003)"""
    def __str__(self):
        return self.name


class Draw(models.Model):
    """Grand Draw, Consolation, Pre-Event"""
    name = models.CharField(max_length=100)
    number_of_winners = models.IntegerField(default=random.randint(10, 30))
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = (('event', 'name'),)

    def __str__(self):
        return self.name


class Contestant(models.Model):
    """Contestant"""
    full_name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(default='test@test.com')

    ticket_number = models.IntegerField(default=random.randint(1, 10000), unique=True)
    table_number = models.IntegerField(default=random.randint(1, 50))

    other_id = models.CharField(max_length=50, blank=True)
    custom_field = models.CharField(max_length=50, blank=True)

    """The event the contestant is attending; possible to have the same contestant attending different events"""
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = (('ticket_number', 'event'),)

    def __str__(self):
        return self.full_name


class Prize(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    """1st, 2nd, 3rd, etc"""
    draw = models.ForeignKey('Draw', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    won_by = models.ForeignKey('Contestant', on_delete=models.CASCADE, null=True)

    class Meta:
        """Each individual prize can only be drawn by one Contestant exactly ONCE per event"""
        unique_together = (('number', 'event', 'draw', 'won_by'),)
        ordering = ['number']

    def __str__(self):
        return self.name
