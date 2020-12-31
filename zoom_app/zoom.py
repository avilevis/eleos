import json
import http.client
import ssl
from django.conf import settings

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


class ZoomReq:
    """ Class for zoom api"""
    headers = {
        'authorization': 'Bearer {}'.format(settings.TOKEN),
        'content-type': 'application/json',
    }

    def get_meetings(self):
        conn = http.client.HTTPSConnection("api.zoom.us")
        conn.request("GET", "/v2/metrics/meetings/", headers=self.headers)
        res = conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))

    def status_meeting(self, meeting_id):
        conn = http.client.HTTPSConnection("api.zoom.us")
        params = {"action": "end"}
        conn.request("PUT", '/v2/meetings/{}/status'.format(meeting_id), body=json.dumps(params), headers=self.headers)
        res = conn.getresponse()
        return res.getcode()
