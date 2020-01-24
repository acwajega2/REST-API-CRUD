from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from cakes.models import Cake

#can be automated
# blank db
User = get_user_model()
class CakeAPITestCase(APITestCase):
    #setting up the database
    def setUp(self):
        user_obj = User(username='test',email='test@gmail.com')
        user_obj.set_password('test123')
        user_obj.save()

        cake = Cake.objects.create(title='sugarcake',
        description='so you are now testing thr cake API')
        #testing the number of cakes entred
    def test_single_cake(self):
        cake_count = Cake.objects.count()
        self.assertEqual(cake_count,1)

    

