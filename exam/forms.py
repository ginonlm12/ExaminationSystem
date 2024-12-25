import json
from django import forms
from django.contrib.auth.models import User
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class TeacherSalaryForm(forms.Form):
    salary=forms.IntegerField()

class CourseForm(forms.ModelForm):
    class Meta:
        model=models.Course
        fields=['course_name','question_number','total_marks']
        
class QuestionForm(forms.ModelForm):
    courseID = forms.ModelChoiceField(queryset=models.Course.objects.all(), empty_label="Chọn khóa thi", to_field_name="id")

    class Meta:
        model = models.Question
        fields = ['marks', 'question', 'option1', 'option2', 'option3', 'option4', 'option5', 'option6', 'correct_answers']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
        }

    # Field to hold multiple correct answers
    correct_answers = forms.MultipleChoiceField(
        choices=[('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'),
                 ('Option4', 'Option4'), ('Option5', 'Option5'), ('Option6', 'Option6')],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def clean_correct_answers(self):
        correct_answers = self.cleaned_data.get('correct_answers')
        # Convert list to JSON string
        return json.dumps(correct_answers)
