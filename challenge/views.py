from typing import Generic, Type, TypeVar
from rest_framework.request import Request
from rest_framework import status, viewsets
from rest_framework.response import Response

from challenge.models import Label, Task
from challenge.serializers import LabelSerializer, TaskSerializer
from rest_framework.serializers import ModelSerializer
from django.db.models import Model
from django.db.models import QuerySet

ModelType = TypeVar("ModelType", bound=Model)
SerializerType = TypeVar("SerializerType", bound=ModelSerializer)


class BaseViewSet(Generic[ModelType, SerializerType], viewsets.ModelViewSet):
    queryset: QuerySet[ModelType]
    serializer_class: Type[SerializerType]

    def list(self, request: Request) -> Response:
        return Response(
            self.serializer_class(
                self.get_queryset().filter(owner=request.user), many=True
            ).data
        )

    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request: Request, pk: int) -> Response:
        obj = self.queryset.filter(pk=pk, owner=request.user).first()
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(self.serializer_class(obj).data)

    def update(self, request: Request, pk: int) -> Response:
        obj = self.queryset.filter(pk=pk, owner=request.user).first()
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk: int) -> Response:
        obj = self.queryset.filter(pk=pk, owner=request.user).first()
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LabelViewSet(BaseViewSet[Label, LabelSerializer]):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class TaskViewSet(BaseViewSet[Task, TaskSerializer]):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
