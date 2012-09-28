from notification.models import Notice


def notification(request):
    if request.user.is_authenticated():
        unseen_count = Notice.objects.unseen_count_for(request.user,
                                                       on_site=True)
        return {"notice_unseen_count": unseen_count}
    else:
        return {}
