from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 1048576:
        raise ValidationError("The maximum file size that can be uploaded is 1MB")
    else:
        return value


def validate_pdf(value):
    import os

    ext = os.path.splitext(value.name)[
        1
    ]  # [0] returns path+filename, [1] returns file extension
    valid_extensions = [".pdf"]

    if not ext.lower() in valid_extensions:
        raise ValidationError("Only PDF files are allowed.")
