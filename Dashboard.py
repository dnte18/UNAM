import dash
import pandas as pd
from dash import dcc, html, Dash
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

template = pd.read_csv('C:/Users/U1028803/OneDrive - Sanofi/Documents/Sanofi/DashboardInteractivo/Template.csv', encoding = 'Latin-1', sep = ';')
Bu = list(template['BU'].unique())
KPI_cat = list(template['KPI_CATEGORY'].unique())
Territory = list(template['TERRITORY_NAME'].unique())
Franchise = list(template['FRANCHISE'].unique())
Producto = list(template['PRODUCTO'].unique())
Customer_id = list(template['CUSTOMER_ID'].unique())
Especialidad = list(template['ESPECIALIDAD'].unique())
Customer_id = list(template['CUSTOMER_ID'].unique())
Especialidad = list(template['ESPECIALIDAD'].unique())


app = dash.Dash(__name__)

app.layout = html.Div([
  #html.Img(src=logo_link, 
        #style={'margin':'30px 0px 0px 0px' }),
  html.H1('Emailing Segmentation Model Breakdowns'),
  html.Div( 
    children=[
    html.Div(
      children=[
      html.H2('Inserte sus especificaciones'),
      html.Br(),
      html.H3('Bussines Unity (BU)'),
      dcc.Dropdown(
        id='bu_unity_id',
        # Set up the Major Category options with the same label and value
        options=[{'label':bu, 'value':bu} for bu in Bu],
      style={'width':'200px', 'margin':'0 auto'}),
      html.Br(),
      html.H3('Categoría de KPI'),
      dcc.Dropdown(
        id='kpi_id',
        style={'width':'200px', 'margin':'0 auto'})
        ],
        style={'width':'350px', 'height':'350px', 'display':'inline-block', 
               'vertical-align':'top', 'border':'1px solid black', 'padding':'20px'}),
    html.Div(
      children=[
      dcc.Graph(id='medical_line')],
      style={'width':'700px', 'height':'650px','display':'inline-block'})
    ]),], 
  style={'text-align':'center', 'display':'inline-block', 'width':'100%'})


# Creamos el callback para los dropdowns 
@app.callback(
    Output('kpi_id', 'options'),
    Input('bu_unity_id', 'value'))


def update_kpi(bu_unity_id):

    bu_kpi = template[['BU', 'KPI_CATEGORY']].drop_duplicates()
    relevant_KPI = bu_kpi[bu_kpi['BU'] == major_cat_dd]['KPI_CATEGORY'].values.tolist()
    
    # Creación y retorno de opciones relevantes 
    formatted_relevant_KPI_options = [{'label':x, 'value':x} for x in relevant_KPI]
    return formatted_relevant_KPI_options

#Run app
if __name__ == '__main__':
    app.run_server(debug=True)
