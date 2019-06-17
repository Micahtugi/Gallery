from django.http import HttpResponse,Http404
from django.shortcuts import render
from . models import Image, Location, Category
from django.views.generic import ListView

def home(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'home.html', context)

class PicListView(ListView):
    model = Image
    template_name = 'home.html'
    context_object_name = "images"

def GetLocation(request):
    data = request.GET["Location"]
    locale = Location.objects.filter(image_location=data).first()
    categ = Category.objects.filter(image_category=data).first()
    if locale:
        images = Image.objects.filter(image_location=locale)
    elif categ:
        images = Image.objects.filter(image_category=categ)
    else:
        images = {}
    return render(request, 'welcome.html', {"images": images})
        

# def welcome(request):
#     return render(request, 'welcome.html')

def search_results(request):
    
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message =f"{search_term}"
        
        return render(request, 'all-photos/search.html',{"message":message,"article": searched_articles})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
    
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/article.html", {"article":article}) 
