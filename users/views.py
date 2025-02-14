import secrets

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserManagerForm, UserProfileForm
from users.models import User


class UserCreateView(CreateView):
    """Представление для создания нового экземпляра модели User"""

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Валидация нового пользователя"""
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="MailGenius - подтверждение Email",
            message=f"Привет, {user.email}! Для окончания регистрации в MailGenius, перейди по ссылке - {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """Верификация почтового ящика нового пользователя"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Представление для просмотра списка экземпляров модели User"""

    model = User
    permission_required = "users.view_user"


class UserDetailView(LoginRequiredMixin, DetailView):
    """Представление для просмотра экземпляра модели User"""

    model = User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Представление для редактирования экземпляра модели User"""

    model = User
    form_class = UserManagerForm
    success_url = reverse_lazy("users:user_list")

    def get_form_class(self):
        """Проверяет права пользователя на редактирование формы пользователя"""
        user = self.request.user
        if user.has_perm("users.can_change_is_active") or user.is_superuser:
            return UserManagerForm
        raise PermissionDenied

    def get_success_url(self):
        """Перенаправление пользователя на страницу объекта после его редактирования"""
        return reverse("users:user_detail", args=[self.kwargs.get("pk")])


class UserProfileUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("mailing:index")

    def get_object(self, queryset=None):
        """Извлекает экземпляр модели User текущего пользователя"""
        return self.request.user
