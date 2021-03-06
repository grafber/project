from django.shortcuts import render

from .models import Article


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)


def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__month=month)
    context = {'year': year, 'month': month, 'article_list': a_list}
    return render(request, 'news/month_archive.html', context)


def article_detail(request, year, month, pk):
    a_list = Article.objects.filter(id=pk)
    context = {'year': year, 'month': month, 'article_list': a_list}
    return render(request, 'news/detail_archive.html', context)

def kolor_detail(request, year, month, pk, color):
    a_list = Article.objects.filter(pub_dare_color=color)
    context = {'year': year, 'month': month, 'color':color 'article_list': a_list}
    return render(request, 'news/detail_archive.html', context)