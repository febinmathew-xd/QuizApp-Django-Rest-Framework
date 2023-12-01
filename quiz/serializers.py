from rest_framework import serializers
from . models import Option, Question , Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'is_active']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option', 'is_true']



class QuestionSerializer(serializers.ModelSerializer):
    option = OptionSerializer(many=True, read_only=True)
    category = CategorySerializer()
    

    class Meta:
        model = Question
        depth =1
        fields = ['id', 'category', 'question', 'option']
