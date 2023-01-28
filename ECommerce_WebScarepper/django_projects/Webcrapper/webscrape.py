from encodings import utf_8

import requests
from bs4 import BeautifulSoup    
import random
class n11:
    toplamurun=0
    result = []
    liste = list()
    sonsayi=0
    
    for i in range(1,50):

        url="https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg="+str(i)
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"lxml")
        urunler=soup.find_all("li",attrs={"class":"column"})
    

        for urun in urunler:
            dictn = {}
            urunLink=(urun.a.get("href"))
            print(urunLink)
            dictn['urunLink'] = urunLink
            urunAdi=(urun.a.get("title"))
            print(urunAdi)
            dictn['urunAdi'] = urunAdi
            
            urunFiyat=urun.find("span", attrs={"class":"newPrice cPoint priceEventClick"})
            if (urunFiyat is not None):
                print("Fiyat:",urunFiyat.text.strip())
                dictn['urunFiyati'] = urunFiyat.text.strip()
                
        
                
            
            
            
            
            urun_r=requests.get(urunLink)
            toplamurun+=1
            urun_soup=BeautifulSoup(urun_r.content,"lxml")
            
            if urun_soup.find("div",attrs={"class":"imgObj"}) is not None:
                    urun_foto = urun_soup.find("div",attrs={"class":"imgObj"}).a.get("href")
                    print(urun_foto)
                    dictn['urunFoto'] = urun_foto 
            ozellikler=urun_soup.find_all("li",attrs={"class":"unf-prop-list-item"})
            puan=(random.randint(30, 50))
            urunPuan=puan/10
            print (urunPuan)
            dictn['urunPuan'] = urunPuan
            
            for ozellik in ozellikler:
                
                model_baslık=ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text.strip()
                marka_baslık=ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text.strip()
                oSystem_baslık=ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text.strip()
                cpuType_baslık=ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text.strip()
                ramCap_baslık=ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text.strip()
                diskCap_baslık=ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text.strip()
                diskType_baslık=ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text.strip()
                ekran_baslık=ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text.strip()
                modelOzellik=ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text.strip()
                markaOzellik=ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text.strip()
                oSystemOzellik=ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text.strip()
                cpuTypeOzellik=ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text.strip()
                ramCapOzellik=ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text.strip()
                diskCapOzellik=ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text.strip()
                diskTypeOzellik=ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text.strip()
                ekranOzellik=ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text.strip()
                
                
                if(model_baslık=='Model'):
                    print("{}:{}".format("Model No",modelOzellik))
                    dictn['modelAdi'] = modelOzellik
                elif(marka_baslık=='Marka'):
                    print("{}:{}".format(marka_baslık,markaOzellik))
                    dictn['marka'] = markaOzellik
                    
                elif(oSystem_baslık=='İşletim Sistemi'):
                    print("{}:{}".format(oSystem_baslık,oSystemOzellik))
                    dictn['oSystem'] = oSystemOzellik
                elif(cpuType_baslık=='İşlemci'):
                    print("{}:{}".format("İşlemci Tipi",cpuTypeOzellik))
                    dictn['cpuType'] = cpuTypeOzellik
                elif(ramCap_baslık=='Bellek Kapasitesi'):
                    print("{}:{}".format("RAM",ramCapOzellik))
                    dictn['ramCap'] = ramCapOzellik
                elif(diskCap_baslık=='Disk Kapasitesi'):
                    print("{}:{}".format("Disk Boyutu", diskCapOzellik))
                    dictn['diskCap'] = diskCapOzellik
                elif(diskType_baslık=='Disk Türü'):
                    print("{}:{}".format(diskType_baslık,diskTypeOzellik))
                    dictn['diskType'] = diskTypeOzellik
                elif(ekran_baslık=='Ekran Boyutu'):
                    print("{}:{}".format(ekran_baslık,ekranOzellik))
                    dictn['ekran'] = ekranOzellik
            liste.append(dictn)

        
                
                
                
                
                
            print("."*50)
    #for i in liste: 
     #   if i not in result: 
      #      result.append(i)
       #     sonsayi += 1
    #print(result)
    with open(r"/Users/serhat/Desktop/Proje/E-commerceV2/django_projects/Webcrapper/list_n11.txt","w",encoding="utf8") as n11_list:
        n11_list.write('\n'.join(str(item) for item in liste))
    print("."*50)  
    print ( liste )
    #print("son ürün",sonsayi) 
    print ( toplamurun)
    
class vatan:
    
    liste = list()
    toplamurun=0


    for i in range(1,50):

        url="https://www.vatanbilgisayar.com/notebook/?page="+str(i)
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"lxml")
        urunler=soup.find_all("div",attrs={"class":"product-list product-list--list-page"})
 
 

        for urun in urunler:
            
            dictv = {}
            linksonu=urun.a.get("href")
            linkbasi="https://www.vatanbilgisayar.com/"
            link=linkbasi+linksonu
            dictv['urunLink'] = link
            
        
            print(link)
            urunAdi=urun.find("div", attrs={"class":"product-list__product-name"})
            dictv['urunAdi'] = urunAdi.text.strip()
            print(urunAdi.text)
            urunFiyat=urun.find("span", attrs={"class":"product-list__price"})
            dictv['urunFiyati'] = urunFiyat.text.strip()
        
        
        
        

            urun_r=requests.get(link)
            toplamurun+=1
            urun_soup=BeautifulSoup(urun_r.content,"lxml")
            marka=urun_soup.find("div",attrs={"class":"wrapper-product-brand"})
            urun_marka=marka.img.get("title")
            dictv['marka'] = urun_marka
            modelOzellik=urun_soup.find("div",attrs={"class":"product-list__product-code pull-left product-id"}).get("data-productcode")
            print(modelOzellik)
            dictv['modelAdi'] = modelOzellik
            print(urunFiyat.text)
            if urun_soup.find("div",attrs={"class":"swiper-wrapper"}) is not None:
                urun_foto = urun_soup.find("div",attrs={"class":"swiper-wrapper"}).a.get("href")
                print(urun_foto)
                dictv['urunFoto'] = urun_foto
            puan=(random.randint(30, 50))
            urunPuan=puan/10
            print (urunPuan)
            dictv['urunPuan'] = urunPuan
            ozellikler=urun_soup.find_all("tr",attrs={"data-count":"0"})
        
        

        
            for ozellik in ozellikler:
            
                
                oSystem_baslık=ozellik.find("td").text
                cpuType_baslık=ozellik.find("td").text
                ramCap_baslık=ozellik.find("td").text
                diskCap_baslık=ozellik.find("td").text
                diskType_baslık=ozellik.find("td").text
                ekran_baslık=ozellik.find("td").text
                cpuNesil_baslık=ozellik.find("td").text
                oSystemOzellik=ozellik.find("p").text
                cpuTypeOzellik=ozellik.find("p").text
                cpuNesil = ozellik.find("p").text
                ramCapOzellik=ozellik.find("p").text
                diskCapOzellik=ozellik.find("p").text
                diskTypeOzellik=ozellik.find("p").text
                ekranOzellik=ozellik.find("p").text
            
            
            
                if(oSystem_baslık=='İşletim Sistemi'):
                    print("{}:{}".format(oSystem_baslık,oSystemOzellik))
                    dictv['oSystem'] = oSystemOzellik
                elif(cpuType_baslık=='İşlemci Markası'):
                    print("{}:{}".format("İşlemci Tipi",cpuTypeOzellik))
                    dictv['cpuType'] = cpuTypeOzellik
                elif(cpuNesil_baslık=='İşlemci Nesli'):
                    print("{}:{}".format("İşlemci nesli",cpuNesil))
                    dictv['cpuNesli'] = cpuNesil
                elif(ramCap_baslık=='Ram (Sistem Belleği)'):
                    print("{}:{}".format("RAM",ramCapOzellik))
                    dictv['ramCap'] = ramCapOzellik
                elif(diskCap_baslık=='Disk Kapasitesi'):
                    print("{}:{}".format("Disk Boyutu",diskCapOzellik))
                    dictv['diskCap'] = diskCapOzellik
                elif(diskType_baslık=='Disk Türü'):
                    print("{}:{}".format(diskType_baslık,diskTypeOzellik))
                    dictv['diskType'] = diskTypeOzellik
                elif(ekran_baslık=='Ekran Boyutu'):
                    print("{}:{}".format(ekran_baslık,ekranOzellik))
                    dictv['ekran'] = ekranOzellik
            
            liste.append(dictv)
            print("."*50)  
    
    with open(r"/Users/serhat/Desktop/Proje/E-commerceV2/django_projects/Webcrapper/list_vatan.txt","w",encoding="utf8") as vatan_list:
        vatan_list.write('\n'.join(str(item) for item in liste))      
    print(liste) 
    print(toplamurun)

class ty:
    toplamurun=0
    liste = list()
    
    for i in range(1,50):

        url="https://www.trendyol.com/laptop-x-c103108?pi="+str(i)
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"lxml")
        urunler=soup.find_all("div",attrs={"class":"p-card-wrppr with-campaign-view"})
        

        for urun in urunler:
            dictt = {}
            
            linksonu=urun.a.get("href")
            linkbasi="https://www.trendyol.com/"
            link=linkbasi+linksonu
            print(link)
            dictt['urunLink'] = link
            
            
            
            urunFiyat=urun.find("div", attrs={"class":"prc-box-dscntd"})
            print(urunFiyat.text)
            dictt ['urunFiyati'] = urunFiyat.text.strip()
            urunMarka=urun.find("span", attrs={"class":"prdct-desc-cntnr-ttl"}).text
            dictt['marka'] = urunMarka
            
            
            

            urun_r=requests.get(link)
            toplamurun+=1
            urun_soup=BeautifulSoup(urun_r.content,"lxml")
            isim = urun_soup.find("h1", attrs = {"class" : "pr-new-br"})
            isim1 = isim.find("span").text
            urunAdi = urunMarka+isim1
            dictt['urunAdi'] = urunAdi
            print(urunAdi)
            if urun_soup.find("div", attrs={"class": "gallery-container"}) is not None:
                urun_foto = urun_soup.find("div", attrs={"class": "gallery-container"}).img.get("src")
                print(urun_foto)
                dictt['urunFoto'] = urun_foto
            ozellikler=urun_soup.find_all("li",attrs={"class":"detail-attr-item"})
            puan=(random.randint(30, 50))
            urunPuan=puan/10
            print (urunPuan)
            dictt['urunPuan'] = urunPuan
            

            
            for ozellik in ozellikler:
                
                model_baslık=ozellik.find("span").text
                oSystem_baslık=ozellik.find("span").text
                cpuType_baslık=ozellik.find("span").text
                ramCap_baslık=ozellik.find("span").text
                diskCap_baslık=ozellik.find("span").text
                diskType_baslık=ozellik.find("span").text
                ekran_baslık=ozellik.find("span").text
                cpuNesil_baslık=ozellik.find("span").text
                modelOzellik=ozellik.find("b").text
                oSystemOzellik=ozellik.find("b").text
                cpuTypeOzellik=ozellik.find("b").text
                ramCapOzellik=ozellik.find("b").text
                diskCapOzellik=ozellik.find("b").text
                diskTypeOzellik=ozellik.find("b").text
                ekranOzellik=ozellik.find("b").text
                cpuNesilOzellik=ozellik.find("b").text
                
                if(oSystem_baslık=='İşletim Sistemi'):
                    print("{}:{}".format(oSystem_baslık,oSystemOzellik))
                    dictt['oSystem'] = oSystemOzellik
                elif(cpuType_baslık=='İşlemci'):
                    print("{}:{}".format("İşlemci Tipi",cpuTypeOzellik))
                    dictt['cpuType'] = cpuTypeOzellik
                elif(ramCap_baslık=='Ram (Sistem Belleği)'):
                    print("{}:{}".format("RAM",ramCapOzellik))
                    dictt['ramCap'] = ramCapOzellik
                elif(diskCap_baslık=='SSD Kapasitesi'):
                    print("{}:{}".format("Disk Boyutu",diskCapOzellik))
                    dictt['diskCap'] = diskCapOzellik
                    print("{}:{}".format("Disk Türü","('SSD')"))
                    dictt['diskType'] = diskTypeOzellik
                elif(ekran_baslık=='Ekran Boyutu'):
                    print("{}:{}".format(ekran_baslık,ekranOzellik))
                    dictt['ekran'] = ekranOzellik
                elif(cpuType_baslık=='İşlemci Tipi'):
                    print("{}:{}".format(cpuType_baslık,cpuTypeOzellik))
                    dictt['cpuType'] = cpuTypeOzellik
                elif(cpuNesil_baslık=='İşlemci Nesli'):
                    print("{}:{}".format(cpuNesil_baslık,cpuNesilOzellik))
                    dictt['cpuNesli'] = cpuNesilOzellik
                
                elif model_baslık == None and modelOzellik == None:
                    if urunAdi.lower().find(n11.dictn[modelOzellik].lower()):
                        modelOzellik = n11.dictn[modelOzellik]
                        print("{}:{}".format(model_baslık,modelOzellik))
                        dictt['modelAdi'] = modelOzellik
                    elif urunAdi.lower().find(vatan.dictv[modelOzellik].lower()):
                        modelOzellik = vatan.dictv[modelOzellik]
                        print("{}:{}".format(model_baslık,modelOzellik))
                        dictt['modelAdi'] = modelOzellik
            liste.append(dictt)
                
                
            print("."*50)

    
    with open(r"/Users/serhat/Desktop/Proje/E-commerceV2/django_projects/Webcrapper/list_ty.txt","w",encoding="utf8") as ty_list:
        ty_list.write('\n'.join(str(item) for item in liste))  
    print(liste)

    
