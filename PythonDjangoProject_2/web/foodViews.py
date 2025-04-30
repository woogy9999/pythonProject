from django.shortcuts import render,redirect
from django.http import JsonResponse

from web import foodModels


def food_list(request):
    return render(request,"food/list.html")

def food_list_vue(request):

    page=int(request.GET.get('page',1))


    curpage=int(page)
    foodList,totalpage=foodModels.foodListData(curpage)
    BLOCK=10
    startPage=((curpage-1)//BLOCK*BLOCK)+1
    endPage=((curpage-1)//BLOCK*BLOCK)+BLOCK

    if(endPage>totalpage):
        endPage=totalpage

    fd=[]
    for f in foodList:
        fdata={"fno":f[0],"name":f[1],"poster":f[2]}
        fd.append(fdata)
    food_data={
        "fd":fd,
        "curpage":curpage,
        "totalpage":totalpage,
        "startPage":startPage,
        "endPage":endPage
    }
    return JsonResponse(food_data)
def food_detail(request):
    fno=request.Get['fno']
    return render(request,"food/detail.html",{
        "fno":fno
    })

def food_detail_vue(request):
    #fno=int(request.GET.get('fno',1))
    fno=request.GET['fno']
    detail=foodModels.foodDetailData(int(fno))

    fd = {
        "fno": detail[0],
        "name": detail[1],
        "poster": detail[2],
        "address": detail[3],
        "phone": detail[4],
        "time": detail[5],
        "theme": detail[6],
        "content": detail[7],
        "type": detail[8],
        "parking": detail[9]
    }

    return JsonResponse(fd)