from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post,Comment

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_picture"]


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas"
    )

    class Meta:
        model = Post
        fields = ['title', 'content','tags']

    # Correct method name (Django will call this automatically)
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("The title must be at least 5 characters long.")
        return title
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # editing an existing post
            current_tags = ", ".join([tag.name for tag in self.instance.tags.all()])
            self.fields["tags"].initial = current_tags

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        # handle tags
        tags_str = self.cleaned_data.get("tags", "")
        tag_names = [name.strip() for name in tags_str.split(",") if name.strip()]

        # clear old tags
        instance.tags.clear()

        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            instance.tags.add(tag)

        return instance
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        def clean_content(self):
            content = self.cleaned_data.get('content')
            if len(content.strip()) == 0:
                raise forms.ValidationError("Content cannot be empty")
            return content
