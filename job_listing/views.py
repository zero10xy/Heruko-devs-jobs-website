from django.shortcuts import render
from django.http import HttpResponse
from utils import mongo_tools
from django.contrib.staticfiles.storage import staticfiles_storage

#url = staticfiles_storage.url('data/foobar.csv')
# Create your views here.
def index(request):
	#return HttpResponse("test")
	collection =mongo_tools.get_mongo_db()["coll1"]
	cursor = collection.find({})
	return render(request, 'job-listing.html', {'data':cursor })