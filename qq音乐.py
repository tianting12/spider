import execjs
import requests
import os

os.environ["EXECJS_RUNTIME"] = "Node"
print(execjs.get().name)

def get_js_function(js_path, func_name, func_args):
    with open(js_path, encoding='utf-8') as fp:
        js = fp.read()
        ctx = execjs.compile(js)
        print(ctx)
        return ctx.call(func_name, func_args)

def get_dataurl(mid,song):
    headers={
        'cookie': 'pgv_pvid=3132870800; pgv_pvi=6310474752; eas_sid=k1o5i5n9B308U1m9e9A9g4q0g0; RK=mYKofuENR5; ptcz=350c704f947e79a6278726585d9a011e73326e651a2c754c96a8f7aab062220a; tvfe_boss_uuid=e09e58a9ea7513be; LW_uid=I1E596R2I6K5b8P4x8Z5g8X1j7; o_cookie=731068380; ts_uid=7126261320; pac_uid=1_731068380; XWINDEXGREY=0; LW_sid=T1u5C7A822q1k1y5R5R3X8b8X1; ptui_loginuin=2404156242; pgv_si=s6507730944; pgv_info=ssid=s7146159662; ts_refer=www.baidu.com/link; userAction=1; _qpsvr_localtk=0.6668019667232461; psrf_access_token_expiresAt=1594519987; psrf_qqaccess_token=3DF5409D8688BD99F226DD883E2BF683; uin=731068380; qqmusic_key=Q_H_L_2ChoJw50e0f7lKx-DlvCap33ne7S-ZMT7oqG3jWh_3Y_JDW0oUqSGdOhY8BiqF8; psrf_qqopenid=6EF31F57DC837C8AB3C0E992C9D6D773; qm_keyst=Q_H_L_2ChoJw50e0f7lKx-DlvCap33ne7S-ZMT7oqG3jWh_3Y_JDW0oUqSGdOhY8BiqF8; psrf_qqunionid=B8A4BA9567B3DEA9D48BA5B38EDDA2CF; psrf_musickey_createtime=1586743987; psrf_qqrefresh_token=DAF9020492CED7143E181B0065F1EA1B; qqmusic_fromtag=66; yqq_stat=0; player_exist=1; yq_playschange=0; yq_playdata=; yplayer_open=1; yq_index=11',
        'origin': 'https://y.qq.com',
        'referer': 'https://y.qq.com/portal/player.html',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.',
    }
    url=get_js_function('qq音乐.js','get_sign',mid)
    # print(url)
    resp=requests.get(url=url,headers=headers)
    # print(resp.text)
    if resp.status_code==200:
        try:
            purl='https://isure.stream.qqmusic.qq.com/'+(resp.json().get('req_0').get('data').get('midurlinfo'))[0].get('purl')
            mp3=requests.get(url=purl,headers=headers).content
            with open(f'{song}.mp3','wb')as f:
                f.write(mp3)
            print('==========下载完成============')
        except Exception as e:
            print(f'something error===>{e}')
            
def sercah(word,page=20):
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.',
    }
    params={
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '42123115147971044',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': '1',
        'n': page,
        'w': word,
        'g_tk_new_20200303': '1649304378',
        'g_tk': '1649304378',
        'loginUin': '1162467606',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
    }
    resp=requests.get(url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?',headers=headers,params=params)
    if resp.status_code==200:
        try:
            lists=resp.json().get('data').get('song').get('list')
            for i in lists:
                content={
                    'name':i.get('name'),
                    'singer':(i.get('singer')[0]).get('name'),
                    'mid':i.get('mid')
                }
                print(content)
            print('==========复制对应歌曲的mid============')

        except Exception as e:
            print(f'something error===>{e}')
if __name__=='__main__':
    song=input('输入下载歌曲:')
    sercah(song)
    mid=input('输入mid:')
    get_dataurl(mid,song)
