sourcen11 = "/Users/serhat/Desktop/Proje/E-commerceV2/django_projects/Webcrapper/list_n11.txt"
destn11 = "/Users/serhat/Desktop/Proje/E-commerceV2/django_projects/Webcrapper/updated_list_n11.txt"

sourcety = "/Users/serhat/Desktop/Proje/E-commerceV2/django_projects/Webcrapper/list_ty.txt"
destty = "/Users/serhat/Desktop/Proje/E-commerceV2/django_projects/Webcrapper/updated_list_ty.txt"

sourcevatan = "/Users/serhat/Desktop/Proje/E-commerceV2/django_projects/Webcrapper/list_vatan.txt"
destvatan = "/Users/serhat/Desktop/Proje/E-commerceV2/django_projects/Webcrapper/updated_list_vatan.txt"

def update(source, dest):
    sourcefile = open(source, "r")
    destfile = open(dest, "w")

    for line in sourcefile.readlines():
        destfile.write(line+",")

update(sourcen11, destn11)
update(sourcety, destty)
update(sourcevatan, destvatan)

def get_list_n11():
    n11_list=[]
    sourcefile = open("/Users/serhat/Desktop/Proje/E-commerceV2/django_projects/Webcrapper/updated_list_n11.txt", "r")
    for line in sourcefile.readlines():
        n11_list.append(line.replace("\n", ""))
    return n11_list

def get_list_n11v2():
    n11_list=[]
    sourcefile = open("/Users/serhat/Desktop/Proje/E-commerceV2/django_projects/Webcrapper/updated_list_n11.txt", "r")
    for line in sourcefile.readlines():
        n11_list.append(line.rstrip())
    return n11_list

n11_list = get_list_n11v2()
print(n11_list)
        
