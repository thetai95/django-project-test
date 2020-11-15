# import from Django
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.views.generic.list import ListView

# import from this project
from .models import News
from .api.serializers import NewsSerializer


class ListNews(View):
    """
    view list items and search items
    """

    def get(self, request):
        news = News.objects.all()

        # get param keyword for Search
        keyword = request.GET.get("keyword")

        # send context dictionary to list view
        context = {}
        if keyword:
            news = news.filter(Q(title__icontains=keyword) |
                               Q(summary__icontains=keyword))
            context["keyword"] = keyword

        news = news.order_by('-id')
        context["news"] = news
        return render(request, "crawl/index.html", context)


class AddNews(View):
    """
    View add item
    """

    def get(self, request):
        return render(request, "crawl/add_item.html")

    def post(self, request):
        # get info from request POST
        data = {
            "title": request.POST.get("title"),
            "summary": request.POST.get("summary"),
            "link": request.POST.get("link"),
            "comment": request.POST.get("comment"),
        }

        # create Item using Serializer
        serializer = NewsSerializer(data=data)

        if not serializer.is_valid():
            # if fields invalid -> send error to view
            errors = {}
            for error, v in serializer.errors.items():
                errors[error] = v[0]
            return render(
                request,
                "crawl/add_item.html",
                context={"errors": errors}
            )

        # save Item
        serializer.save()
        return redirect('crawl:index')


class UpdateNews(View):
    """
    View update item
    """

    def get(self, request, pk):
        item = News.objects.filter(pk=pk).first()
        return render(request, "crawl/update_item.html", context={"item": item})

    def post(self, request, pk):
        item = News.objects.filter(pk=pk).first()
        data = {
            "title": request.POST.get("title"),
            "summary": request.POST.get("summary"),
            "link": request.POST.get("link"),
            "comment": request.POST.get("comment"),
        }

        serializer = NewsSerializer(item, data=data)

        if not serializer.is_valid():
            errors = {}
            for error, v in serializer.errors.items():
                errors[error] = v[0]
            return render(request, "crawl/update_item.html", context={
                "errors": errors,
                "item": item
            })

        serializer.save()
        return redirect('crawl:index')


class DestroyNews(View):
    """
    View confirm delete item
    """

    def get(self, request, pk):
        item = News.objects.filter(pk=pk).first()
        return render(request, "crawl/delete_item.html", context={"item": item})

    def post(self, request, pk):
        News.objects.filter(pk=pk).delete()
        return redirect('crawl:index')
