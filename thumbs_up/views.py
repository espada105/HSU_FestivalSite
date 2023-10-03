from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import intruduce
from django.views.generic import ListView, DetailView

import json
from django.http import HttpResponse

from django.views.decorators.http import require_POST


class intruduceList(ListView):
    model = intruduce #이렇게 선언하는 동시에 get_contexxt_data에서 자동으로 post_list = Post.objects.all()을 명령함 그래서  post_list.html에서 {% for %} 명령문을 바로 쓸 쑤 있음.
    #template_name = 'board/ShowPost.html' intruduce
    ordering = '-pk'
    def get_context_data(self, **kwargs): #p326
        context = super(intruduceList, self).get_context_data()
        page = context['page_obj']
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(page.number, on_each_side=3, on_ends=0)
        context['pagelist'] = pagelist
        return context

class intruduceDetail(DetailView):
    model = intruduce
    template_name = 'Booth_info2.html'
    def get_context_data(self, **kwargs): #p326
        context = super(intruduceDetail, self).get_context_data()
        return context
    
def intruduce_lend1(request):
    intruduce_list = intruduce.objects.order_by('pk')
    return render(request, 'Booth_Info.html', {'intruduce_list': intruduce_list, })
    
    
def like_counter(request,pk):
    product = intruduce.objects.get(pk = pk)
    a = str(pk)
    try:
        #choice모델을 불러와서 1을 증가시킨다 
        # choice = Choice.objects.get(poll_id = poll.id, candidate_id = selection)
        product.likecount += 1
        product.save()
    except:
        #최초로 투표하는 경우, DB에 저장된 Choice객체가 없기 때문에 Choice를 새로 생성합니다
        product.likecount += 1
        product.save()
    return redirect('/intru/'+a+'/')

    
def like_counter2(request,pk):
    product = intruduce.objects.get(pk = pk)
    a = str(pk)
    try:
        #choice모델을 불러와서 1을 증가시킨다 
        # choice = Choice.objects.get(poll_id = poll.id, candidate_id = selection)
        product.likecount += 1
        product.save()
    except:
        #최초로 투표하는 경우, DB에 저장된 Choice객체가 없기 때문에 Choice를 새로 생성합니다
        product.likecount += 1
        product.save()
    return redirect('/intru/')



@require_POST
def video_like(request):
    pk = request.POST.get('pk', None)
    product = get_object_or_404(intruduce, pk=pk)
    product.likecount += 1
    product.save()
    context = {'likes_count':product.likecount}
    return HttpResponse(json.dumps(context), content_type="application/json")