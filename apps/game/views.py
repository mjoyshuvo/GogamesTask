from rest_framework import serializers, viewsets
from apps.game.models import Game
from rest_framework.filters import SearchFilter, OrderingFilter


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    model = Game
    queryset = Game.objects.all()

    def get_queryset(self):
        queryset = Game.objects.all()
        category = self.request.query_params.get('category')
        if category:
            queryset = Game.objects.filter(category=category)
        return queryset
