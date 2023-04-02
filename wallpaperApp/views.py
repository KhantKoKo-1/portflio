from django.shortcuts import render
from pymongo import MongoClient
connection_string = "mongodb+srv://khantkoko:53526512@cluster0." \
                    "gbupzbb.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client['my_DB']
collection = db['myCol']


def home(request):
    return render(request, 'Dialog.html')

def result(request):
    user_email = request.POST['email']
    user_message = request.POST['message']
    data ={'Email': user_email, 'Contact Message': user_message}
    collection.insert_one(data)
    return render(request, 'result.html', {'email': user_email,'message': user_message})
