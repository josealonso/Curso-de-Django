from rest_framework.views import APIView
from rest_framework.response import Response


class HelloWorld(APIView):

    def get(self, request):
        return Response(['hello', 'world'])

    def post(self, request):
        return Response(request.data)

    def put(self, request):
        return Response(request.data)

