from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.utils import timezone
from django.template import RequestContext
from django.db import transaction

from darkoob.group.forms import GroupForm
from darkoob.group.models import Group
from darkoob.book.models import Quote
from darkoob.social.forms import NewPostForm
from darkoob.group.models import Post

def group(request, group_id, group_slug):
    template = 'group/group_page.html'

    group = Group.objects.get(id=group_id)
    quote = Quote.get_random_quote()
    if request.is_ajax():
        template = 'post/posts.html'

    if group and group_slug == slugify(group.name):
        group.admins = group.admin.admin_set.all()
        #group.members = group.members.all()

        is_member = False
        if group in request.user.group_set.all():
            is_member = True

        posts = Post.objects.filter(group=group).order_by("-submitted_time").all()

        # Calculate Deadlines for group
        book_deadlines = []
        for schedule in group.schedule_set.all():
            deadline_set = schedule.deadline_set.all()
            for i in range(len(deadline_set)):
                deadline_set[i].time_percentage = (timezone.now() - deadline_set[i].start_time).total_seconds()  / (deadline_set[i].end_time - deadline_set[i].start_time).total_seconds() * 100
            book_deadlines.append([ schedule.book , deadline_set])
        return render(request, template, {
            'group': group,
            'posts': posts,
            'quote': quote,
            'new_post_form': NewPostForm,
            'is_member': is_member,
            'book_deadlines': book_deadlines,
        })

    else:
        return HttpResponse("Group Is not exist!")

@login_required
@transaction.commit_manually
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if not request.user.userprofile.quote:
                group = Group(name=cd['name'], admin=request.user)
            else:
                group = Group(name=cd['name'], admin=request.user, quote=request.user.userprofile.quote)
            group.save()
            for member in cd['members'].strip(',').split(','):
                try:
                    user = User.objects.get(username=member)
                    group.members.add(user)
                except:
                    pass
            group.save()
            transaction.commit()
            groups = request.user.group_set.all()
            admin_groups = request.user.admin_set.all()
            return HttpResponseRedirect('/group/%i/%s'%(group.id,slugify(group.name)))

    else:
        transaction.rollback()
        form = GroupForm()
        groups = request.user.group_set.all()
        admin_groups = request.user.admin_set.all()
        return render(request, 'group/create_group.html', {'form': form, 'groups': groups, 'admin_groups': admin_groups })


@login_required
def members(request):
    pass

@login_required
def schedules(request):
    pass
