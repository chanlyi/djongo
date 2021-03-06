from djongo import models
from djongo.models import forms

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        abstract = True


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = (
            'name', 'email'
        )


class BlogContent(models.Model):
    comment = models.CharField(max_length=100)
    author = models.EmbeddedModelField(
        model_container=Author,
        model_form=AuthorForm
    )
    class Meta:
        abstract = True


class BlogContentForm(forms.ModelForm):

    class Meta:
        model = BlogContent
        fields = (
            'comment', 'author'
        )


class BlogPost(models.Model):
    h1 = models.CharField(max_length=100)
    content = models.EmbeddedModelField(
        model_container=BlogContent,
        model_form=BlogContentForm
    )

    objects = models.DjongoManager()


class Dummy2(models.Model):
    test = models.CharField(max_length=10)


class MultipleBlogPosts(models.Model):
    h1 = models.CharField(max_length=100)
    content = models.ArrayModelField(
        model_container=BlogContent,
        model_form=BlogContentForm
    )

    objects = models.DjongoManager()