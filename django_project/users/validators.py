from django.core.exceptions import ValidationError


def ValidateSchoolEmail(value):
    if "@hfed.net" not in value:
        raise ValidationError("A valid Harris email address must be entered in")
    else:
        return value
