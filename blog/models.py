# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User
# from blog.fields import OrderField
#
# # Create your models here.
#
#
#
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from blog.fields import OrderField

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    class Syntax(models.TextChoices):
        SHELL = 'SH', 'Shell'
        PYTHON = 'PY', 'Python'
        JAVASCRIPT = 'JS', 'JavaScript'
        HTML_CSS = 'WEB', "HTML/CSS"
        SQL = 'SQL', 'SQL'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User,
        related_name='blog_posts',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )
    syntax = models.CharField(
        max_length=3,
        choices=Syntax.choices,
        default=Syntax.SHELL
    )

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

#
#
#
# class Post(models.Model):
#     class Status(models.TextChoices):
#         DRAFT = 'DF', 'Draft'
#         PUBLISHED = 'PB', 'Published'
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250)
#     author = models.ForeignKey(
#         User,
#         related_name='blog_posts',
#         on_delete=models.CASCADE
#     )
#     body_intro = models.TextField()
#     body_template = models.TextField(blank=True)
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(
#         max_length=2,
#         choices=Status.choices,
#         default=Status.DRAFT
#     )
#
#     class Meta:
#         ordering = ['-publish']
#         indexes = [
#             models.Index(fields=['-publish']),
#         ]
#
#     def __str__(self):
#         return self.title
#
#
#
#
#
# class PostSnippet(models.Model):
#     class Syntax(models.TextChoices):
#         PYTHON = 'PY', "Python"
#         JAVASCRIPT = 'JS', "JavaScript"
#         SHELL = "SH", 'Shell'
#         HTML = 'HTML', 'HTML'
#         CSS = 'CSS', 'CSS'
#
#     post = models.ForeignKey(
#         Post,
#         related_name='snippets',
#         on_delete=models.CASCADE
#     )
#     title = models.CharField(max_length=250)
#     order = OrderField(blank=True, for_fields=['post', 'syntax'])
#     body = models.TextField()
#     syntax = models.CharField(
#         max_length=4,
#         choices=Syntax.choices,
#         default=Syntax.SHELL
#     )
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['order']
#         indexes = [
#             models.Index(fields=['post', 'order'])
#         ]
#
#     def __str__(self):
#         return f'<{self.syntax} #{self.order} for {self.post}>\n```\n{self.body}\n```'
#
#
#
#
#
#
#
