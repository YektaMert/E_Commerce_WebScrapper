import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client['dataTest']

def remove_dict(dictlist, remo):
    for group in dictlist:
        if group.get('_id') == remo:
            dictlist.remove(group)
            break
    return dictlist



def near_dup_osys(db):

    #near duplicate
    pipelineoSystem = [
        {
            "$group": {
                "_id": "$oSystem",
                #"docs": {"$push": "$_id"}
            }
        }
    ]

    results = remove_dict(list(db["laptoplar"].aggregate(pipelineoSystem)),None)

    for i in range(0,len(results)):
        for j in range(i+1, len(results)):
            firstid= ''.join(e for e in results[i]["_id"].lower() if e.isalnum())
            secondid= ''.join(e for e in results[j]["_id"].lower() if e.isalnum())


            if firstid == secondid:
                db["laptoplar"].update_many(
                    {"oSystem": results[j]["_id"]},
                    {"$set": {"oSystem": results[i]["_id"]}}
                )
    db["osystems"].drop()


    resulta = db["laptoplar"].aggregate(pipelineoSystem)
    for osys in resulta:
        db["osystems"].insert_one({"deger": osys["_id"]})

#windows-macos birleştirme


def near_dup_marka(db):
    pipelinemarka = [
        {
            "$group": {
                "_id": "$marka",
                #"docs": {"$push": "$_id"}
            }
        }
    ]
    results = remove_dict(list(db["laptoplar"].aggregate(pipelinemarka)),None)

    for i in range(0,len(results)):
        for j in range(i+1, len(results)):
            firstid= ''.join(e for e in results[i]["_id"].lower() if e.isalnum())
            secondid= ''.join(e for e in results[j]["_id"].lower() if e.isalnum())
            if firstid == secondid:
                db["laptoplar"].update_many(
                    {"marka": results[j]["_id"]},
                    {"$set": {"marka": results[i]["_id"]}}
                )
    db["markalar"].drop()

    resulta = db["laptoplar"].aggregate(pipelinemarka)
    for osys in resulta:
        db["markalar"].insert_one({"deger": osys["_id"]})

def near_dup_ekran(db):
    pipelineekran = [
        {
            "$group": {
                "_id": "$ekran",
                #"docs": {"$push": "$_id"}
            }
        }
    ]

    results = remove_dict(list(db["laptoplar"].aggregate(pipelineekran)),None)

    for i in range(0,len(results)):
        for j in range(i+1, len(results)):
            firstid= (''.join(e for e in results[i]["_id"].lower() if e.isalnum())).replace("inch","").replace("inç","")
            secondid= (''.join(e for e in results[j]["_id"].lower() if e.isalnum())).replace("inch","").replace("inç","")
            if firstid == secondid:
                db["laptoplar"].update_many(
                    {"ekran": results[j]["_id"]},
                    {"$set": {"ekran": results[i]["_id"]}}
                )
    db["ekranboyutlari"].drop()

    resulta = db["laptoplar"].aggregate(pipelineekran)
    for osys in resulta:
        db["ekranboyutlari"].insert_one({"deger": osys["_id"]})

def near_dup_cputype(db):
    pipelinecputype = [
        {
            "$group": {
                "_id": "$cpuType",
                #"docs": {"$push": "$_id"}
            }
        }
    ]

    results = remove_dict(list(db["laptoplar"].aggregate(pipelinecputype)),None)

    for i in range(0,len(results)):
        for j in range(i+1, len(results)):
            firstid= (''.join(e for e in results[i]["_id"].lower() if e.isalnum())).replace("intel","").replace("amdryzen","")
            secondid= (''.join(e for e in results[j]["_id"].lower() if e.isalnum())).replace("intel","").replace("amdryzen","")
            if firstid == secondid:
                db["laptoplar"].update_many(
                    {"cpuType": results[j]["_id"]},
                    {"$set": {"cpuType": results[i]["_id"]}}
                )
    db["cputypes"].drop()

    resulta = db["laptoplar"].aggregate(pipelinecputype)
    for osys in resulta:
        db["cputypes"].insert_one({"deger": osys["_id"]})

def near_dup_ramcap(db):
    pipelineramcap = [
        {
            "$group": {
                "_id": "$ramCap",
                #"docs": {"$push": "$_id"}
            }
        }
    ]

    results = remove_dict(list(db["laptoplar"].aggregate(pipelineramcap)),None)

    for i in range(0,len(results)):
        for j in range(0, len(results)):
            firstid= (''.join(e for e in results[i]["_id"].lower() if e.isalnum()))
            secondid= (''.join(e for e in results[j]["_id"].lower() if e.isalnum()))
            if firstid == secondid:
                db["laptoplar"].update_many(
                    {"ramCap": results[j]["_id"]},
                    {"$set": {"ramCap": results[i]["_id"]}}
                )
    db["ramcaps"].drop()

    resulta = db["laptoplar"].aggregate(pipelineramcap)
    for osys in resulta:
        db["ramcaps"].insert_one({"deger": osys["_id"]})

def near_dup_diskcap(db):
    pipelinediskcap = [
        {
            "$group": {
                "_id": "$diskCap",
                #"docs": {"$push": "$_id"}
            }
        }
    ]

    results = remove_dict(list(db["laptoplar"].aggregate(pipelinediskcap)),None)

    for i in range(0,len(results)):
        for j in range(0, len(results)):
            firstid= (''.join(e for e in results[i]["_id"].lower() if e.isalnum())).replace("hdd", "").replace("ssd", "").replace("optane", "")
            secondid= (''.join(e for e in results[j]["_id"].lower() if e.isalnum())).replace("hdd", "").replace("ssd", "").replace("optane", "")
            if firstid == secondid:
                db["laptoplar"].update_many(
                    {"diskCap": results[j]["_id"]},
                    {"$set": {"diskCap": results[i]["_id"]}}
                )
    db["diskcaps"].drop()

    resulta = db["laptoplar"].aggregate(pipelinediskcap)
    for osys in resulta:
        db["diskcaps"].insert_one({"deger": osys["_id"]})

def near_dup_cpugen(db):
    pipelinecpugen = [
        {
            "$group": {
                "_id": "$cpuGen",
                #"docs": {"$push": "$_id"}
            }
        }
    ]

    results = remove_dict(list(db["laptoplar"].aggregate(pipelinecpugen)),None)

    for i in range(0,len(results)):
        for j in range(i+1, len(results)):
            firstid= (''.join(e for e in results[i]["_id"].lower() if e.isalnum())).replace("intel","").replace("amdryzen","")
            secondid= (''.join(e for e in results[j]["_id"].lower() if e.isalnum())).replace("intel","").replace("amdryzen","")
            if firstid == secondid:
                db["laptoplar"].update_many(
                    {"cpuGen": results[j]["_id"]},
                    {"$set": {"cpuGen": results[i]["_id"]}}
                )
    db["cpugens"].drop()

    resulta = db["laptoplar"].aggregate(pipelinecpugen)
    for osys in resulta:
        db["cpugens"].insert_one({"deger": osys["_id"]})
    pass

def update_all_filters(db):
    print("filters updated")
    near_dup_cputype(db)
    near_dup_ekran(db)
    near_dup_marka(db)
    near_dup_osys(db)
    near_dup_ramcap(db)
    near_dup_diskcap(db)
    near_dup_cpugen(db)
