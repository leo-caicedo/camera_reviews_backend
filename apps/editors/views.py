# Django
from django.shortcuts import render


def main(request):
    context = {
        'name': 'leo'
    }

    return render(request, 'editors/base.html', context)
