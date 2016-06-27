# GEOStatIL

[![PyPi](https://img.shields.io/pypi/v/geostatil.svg)](https://pypi.python.org/pypi/geostatil)

This library allows you to get detailed statistical data on any point in Israel.

It uses the 2008 census (done by the LAMAS, Israel's statistical bureau). The census holds data for "statistical areas", which are is a fine grained partition of the land into areas with similar properties. Each statistical area describes a few 1000s of people.

It accepts both latitude/longitude pairs as well as textual addresses (which are geocoded using an online service).

## Usage

```python
>>> from geostatil import GEOStatIL
>>> gsi = GEOStatIL()
>>> gsi(address=u'דיזנגוף 99, תל אביב')

{'אוכלוסייה – סך הכל (אלפים)': '1.9',
 'אזור טבעי': 'אזור תל אביב',
 'אזור סטטיסטי': '343',
 'אחוז  בני 15 ומעלה שעבדו בשנת 2008 בענף "מסחר סיטוני וקמעוני, תיקון כלי רכב מנועיים, אופנועים, קטנועים וטובין לשימוש אישי וביתי"': '11.0',
 'אחוז  גברים בני 15 ומעלה בעלי תעודות אחרות': '4.3',
 'אחוז בני  17-0 ': '5.0',
 'אחוז בני  64-18  ': '85.4',
 'אחוז בני  65+ ': '9.5',
 'אחוז בני 15 ומעלה בכוח העבודה האזרחי השנתי': '86.2',
 'אחוז בני 15 ומעלה בעלי תואר אקדמי ראשון': '35.9',

 ### ...Omitting another ~250 rows...

 'סמל מחוז': '5',
 'סמל מטרופולין': '110',
 'סמל מעמד מוניציפלי': '0',
 'סמל נפה': '51',
 'סמל צורת יישוב': '130',
 'צורת יישוב': 'יישוב יהודי 499,999-200,000 תושבים',
 'צפיפות אוכלוסייה (לקמ"ר)': '',
 'צפיפות דיור ממוצעת למשק בית': '0.8',
 'רובע': '3',
 'שטח היישוב (קמ"ר)': '',
 'שנת יסוד': '1909',
 'תת-רובע': '34'}

 # שAlso pssible to use direct coordinates:
>>> gsi(lat=32.526095,lon=34.9024513)
 # ...
```

## Installation
```
$ pip install geostatil
```
