from django import forms
from django.forms.models import inlineformset_factory
from courses.models import Course, Module, Review, Subject, Content
from students.models import (
    User
)

class ModuleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'cols': 40, 'rows': 8}))

    class Meta:
        model = Module
        exclude = ()

ModuleFormSet = inlineformset_factory(Course, Module, form=ModuleForm, fields=['title', 'description',], extra=2, can_delete=True)


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 40, 'rows': 15, 'class':'form-control'})
        }


class CourseCreateForm(forms.ModelForm):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    overview = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'cols': 40, 'rows': 15}))

    class Meta:
        model = Course
        fields = ['subject', 'title', 'overview',]
