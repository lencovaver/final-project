import pytest
from django.test import Client
from django.urls import reverse
from users.models import User
from users.forms import RegistrationForm


@pytest.mark.django_db
def test_registration_view():
    # Test user registration view.

    client = Client()
    url = reverse(
        "registration"
    )  # Replace 'registration' with the actual url name for RegistrationView
    response = client.get(url)

    # Check if the status code of the response is 200 (OK)
    assert response.status_code == 200

    # Check if the correct template was used
    assert response.templates[0].name == "registration.html"

    user_count = User.objects.count()

    form_data = {
        "username": "testuser",
        "password1": "Testpassword123",
        "password2": "Testpassword123",
    }
    response = client.post(url, form_data)

    assert response.status_code == 302
    assert response.url == reverse("registration-success")

    assert User.objects.count() == user_count + 1
    assert User.objects.last().username == "testuser"
