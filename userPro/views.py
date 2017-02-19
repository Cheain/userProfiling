from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homePage(request):
    m={}
    m['title']='首页'
    return render(request, 'homePage.html',m)

def search(request):
    m={}
    m['title']='搜索'
    return render(request,'search.html')

def searchResult(request):
    searchs={}
    if request.GET.get('q'):
        q = request.GET.get('q')
        # movies = movie.objects.filter(name__icontains=q)
        # searchs = searchResult(request, movies)
        searchs['title'] = '搜索“%s”' % q
        searchs['qTag']=True
        searchs['q'] = q

        searchs['name'] = '会飞的猪'
        searchs['icon'] = '/static/userPro/img/u1.png'
        searchs['tag'] = ['服装', '时尚']
    else:
        searchs['title']='搜索出错'
        searchs['qTag']=False
        searchs['msg']='搜索关键字不能为空'
    return render(request, 'searchResult.html', searchs)

def userPage(request,userID):
    # SQL

    userInfo={}
    userInfo['userID']=userID
    userInfo['title'] = '用户%s'%userID

    userInfo['name']='会飞的猪'
    userInfo['icon']='/static/userPro/img/u1.png'
    userInfo['about'] = '小白菜'
    userInfo['tag'] = ['服装','时尚']

    return render(request,'userPage.html',userInfo)


def propertyPage(request,property):
    propertyInfo={}
    propertyInfo['title']=property
    propertyInfo['property'] = property
    propertyInfo['keyWord']=[1,2,3,4]


    return render(request,'propertyPage.html',propertyInfo)


from .forms import AddForm
def test(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            #return render(request,'1.html',{'a':a,'b':b})
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = AddForm()
    return render(request, '1.html', {'form': form})
    #return render(request,'base.html')

