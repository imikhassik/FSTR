from rest_framework import mixins
from rest_framework import generics

from .models import Pereval
from .serializers import PerevalSerializer


class SubmitData(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
