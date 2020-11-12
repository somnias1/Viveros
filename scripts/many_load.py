import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, States, Region, ISO, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    ISO.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        ds=row[0]
        g=row[1]
        h=row[2]
        e=row[3]
        i=row[4]
        j=row[5]
        f=row[6]
        a, created = Category.objects.get_or_create(name=row[7])
        a.save()
        b, created = States.objects.get_or_create(name=row[8])
        b.save()
        c, created = Region.objects.get_or_create(name=row[9])
        c.save()
        d, created = ISO.objects.get_or_create(name=row[10])
        d.save()
        #for year
        try:
            e = int(row[3])
        except:
            e = None
        #for longitude
        try:
            i = float(row[4])
        except:
            i = None
        #for latitude
        try:
            j = float(row[5])
        except:
            j = None
        #for area_hectares
        try:
            f = float(row[6])
        except:
            f = None
        #name,description,justification,year,longitude,latitude,area_hectares,category,states,region,iso
        site = Site(name = ds ,description=g ,justification=h,year=e, longitude=i, latitude = j,area_hectares=f ,category=a, states=b, region=c, iso=d)
        site.save()