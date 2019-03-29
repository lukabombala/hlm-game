from django.db import models


class Troop(models.Model):
    troop_name = models.CharField(max_length=200)
    displayed = models.BooleanField(default=False)
    money = models.IntegerField(default=0)


class Message(models.Model):
    question = models.ForeignKey(Troop, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=200)