# from django.http import HttpResponse
# from django.contrib.auth.decorators import user_passes_test

# def is_librarian(user):
#     return user.userprofile.role == 'Librarian'

# @user_passes_test(is_librarian)
# def librarian_dashboard(request):
#     return HttpResponse("Librarian Dashboard: Only accessible to Librarians.")
