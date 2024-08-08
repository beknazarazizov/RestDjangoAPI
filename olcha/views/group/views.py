from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from olcha.models import Group
from olcha.serializers import GroupSerializer


class GroupApiView(APIView):

    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



class GroupCreateApiView(APIView):
    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupUpdateApiView(APIView):

    def put(self, request, pk):
        group = Group.objects.get(pk=pk)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupDeleteApiView(APIView):

    def delete(self, request, pk):
        group = Group.objects.get(pk=pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupDetailApiView(APIView):

    def get(self, request, pk):
        group = Group.objects.get(pk=pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

