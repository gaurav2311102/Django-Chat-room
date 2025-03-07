from django import forms
from .models import Room,Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Room, Topic

class RoomForm(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "custom-multi-select"}),
        required=True  
    )

    class Meta:
        model = Room
        fields = ['topics', 'name', 'description']
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter room name", "class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Enter description", "class": "form-control"}),
        }

        
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password1',"password2"]
        
    def clean_email(self):
            email = self.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email already exists')
            
            return email
        
class UpdateMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        
        widgets = {
            'text' : forms.Textarea(attrs={'placeholder':'Update message','rows':4, "class":"form-control"})
        }