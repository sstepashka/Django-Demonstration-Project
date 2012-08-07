from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource
from blogpost.models import BlogPost, Comment

class BlogPostResource(ModelResource):
	model = BlogPost

	fields = ('created', 'title', 'content', 'url', 'comments',)
	ordering = ('-created',)

	def comments(self, instance):
		return reverse('comments', kwargs={'blogpost':instance.id})

class CommentResource(ModelResource):
	model = Comment
	
	fields = ('created', 'comment', 'url', 'blogpost',)
	ordering = ('-created',)

	def blogpost(self, instance):
		return reverse('blog-post', kwargs={'id':instance.blogpost.id})