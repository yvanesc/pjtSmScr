import urllib2
import json
#f = urllib2.urlopen('http://api.wunderground.com/api/a71894d18588a38f/geolookup/q/46.521 ,-6.674.json')
f = urllib2.urlopen('http://api.wunderground.com/api/a71894d18588a38f/geolookup/q/ch/Lausanne.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_t = parsed_json['current_observation']['temp_t']
print "Current temperature in %s is: %s" % (location, temp_t)
f.close()
