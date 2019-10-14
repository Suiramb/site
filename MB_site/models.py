from django.db import models


class Account(object):
	username = models.CharField()
	mail_adress = models.CharField()
	password = models.CharField()
	"""docstring for Account"""
	def __init__(self, arg):
		super(Account, self).__init__()
		self.arg = arg
