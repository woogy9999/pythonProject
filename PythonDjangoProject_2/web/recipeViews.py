from django.shortcuts import render,redirect
from web import recipeModels


def recipe_list(request):

    page = int(request.GET.get('page', 1))
    '''
    try:
        page=request.GET['page']
    except Exception as e:
        page="1"
    '''
    curpage=int(page)
    recipeList,totalpage=recipeModels.recipeListData(curpage)
    BLOCK=10
    startPage=((curpage-1)//BLOCK*BLOCK)+1
    endPage=((curpage-1)//BLOCK*BLOCK)+BLOCK

    if(endPage>totalpage):
        endPage=totalpage

    rd=[]
    for r in recipeList:
        rdata={"no":r[0],"title":r[1],"poster":r[2],"chef":r[3]}
        rd.append(rdata)
    recipe_data={
        "rd":rd,
        "curpage":curpage,
        "totalpage":totalpage,
        "range":range(startPage,endPage+1),
        "startPage":startPage,
        "endPage":endPage
    }

    return render(request, 'recipe/list.html',recipe_data)

# 상세보기 => 쿠키 => redirect => detail_before
def recipe_before(request):
    no = request.GET['no']
    response = redirect("/web/recipe/detail/?no="+str(no))
    response.set_cookie(f"recipe{no}", no, max_age=60 * 60)  # 쿠키 1시간
    return response

def recipe_detail(request):
    no=request.GET['no']
    # String no=request.getParameter("no")
    rd,rmake,rdata=recipeModels.recipeDetailData(int(no))
    # rd = () = {}:JSON
    '''
      no,title,chef,chef_poster,chef_profile,
      info1,info2,info3,content,foodmake,data.poster
    '''
    recipe_data={
        "no":rd[0],
        "title":rd[1],
        "chef":rd[2],
        "chef_poster":rd[3],
        "chef_profile":rd[4],
        "info1":rd[5],
        "info2":rd[6],
        "info3":rd[7],
        "content":rd[8],
        "poster":rd[9]
    }
    fm=rmake.split("\\n")
    posters=[]
    make=[]
    #재료 => ,
    data=rdata.split(",")
    for m in range(len(fm)-1):
        temp=fm[m].split("^")
        make.append(temp[0])
        posters.append(temp[1])
    detail={
        "detail":recipe_data,
        "posters":posters,
        "make":make,
        "data":data
    }
    make_posters = zip(detail["make"], detail["posters"])
    detail["make_posters"] = make_posters
    return render(request,"recipe/detail.html",{"rd":detail })
