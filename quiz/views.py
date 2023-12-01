from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Option, Question
from .serializers import QuestionSerializer, CategorySerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import status



@api_view(["GET"])
def get_all_questions(request, pk):
    
    category = Category.objects.get(pk=pk)
    questions = Question.objects.filter(category=category).prefetch_related("option")
    serializer = QuestionSerializer(questions, many=True)
    

    return Response(serializer.data)

@api_view(['GET'])
def get_active_category(request):

    categories = Category.objects.filter(is_active=True)
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_history_category(request):

    categories = Category.objects.filter(is_active=False)
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)


@api_view(['PATCH'])
def edit_active_status(request,pk):
    
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"error":"category doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CategorySerializer(category, data=request.data, partial=True)

    if serializer.is_valid():

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






