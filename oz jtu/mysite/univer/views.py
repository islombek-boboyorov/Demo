from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
import datetime
from . import servise


def index(request):
    populars = servise.get_news()
    fresh_news = News.objects.all().order_by("-created_at")[:5]
    menus = servise.get_menu()
    basics = servise.get_basic()
    categories = servise.get_category()
    ctx = {
        "menus": menus,
        "basics": basics,
        "categories": categories,
        "populars": populars,
        "fresh_news": fresh_news,
    }
    return render(request, 'fronted/news/index.html', ctx)


def news(request, news_id=None):
    new = servise.get_news_by_id(news_id)
    print(new)
    actuals = News.objects.all().filter(
        created_at__range=[timezone.now() - datetime.timedelta(days=1), timezone.now()]
    )
    populars = News.objects.all().order_by("-views")[:4]
    fresh_news = News.objects.all().order_by("-created_at")[:4]
    categories = servise.get_category()
    menus = servise.get_menu()
    basics = servise.get_basic()
    ctx = {
        "actuals": actuals,
        "fresh_news": fresh_news,
        "populars": populars,
        "new": new,
        "categories": categories,
        "menus": menus,
        "basics": basics,

    }
    return render(request, 'fronted/news/category.html', ctx)


def basic(request, news_id=None):
    new = servise.get_basic_by_id(news_id)
    print(new)
    actuals = News.objects.all().filter(
        created_at__range=[timezone.now() - datetime.timedelta(days=1), timezone.now()]
    )
    populars = News.objects.all().order_by("-views")[:4]
    fresh_news = News.objects.all().order_by("-created_at")[:4]
    categories = Category.objects.all()
    menus = servise.get_menu()
    basics = servise.get_basic()
    ctx = {
        "actuals": actuals,
        "fresh_news": fresh_news,
        "populars": populars,
        "new": new,
        "categories": categories,
        "menus": menus,
        "basics": basics,

    }
    return render(request, 'fronted/news/category.html', ctx)


def view(request, pk=None):
    categories = servise.get_category()
    new = servise.get_news_by_id_one(pk)
    sums = News.objects.all().order_by("-views")
    menus = servise.get_menu()
    basics = servise.get_basic()
    ctx = {
        "new": new,
        "sums": sums,
        "categories": categories,
        "menus": menus,
        "basics": basics,
    }
    return render(request, 'fronted/news/view.html', ctx)


def search(request):
    new = []
    fresh_news = News.objects.all().order_by("-created_at")
    menus = servise.get_menu()
    basics = servise.get_basic()
    categories = servise.get_category()
    if request.GET and request.GET.get("search"):
        new = News.objects.filter(title__icontains=request.GET.get("search"))
    ctx = {
        "new": new,
        "fresh_news": fresh_news,
        "search_count": len(new),
        "search_text": request.GET.get("search"),
        "categories": categories,
        "menus": menus,
        "basics": basics,
    }
    return render(request, 'fronted/news/search.html', ctx)
