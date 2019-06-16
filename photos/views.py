from django.http import HttpResponse
from django.shortcuts import render
import datetime as dt

def welcome(request):
    return render(request, 'welcome.html')

def search_results(request):
    
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message =f"{search_term}"
        
        return render(request, 'all-news/search.html',{"message":message,"article": searched_article})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
