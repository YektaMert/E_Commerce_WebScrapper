from http.client import HTTPResponse
from turtle import update
from django.shortcuts import render, redirect
from pymongo import MongoClient
import pymongo
from . import dbfuncs
#import dbfuncs

#mongodbye bağlanma
client = pymongo.MongoClient('localhost', 27017)
db = client['dataTest']

#objectid get
#colname = db["laptoplar"]
#data = colname.find_one({"marka": "Lenovo"})
#print(data["_id"])


# Create your views here.

# initial laptop liste sayfası/homepage 
def pList(request):
	dbfuncs.update_filters(db)
	context = {
		"laptoplar": dbfuncs.get_all_laptops(db),
		"filtreler": dbfuncs.get_filters(db)
	}
	return render(request, 'productListPage/productListPage.html', context)

#laptop detay sayfası, tek bir laptop objesini alır productPage'e gönderir
def pPage(request, laptop_id):
	#context must be a dictionary
	print(dbfuncs.get_specific_laptop(db, laptop_id))
	context = { "laptoplar": dbfuncs.get_specific_laptop(db, laptop_id) }
	return render(request, 'productListPage/productPage.html', context)

#laptopun orijinal sitesine gitmek için
def external(request, url):
	return redirect(url)

def filter(request, kategori ,feature_name):
	context = {
		"laptoplar": dbfuncs.get_filter_laptops(db, kategori, feature_name),
		"filtreler": dbfuncs.get_filters(db)
	}
	return render(request, 'productListPage/productListPage.html', context)

#search view
def search(request):
	if request.method == "GET":

		query = request.GET.get('search')
		if query == '':

			query = 'None'


	context = {
		"laptoplar": dbfuncs.get_search(db, query),
		"filtreler": dbfuncs.get_filters(db)
	}

	return render(request, 'productListPage/productListPage.html', context)

#sort viewları
def sortHighestFiyat(request):
	context = {
		"laptoplar": dbfuncs.sort_highest_fiyat(db),
		"filtreler": dbfuncs.get_filters(db)
	}
	return render(request, 'productListPage/productListPage.html', context)

def sortLowestFiyat(request):
	context = {
		"laptoplar": dbfuncs.sort_lowest_fiyat(db),
		"filtreler": dbfuncs.get_filters(db)
	}
	return render(request, 'productListPage/productListPage.html', context)

def sortHighestPuan(request):
	context = {
		"laptoplar": dbfuncs.sort_highest_puan(db),
		"filtreler": dbfuncs.get_filters(db)
	}
	return	render(request, 'productListPage/productListPage.html', context)

def admininitial(request):
	context = {

	}
	return render(request, 'productListPage/admin.html', context)