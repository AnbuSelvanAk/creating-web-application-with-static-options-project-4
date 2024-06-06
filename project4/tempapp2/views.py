from django.shortcuts import render
def testing(request):
	c='DJANGO FRAMEWORK-ANBU'
	x={'text':c}
	return render(request,'apps/sample.html',context=x)
