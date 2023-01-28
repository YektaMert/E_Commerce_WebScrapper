from django.urls import path
from . import views

urlpatterns = [
	path('', views.pList, name='pList'),
	path('pPage/<str:laptop_id>', views.pPage, name='pPage'),
	path('filter/<str:kategori>/<str:feature_name>', views.filter, name='filter'),
	path('external/str:<url>', views.external, name='external'),
	path('sortArtanFiyat', views.sortLowestFiyat, name='artanFiyat'),
	path('sortAzalanFiyat', views.sortHighestFiyat, name='azalanFiyat'),
	path('sortHighestPuan', views.sortHighestPuan, name='sortHighestPuan'),
	path("search/", views.search, name="search"),
	path("customadmin/", views.admininitial, name="admininitial"),
]
