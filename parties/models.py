from django.db import models

class Party(models.Model):
	party_name = models.CharField(default="", max_length=200)
	litness = models.IntegerField(default=3)
	safety = models.IntegerField(default=3)
	#location = models.PointField()
	music = models.ForeignKey("Song", on_delete=models.CASCADE)
	population = models.IntegerField(default=0)
	duration = models.FloatField(default=0) # length of party in hours
	num_recommendations = models.IntegerField(default=0)
	radius = models.FloatField(default=0)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.party_name

class User(models.Model):
	cookies = models.CharField(default="", max_length=200)
	#location = models.PointField()
	party_at = models.OneToOneField("Party", on_delete=models.CASCADE)

class Organizer(models.Model):
	organization = models.CharField(default="", max_length=200) # Name of organization
	user = models.OneToOneField("User", on_delete=models.CASCADE)
	party = models.OneToOneField("Party", on_delete=models.CASCADE)
	def __str__(self):
		return self.organization

class Song(models.Model):
	title = models.CharField(default="", max_length=200)
	artist = models.CharField(default="", max_length=200)
	def __str__(self):
		return self.title + ": " + self.artist
