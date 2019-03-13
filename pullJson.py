import urllib.request, json
import time

while (True):

    with urllib.request.urlopen("http://10.4.57.18:8080/qpe/getTagPosition?version=2&humanReadable=true&maxAge=5000") as url:
        data = json.loads(url.read().decode())

        tags = data.get("tags", "ERROR")

        tag_Nr_1= tags[0]
        #tag_Nr_2 = tags[1]

        #tag_Nr_1.get("name", "Error")
        #tag_Nr_1.get("smoothedPosition", "Error")
        #tag_Nr_1.get("positionTS", "Error")
        #tag_Nr_1.get("covarianceMatrix", "Error")

        print(tag_Nr_1["name"])
        print(tag_Nr_1["smoothedPosition"])
        print(tag_Nr_1["positionTS"])
        print(tag_Nr_1["covarianceMatrix"])
        print(tag_Nr_1["zones"])

        #print(tag_Nr_2["name"])
        #print(tag_Nr_2["smoothedPosition"])
        #print(tag_Nr_2["positionTS"])
        #print(tag_Nr_2["covarianceMatrix"])
        #print(tag_Nr_2["zones"])

        time.sleep(1)

