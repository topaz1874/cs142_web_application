from django import forms
# from django.forms import ModelForm
from .models import User

class ImageUploadForm(forms.Form):
    imagefile = forms.ImageField(label='Select a file',)


class CommentForm(forms.Form):
    user_choices = [(user.slug, str(user)) for user in User.objects.all()]
    user = forms.ChoiceField(choices=user_choices)
    comments = forms.CharField(widget=forms.Textarea)

class DeleteForm(forms.Form):
    # cool_choices = (('somestuff', 'spam'),
    #             ('otherstuff', 'eggs'),
    #             ('banana', 'bar'))
    photo_id = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        )
