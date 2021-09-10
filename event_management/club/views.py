from django.views import generic
from django.views.generic.edit import CreateView
from club.models import Club
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    context_object_name = 'club_list'
    template_name = 'club/index.html'
 
    def get_queryset(self):
        return Club.objects.all()
 
# view for the product entry page
class ClubEntry(CreateView):
    model = Club
    fields = ['club_name', 'email', 'password']