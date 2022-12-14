from django.shortcuts import render, redirect
from .models import Profile
from .forms import ShweetForm

# Create your views here.

def dashboard(request):
    """
    The default view page that lists the user's shweets
    and those of the followers
    """
    form = ShweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            shweet = form.save(commit=False)
            shweet.user = request.user
            shweet.save()
            return redirect("shwitterApp:dashboard")
    return render(request, "shwitter/dashboard.html", {"form": form})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "shwitter/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "shwitter/profile.html", {"profile": profile})
