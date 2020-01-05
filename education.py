from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Tab, Line, Map, Timeline, Grid, Scatter
import chart_studio.plotly as py
from plotly.offline import plot
import cufflinks as cf
import numpy as np
import plotly
from pyecharts.charts import Bar, Geo


choice_available = ['1、历年分省教育经费',
                    '2、历年分省高等教育每十万人人数',
                    '3、分省居民人均可支配收入',
                    '4、历年分省每10万人高中在校生数(人)',
                    '5、2017分省受教育情况',
                    '6、城乡划分家庭校内外支出占比',
                    '7、生均家庭教育支出（元）',
                    '8、城农家庭教育支出水平',
                    '9、家庭校内外支出占比',
                    '10、学科类校外培训参与率']

app = Flask(__name__)

#  a 制图函数
def timeline_map_a() -> Timeline:
    tl = Timeline()
    for i in range(2014, 2018):
        map0 = (
            Map()
                .add(
                "历年分省教育经费", list(zip(list(a.地区), list(a["{}".format(i)]))), "china", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年分省教育经费".format(i), subtitle=""),
                visualmap_opts=opts.VisualMapOpts(min_=1000000, max_=30000000),
            ))

        tl.add(map0, "{}年".format(i))
    return tl.render_embed()

# b
def timeline_map_b() -> Timeline:
    tl = Timeline()
    for i in range(2014, 2019):
        map1 = (
            Map()
                .add(
                "历年分省高等教育每十万人人数", list(zip(list(b.地区), list(b["{}".format(i)]))), "china", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年分省高等教育每十万人人数".format(i), subtitle=""),
                visualmap_opts=opts.VisualMapOpts(min_=1200, max_=5200),
            )
        )
        tl.add(map1, "{}年".format(i))
    return tl.render_embed()

# d
def timeline_map_d() -> Timeline:
    tl = Timeline()
    for i in range(2014, 2019):
        map1 = (
            Map()
                .add(
                "历年分省每10万人高中在校生数(人)", list(zip(list(d.地区), list(d["{}".format(i)]))), "china", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年分省每10万人高中在校生数(人)".format(i), subtitle=""),
                visualmap_opts=opts.VisualMapOpts(min_=1000, max_=4000),
            )
        )
        tl.add(map1, "{}年".format(i))
    return tl.render_embed()
# e
def bar_base_e() -> Bar:
    小学down = e['小学以下'].tolist()
    中学 = e['中学'].tolist()
    大学up = e['大学以上'].tolist()
    EY = e['地区'].tolist()
    CO = (
        Bar()
            .add_xaxis(EY)
            .add_yaxis("小学以下", 小学down)
            .add_yaxis("中学", 中学)
            .add_yaxis("大学以上", 大学up)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2017分省受教育情况（%）", subtitle="2017分省受教育情况"),
            toolbox_opts=opts.ToolboxOpts(),

            datazoom_opts=opts.DataZoomOpts(),
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),

        )

    )
    return CO.render_embed()
# f
def bar_base_f() -> Bar:
    校内 = f['校内'].tolist()
    校外 = f['校外'].tolist()
    FY = f['指标'].tolist()
    CO = (
        Bar()
            .add_xaxis(FY)
            .add_yaxis("校内", 校内)
            .add_yaxis("校外", 校外)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2017城乡及地区划分家庭教育校内外支出占比", subtitle="小学"),
            toolbox_opts=opts.ToolboxOpts(),

            datazoom_opts=opts.DataZoomOpts(),
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),

        )

    )
    return CO.render_embed()
# g
def bar_base_g() -> Bar:
    生均家庭教育支出 = g['生均家庭教育支出'].tolist()
    GY = g['地区'].tolist()
    CO = (
        Bar()
            .add_xaxis(GY)
            .add_yaxis("生均家庭教育支出", 生均家庭教育支出)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2017生均家庭教育支出（元）", subtitle="生均家庭教育支出"),
            toolbox_opts=opts.ToolboxOpts(),

            datazoom_opts=opts.DataZoomOpts(),
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),

        )

    )
    return CO.render_embed()
# h
def bar_base_h() -> Bar:
    学前 = h['学前'].tolist()
    小学 = h['小学'].tolist()
    初中 = h['初中'].tolist()
    普通高中 = h['普通高中'].tolist()
    中职 = h['中职'].tolist()
    HY = h['指标'].tolist()
    CO = (
        Bar()
            .add_xaxis(HY)
            .add_yaxis("学前", 学前)
            .add_yaxis("小学", 小学)
            .add_yaxis("初中", 初中)
            .add_yaxis("普通高中", 普通高中)
            .add_yaxis("中职", 中职)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2017城农家庭教育支出水平", subtitle="教育支出水平（元）"),
            toolbox_opts=opts.ToolboxOpts(),

            datazoom_opts=opts.DataZoomOpts(),
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),

        )

    )
    return CO.render_embed()
# j
def bar_base_j() -> Bar:
    j全国 = j['全国'].tolist()
    j农村 = j['农村'].tolist()
    j城镇 = j['城镇'].tolist()
    j东部 = j['东部'].tolist()
    j东北部 = j['东北部'].tolist()
    j中部 = j['中部'].tolist()
    j西部 = j['西部'].tolist()
    JY = j['阶段'].tolist()
    CO = (
        Bar()
            .add_xaxis(JY)
            .add_yaxis("全国", j全国)
            .add_yaxis("农村", j农村)
            .add_yaxis("城镇", j城镇)
            .add_yaxis("东部", j东部)
            .add_yaxis("东北部", j东北部)
            .add_yaxis("中部", j中部)
            .add_yaxis("西部", j西部)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="学科类校外培训参与率", subtitle="全国中小学生（%）"),
            toolbox_opts=opts.ToolboxOpts(),

            datazoom_opts=opts.DataZoomOpts(),
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),

        )

    )
    return CO.render_embed()

# x
def bar_base_x() -> Bar:
    x校内 = x['校内'].tolist()
    x校外 = x['校外'].tolist()
    xY = x['阶段'].tolist()
    CO = (
        Bar()
            .add_xaxis(xY)
            .add_yaxis("校内", x校内)
            .add_yaxis("校外", x校外)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2017全国家庭校内外支出占比", subtitle="家庭校内外支出占比（%）"),
            toolbox_opts=opts.ToolboxOpts(),

            datazoom_opts=opts.DataZoomOpts(),
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),

        )

    )
    return CO.render_embed()
@app.route('/', methods=['GET'])
def to_index():
    return render_template('index.html',)

@app.route("/index",methods=['POST','GET'])
def index():
    return render_template('details.html',
                           choice_available=choice_available,)

@app.route('/data', methods=['POST'])
def data_redirect() ->'html':
    # 描述：此函数的作用是根据用户的选择不同，重定向到不同的route，返回不同的页面
    # if-elif-else为条件语句； url = url_for("to_a"),url反向解析，通过视图函数名找到对应的url路径；
    # return redirect(url)执行重定向
    the_form_selected = request.form["the_form_selected"]
    if the_form_selected == '1、历年分省教育经费':
        url = url_for("to_a")
    elif the_form_selected == '2、历年分省高等教育每十万人人数':
        url = url_for("to_b")
    elif the_form_selected == '3、分省居民人均可支配收入':
        url = url_for("to_c")
    elif the_form_selected == '4、历年分省每10万人高中在校生数(人)':
        url = url_for("to_d")
    elif the_form_selected == '5、2017分省受教育情况':
        url = url_for("to_e")
    elif the_form_selected == '6、城乡划分家庭校内外支出占比':
        url = url_for("to_f")
    elif the_form_selected == '7、生均家庭教育支出（元）':
        url = url_for("to_g")
    elif the_form_selected == '8、城农家庭教育支出水平':
        url = url_for("to_h")
    elif the_form_selected == '9、家庭校内外支出占比':
        url = url_for("to_x")
    else:
        url = url_for("to_j")
    return redirect(url)

# a.html,b.html,c.html,d.html,e.html,f.html,g.html,h.html,j.html,x.html 的运行机制相同。
# 均是通过url_for()重定向到 a.html，并实现在 a.html中进行数据过滤筛选。
# 代码功能解释：
# pandas读取.csv 文件数据 ；dropna()；unique()使属性为唯一值，不重复；

# a.html --对应数据--> 教育经费-分省年度数据.csv
a = pd.read_csv('教育经费-分省年度数据.csv')
cf.set_config_file(offline=True, theme="ggplot")
@app.route('/to_a')
def to_a():
    the_title = '历年分省教育经费'
    the_word = "通过图表，我们可以很明显的看到中国东部以及东北部地区（到北京），这两个地区的教育经费每年都增长不少，并且本身基数并不低，中部地区处于一个正常的水平，介于两者之间，但是西部地区除了四川外，像新疆、青海只有四川的八分之一。北部地区如，内蒙古、黑龙江、吉林、辽宁教育经费投入甚少。其中，环顾整个中国，经济大省或者直辖市的教育经费投入巨大，尤其是沿海地区，拥有更多的教育经费。教育经费的增加，有利于优质教育资源的聚集。 "
    the_res = a.to_html()
    regions_available = list(a.地区.dropna().unique())
    return render_template('a.html',
                           the_title=the_title,
                           the_word=the_word,
                           the_select_region =regions_available,
                           choice_available=choice_available,
                           the_res = the_res,
                           the_plot=timeline_map_a(),
                           )

@app.route('/a_selector',  methods=['POST'])
def table_a() ->'html':
    the_region= request.form['the_region_selected']
    print(the_region)
    regions_available = list(a.地区.dropna().unique())
    dfs = a.query("地区=='{}'".format(the_region))
    data_str = dfs.to_html()
    the_title = '历年分省教育经费'
    the_word = "通过图表，我们可以很明显的看到中国东部以及东北部地区（到北京），这两个地区的教育经费每年都增长不少，并且本身基数并不低，中部地区处于一个正常的水平，介于两者之间，但是西部地区除了四川外，像新疆、青海只有四川的八分之一。北部地区如，内蒙古、黑龙江、吉林、辽宁教育经费投入甚少。其中，环顾整个中国，经济大省或者直辖市的教育经费投入巨大，尤其是沿海地区，拥有更多的教育经费。教育经费的增加，有利于优质教育资源的聚集。"
    return render_template('a.html',
                           the_res=data_str,
                           the_title=the_title,
                           the_word=the_word,
                           choice_available=choice_available,
                           the_select_region=regions_available,
                           the_plot = timeline_map_a(),
                           )

# b.html
b = pd.read_csv('高等教育分省年度数据.csv')
cf.set_config_file(offline=True, theme="ggplot")
@app.route('/to_b')
def to_b():
    the_title = "历年分省高等教育每十万人人数"
    the_word = "北京、天津、陕西、上海、吉林拥有着众多高等教育院校和学生，这五个地方，每十万人均有3000人以上正在接受高等教育，不计算人口总量因素，这从侧面反映出这些地区的高等教育较为完善，高等教育人才密度更高。"
    regions_available = list(b.地区.dropna().unique())
    the_res = b.to_html()
    return render_template('b.html',
                           the_title=the_title,
                           the_word=the_word,
                           the_select_region=regions_available,
                           choice_available=choice_available,
                           the_res=the_res,
                           the_plot=timeline_map_b(),
                           )
@app.route('/b_selector',  methods=['POST'])
def table_b() ->'html':
    the_region= request.form['the_region_selected']
    print(the_region)
    regions_available = list(b.地区.dropna().unique())
    dfs = b.query("地区=='{}'".format(the_region))
    data_str = dfs.to_html()
    the_title = "历年分省高等教育每十万人人数"
    the_word = "北京、天津、陕西、上海、吉林拥有着众多高等教育院校和学生，这五个地方，每十万人均有3000人以上正在接受高等教育，不计算人口总量因素，这从侧面反映出这些地区的高等教育较为完善，高等教育人才密度更高。"
    return render_template('b.html',
                           the_res=data_str,
                           choice_available=choice_available,
                           the_select_region=regions_available,
                           the_title=the_title,
                           the_word=the_word,
                           the_plot=timeline_map_b(),
                           )

# c.html
c = pd.read_csv('居民人均可支配收入分省年度数据.csv')
cf.set_config_file(offline=True, theme="ggplot")

@app.route('/to_c')
def to_c():
    the_title = '分省居民人均可支配收入'
    the_word = "居民人均可支配收入前五分别是上海、北京、浙江、天津、江苏，这五个地区中的上海、天津、北京，这三个地区的高等教育人数亦是前五，但是高中的情况却有所相反，教育经费投入少以及居民人均可支配稍低的地区，反而高中学生的密度大。"
    regions_available = list(c.地区.dropna().unique())
    the_res = c.to_html()
    return render_template('c.html',
                           the_title=the_title,
                           the_word=the_word,
                           the_select_region=regions_available,
                           choice_available=choice_available,
                           the_res=the_res,
                           )
@app.route('/c_selector',  methods=['POST'])
def table_c() ->'html':
    the_region= request.form['the_region_selected']
    print(the_region)
    regions_available = list(c.地区.dropna().unique())
    dfs = c.query("地区=='{}'".format(the_region))
    data_str = dfs.to_html()
    return render_template('c.html',
                           the_res=data_str,
                           choice_available=choice_available,
                           the_select_region=regions_available,
                           )

# d.html
d = pd.read_csv('高中分省年度数据.csv')
cf.set_config_file(offline=True, theme="ggplot")

@app.route('/to_d')
def to_d():
    the_title = '历年分省每10万人高中在校生数(人)'
    the_word = "教育经费较少的地区，反而比教育经费多的地区具有更多的高中在校生数（每10万人）。随着时间的推移，高中在校生密度大的地区开始向西部和南部地区转移，呈现中部向四周扩散的趋势。"
    regions_available = list(d.地区.dropna().unique())
    the_res = d.to_html()
    return render_template('d.html',
                           the_title=the_title,
                           the_word=the_word,
                           the_select_region=regions_available,
                           choice_available=choice_available,
                           the_res=the_res,
                           the_plot=timeline_map_d(),
                           )
@app.route('/d_selector',  methods=['POST'])
def table_d() ->'html':
    the_region= request.form['the_region_selected']
    print(the_region)
    regions_available = list(d.地区.dropna().unique())
    dfs = d.query("地区=='{}'".format(the_region))
    data_str = dfs.to_html()
    the_title = '历年分省每10万人高中在校生数(人)'
    the_word = "教育经费较少的地区，反而比教育经费多的地区具有更多的高中在校生数（每10万人）。随着时间的推移，高中在校生密度大的地区开始向西部和南部地区转移，呈现中部向四周扩散的趋势。"
    return render_template('d.html',
                           the_res=data_str,
                           the_title=the_title,
                           the_word=the_word,
                           choice_available=choice_available,
                           the_select_region=regions_available,
                           the_plot=timeline_map_d(),
                           )

# e.html
e = pd.read_csv('2017分省受教育情况.csv')
cf.set_config_file(offline=True, theme="ggplot")

@app.route('/to_e')
def to_e():
    the_title = '2017分省受教育情况'
    the_word = "该图是我国2017年分省学历分布状况，教育经费多，以及居民可支配收入越高的地区，那么该地区的小学及以下的人口占比就会更少，而大学以上的占比就会呈现出很大的优势，尤其是作为我国的首都北京。以及我国经济重点城市上海，这两个地区都有着比别的地区更加多的高等人才。而中学的占比，所有地区都差不多，只有西藏这一地区，占比比较低。这也能说明我国推行的义务教育，很大程度上保障了每个人到中学的受教育权利。"
    regions_available = list(e.地区.dropna().unique())
    the_res = e.to_html()
    return render_template('e.html',
                           the_title=the_title,
                           the_word=the_word,
                           the_select_region=regions_available,
                           choice_available=choice_available,
                           the_res=the_res,
                           the_plot=bar_base_e(),
                           )
@app.route('/e_selector',  methods=['POST'])
def table_e() ->'html':
    the_region= request.form['the_region_selected']
    print(the_region)
    regions_available = list(e.地区.dropna().unique())
    dfs = e.query("地区=='{}'".format(the_region))
    data_str = dfs.to_html()
    the_title = '2017分省受教育情况'
    the_word = "该图是我国2017年分省学历分布状况，教育经费多，以及居民可支配收入越高的地区，那么该地区的小学及以下的人口占比就会更少，而大学以上的占比就会呈现出很大的优势，尤其是作为我国的首都北京。以及我国经济重点城市上海，这两个地区都有着比别的地区更加多的高等人才。而中学的占比，所有地区都差不多，只有西藏这一地区，占比比较低。这也能说明我国推行的义务教育，很大程度上保障了每个人到中学的受教育权利。"
    return render_template('e.html',
                           the_res=data_str,
                           the_title=the_title,
                           the_word=the_word,
                           choice_available=choice_available,
                           the_select_region=regions_available,
                           the_plot=bar_base_e(),
                           )
# f.html
f = pd.read_csv('城乡划分家庭校内外支出占比（小学）.csv')
cf.set_config_file(offline=True, theme="ggplot")

@app.route('/to_f')
def to_f():
    the_title = '城乡划分家庭校内外支出占比'
    the_word = "通过此图可以看到小学时期农村比城市家庭教育校内支出占比高很多，以及经济较好的地区的家庭教育支出校内占比会比经济稍差的地区低。由此可见，经济发达，居民人均可支配更高的地区，教育支出校外占比会更加高。"
    regions_available = list(f.指标.dropna().unique())
    the_res = f.to_html()
    return render_template('f.html',
                           the_title=the_title,
                           the_word=the_word,
                           the_select_region=regions_available,
                           choice_available=choice_available,
                           the_res=the_res,
                           the_plot=bar_base_f(),
                           )

@app.route('/f_selector',  methods=['POST'])
def table_f() ->'html':
    the_region= request.form['the_region_selected']
    print(the_region)
    regions_available = list(f.指标.dropna().unique())
    dfs = f.query("指标=='{}'".format(the_region))
    data_str = dfs.to_html()
    the_title = '城乡划分家庭校内外支出占比'
    the_word = "通过此图可以看到小学时期农村比城市家庭教育校内支出占比高很多，以及经济较好的地区的家庭教育支出校内占比会比经济稍差的地区低。由此可见，经济发达，居民人均可支配更高的地区，教育支出校外占比会更加高。"
    return render_template('f.html',
                           the_res=data_str,
                           the_title=the_title,
                           the_word=the_word,
                           choice_available=choice_available,
                           the_select_region=regions_available,
                           the_plot=bar_base_f(),
                           )


# g.html
g = pd.read_csv('地区划分家庭教育支出水平（义务教育阶段） .csv')
cf.set_config_file(offline=True, theme="ggplot")

@app.route('/to_g')
def to_g():
    the_title = '生均家庭教育支出（元）'
    the_word = "高等教育密度大，人才多的地方，生均家庭教育支出会比别的地区多。"
    regions_available = list(g.地区.dropna().unique())
    the_res = g.to_html()
    return render_template('g.html',
                           the_title=the_title,
                           the_word=the_word,
                           the_select_region=regions_available,
                           choice_available=choice_available,
                           the_res=the_res,
                           the_plot=bar_base_g(),
                           )
@app.route('/g_selector',  methods=['POST'])
def table_g() ->'html':
    the_region= request.form['the_region_selected']
    print(the_region)
    regions_available = list(g.地区.dropna().unique())
    dfs = g.query("地区=='{}'".format(the_region))
    data_str = dfs.to_html()
    the_title = '生均家庭教育支出（元）'
    the_word = "高等教育密度大，人才多的地方，生均家庭教育支出会比别的地区多。"
    return render_template('g.html',
                           the_res=data_str,
                           the_title=the_title,
                           the_word=the_word,
                           choice_available=choice_available,
                           the_select_region=regions_available,
                           the_plot=bar_base_g(),
                           )


# h.html
h = pd.read_csv('城农划分家庭教育支出水平.csv')
cf.set_config_file(offline=True, theme="ggplot")

@app.route('/to_h')
def to_h():
    the_title = '城农家庭教育支出水平'
    the_word = "随着教育程度的提高，所要花费的金额也会不断上涨。跨过了义务教育阶段，来到高中后，无论是农村还是城市，家庭教育支出都会迎来大幅上涨。其中，城市在教育各阶段都会比农村支出高得多，义务教务阶段差距几乎高达一倍。"
    regions_available = list(h.指标.dropna().unique())
    the_res = h.to_html()
    return render_template('h.html',
                           the_title=the_title,
                           the_word=the_word,
                           the_select_region=regions_available,
                           choice_available=choice_available,
                           the_res=the_res,
                           the_plot=bar_base_h(),
                           )
@app.route('/h_selector',  methods=['POST'])
def table_h() ->'html':
    the_region= request.form['the_region_selected']
    print(the_region)
    regions_available = list(h.指标.dropna().unique())
    dfs = h.query("指标=='{}'".format(the_region))
    data_str = dfs.to_html()
    the_title = '城农家庭教育支出水平'
    the_word = "随着教育程度的提高，所要花费的金额也会不断上涨。跨过了义务教育阶段，来到高中后，无论是农村还是城市，家庭教育支出都会迎来大幅上涨。其中，城市在教育各阶段都会比农村支出高得多，义务教务阶段差距几乎高达一倍。"
    return render_template('h.html',
                           the_res=data_str,
                           the_title=the_title,
                           the_word=the_word,
                           choice_available=choice_available,
                           the_select_region=regions_available,
                           the_plot=bar_base_h(),
                           )

# x.html
x = pd.read_csv('阶段划分家庭校内外支出占比.csv')
cf.set_config_file(offline=True, theme="ggplot")

@app.route('/to_x')
def to_x():
    the_title = '家庭校内外支出占比'
    the_word = "从全国平均家庭教育支出来看，家庭教育支出主要是以校内支出为主。"
    regions_available = list(x.阶段.dropna().unique())
    the_res = x.to_html()
    return render_template('x.html',
                           the_title=the_title,
                           the_word=the_word,
                           the_select_region=regions_available,
                           choice_available=choice_available,
                           the_res=the_res,
                           the_plot=bar_base_x(),
                           )
@app.route('/x_selector',  methods=['POST'])
def table_x() ->'html':
    the_region= request.form['the_region_selected']
    print(the_region)
    regions_available = list(x.阶段.dropna().unique())
    dfs = x.query("指标=='{}'".format(the_region))
    data_str = dfs.to_html()
    the_title = '家庭校内外支出占比'
    the_word = "从全国平均家庭教育支出来看，家庭教育支出主要是以校内支出为主。"
    return render_template('x.html',
                           the_res=data_str,
                           the_title=the_title,
                           the_word=the_word,
                           choice_available=choice_available,
                           the_select_region=regions_available,
                           the_plot=bar_base_x(),
                           )

# j.html
j = pd.read_csv('全国中小学生学科类校外培训参与率.csv')
cf.set_config_file(offline=True, theme="ggplot")

@app.route('/to_j')
def to_j():
    the_title = '学科类校外培训参与率'
    the_word = "综合全国来看，无论是农村还是城市，每个求学阶段都有校外培训的需求，但是校外培训参与率有所不同。其中，校外培训参与率随着教学阶段的递进有一定程度的上涨，城市的上涨幅度比农村的上涨幅度更高，校外培训的需求增长更快，同时在每一个求学阶段，城市的校外培训需求都比农村要高。按照地区划分来看，东北部地区的校外培训参与率在每个求学阶段都比东部、中部、西部地区大幅领先。同时东北部地区也是教育经费投入较多，居民收入较多的地区。"
    regions_available = list(j.阶段.dropna().unique())
    the_res = j.to_html()
    return render_template('j.html',
                           the_title=the_title,
                           the_word=the_word,
                           the_select_region=regions_available,
                           choice_available=choice_available,
                           the_res=the_res,
                           the_plot=bar_base_j(),
                           )
@app.route('/j_selector',  methods=['POST'])
def table_j() ->'html':
    the_region= request.form['the_region_selected']
    print(the_region)
    regions_available = list(j.阶段.dropna().unique())
    dfs = j.query("阶段=='{}'".format(the_region))
    data_str = dfs.to_html()
    the_title = '学科类校外培训参与率'
    the_word = "综合全国来看，无论是农村还是城市，每个求学阶段都有校外培训的需求，但是校外培训参与率有所不同。其中，校外培训参与率随着教学阶段的递进有一定程度的上涨，城市的上涨幅度比农村的上涨幅度更高，校外培训的需求增长更快，同时在每一个求学阶段，城市的校外培训需求都比农村要高。按照地区划分来看，东北部地区的校外培训参与率在每个求学阶段都比东部、中部、西部地区大幅领先。同时东北部地区也是教育经费投入较多，居民收入较多的地区。"
    return render_template('j.html',
                           the_title=the_title,
                           the_word=the_word,
                           the_res=data_str,
                           choice_available=choice_available,
                           the_select_region=regions_available,
                           the_plot=bar_base_j(),
                           )

if __name__ == '__main__':
    app.run(debug=True)
