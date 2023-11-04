from django import forms

from blog.models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['post']
        labels = {'user_name':'Your Name', 'user_email':'Your Email', 'text':'Your Comment'}
