import urllib.request, json
import time
import webbrowser
from Coil import *
from Vehicle import *
import matplotlib.pyplot as plt

def main():
    new = 2
    #url_configure_tags_to_0m_Elevation_group = "http://10.4.57.18:8080/qpe/setTagGroup?version=2&humanReadable=true&tag=a4da22e05e8a&id=0m_Elevation"
    url_configure_tags_to_Bouvet_Ansatt = "http://10.4.57.18:8080/qpe/setTagGroup?version=2&humanReadable=true&tag=a4da22e05e8a&id=Bouvet_Ansatt"

    testCoil = Coil(123)

    testVehicle = Vehicle("Pallet Truck #1", "ASU", [0 , 2])

    while (True):
        try:
            with urllib.request.urlopen("http://10.4.57.18:8080/qpe/getTagPosition?version=2&humanReadable=true&maxAge=5000") as url:
                data = json.loads(url.read().decode())

                tags = data.get("tags", "ERROR")

                for tag in tags:
                    zones_tag = tag.get("zones", "Error")
                    id_tag = tag.get("id")
                    if zones_tag == [{'id': 'de10055f-688d-4f7e-b4c8-7c4fff20d8b2', 'name': 'Gang'}]:
                        print("Tag " + tag["name"] + " er nå i Gang")
                        #webbrowser.open(url_configure_tags_to_0m_Elevation_group,new=new);
                        webbrowser.open("http://10.4.57.18:8080/qpe/setTagGroup?version=2&humanReadable=true&tag="+ id_tag +"&id=0m_Elevation", new=new)
                    else:
                        print("Tag " + tag["name"] + " er IKKE i Gang")
                        webbrowser.open(
                            "http://10.4.57.18:8080/qpe/setTagGroup?version=2&humanReadable=true&tag=" + id_tag + "&id=Bouvet_Ansatt", new=new)

        except Exception:
            print("Tag Error")

        try:
            with urllib.request.urlopen("http://10.4.57.18:8080/qpe/getTagPosition?version=2&humanReadable=true&maxAge=5000") as url:
                data = json.loads(url.read().decode())

                tags = data.get("tags", "ERROR Yalla")

                tag1 = tags[0]
                tag2= tags[1]

                #print(tag1.get("position"))
                #print(tag2.get("position"))

                x = tag1.get("position")
                y = tag2.get("position")
                i = 0
                z=[0, 0, 0]
                for element in x:
                    element = element-y[i]
                    z[i] = element
                    i = i+1

                direction = [z[0], z[1]]
                print(direction)

                testVehicle.set_direction_vector(direction)
                plt.plot([0,1],direction)
                plt.show()


        except Exception:
            print("Yalla")

        time.sleep(3)




main()