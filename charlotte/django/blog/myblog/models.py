from django.db import models
from versatileimagefield.fields import VersatileImageField

class Post(models.Model):
    STATUS_CHOICES = (('published', 'Published'), ('draft', 'Draft'), ('archived', 'Archived'),)
    POST_STATUS = (('published', 'Published'),('draft', 'Draft'),('archived', 'Archived'),)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    banner_photo = VersatileImageField()
    body = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    status = models.CharField(max_length=10, choices=POST_STATUS, default='published')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

class Tag(models.Model):
    title                   = models.CharField(max_length=150)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)


class Category(models.Model):
    title                   = models.CharField(max_length=150)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)


#class Comment(models.Model):
    # post = models.ForeignKey('Post', on_delete=models.CASCADE)
    # content = models.TextField()
    # author = models.CharField(max_length=150)
    # date_created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
        # return '{}'.format(self.content)