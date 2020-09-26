from django import forms
from .models import Student, Branch

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'birthdate', 'college','branch')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'college' in self.data:
            try:
                college_id = int(self.data.get('college'))
                self.fields['branch'].queryset = Branch.objects.filter(college_id=college_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.college.branch_set.order_by('name')