from django.shortcuts import render
import ollama

def chat_view(request):
    text_box = ""
    if request.method=='POST':
        prompt = request.POST.get("prompt")
        response = ollama.chat(
            model = 'llama3',
            messages =[{
                "role":"user",
                "content":prompt
            }]
            

        )


        text_box = response["message"]["content"]
    return render(request,"chat.html" , {"response":text_box})

