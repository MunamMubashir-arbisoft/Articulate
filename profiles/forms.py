from django import forms
from .models import Profile
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Username"}), label="", )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder":"Password"}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder":"Confirm password"}), label="")

    class Meta:
        model = Profile
        fields = ("username",)

    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")

        username = self.cleaned_data.get("username")

        if username is not None:
            if Profile.objects.filter(username=username).exists():
                raise ValidationError("Username already in use")

        return self.cleaned_data


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Username"}), label="", )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder":"Password"}), label="")

    def clean(self):
        password = self.cleaned_data.get("password")
        username = self.cleaned_data.get("username")

        if username is not None and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("Invalid username or password")
            else:
                if not user.is_active:
                    raise ValidationError("User is not active")
                else:
                    self.cleaned_data["user"] = user
        return self.cleaned_data


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'display', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]