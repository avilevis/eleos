from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .zoom import ZoomReq
from .models import ZoomModel


class ZoomView(View):
    """ View for zoom api"""
    @staticmethod
    def get(request):
        zoom_obj = ZoomReq
        meeting_info = zoom_obj.get_meetings(zoom_obj)
        save_rows(meeting_info.get('meetings'))
        return render(request, 'zoom_list.html', meeting_info)

    @staticmethod
    def post(request):
        meeting_id = request.POST.get('meeting_id')
        zoom_obj = ZoomReq
        code = zoom_obj.status_meeting(zoom_obj, meeting_id)
        if code == 204:
            meeting = ZoomModel.objects.get(meeting_id=meeting_id)
            meeting.delete()
            return HttpResponse(code)
        return HttpResponse("error {}".format(code))


def save_rows(rows):
    for row in rows:
        meeting = ZoomModel(meeting_id=row.meeting_id, participants=row.participants)
        meeting.save()

