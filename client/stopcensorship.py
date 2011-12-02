import urllib
import urllib2

def request(params=None, debug=False):
    if debug:
        h=urllib2.HTTPHandler(debuglevel=1)
        opener = urllib2.build_opener(h)
        urllib2.install_opener(opener)

    if params:
	params = urllib.urlencode(params)
    request = urllib2.Request("https://boxee.mcommons.com/profiles/join", params)
    try:
        r = urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        print "Error!: " + str(e)
        return False
    return r
