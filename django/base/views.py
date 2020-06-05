from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from base.models import CardData
from base.forms import CardForm
from base.forms import MarkFound


def main(request):
    """
    Returns main page with links to index and form submission.
    """
    return render(request, "base/main.html", {})

class IndexView(generic.ListView):
    """
    Index using generic views.
    """
    template_name = "base/index.html"
    context_object_name = "card_data_list"

    def get_queryset(self):
        """
        Returns list of card objects ordered by name
        """
        return CardData.objects.order_by("name").filter(active=True)

def form(request):
    """
    Returms form if a GET request is sent and inputs data
    if POST is submit.
    """
    if request.method == "POST":
        card_form = CardForm(request.POST, request.FILES)
        if card_form.is_valid():
            email = card_form.cleaned_data["email"]
            name = card_form.cleaned_data["name"]
            id_number = card_form.cleaned_data["id_number"]
            picture = card_form.cleaned_data["picture"]
            passphrase = card_form.cleaned_data["password"]
            card = CardData(name=name, id_number=id_number, picture=picture, email=email, passphrase=passphrase) 
            card.save()
            return HttpResponseRedirect(reverse("success"))

    else:
        card_form = CardForm()
    return render(request, "base/form.html", {"card_form" : card_form})

def success(request):
    """
    View returned if submission is successful.
    """
    return render(request, "base/success.html", {})

class DetailView(generic.DetailView):
    """
    Generic for detail view for card data.
    """
    model = CardData
    template_name = "base/detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        mark_found = MarkFound()
        context["found_form"] = mark_found 
        return context

def found(request, card_id):
    """
    Marks card as found so it will no longer appear in index.
    """
    card_data = CardData.objects.filter(id=card_id)[0]
    found_form = MarkFound(request.POST)
    if not found_form.is_valid():
        return HttpResponseRedirect(reverse("password_incorrect", args=[card_id]))
    password = found_form.cleaned_data["password"]
    success = card_data.mark_found(password)
    if success:
        return HttpResponseRedirect(reverse("password_correct", args=[card_id]))
    return HttpResponseRedirect(reverse("password_incorrect", args=[card_id]))

def password_correct(request, card_id):
    """
    Displays confirmation that card is no longer active.
    """
    return render(request, "base/correct.html", {})


def password_incorrect(request, card_id):
    """
    Displays confirmation that card is no longer active.
    """
    return render(request, "base/incorrect.html", {"card_id" : card_id})

