from django.shortcuts import render
from django.http import HttpResponse
from .forms import PDFMergeForm
from .utils import merge_pdfs
import os


def merge_view(request):
    if request.method == "POST":
        files = request.FILES.getlist("files")

        if len(files) >= 2:
            file_paths = []

            try:
                for file in files:
                    file_path = f"/tmp/{file.name}"
                    file_paths.append(file_path)
                    with open(file_path, "wb+") as f:
                        for chunk in file.chunks():
                            f.write(chunk)

                output_path = "/tmp/merged.pdf"
                merge_pdfs(file_paths, output_path)

                with open(output_path, "rb") as merged_file:
                    response = HttpResponse(
                        merged_file.read(), content_type="application/pdf"
                    )
                    response["Content-Disposition"] = (
                        'attachment; filename="merged.pdf"'
                    )

                return response

            finally:
                for path in file_paths:
                    if os.path.exists(path):
                        os.remove(path)
                if os.path.exists(output_path):
                    os.remove(output_path)

        else:
            return HttpResponse("Upload at least two PDF files.", status=400)
    else:
        form = PDFMergeForm()

    return render(request, "pdfmerger_app/merge_form.html", {"form": form})
