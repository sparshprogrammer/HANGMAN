import random
from django.shortcuts import render
from django.shortcuts import render_to_response,  render,RequestContext,redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
# Create your views here.
def index(request):
    movies_list=['SPIDERMAN','SUPERMAN','DANGAL','DHOOM','RUSTOM','DABANG','HARAMKHOR','GOLMAAL','ROBOT','FAN']
    movie= random.choice(movies_list)
    movie_length = len(movie)
    dashes = '_ '*movie_length
    print dashes
    return render(request,'hangman_main.html',{'dashes':dashes})