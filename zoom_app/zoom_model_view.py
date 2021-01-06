from rest_framework import viewsets
from django.shortcuts import render
from .serializer import ZoomSerializer
from .models import ZoomModel


class ZoomView(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = ZoomSerializer
    queryset = ZoomModel.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        meeting_info = {
            'meetings': serializer.data
        }
        return render(request, 'zoom_list.html', meeting_info)

