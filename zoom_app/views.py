from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .zoom import ZoomReq
from .zoom_db import ZoomDataBase

zoom_db = ZoomDataBase()


class ZoomView(View):
    """ View for zoom api"""
    @staticmethod
    def get(request):
        zoom_obj = ZoomReq
        meeting_info = zoom_obj.get_meetings(zoom_obj)
        zoom_db.add_rows(meeting_info.get('meetings'))
        return render(request, 'zoom_list.html', meeting_info)

    @staticmethod
    def post(request):
        meeting_id = request.POST.get('meeting_id')
        zoom_obj = ZoomReq
        code = zoom_obj.status_meeting(zoom_obj, meeting_id)
        if code == 204:
            zoom_table = ZoomDataBase
            zoom_table.delete_row(meeting_id)
            return HttpResponse(code)
        return HttpResponse("error {}".format(code))


class ZoomDataBaseView(View):
    """ View for showing the database"""
    @staticmethod
    def get(request):
        zoom_table = ZoomDataBase
        meeting_info = {
            'meetings': zoom_table.get_all()
        }
        return render(request, 'zoom_list.html', meeting_info)
