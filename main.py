# some dummy text here
import csv
from datetime import datetime


def string_to_date(date_string: str) -> datetime:
    try:
        return datetime.strptime(date_string, "%d/%m/%y")
    except ValueError:
        return datetime.strptime(date_string, "%d/%m/%Y")


with open("sales_data.csv", newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    i = 1

    for order in reader:
        order_num = order["OrderNumber"]
        order_date = order["OrderDate"]
        order_date = string_to_date(order_date)
        delivery_date = order["DeliveryDate"]
        delivery_date = string_to_date(delivery_date)

        lead_time = delivery_date-order_date
        print(f"{order_num} has {lead_time.days} leap days")

