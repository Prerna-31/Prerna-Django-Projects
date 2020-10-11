from django.shortcuts import render
from .models import destination

# Create your views here.
def index(request):
    ## creating 6 objects and initializing them. This is not required in real time as data will be coming 
    ## from database.So one object will be enough.
   # dest1 = destination()
   # dest1.id = 1
   # dest1.img = 'destination_1.jpg'
   # dest1.name = 'Mumbai'
   # dest1.desc = 'The city which does not sleep'
   # dest1.price = 700
   # dest1.offer = True

   # dest2 = destination()
   # dest2.id = 2
   # dest2.img = 'destination_6.jpg'
   # dest2.name = 'Hyderabad'
   # dest2.desc = 'First Biryani , then Sherwani'
   # dest2.price = 650
   # dest2.offer = False

   # dest3 = destination()
   # dest3.id = 3
   # dest3.img = 'destination_3.jpg'
   # dest3.name = 'Bengalore'
   # dest3.desc = 'An IT hub , a silicon valley'
   # dest3.price = 780
   # dest3.offer = True


    #destList = [dest1, dest2, dest3]
    destObj = destination.objects.all()
    #return render(request,'index.html',{'dests' : destList})
    return render(request,'index.html',{'dests' : destObj})
