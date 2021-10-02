from django.urls import path
from .views import UserView, FormPostView


urlpatterns = [
    path('referral/<str:pk>', UserView.as_view(), name='get_user'),
    path('postform/', FormPostView.as_view(), name='post_form'),
]
