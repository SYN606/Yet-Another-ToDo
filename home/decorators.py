from django.shortcuts import redirect


def check_authenticated_user(view_func):
    """
    Redirects an already authenticated user away from login/register pages.
    """

    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("homepage")
        return view_func(request, *args, **kwargs)

    return wrapper
