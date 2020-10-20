import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import webbrowser
from GooPyForDash import GooPy

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def initializeVariables(urlInput, keyWordInput):
    data = GooPy(url= urlInput, keyWords= keyWordInput).checkWebpageForWords()
    description = "Counting Words/Letters"
    dataDict = pd.DataFrame({"Object": data[0], "Times": data[1], "Listed Objects": data[0]})
    defineGraphAxes = px.bar(dataDict, x= f"Object", y= f"Times", color="Listed Objects", barmode="stack")
    title = f"Word Counter for: ({urlInput})"

    setUpHtml(title, description, defineGraphAxes)

def setUpHtml(title, description, defineGraphAxes):
    app.layout = html.Div(children=[
        html.H1(children=f'{title}'),
        html.Div(children=f"{description}"),
    
        dcc.Graph(
            id='example-graph',
            figure = defineGraphAxes
        )
    ])
    
    webbrowser.open("http://127.0.0.1:8050/")

if __name__ == '__main__':
    initializeVariables("URL", ["Keywords"])
    app.run_server(debug=True)
