from django.template import Context, Library, loader
from notification.models import Notice, User

register = Library()


@register.filter
def unseen_notice_count(user):
    return str(Notice.objects.unseen_count_for(user))


@register.filter
def head(list, size=5):
    return list[:size]


@register.simple_tag
def notices(user, template='notification/notices.html'):
    template = loader.get_template(template)
    notices = Notice.objects.notices_for(user, on_site=True)
    unseen = Notice.objects.notices_for(user, on_site=True, unseen=True)
    seen = Notice.objects.notices_for(user, on_site=True, unseen=False)
    return template.render(Context({
        "notices": notices,
        "unseen": unseen,
        "seen": seen,
	}))