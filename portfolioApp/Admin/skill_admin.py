from django.contrib import admin
from django import forms
from ..models import Skill

class SkillAdminForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. ReactJs'
            }),
            'percent': forms.NumberInput(attrs={
                'type': 'range',
                'min': '0',
                'max': '100',
                'step': '1',
                'oninput': 'document.getElementById("percent-value").innerText = this.value + "%"'
            })
        }

    class Media:
        js = ('admin/js/skill_slider.js',)


class SkillAdmin(admin.ModelAdmin):
    form = SkillAdminForm
