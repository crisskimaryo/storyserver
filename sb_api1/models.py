from django.db import models


class author(models.Model):
	"""docstring for ClassName"""
	firstname=models.CharField(max_length=100,null=True)
	lastname=models.CharField(max_length=100,null=True)
	email=models.CharField(max_length=100,null=True)
	phone=models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.firstname

class booksmodel(models.Model):
	"""docstring for ClassName"""
	title=models.CharField(max_length=100,null=True)
# 	content= models.ForeignKey(contents, on_delete=models.CASCADE,null=True, related_name='stories')
	author= models.ForeignKey(author, on_delete=models.CASCADE,null=True)
# 	manytomany should be used
	extra=models.CharField(max_length=100,null=True, blank=True)
	cover=models.TextField(null=True,blank=True)
	n_likes=models.IntegerField(default=0)
	like= models.BooleanField(default=False)
	def __str__(self):
		return self.title

class contents(models.Model):
	"""docstring for ClassName"""
	book= models.ForeignKey(booksmodel, related_name='stories')
	sub_title=models.CharField(max_length=100,null=True)
	content=models.TextField(null=True)
	chapter=models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.sub_title


