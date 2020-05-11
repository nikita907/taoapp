from django.contrib.auth.models import User
from django import forms
from .models import Users,Image,UserInfo
class UserRegistrationForm(forms.ModelForm):
    username=forms.CharField(widget=forms.Textarea(attrs={"class":"myclass"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class":"myclass"}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={"class":"myclass"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"myclass"}))
    a=Users.objects.all()
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=('photo',)
class UserInfoForm(forms.ModelForm):
    userAge=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"myclass"}))
    userTown = forms.CharField(widget=forms.Textarea(attrs={"class":"myclass"}))
    userCountry = forms.CharField(widget=forms.Textarea(attrs={"class":"myclass"}))
    CHOICES = [('Мужской','Мужской'), ('Женский','Женский')]
    userSex = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model=UserInfo
        fields=('userAge','userTown','userCountry','userSex')