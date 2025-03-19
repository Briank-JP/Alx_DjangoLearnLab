from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# class based vies for crud operations
from django.views.generic import ListView,CreateView,DeleteView, DetailView, UpdateView
from.models import Post


# Create your views here.
class RegisterVeiw(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name ='blog/register.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
# create a view to handle user profile updates

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
        
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'blog/profile.html', {'user_form': user_form, 'profile_form': profile_form})

# creating classbased vies to handle all crud operations

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date'] # this one orders the post in decending order from the newest to the oldest using the -
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    # Assign a logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign logged-in user as author
        return super().form_valid(form)
    
    success_url = reverse_lazy('posts_home') 
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # Assign a logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign logged-in user as author
        return super().form_valid(form)
    success_url = reverse_lazy('posts_home') 
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts_home')
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False