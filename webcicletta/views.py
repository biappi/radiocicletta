from django.shortcuts import render_to_response, get_object_or_404
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from models import Post, Show, Page, set_current_show, ShowSchedule

def render_req_to_resp(request, template, dict={}):
	return render_to_response(template, dict, context_instance=RequestContext(request))

def index(request):
	post = Post.objects.latest('date')
	return render_req_to_resp(request, 'index.html', {'post': post})

def post_list(request):
	posts = Post.objects.all().order_by('-date')
	
	if not request.user.is_authenticated():
		posts = posts.filter(draft__exact = False)
	
	return render_req_to_resp(request, 'post_list.html', {'posts': posts})

def blog_post(request, slug):
	post = get_object_or_404(Post, title_slug=slug)
	return render_req_to_resp(request, 'post.html', {'post': post})

def update_post_with_request(newPost, request, update_user = False, force_slug = True):
	valid = True
	
	try:
		newPost.title = request.POST['post_title']
		if force_slug:
			newPost.title_slug = slugify(newPost.title)
	except:
		valid = False
	
	try:
		newPost.text = request.POST['post_content']
	except:
		valid = False
	
	try:
		newPost.draft = request.POST['post_status'] == 'draft'
	except:
		valid = False

	if valid:
		if update_user:
			newPost.author = request.user

		try:
			newPost.save()
		except:#IntegrityError:
			originalSlug = newPost.title_slug

			keepGoing = True
			disambiguate = 0
			while keepGoing == True:
				try:
					newPost.title_slug = originalSlug + '-' + str(disambiguate)
					newPost.save()
					keepGoing = False
				except:
					disambiguate += 1
		
		return True
	else:
		return False

@login_required
def new_blog_post(request):
	newPost = Post()
	newPost.draft = True

	if update_post_with_request(newPost, request, update_user=True):
		return HttpResponseRedirect('/')
	else:   
		return render_req_to_resp(request, 'post_edit.html', {'post': newPost})


@login_required
def edit_blog_post(request, slug):
	post = get_object_or_404(Post, title_slug=slug)
	if update_post_with_request(post, request):
		return HttpResponseRedirect(post.get_absolute_url())
	else:
		return render_req_to_resp(request, 'post_edit.html', {'post': post})

def profile(request):
	return render_req_to_resp(request, 'registration/profile.html')

def shows(request):
	import datetime
	today = datetime.date.today()
	delta = datetime.timedelta(-today.weekday())
	monday = today + delta

	def to_js_date(x):
		return "new Date(%d, %d, %d, %d, %d, %d)" % (x.year, x.month - 1, x.day, x.hour, x.minute, x.second)

	def do_dict(x):
		return	{
				'title': x.show.title,
				'start': to_js_date(datetime.datetime.combine(monday + x.delta_from_monday(), x.begin)),#time_to_jstime(monday + x.begin_timedelta_from_monday()),
				'end': to_js_date(datetime.datetime.combine(monday + x.delta_from_monday(), x.end)),#time_to_jstime(monday + x.end_timedelta_from_monday())
				'url': x.show.get_absolute_url()
			}

	shows = map(do_dict, ShowSchedule.objects.all())
	
	return render_req_to_resp(request, 'shows_schedule.html', {'schedule': shows})

def show_info(request, slug):
	show = get_object_or_404(Show, title_slug=slug)
	return render_req_to_resp(request, 'show_info.html', {'show': show})

def page(request, slug):
	try:
		page = Page.objects.get(title_slug=slug)
	except Page.DoesNotExist:
		if not request.user.is_authenticated():
			raise Http404
		page = None

	return render_req_to_resp(request, 'page.html', {'page': page})

@login_required
def edit_page(request, slug):
	try:
		page = Page.objects.get(title_slug=slug)
	except Page.DoesNotExist:
		page = Page()
		page.title = slug
		page.title_slug = slug
	
	if update_post_with_request(page, request, update_user=True, force_slug=False):
		return HttpResponseRedirect(page.get_absolute_url())
	else:
		return render_req_to_resp(request, 'post_edit.html', {'post': page})

@login_required
def change_current_show(request):
	#try:
	show = Show.objects.get(title_slug=request.POST["new_show"])
	set_current_show(show)
	#except:
	#	pass
	
	return HttpResponseRedirect('/')
