import csv
import os
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User
from store.models import *
from faker import Faker


class Command(BaseCommand):
    help = 'Import data from csv file'

    def handle(self, *args, **options):

        # drop all data from tables
        User.objects.all().delete()
        Product.objects.all().delete()
        Customer.objects.all().delete()
        Order.objects.all().delete()
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/project.csv', newline='') as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)  # skip the header line
            number=100000
            num=1
            for row in reader:
                if len(row) < 12:
                    next(reader)
                elif row[1]=='' or row[2]=='' or row[3]=='' or row[4]=='' or row[5]=='' or row[6]=='' or row[7]=='' or row[8]=='' or row[9]=='' or row[10]=='' or row[11]=='': 
                    next(reader)
                else:
                    print(row)
                    product = Product.objects.create(
                        product_id = row[0],
                        product_url = row[1],
                        product_name = row[2],
                        product_category = row[3],
                        price = float(row[4]),
                        image = row[5],
                        description = row[6],
                        product_specification = row[7],
                    )
                    product.save()

                    fake = Faker()

                    username=fake.name()+str(num)
                    num=num+1
                    email=fake.free_email()

                    user = User.objects.create_user(username=username,
                                                    email=email,
                                                    password='password')
                    user.is_active = True
                    user.save()

                    customer = Customer.objects.create(
                        user=user,
                    )
                    customer.save()
                    for _ in range(1,4):
                        order = Order.objects.create(
                            transaction_id=str(number),
                            customer=customer,
                        )
                        number+=1
                        order.save()