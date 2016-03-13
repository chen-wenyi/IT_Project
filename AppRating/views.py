from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'home':'active',}
    return render(request,'index.html',context_dict)

def editorRecommend(request):
    context_dict={'editor':'active'}
    return render(request,'index.html',context_dict)

def rankList(request):
    context_dict={'ranklist':'active'}
    return render(request,'index.html',context_dict)

def newArrival(request):
    context_dict={'newarrival':'active'}
    return render(request,'index.html',context_dict)

def categories(request):
    context_dict={'categories':'active'}
    return render(request,'index.html',context_dict)



