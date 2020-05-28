from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import viewsets
from rest_framework.status import \
    HTTP_400_BAD_REQUEST as BAD_REQUEST, \
    HTTP_201_CREATED as CREATED, \
    HTTP_404_NOT_FOUND as NOT_FOUND
from rest_framework.response import Response
from lucky_draw import serializers, models


class ContestantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContestantSerializer
    queryset = models.Contestant.objects.all()

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = serializers.ContestantSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = self.get_queryset()
        contestant = get_object_or_404(queryset, pk=id)
        serializer = serializers.ContestantSerializer(contestant)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = serializers.ContestantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=BAD_REQUEST)

        return Response(serializer.data, status=CREATED)


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = serializers.EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = self.get_queryset()
        event = get_object_or_404(queryset, pk=pk)
        serializer = serializers.EventSerializer(event)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = serializers.EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=BAD_REQUEST)

        return Response(serializer.data, status=CREATED)


class DrawViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DrawSerializer
    queryset = models.Draw.objects.all()

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = serializers.DrawSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = self.get_queryset()
        draw = get_object_or_404(queryset, pk=id)
        serializer = serializers.DrawSerializer(draw)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = serializers.DrawSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=BAD_REQUEST)

        return Response(serializer.data, status=CREATED)


class PrizeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PrizeSerializer
    queryset = models.Prize.objects.all()

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = serializers.PrizeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = self.get_queryset()
        contestant = get_object_or_404(queryset, pk=id)
        serializer = serializers.PrizeSerializer(contestant)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = serializers.PrizeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=BAD_REQUEST)

        return Response(serializer.data, status=CREATED)

