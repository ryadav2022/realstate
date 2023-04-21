from django.shortcuts import render
from property.models import Neibhorhood,PriceRange,PropertyType

# Create your views here.
def home(request):
    neigs = Neibhorhood.objects.all() 
    price_ranges = PriceRange.objects.all() 
    properties_type = PropertyType.objects.all() 
    context = {
        'neighbours': neigs,
        'price_ranges': price_ranges, 
        'properties_types': price_ranges
    }

    return render(request,'index.html',context)