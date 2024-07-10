from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConversationListView(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        participants = self.request.data.get('participants')
        conversation = serializer.save()
        for participant_id in participants:
            user = User.objects.get(id=participant_id)
            conversation.participants.add(user)

class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
