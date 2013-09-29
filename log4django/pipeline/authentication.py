

def is_logged(request):
    return request.user.is_authenticated()