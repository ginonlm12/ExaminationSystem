import json
from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    def __str__(self):
        return self.course_name

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200, blank=True, null=False)
    option2 = models.CharField(max_length=200, blank=True, null=True)
    option3 = models.CharField(max_length=200, blank=True, null=True)
    option4 = models.CharField(max_length=200, blank=True, null=True)
    option5 = models.CharField(max_length=200, blank=True, null=True)
    option6 = models.CharField(max_length=200, blank=True, null=True)
    
    # This field stores correct answers as a JSON string
    correct_answers = models.TextField()  # Store correct answers as a JSON string

    def save(self, *args, **kwargs):
        if isinstance(self.correct_answers, list):
            self.correct_answers = json.dumps(self.correct_answers)  # Convert list to JSON string
        super().save(*args, **kwargs)

    def get_correct_answers(self):
        return json.loads(self.correct_answers)  # Convert JSON string back to list
    
# exam/models.py
from django.db import models
from student.models import Student  # Đảm bảo bạn có import Student nếu cần

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey('Course', on_delete=models.CASCADE)  # Đảm bảo Course đã được định nghĩa
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)  # Trường lưu thời gian tạo kết quả

    def __str__(self):
        return f"{self.student} - {self.exam.course_name} - {self.marks} marks"
    

class QuestionResult(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='question_results')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    selected_answer = models.CharField(max_length=255, blank=True, null=True)
    marks = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return f"Result: {self.result.student.user.username} - Question: {self.question.id} - Correct: {self.is_correct}"

    class Meta:
        verbose_name = "Question Result"
        verbose_name_plural = "Question Results"

