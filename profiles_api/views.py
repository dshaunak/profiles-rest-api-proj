from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        """Every HTTP function we write is expected to return a response object"""
        """"The returned obj must have a dictionary or list in its arguments as Django converts the return object into JSON"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View, but is specific to APIs',
            'Gives you the most control over your API logic',
            'Is mapped manually to URLs',
            'Euuu',
        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})
