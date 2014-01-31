from rest_framework.views import APIView
from rest_framework.response import Response
from los.lo import LO, DATA
from los.serializers import LOSerializer, PaginatedLOSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class LOList(APIView):
    """
    List all los
    """

    def get(self, request, format=None):
        URL = "http://%s%s" % (request.META['HTTP_HOST'], request.path)
        for el in DATA:
            el.url = URL + str(DATA.index(el))
            el.description = el.title

        paginator = Paginator(DATA, 10)

        page = request.QUERY_PARAMS.get('page')
        try:
            chuncks = paginator.page(page)
        except PageNotAnInteger:
            chuncks = paginator.page(1)
        except EmptyPage:
            chuncks = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = PaginatedLOSerializer(chuncks, context=serializer_context)

        return Response(serializer.data)


class LODetail(APIView):
    """
    Retrieve an lo instance
    """

    def get(self, request, pk, format=None):
        lo = filter(lambda x: x.pk == int(pk), DATA)
        serializer = LOSerializer(lo, many=True)
        return Response(serializer.data)
