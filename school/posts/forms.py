from django import forms


from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'text', 'is_important', 'image', 'video')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('group', 'title', 'slug')
