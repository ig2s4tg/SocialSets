import requests
import json
from multi_key_dict import multi_key_dict

import common

BASE_URL = "https://canvas.instructure.com/api/v1"


# alias classes so that they can be referenced without knowing an ID
# Would have to be changed for any reuse/ will have to be changed nex semester
class_map = multi_key_dict()
class_map["handball", "intro to handball"] = 10170000001178793
class_map["os", "operating systems"] = 10170000001173763
class_map["fri", "robotics", "research"] = 10170000001173703
class_map["startup seminar", "startup", "lss"] = 1017000000117360
class_map["nt", "new testament", "intro to new testament"] = 10170000001180398


# make a call to the api
# returns json
def call(subpath):
    url = BASE_URL + subpath + "?per_page=200&access_token=" + common.auth("canvas")
    return requests.get(url).json()

courses = call("/courses")

for item in courses:
    print item

    print item["name"]
    id = item["id"]
    students = call("/courses/" + str(id) + "/users")
    if "status" not in students:
        for s in students:
            print "   " + s["name"]


def people_in(_class):
    if _class.isdigit():
        students = call("/courses/" + str(id) + "/users")
        pass
    pass
