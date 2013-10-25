from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Person


class PersonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-person-form"
        self.helper.form_method = 'post'
        self.helper.form_action = 'home'

        self.helper.add_input(Submit('submit', _('Submit')))

    class Meta:
        model = Person
