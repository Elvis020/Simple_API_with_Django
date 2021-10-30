from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Movie


# Create your views here.
def index(request):
    all_movies = Movie.objects.all()
    # output = ', '.join([movie.title for movie in all_movies])
    return render(request,'movies/index.html',{'all_movies': all_movies})

def detail(request, movie_id):
    # Alternative 1
    # try:
    #     movie =Movie.objects.get(id=movie_id)
    #     return render(request,'movies/detail.html',{'movie':movie})
    # except Movie.DoesNotExist:
    #     raise Http404()

    # Alternative 2(preferred one)
    movie = get_object_or_404(Movie,id=movie_id)
    return render(request,'movies/detail.html',{'movie':movie})