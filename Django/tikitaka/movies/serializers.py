from rest_framework import serializers
from .models import Movie, Country, People, WatchProvider, Genre


class PosterListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title', 'poster_path', 'backdrop_path',)


# class MovieNameSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Movie
#         fields = ('title',)


# class ReviewListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Review
#         fields = ('title', 'content',)


# class ReviewSerializer(serializers.ModelSerializer):
#     movie = MovieNameSerializer(read_only=True)

#     class Meta:
#         model = Review
#         fields = '__all__'


# class ActorListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         fields = '__all__'
#         read_only_fields = ('movies',)


# class ActorNameSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         fields = ('name',)


# class MovieSerializer(serializers.ModelSerializer):
#     actors = ActorNameSerializer(many=True, read_only=True)
#     review_set = ReviewSerializer(many=True, read_only=True)
#     class Meta:
#         model = Movie
#         fields = '__all__'




class PeopleSerializer(serializers.ModelSerializer):
    movies = PosterListSerializer(many=True, read_only=True)
    class Meta:
        model = People
        fields = '__all__'