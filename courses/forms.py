from django import forms

from . import models

class CourseForm(forms.ModelForm):
	class Meta:
		model = models.Course
		fields = [
			'title',
			'description'
		]

class UploadFileForm(forms.Form):
	order = forms.IntegerField()
	title = forms.CharField(max_length=255)
	file = forms.FileField()

class TextForm(forms.ModelForm):
	class Media:
		css = {'all':('courses/css/text_step.css',)}

	class Meta:
		model = models.Text
		fields = [
			'title',
			'description',
			'order',
			'content'
		]

class QuizForm(forms.ModelForm):
	class Meta:
		model = models.Quiz 
		fields = [
			'title',
			'description',
			'order',
			'total_questions',
		]

class QuestionForm(forms.ModelForm):
	class Media:
		css = {'all': ('courses/css/order.css',)}
		js = (
			'/static/js/sortable.min.js',
			'courses/js/order.js'
		)

class TrueFalseQuestionForm(QuestionForm):
	class Meta:
		model = models.TrueFalseQuestion
		fields = ['order', 'prompt']

class MultipleChoiceQuestionForm(QuestionForm):
	class Meta:
		model = models.MultipleChoiceQuestion
		fields = [
			'order',
			'prompt',
			'shuffle_answers'
		]

class AnswerForm(forms.ModelForm):
	class Meta:
		model = models.Answer
		fields = [
			'text',
			'correct',
			'order'
		]

AnswerFormSet = forms.modelformset_factory(
	models.Answer,
	form=AnswerForm,
	extra=2,
)

AnswerInlineFormSet = forms.inlineformset_factory(
	models.Question,
	models.Answer,
	extra=1,
	fields=('order', 'text', 'correct'),
	formset=AnswerFormSet,
	min_num=1,
)