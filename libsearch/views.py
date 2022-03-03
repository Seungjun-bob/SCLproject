from django.shortcuts import render
from libsearch.models import Library

def libsearch(request):
    library_div = request.GET.get("lbrry_se_name", None)
    library_gu = request.GET.get("code_value", None)
    library_info = Library.objects.all()
    div_gu_list = library_info.filter(lbrry_se_name=library_div, code_value=library_gu)
    context = {
        "div_gu_list": div_gu_list,
    }
    # if library_div and library_gu:
    #     div_gu_list = library_info.filter(lbrry_se_name=library_div, code_value=library_gu)
    #     context = {
    #         "div_gu_list": div_gu_list,
    #     }
    # elif library_div:
    #     div_list = library_info.filter(lbrry_se_name=library_div)
    #     context = {
    #         "div_list": div_list,
    #     }
    # elif library_gu:
    #     gu_list = library_info.filter(code_value=library_gu)
    #     context = {
    #         "gu_list": gu_list,
    #     }
    # else:
    #     context = None


    return render(request, 'libsearch.html', context)


