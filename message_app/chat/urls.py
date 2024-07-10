from django.urls import path
from .views import UserListView, ConversationListView, MessageListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('conversations/', ConversationListView.as_view(), name='conversation-list'),
    path('messages/', MessageListView.as_view(), name='message-list'),
]
