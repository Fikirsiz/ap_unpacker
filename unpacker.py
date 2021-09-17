import csv
import sys
from zipfile import ZipFile
import json
from collections import Counter


with ZipFile(sys.argv[1]) as f:
    access_points = json.loads(f.read("accessPoints.json"))
    vendor_model = []
    for ap in access_points["accessPoints"]:
        vendor_model += [(ap["vendor"], ap["model"])]

with open("access_points.csv", "w") as csv_f:
    csv_result = csv.writer(csv_f, dialect="excel")
    for ap, count in Counter(vendor_model).items():
        csv_result.writerow([ap[0], ap[1], count])
