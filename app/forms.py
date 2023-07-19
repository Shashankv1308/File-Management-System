from django import forms
from .models import file,Students,Faculty
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUp(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                'style':'width: 400px; padding:4px; border-radius:10px; ; '
            }
        )
    )

    password1= forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                'style':'width: 180px; padding:4px; border-radius:10px'
            }
        )
    )
    password2= forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                'style':'width: 180px; padding:4px; border-radius:10px'
            }
        )
    )
    email = forms.CharField(
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
               'style':'width: 400px; padding:4px; border-radius:10px'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' , 'is_staff', 'is_student', 'is_admin')



class file_form(forms.ModelForm):
    
    class Meta:
        model=file
        fields='__all__'
        widget={
            'name':forms.TextInput(attrs={"class":"form-control","placeholder": "Enter the Name of the file"}),
            'date':forms.DateTimeInput(attrs={'type': 'date',"class": "form-control", "placeholder": "Date and Time"}),
            'source':forms.Select(attrs={"class": "form-control", "placeholder": "Select source"}),
            'fo':forms.Select(attrs={"class": "form-control", "placeholder": "Select"}),
            'files':forms.FileInput(attrs={"class":"form-control","placeholder": "Upload file"}),
        }

class S_form(forms.ModelForm):

    class Meta:
        model=Students
        fields='__all__'
        widget= {
            'Name':forms.TextInput(attrs={"class":"form-control","placeholder": "Name"}),
            'Usn':forms.TextInput(attrs={"class":"form-control","placeholder": "Usn"}),
            'Email':forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the email"}),
            'Sem':forms.TextInput(attrs={"class": "form-control", "placeholder": "Sem"})
        }
            
        

class F_form(forms.ModelForm):

    class Meta:
        model=Faculty
        fields='__all__'
        widget={
            'Name':forms.TextInput(attrs={"class":"form-control","placeholder": "Name"}),
            'Ssn':forms.TextInput(attrs={"class":"form-control","placeholder": "Usn"}),
            'Email':forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the email"}),
            
        }



class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control"}
        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
