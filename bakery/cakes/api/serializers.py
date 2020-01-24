from rest_framework import serializers

from cakes.models import Cake

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ['pk','title','description']
        read_only_fields = ['pk']
    # converts to Json and Validates

    #say we want to make sure that the titles are not repeated
    def validate_title(self,value):
        current_title = Cake.objects.filter(title__iexact = value)
        if self.instance:
            current_title = current_title.exclude(pk=self.instance.pk)
        if current_title.exists():
            raise serializers.ValidationError("Sorry, the provided cake title has already been registered!!")
        return value
    






