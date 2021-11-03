from django.shortcuts import render
from django.views import View


class SampleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "app_folder/page01.html")

    def post(self, request, *args, **kwargs):
        fasta_mapping = {
            "G": "C",
            "C": "G",
            "A": "T",
            "T": "A",
            "g": "C",
            "c": "G",
            "a": "T",
            "t": "A",
        }
        input_fasta = request.POST["input_data"]
        input_fasta_list = list(input_fasta)
        complement_fasta_list = []
        for i in input_fasta_list:
            if i in fasta_mapping:
                complement_fasta_list.append(fasta_mapping.pop(i))
            else:
                raise Exception("Error: An invalid value was entered.")
        reverse_complement_fasta_list = reversed(complement_fasta_list)
        reverse_complement_fasta = "".join(reverse_complement_fasta_list)
        context = {
            "complement": "".join(complement_fasta_list),
            "reverse_complement": reverse_complement_fasta,
        }
        return render(
            request,
            "app_folder/page02.html",
            context=context,
        )


top_page = SampleView.as_view()
