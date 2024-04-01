import time
from django.http import StreamingHttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from faker import Faker
from faker.providers import internet



class StreamDataViewSet(viewsets.ViewSet):
    fake = Faker()
    fake.add_provider(internet)


    @action(methods=['GET' ], detail=False)
    def stream_data(self, request):
        # Simulated data generator function
        def generate_data():
            for i in range(10):
                yield f"Data point {i}\n"
                # Simulated delay for demonstration purposes
                time.sleep(1)
        
        # Return a streaming response with the generated data
        return StreamingHttpResponse(generate_data(), content_type="text/plain")



    def generate_user_data(self):
            for i in range(10):
                yield {'Username' : {self.fake.name()}, 'IP': {self.fake.ipv4_private()}}

    @action(methods=['GET' ], detail=False)
    def user_data(self, request):
        return StreamingHttpResponse(self.generate_user_data(), content_type="text/plain")
