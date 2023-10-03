from django.shortcuts import render
from thumbs_up.models import intruduce


def main(request):
    intruduce_list = intruduce.objects.order_by('-likecount')[0:5]
    return render(request, 'main.html',
                {'intruduce_list': intruduce_list,})
def about(request):
    return render(request,"about.html")