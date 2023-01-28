from django.db import models
from django.urls import reverse

# Create your models here.

#featurelar
class marka(models.Model):

	markaAdi = models.CharField(max_length = 20)

	def __str__(self):
		return self.markaAdi

class oSystem(models.Model):

	oSystem = models.CharField(max_length=20)

	def __str__(self):
		return self.oSystem

class cpuType(models.Model):

	cpuType = models.CharField(max_length=10)

	def __str__(self):
		return self.cpuType

class cpuGen(models.Model):

	cpuGen = models.CharField(max_length=10)

	def __str__(self):
		return self.cpuGen

class ram(models.Model):

	ram = models.IntegerField()

	def __str__(self):
		return str(self.ram)

class diskCap(models.Model):

	diskCap = models.IntegerField()

	def __str__(self):
		return str(self.diskCap)

class diskType(models.Model):

	diskType = models.CharField(max_length=10)

	def __str__(self):
		return self.diskType

class site(models.Model):

	siteAdi = models.CharField(max_length=20)
	logo = models.CharField(max_length=20)

	def __str__(self):
		return self.siteAdi

class ekran(models.Model):

	ekran = models.CharField(max_length=6)

	def __str__(self):
		return self.ekran



#Objeler
class laptop(models.Model):

	#Fields
	modelAdi = models.CharField(max_length=20)
	modelNo = models.CharField(max_length=20)
	marka = models.ForeignKey('marka', on_delete=models.CASCADE)
	os = models.ForeignKey('oSystem', on_delete=models.CASCADE)
	cpuType = models.ForeignKey('cpuType', on_delete=models.CASCADE)
	cpuGen = models.ForeignKey('cpuGen', on_delete=models.CASCADE)
	ram = models.ForeignKey('ram', on_delete=models.CASCADE)
	diskCap = models.ForeignKey('diskCap', on_delete=models.CASCADE)
	diskType = models.ForeignKey('diskType', on_delete=models.CASCADE)
	ekran = models.ForeignKey('ekran', on_delete=models.CASCADE)
	resim = models.CharField(max_length=20)

	#Metadata

	#Methods

	def __str__(self):
		return self.modelAdi

class laptopFromSite(models.Model):

	laptop = models.ForeignKey('laptop', on_delete=models.CASCADE)
	site = models.ForeignKey('site', on_delete=models.CASCADE)
	fiyat = models.FloatField()
	puan = models.FloatField()
	URL = models.URLField(max_length = 200)

	def __str__(self):
		return str(self.id)

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])

class laptopInstance(models.Model):

	laptop = laptop = models.ForeignKey('laptop', on_delete=models.CASCADE)

	laptopDeals = [models.ManyToManyField('laptopFromSite'),
				models.ManyToManyField('laptopFromSite'),
				models.ManyToManyField('laptopFromSite')
		]

	def __str__(self):
		return str(self.id)

