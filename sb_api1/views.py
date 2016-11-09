from .models import booksmodel, contents
from .serializers import booksserializer , contentserializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import viewsets
# from drf_multiple_model.views import MultipleModelAPIView , MultipleModelViewSet



class books(APIView):


    def get(self, request):
        books= booksmodel.objects.filter(pk=1)
        content=contents.objects.all()
        book=booksserializer(books, many=True)
        content=contentserializer(content, many=True)
        return Response({
        'book': book.data,
        'content': content.data,
    })

    def get_content(self):
        b=contents.objects.filter(pk=1)
        return b




    def post(self):
        pass



class booksViewSet(viewsets.ModelViewSet):
	queryset = booksmodel.objects.all()
	serializer_class = booksserializer
