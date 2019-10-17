from django.shortcuts import render

posts = [
    {
        'author': 'Jan Bertlik',
        'title': 'Blog post 1',
        'content': 'This is the first post',
        'date_posted': 'October 17th 2019'
    },
    {
        'author': 'Nikola Telsa',
        'title': 'Blog post 2',
        'content': 'This is the second post',
        'date_posted': 'October 18th 2019'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
