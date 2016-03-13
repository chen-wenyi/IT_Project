from django.shortcuts import render
from AppRating.forms import UserForm

# Create your views here.
def index(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

# If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            # user.set_password(user.password)
            # user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    context_dict={'home':'active','user_form': user_form, 'registered': registered,}
    return render(request,'index.html',context_dict)

def editorRecommend(request):
    context_dict={'editor':'active'}
    return render(request,'index.html',context_dict)

def rankList(request):
    context_dict={'ranklist':'active'}
    return render(request,'index.html',context_dict)

def newArrival(request):
    context_dict={'newarrival':'active'}
    return render(request,'index.html',context_dict)

def categories(request):
    context_dict={'categories':'active'}
    return render(request,'index.html',context_dict)
