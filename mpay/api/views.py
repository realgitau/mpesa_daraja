from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from mpay.models import LNMOnline
from mpay.api.serializers import LNMOnlineSerializer


class LNMCallbackAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self,request):
        print(request.data, "this is request.data")