# from django.shortcuts import render



# from ai_agents.classifier_agent import classify_format_and_intent

# # Create your views here.

# def index(request):
#     result = "" 
#     if request.method == "POST":
#         content = request.POST.get("input_data","")
#         result = classify_format_and_intent(content)
#     return render(request,"index.html",{"result":result})

from django.shortcuts import render
from ai_agents.classifier_agent import classify_format_and_intent

def index(request):
    result = ""

    if request.method == "POST":
        content = request.POST.get("input_data", "")

        if request.FILES.get("file_input"):
            uploaded_file = request.FILES["file_input"]
            file_name = uploaded_file.name.lower()

            if file_name.endswith(".json"):
                content = uploaded_file.read().decode("utf-8")
            elif file_name.endswith(".pdf"):
                import fitz  # PyMuPDF
                doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
                content = " ".join([page.get_text() for page in doc])

        if content:
            result = classify_format_and_intent(content)

    return render(request, "index.html", {"result": result})

