from rest_framework import serializers

from .models import Question, QuestionCategory, Answer, QuestionComment, AnswerComment


class QuestionCategorySerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize Question model.
    """
    class Meta:
        model = QuestionCategory
        fields = ('id', 'name',)


class BaseSerializer(serializers.ModelSerializer):
    """
    Base serializer class.
    """
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(source='author.get_full_name', read_only=True)


class QuestionCommentSerializer(BaseSerializer):
    """
    Serializer class to seralize QuestionComment model.
    """
    class Meta:
        model = QuestionComment
        fields = ('__all__')


class AnswerCommentSerializer(BaseSerializer):
    """
    Serializer class to seralize AnswerComment model.
    """
    class Meta:
        model = AnswerComment
        fields = ('__all__')


class AnswerModelSerializer(BaseSerializer):
    """
    Serializer class to seralize Answer model.
    """
    comments = AnswerCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Answer
        fields = ('__all__')


class QuestionSerializer(BaseSerializer):
    """
    Serializer class to seralize Question model.
    """
    categories = QuestionCategorySerializer(many=True)
    answer = AnswerModelSerializer(many=True, read_only=True)
    comments = QuestionCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('__all__')

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        category_list = []

        question = Question.objects.create(**validated_data)

        for category_data in categories_data:
            category, _ = QuestionCategory.objects.get_or_create(
                **category_data)
            category_list.append(category)

        question.categories.set(category_list)
        return question

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories')
        category_list = []

        for category_data in categories_data:
            category, _ = QuestionCategory.objects.update_or_create(
                **category_data)
            category_list.append(category)

        instance.categories.set(category_list)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)

        instance.save()
        return instance
