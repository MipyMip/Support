from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class SupportView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'key': 'reddison'})