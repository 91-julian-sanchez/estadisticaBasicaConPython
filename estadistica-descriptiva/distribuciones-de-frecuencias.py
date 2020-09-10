import pandas as pd

def graphic(figure=None,x_values=None,y_values=None,title=None,data=None):

    if figure is 'bar_basic':

        from bokeh.io import output_file, show
        from bokeh.plotting import figure

        output_file("graphics/bar_basic.html")

        p = figure(x_range=x_values, plot_height=350, title=title,
                   toolbar_location=None, tools="")

        p.vbar(x=x_values, top=y_values, width=0.9)

        p.xgrid.grid_line_color = None
        p.y_range.start = 0

        show(p)

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
    frecuencia_de_clases_titanic = df["pclass"].value_counts(ascending=True)
    print(frecuencia_de_clases_titanic)

    print("bar:")
    x_values = []
    y_values = []

    for pclass, count in frecuencia_de_clases_titanic.iteritems():
        print(f"Clase {pclass}: {count}")
        x_values.append(f"class {pclass}")
        y_values.append(count)

    graphic(figure="bar_basic",x_values=x_values,y_values=y_values,title="Pasajeros segun su clase en el Titanic",)

    print("pie:")
    data = pd.Series(frecuencia_de_clases_titanic).reset_index(name='value').rename(columns={'index': 'class'})
    print(data)
    print(data["class"])
    graphic(figure="pie",title="Pasajeros segun su clase en el Titanic",data=data)

    pass