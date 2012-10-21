# Create your views here.
from calimba.wiki.models import Page
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


def index(request):
  #pages = Page.objects.all()
  p = Page()
  pages = p.list_pages()
  
  if "fav_color" in request.session:
    request.session["fav_color"] = "blue"
  return render_to_response("index.html" ,{"pages":pages },context_instance=RequestContext(request))
      
      
def edit_page(request, page_slug):
  try:
    page= Page.objects.get(slug=page_slug)
    content = page.content
  except Page.DoesNotExist:
    page = Page(slug = page_slug, name= page_slug, content = "content for the " + page_slug, pub_date = timezone.now())
  return render_to_response("edit.html" ,{"page":page },context_instance=RequestContext(request))
  
  
def view_page(request, page_slug):
  try:
    page= Page.objects.get(slug=page_slug)
    return render_to_response("view.html", {"page":page} )
  except Page.DoesNotExist:
    return render_to_response("create.html", {"page_slug":page_slug } )
    
def save_page(request, page_slug):
  #slug    = request.POST["slug"]
  name    = request.POST["name"]
  content = request.POST["content"]
  try:
    page = Page.objects.get(slug=page_slug)
    page.content = content
    page.slug = page_slug
    page.name = name
  except Page.DoesNotExist:
    page = Page(slug = page_slug, name= name, content = content)
  page.save()
  
  return HttpResponseRedirect("/wiki/"+ page_slug)
    