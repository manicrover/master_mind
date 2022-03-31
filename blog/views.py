from ast import Param
from django.shortcuts import render
from blog.models import blog
# Create your views here.
raw_qs = blog.objects.all()[0]


def make_dict( name="none"):
    curr = blog.objects.get(name_of_exam=name)
    qs_dict={}
    qs_dict['sno']= curr.s_no
    qs_dict['name'] = curr.name_of_exam
    qs_dict['age'] = curr.age_limit
    qs_dict['subs'] = curr.required_subjects
    qs_dict['p_criteria'] = curr.percentage_crietria
    qs_dict['study_mno'] = curr.suggested_study_material
    qs_dict['cut_off'] = curr.cut_off
    qs_dict['details'] = curr.more_details
    qs_dict['official'] = curr.official_website
    qs_dict['registeration'] = curr.registration_link
    qs_dict['source'] = curr.source

    return qs_dict


def index(request):
    raw_qs = blog.objects.all()
    params = {}
    names = []
    pipelines = []
    for i in raw_qs:
        names.append(i.name_of_exam)
        pipelines.append("")

    params['names']=names
    params['urls']=pipelines

    # temp code 
    # params = {}
    # raw_qs = blog.objects.all()


    # tce
    return render(request, "blog/index.html", params)


def article(request):
    params = make_dict(name="JEE(mains)")
    # print(params)
    return render(request, "blog/article.html",params)

def neet(request):
    params = make_dict(name="NEET")
    print(len(params))
    return render(request, "blog/article.html",params)
