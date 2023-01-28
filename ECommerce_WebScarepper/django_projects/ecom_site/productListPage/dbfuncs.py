from tkinter import image_types
import pymongo
from bson import ObjectId
from . import near_dup
from thefuzz import fuzz
from thefuzz import process

def get_all_laptops(db):
	
	return pack_laptop_deals(list(db["laptoplar"].find()),db)

def pack_laptop_deals(laptopdata,db):

	finaldata = [

	] 

	
	for laptop in laptopdata:

		reldeals = list(db["deals"].find({"laptopid": str(laptop["_id"])}).sort("fiyat"))
		tempdic = {}
		tempdic["laptop"] = laptop
		tempdic["deals"] = reldeals
		finaldata.append(tempdic)

	
	return finaldata

def get_specific_laptop(db, laptop_id):
	return	pack_laptop_deals(list(db["laptoplar"].find({"_id": ObjectId(laptop_id)})), db)

def get_filters(db):
	tempdic = { }
	tempdic["marka"] = list(db["markalar"].find().sort("deger"))
	tempdic["oSystem"] = list(db["osystems"].find().sort("deger"))
	tempdic["cpuType"] = list(db["cputypes"].find().sort("deger"))
	tempdic["cpuGen"] = list(db["cpugens"].find().sort("deger"))
	tempdic["ramCap"] = list(db["ramcaps"].find().sort("deger"))
	tempdic["diskCap"] = list(db["diskcaps"].find().sort("deger"))
	tempdic["diskType"] = list(db["disktypes"].find().sort("deger"))
	tempdic["ekran"] = list(db["ekranboyutlari"].find().sort("deger"))
	
	return tempdic

def update_filters(db):
	near_dup.update_all_filters(db)
	

#ram int olduğu için sıkıntı çıkıyor
def get_filter_laptops(db, kategori, feature_name):
    return pack_laptop_deals(list(db["laptoplar"].find({kategori: feature_name})),db)

def get_search(db, query):
	#aramaya karar verme
	aranancomp = {}
	aranancomp["eslesen"] = query
	aranancomp["ratio"] = 50
	ratio = fuzz.ratio("trendyol",query.lower())
	if aranancomp["ratio"] < ratio:
		aranancomp["eslesen": "Trendyol", "ratio": ratio, "kategori": "site"]
	ratio = fuzz.ratio("vatan",query.lower())
	if aranancomp["ratio"] < ratio:
		aranancomp["eslesen": "Vatan", "ratio": ratio, "kategori": "site"]
	ratio = fuzz.ratio("n11",query.lower())
	if aranancomp["ratio"] < ratio:
		aranancomp["eslesen": "n11", "ratio": ratio, "kategori": "site"]

	filtreler = get_filters(db)
	for marka in filtreler["marka"]:
		ratio = fuzz.ratio(marka["deger"].lower(),query.lower())
		if aranancomp["ratio"] < ratio:
			aranancomp["eslesen"] =  marka["deger"]
			aranancomp["ratio"] = ratio
			aranancomp["kategori"] = "marka"

	for osys in filtreler["oSystem"]:
		ratio = fuzz.ratio(osys["deger"].lower(),query.lower())
		if aranancomp["ratio"] < ratio:
			aranancomp["eslesen"] =  osys["deger"]
			aranancomp["ratio"] = ratio
			aranancomp["kategori"] = "oSystem"

	for cputype in filtreler["cpuType"]:
		ratio = fuzz.ratio(cputype["deger"].lower(),query.lower())
		if aranancomp["ratio"] < ratio:
			aranancomp["eslesen"] =  cputype["deger"]
			aranancomp["ratio"] = ratio
			aranancomp["kategori"] = "cpuType"

	for cpugen in filtreler["cpuGen"]:
		try:
			ratio = fuzz.ratio(cpugen["deger"].lower(),query.lower())
			if aranancomp["ratio"] < ratio:
				aranancomp["eslesen"] =  cpugen["deger"]
				aranancomp["ratio"] = ratio
				aranancomp["kategori"] = "cpuGen"
		except:
			pass
	
	for ramcap in filtreler["ramCap"]:
		ratio = fuzz.ratio(ramcap["deger"].lower(),query.lower())
		if aranancomp["ratio"] < ratio:
			aranancomp["eslesen"] =  ramcap["deger"]
			aranancomp["ratio"] = ratio
			aranancomp["kategori"] = "ramCap"

	for diskcap in filtreler["diskCap"]:
		ratio = fuzz.ratio(diskcap["deger"].lower(),query.lower())
		if aranancomp["ratio"] < ratio:
			aranancomp["eslesen"] =  diskcap["deger"]
			aranancomp["ratio"] = ratio
			aranancomp["kategori"] = "diskCap"

	for disktype in filtreler["diskType"]:
		ratio = fuzz.ratio(disktype["deger"].lower(),query.lower())
		if aranancomp["ratio"] < ratio:
			aranancomp["eslesen"] =  disktype["deger"]
			aranancomp["ratio"] = ratio
			aranancomp["kategori"] = "diskType"

	for ekran in filtreler["ekran"]:
		ratio = fuzz.ratio(ekran["deger"].lower(),query.lower())
		if aranancomp["ratio"] < ratio:
			aranancomp["eslesen"] =  ekran["deger"]
			aranancomp["ratio"] = ratio
			aranancomp["kategori"] = "ekran"

	print(aranancomp)
	print(query)
	print(fuzz.ratio(query, "asus"))
	try:
		if aranancomp["kategori"] == "site":
			return
	except:
		pass

	try:
		return pack_laptop_deals(list(db["laptoplar"].find({aranancomp["kategori"]: aranancomp["eslesen"]})), db)
		print("alo")
	except:
		pass
	return 
	

	




	

def sort_highest_fiyat(db):
	sorted = get_all_laptops(db)
	sorted.sort(key=sort_func, reverse=True)
	return sorted

def sort_lowest_fiyat(db):
	sorted = get_all_laptops(db)
	sorted.sort(key=sort_func)
	return sorted

def sort_highest_puan(db):
	sorted = get_all_laptops(db)
	sorted.sort(key=sort_puan_func, reverse=True)
	return sorted



def sort_func(laptop):
	try:
		return laptop["deals"][0]["fiyat"]
	except:
		pass

def sort_puan_func(laptop):
	ortalama = 0.0
	for deal in laptop["deals"]:
		ortalama += deal["puan"]
	

	return ortalama/len(laptop["deals"])


#test laptop data
#data = {
#	"laptoplar": [
#		{
#			"modelAdi": "mdgmsa56",
#			"modelNo": "155131f",
#			"marka": "Lenovo",
#			"oSystem": "Windows",
#			"cpuType": "i7",
#			"cpuGen": "11",
#			"ramCap": 16,
#			"diskCap": "512gb",
#			"diskType": "SSD",
#			"ekran": '15.6"',
#		},
#		{
#			"modelAdi": "skalfk876",
#			"modelNo": "1154621gx",
#			"marka": "MSI",
#			"oSystem": "Windows",
#			"cpuType": "i9",
#			"cpuGen": "12",
#			"ramCap": 32,
#			"diskCap": "1TB",
#			"diskType": "SSD",
#			"ekran": '17.3"',
#		},
#		{
#			"modelAdi": "mdfjfla51",
#			"modelNo": "1545654a",
#			"marka": "Asus",
#			"oSystem": "Windows",
#			"cpuType": "i5",
#			"cpuGen": "10",
#			"ramCap": 8,
#			"diskCap": "256gb",
#			"diskType": "SSD",
#			"ekran": '14"',
#		}
#	]
#}

#siteye gönderilecek veri şeması
#dealcol = db["deals"]
#finaldata = {
#		productListPage'e giden kısım
#    "laptoplar": [
#			_laptop'a giden kısım
#        {
#            "laptop": {
#                "modelAdi": "mdfjfla51",
#			    "modelNo": "1545654a",
#			    "marka": "Asus",
#			    "oSystem": "Windows",
#			    "cpuType": "i5",
#                "cpuGen": "10",
#                "ramCap": 8,
#                "diskCap": "256gb",
#                "diskType": "SSD",
#                "ekran": '14"',
#            },
#            "deals": [
#                {	 
#					 "_id": sasdfad
#					 "laptopid": "afadgadgadga"
#                    "site": "hepsiburada"
#					 "fiyat": 14131
#					 "puan": 4
#					 "URL": "afadgad"
#                },
#                {
#                    "sitead": "n11"
#                },
#                {
#                    "sitead": "vatan"
#                }
#            ]
#        }
#    ]
#}

#print(finaldata["laptoplar"][0]["laptop"]["modelAdi"])
#print(finaldata["laptoplar"][0]["deals"][2]["sitead"])

#ek = {"sitead": "mediamarkt"}
#finaldata["laptoplar"][0]["deals"].append(ek)

#for i in finaldata["laptoplar"][0]["deals"]:
#    print(i["sitead"])


#dealsa many insert
#dealdata = [
#		
#		{
#			"laptopid": "63528e4cb62082adaa81ffdb",
#			"site": "Hepsiburada",
#			"fiyat": 17000.5,
#			"puan": 4.4,
#			"URL": "https://www.hepsiburada.com/63528e4cb62082adaa81ffdb"
#		},
#		{
#			"laptopid": "63528e4cb62082adaa81ffdb",
#			"site": "Vatan",
#			"fiyat": 15000.5,
#			"puan": 4.4,
#			"URL": "https://www.vatanbilgisayar.com/63528e4cb62082adaa81ffdb"
#		},
#		{
#			"laptopid": "63528e4cb62082adaa81ffdb",
#			"site": "n11",
#			"fiyat": 16000.5,
#			"puan": 4.7,
#			"URL": "https://www.n11.com/63528e4cb62082adaa81ffdb"
#		},
#		{
#			"laptopid": "63528e740083dee74adbbbb0",
#			"site": "Vatan",
#			"fiyat": 13000.5,
#			"puan": 4.1,
#			"URL": "https://www.vatanbilgisayar.com/63528e740083dee74adbbbb0"
#		},
#		{
#			"laptopid": "63528e84161e05fb5190ef81",
#			"site": "n11",
#			"fiyat": 22000.5,
#			"puan": 4.6,
#			"URL": "https://www.n11.com/63528e84161e05fb5190ef81"
#		},
#		{
#			"laptopid": "63528e84161e05fb5190ef81",
#			"site": "Hepsiburada",
#			"fiyat": 8000.5,
#			"puan": 3.4,
#			"URL": "https://www.hepsiburada.com/63528e84161e05fb5190ef81"
#		}
#	]

    #dealcol.insert_many(dealdata)
