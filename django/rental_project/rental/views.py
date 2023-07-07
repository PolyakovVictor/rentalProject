from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model

from .forms import CreateGroupForm
from .utils import (
    get_apartment_data,
    get_apartment_data_by_id,
    get_group_data_by_user_id,
    get_group_data_by_id,
    get_group_data_by_apartment_id,
    create_group,
    get_users_by_group_id,
    add_user_to_group,
    leave_from_group as leave_from_group_util,
    delete_group
)


def explore_page_view(request):
    apartment_data = get_apartment_data()
    context = {'apartment_data': apartment_data}
    return render(request, 'rental/explore.html', context)


def home_page_view(request):
    return render(request, 'rental/home.html')


def host_page_view(request):
    return render(request, 'rental/host.html')


def product_page_view(request, apartment_id):
    apartment_data = get_apartment_data_by_id(apartment_id)
    groups_data = get_group_data_by_apartment_id(apartment_id)
    context = {'apartment_data': apartment_data, 'groups_data': groups_data}
    return render(request, 'rental/product.html', context)


def group_page_view(request, group_id):
    group_data = get_group_data_by_id(group_id)
    group_users = [get_user_model().objects.get(id=user_id) for user_id in get_users_by_group_id(group_id)]
    context = {'group': group_data, 'group_users': group_users}
    return render(request, 'rental/group.html', context)


def user_groups_page_view(request):
    user = request.user
    group_data = get_group_data_by_user_id(user.id)
    context = {'group_data': group_data}
    return render(request, 'rental/groups.html', context)


def leave_from_group(request, group_id: int):
    leave_from_group_util(request.user.id, group_id)
    if len(get_users_by_group_id(group_id)) == 0:
        delete_group(group_id)
    return redirect('/')


def join_to_group(request, group_id: int):
    add_user_to_group(request.user.id, group_id)
    return redirect(f'/group/{group_id}')


class CreateGroup(View):
    template_name = "rental/create_group.html"

    def get(self, request, apartment_id):
        context = {
            'form': CreateGroupForm(),
            'aid': apartment_id
        }
        return render(request, self.template_name, context)

    def post(self, request, apartment_id):
        form = CreateGroupForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            settlers_limit = form.cleaned_data.get('settlers_limit')
            start_of_lease = form.cleaned_data.get('start_of_lease')
            end_of_lease = form.cleaned_data.get('end_of_lease')

            group_id = create_group(apartment_id,
                                    title,
                                    description,
                                    settlers_limit,
                                    start_of_lease,
                                    end_of_lease
                                    )
            user = request.user
            add_user_to_group(user.id, group_id.get('id'))
            return redirect(f"/product/{apartment_id}")
        context = {
            "form": form
        }
        return render(request, self.template_name, context)
