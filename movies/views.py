from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from movies.models import Movie


def index(request):
    movies = Movie.objects.all()
    output = ', '.join([m.title for m in movies])
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    try:
        movie = get_object_or_404(Movie, pk=movie_id)
        return render(request, 'movies/detail.html', {'movie': movie})
    except Movie.DoesNotExist:
        raise Http404()
