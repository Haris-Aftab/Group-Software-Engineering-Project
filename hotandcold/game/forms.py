"""Forms used in game app.

Used for entering, validating and cleaning user input with HTML forms.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    """User registration form.

    Used for creating users. Inherits from UserCreationForm and adds an
    email field.
    """
    class Meta(UserCreationForm.Meta):
        """Metadata for form."""

        # Add email field to form.
        fields = UserCreationForm.Meta.fields + ("email",)


class UserUpdateEmailForm(forms.Form):
    """User update email form.

    Used for updating the email of a user.
    """
    email = forms.EmailField()


class EventCreationForm(forms.Form):
    """Event creation form.

    Used for creating events, inherits from normal Form.
    """
    # Title and description fields.
    title = forms.CharField(label="Title", max_length=80)
    description = forms.CharField(label="Description", max_length=200)

    # Start/end datetime fields.
    start = forms.DateTimeField(label="Start",
            widget=forms.DateTimeInput(attrs={"type": "datetime-local"}))
    end = forms.DateTimeField(label="End",
            widget=forms.DateTimeInput(attrs={"type": "datetime-local"}))

    # Latitude/longitude decimal fields.
    latitude = forms.DecimalField(label="Latitude", max_digits=22, decimal_places=16)
    longitude = forms.DecimalField(label="Longitude", max_digits=22, decimal_places=16)


class TreasureChestCreationForm(forms.Form):
    """TreasureChest creation form.

    Used for creating treasure chests, inherits from normal Form.
    """
    # Name field.
    name = forms.CharField(label="Name")

    # Points field.
    points = forms.IntegerField(label="Points")

    # Latitude/longitude decimal fields.
    latitude = forms.DecimalField(label="Latitude", max_digits=22, decimal_places=16)
    longitude = forms.DecimalField(label="Longitude", max_digits=22, decimal_places=16)
