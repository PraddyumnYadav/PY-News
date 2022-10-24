from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    r = requests.get(
        'http://api.mediastack.com/v1/news?access_key=e77a1cc74ab7b96f04376b4b4afc6801&countries=us,gb,de,in&sources=en,cnn&categories=business,science,technology,entertainment')


    res = r.json()
    data = res['data']

    title = []
    description = []
    image = []
    url = []

    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])

    news = zip(title, description, image, url)

    return render(request, 'NewsApp/index.html', {'news': news})
