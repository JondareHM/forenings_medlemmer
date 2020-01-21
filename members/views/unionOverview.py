from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from members.utils.user import user_to_person, has_user


@login_required
@user_passes_test(has_user, "/admin_signup/")
def unionOverview(request):
    union = admin_user_information.union
    members = union.members()
    return render(request, "admin/unionOverview.html", members)
