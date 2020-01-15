from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django import forms

from dashboard.models import Umuryango, Cell, KPI, Village


class FamilyForm(forms.ModelForm):
    name = forms.CharField(label='Uhagarariye Umuryango',
                           widget=forms.TextInput(attrs={'placeholder': 'Uhagaririrye Umuryango'}))
    number_of_member = forms.CharField(label='Umubare Wabagize Umuryango',
                                       widget=forms.TextInput(attrs={'placeholder': 'urugero: 10'}))

    class Meta:
        model = Umuryango
        fields = [
            'name',
            'number_of_member',
            'icyiciro',
            'irangamuntu',
            'kpi',
            'sector',
            'cell',
            'village']
        widgets = {
            'name': forms.TextInput(),
            'number_of_member': forms.TextInput(),
        }

    # --------------snippets for loading cells based on sector -------------#
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cell'].queryset = Cell.objects.none()

        if 'sector' in self.data:
            try:
                sector_id = int(self.data.get('sector'))
                self.fields['cell'].queryset = Cell.objects.filter(sector_id=sector_id).order_by('name')

            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields['cell'].querset = self.instance.sector.cell_set.order_by('name')

    # --------------snippets for loading cells based on sector -------------#
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['village'].queryset = Village.objects.none()

        if 'cell' in self.data:
            try:
                cell_id = int(self.data.get('cell'))
                self.fields['village'].queryset = Village.objects.filter(cell_id=cell_id).order_by('name')

            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields['village'].querset = self.instance.cell.village_set.order_by('name')


class AddKpiForm(forms.ModelForm):
    class Meta:
        model = KPI
        fields = [
            'name'
        ]


class UploadImage(forms.ModelForm):
    class Meta:
        model = Umuryango
        fields = [
            'image'
        ]
