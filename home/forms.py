from django import forms
from .models import Todo
from django_ckeditor_5.widgets import CKEditor5Widget


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ["title", "description", "completed"]
        widgets = {
            "title":
            forms.TextInput(
                attrs={
                    "class":
                    "w-full rounded-lg border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-200 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2",
                    "placeholder": "Enter Todo Title",
                }),
            "description":
            CKEditor5Widget(config_name="extends"),
            "completed":
            forms.CheckboxInput(
                attrs={
                    "class":
                    "h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
                }),
        }
