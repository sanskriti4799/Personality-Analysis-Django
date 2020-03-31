from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Quest
from django.http import HttpResponse
#from .models import Author
from django.core.mail import send_mail,EmailMessage
from django.conf import  settings
import matplotlib.pyplot as mp
import io
from django import forms


scores =[]


# Create your views here.
def signup(req):
    if req.method=='POST':
    
        new_user=User.objects.create_user(
            username=req.POST.get('username'),
            first_name=req.POST.get('fname'),
            last_name=req.POST.get('lname'),
            email=req.POST.get('email'),
            password=req.POST.get('password')

        )
        return redirect('home:login')
    else:
        return render(req,'home/signup.html')



def loginUser(req):
    if req.method=='POST':

        user=authenticate(
            username=req.POST.get('username'),
            password=req.POST.get('password')
            
        )
        if user:
            login(req,user)
            return render(req,'home/home.html')
        else:
            return HttpResponse('Invalid Credentials!')

    else:
        return render(req,'home/login.html')
 
@login_required
def questionnare(req):
    if req.method=='POST':
        new_post=Quest(
            qid=req.POST.get('qid'),
            question=req.POST.get('question'),
            a=req.POST.get('a'),
            b=req.POST.get('b'),
            c=req.POST.get('c'),
            d=req.POST.get('d'),
            aw=req.POST.get('aw'),
            bw=req.POST.get('bw'),
            cw=req.POST.get('cw'),
            dw=req.POST.get('dw'),
            domain=req.POST.get('domain'),

            posted_by=req.user
        )
        new_post.save()
        return HttpResponse("Post Added sucessfully")
    else:
        return render(req,'home/post.html',{'data':'random data'})

@login_required
def logoutUser(req):
    logout(req)
    return redirect('home:login')

def index(req):
   # post = Post.objects.get(id=1)
    
    q = Quest.objects.all()
    return render(req,'home/index.html',{'q':q})

def home(req):
    return render(req,'home/home.html')


def confidence(req):
   # post = Post.objects.get(id=1)
    if req.method == "POST":
        que_ans = req.POST.dict()
        del que_ans['csrfmiddlewaretoken']
        print(que_ans)
        return HttpResponse("form submitted !")
    else:       
        q = Quest.objects.filter(domain='co')
        return render(req,'home/confidence.html',{'q':q})

def academics(req):
   # post = Post.objects.get(id=1)
    if req.method == "POST":
        que_ans = req.POST.dict()
        del que_ans['csrfmiddlewaretoken']
        print(que_ans)
        return HttpResponse("form submitted !")
    else:       
        q = Quest.objects.filter(domain='ac')
        
        return render(req,'home/academics.html',{'q':q})


def fitness(req):
   # post = Post.objects.get(id=1)
    if req.method == "POST":
        que_ans = req.POST.dict()
        del que_ans['csrfmiddlewaretoken']
        print(que_ans)
        return HttpResponse("form submitted !")
    else:       
        q = Quest.objects.filter(domain='fi')
        return render(req,'home/fitness.html',{'q':q})


def personality_development(req):
   # post = Post.objects.get(id=1)
    if req.method == "POST":
        que_ans = req.POST.dict()
        del que_ans['csrfmiddlewaretoken']
        print(que_ans)
        return HttpResponse("form submitted !")
    else:       
        q = Quest.objects.filter(domain='pd')
        return render(req,'home/personality.html',{'q':q})


def Attempt(req):
    score=0
    if req.method == "POST":
        que_ans = req.POST.dict()
        for qid,ans in que_ans.items():
            obj=Quest.objects.get(id = qid)
            if(ans=='a'):
                score+= obj.aw
            elif(ans=='b'):
                score+= obj.bw
            elif(ans=='c'):
                score+= obj.cw
            else:
                score+= obj.dw
        print(score)
    else:       
        q = Quest.objects.filter(domain='co')
        return render(req,'home/communication.html',{'q':q})

def addon(req):
    return render(req,'home/addon.html')
    
def feedback(req):
    return render(req,'home/feedback.html')
def report(req):
    return render(req,'home/report.html')

def certificate(req):
    return render(req,'home/certificate.html')

def display():
    print("====================")
    print([round(x/7 , 2) for x in scores])



def getvalues(req):
    if req.method=='POST':
        sum=int(req.POST.get('mainsum'))
        scores.append(sum)
        display()
        return HttpResponse(sum)
    return HttpResponse('hi')



def barg(req):
    if req.method=='POST':
        print('hello')
    else:
        domain =['Confidence','Fitness','Academics','Personal_Devel']
        values=[70,60,85,45]
        fig = mp.figure()
        fig.patch.set_facecolor("gray")
        graph1 = fig.add_subplot(1, 1, 1)
        graph1.bar(domain, values, color="blue", label="Bar")
        graph1.set_ylabel("Score", color="green")
        graph1.set_xlabel("Type of form", color="green")
        graph1.set_title("Your score in different domain", color="red")
        graph1.autoscale(enable=True, axis='both', tight=False)
        graph1.grid(True)
        buf = io.BytesIO()
        mp.savefig(buf, format='png')
        mp.show()
        mp.close(fig)
        print(buf.getvalue())
        return HttpResponse(buf.getvalue(), content_type='image/png')
        #return HttpResponse('hi')
       
