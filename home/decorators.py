from django.shortcuts import redirect

def check_authenticated_user(view_function):
    def logic(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(request)
        else:
            return view_function(request, *args, **kwargs)
    return logic