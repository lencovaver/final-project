import unittest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from message.models import Message


class TestInboxView(TestCase):
    def setUp(self):
        # Create users
        self.user_a = User.objects.create_user(username="UserA", password="123456")
        self.user_b = User.objects.create_user(username="UserB", password="123456")

        # User A sends two messages to User B
        Message.objects.create(
            sender=self.user_a, recipient=self.user_b, content="Hello, User B!"
        )
        Message.objects.create(
            sender=self.user_a, recipient=self.user_b, content="How are you, User B?"
        )

        self.client = Client()

    def test_inbox_view_for_user_a(self):
        # Log in as User A
        self.client.login(username="UserA", password="123456")

        # Access the inbox view
        response = self.client.get("/inbox/")

        # Check if HTTP response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if User A's inbox includes the two messages it sent
        messages = list(response.context["inbox"])
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0].content, "How are you, User B?")
        self.assertEqual(messages[1].content, "Hello, User B!")
