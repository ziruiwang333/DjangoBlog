from turtle import forward
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Education
from .models import Work_Experience
from .models import *

# Create your views here.

def index(request):
    top_post = Post.objects.order_by('-total_views').first()
    most_recent = Post.objects.order_by('-published_date').first()
    return render(request, 'blog/index.html', {'top_post':top_post, 'most_recent':most_recent})
    
def introduction(request):
    educations = Education.objects.all().order_by('-id')
    print(educations)
    courses = Course.objects.all()
    work_experience = Work_Experience.objects.all()
    details = MyDetail.objects.first()

    uob_year1 = []
    uob_year2 = []
    uob_year3 = []
    uom_year1 = []

    for course in courses:
        if(course.university.university == 'University of Birmingham'):
            if(course.year == 1):
                uob_year1.append(course.course_name)
            if(course.year == 2):
                uob_year2.append(course.course_name)
            if(course.year == 3):
                uob_year3.append(course.course_name)
        elif(course.university.university == 'The University of Manchester'):
            uom_year1.append(course.course_name)

    forward_dict = {'educations':educations, 
    'work_experience':work_experience, 
    'uob':[uob_year1, uob_year2, uob_year3],
    'uom':[uom_year1],
    'courses':courses,
    'details':details,
    }
    return render(request, 'blog/introduction.html', forward_dict)
    
def daily(request):
    albums = Gallery.objects.all()
    return render(request, 'blog/daily.html', {'albums':albums})
    
def daily_detail(request, pk, album_name):
    album = get_object_or_404(Gallery, pk=pk)
    photos = Photos.objects.filter(album_name=pk)
    return render(request, 'blog/daily_detail.html',{'album':album, 'photos':photos})
    
def photo(request, pk):
    photoPK = Photos.objects.get(pk=pk)
    return render(request, 'blog/photo.html', {'photoPK':photoPK})

def posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts':posts})
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.total_views += 1
    post.save(update_fields=['total_views'])
    return render(request, 'blog/post_detail.html',{'post':post})
