from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by("-created_at")
    serializer_class = ReviewSerializer



from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if not user:
        return Response({"error": "Invalid credentials"}, status=401)

    refresh = RefreshToken.for_user(user)

    return Response({
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
        }
    })

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsAdmin, IsMentor


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin])
def admin_only_view(request):
    return Response({
        "message": "Welcome Admin",
        "user": request.user.username
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsMentor])
def mentor_only_view(request):
    return Response({
        "message": "Welcome Mentor",
        "user": request.user.username
    })
