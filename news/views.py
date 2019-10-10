from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Location

# Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')
    
def all_images(request):
    date = dt.date.today()
    images = Image.displaying_images()
    return render(request, 'all-news/today-news.html', {"date": date,"images":images})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

# View Function to present news from past days
# def past_days_news(request, past_date):
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(news_today)

#     news = Article.days_news(date)
#     return render(request, 'all-news/past-news.html',{"date": date,"news":news})    

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

def image(request,images_id):
    try:
        image = Image.objects.get(id = images_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"image":image})