#encoding: utf8
import os
import bisect
import json
import shapely.geometry
import pyproj
import geocoder

class GEOStatIL(object):

    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__),'data')
        self.stat_data = {}
        self.header_conversion = {}
        self.stat_data, self.header_conversion = \
            json.load(open(os.path.join(self.path,'stat-data.json')))
        geometries = json.load(open(os.path.join(self.path,'geometries.json')))
        crs = json.load(open(os.path.join(self.path,'crs.json')))
        self.proj = pyproj.Proj(crs)
        self.recs = [{
            'shp':shapely.geometry.asShape(geometry),
            'area': area_id,
        } for area_id, geometry in geometries.items()]

        for r in self.recs:
            bounds = r['shp'].bounds
            r['key'] = bounds[2] + bounds[3]
            r['bounds'] = bounds
        self.recs.sort(key=lambda r:r['key'])
        self.rec_keys = [r['key'] for r in self.recs]

    def find_stat_area(self, lat, lon):
        lon, lat = self.proj(lon,lat)
        i = bisect.bisect_left(self.rec_keys, lat+lon)
        for rec in self.recs[i:]:
            point = shapely.geometry.Point(lon, lat) # longitude, latitude
            bounds = rec['bounds']
            bounding_box = shapely.geometry.box(*bounds)
            if bounding_box.contains(point):
                if rec['shp'].contains(point):
                    return rec['area'].split('/')
            if bounds[0] + bounds[1] > lat+lon:
                break

    def get_stat_area_data(self, yeshuv, area_id):
        ret = self.stat_data.get('/'.join([yeshuv, area_id]))
        if ret is None:
            ret = self.stat_data.get('/'.join([yeshuv, '*']),{})
        ret = dict((self.header_conversion[k],v)
                    for k,v in ret.items())
        return ret

    def __call__(self, address=None, lat=None, lon=None):
        if address is not None:
            lat, lon = geocoder.google(address).latlng
        return self.get_stat_area_data(*self.find_stat_area(lat,lon))


if __name__ == '__main__':
    gsi = GEOStatIL()
    import pprint
    print(gsi(lat=32.190343, lon=34.864845) is None)
    print(gsi(lat=32.190343, lon=34.864845) is None)
    print(gsi(lat=32.190343, lon=34.864845) is None)
    print(gsi(lat=32.190343, lon=34.864845))
    # for x in gsi(address=u'סמטת החומה 2, רעננה').items():
        # print('{0}: {1}'.format(*x))
