from django.contrib import admin

from .models import marka, oSystem, cpuType, cpuGen, ram, diskType, diskCap, site, ekran, laptop, laptopFromSite, laptopInstance

# Register your models here.

admin.site.register(marka)
admin.site.register(oSystem)
admin.site.register(cpuType)
admin.site.register(cpuGen)
admin.site.register(ram)
admin.site.register(diskType)
admin.site.register(diskCap)
admin.site.register(site)
admin.site.register(ekran)
admin.site.register(laptop)
admin.site.register(laptopFromSite)
admin.site.register(laptopInstance)
