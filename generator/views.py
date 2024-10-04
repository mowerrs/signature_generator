from django.shortcuts import render
from django.template.loader import render_to_string

from signature_generator.settings import STATIC_URL
from .forms import SignatureForm


def generate_signature(request):
    if request.method == "POST":
        form = SignatureForm(request.POST)
        if form.is_valid():

            mobile_number = "0" + form.cleaned_data["phone"].replace(" ", "").replace(
                "+64", "0"
            ).replace("64", "0").lstrip("0")
            formatted_number = (
                mobile_number[:3] + " " + mobile_number[3:6] + " " + mobile_number[6:]
            )

            context = {
                "name": form.cleaned_data["name"],
                "title": form.cleaned_data["title"],
                "division": form.cleaned_data.get("division"),
                "phone": formatted_number,
            }

            content = render_to_string("result.html", context)
            with open(
                f"{STATIC_URL}/{context['name']}.html", "w", encoding="UTF-8"
            ) as static_file:
                static_file.write(content)

            return render(request, "result.html", context)
    else:
        form = SignatureForm()

    return render(request, "create_form.html", {"form": form})
