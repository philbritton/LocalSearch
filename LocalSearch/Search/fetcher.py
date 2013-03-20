import urllib2
import json
def getresult(query):
    #query="ATM"
    #print "Enter location to search"
    #query=raw_input()
    url=urllib2.urlopen("https://api.foursquare.com/v2/venues/search?ll=10.941192,77.01416&query="+query+"&oauth_token=PNNFCO0IYL5R2LIN3CU44RNROKUBNSI44XRHSXLOGKUJVXFH&v=20130312")
    result = json.load(url)
    return result