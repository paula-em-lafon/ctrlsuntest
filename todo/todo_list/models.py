from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class Task(models.Model):
    TASK_STATUS = [
        ('NW', 'New'),
        ('IP', 'In Process'),
        ('IV', 'In Validation'),
        ('CP', 'Completed'),
        ('RJ', 'Rejected'),
    ]

    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    status = models.CharField(max_length=2,
        choices=TASK_STATUS,
        default= 'NW')

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.__old_deadline = self.deadline

    
    def clean(self):
        " Make sure expiry time cannot be in the past "
        if (not self.id or self.__old_deadline != self.deadline)\
           and self.deadline < timezone.localdate():
            raise ValidationError('Deadlines cannot be set to expire in the past')

    def __str__(self):
        return self.task_name

@receiver(pre_delete, sender=Task, dispatch_uid='task_pre_delete_signal')
def protect_posts(sender, instance, using, **kwargs):
    print(instance.status)
    if instance.status == 'CP': 
        pass
    else:  # Any other status types I add later will also be protected
        raise ValidationError('Only unpublished posts can be deleted.')

