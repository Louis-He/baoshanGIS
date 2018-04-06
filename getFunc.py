import web
import json
import time
import os
import urllib2

urls = (
    '/index', 'index',
    '/getStationInfo', 'getStationInfo'
)

class index:
    def GET(self):
        return (open(r'map.html', 'r').read())

class getStationInfo:
    def GET(self):
        try:
            data = urllib2.urlopen('http://www.bsqx.com/GetTemperInfo/').read()
            return data
        except:
            return '[]'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
