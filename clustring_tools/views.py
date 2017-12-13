from django.shortcuts import render_to_response


def labeling(request):
    return render_to_response('index.html', {})


def validations(request):
    return render_to_response('validations.html', {})
