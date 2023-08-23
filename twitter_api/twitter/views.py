from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from twitter.models import Tweet
from twitter.serializers import TweetSerializer


class TweetView(APIView):

	def post(self, request):
		serializer = TweetSerializer(data=request.data, many=False)
		# Check Data Validation
		if serializer.is_valid():                                       # If data is valid, create new
			serializer.create(serializer.validated_data)
			response_message = "Post created successfully"
			status_code = status.HTTP_201_CREATED
		else:                                                           # If data is not valid, show error
			response_message = serializer.errors
			status_code = status.HTTP_406_NOT_ACCEPTABLE

		return Response(response_message, status=status_code)

	def get(self, request):
		queryset = Tweet.objects.all()                                  # Getting all post
		serializer = TweetSerializer(queryset, many=True)               # Serializing queryset
		return Response(serializer.data, status=status.HTTP_200_OK)
