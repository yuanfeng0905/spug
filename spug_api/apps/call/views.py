from django.views.generic import View
from libs import json_response

class TestView(View):
    def get(self, request):
        host_id = request.GET.get('id')
        
        return json_response({'hello': 'test'})