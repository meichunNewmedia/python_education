# python_education

## 主题：教育经费以及收入差距对教育需求造成的影响

代码Github :

[代码](https://github.com/meichunNewmedia/python_education/blob/master/final.zip)

pythonanywhere：
[http://meichun.pythonanywhere.com/](http://meichun.pythonanywhere.com/)

项目详情
[了解更多](https://github.com/meichunNewmedia/python_education/blob/master/details.md)


##### 主要内容包括：项目背景、数据来源、可视化视图、研究结果四个部分

#### 项目背景

> 随着我国社会经济的不断发展，民众对教育需求的增长和市场力量的发展，私人教育投入在教育总经费中所占比重不断上升。同时，随着人群之间的收入差距拉大以及家庭个性化、多元化的教育需求，不同家庭背景的学生在校内和校外享受到的教育机会和教育资源开始分化，由此可能造成新的教育不公平。因此，为了对全国的教育投入有一个全面的把握，不仅需要政府和学校等教育机构的教育经费数据，也需要知道家庭对子女教育的投入。

#### 数据来源

- 艾瑞网
- 中国国家统计局
- 世界银行
- 北京大学中国教育财政科学研究所
- CHFS

#### Flask-app的使用价值

将可视化的图表有序呈现，使图表故事脉络更加清晰，体验更佳！

#### 主要的特点：

1、首页为动态星空背景图，点击“开始探索”进入主题

2、详情页完整地呈现出项目总体概要

3、详情页有下拉框，可以筛选到用户想要详细了解的图表内容，可视化图丰富多样，共有10张

4、图表页面还有一个下拉框，可以再一次筛选出详细的数据内容

5、图表页面设有跳转到详情页的“点击此处查看详情”的按钮，实现用户在任意页面跳转的功能

#### 关于Flask-app


url个数 | html个数 | 图表个数
---|--- |---
23个 | 13个 | 10个

##### 四个主要的控件：
* 两个超链接：首页的“开始探索”与“点击此处查看详情”都用到url_for 反解析的方法对应到相应的路由。
* 两个菜单：数据查询“菜单1”与数据筛选“菜单2”的原理不同，菜单1是通过重定向的方法返回不同页面，而菜单2是通过函数过滤筛选出来的。

##### 具体页面描述与参数传递详情

###### url=”/”  GET （index.html）

页面描述：页面描述：首先GET index.html,此页面为首页，以动态的星空图为背景，显示主题名和“开始探索”按钮，进入(/details)详情页。

参数传递：前端通过<a href=“{{ url_for(“index”)}}”>,使用url_for()反解析,通过视图函数访问对应的路由访问到后端@app.route(‘/index’),并执行return render_template('details.html')

###### Url=”/index”   POST 、GET （details.html）

- 页面描述：该页为详情页，包含项目背景、数据来源、数据查询、研究成果四个部分。其中数据查询部分设有一个select下拉菜单（记为菜单1），其中option选项为该项目所有数据表的题目,并按数字顺序排列，用户通过按顺序查看，图文结合，便于梳理脉络。

- 参数传递：option选项通过jinja2 {% %} for循环语句赋值，循环遍历后端提供的选项列表产生，列表是有序的，故可以对选项进行排序，前端通过<form>表单里的提交按钮传递参数,action=’/data’，访问到后端@app.route(‘/data’),并执行自定义函数data_redirect()。此函数的作用是：根据用户的选择不同，重定向到不同的route，返回不同的页面。使用request.form获取以POST方式提交的数据（接收Form提交来的数据）,再通过“if...elif...else”条件语句对数据进行判断，url反向解析，通过视图函数名找到对应的url路径，return redirect(url)执行重定向，返回到不同的页面

例如：
if the_form_selected == '1、历年分省教育经费':
    url = url_for("to_a")
return redirect(url)

###### Url=“/to_a”“/to_b”“/to_c”“/to_d”“/to_e”“/to_f”“/to_g”“/to_h”“/to_j” “/to_x” 对应到页面以base.html为基模板继承的： a.html 、b.html 、c.html 、d.html 、e.html 、f.html 、g.html 、h.html、j.html 、x.html 

- 页面描述：返回的这些页面，样式、结构相同，均继承基模板。相比详情页，相同点是都有标题、项目背景、数据来源、“数据查询”（菜单1）。不同点是：少了关于“研究成果”部分的大多数文字描述，多了小标题、图表、对图表的文字描述、表格筛选菜单（记为“菜单2”）、以及可以返回详情页的“点击此处查看详情”超链接（设置在“主题背景”之下）。

- 参数传递：“点击此处查看详情”超链接是通过href="{{url_for('index')}}反解析，对应到@app.route（‘/index’）访问详情页。用户通过不同选择返回不同的页面，由于每个图表需要传递不同的the_title标题 和 the_word文字描述等每张图表特有的数值，故代码无法实现重复利用。后端通过赋值，传递参数到前端{{the_title}} {{the_word}} 等变量。


###### url=“/a_selector”“/b_selector”“c_selector”“/d_selector”“/e_selector”“/f_selector”“/g_selector”“h_selector”“/j_selector”“/x_selector”
对应到页面以base.html为基模板继承的： a.html 、b.html 、c.html 、d.html 、e.html 、f.html 、g.html 、h.html、j.html 、x.html

- 页面描述：该页面返回用户筛选的结果,由于数据并不复杂，实际作用不大。

- 数据传递：表格筛选菜单（菜单2）的option选项是循环遍历表头的属性值赋值，当用户选择并按下“筛选”按钮，<form>表单以POST方式提交的数据，数据传递到后端，query("地区=='{}'"对数据进行过滤，将过滤后的数据返回到{{the_form|safe }}。

