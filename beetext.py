import ConfigParser
import datetime
import urllib
import urllib2
import requests
import sys
import simplejson
import time

# complain on config file issues
# complain on bad login
# don't hardcode timezone to japan

CONFIG_FILE_NAME = 'config.ini'
FILENAME_SECTION = 'filename'
BEEMINDER_SECTION = 'beeminder'

BASE_URL= "https://www.beeminder.com/api/v1/"
GET_DATAPOINTS_URL = BASE_URL + "users/%s/goals/%s/datapoints.json?auth_token=%s"
POST_MANY_DATAPOINTS_URL = BASE_URL + "users/%s/goals/%s/datapoints/create_all.json?auth_token=%s"
POST_DATAPOINTS_URL = GET_DATAPOINTS_URL + "&timestamp=%s&value=%s"

def get_wordcount():
    config = ConfigParser.RawConfigParser()
    config.read(CONFIG_FILE_NAME)

    path = config.get(FILENAME_SECTION, "path")

    total_words = 0
    with open(path) as f:
        total_words = sum([len(line.split()) for line in f])

    return total_words

def post_beeminder_entry(entry):
    config = ConfigParser.RawConfigParser()
    config.read(CONFIG_FILE_NAME)

    username = config.get(BEEMINDER_SECTION, "username")
    auth_token = config.get(BEEMINDER_SECTION, "auth_token")
    goal_name = config.get(BEEMINDER_SECTION, "goal_name")

    session = requests.session()
    full_url = POST_DATAPOINTS_URL % (username, goal_name, auth_token, entry["timestamp"], entry["value"])
    r = session.post(full_url)

    print "Posted entry: %s" % r.text


if __name__ == "__main__":
    # get dates of days meditated, from insight
    total_wordcount = get_wordcount()
    print "%s words written" % total_wordcount

    # create beeminder-friendly datapoints
    new_datapoint = {'timestamp': int(time.time()), 'value':total_wordcount, "comment":"test"}

    post_beeminder_entry(new_datapoint)
