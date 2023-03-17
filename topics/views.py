from django.shortcuts import get_object_or_404, render
from .models import Video, Topic, Sub_Topic
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    topics = Topic.objects.order_by('-create_date')

    context = {
        'topics': topics
    }
    return render(request, 'topics/topics.html', context=context)


@login_required(login_url='login')
def topic(request, topic_id):
    objs = get_object_or_404(Topic, pk=topic_id)
    topics = Sub_Topic.objects.order_by('-create_date')
    context = {
        'topics': topics,
        'objs': objs
    }
    return render(request, 'topics/topic.html', context=context)


@login_required(login_url='login')
def video(request):
    return render(request, 'topics/video.html')
