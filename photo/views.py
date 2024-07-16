from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Photo

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id  # 'instace'를 'instance'로 수정
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

@login_required
def photo_list(request):

class PhotoUploadView(LoginRequiredMixin, CreateView):

class PhotoDeleteView(LoginRequiredMixin, DeleteView):

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
