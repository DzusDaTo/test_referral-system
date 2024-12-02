import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from random import randint


class SendCodeView(APIView):
    """
    Имитирует отправку кода на телефон
    """
    codes = {}

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"error": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

        code = randint(1000, 9999)
        self.codes[phone_number] = code
        time.sleep(2)
        return Response({"message": "Code sent", "code": code})


class VerifyCodeView(APIView):
    """
    Проверяет код авторизации
    """
    codes = SendCodeView.codes

    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        if not phone_number or not code:
            return Response({"error": "Phone number and code are required"}, status=status.HTTP_400_BAD_REQUEST)

        if phone_number in self.codes and self.codes[phone_number] == int(code):
            user, created = User.objects.get_or_create(phone_number=phone_number)
            return Response({"message": "Authorized", "user": UserSerializer(user).data})
        return Response({"error": "Invalid code"}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    """
    Возвращает профиль пользователя
    """
    def get(self, request):
        phone_number = request.query_params.get('phone_number')
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(UserSerializer(user).data)

    def post(self, request):
        """
        Активирует инвайт-код
        """
        phone_number = request.data.get('phone_number')
        invite_code = request.data.get('invite_code')

        user = User.objects.filter(phone_number=phone_number).first()
        inviter = User.objects.filter(invite_code=invite_code).first()

        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if not inviter:
            return Response({"error": "Invite code not found"}, status=status.HTTP_400_BAD_REQUEST)
        if user.activated_invite:
            return Response({"error": "Invite code already activated"}, status=status.HTTP_400_BAD_REQUEST)

        user.activated_invite = invite_code
        inviter.invited_users.add(user)
        user.save()
        return Response({"message": "Invite code activated"})

