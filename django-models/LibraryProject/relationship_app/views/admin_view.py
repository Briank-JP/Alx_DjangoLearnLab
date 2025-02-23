from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_dashboard(request):
    return HttpResponse("Admin Dashboard: Only accessible to Admins.")
