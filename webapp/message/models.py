from django.core.validators import FileExtensionValidator
from django.db import models
from users.models import User
from jobapp.models import PostJob
from .validators import validate_file_size, validate_pdf


class Message(models.Model):
    """

    The `Message` class represents a message sent between two users in the application. It is a Django model that is used to store message-related information in the database.

    Attributes:
    - `sender`: A foreign key to the `User` model representing the user who sent the message.
    - `recipient`: A foreign key to the `User` model representing the user who received the message.
    - `content`: A TextField to store the content of the message.
    - `timestamp`: A DateTimeField that automatically stores the date and time when the message was created.
    - `is_read`: A BooleanField indicating whether the message has been read by the recipient. Default is `False`.
    - `is_archived`: A BooleanField indicating whether the message has been archived. Default is `False`.
    - `job`: A foreign key to the `PostJob` model representing the job associated with the message. It is optional and can be `null` or blank.
    - `attachment`: A FileField to store any attachments associated with the message. It is optional and can be `null` or blank. It uses the `validate_pdf` and `validate_file_size` validators.

    Usage:
    The `Message` model can be used to create, update, and retrieve messages between users in the application.

    Example:
    # Create a new message
    sender = User.objects.get(username="sender")
    recipient = User.objects.get(username="recipient")
    message = Message(sender=sender, recipient=recipient, content="Hello!")
    message.save()

    # Retrieve all messages
    messages = Message.objects.all()

    # Update a message
    message = Message.objects.get(id=1)
    message.content = "Updated content"
    message.save()
    """
    sender = models.ForeignKey(
        User, related_name="sent_messages", on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User, related_name="received_messages", on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    job = models.ForeignKey(PostJob, on_delete=models.PROTECT, null=True, blank=True)
    attachment = models.FileField(
        upload_to="attachments/",
        blank=True,
        null=True,
        validators=[validate_pdf, validate_file_size],
    )
