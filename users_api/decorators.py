from functools import wraps

def client_only(view):
    @wraps(view)
    def wrapped_view(request, *args, **kwargs):
        if request.user.role != 2:
            return False
        return True
    return wrapped_view

def employee_only(view):
    @wraps(view)
    def wrapped_view(request, *args, **kwargs):
        if request.user.role != 2:
            return False
        return True
    return wrapped_view