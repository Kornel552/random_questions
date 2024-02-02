from .models import Topic


def add_topics_to_context(request):
    return {
        'topics': Topic.objects.all()
    }