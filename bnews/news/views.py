from django.http import JsonResponse
from django.shortcuts import render, redirect


from .models import News, Catigories
from django.views.generic.base import View
import datetime

from .forms import ReviewForm



class NewssAllView(View):
    def get(self, request):
        all_news = News.objects.exclude(url_cat="businnes").order_by('-published')
        b_news = News.objects.filter(url_cat="businnes")
        footer_news = News.objects.order_by('?')
        date_now = datetime.datetime.now()
        catigories = Catigories.objects.all()
        return render(request, "news/news_list.html", {'catigories': catigories, 'news_list': all_news, 'businnes': b_news, 'footer_news': footer_news, 'date_now': date_now})



def by_rubric(request, slug):
    bbs = News.objects.filter(url_cat=slug)
    rubrics = Catigories.objects.all()
    current_rubric = Catigories.objects.get(url_cat=slug)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'news/catigory.html', context)



def get_detail(request, slug):
        single_news = News.objects.get(url=slug)
        footer_news = News.objects.order_by('?')
        b_news = News.objects.filter(url_cat="businnes")
        form = ReviewForm()
        catigories = Catigories.objects.all()
        context = {'form': form, 'single_news': single_news, 'catigories': catigories, 'footer_news': footer_news, 'businnes': b_news, 'news_id': single_news.id, 'news': single_news}
        return render(request, 'news/single_news.html', context)




class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        news = News.objects.get(id=pk)

        if form.is_valid():
            review = form.save(commit=False)
            if request.POST.get("parent", None):
                review.parent_id = int(request.POST.get("parent"))
            review.news = news
            review.save()
            return redirect(news.get_single())
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400, safe=False, content_type='application/json')







