import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df  = pd.read_csv('Cleande_df_correos.csv')
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server = app.server
first = [{'label': '-','value':'all'}]
group_dict = [{'label': group,'value':group} for group in df['Grupo'].unique()]
group_dict = first + group_dict
app.title = 'ESFM | Horario'
loc_list = [1,2,4,6,7,8,9,10,11,17,18]
colors = {
    'text': '#1866B9',
    'background': '#FFFFFF'
}

style_subtitles= {
    'margin-left':100,
    'margin-right':'auto',
    'width': 300

}
style_bar = {  
    'border-top-style': 'double',
    'border-top-color': '#79003E',#'#1866B9',
    'width': 900,
    'margin-left': 'auto',
    'margin-right': 'auto'
}
app.layout = html.Div( children = [
    html.Header(
        children = [html.Br(),html.H1('Información de horarios - ESFM', style={'margin-bottom':0}),html.P(children = 'Página no oficial del IPN', style = {'color':'#959595'}), html.Br()],
        style= {
           # 'backgroundColor': '#79003E',#colors['text'],#colors['background'],
            'color': '#79003E',#'#FFFFFF',#colors['text'],
            'margin-top':0,
            'margin-bottom':0,
            'margin-left':'auto',
            'margin-right':'auto',
            'text-align':'center',
            'margin-left':0,
            'height':130
            #'width':730
        }
    ),
    # html.Div(style= {
    #         'backgroundColor': '#79003E',#colors['text'],#colors['background'],
    #         'height':10,
    #         'margin-left':30,
    #         ''
    #         }
    # ),
    html.H3(children = 'Filtrar por grupo', style = style_subtitles),
    html.Div('', style = style_bar),
    html.Div(children = [
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
                'width': 200,
                'margin-bottom':10,
                'margin-top': 20,
                'margin-right':10
                
            },
            className = 'six columns'
        
        ),
        html.Div(
            children = dcc.Dropdown(id = 'Semestre', #options = group_dict,
                                                    value = '1MV2',
                                                    searchable = False,
                                                    clearable = False),
            style = {
                'margin':40,
                'width': 150,
                'margin-top':20,
                'margin-bottom':20,
                'margin-left':0
            },
            className = 'six columns'
    
    )],className = 'row', style = {'width': 500, 'margin-left':'auto', 'margin-right':'auto'}),

    html.Table(id = 'First_table',style = {
                                            'textAlign': 'center',
                                            'margin':80,
                                            'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            'margin-bottom':40,
                                            'width': 250,
                                            'height':'auto'
                                           }
    ),
   
    html.H3(children = 'Filtrar por materia', style = style_subtitles),
    html.Div('', style = style_bar),
    html.Div(children=[
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
            'width': 200,
            'margin-bottom':10,
            'margin-top': 20,
            'margin-right':10
        },
        className = 'six columns'
    
    ),
    html.Div(
        children = dcc.Dropdown(id = 'Materia', #options = group_dict,
                                                value = '1MV2',
                                                #searchable = False,
                                                clearable = False),
        style = {
            'margin':40,
            'width': 450,
            'margin-top':20,
            'margin-bottom':20,
            'margin-left':0
        },
        className = 'six columns'
    
    )
    ], className = 'row', style = {'width': 800, 'margin-left':'auto', 'margin-right':'auto'}),

    html.Table(id = 'second_table',style = {
                                            'textAlign': 'center',
                                            'margin':80,
                                            'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            'margin-bottom':40,
                                            'width':  250,
                                            'height':'auto'
                                           }
    ),
    
    html.H3(children = 'Organizar horario', style = style_subtitles),
    html.Div('', style = style_bar),
    html.Div(children = [
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
                'width': 200,
                'margin-bottom':10,
                'margin-top': 20,
                'margin-right':10
            },
            className = 'two columns'
        
        ),
        html.Div(
            children = dcc.Dropdown(id = 'Materia_y_grupo', #options = group_dict,
                                                    value = ['1MV2','0'],
                                                    #searchable = False,
                                                    multi=True,
                                                    clearable = True),
            style = {
                'margin':40,
                'width': 500,
                'margin-top':20,
                'margin-bottom':20,
                'margin-left':0,
            },
            className = 'two columns'
        
        )
    ], className = 'row', style = {'width': 800, 'margin-left':'auto', 'margin-right':'auto'}),

    html.Table(id = 'third_table',style = {
                                            'textAlign': 'center',
                                            'margin':80,
                                            'margin-top':10,
                                            'margin-left':'auto',
                                            'margin-right':'auto',
                                            'margin-bottom':40,
                                            'width':  250,
                                            'height':'auto'
                                           }
    ),

    html.Footer(children= [
                                         html.Div(children = ['Hecho por Julio César Hernández -  ',
                                                                html.A('GitHub',href = 'https://github.com/JoulesCH',target='_blank'),
                                                                ' - ',
                                                                html.A('LinkedIn',href = 'https://www.linkedin.com/in/julio-césar-hernández-b426a1161/',target='_blank') ,'.' 
                                                        ], 
                                                style = {
                                                    'textAlign': 'center',
                                                    'margin': 10,
                                                    'margin-left': 'auto',
                                                    'margin-right': 'auto'
                                                 }
                                         ),
                                         html.Div(children= ['Datos obtenidos de ', html.A('Mis Profesores',href = 'https://www.misprofesores.com/escuelas/ESFM-IPN_1691',target='_blank'),
                                                                                            ' y ', 
                                                                                            html.A('ESFM',href = 'https://www.esfm.ipn.mx/assets/files/esfm/docs/HORARIOS.pdf',target='_blank'),
                                                                                            '. '],
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
                                        #'border-top-style': 'double',
                                        #'border-top-color': '#1866B9',
                                        'margin-left': 'auto',
                                        'margin-right': 'auto',
                                        'margin-top': 15
                                        
                                }
                    )


   

],style={'margin-top':0}
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
    df2 = df[df['Programa'] == carrera]
    df3 = df2.reset_index()
    first = [{'label': '-','value':'all'}]
    for ind in range(df3.shape[0]):
        grupo = df3.loc[ind,'Grupo']
        materia = df3.loc[ind,'Unidad de aprendizaje']
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
        dataframe = dataframe.drop('Unnamed: 0',axis = 1).iloc[:,loc_list].rename(columns={'Semestre':'Sem','Calificacion':'Cal'})
        return [ html.Thead(
                    html.Tr([html.Th(col) for col in dataframe.columns])
                ),

                html.Tbody([html.Tr([
                        html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                    ]) for i in range(min(len(dataframe), max_rows))
                ], style = {'color':'#414242' , 'width': 200})

            ]

@app.callback(Output('second_table','children'),[Input('Materia','value'),Input('Carrera_2','value')])
def generate_2table(materia,carrera, dataframe = df, max_rows = 100):
    if materia:
        dataframe = dataframe[(dataframe['Programa']==carrera) & (dataframe['Unidad de aprendizaje']==materia)]

        dataframe = dataframe.drop('Unnamed: 0',axis = 1).iloc[:,loc_list].rename(columns={'Semestre':'Sem','Calificacion':'Cal'})
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
        dataframe = dataframe.drop('Unnamed: 0',axis = 1).iloc[:,loc_list].rename(columns={'Semestre':'Sem','Calificacion':'Cal'})
    except:
        dataframe = df[df['Unidad de aprendizaje'] == ''].drop('Unnamed: 0',axis = 1).iloc[:,loc_list].rename(columns={'Semestre':'Sem','Calificacion':'Cal'})
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
