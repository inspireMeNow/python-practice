from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline,Grid
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
import pandas as pd
data=pd.read_csv('微博热搜.csv')
tl = Timeline({"theme": ThemeType.MACARONS})
for i in range(20):
    bar = (
        Bar({"theme": ThemeType.MACARONS})
        .add_xaxis(list(data['内容'])[i*10:i*10+10][::-1])
        .add_yaxis("微博热搜榜", list(data['热度'])[i*10:i*10+10][::-1])
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts("{}".format(list(data['时间'])[i*10]),pos_right='0%',pos_bottom='15%'),
            xaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=True),
                position='top',
                name_gap=10,
                boundary_gap=['20%', '20%']),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True),
                                     axislabel_opts=opts.LabelOpts(color='#FF7F50')),)
        .set_series_opts(label_opts=opts.LabelOpts(position="right",color='#9400D3'))
    )
    grid = (
        Grid()
        .add(bar, grid_opts=opts.GridOpts(pos_left="25%",pos_right="0%"))
    )
    tl.add(grid, "{}年".format(i))
    tl.add_schema(
        play_interval=1000,   #播放速度
        is_timeline_show=True,  #是否显示 timeline 组件
        is_auto_play=True,
    )
tl.render_notebook()
