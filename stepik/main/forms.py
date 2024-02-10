from django import forms
from .models import *
from django.core.validators import MinValueValidator, MaxValueValidator


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude=['is_published']


class AddLessonForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'


class AddCourseToUserForm(forms.ModelForm):
    
    class Meta:
        model = LessonContainer
        fields = '__all__'        


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Learner
        fields = '__all__'
        exclude=['user', 'coins']
        

class YourForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)        
    
    
class MyModelForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('idUser', 'idCourse')    
        

class CommentForm(forms.ModelForm):
    rate = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    class Meta:
        model = Comment
        fields = ('name', 'email','rate', 'body',)        