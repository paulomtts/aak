from rest_framework import serializers

from challenge.models import Label, Task


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ["name", "owner"]
        read_only_fields = ["owner"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "is_completed",
            "owner",
            "labels",
        ]
        read_only_fields = ["owner"]
