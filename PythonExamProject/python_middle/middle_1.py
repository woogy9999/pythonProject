#_*_ coding:utf-8 _*_
# BS => 크롤링 = 셀리니움
import urllib.request as req
from http.client import responses

from bs4 import BeautifulSoup
import requests
"""
<ul class="common_sp_list_ul ea4" style="padding:0 0 0 8px;">
            <li class="common_sp_list_li">
                <div class="common_sp_thumb">
                    <a href="/recipe/7052126" class="common_sp_link">
                                                <img src="https://recipe1.ezmember.co.kr/cache/recipe/2025/05/04/26f743f3ee5b6ad679cc26e726179c7b1_m.jpg">
                    </a>
                </div>
                <div class="common_sp_caption">
                                        <div class="common_sp_caption_tit line2">53.오트밀 과일파이(ft.4구에그팬,시나몬시럽)(2025.5.8)</div>
                    <div class="common_sp_caption_rv_name" style="display: inline-block; vertical-align: bottom;">
                        <a href="/profile/recipe.html?uid=25757478"><img src="https://recipe1.ezmember.co.kr/cache/rpf/2025/04/14/1c4021b4b61a61c12b242a594594b0231.77bf95abca70e4f63d14d79d0dbf76f7">벚꽃조이나</a>
                    </div>
                    <div class="common_sp_caption_rv">
                                                    <span class="common_sp_caption_rv_star"><img src="https://recipe1.ezmember.co.kr/img/mobile/icon_star2_on.png"><img src="https://recipe1.ezmember.co.kr/img/mobile/icon_star2_on.png"><img src="https://recipe1.ezmember.co.kr/img/mobile/icon_star2_on.png"><img src="https://recipe1.ezmember.co.kr/img/mobile/icon_star2_on.png"><img src="https://recipe1.ezmember.co.kr/img/mobile/icon_star2_on.png"></span>
                            <span class="common_sp_caption_rv_ea">(1)</span>
                                                <span class="common_sp_caption_buyer" style="vertical-align: middle;">조회수 49</span>
                    </div>
                </div>
            </li>


"""
def recipe():
  for page in range(1,11):
    url = f'https://www.10000recipe.com/recipe/list.html?order=reco&page={page}'
    res_html = requests.get(url)
    recipe_data=res_html.text
    #print(recipe_data)

    soup = BeautifulSoup(recipe_data, 'html.parser')
    title = soup.select(".common_sp_caption .common_sp_caption_tit")
    chef = soup.select(".common_sp_caption_rv_name")
    img = soup.select(".common_sp_thumb .common_sp_link img")
    hit = soup.select(".common_sp_caption_buyer")


    for i in range(0,len(title)):
        print(title[i].text)
        print(chef[i].text)
        print(hit[i].text)
        print(img[i].attrs['src'])

recipe()


