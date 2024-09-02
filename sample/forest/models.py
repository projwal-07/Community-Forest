from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Feedback_User(models.Model):
    name = models. CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
#Creating function to store image according to the tole for respective folder
def tole_member_image_upload_path(instance, filename):
    return os.path.join(
        'tole_samiti',
        instance.tole.tole_name.replace(" ","_"),
        filename
     )

#Model for Storing Details of Tole samiti

class Tole_Samiti(models.Model):
    tole_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tole_name

class Tole_Samiti_Member(models.Model):
    POSITION_CHOICES = [
        ('chairman', 'Chairman'),
        ('secretary', 'Secretary'),
        ('treasurer', 'Treasurer'),
        ('member', 'Member'),
        ('advisor', 'Advisor'),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100,choices=POSITION_CHOICES)
    image = models.ImageField(upload_to= tole_member_image_upload_path, default='default_image.jpg')
    tole = models.ForeignKey(Tole_Samiti, on_delete=models.CASCADE, related_name='tole_samiti_members')

    def __str__(self):
        return f"{self.name} ({self.position}) - {self.tole.tole_name}"
    
#Creating function to store image according to the Chetra for respective Chetra_folder
def chetriya_member_image_upload_path(instance, filename):
    return os.path.join(
        'chetriya_samiti',
        instance.chetra.chetra_name.replace(" ","_"),
        filename
     )

#Creating Model For Chetriya Samiti

class Chetriya_Samiti(models.Model):
    chetra_name = models.CharField(max_length=100)

    def __str__(self):
        return self.chetra_name

class Chetriya_Samiti_Member(models.Model):
    POSITION_CHOICES = [
        ('chairman', 'Chairman'),
        ('secretary', 'Secretary'),
        ('treasurer', 'Treasurer'),
        ('member', 'Member'),
        ('advisor', 'Advisor'),
    ]


    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100,choices=POSITION_CHOICES)
    image = models.ImageField(upload_to= chetriya_member_image_upload_path, default='default_image.jpg')
    chetra = models.ForeignKey(Chetriya_Samiti, on_delete=models.CASCADE, related_name='chetra_samiti_members')

    def __str__(self):
        return f"{self.name} ({self.position}) - {self.chetra.chetra_name}"

#Model For Karya Samiti
#To Delete the Chetriya Samiti Image from database and device
    
@receiver(post_delete, sender=Chetriya_Samiti_Member,)
def delete_image_file(sender, instance, **kwargs):
    if instance.image and instance.image.name != 'default_image.jpg':
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
#To Delete the Tole Samiti Image from database and device
@receiver(post_delete, sender=Tole_Samiti_Member,)
def delete_image_file(sender, instance, **kwargs):
    if instance.image and instance.image.name != 'default_image.jpg':
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

