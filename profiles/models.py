from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from embed_video.fields import EmbedVideoField
from versatileimagefield.fields import VersatileImageField


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	INDIVIDUAL = 'IN'
	COMPANY = 'CO'
	ACCOUNT_CHOICES = (
		(INDIVIDUAL, 'Individual'),
		(COMPANY, 'Company'),
	)
	account_type = models.CharField(
		max_length=2,
		choices = ACCOUNT_CHOICES,
		blank=False,
	)
	display_name = models.CharField(blank=True, max_length=255)
	image = VersatileImageField(
		upload_to='profile_image',
		blank=True
	)
	website = models.CharField(blank=True, max_length=255)
	facebook = models.CharField(blank=True, max_length=255)
	twitter = models.CharField(blank=True, max_length=255)
	pinterest = models.CharField(blank=True, max_length=255)
	instagram = models.CharField(blank=True, max_length=255)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=16)
	standard_video = EmbedVideoField(blank=True, max_length=255)
	vr_video = EmbedVideoField(blank=True, max_length=255)
	recommend = models.ManyToManyField("self", related_name="recommends", symmetrical=False, blank=True)
	indifferent = models.ManyToManyField("self", related_name="is_indifferent", symmetrical=False, blank=True)
	donotrecommend = models.ManyToManyField("self", related_name="does_not_recommend", symmetrical=False, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()