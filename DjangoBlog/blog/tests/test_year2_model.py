from django.test import TestCase
from blog.models import UoB_Year_2

class Year2Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        UoB_Year_2.objects.create(course = 'course1')
        UoB_Year_2.objects.create(course = 'course2')
        UoB_Year_2.objects.create(course = 'course3')
        UoB_Year_2.objects.create(course = 'course4')
        UoB_Year_2.objects.create(course = 'course5')
        UoB_Year_2.objects.create(course = 'course6')
        
    def testCourse1(self):
        testQuery = UoB_Year_2.objects.get(id=1)
        course1 = testQuery.course
        print("year2 course1: " + course1)
        self.assertEquals(course1, 'course1')
        
    def testCourse2(self):
        testQuery = UoB_Year_2.objects.get(id=2)
        course2 = testQuery.course
        print("year2 course2: " + course2)
        self.assertEquals(course2, 'course2')
        
    def testCourse3(self):
        testQuery = UoB_Year_2.objects.get(id=3)
        course3 = testQuery.course
        print("year2 course3: " + course3)
        self.assertEquals(course3, 'course3')
        
    def testCourse4(self):
        testQuery = UoB_Year_2.objects.get(id=4)
        course4 = testQuery.course
        print("year2 course4: " + course4)
        self.assertEquals(course4, 'course4')
        
    def testCourse5(self):
        testQuery = UoB_Year_2.objects.get(id=5)
        course5 = testQuery.course
        print("year2 course5: " + course5)
        self.assertEquals(course5, 'course5')
        
    def testCourse6(self):
        testQuery = UoB_Year_2.objects.get(id=6)
        course6 = testQuery.course
        print("year2 course6: " + course6)
        self.assertEquals(course6, 'course6')
        
    def test_year2_course_max_length(self):
        testQuery = UoB_Year_2.objects.get(id=1)
        max_length = testQuery._meta.get_field('course').max_length
        print("year1 course max length: " + str(max_length))
        self.assertEquals(max_length, 200)