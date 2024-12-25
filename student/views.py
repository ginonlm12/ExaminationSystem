import json
from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from datetime import date, timedelta
from exam import models as QMODEL
from teacher import models as TMODEL
from exam.models import Result


# for showing signup/login button for student
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'student/studentclick.html')


def student_signup_view(request):
    userForm = forms.StudentUserForm()
    studentForm = forms.StudentForm()
    mydict = {'userForm': userForm, 'studentForm': studentForm}
    if request.method == 'POST':
        userForm = forms.StudentUserForm(request.POST)
        studentForm = forms.StudentForm(request.POST, request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            student = studentForm.save(commit=False)
            student.user = user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request, 'student/studentsignup.html', context=mydict)


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    dict = {
        'total_course': QMODEL.Course.objects.all().count(),
        'total_question': QMODEL.Question.objects.all().count(),
    }
    return render(request, 'student/student_dashboard.html', context=dict)


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'student/student_exam.html', {'courses': courses})


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def take_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    total_questions = QMODEL.Question.objects.all().filter(course=course).count()
    questions = QMODEL.Question.objects.all().filter(course=course)
    total_marks = 0
    for q in questions:
        total_marks = total_marks + q.marks

    return render(request, 'student/take_exam.html', {
        'course': course,
        'total_questions': total_questions,
        'total_marks': total_marks
    })


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def start_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    questions = QMODEL.Question.objects.all().filter(course=course)

    # Tính số lượng các lựa chọn không phải null và không phải chuỗi "None" cho mỗi câu hỏi
    for question in questions:
        question.num_options = sum(1 for option in [question.option1, question.option2, question.option3, 
                                                     question.option4, question.option5, question.option6]
                                    if option is not None and option != "None")  # Kiểm tra không phải "None"
        
        # Lưu danh sách đáp án vào questions để tiện xử lý trong template
        question.options = [
            question.option1,
            question.option2,
            question.option3,
            question.option4,
            question.option5,
            question.option6
        ][:question.num_options]  # Trả về danh sách đáp án hợp lệ (không phải None hoặc "None")
        print(question.options)
    response = render(request, 'student/start_exam.html', {'course': course, 'questions': questions})
    response.set_cookie('course_id', course.id)
    return response

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def calculate_marks_view(request):
    if request.method == 'POST':
        total_marks = 0
        course_id = request.COOKIES.get('course_id')  # Lấy khóa thi từ cookie hoặc session
        print(f"Course ID: {course_id}")  # In ra Course ID
        
        course = QMODEL.Course.objects.get(id=course_id)
        questions = QMODEL.Question.objects.all().filter(course=course)

        student = models.Student.objects.get(user_id=request.user.id)

        # Lưu kết quả vào bảng Result trước khi lưu QuestionResult
        result = QMODEL.Result()
        result.marks = 0  # Khởi tạo điểm tổng bằng 0
        result.exam = course
        result.student = student
        result.save()  # Lưu Result để có result_id

        # Kiểm tra đáp án của học sinh cho mỗi câu hỏi
        for q in questions:
            selected_answers = []

            # Kiểm tra các đáp án học sinh đã chọn trong form
            if request.POST.get(f"question_{q.id}_Option1"):
                selected_answers.append("Option1")
            if request.POST.get(f"question_{q.id}_Option2"):
                selected_answers.append("Option2")
            if request.POST.get(f"question_{q.id}_Option3"):
                selected_answers.append("Option3")
            if request.POST.get(f"question_{q.id}_Option4"):
                selected_answers.append("Option4")
            if request.POST.get(f"question_{q.id}_Option5"):
                selected_answers.append("Option5")
            if request.POST.get(f"question_{q.id}_Option6"):
                selected_answers.append("Option6")
            
            # In ra các đáp án học sinh đã chọn
            print(f"Question ID: {q.id}, Selected Answers: {selected_answers}")

            # Lấy các đáp án đúng từ cơ sở dữ liệu
            correct_answers = json.loads(q.correct_answers)
            print(f"Question ID: {q.id}, Correct Answers: {correct_answers}")  # In ra đáp án đúng

            # Kiểm tra xem các đáp án học sinh chọn có đúng không
            is_correct = set(selected_answers) == set(correct_answers)

            # Tính điểm nếu đúng
            marks_for_question = q.marks if is_correct else 0

            # Cộng điểm vào tổng điểm
            total_marks += marks_for_question

            # Lưu kết quả của câu hỏi vào bảng QuestionResult
            question_result = QMODEL.QuestionResult(
                result=result,  # Liên kết với đối tượng Result đã lưu
                question=q,
                is_correct=is_correct,
                selected_answer=','.join(selected_answers),  # Lưu các đáp án học sinh chọn
                marks=marks_for_question
            )
            question_result.save()

        # Cập nhật điểm tổng vào bảng Result sau khi tính điểm cho tất cả câu hỏi
        result.marks = total_marks
        result.save()

        # Sau khi tính điểm xong, chuyển hướng sang trang kết quả
        return HttpResponseRedirect('view-result')

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def view_result_view(request):
    student = models.Student.objects.get(user_id=request.user.id)
    results = QMODEL.Result.objects.filter(student=student).order_by('-exam__date')

    # Trả về các kết quả của học sinh
    return render(request, 'student/view_result.html', {'results': results})


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def check_marks_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    student = models.Student.objects.get(user_id=request.user.id)
    results = QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request, 'student/check_marks.html', {'results': results})


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_marks_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/student_marks.html',{'courses':courses})
