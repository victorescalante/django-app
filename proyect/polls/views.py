from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer


class ListQuestions(APIView):

    def get(self, request):
        questions = Question.objects.all()
        questions_serializer = QuestionSerializer(questions, many=True)
        return Response(questions_serializer.data)

    def post(self, request):
        question_serializer = QuestionSerializer(data=request.data)
        if question_serializer.is_valid():
            question_serializer.save()
            return Response(question_serializer.data)
        return Response(question_serializer.errors)
