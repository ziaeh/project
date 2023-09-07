from django.shortcuts import render,redirect
from django.contrib import messages

def self_page(request):
    
            # msg = request.GET['msg']
            # return redirect("self-page")
    # print("접속완료 --> 선택해!")
    if request.method=="POST":
        print("선택했고")
        if 'text_sum' in request.POST:
            
            text_sum=request.POST['text_sum']
            messages.info(request, text_sum,extra_tags='summary')
            return redirect("self-page")
        elif 'text_talk' in request.POST:
            text_talk=request.POST['text_talk']
            messages.info(request, text_talk,extra_tags='talk')
            return redirect("self-page")
        # if  "msg" in request.POST:
        #     print("요약버튼 누름")
        # return redirect("self-page")
    return render(request,'news/news.html')

# Create your views here.
