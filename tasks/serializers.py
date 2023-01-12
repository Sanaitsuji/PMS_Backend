from rest_framework import serializers
from .models import Task, STATE_CHOICES

class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data or key == data:
                return key
        self.fail('invalid_choice', input=data)

class TaskSerializer(serializers.ModelSerializer):
    state = ChoiceField(choices=STATE_CHOICES)

    class Meta:
        model = Task
        fields = ('id', 'name', 'user_story', 'assigned_user', 'state', 'description', 'invested_time', 'estimated_time', 'remaining_time')
        read_only_fields = ('created_at',)