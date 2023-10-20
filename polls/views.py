from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from .models import Question, Choice
from django.views import generic


# using generic views
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DeleteView):
    template_name = "polls/details.html"
    model = Question


class ResultView(generic.DetailView):
    template_name = "polls/results.html"
    model = Question

# F() objects assigned to model fields persist after saving the model instance and will be applied on each save(). For example:


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", {"question": question, "error_message": "You didn't select a choice"})
    else:
        # avoiding race conditions using F
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
