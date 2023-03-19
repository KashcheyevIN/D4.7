from django.forms import ModelForm
from .models import Post

class PostSearchForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_header', 'post_category', 'author_post', 'post_text']