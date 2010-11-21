from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	class Admin: pass
        title = models.CharField(maxlength=1024)
        title_slug = models.SlugField(prepopulate_from=('title',), unique=True)
        author = models.ForeignKey(User)
        date = models.DateTimeField(auto_now=True)
        text = models.TextField()
	draft = models.BooleanField()

        def __str__(self):
                return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('webcicletta.views.blog_post', (str(self.title_slug),))

class Page(models.Model):
	class Admin: pass
        title = models.CharField(maxlength=1024)
        title_slug = models.SlugField(prepopulate_from=('title',))
        author = models.ForeignKey(User)
        date = models.DateTimeField(auto_now=True)
        text = models.TextField()
	draft = models.BooleanField()

        def __str__(self):
                return self.title
	
	@models.permalink
	def get_absolute_url(self):
		return ('webcicletta.views.page', (str(self.title_slug),))

class Show(models.Model):
	class Admin: pass
	title = models.CharField(maxlength=1024)
	title_slug = models.SlugField(prepopulate_from=('title',))
	description = models.TextField()
	notes = models.TextField(maxlength=1024, blank=True)
	authors = models.ManyToManyField(User,blank=True)
	
	def is_current(self): return get_current_show().title_slug == self.title_slug

	def __str__(self): return self.title

	@models.permalink
	def get_absolute_url(self): return ('webcicletta.views.show_info', (self.title_slug,))

giorni = (('lu', 'Lunedi'), ('ma', 'Martedi'), ('me', 'Mercoledi'), ('gi', 'Giovedi'), ('ve', 'Venerdi'), ('sa', 'Sabato'), ('do', 'Domenica'))
giorni_n = {'lu': 0, 'ma': 1, 'me': 2, 'gi': 3, 've': 4, 'sa': 5, 'do': 6}

from datetime import *

class ShowSchedule(models.Model):
	class Admin: pass
	show = models.ForeignKey(Show)
	day = models.CharField(maxlength=2,choices=giorni)
	begin = models.TimeField()
	end = models.TimeField()

	def delta_from_monday(self): return timedelta(giorni_n[self.day])
	
	def __str__(self): return str(self.show) + " " + self.day + " - " + str(self.begin) + " to " +str(self.end)

class CurrentShow(models.Model):
	show = models.ForeignKey(Show)

def get_current_show():
	try:
		current_show = CurrentShow.objects.get()
	except:
		return None
	
	return current_show.show

def set_current_show(show):
	try:
		current_show = CurrentShow.objects.get()
	except:
		current_show = CurrentShow()
	
	current_show.show = show
	current_show.save()

def current_show_processor(request):
	if request.user.is_authenticated():
		all_shows = Show.objects.all()
	else:
		all_shows = None
	return {'current_show': get_current_show(), 'all_shows': all_shows}

