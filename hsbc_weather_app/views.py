from django.shortcuts import render
import requests, json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def get_details(request):
    if request.method != 'POST':

        return JsonResponse({
            'status': 'error',
            'message': 'Only POST method is allowed'
        }, status=405)
    try:
        input=request.POST.get('letter')
        response = requests.get('https://samples.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&appid=b6907d289e10d714a6e88b30761fae22')
        # list_details=details[list]
        raw_content = response.json()
        result = [i for i in raw_content['list'] if i['name'].upper().startswith(input.upper())]
        print(result)
        return JsonResponse({"count":len(result),"result":result},status=200)
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"Unexpected error: {e}")  # Log for debugging
        return JsonResponse({
            'status': 'error',
            'message': 'An unexpected error occurred'
        }, status=500)

def input_form_view(request):
    return render(request,'my_app/input_form.html')

