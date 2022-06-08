from .models import Link


def social_list(request):
    return {
        'SOCIAL_LIST': Link.objects.all()
    }
