from django.shortcuts import render
from .collections import (get_collection_names,get_collections_attributes,get_matchec_nfts_with_selected_choices)


# Create your views here.


def set_alarm_view(request):
    text = request.GET
    collections_list = get_collection_names()
    context = {"data": collections_list}
    return render(request, "setAlarm.html", context)


def load_attributes(request):
    collection_name = request.GET.get("collection")
    print(collection_name)
    attribute_dict=get_collections_attributes(collection_name)
    print(type(attribute_dict))
    context = {"data": attribute_dict}

    return render(request, "attributes.html", context)
