from django.shortcuts import render

# render the form and save user input to the database ourself
from .forms import UsersForm
from users_app.models import Users


# this code is for level 2 when we were creating the website database ourself
# data from a saved model instance (as in the case of admin forms for editing)

def display_users(request):

    Users_sql_var = Users.objects.order_by('lname')
    users_dict = {'users_db': Users_sql_var}
    
    return render(request, 'users_app/users.html',context=users_dict)


def user_view(request):
    users_dict = {}
    if request.method == 'POST':
    # create object of form
        form = UsersForm(request.POST)

    # model form validation is triggered implicitly
        if form.is_valid():
        # save the form data to model
        # Every ModelForm also has a save() method. This method creates 
        # and saves a database object from the data bound to the form. 
        # A subclass of ModelForm can accept an existing model instance 
        # as the keyword argument instance; if this is supplied, 
        # save() will update that instance. If it’s not supplied, 
        # save() will create a new instance of the specified model:
 
            form.save(commit=True)
            # return db page after pressing submit
            return display_users(request)
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UsersForm()

    users_dict['form'] = form
    return render(request, 'users_app/users2.html',context=users_dict)






