import base64
import datetime
import hashlib
import random
import time

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from App.forms import Add_english
from App.models import CarLogo, Rank, Idiom, Englishword,EngStu
from App.utils import Ncov

from pypinyin import pinyin

def home(request):
    return render(request, 'main/add.html')


def add(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))


def add_ajax(request, c, d):
    if request.is_ajax():
        ajax_string = 'ajax request:'
    else:
        ajax_string = 'not ajax request:'
    c = request.GET.get('c')
    d = request.GET.get('d')
    e = int(c) + int(d)

    return HttpResponse(ajax_string +str(e))

#打卡
def gy(request):
    return render(request, 'main/daka.html')

#最新ncov疫情地图
def echarts_ncov_map(request):
    nv = Ncov()
    nv.data_info()
    return render(request, 'ncov/中国地图/最新ncov疫情中国地图(%s).html'%datetime.date.today())

#新增疫情中国地图
def echarts_ncov_map_add(request):
    return render(request, 'ncov/中国地图/最新ncov疫情中国新增病例地图(%s).html'%datetime.date.today())

#最新ncov疫情折线图
def echarts_ncov_line(request):
    nv = Ncov()
    nv.china_cumulative_data()
    return render(request, 'ncov/中国地图折线图/最新ncov疫情折线图(%s).html'%datetime.date.today())

#最新ncov世界地图
def echarts_ncov_world(request):
    nv = Ncov()
    nv.foreign_ncov()
    return render(request, 'ncov/最新世界地图/最新世界ncov疫情分布图(%s).html'%datetime.date.today())

#最新世界柱状图确诊人数
def echarts_ncov_world_bar(request):

    return render(request,'ncov/最新世界地图/最新世界ncov疫情柱状图(%s).html'%datetime.date.today())
#get AJAX 请求
def get_ajax01(request):
    print(1)
    return HttpResponse('这是一个ajax请求')

@csrf_exempt
def get_ajax02(request):
    print(request.GET)
    uname = request.GET.get('uname')
    return HttpResponse('欢迎:'+ str(uname) )


def yuyue_index(request):
    return render(request,'yuyue/index.html')

@csrf_exempt
def yuyue_login(request):
    return render(request, 'yuyue/login.html')

@csrf_exempt
def chengyu_idnex(request):
    if request.method == 'POST':
        user = request.POST.get('name')
        # print(user)
        request.session['user'] = user
        request.session['round'] = 1
        return redirect(reverse('app:chengyugame'))
    rank_list = Rank.objects.all().order_by('-round_num')[:5]
    # print(rank_list)
    return render(request,'chengyu\login.html', locals())



def chengyu_name(request):
    try:
    # print(request.session.get('user'))
        if not request.session.get('user'):
            return redirect(reverse('app:chengyuindex'))
        id = random.randint(1, 45126)

        user = request.session.get('user')
        idiom = Idiom.objects.get(pk = id)
        # print(idiom.speak)
    except:
        return redirect(reverse('app:chengyugame'))
    return render(request,'chengyu\game.html', locals())




def chengyu_more(requset):
    user_idion = requset.GET.get('user_idiom')

    speak_list = pinyin(user_idion)
    # print(speak_list[-1][0])
    idiom_speak = '  '.join(map(lambda x: x[0], speak_list))
    if Idiom.objects.filter(speak=idiom_speak) and idiom_speak:
        new_idioms = Idiom.objects.filter(speak__startswith=speak_list[-1][0])
        index = len(new_idioms)
        new_idiom = new_idioms[random.randint(0,index-1)]
        print(type(new_idiom))
        print({'code': 200, 'round': requset.session.get('round'),
                             'name':new_idiom.name,'speak':new_idiom.speak,'meaning':new_idiom.meaning,
                             'example':new_idiom.example})
        requset.session['round'] = requset.session.get('round') + 1
        data = {'code': 200, 'round': requset.session.get('round'),
                             'name':new_idiom.name,'speak':new_idiom.speak,'meaning':new_idiom.meaning,
                             'example':new_idiom.example}
        return HttpResponse(data)
    else:

        data = {'code': 404, 'error': "挑战结束：用户输入的成语是自己编的吧！", 'url': 'app/chengyuindex/'}
        return HttpResponse(data)


def car_logo(request):
    try:
        id = random.randint(1,144)
        car = CarLogo.objects.get(pk=id)
        print(len(car))
        image= base64.b64decode(car['image'])
        print(image)
    except:
        pass
        # return redirect(reverse('app:car_logo'))
    return render(request,'car_logo/car_logo.html', locals())

@csrf_exempt
def english_add(request):
    if request.method == 'POST':
        add_english = Add_english(request.POST)

        if add_english.is_valid():
            word = add_english.cleaned_data['word']
            word_chinese = add_english.cleaned_data['word_chinese']
            cx = add_english.cleaned_data['cx']

            same_name_word = Englishword.objects.filter(word=word)
            if same_name_word:
                message = '单词已存在！请重新添加单词'
                return render(request, 'English/index.html', locals())
            message = "单词添加成功 ！"

            new_word = Englishword.objects.create()
            new_word.word = word
            new_word.word_chinese =word_chinese
            new_word.cixing = cx
            new_word.study_time =  datetime.date.today()
            new_word.save()

            return redirect(reverse('app:english_add'))
    add_english = Add_english()
    return render(request, 'English/index.html', locals())


def english_study(request):
    # id =  English_word.objects.all().count()
    page = int(request.GET.get('page',1))
    per_page = int(request.GET.get('per_page',10))
    # words_list = EngStu.objects.all()[per_page*(page-1) : page*per_page]

    words_list = EngStu.objects.all()
    paginator = Paginator(words_list, per_page)

    page_object = paginator.page(page)
    
    data = {
        'page_object':page_object,
        'page_range': paginator.page_range
    }
    return render(request, 'English\show.html', context= data)

