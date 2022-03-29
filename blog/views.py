from django.shortcuts import render
from blog.models import blog
# Create your views here.
raw_qs = blog.objects.all()[0]
def make_dict (qs,name="none"):
    curr = blog.objects.get(name_of_exam=name)

    sno=curr.s_no
    name=curr.s_no
    age=curr.s_no
    subs=curr.s_no
    sno=curr.s_no
    sno=curr.s_no
    sno=curr.s_no
    sno=curr.s_no
    sno=curr.s_no
    sno=curr.s_no
    sno=curr.s_no
    
    pass

def index(request):
    return render(request,"blog/index.html")    

def article(request):
    print(raw_qs.s_no)
    return render(request,"blog/article.html")