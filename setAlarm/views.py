from webbrowser import get
from django.shortcuts import render
from .collections import (get_collection_names,get_collections_attributes,get_matched_nfts_with_selected_choices)
import pandas as pd

# Create your views here.

global_flag=False
global_matched_nft=[]


def set_alarm_view(request):
    global global_matched_nft
    text = request.GET
    collections_list = get_collection_names()
    context = {"data": collections_list}
    if global_flag:
        collection_name = str(text.get("collection", ""))
        attribute_dict=get_collections_attributes(collection_name)
        if attribute_dict:
            for key,value in attribute_dict.items():
                attribute_dict[key]=str(text.get(key, ""))

            global_matched_nft=get_matched_nfts_with_selected_choices(collection_name=collection_name,attributes=attribute_dict)
            print(global_matched_nft)
            print(type(global_matched_nft))

            
           
        
    return render(request, "setAlarm.html", context)



def load_attributes(request):
    global global_flag
    global_flag=True
    text = request.GET
    collection_name = text.get("collection")
    attribute_dict=get_collections_attributes(collection_name)
    context = {"data": attribute_dict}
    return render(request, "attributes.html", context)

def start_tracking(request):
    context={}
    return render(request,"login.html",context)

def show_results(request):
    keys = global_matched_nft[0].keys()
    values = []
    for i in global_matched_nft:
        temp_list = []
        for k in keys:
            temp_list.append(i[k])
        values.append(temp_list)
    context={"data":keys,"data2":values}
    return render(request,"results.html",context)