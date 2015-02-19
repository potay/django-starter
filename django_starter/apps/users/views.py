from django.utils import timezone
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from models import Profile

# Create your views here.
def home(request):
  return render(request, 'base.html')
