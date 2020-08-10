from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.Serializer):
    questions_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateField()

    class Meta:
        model = Question

    def create(self, validated_data):
        return Question.objects.create(**validated_data)