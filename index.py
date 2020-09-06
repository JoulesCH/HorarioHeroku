import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']

df  = pd.read_csv('Cleande_df.csv')
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
first = [{'label': '-','value':'all'}]
group_dict = [{'label': group,'value':group} for group in df['Grupo'].unique()]
group_dict = first + group_dict
app.title = 'ESFM | Horario'

app.layout = html.Div( children = [
    html.H3(children = 'Filtrar por grupo'),
    html.Div(
        children = dcc.Dropdown(id = 'Carrera', options = [{'label':'Ingeniería Matemática',
                                                            'value':'LIM'},
                                                            {'label':'Física y Matemáticas',
                                                            'value':'LFM'}
                                                            ],
                                                value = 'LIM',
                                                searchable = False,
                                                clearable = False),
        style = {
            'margin':40,
            'width': 250,
            'margin-bottom':10,
            'margin-top': 20
        }
    
    ),
    html.Div(
        children = dcc.Dropdown(id = 'Semestre', #options = group_dict,
                                                value = '1MV2',
                                                searchable = False,
                                                clearable = False),
        style = {
            'margin':40,
            'width': 250,
            'margin-top':0,
            'margin-bottom':20
        }
    
    ),

    html.Table(id = 'First_table',style = {
                                            'textAlign': 'center',
                                            'margin':80,
                                            'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            'margin-bottom':40,
                                            'width': 1100
                                           }
    ),
    html.H3(children = 'Filtrar por materia'),
    html.Div(
        children = dcc.Dropdown(id = 'Carrera_2', options = [{'label':'Ingeniería Matemática',
                                                            'value':'LIM'},
                                                            {'label':'Física y Matemáticas',
                                                            'value':'LFM'}
                                                            ],
                                                value = 'LIM',
                                                searchable = False,
                                                clearable = False),
        style = {
            'margin':40,
            'width': 250,
            'margin-bottom':10,
            'margin-top': 20
        }
    
    ),
    html.Div(
        children = dcc.Dropdown(id = 'Materia', #options = group_dict,
                                                value = '1MV2',
                                                #searchable = False,
                                                clearable = False),
        style = {
            'margin':40,
            'width': 450,
            'margin-top':0,
            'margin-bottom':20
        }
    
    ),

    html.Table(id = 'second_table',style = {
                                            'textAlign': 'center',
                                            'margin':80,
                                            'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            'margin-bottom':40,
                                            'width': 1100
                                           }
    ),
    html.H3(children = 'Organiza tu horario'),
    html.Div(
        children = dcc.Dropdown(id = 'Carrera_3', options = [{'label':'Ingeniería Matemática',
                                                            'value':'LIM'},
                                                            {'label':'Física y Matemáticas',
                                                            'value':'LFM'}
                                                            ],
                                                value = 'LIM',
                                                searchable = False,
                                                clearable = False),
        style = {
            'margin':40,
            'width': 250,
            'margin-bottom':10,
            'margin-top': 20
        }
    
    ),
    html.Div(
        children = dcc.Dropdown(id = 'Materia_y_grupo', #options = group_dict,
                                                value = ['1MV2','0'],
                                                #searchable = False,
                                                multi=True,
                                                clearable = True),
        style = {
            'margin':40,
            'width': 'auto',
            'margin-top':0,
            'margin-bottom':20
        }
    
    ),

    html.Table(id = 'third_table',style = {
                                            'textAlign': 'center',
                                            'margin':80,
                                            'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            'margin-bottom':40,
                                            'width': 1100
                                           }
    ),
    html.Footer(children= [
                                         html.Div(children = ['Made by Joules CH -  ',
                                                                html.A('GitHub',href = 'https://github.com/JoulesCH') 
                                                        ], 
                                                style = {
                                                    'textAlign': 'center',
                                                    'margin': 10,
                                                    'margin-left': 'auto',
                                                    'margin-right': 'auto'
                                                 }
                                         )
                                    ],
                                style={
                                        'width': 777,
                                        'border-top-style': 'double',
                                        'border-top-color': '#1866B9',
                                        'margin-left': 'auto',
                                        'margin-right': 'auto',
                                        'margin-top': 15
                                        
                                }
                    )


   

]
)

@app.callback(Output('Semestre','options'),[Input('Carrera','value')])
def set_dict(carrera):
    global group_dict
    first = [{'label': '-','value':'all'}]
    group_dict = [{'label': group,'value':group} for group in df[df['Programa']== carrera]['Grupo'].unique()]
    group_dict = first + group_dict
    return group_dict

@app.callback(Output('Materia','options'),[Input('Carrera_2','value')])
def set_2dict(carrera):
    global group_dict
    first = [{'label': '-','value':'all'}]
    group_dict = [{'label': materia,'value':materia} for materia in df[df['Programa']== carrera]['Unidad de aprendizaje'].unique()]
    group_dict = first + group_dict
    return group_dict

@app.callback(Output('Materia_y_grupo','options'),[Input('Carrera_3','value')])
def set_3dict(carrera):
    group_dict = []
    first = [{'label': '-','value':'all'}]
    for ind in range(df.shape[0]):
        grupo = df.loc[ind,'Grupo']
        materia = df.loc[ind,'Unidad de aprendizaje']
        group_dict.append( {'label': materia +' '+ grupo,'value':materia+'*'+grupo})
    group_dict = first + group_dict
    return group_dict

@app.callback(Output('First_table','children'),[Input('Semestre','value'),Input('Carrera','value')])
def generate_table(semestre,carrera, dataframe = df, max_rows = 100):
    if semestre:
        if semestre != 'all':
            dataframe = dataframe[(dataframe['Programa']==carrera) & (dataframe['Grupo'] == semestre)]
        else:
            dataframe = dataframe[(dataframe['Programa']==carrera)]
        dataframe = dataframe.drop('Unnamed: 0',axis = 1).iloc[:,[0,1,3,5,6,7,8,9,10,16]]
        return [ html.Thead(
                    html.Tr([html.Th(col) for col in dataframe.columns])
                ),

                html.Tbody([html.Tr([
                        html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                    ]) for i in range(min(len(dataframe), max_rows))
                ], style = {'color':'#414242' })

            ]

@app.callback(Output('second_table','children'),[Input('Materia','value'),Input('Carrera_2','value')])
def generate_2table(materia,carrera, dataframe = df, max_rows = 100):
    if materia:
        dataframe = dataframe[(dataframe['Programa']==carrera) & (dataframe['Unidad de aprendizaje']==materia)]

        dataframe = dataframe.drop('Unnamed: 0',axis = 1).iloc[:,[0,1,3,5,6,7,8,9,10,15,16]]
        return [ html.Thead(
                    html.Tr([html.Th(col) for col in dataframe.columns])
                ),

                html.Tbody([html.Tr([
                        html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                    ]) for i in range(min(len(dataframe), max_rows))
                ], style = {'color':'#414242' })

            ]

@app.callback(Output('third_table','children'),[Input('Materia_y_grupo','value'),Input('Carrera_3','value')])
def generate_3table(materia_grupo,carrera, dataframe = df, max_rows = 100):
    dataframe = df
    new_df = pd.DataFrame()
    for materia_g in materia_grupo:
        materia = materia_g.split('*')[0]
        try:
            grupo = materia_g.split('*')[1]
        except:
            grupo = ''

        new_df = pd.concat([  new_df, df[ (df['Unidad de aprendizaje']== materia) & (df['Programa']== carrera) & (df['Grupo']== grupo)]  ])
    
    dataframe = new_df
    try:
        dataframe = dataframe.drop('Unnamed: 0',axis = 1).iloc[:,[0,1,3,5,6,7,8,9,10,16]]
    except:
        dataframe = df[df['Unidad de aprendizaje'] == ''].drop('Unnamed: 0',axis = 1).iloc[:,[0,1,3,5,6,7,8,9,10,16]]
    if True:
        
    #     dataframe = dataframe[(dataframe['Programa']==carrera) & (dataframe['Unidad de aprendizaje']==materia)]

    #     dataframe = dataframe.drop('Unnamed: 0',axis = 1).iloc[:,[0,1,3,5,6,7,8,9,10,16]]
        return [ html.Thead(
                    html.Tr([html.Th(col) for col in dataframe.columns])
                ),

                html.Tbody([html.Tr([
                        html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                    ]) for i in range(min(len(dataframe), max_rows))
                ], style = {'color':'#414242' })

            ]

if __name__ == '__main__':
    app.run_server(debug = True)