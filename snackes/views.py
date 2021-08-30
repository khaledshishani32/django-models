from django.db import models
from django.views.generic import ListView
from .models import Snack

# Create your views here.

class SnackListView(ListView):
    templet_name = 'snack_detail.html'
    
    model = Snack