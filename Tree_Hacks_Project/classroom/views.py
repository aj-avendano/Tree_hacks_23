from django.shortcuts import render
from django.views import View

import openai
import requests
openai.api_key = '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'
def dalle_response(user_input):
    response = openai.Image.create(prompt='a white siamese cat',n=1,size="1024x1024")
    image = response['data'][0]['url']
    return image_url
class imageView(View):
    def post(self, request):
        user_input = request.POST['user_input']
        image_url = dalle_response(user_input)
        return HttpResponse(image_url)
