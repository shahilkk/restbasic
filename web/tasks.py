from celery import shared_task
from .models import *




@shared_task(blind=True)
def change_status(self):
    brand=Brand.objects.all()
    for i in brand:
        print(i.status)
        if i.status=="approved":
            Feed.objects.filter(brand=i.id).update(status="approved")
            print('worked')
    return "Done"        