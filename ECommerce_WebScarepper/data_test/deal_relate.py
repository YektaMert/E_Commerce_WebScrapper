import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['dataTest']

collaptop = db["laptoplar"]
coldeal = db["deals"]

def remove_dict(dictlist, remo):
    for group in dictlist:
        if group.get('_id') == remo:
            dictlist.remove(group)
            break
    return dictlist

pipelineModelAdi = [
    {
        "$group": {
            "_id": "$modelAdi",
            "count": {"$sum":  1},
            #"docs": {"$push": "$_id"}
        }
    },
    {
        "$match": {
            "count": {"$gt" : 1}
        }
    }
]

pipelineoSystem = [
    {
        "$group": {
            "_id": "$oSystem",
            "docs": {"$push": "$_id"}
        }
    }
]

pipeline = [
    {
        "$group": {
            "_id": "$oSystem",
            #"docs": {"$push": "$_id"}
        }
    }
]

results = remove_dict(list(collaptop.aggregate(pipelineoSystem)),None)

for i in range(0,len(results)):
    for j in range(i+1, len(results)):
        firstid= ''.join(e for e in results[i]["_id"].lower() if e.isalnum())
        secondid= ''.join(e for e in results[j]["_id"].lower() if e.isalnum())
        if firstid == secondid:
            print(results[i]["_id"], results[j]["_id"])
            collaptop.update_many(
                {"oSystem": results[j]["_id"]},
                {"$set": {"oSystem": results[i]["_id"]}}
            )


pipelineoSystem = [
		{
			"$group": {
				"_id": "$oSystem",
				#"docs": {"$push": "$_id"}
			}
		}
	]
db["osystems"].drop()


resulta = db["laptoplar"].aggregate(pipelineoSystem)
for osys in resulta:
	db["osystems"].insert_one({"deger": osys["_id"]})
