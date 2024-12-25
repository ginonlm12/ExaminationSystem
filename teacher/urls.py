from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('teacherclick', views.teacherclick_view),
    path('teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'), name='teacherlogin'),
    path('teachersignup', views.teacher_signup_view, name='teachersignup'),
    path('teacher-dashboard', views.teacher_dashboard_view, name='teacher-dashboard'),
    path('teacher-exam', views.teacher_exam_view, name='teacher-exam'),
    path('teacher-add-exam', views.teacher_add_exam_view, name='teacher-add-question'),
    path('teacher-view-exam', views.teacher_view_exam_view, name='teacher-view-question'),
    path('delete-exam/<int:pk>', views.delete_exam_view, name='delete-exam'),
    path('export_excel/', views.export_excel, name='export_excel'),
    path('teacher-question', views.teacher_question_view, name='teacher-question'),
    path('teacher-add-question', views.teacher_add_question_view, name='teacher-add-question'),
    path('teacher-add-question/<int:course_id>/', views.teacher_add_question_view, name='teacher-add-question'),
    path('teacher-view-question', views.teacher_view_question_view, name='teacher-view-question'),
    path('see-question/<int:pk>/', views.see_question_view, name='see-question'),
    path('export_excel/<int:pk>/', views.export_questions_excel, name='export-excel'),
    path('remove-question/<int:pk>', views.remove_question_view, name='remove-question'),
    path('edit-question/<int:pk>/', views.edit_question_view, name='edit-question'),  # Đảm bảo URL sửa câu hỏi
    path('recommend_answer/', views.recommend_answer, name='recommend_answer'),

    # **Các URL cho thống kê**
    path('view-student-scores/<int:course_id>/', views.view_student_scores, name='view-student-scores'),
    path('question-statistics/<int:course_id>/', views.question_statistics, name='question-statistics'),
]
