from django.http import Http404


class CompanyFilterMixin:
    def get_queryset(self):
        user_company = self.request.user.company
        return super().get_queryset().filter(company=user_company)


class CompanyObjectMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.company != self.request.user.company:
            raise Http404("You do not have permission to access this inventory item.")
        return obj


class CompanyCreateMixin:
    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)
