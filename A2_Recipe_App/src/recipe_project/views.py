from django.shortcuts import render, redirect
import logging

# Django authentication libraries
from django.contrib.auth import authenticate, login, logout

# Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm

logger = logging.getLogger(__name__)

# define a function view called login_view that takes a request from user
def login_view(request):
    # initialize:
    # error_message to None
    error_message = None
    # form object with username and password fields
    form = AuthenticationForm()

    # when user hits "login" button, then POST request is generated
    if request.method == 'POST':
        # read the data sent by the form via POST request
        form = AuthenticationForm(request=request, data=request.POST)

        # check if form is valid
        if form.is_valid():
            username = form.cleaned_data.get('username')  # read username
            password = form.cleaned_data.get('password')  # read password

            logger.info(f"Login attempt for user: {username}")
            
            # use Django authenticate function to validate the user
            user = authenticate(username=username, password=password)
            if user is not None:  # if user is authenticated
                logger.info(f"Authentication successful for user: {username}")
                # then use pre-defined Django function to login
                login(request, user)
                return redirect('recipes:list')  # & send the user to desired page
            else:
                logger.warning(f"Authentication failed for user: {username}")
                error_message = 'Invalid username or password'
        else:  # in case of error
            logger.error(f"Form validation failed. Errors: {form.errors}")
            error_message = f'Form error: {form.errors}'  # print error message

    # prepare data to send from view to template
    context = {
        'form': form,  # send the form data
        'error_message': error_message  # and the error_message
    }
    # load the login page using "context" information
    return render(request, 'auth/login.html', context)


# define a function view called logout_view that takes a request from user
def logout_view(request):
    logout(request)  # the use pre-defined Django function to logout
    return redirect('logout-success')  # after logging out go to success page
