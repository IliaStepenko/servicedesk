from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from usermanager.serializers import RegistrationSerializer


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializers = RegistrationSerializer(data=request.data)
        data = {}
        if serializers.is_valid():
            user = serializers.save()
            data['response'] = "successfully registered"
            data['email'] = user.email
            data['username'] = user.username
            data['token'] = Token.objects.get(user = user).key
        else:
            data = serializers.errors

        return Response(data)