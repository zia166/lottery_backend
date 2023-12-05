from datetime import datetime
from django.db import models

class Performance(models.Model):
    performance_id = models.IntegerField(primary_key=True)
    performance_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    available_tickets = models.IntegerField()

    def __str__(self):
        return self.performance_name
    class Meta:
        db_table = 'performances'


class LotteryEntry(models.Model):
    username = models.CharField(max_length=255)
    performance_name = models.CharField(max_length=255)
    no_of_tickets = models.IntegerField()
    show_time = models.TimeField()
    entry_time = models.DateTimeField()
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'lottery_entries'


class Winner(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    no_of_ticket = models.IntegerField()
    winning_time = models.DateTimeField()

    def __str__(self):
        return f"{self.username} - {self.performance}"

    class Meta:
        db_table = 'winners'
       