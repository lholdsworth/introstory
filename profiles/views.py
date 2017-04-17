from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import transaction
from django.core.urlresolvers import reverse
from .models import Profile
from .forms import UserForm, ProfileForm
import math

# Home page
def index(request):
    welcome = "Oi Oi Savloy"
    return render(request, 'home.html', {'welcome':welcome})


# view profile
def view_profile(request, username):
    user = User.objects.get(username=username)
    userid = user.id

    current_user = request.user
    recommends, is_indifferent, does_not_recommend = None, None, None

    if  current_user.profile in user.profile.recommends.all():
        recommends = True

    if  current_user.profile in user.profile.is_indifferent.all():
        is_indifferent = True

    if  current_user.profile in user.profile.does_not_recommend.all():
        does_not_recommend = True

    r_count = Profile.objects.filter(recommend=user.profile).count()
    i_count = Profile.objects.filter(indifferent=user.profile).count()
    d_count = Profile.objects.filter(donotrecommend=user.profile).count()
    total_votes = r_count + d_count + i_count
    score = 0
    score = score + r_count
    score = score - d_count
    total = (total_votes +1)/3
    if score >= math.floor(total):
        rating = "recommend"
    elif score <= (math.ceil(total))*-1:
        rating = "notrecommend"
    else:
        rating = "indifferent"

    return render(request, 'profiles/view_profile.html', {
		'user': user,
        'recommends': recommends,
        'is_indifferent': is_indifferent,
        'does_not_recommend':does_not_recommend,
        'r_count':r_count,
        'i_count':i_count,
        'd_count':d_count,
        'rating':rating,
		})


# edit users profile
@login_required
@transaction.atomic
def edit_profile(request, userid):

	# check that the userid passed in the url exists
    try:   
        user = User.objects.get(id=userid)
    except User.DoesNotExist:
        return redirect('profiles:index')


    # check current user is the user we're trying to edit
    current_user = request.user
    if user == current_user:
        pass
    else:
        return redirect('profiles:index')    


    # get profile object that matches user, or create it
    userprofile = Profile.objects.get_or_create(user=user)[0]

    # create a UserForm object with the current user
    user_form = UserForm(instance=request.user)

    # create a ProfileForm object and pre-populate fields if values exists
    profile_form = ProfileForm({
        'display_name':userprofile.display_name,
        'image':userprofile.image,
        'website':userprofile.website,
        'facebook':userprofile.facebook,
        'twitter':userprofile.twitter,
        'pinterest':userprofile.pinterest,
        'instagram':userprofile.instagram,
        'phone_number':userprofile.phone_number,
        'standard_video':userprofile.standard_video,
        'vr_video':userprofile.vr_video,
        }, 
        instance=request.user.profile)

    # if a form was submitted (i.e. form update sent)
    if request.method == 'POST':
    	# create UserForm object using the submitted UserForm data
        user_form = UserForm(request.POST, instance=request.user)
        # create Profile object same as above, also getting FILES for image submitted
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        # check both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
        	# save the user form
            user_form.save()
            # save the profile form
            profile_form.save()
            # get outa here. use correct redirect to avoid user refresh/resubmission issue
            return HttpResponseRedirect(reverse('profiles:edit_profile',args=(request.user.id,)))
        else:
        	# if there were errors, WHY?!
        	print(user_form.errors)
        	print(profile_form.errors)

	# return the shiznit
    return render(request, 'profiles/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'selecteduser': user,
    })


# recommend
@login_required
def recommend(request):
    user_id = None
    success = "failed"
    current_user = request.user
    if request.method == 'GET':
        user_id = request.GET['user_id']
        if user_id:
            user = User.objects.get(id=user_id)
            if user:
                user.profile.recommends.add(current_user.profile)

                if  current_user.profile in user.profile.is_indifferent.all():
                    user.profile.is_indifferent.remove(current_user.profile)

                if  current_user.profile in user.profile.does_not_recommend.all():
                    user.profile.does_not_recommend.remove(current_user.profile)

                success = "success"
        return JsonResponse({'success':success})


# indifferent
@login_required
def indifferent(request):
    user_id = None
    success = "failed"
    current_user = request.user
    if request.method == 'GET':
        user_id = request.GET['user_id']
        if user_id:
            user = User.objects.get(id=user_id)
            if user:
                user.profile.is_indifferent.add(current_user.profile)

                if  current_user.profile in user.profile.recommends.all():
                    user.profile.recommends.remove(current_user.profile)

                if  current_user.profile in user.profile.does_not_recommend.all():
                    user.profile.does_not_recommend.remove(current_user.profile)

                success = "success"
        return JsonResponse({'success':success})


# do not recommend
@login_required
def do_not_recommend(request):
    user_id = None
    success = "failed"
    current_user = request.user
    if request.method == 'GET':
        user_id = request.GET['user_id']
        if user_id:
            user = User.objects.get(id=user_id)
            if user:
                user.profile.does_not_recommend.add(current_user.profile)

                if  current_user.profile in user.profile.recommends.all():
                    user.profile.recommends.remove(current_user.profile)

                if  current_user.profile in user.profile.is_indifferent.all():
                    user.profile.is_indifferent.remove(current_user.profile)

                success = "success"
        return JsonResponse({'success':success})