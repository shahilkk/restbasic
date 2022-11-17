
from rest_framework import serializers
from web.models import *

class CreateUser(serializers.ModelSerializer):
    # place = serializers.RelatedField(source='place', read_only=True)
    class Meta:
        model = Brand
        fields = ["id","name","created_date","place","code","image"]

    def create(self, validated_data):
        brand = Brand.objects.create(
            name=validated_data["name"],
            created_date=validated_data["created_date"],
            place=validated_data["place"],
            code=validated_data["code"],
            image=validated_data["image"],
        )
        brand.save()
        return brand

class EditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id","name", "place", "code","created_date","image"]

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name')
        instance.place=validated_data.get('place')
        instance.code=validated_data.get('code')
        instance.created_date=validated_data.get('created_date')
        instance.image=validated_data.get('image')
        instance.save()
        return instance



class FeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feed
        fields = ['id', 'subject', 'sprit_category', 'sprit_subcategory', 'wine_category', 'wine_subcategory', 'beer_category', 'beer_subcategory']

    def create(self, validated_data):
        brand_id = self.context['brand_id']
        return Feed.objects.create(brand_id=brand_id, **validated_data)


