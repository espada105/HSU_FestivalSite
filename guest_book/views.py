from django.shortcuts import render, redirect
from .models import Comments

def index(request):
    if request.method == 'GET':
        comments = Comments.objects.all().order_by('-created')
        print(comments)
        return render(request, 'comments.html', {'comments': comments})
    elif request.method == 'POST':
        nickname = request.POST['nickname']
        comment = request.POST['comment']
        Comments(comment=comment, nickname=nickname).save()
        return redirect('comments')
