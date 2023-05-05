import os
import csv
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from store.models import *
from django.contrib.auth.models import User
from faker import Faker

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        User.objects.all().delete()
        Product.objects.all().delete()
        # Customer.objects.all().delete()
        Order.objects.all().delete()
        print("table dropped successfully")

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/project.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            number = 100000
            num = 1
            for row in reader:
                if len(row) < 12:
                    next(reader)
                else:
                    print(row)
                    product = Product.objects.create(
                        product_id = row[1],
                        product_url = row[2],
                        product_name = row[3],
                        product_category = row[4],
                        price = float(row[5]),
                        image = row[6],
                        description = row[7],
                        product_specification = row[8],
                    )
                    product.save()

                    fake = Faker()

                    username=fake.name()+ str(num)
                    num = num + 1
                    email=fake.free_email()

                    user =User.objects.create_user(username=username, email=email, password=password)
                    user.is_active = True
                    user.save()

                    Customer = Customer.objects.create(
                        user=user,
                    )
                    customer.save()
                    for _ in range(1,4):
                        order = Order.objects.create(
                            transaction_id=str(number),
                            customer=customer,
                        )
                        number += 1
                        order.save()

    print("data parsed successfully")
