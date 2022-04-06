from django.contrib.auth.mixins import UserPassesTestMixin

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True#制限に引っかかった場合に例外発生するように

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk']
