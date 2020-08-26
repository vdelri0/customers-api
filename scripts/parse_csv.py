import csv
from customers.models import Customer
from pathlib import Path
import geocoder

api_key = 'AIzaSyDHVCOSbx-b4iAfVwgOZdl4WHideVzZ93Q'


def run():
    ipath = Path(__file__).parent / '../customers.csv'
    opath = Path(__file__).parent / '../customers_output.csv'
    with ipath.open(mode='r') as i_obj, opath.open(mode='w') as o_obj:
        input_reader = csv.reader(i_obj)
        output_writer = csv.writer(o_obj)

        print('The csv file filling started.')
        for idx, row in enumerate(input_reader):
            if idx == 0:
                row.append('latitude')
                row.append('longitude')
            else:
                g = geocoder.google(row[6], key=api_key)
                lat, lng = g.latlng
                row.append(lat)
                row.append(lng)

            output_writer.writerow(row)
        print('The csv file filling ended.')

    with opath.open(mode='r') as o_obj:
        output_reader = csv.reader(o_obj)
        next(output_reader)  # Jumps over the first line

        print('The DB filling started.')
        Customer.objects.all().delete()
        Customer.objects.bulk_create([Customer(**{
                                                  'id': row[0],
                                                  'first_name': row[1],
                                                  'last_name': row[2],
                                                  'email': row[3],
                                                  'gender': row[4],
                                                  'company': row[5],
                                                  'city': row[6],
                                                  'title': row[7],
                                                  'latitude': row[8],
                                                  'longitude': row[9]})
                                      for row in output_reader])
        print('The DB filling ended.')

    print('csv process done!')
