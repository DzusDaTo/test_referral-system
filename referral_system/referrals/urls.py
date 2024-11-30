from django.urls import path
from .views import SendCodeView, VerifyCodeView, UserProfileView

urlpatterns = [
    path('send-code/', SendCodeView.as_view(), name='send-code'),
    path('verify-code/', VerifyCodeView.as_view(), name='verify-code'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
