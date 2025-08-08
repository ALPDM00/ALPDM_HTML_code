from pyecharts import options as opts
from pyecharts.charts import Map, Map3D
from pyecharts.globals import ChartType
import random

# 1. 准备数据：各省名称及模拟数值（如GDP）
provinces = ["广东省", "山东省", "河南省", "四川省", "江苏省", "河北省"]
data = [(province, random.randint(3000, 20000)) for province in provinces]

# 2. 创建基础地图（2D）
def create_2d_map():
    map_2d = (
        Map(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(
            series_name="GDP（亿元）",
            data_pair=data,
            maptype="china",
            is_map_symbol_show=False,  # 不显示标记点
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中国各省经济分布图（2D）"),
            visualmap_opts=opts.VisualMapOpts(
                max_=20000,
                is_piecewise=True,  # 分段显示色阶
                range_color=["#CCD3D9", "#D4587A", "#DC364C"]  # 颜色梯度
            ),
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{b}: {c} 亿元")
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            # 高亮样式设置
            emphasis_opts=opts.EmphasisOpts(
                itemstyle_opts=opts.ItemStyleOpts(
                    border_color="#000",  # 高亮边框颜色
                    border_width=2,       # 边框加粗
                    area_color="#3be2fb"  # 高亮填充色
                ),
                label_opts=opts.LabelOpts(
                    is_show=True,         # 高亮时显示标签
                    color="#000",         # 标签字体颜色
                    font_size=12
                )
            )
        )
    )
    return map_2d

# 3. 创建3D地图（需额外安装 echarts-map3d 拓展）
def create_3d_map():
    map_3d = (
        Map3D(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add_schema(
            itemstyle_opts=opts.ItemStyleOpts(color="#1c3fbf", border_color="#070093"),
            map3d_label=opts.Map3DLabelOpts(is_show=False),
            light_opts=opts.Map3DLightOpts(is_main_shadow=True)  # 修正此处：main_shadow -> is_main_shadow
        )
        .add(
            series_name="GDP（亿元）",
            data_pair=data,
            type_=ChartType.BAR3D,  # 3D柱状效果
            bar_size=0.5,           # 柱子粗细
            shading="lambert"       # 光照渲染模式
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中国各省经济分布图（3D）"),
            visualmap_opts=opts.VisualMapOpts(max_=20000)
        )
    )
    return map_3d

# 4. 生成并渲染地图
map_2d = create_2d_map()
map_3d = create_3d_map()

# 保存为HTML
map_2d.render("china_map_2d.html")
map_3d.render("china_map_3d.html")