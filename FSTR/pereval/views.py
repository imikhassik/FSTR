from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from .models import PerevalAdded
from .serializers import PerevalAddedSerializer


# class SubmitData(APIView):
#     serializer_class = PerevalAddedSerializer
#
#     def get_serializer(self):
#         return self.serializer_class()
#
#     def get(self, request):
#         perevals = PerevalAdded.objects.all()
#         serializer = PerevalAddedSerializer(perevals, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PerevalAddedSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubmitData(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
