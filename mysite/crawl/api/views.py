from rest_framework import generics
from ..models import News
from .serializers import NewsSerializer
from rest_framework.response import Response
from django.db.models import Q


class CRUDNews(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        # get keyword from request for search
        keyword = self.request.GET.get("keyword")
        if keyword:
            # if keyword -> search item with title and summary
            # else -> list all item
            self.queryset = self.queryset.filter(Q(title__icontains=keyword) | Q(summary__icontains=keyword))

        return self.queryset.order_by('-id')

    def post(self, request):
        # create Item using Serializer
        serializer = NewsSerializer(data=request.data)
        if not serializer.is_valid():
            # if some field invalid -> response Fail
            return Response({
                "message": "Create Fail!",
                "data": serializer.errors
            })
        # save Item
        serializer.save()
        return Response({
            "message": "Create Success!",
            "data": serializer.data
        })

    def put(self, request):
        data = request.data
        id_news = data.get("id")
        if not id_news:
            return Response({"message": "field 'id' not found!"})

        news = News.objects.filter(pk=id_news).first()
        if not news:
            return Response({"message": "News with ID={} doesn’t exist!".format(id_news)})

        serializer = NewsSerializer(news, data=data)
        if not serializer.is_valid():
            return Response({
                "message": "Update Fail!",
                "data": serializer.errors
            })
        serializer.save()
        return Response({
            "message": "Update Success!",
            "data": serializer.data
        })

    def delete(self, request):
        id_news = request.data.get("id")
        if not id_news:
            return Response({"message": "field 'id' not found!"})

        news = News.objects.filter(pk=id_news).first()
        if not news:
            return Response({"message": "News with ID={} doesn’t exist!".format(id_news)})

        news.delete()
        return Response({
            "message": "Delete Success!",
        })
