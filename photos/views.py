from django.http import HttpResponse,Http404
from django.shortcuts import render
from . models import Image, Location, Category
from django.views.generic import ListView

def home(request):
    
    images= Image.objects.all()

    return render(request, 'home.html', {"images": images})

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
    
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_image = Image.search_by_category(search_term)
        message =f"{search_term}"
        
        return render(request, 'all-photos/search.html',{"message":message,"all_images": searched_image})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
    
def get_category(request,category):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    category_results = Image.objects.filter(image_category__cat_name = category)
    return render(request,'all-photos/search.html',{'all_images':category_result,'category_results':category_results,'location_results':location_results} )

def get_location(request,location):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    location_results = Image.objects.filter(image_location__location_name= location)
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})