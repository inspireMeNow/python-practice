# from pyecharts import options as opts
# from pyecharts.charts import Map
# from pyecharts.globals import ChartType
# # 构造数据
# data = [("北京市", 1)]
# # 绘制地图
# m = (
#     Map()
#     .add(series_name='城市',data_pair=[('海淀区',650),('朝阳区',234),('房山区',134),('昌平区',68),('丰台区',123),('西城区',500),('大兴区',54),('东城区',21),('石景山区',9),('通州区',55),('顺义区',257)],maptype='北京')
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="中国地图", subtitle="包含北京市"),
#         visualmap_opts=opts.VisualMapOpts(max_=1)
#     )
# )
# m.render("北京市地图.html")
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Map
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
CurrentConfig.ONLINE_HOST
covid_data = pd.read_csv('DXYArea.csv')
# 保存地图
new_data = covid_data[covid_data['provinceName'] == '北京市']
print(new_data)
new_data = new_data[['cityName', 'city_confirmedCount']]
new_data = new_data.drop_duplicates(subset='cityName')
new_data = new_data.loc[new_data['cityName'] != '北京市']
city = new_data["cityName"].values.tolist()
print(new_data["cityName"].values)
nowConfirm = new_data["city_confirmedCount"].values.tolist()
data = []
i = 0
while i < len(city):
    data.append((city[i], nowConfirm[i]))
    i += 1
print(data)
m = Map()
m.add("城市", data,
      maptype="北京")
m.set_global_opts(
    title_opts=opts.TitleOpts(title="COVID-19中国现有地区现有确诊人数地图"),
    visualmap_opts=opts.VisualMapOpts(
        is_piecewise=True,
        pieces=[
            {
                "min": 50000,
                "label": '>50000',
                "color": "#893448"
            },  # 不指定 max，表示 max 为无限大
            {
                "min": 20000,
                "max": 49999,
                "label": '20000-49999',
                "color": "#ff585e"
            },
            {
                "min": 10000,
                "max": 19999,
                "label": '10000-19999',
                "color": "#fb8146"
            },
            {
                "min": 5000,
                "max": 9999,
                "label": '5000-9999',
                "color": "#ffA500"
            },
            {
                "min": 1000,
                "max": 4999,
                "label": '1000-4999',
                "color": "#ffb248"
            },
            {
                "min": 500,
                "max": 999,
                "label": '500-999',
                "color": "#fff2d1"
            },
            {
                "max": 499,
                "label": '0-499',
                "color": "#ffffff"
            }
        ]))
m.render("北京疫情地图.html")
