from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Course, Step

class CourseModelTests(TestCase):

	def test_course_creation(self):

		course = Course.objects.create(
			title="Python Regular Expressions",
			description="Learn to write regular expressions in Python"
		)

		now = timezone.now()
		self.assertLessEqual(course.created_at, now)

class StepModelTests(TestCase):

	def test_step_creation(self):
		course = Course.objects.create(
			title="Python Regular Expressions",
			description="Learn to write regular expressions in Python"
		)

		step = Step.objects.create(
			title="Basics of Regular Expressions",
			description="Lets start with a few simple regular expressions!",
			content="No content yet, this is just a test!",
			order=0,
			course=course
		)

		now = timezone.now()
		self.assertEqual("Basics of Regular Expressions", step.title)


class CourseViewsTests(TestCase):
	def setUp(self):
		self.course=Course.objects.create(
			title="Python Testing",
			description="Learn to write tests in Python"
		)
		self.course2= Course.objects.create(
			title="New Course",
			description="Course Description"
		)
		self.step = Step.objects.create(
			title="Introduction to Doctests",
			description="Learn how to write tests in your docstrings.",
			course=self.course
		)
		self.step2 = Step.objects.create(
			title="Introduction to Unittests",
			description="Learn how to use Python's Unittests library",
			course=self.course
		)

	def test_course_list_view(self):
		resp = self.client.get(reverse('courses:list'))

		self.assertEqual(resp.status_code, 200)
		self.assertIn(self.course, resp.context['courses'])
		self.assertIn(self.course2, resp.context['courses'])

	def test_course_detail_view(self):
		resp = self.client.get(reverse('courses:detail', args=[1]))

		self.assertEqual(self.course.title, resp.context['course'].title)
		self.assertNotIn(self.course2.title, resp.context['course'].title)


class StepViewsTests(TestCase):
	def setUp(self):
		self.course=Course.objects.create(
			title="Python Testing",
			description="Learn to write tests in Python"
		)
		self.step = Step.objects.create(
			title="Introduction to Unittests",
			description="Learn how to use Python's Unittests library",
			course=self.course
		)
		self.step2 = Step.objects.create(
			title="Introduction to Doctests",
			description="Learn how to write tests in your docstrings.",
			course=self.course
		)

	def test_step_detail_view(self):
		resp = self.client.get(reverse('courses:step', args=[1,1]))

		self.assertEqual(self.step.title, resp.context['step'].title)
		self.assertNotIn(self.step2.title, resp.context['step'].title)

		

		