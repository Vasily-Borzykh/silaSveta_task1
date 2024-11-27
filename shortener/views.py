from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortenedURL
from .forms import URLForm
import random
import string

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def create_short_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            short_code = generate_short_code()
            while ShortenedURL.objects.filter(short_code=short_code).exists():
                short_code = generate_short_code()
            shortened_url = form.save(commit=False)
            shortened_url.short_code = short_code
            shortened_url.save()
            return redirect('shortener:link_list')
    else:
        form = URLForm()
    return render(request, 'shortener/create_short_url.html', {'form': form})

def link_list(request):
    links = ShortenedURL.objects.all()
    return render(request, 'shortener/link_list.html', {'links': links})

def redirect_short_url(request, short_code):
    shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
    return redirect(shortened_url.original_url)
