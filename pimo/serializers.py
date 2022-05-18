from rest_framework import serializers

from pimo.models.order import Order
from pimo.models.offer import Offer
from pimo.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "title", 'created_by', "deadline", "status", "details")
        read_only_fields = ('created_by', )


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'title', 'created_by', 'deadline', 'status', 'details', )
        read_only_fields = ('created_by', )
