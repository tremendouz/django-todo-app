from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['pk', 'user', 'title', 'description',
                  'timestamp', 'updated', 'slug']
        read_only_fields = ['pk']

    def validate_title(self, value):
        qs = Task.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This title already exists")
        return value
