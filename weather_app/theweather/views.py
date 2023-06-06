import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    # city = 'Dubai'
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=812795cc248e8086f19c3115ff734571'
    #url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=812795cc248e8086f19c3115ff734571'

    if request.method =='POST':
        form=CityForm(request.POST)
        form.save()
    form=CityForm()


    cities = City.objects.all()

    theweather_data=[]

    for city in cities:

        data= requests.get(url.format(city)).json()

        city_theweather={
                'city':city.name,
                 'temperature': data['main']['temp'],
                 #'humidity':data['main']['humidity'],
                'description':data['weather'][0]['description'],
                'icon':data['weather'][0]['icon'],
        }

        theweather_data.append(city_theweather)
        # print(theweather_data)


    context={'theweather_data':theweather_data,'form':form}
    return render(request,'theweather/theweather.html',context)

