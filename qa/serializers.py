from rest_framework import serializers
from .models import Question, QuestionCategory


class QuestionCategorySerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize Question model.
    """

    class Meta:
        model = QuestionCategory
        fields = (
            'id', 'name',
        )


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize Question model.
    """
    category = QuestionCategorySerializer()
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = (
            'id', 'title', 'author', 'category', 'body',
        )

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        data, _ = QuestionCategory.objects.get_or_create(**category_data)
        question = Question.objects.create(category=data, **validated_data)
        return question

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.name = category_data.get(
            'name', instance.category.name)
        instance.save()

        category = instance.category
        category.name = category_data.get('name', category.name)
        category.save()
        return instance
