from django.contrib.syndication.feeds import Feed,FeedDoesNotExist
from models import Post
from django.shortcuts import get_object_or_404

class BlogFeed(Feed):
    title='Radiocicletta Blog'
    link='http://radiocicletta.it/blog/' #URI of site
    description='Latest Blog Entries'

    '''def get_object(self, request, post_id):
        return get_object_or_404(Post, pk=post_id)

    def title(self, obj):
        return "Radiocicletta.it: %s" % obj.title

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return "News dal blog di radiocicletta: %s" % obj.title'''

    def items(self, obj):
        return Post.objects.all().order_by('-date')

    def item_pubdate(self,item):
        #For each item, what is the pubdate?
        return item.date

