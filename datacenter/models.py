from django.db import models
from datetime import timedelta
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self) -> timedelta:
        leave_time = localtime()
        if self.leaved_at:
            leave_time = localtime(self.leaved_at)
        return leave_time - localtime(self.entered_at)

    def format_duration(self) -> str:
        return f'{str(self.get_duration()).split(".")[0]}'

    def is_visit_long(self, minutes=60):
        return self.get_duration().total_seconds() >= minutes*60

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )
