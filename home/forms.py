from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:

        model = Todo

        fields = [
            "title",
            "description",
            "completed",
        ]

        widgets = {

            # Title
            "title":
            forms.TextInput(
                attrs={
                    "class": ("w-full rounded-2xl border border-zinc-200 "
                              "bg-white/60 px-4 py-3 text-sm text-zinc-900 "
                              "outline-none transition "
                              "focus:border-primary focus:ring-2 "
                              "focus:ring-primary/20 "
                              "dark:border-zinc-700 "
                              "dark:bg-zinc-950/40 "
                              "dark:text-zinc-100"),
                    "placeholder":
                    "Enter todo title...",
                    "autocomplete":
                    "off",
                }),

            # Description
            "description":
            CKEditor5Widget(
                config_name="extends",
                attrs={
                    "class": "django_ckeditor_5",
                },
            ),

            # Completed
            "completed":
            forms.CheckboxInput(
                attrs={
                    "class": ("h-5 w-5 rounded border-zinc-300 "
                              "text-primary focus:ring-primary "
                              "dark:border-zinc-700 "
                              "dark:bg-zinc-900"),
                }),
        }

    def clean_title(self):

        title = self.cleaned_data.get(
            "title",
            "",
        ).strip()

        if len(title) < 3:

            raise forms.ValidationError(
                "Title must contain at least 3 characters.", )

        return title
