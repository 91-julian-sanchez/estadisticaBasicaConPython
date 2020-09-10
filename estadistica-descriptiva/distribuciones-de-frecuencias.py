import pandas as pd

def graphic(x_values,y_values,title=None):
    from bokeh.io import output_file, show
    from bokeh.plotting import figure

    output_file("bar_basic.html")

    p = figure(x_range=x_values, plot_height=350, title=title,
               toolbar_location=None, tools="")

    p.vbar(x=x_values, top=y_values, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    show(p)

if __name__ == "__main__":
    print("Hola estadistica descriptiva")
    data = pd.read_excel(r'titanic3.xls')
    # print(df)
    df = pd.DataFrame(data)
    print("dataframe")
    print(df)
    print(df.size)

    print("Frecuencia clases titanic: ")
    frecuencia_de_clases_titanic = df["pclass"].value_counts(ascending=True)
    print(type(frecuencia_de_clases_titanic))

    x_values = []
    y_values = []

    for pclass, count in frecuencia_de_clases_titanic.iteritems():
        print(f"Clase {pclass}: {count}")
        x_values.append(f"class {pclass}")
        y_values.append(count)

    graphic(x_values,y_values,"Pasajeros segun su clase en el Titanic")
    pass