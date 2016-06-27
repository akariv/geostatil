import fiona
import fiona.crs
import csv
import glob

stat_data = {}
header_conversion = {}
for mifkad_file in glob.glob('mifkad2008/גיליון*.csv'):
    with open(mifkad_file) as f:
        reader = csv.reader(f)
        for _ in range(3):
            next(reader)
        heb_headers = next(reader)
        eng_headers = next(reader)
        header_conversion.update(dict(zip(eng_headers, heb_headers)))
        for row in reader:
            rec = dict(zip(eng_headers, row))
            lc = rec['LocalityCode']
            sa = rec.get('StatAreaCmb','1')
            if sa == '': sa = '*'
            sas = sa.split('+')
            if lc == '':
                continue
            for sa in sas:
                stat_area = '/'.join([lc, sa])
                try:
                    int(lc)
                    if sa != '*': int(sa)
                except:
                    continue
                stat_data.setdefault(stat_area,{}).update(rec)
json.dump((stat_data, header_conversion),
          open('stat-data.json','w'),indent=2,sort_keys=True)

geometries = {}
with fiona.open("lamas-geo/stat_2008_NEW_04Nov_1335.shp") as collection:
    for r in collection:
        if r['properties']['STAT08'] != 0:
            key = '/'.join([
                        str(r['properties']['SEMEL_YISH']),
                        str(r['properties']['STAT08'])
                  ])
            geometries[key] = r['geometry']
    json.dump(geometries, open('geometries.json','w'),indent=2,sort_keys=True)
    json.dump(fiona.crs.to_string(collection.crs), open('crs.json','w'))
