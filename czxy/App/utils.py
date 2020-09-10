#coding:utf-8
import datetime

import requests

import json
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import *

item_contry= {'阿富汗': 'Afghanistan', '奥兰群岛': 'Aland Islands', '阿尔巴尼亚': 'Albania', '阿尔及利亚': 'Algeria', '美属萨摩亚': 'American Samoa', '安道尔': 'Andorra', '安哥拉': 'Angola', '安圭拉': 'Anguilla', '安提瓜和巴布达': 'Antigua and Barbuda', '阿根廷': 'Argentina', '亚美尼亚': 'Armenia', '阿鲁巴': 'Aruba', '澳大利亚': 'Australia', '奥地利': 'Austria', '阿塞拜疆': 'Azerbaijan', '孟加拉': 'Bangladesh', '巴林': 'Bahrain', '巴哈马': 'Bahamas', '巴巴多斯': 'Barbados', '白俄罗斯': 'Belarus', '比利时': 'Belgium', '伯利兹': 'Belize', '贝宁': 'Benin', '百慕大': 'Bermuda', '不丹': 'Bhutan', '玻利维亚': 'Bolivia', '波斯尼亚和黑塞哥维那': 'Bosnia and Herzegovina', '博茨瓦纳': 'Botswana', '布维岛': 'Bouvet Island', '巴西': 'Brazil', '文莱': 'Brunei', '保加利亚': 'Bulgaria', '布基纳法索': 'Burkina Faso', '布隆迪': 'Burundi', '柬埔寨': 'Cambodia', '喀麦隆': 'Cameroon', '加拿大': 'Canada', '佛得角': 'Cape Verde', '中非': 'Central African Republic', '乍得': 'Chad', '智利': 'Chile', '圣诞岛': 'Christmas Islands', '科科斯（基林）群岛': 'Cocos (keeling) Islands', '哥伦比亚': 'Colombia', '科摩罗': 'Comoros', '刚果（金）': 'Congo (Congo-Kinshasa)', '刚果': 'Congo', '库克群岛': 'Cook Islands', '哥斯达黎加': 'Costa Rica', '科特迪瓦': 'Cote D’Ivoire', '中国': 'China', '克罗地亚': 'Croatia', '古巴': 'Cuba', '捷克': 'Czech', '塞浦路斯': 'Cyprus', '丹麦': 'Denmark', '吉布提': 'Djibouti', '多米尼加': 'Dominica', '东帝汶': 'Timor-Leste', '厄瓜多尔': 'Ecuador', '埃及': 'Egypt', '赤道几内亚': 'Equatorial Guinea', '厄立特里亚': 'Eritrea', '爱沙尼亚': 'Estonia', '埃塞俄比亚': 'Ethiopia', '法罗群岛': 'Faroe Islands', '斐济': 'Fiji', 'Finland': 'Finland', '法国': 'France', '法国大都会': 'Franch Metropolitan', '法属圭亚那': 'Franch Guiana', '法属波利尼西亚': 'French Polynesia', '加蓬': 'Gabon', '冈比亚': 'Gambia', '格鲁吉亚': 'Georgia', '德国': 'Germany', '加纳': 'Ghana', '直布罗陀': 'Gibraltar', '希腊': 'Greece', '格林纳达': 'Grenada', '瓜德罗普岛': 'Guadeloupe', '关岛': 'Guam', '危地马拉': 'Guatemala', '根西岛': 'Guernsey', '几内亚比绍': 'Guinea-Bissau', '几内亚': 'Guinea', '圭亚那': 'Guyana', '香港 （中国）': 'Hong Kong', '海地': 'Haiti', '洪都拉斯': 'Honduras', '匈牙利': 'Hungary', '冰岛': 'Iceland', '印度': 'India', '印度尼西亚': 'Indonesia', '伊朗': 'Iran', '伊拉克': 'Iraq', '爱尔兰': 'Ireland', '马恩岛': 'Isle of Man', '以色列': 'Israel', '意大利': 'Italy', '牙买加': 'Jamaica', '日本': 'Japan', '泽西岛': 'Jersey', '约旦': 'Jordan', '哈萨克斯坦': 'Kazakhstan', '肯尼亚': 'Kenya', '基里巴斯': 'Kiribati', '韩国': 'Korea', '朝鲜': 'Korea (North)', '科威特': 'Kuwait', '吉尔吉斯斯坦': 'Kyrgyzstan', '老挝': 'Laos', '拉脱维亚': 'Latvia', '黎巴嫩': 'Lebanon', '莱索托': 'Lesotho', '利比里亚': 'Liberia', '利比亚': 'Libya', '列支敦士登': 'Liechtenstein', '立陶宛': 'Lithuania', '卢森堡': 'Luxembourg', '澳门（中国）': 'Macau', '马其顿': 'Macedonia', '马拉维': 'Malawi', '马来西亚': 'Malaysia', '马达加斯加': 'Madagascar', '马尔代夫': 'Maldives', '马里': 'Mali', '马耳他': 'Malta', '马绍尔群岛': 'Marshall Islands', '马提尼克岛': 'Martinique', '毛里塔尼亚': 'Mauritania', '毛里求斯': 'Mauritius', '马约特': 'Mayotte', '墨西哥': 'Mexico', '密克罗尼西亚': 'Micronesia', '摩尔多瓦': 'Moldova', '摩纳哥': 'Monaco', '蒙古': 'Mongolia', '黑山': 'Montenegro', '蒙特塞拉特': 'Montserrat', '摩洛哥': 'Morocco', '莫桑比克': 'Mozambique', '缅甸': 'Myanmar', '纳米比亚': 'Namibia', '瑙鲁': 'Nauru', '尼泊尔': 'Nepal', '荷兰': 'Netherlands', '新喀里多尼亚': 'New Caledonia', '新西兰': 'New Zealand', '尼加拉瓜': 'Nicaragua', '尼日尔': 'Niger', '尼日利亚': 'Nigeria', '纽埃': 'Niue', '诺福克岛': 'Norfolk Island', '挪威': 'Norway', '阿曼': 'Oman', '巴基斯坦': 'Pakistan', '帕劳': 'Palau', '巴勒斯坦': 'Palestine', '巴拿马': 'Panama', '巴布亚新几内亚': 'Papua New Guinea', '巴拉圭': 'Paraguay', '秘鲁': 'Peru', '菲律宾': 'Philippines', '皮特凯恩群岛': 'Pitcairn Islands', '波兰': 'Poland', '葡萄牙': 'Portugal', '波多黎各': 'Puerto Rico', '卡塔尔': 'Qatar', '留尼汪岛': 'Reunion', '罗马尼亚': 'Romania', '卢旺达': 'Rwanda', '俄罗斯联邦': 'Russian Federation', '圣赫勒拿': 'Saint Helena', '圣基茨和尼维斯': 'Saint Kitts-Nevis', '圣卢西亚': 'Saint Lucia', '圣文森特和格林纳丁斯': 'Saint Vincent and the Grenadines', '萨尔瓦多': 'El Salvador', '萨摩亚': 'Samoa', '圣马力诺': 'San Marino', '圣多美和普林西比': 'Sao Tome and Principe', '沙特阿拉伯': 'Saudi Arabia', '塞内加尔': 'Senegal', '塞舌尔': 'Seychelles', '塞拉利昂': 'Sierra Leone', '新加坡': 'Singapore', '塞尔维亚': 'Serbia', '斯洛伐克': 'Slovakia', '斯洛文尼亚': 'Slovenia', '所罗门群岛': 'Solomon Islands', '索马里': 'Somalia', '南非': 'South Africa', '西班牙': 'Spain', '斯里兰卡': 'Sri Lanka', '苏丹': 'Sudan', '苏里南': 'Suriname', '斯威士兰': 'Swaziland', '瑞典': 'Sweden', '瑞士': 'Switzerland', '叙利亚': 'Syria', '塔吉克斯坦': 'Tajikistan', '坦桑尼亚': 'Tanzania', '台湾 （中国）': 'Taiwan', '泰国': 'Thailand', '特立尼达和多巴哥': 'Trinidad and Tobago', '多哥': 'Togo', '托克劳': 'Tokelau', '汤加': 'Tonga', '突尼斯': 'Tunisia', '土耳其': 'Turkey', '土库曼斯坦': 'Turkmenistan', '图瓦卢': 'Tuvalu', '乌干达': 'Uganda', '乌克兰': 'Ukraine', '阿拉伯联合酋长国': 'United Arab Emirates', '英国': 'United Kingdom', '美国': 'United States', '乌拉圭': 'Uruguay', '乌兹别克斯坦': 'Uzbekistan', '瓦努阿图': 'Vanuatu', '梵蒂冈': 'Vatican City', '委内瑞拉': 'Venezuela', '越南': 'Vietnam', '瓦利斯群岛和富图纳群岛': 'Wallis and Futuna', '西撒哈拉': 'Western Sahara', '也门': 'Yemen', '南斯拉夫': 'Yugoslavia', '赞比亚': 'Zambia', '津巴布韦': 'Zimbabwe', '阿联酋': 'United Arab Emirates', '芬兰': 'Finland', '俄罗斯': 'Russia', '波黑': 'Bosnia and Herzegovina', '北马其顿': 'The Republic of North Macedonia', '列支敦士登公国': 'Liechtenstein', '日本本土': 'Japan', '科索沃': 'Kosovo', '刚果（布）': 'The Republic of Congo'}

class Ncov(object):
    def __init__(self):
        self.api_url ='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5' # tengxun 国内数据api
        self.china =  'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other' #外国和历史数据api
        self.cities = []
        self.cuntry = []

    #获取国内数据
    def get_data(self):
        data = requests.get(self.api_url).json()['data']
        return data

    #获取国外数据和历史数据
    def get_ding_data(self):
        data = requests.get(self.china).json()['data']
        return data

    #数据处理 china 并保存国内数据
    def data_info(self):
        all = json.loads(self.get_data())
        chinaTotal = all['chinaTotal']  # 目前中国总患病数
        date = all['lastUpdateTime']
        chinaAdd = all['chinaAdd']  # 昨日增加
        areaTree = all['areaTree'][0]['children']  #

        for provice in areaTree:
            provice_name = provice['name']  # 获取省份

            for city in provice['children']:
                city_ncov = {
                    '日期': date,
                    '省份': provice_name,
                    '市': city['name'],
                    '新增病例': city['today']['confirm'],
                    # '新增死亡病例': city['today']['dead'],
                    # '新增治愈病例': city['today']['heal'],
                    '累计确认': city['total']['confirm'],
                    '累计死亡': city['total']['dead'],
                    '累计治愈': city['total']['heal']
                }
                # print(city_ncov)
                # print(city)
                self.cities.append(city_ncov)
        df = pd.DataFrame(self.cities)
        # df.to_csv('中国疫情信息\{}{}.csv'.format('中国疫情各省份市信息', datetime.date.today()), index=False)
        # self.export_csv(self.cities,title='中国疫情各省份市信息')
        # print('中国疫情各省份市信息下载完成')

        #绘制中国疫情确诊地图
        map_china_echarts = Map(
            init_opts=opts.InitOpts(width='1500px', height='1500px')
        )
        map_china_echarts.add(
            '中国',
            [list(z) for z in zip(list(df["省份"]), list(df['累计确认']))],
            'china',
            is_map_symbol_show=False
        )
        map_china_echarts.set_global_opts(
            title_opts=opts.TitleOpts(
                title='最新ncov疫情地图(' + str(datetime.date.today()) + ')'  # title
            ),
            visualmap_opts=opts.VisualMapOpts(
                max_=10000,
                is_piecewise=True,  # 颜色是否分段显示（False为渐变，True为分段）
                pieces=[
                    {"min": 1, "max": 9, "label": "10人以下", "color": "#FFE6BE"},
                    {"min": 10, "max": 99, "label": "10-99人", "color": "#FFB769"},
                    {"min": 100, "max": 499, "label": "100-499人", "color": "#FF8F66"},
                    {"min": 500, "max": 999, "label": "500-999人", "color": "#ED514E"},
                    {"min": 1000, "max": 9999, "label": "1000人以上", "color": "#CA0D11"},
                    {"min": 10000, "max": 99999, "label": "1000人以上", "color": "#C23531"},
                ]
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,  # 显示
                trigger_on='mousemove|click',  # 鼠标点击或者移动到出现具体的数值
            ),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True,  # 是否显示提示框组件，包括提示框浮层和axisPointer。
            )
        )
        map_china_echarts.render(r'G:\django\czxy\templates\ncov\中国地图\最新ncov疫情中国地图({}).html'.format(datetime.date.today()))
        # print('最新ncov疫情中国地图下载完成')

        # 绘制中国疫情新增确诊地图
        map_china_add_echarts = Map(
            init_opts=opts.InitOpts(width='1500px', height='1500px')
        )
        map_china_add_echarts.add(
            '中国',
            [list(z) for z in zip(list(df["省份"]), list(df['新增病例']))],
            'china',
            is_map_symbol_show=False
        )
        map_china_add_echarts.set_global_opts(
            title_opts=opts.TitleOpts(
                title='最新ncov疫情地图(' + str(datetime.date.today()) + ')'  # title
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_piecewise=True,  # 颜色是否分段显示（False为渐变，True为分段）
                pieces=[
                    {"min": 0, "max": 0, "label": "0人", "color": "#FFFFFF"},
                    {"min": 0, "max": 10, "label": "1-5人", "color": "#FFAA85"},
                    {"min": 10, "max": 20, "label": "5-10", "color": "#FF7B69"},
                    {"min": 20, "max": 50, "label": "30-50人", "color": "#CA0D11"},
                    {"min": 50, "max": 99999, "label": "50人以上", "color": "#660208"},
                ]
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,  # 显示
                trigger_on='mousemove|click',  # 鼠标点击或者移动到出现具体的数值
            ),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True,  # 是否显示提示框组件，包括提示框浮层和axisPointer。
            )
        )
        map_china_add_echarts.render(r'G:\django\czxy\templates\ncov\中国地图\最新ncov疫情中国新增病例地图({}).html'.format(datetime.date.today()))
        # print(df[df['新增病例']>0])
        # print('最新ncov疫情中国地图新增下载完成')

    #中国累计数据
    def china_cumulative_data(self):
        count = []
        all = json.loads(self.get_ding_data())
        for i in all['chinaDayList']:
            time_ncov = {
                '日期':i['date'],
                '确诊':i['confirm'],
                '疑似':i['suspect'],
                '死亡':i['dead'],
                '治愈':i['heal'],
            }
            # print(time_ncov)
            count.append(time_ncov)
        df = pd.DataFrame(count)

        # df.to_csv('中国疫情信息\中国累计数据.csv',index=False)
        # print('中国累计数据下载完成')

        line_echarts = Line()
        line_echarts.add_xaxis(list(df['日期']))
        line_echarts.add_yaxis('确认', list(df['确诊']),is_smooth=True,)
        line_echarts.add_yaxis('疑似', list(df['疑似']))
        line_echarts.set_global_opts(
            title_opts=opts.TitleOpts(title="nCoV确认病例与疑似病例曲线"),
            datazoom_opts=opts.DataZoomOpts(
                is_show=True,  #显示
                is_realtime=True, #拖动时，是否实时更新系列的视图。如果设置为 false，则只在拖拽结束的时候更新。
                range_end= 60, # 数据窗口范围的结束百分比。
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True, # 是否显示提示框组件，包括提示框浮层和axisPointer。
                trigger='axis', #坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                trigger_on='mousemove|click', #同时鼠标移动和点击时触发。
            ),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True, #是否显示提示框组件，包括提示框浮层和axisPointer。

            )

        )

        line_echarts.render(r'G:\django\czxy\templates\ncov\中国地图折线图\最新ncov疫情折线图({}).html'.format(datetime.date.today()))
        # print("最新ncov中国疫情折线图完成")

    #外国疫情具体到国家
    def foreign_ncov(self):
        count = []
        count.append({'国家中': '中国', '国家英': 'China', '确诊': 81692, '死亡': 3276, '治愈': 72848, '新增': 102})
        # count.append({'国家中': '日本', '国家英': 'Japan', '确诊': 1116, '死亡': 12, '治愈': 248, '新增': 71})
        all = json.loads(self.get_ding_data())
        try:
            for i in all['foreignList']:
                if i['name'] != '钻石号邮轮':
                    contry = {
                        '国家中':i['name'],
                        '国家英':item_contry[i['name']],
                        '确诊':i['confirm'],
                        '死亡':i['dead'],
                        '治愈':i['heal'],
                        '新增':i['confirmAdd'],
                    }
                    count.append(contry)

                #判断国家具体地区的感染人数如果感染人数多则进行具体国家的数据统计 暂时没想着画地图
                try:
                    contry_conunt = []
                    contry_area = i['children']

                    for j in contry_area:
                        # print(j)
                        contryareas = {
                            '地区':j['name'],
                            '确诊':j['confirm'],
                            '死亡':j['dead'],
                            '治愈':j['heal'],
                            '新增':j['confirmAdd'],
                        }
                        contry_conunt.append(contryareas)
                    # self.export_csv(contry_conunt,i['name'])
                    # print(contry_conunt)
                    df2 = pd.DataFrame(contry_conunt)
                    # df2.to_csv('各国疫情状况\{}{}.csv'.format(i['name'],datetime.date.today()), index=False)
                    # print(i['name'] + '今日疫情下载完成')

                except:
                    pass
        except:
            pass
        # count.append({'国家中':'中国','国家英':'China','确诊':80813,'死亡':3073,'治愈':55490,'新增':103})
        # count.append({'国家中':'日本','国家英':'Japan','确诊':1116,'死亡':12,'治愈':248,'新增':71})
        df = pd.DataFrame(count)
        # df.to_csv('各国疫情状况\{}{}.csv'.format('世界各国疫情',datetime.date.today()), index=False)
        # print('世界各国疫情下载完成')

        # print(df)

        world_map = (
            Map()
            .add(
                series_name='世界地图', #系列名称，用于 tooltip 的显示，legend 的图例筛选。
                data_pair=[list(z) for z in zip(list(df['国家英']), list(df['确诊']))], # 数据项 (坐标点名称，坐标点值)
                maptype='world', # 地图类型，具体参考 pyecharts.datasets.map_filenames.json 文件
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title='世界疫情地图ncov' #标题
                ),
                visualmap_opts=opts.VisualMapOpts(
                    type_='color' #根据颜色来进行区分
                ),
                tooltip_opts=opts.TooltipOpts(
                    is_show=True, # 显示
                    trigger_on='mousemove|click', #鼠标点击或者移动到出现具体的数值
                ),
                toolbox_opts=opts.ToolboxOpts(
                    is_show=True, # 工具栏 下载图片，修改数据等
                )

            )
        )
        world_map.render(r'G:\django\czxy\templates\ncov\最新世界地图\最新世界ncov疫情分布图({}).html'.format(datetime.date.today()))
        # print("最新世界ncov疫情分布图下载完成")
        bar_map = (
            Bar()
                .add_xaxis(list(df['国家中']))
                .add_yaxis('确诊人数', list(df['确诊']))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="nCoV国家确诊人数柱状图"),
                datazoom_opts=opts.DataZoomOpts(
                    is_show=True,  # 显示
                    is_realtime=True,  # 拖动时，是否实时更新系列的视图。如果设置为 false，则只在拖拽结束的时候更新。
                    range_end=5,  # 数据窗口范围的结束百分比。
                ),
                tooltip_opts=opts.TooltipOpts(
                    is_show=True,  # 是否显示提示框组件，包括提示框浮层和axisPointer。
                    trigger='axis',  # 坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                    trigger_on='mousemove|click',  # 同时鼠标移动和点击时触发。
                ),
                toolbox_opts=opts.ToolboxOpts(
                    is_show=True,  # 是否显示提示框组件，包括提示框浮层和axisPointer。

                )
            )
        )
        bar_map.render(r'G:\django\czxy\templates\ncov\最新世界地图\最新世界ncov疫情柱状图({}).html'.format(datetime.date.today()))
        # print('最新世界ncov疫情柱状图下载完成')
    #翻译


    # 保存到csv
    # 参数 data = 需要保存的数据
    #参数 title = 保存的名字
    # def export_csv(self,data,title):
    #     # print(cities)
    #     df = pd.DataFrame(self.cities)
    #     df.to_csv('{}{}.csv'.format(title,datetime.date.today()), index=False)

    def run(self):
        # self.data_info()
        # self.china_cumulative_data() #中国累计确诊数据
        # self.foreign_ncov()
        pass


# nc = Ncov()
# nc.run()

# item_contry['刚果（布）'] = 'The Republic of Congo'
# # print(item_contry)

