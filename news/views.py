from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
import pyperclip
from .models import Image,Location,category

# Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')
    
def all_images(request):
    date = dt.date.today()
    images = Image.displaying_images()
    location = Location.objects.all()
    categories = category.objects.all()
    return render(request, 'all-news/today-news.html', {"date": date,"images":images,"location":location,"category":category})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day    

def search_results(request):

    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"


        return render(request, 'all-news/search.html',{"message":message,"searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

def image(request,images_id):
    try:
        image = Image.objects.get(id = images_id)
        print('image.name')
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"image":image})

# def copy_url(request,image_url):
#     image_url = Image.objects.get(image=image_url)
#     print('image_url.url')
#     pyperclip.copy(image_url.url)
#     return render(request, 'all-news/today-news.html', {"image_url": image_url})