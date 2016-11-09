from rest_framework import serializers
from .models import booksmodel,contents


class contentserializer(serializers.ModelSerializer):

	class Meta:
		model =contents
		fields ='__all__'


class booksserializer(serializers.ModelSerializer):
    stories = serializers.StringRelatedField(many=True)

    class Meta:
        model = booksmodel
        fields =('title', 'cover', 'stories')
