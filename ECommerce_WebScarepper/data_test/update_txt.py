source = "/Users/serhat/Desktop/Proje/E-commerceV2/data_test/list_ty.txt"
dest = "/Users/serhat/Desktop/Proje/E-commerceV2/data_test/updated_list_ty.txt"

sourcefile = open(source, "r")
destfile = open(dest, "w")

for line in sourcefile.readlines():
    destfile.write(line+",")
    pass