import pandas as pd

def graphic(figure=None,x_values=None,y_values=None,title=None,x_axis_label=None,y_axis_label=None,data=None):

    if figure is 'bar_basic':

        import pandas as pd
        from bokeh.plotting import figure, output_file, show
        from bokeh.models import ColumnDataSource
        from bokeh.models.tools import HoverTool

        from bokeh.palettes import Spectral5
        from bokeh.transform import factor_cmap
        output_file('munitions_by_country.html')

        # raise Exception("xxx")
        source = ColumnDataSource(data)

        x_range = source.data['pclass'].tolist()
        p = figure(x_range=x_range)
        
        # color_map = factor_cmap(field_name='pclass', palette=Spectral5, factors=x_range)
        
        p.vbar(x='pclass', top='value', source=source, width=0.70)

        p.title.text = title
        p.xaxis.axis_label = x_axis_label
        p.yaxis.axis_label = y_axis_label

        hover = HoverTool()
        hover.tooltips = [
            ("@pclass Total", "@value Pasajeros")]

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
        from bokeh.plotting import figure
        from bokeh.transform import cumsum

        output_file("graphics/pie.html")

        data['angle'] = data['value'] / data['value'].sum() * 2 * pi
        data['color'] = Category20c[len(data)]

        p = figure(plot_height=350, title=title, toolbar_location=None,
                   tools="hover", tooltips="@class clase: @value")

        p.wedge(x=0, y=1, radius=0.4,
                start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
                line_color="white", fill_color='color', legend_field='class', source=data)

        p.axis.axis_label = None
        p.axis.visible = False
        p.grid.grid_line_color = None

        show(p)

if __name__ == "__main__":

    data = pd.read_excel(r'titanic3.xls')
    # print(df)
    df = pd.DataFrame(data)
    print("dataframe")
    print(df)
    print(df.size)

    print("Frecuencia clases titanic: ")
    frecuencia_de_clases_titanic = df.groupby('pclass')['pclass'].count() 
    print(frecuencia_de_clases_titanic)

    data = frecuencia_de_clases_titanic.reset_index(name='value')
    data['pclass'] = data['pclass'].astype('str')
    print("data")
    print(data)
    
    print("bar:")
    graphic(figure="bar_basic", title="Pasajeros segun su clase en el Titanic", x_axis_label="Clase", y_axis_label="# pasajeros", data=data)

    print("pie:")
    data = pd.Series(frecuencia_de_clases_titanic).reset_index(name='value').rename(columns={'index': 'class'})
    print(data)
    print(data["class"])
    graphic(figure="pie",title="Pasajeros segun su clase en el Titanic",data=data)

    pass