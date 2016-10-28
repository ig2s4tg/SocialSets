import json

authentication = ""

with open(".tokens") as file:
    authentication = json.loads(file.read())

def auth(platform):
    return authentication[platform]

def get_person():


class Person(object):

    def __init__(self, name=None, _friend=False):
        self.first_name = name.split()[0]
        self.last_name = name.split()[1]
        self.aliases = []

        # facebook
        self.facebook_id = None
        self.friend = _friend

        #twitter
        self.twitter_name = None

        #instagram
        self.instagram_name = None

        #canvas
        self.canvas_class_to_id_map = {}
        self.common_classes = []

        #reddit
        self.reddit_name = None
        self.reddit_link = None
