
from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse,reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView,FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

from .models import User,Photo,Comments
from .forms import ImageUploadForm, DeleteForm, CommentForm


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispath(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self
            ).dispatch(request, *args, **kwargs)


def userlistview(request):
    context = {}
    context['users'] = User.objects.all()
    return render(request, 'userlistview.html', context)

class photolistview(ListView):

    template_name = 'photolistview.html'
    context_object_name = 'photo_list'

    def get_queryset(self):
        return Photo.objects.all().order_by('user')


class photodetailview(DetailView):

    template_name = 'photodetailview.html'
    model = Photo


# display user's photos
def userdetailview(request, user_slug):
    user = User.objects.get(slug=user_slug)
    photo_list = get_list_or_404(Photo,user=user)
    return render(request, 'userdetailview.html', {'user': user,
                                                   'photo_list':photo_list,
                                                    })
# upload photos 
def photouploadview(request, user_slug):
    user = User.objects.get(slug=user_slug)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            newimage = Photo(image=request.FILES['imagefile'],user=user, file_name=request.FILES['imagefile'])
            newimage.save()
            return HttpResponseRedirect(reverse('userdetail',kwargs = {'user_slug': user_slug}))
    else:
        form = ImageUploadForm()
    return render(request, 'photoupload.html', {'form':form,
                                                'user': user, 
                                                })
# delete photos
def photodeleteview(request, user_slug):
    user = User.objects.get(slug=user_slug)
    photos = Photo.objects.filter(user=user)

    form = DeleteForm()
    form.fields['photo_id'].choices = [(_.id, _) for _ in photos]

    if request.method == 'POST':
        lst = request.POST.getlist('photo_id')
        for p_id in lst:
            image = Photo.objects.get(id=p_id).image
            image.delete(save=True)
            Photo.objects.get(id=p_id).delete()

        return redirect('userdetail', user_slug=user_slug)
        # form = DeleteForm()
        # print form.is_valid()

        
    return render(request, 'photodeleteview.html', {'photos': photos,
                                             'form': form,
                                            })
    
# add comments
# def commentcreateview(request, photo_id):
#     photo = Photo.objects.get(id=photo_id)

#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)

#         if comment_form.is_valid():
#             comments = comment_form.cleaned_data['comments']
#             user_slug = comment_form.cleaned_data['user']
#             Comments.objects.create(user=User.objects.get(slug=user_slug), photo=photo, comment=comments)
#             return redirect('userdetail', user_slug=photo.user.slug)
#     else:
#         comment_form = CommentForm()

#     return render(request, 'comments_form.html', {'form': comment_form,
#         })

class CommentCreate(SuccessMessageMixin,CreateView):
    model = Comments
    template_name = 'comments_form.html'
    fields = ['user', 'comment', 'photo']
    success_message = '%(user)s has successful created a comment.'

    def get_initial(self):
        self.initial.update({
            'photo': self.kwargs.get('pk'),
            })
        return super(CreateView, self).get_initial()

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super(CommentCreate, self).form_valid(form)


# def comment_edit_view(request, comment_id):
#     c = Comments.objects.get(id=comment_id)
#     form = CommentForm(request.POST or None, initial={'user' :c.user.slug,
#                                                       'comments': c.comment})
#     if form.is_valid():
#         c.comment = form.cleaned_data['comments']
#         c.save()
#         return redirect('userdetail', user_slug=c.user.slug)
#     return render(request, 'commentcreateview.html', {'comment_form':form})

class CommentUpdate(SuccessMessageMixin,UpdateView):

    model = Comments
    fields = ['comment',]
    template_name = 'comments_form.html'
    success_message = '%(user)s has updated the comment.'
    def form_valid(self,form):
        orgin_comment = Comments.objects.get(photo=self.object.photo).comment
        if orgin_comment != self.object.comment:
            return super(CommentUpdate, self).form_valid(form)
        else:
            return HttpResponseRedirect(self.object.get_absolute_url())
    def get_success_message(self, cleaned_data):
        return self.success_message % dict (
            cleaned_data,
            user=self.object.user
                       )

class CommentDelete(DeleteView):

    model = Comments
    template_name = 'comments_confirm_delete.html'

    def get_success_url(self):
        print dir(self)
        user = self.object.photo.user
        return  reverse_lazy('userdetail',kwargs = {'user_slug': user.slug})

class CommentThread(FormView, DetailView):
    model = Comments
    context_object_name = 'comment'
    template_name = 'commentsthread.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(CommentThread, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context 

    def get_queryset(self):
        return Comments.objects.filter(pk=self.kwargs.get('pk'))


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            parent_id = request.POST.get('parent_id')
            parent_comment = Comments.objects.get(id=parent_id)
            comment_text = form.cleaned_data['comments']
            user = form.cleaned_data['user']
            Comments.objects.create(
                user=User.objects.get(slug=user),
                comment=comment_text,
                photo=parent_comment.photo,
                parent=parent_comment)

        return FormView.post(self, request, *args, **kwargs)


    def get_success_url(self):
        return reverse_lazy('commentthread',kwargs = {'pk': self.kwargs.get('pk')})
