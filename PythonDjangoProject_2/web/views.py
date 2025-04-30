from django.shortcuts import render,redirect

'''
    사용자 요청 => DispatcherServlet => Model(@Controller)
        |
    사용자 요청 => urls.py => views.py => models.py
    
    urls.py : @GetMapping, @PostMapping , @RequestMapping
    views.py : @Controller , @RestController
    models.py : @Repository
    
    
    
    
    
     
    
'''
# Create your views here.
from web import models

def main_page(request):
    recipe_list,food_list=models.mainData()

    '''
    데이터 전송은 dict만 가능 {키:값}
    
    
    '''
    # 튜플을 딕셔너리로
    recipe_list = [
        {'no':r[0],'title': r[1],'poster': r[2]} for r in recipe_list
    ]
    food_list = [
        {'fno':f[0],'name': f[1],'poster': f[2] } for f in food_list
    ]

    return render(request, 'main/home.html', {
        'recipe_list': recipe_list,
        'food_list': food_list
    })
