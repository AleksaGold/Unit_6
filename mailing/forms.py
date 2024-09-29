from django.forms import BooleanField, ModelMultipleChoiceField


from mailing.models import MailingSettings, Message
from django import forms


class StyleFormMixin:
    """Миксин для стилизации формы"""

    pass

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for fild_name, field in self.fields.items():
    #         if isinstance(field, BooleanField):
    #             field.widget.attrs["class"] = "custom-check-input"
    #         elif isinstance(field, ModelMultipleChoiceField):
    #             field.widget.attrs["class"] = "custom-select"
    #         else:
    #             field.widget.attrs["class"] = "form-control"


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = MailingSettings
        fields = "__all__"

        widgets = {
            "start_from": forms.DateInput(attrs={"type": "datetime-local"}),
            "end_on": forms.DateInput(attrs={"type": "datetime-local"}),
            "clients": forms.CheckboxSelectMultiple,
            "next_sending": forms.HiddenInput(),
        }


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
