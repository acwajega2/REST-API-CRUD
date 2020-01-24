# using generic views
from rest_framework import generics,mixins
from cakes.models import Cake
from .serializers import CakeSerializer
from .permissions import IsOwnerOrReadOnly

from django.db.models import Q

#List Cake View
class CakeListAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CakeSerializer
 
    def get_queryset(self):
        qs = Cake.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(description__icontains=query)) .distinct()


        return qs

    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)
   
  


#Create Cake View
class CakeAPIView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = CakeSerializer
 
    def get_queryset(self):
        return Cake.objects.all()
  

#Retirve Update Delete View
class CakeRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CakeSerializer
    permission_classes =[IsOwnerOrReadOnly]
 
    def get_queryset(self):
        return Cake.objects.all()
    

    

