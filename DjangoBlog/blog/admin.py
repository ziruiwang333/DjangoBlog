from django.contrib import admin
from .models import Post
from .models import Education
from .models import Work_Experience
from .models import MyDetail
from .models import Gallery, Photos
from .models import Course
from .models import Post_Type

# Register your models here.
admin.site.register(Post)
admin.site.register(Post_Type)
admin.site.register(Education)
admin.site.register(Work_Experience)
admin.site.register(Gallery)
admin.site.register(Photos)


class CourseAdmin(admin.ModelAdmin):
    list_display = ["course_name", "university", "year"]
admin.site.register(Course, CourseAdmin)

class MyDetailAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "date_of_birth", "phone1", "phone2", "email"]
admin.site.register(MyDetail, MyDetailAdmin)