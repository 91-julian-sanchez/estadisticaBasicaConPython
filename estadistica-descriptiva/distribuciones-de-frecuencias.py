import pandas as pd

def graphic(
        figure=None,
        x_values=None,
        y_values=None,
        title=None,
        x_axis_label=None,
        y_axis_label=None,
        data=None,
        x_field=None,
        y_field=None
):

    if figure is 'bar_basic':

        import pandas as pd
        from bokeh.plotting import figure, output_file, show
        from bokeh.models import ColumnDataSource
        from bokeh.models.tools import HoverTool

        from bokeh.palettes import Spectral5
        from bokeh.transform import factor_cmap
        output_file('munitions_by_country.html')

        source = ColumnDataSource(data)
        x_range = source.data[x_field].tolist()
        print(x_range)
        p = figure(x_range=x_range)

        # color_map = factor_cmap(field_name='pclass', palette=Spectral5, factors=x_range)

        p.vbar(x=x_field, top=y_field, source=source, width=0.70)

        p.title.text = title
        p.xaxis.axis_label = x_axis_label
        p.yaxis.axis_label = y_axis_label

        hover = HoverTool()
        hover.tooltips = [
            (f"@{x_field} Total", f"@{y_field} Pasajeros")]

        hover.mode = 'vline'

        p.add_tools(hover)

        # print(classes)
        show(p)

        # from bokeh.io import output_file, show
        # from bokeh.plotting import figure

        # output_file("graphics/bar_basic.html")

        # p = figure(x_range=x_values, plot_height=350, title=title,
        #            toolbar_location=None, tools="")

        # p.vbar(x=x_values, top=y_values, width=0.9)

        # p.xgrid.grid_line_color = None
        # p.y_range.start = 0

        # show(p)

    elif figure is 'pie':
        from math import pi
        from bokeh.io import output_file, show
        from bokeh.palettes import Category20c
        from bokeh.palettes import Category10
        from bokeh.palettes import BuPu
        from bokeh.plotting import figure
        from bokeh.transform import cumsum

        output_file("graphics/pie.html")

        data['angle'] = data['value'] / data['value'].sum() * 2 * pi
        data['color'] = BuPu[len(data)]

        p = figure(plot_height=350, title=title, toolbar_location=None,
                   tools="hover", tooltips=f"@{x_field}: @{y_field}")

        p.wedge(x=0, y=1, radius=0.4,
                start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
                line_color="white", fill_color='color', legend_field=x_field, source=data)

        p.axis.axis_label = None
        p.axis.visible = False
        p.grid.grid_line_color = None

        show(p)


if __name__ == "__main__":

    titanic3_data = pd.read_excel(r'titanic3.xls')
    df = pd.DataFrame(titanic3_data)
    print("dataframe")
    print(df)
    print(df.size)

    print("Frecuencia clases titanic: ")
    frecuencia_de_clases_titanic = df.groupby('pclass')['pclass'].count()
    print(frecuencia_de_clases_titanic)

    data = frecuencia_de_clases_titanic.reset_index(name='value')
    data['pclass'] = data['pclass'].astype('str')
    print("data =================================================")
    print(data)

    print("bar ==================================================")
    graphic(figure="bar_basic", title="Pasajeros segun su clase en el Titanic", x_axis_label="Clase", y_axis_label="# pasajeros", data=data,x_field='pclass',
        y_field='value')

    print("pie ==================================================")
    graphic(figure="pie",title="Pasajeros segun su clase en el Titanic",data=data,x_field='pclass',
        y_field='value')

    from bokeh.io import output_file, show
    from bokeh.palettes import BuPu3
    from bokeh.plotting import figure
    from bokeh.transform import factor_cmap

    output_file("bar_pandas_groupby_nested.html")
    import numpy as np
    df1 = pd.DataFrame(titanic3_data)
    df2 = df1.replace(np.nan,0)
    df2.pclass = df2['pclass'].astype(str)
    group = df2.groupby(['pclass', 'sex'])

    index_cmap = factor_cmap('pclass_sex', palette=BuPu3, factors=sorted(df2.pclass.unique()),start=0, end=1)
    p = figure(plot_width=800, plot_height=300, title="Pasajeros",
               x_range=group, toolbar_location=None, tooltips = [("Total", "@survived_count"), ("pclass, sex", "@pclass_sex")])

    p.vbar(x='pclass_sex', top='survived_count', width=1, source=group,line_color="white", fill_color=index_cmap )
    p.y_range.start = 0
    p.x_range.range_padding = 0.05
    p.xgrid.grid_line_color = None
    p.xaxis.axis_label = "Clases agrupada por genero"
    p.xaxis.major_label_orientation = 1.2
    p.outline_line_color = None

    show(p)

    pass