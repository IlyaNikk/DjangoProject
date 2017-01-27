from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ask.models import Profile, Question, Answer, Tags_Question
from django.contrib.auth.models import User
from django.http import Http404
from ask.forms import UserForm,SignUpForm, QuestionForm, AnswerForm
import datetime
import random
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    questions_list = [ ]
    questions_list = Question.objects.new()

    current_page = listing(questions_list,request)
    return render(request, 'question.html', {
        'questions' : current_page['page'],
        'contacts' : current_page['contact'],
        'pages' : current_page['pages'],
        'current' : int(current_page['current']),
    })

def signup(request):
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            this_username = form.cleaned_data.get('username')
            this_password = form.cleaned_data.get('password')
            user = auth.authenticate(username = this_username, password = this_password)
            if user is not None:
                auth.login(request, user)
                next = form.cleaned_data.get('url_to_redirect')
                return redirect(str(next))
            else:
                return render(request, 'formsignup.html', {
                        'form' : form,
                        'login_error' : True,
                })
    else :
        url = request.GET.get('next', '/')
        form = SignUpForm ( initial = {
            'url_to_redirect' : url
        })
        print (url)
    return render(request, 'formsignup.html', {
        'form' : form,
    })

def logout(request):
    auth.logout(request)
    return redirect('/')


def question_answer(request):
    q_id = request.GET.get('id')
    try:
        question = Question.objects.get(pk = q_id)
    except Question.DoesNotExist:
        raise Http404
    answer_list = [ ]
    answer_list = Answer.objects.filter(question_id = q_id)
    current_page = listing(answer_list,request)
    form = AnswerForm()
    return render(request, 'answer_form.html',{
        'answers' : current_page['paginator'],
        'question' : question,
        'contacts' : current_page['contact'],
        'pages' : current_page['pages'],
        'current' : int(current_page['current']),
        'question_id' : int(q_id),
        'form': form,
    })

@login_required
def new_question(request):
    if request.POST:
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = Question(
                profile = request.user,
                question_title = form.cleaned_data.get('question_title'),
                question_text = form.cleaned_data.get('question_text'),
                question_num_answers = 0,
                question_rank = 0,
            )
            q.save()
            for tag in form.cleaned_data['question_tag'].replace(' ', '' ).split(','):
                check_tag = Tags_Question.objects.filter(tag_question = tag)
                if check_tag != tag:
                    new_tag= Tags_Question(
                        tag_question = tag
                    )
                    new_tag.save()
                    q.question_tag.add(new_tag)
                else:
                    q.question_tag.add(check_tag)
                    id_redirect = str(q.id)
            return redirect('/question/?id=' + str(q.id))
        else:
            return render(request, 'question_form.html',{
                'form' : form,
            })
    else:
        form = QuestionForm()
    return render(request, 'question_form.html',{
        'form' : form,
    })

def add_answer(request):
    q_id = request.GET.get('id')
    question = Question.objects.get(pk = q_id)
    answer_list = [ ]
    answer_list = Answer.objects.filter(question_id = q_id)
    current_page = listing(answer_list,request)
    if request.POST:
        form = AnswerForm(request.POST)
        if form.is_valid():
            a = Answer(
                question = question,
                profile = request.user,
                answer_text = form.cleaned_data.get('text'),
                answer_rank = 0,
            )
            a.save()
            answer_list = Answer.objects.filter(question_id = q_id)
            current_page = listing(answer_list,request)
            return redirect('/question/?id=' + str(question.id) + '&page=' + str(current_page['num_pages']) +  '#' + str(a.id))
    else:
        form = AnswerForm()
    return render(request, 'answer_form.html',{
        'answers' : current_page['paginator'],
        'question' : question,
        'contacts' : current_page['contact'],
        'pages' : current_page['pages'],
        'current' : int(current_page['current']),
        'question_id' : int(q_id),
        'form': form,
    })


def registr(request):
    if request.POST:
        print('OK')
        form = UserForm(request.POST)
        if form.is_valid():
            print('OK')
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            if User.objects.filter(email = email):
                return render(request,'registartion_form.html', {
                    'form' : form,
                    'email_error' : True,
                })
            if User.objects.filter(username = username):
                return render(request,'registartion_form.html', {
                    'form' : form,
                    'username_error' : True,
                })
            if password == repeat_password:
                u = User.objects.create_user(
                    username = username,
                    first_name = first_name,
                    last_name = last_name,
                    password = password,
                    email = email,
                    last_login = datetime.datetime(2015 , 4, 29, 15, 59),
                )
                user = auth.authenticate(username = username, password = password)
                auth.login(request, user)
                redir = form.cleaned_data.get('url_to_redirect')
                return redirect(str(redir))
            else:
               return render(request,'registartion_form.html', {
                    'form' : form,
                    'password_error' : True,
                })
        else:
             import pprint
             pprint.pprint(form.errors)
             return render(request,'registartion_form.html', {
                'form' : form,
             })
    else:
        url = request.GET.get('next', '/')
        form = UserForm( initial = {
            'url_to_redirect' : url
        })
        print (url)
    return render(request,'registartion_form.html', {
        'form' : form,
    })


def noauto(request):
    questions_list = [ ]
    questions_list = Question.objects.new()
    current_page = listing(questions_list,request)
    return render(request, 'question.html', {
        'questions' : current_page['paginator'],
        'contacts' : current_page['contact'],
        'current' : int(current_page['current']),
        'pages' : current_page['pages'],
    })

def tagsearch(request):
    try:
        tags = str(request.GET.get('tag'))
    except ValueError:
        raise  Http404
    questions_list = []
    questions_list = Question.objects.getbytag(tags)
    current_page = listing(questions_list,request)
    return render(request, 'question.html', {
        'questions' : current_page['paginator'],
        'contacts' : current_page['contact'],
        'current' : int(current_page['current']),
        'pages' : current_page['pages'],
        'tag' : tags,
    })

def listing(list,request):
    paginator = Paginator(list, 5) # Show 5 contacts per page
    pages = [ ]
    try:
        page = request.GET.get('page')
        contact = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contact = paginator.page(1)
        page = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contact = paginator.page(paginator.num_pages)
    except ValueError:
        contact = paginator.page(1)
        page = 1

    for i in range (-2,3):
        if(int(page) + int(i) > 0 and int(page) + int(i) <= paginator.num_pages):
            pages.append(int(page) + int(i))


    return {
        'contact': contact,
        'paginator' : paginator,
        'current' : page,
        'pages' : pages,
        'num_pages' : int(paginator.num_pages),
    }