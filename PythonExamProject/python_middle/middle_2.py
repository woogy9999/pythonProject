# _*_ coding:utf-8 _*_
from bs4 import BeautifulSoup
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
"""
<table class="list-wrap">
                        <caption>곡 리스트</caption>
                        <thead>
                        <tr>
                            <th scope="col" class="hd-check"><span class="hide">선택</span></th>
                            <th scope="col" class="hd-number">순위</th>
                            <th scope="col" class="hd-album"><span class="hide">앨범이미지</span></th>
                            <th scope="col" class="hd-link"><span class="hide">곡정보 이동 링크</span></th>
                            <th scope="col" class="hd-info">곡정보</th>
                            <th scope="col" class="hd-btns">듣기</th>
                            <th scope="col" class="hd-btns">추가</th>
                            <th scope="col" class="hd-btns">담기</th>
                            <th scope="col" class="hd-btns">다운</th>
                            <th scope="col" class="hd-btns">뮤비</th>
                            <th scope="col" class="hd-more">더보기</th>
                        </tr>
                        </thead>

                        <tbody>

                            <tr class="list" songid="101514417">
                                <td class="check"><input type="checkbox" class="select-check" title="Drowning" /></td>
                                <td class="number">1

                                    <span class="rank">



                                                <span class="rank"><span class="rank-none"><span
                                                        class="hide">유지</span></span></span>




                                    </span>
                                </td>
                                <td><a href="#" class="cover" onclick="fnViewAlbumLayer('83570761');return false;"><span class="mask"></span><img src="//image.genie.co.kr/Y/IMAGE/IMG_ALBUM/083/570/761/83570761_1682496044865_1_140x140.JPG/dims/resize/Q_80,0" onerror="this.src='//image.genie.co.kr/imageg/web/common/blank_68.gif';" alt="OO-LI" /></a></td>
                                <td class="link"><a href="#" class="btn-basic btn-info" onclick="fnViewSongInfo('101514417');return false;">곡 제목 정보 페이지</a></td>
                                <td class="info">


                                    <a href="#" class="title ellipsis" title="재생" onclick="fnPlaySong('101514417','1');return false;">







                                                Drowning</a>

                                        <a href="#" class="artist ellipsis" onclick="fnViewArtist('80619594');return false;">WOODZ</a>
                                        <i class="bar">|</i>
                                        <a href="#" class="albumtitle ellipsis" onclick="fnViewAlbumLayer('83570761');return false;">OO-LI</a>
                                </td>
"""


def genieMusic():
    for page in range(1, 5):
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        url = f"https://www.genie.co.kr/chart/top200?ditc=D&ymd=20250509&hh=09&rtm=Y&pg={page}"
        music_data = requests.get(url, headers=headers)
        music_data = music_data.text
        print(music_data)
        soup = BeautifulSoup(music_data, 'html.parser')
        title = soup.select('.list-wrap .title')
        singer = soup.select('.list-wrap .artist')
        album = soup.select('.list-wrap .albumtitle')
        poster = soup.select('.list-wrap .cover img')
        for i in range(0, len(title)):
            print(title[i].text)
            print(singer[i].text)
            print(album[i].text)
            print(poster[i].attrs['src'])


# genieMusic()
def melonMusic():
    pass