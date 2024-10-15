from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Question
from .forms import QuestionForm, TopicForm
from django.http import HttpResponseRedirect
import random


def base(request):
    topics = Topic.objects.all()
    return render(request, 'base.html', {'topics':topics})


def home(request):
    topics = Topic.objects.all()
    if request.method=='POST':
        topic_form = TopicForm(request.POST)
        if topic_form.is_valid():
            topic_form.save()
            return redirect('')
    else:
        topic_form = TopicForm()
    context = {
        'topics':topics,
        'topic_form':topic_form
    }
    return render(request, 'home.html', context)


def edit(request, item_id):
    topic = get_object_or_404(Topic, pk=item_id)
    questions = Question.objects.filter(key_id=topic.id)
    name = Topic.objects.filter(pk=item_id)

    if request.method == 'POST':
        changeform = TopicForm(request.POST, instance=topic)
        if changeform.is_valid():
            changeform.save()
            return redirect('edit', item_id=item_id)
    else:
        changeform = TopicForm(instance=topic)

    if request.method == 'POST':
        if 'delete_question' in request.POST:  # Logika usuwania
            question_id = request.POST.get('delete_question')
            question = get_object_or_404(Question, pk=question_id)
            question.delete()
            return HttpResponseRedirect(request.path_info)  # Odświeżenie strony

        else:  # Logika dodawania/pytania
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.key = topic
                question.save()
                return redirect('edit', item_id=item_id)
    else:
        form = QuestionForm()

    context = {
        'form': form,
        'item': topic,
        'questions': questions,
        'name': name,
        'changeform': changeform
    }
    return render(request, 'edit.html', context)


def delete(request):
    posts = Topic.objects.all()
    if request.method=='POST':
        post_id = request.POST.get('post_id')
        Topic.objects.filter(id=post_id).delete()
    return render(request, 'delete.html', {'posts': posts})


def random_question_view(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    questions = Question.objects.filter(key=topic)
    last_question_id = request.session.get('last_question_id')

    # Sprawdzenie, czy jest tylko jeden wpis
    if len(questions) == 1:
        selected_question = questions[0]
    else:
        questions = [q for q in questions if q.id != last_question_id]

        if questions:
            selected_question = random.choice(questions)
            request.session['last_question_id'] = selected_question.id
        else:
            # Wiadomość o braku pytań lub przekierowanie gdzie indziej
            return render(request, 'random.html', {'message': 'Brak pytań dla tego tematu.'})

    return render(request, 'random.html', {'question': selected_question, 'topic': topic})


def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    questions = Question.objects.filter(key=topic)
    context = {
        'topic': topic,
        'questions':questions,
    }

    return render(request, 'topic.html', context)


def edit_question(request, topic_id, question_id):
    question = get_object_or_404(Question, pk=question_id, key_id=topic_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('edit', item_id=topic_id)  # Assuming 'edit' is the name of the view to go back to
    else:
        form = QuestionForm(instance=question)

    context = {
        'form': form,
        'question': question,
    }
    return render(request, 'edit_question.html', context)