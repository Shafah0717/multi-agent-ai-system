from django.shortcuts import render



from ai_agents.classifier_agent import classify_format_and_intent

# Create your views here.

def index(request):
    result = "" 
    if request.method == "POST":
        content = request.POST.get("input_data","")
        result = classify_format_and_intent(content)
    return render(request,"index.html",{"result":result})
