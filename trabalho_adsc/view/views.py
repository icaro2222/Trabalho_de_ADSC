from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def index(request):
    # return render(request, 'indexTest.html')
    
    return TemplateView.as_view(template_name="index.html")


def dashboard(request):
    # return render(request, 'indexTest.html')

    menssagem = """OIIIIII"""


    figura = go.Figure()

    trace1 = go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0887, 0.544, 1.0865],
                    name = 'Windows 11',
                    marker = {'color': '#b6bccf'},
                    text=[0.0887, 0.544, 1.0865],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[0.0049433205036927864, 0.02915989958525339, 0.040226582751884815])
                    )
    trace2 = go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0661, 0.253, 2.1656],
                    name = 'Ubuntu 22',
                    marker = {'color': '#68adfc'},
                    text=[0.0661, 0.253, 2.1656],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[0.007738649910551172, 0.008672861580959234, 0.035113223583310406])
                    )

    data = [trace1, trace2]
    figura = go.Figure(data=data)


    figura.update_traces(
         marker_line_color='rgb(8,48,107)',
        marker_line_width=1.5, 
        opacity=1
        )

    figura.update_layout(
        title_text='Gráfico de Inserts no PostgresSQL',
        height=500,
        xaxis_title="Valor da Carga",
        yaxis_title="Tempo em milissegundos",
        legend_title="Legenda",
        uniformtext_minsize=8, 
        uniformtext_mode='hide',
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    grafico = figura.to_html()


    trace1 = go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.079, 0.0867, 0.1554],
                    name = 'Windows 11',
                    marker = {'color': '#b6bccf'},
                    text=[0.079, 0.0867, 0.1554],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[0.012114005120714243, 0.010749845096837558, 0.01669386205687868])
                    )
    trace2 = go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0584, 0.0702, 0.3249],
                    name = 'Ubuntu 22',
                    marker = {'color': '#68adfc'},
                    text= [0.0584, 0.0702, 0.3249],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[0.006074102929651422, 0.008089839158348239, 0.011725486016817912])
                    )
    data = [trace1, trace2]
    figura = go.Figure(data=data)


    figura.update_traces(
         marker_line_color='rgb(8,48,107)',
        marker_line_width=1.5, 
        opacity=1
        )

    figura.update_layout(
        title_text='Gráfico de Inserts no PostgresSQL',
        height=500,
        xaxis_title="Valor da Carga",
        yaxis_title="Tempo em milissegundos",
        legend_title="Legenda",
        uniformtext_minsize=8, 
        uniformtext_mode='hide',
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )


    grafico2 = figura.to_html()



    trace1 = go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.1127, 0.0963, 0.1087],
                    name = 'Windows 11',
                    marker = {'color': '#b6bccf'},
                    text= [0.1127, 0.0963, 0.1087],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[0.018269155692079184, 0.010746270871543439, 0.024702299199191965])
                    )
    trace2 = go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0692, 0.0764, 0.0933],
                    name = 'Ubuntu 22',
                    marker = {'color': '#68adfc'},
                    text= [0.0692, 0.0764, 0.0933],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[0.0033812130368940066, 0.006693909351044425, 0.003969181477559334])
                    )
    data = [trace1, trace2]
    figura = go.Figure(data=data)

    figura.update_traces(
         marker_line_color='rgb(8,48,107)',
        marker_line_width=1.5, 
        opacity=1
        )

    figura.update_layout(
        title_text='Gráfico de Select no PostgresSQL',
        height=500,
        xaxis_title="Valor da Carga",
        yaxis_title="Tempo em milissegundos",
        legend_title="Legenda",
        uniformtext_minsize=8, 
        uniformtext_mode='hide',
        font=dict(
            family="Arial",
            size=12,
            color="black"
        ) 
    )


    grafico3 = figura.to_html()



    trace1 = go.Bar(x = ['1000', '10000', '100000'], #parei a analise aqui
                    y = [0.0705, 0.0777, 0.092],
                    name = 'Windows 11',
                    marker = {'color': '#b6bccf'},
                    text= [0.0705, 0.0777, 0.092],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[0.008435972973663405, 0.00924758658063027, 0.013018885970755612])
                    )
    trace2 = go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0653, 0.0578, 0.1036],
                    name = 'Ubuntu 22',
                    marker = {'color': '#68adfc'},
                    text= [0.0653, 0.0578, 0.1036],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[0.0063996326130711855, 0.005206373939701219, 0.0072609998231393125])
                    )
    data = [trace1, trace2]
    figura = go.Figure(data=data)


    figura.update_traces(
         marker_line_color='rgb(8,48,107)',
        marker_line_width=1.5, 
        opacity=1
        )

    figura.update_layout(
        title_text='Gráfico de Delete no PostgresSQL',
        height=500,
        xaxis_title="Valor da Carga",
        yaxis_title="Tempo em milissegundos",
        legend_title="Legenda",
        uniformtext_minsize=8, 
        uniformtext_mode='hide',
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    grafico4 = figura.to_html()


    # Análise do Mysql



    trace1 = go.Bar(x = ['1000', '10000', '100000'], #parei a analise aqui
                    y = [24.9, 270.1, 1587.5],
                    name = 'Windows 11',
                    marker = {'color': '#b6bccf'},
                    text= [24.9, 270.1, 1587.5],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[4.764453210777755, 88.4641825655197, 50.73731730978261])
                    )
    trace2 = go.Bar(x = ['1000', '10000', '100000'],#Falta o do Ubuntu
                    y = [ 25, 207, 2092],
                    name = 'Ubuntu 22',
                    marker = {'color': '#68adfc'},
                    text= [ 25, 207, 2092],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[9, 99, 89])
                    )
    data = [trace1, trace2]
    figura = go.Figure(data=data)


    figura.update_traces(
         marker_line_color='rgb(8,48,107)',
        marker_line_width=1.5, 
        opacity=1
        )

    figura.update_layout(
        title_text='Gráfico de Inserts no PostgresSQL',
        height=500,
        xaxis_title="Valor da Carga",
        yaxis_title="Tempo em milissegundos",
        legend_title="Legenda",
        uniformtext_minsize=8, 
        uniformtext_mode='hide',
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    grafico5 = figura.to_html()

    trace1 = go.Bar(x = ['1000', '10000', '100000'],
                    y = [35.8, 259.4, 1570.3],
                    name = 'Windows 11',
                    marker = {'color': '#b6bccf'},
                    text= [35.8, 259.4, 1570.3],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[10.684427250009715, 90.97575997696596, 67.97163008151377])
                    )
    trace2 = go.Bar(x = ['1000', '10000', '100000'], #Falta o do Ubuntu
                    y = [ 35.8, 277, 2092],
                    name = 'Ubuntu 22',
                    marker = {'color': '#68adfc'},
                    text= [ 35.8, 277, 2092],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[9, 29, 89])
                    )
    data = [trace1, trace2]
    figura = go.Figure(data=data)


    figura.update_traces(
         marker_line_color='rgb(8,48,107)',
        marker_line_width=1.5, 
        opacity=1
        )

    figura.update_layout(
        title_text='Gráfico de Update no PostgresSQL',
        height=500,
        xaxis_title="Valor da Carga",
        yaxis_title="Tempo em milissegundos",
        legend_title="Legenda",
        uniformtext_minsize=8, 
        uniformtext_mode='hide',
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )


    grafico6 = figura.to_html()

    trace1 = go.Bar(x = ['1000', '10000', '100000'], #parei a analise aqui
                    y = [2705, 2277, 22],
                    name = 'Windows 11',
                    marker = {'color': '#68adfc'},
                    text=  [2705, 2277, 22],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[99, 2099, 889])
                    )
    trace2 = go.Bar(x = ['1000', '10000', '100000'],#Falta o do Ubuntu
                    y = [ 20705, 20777, 2092],
                    name = 'Ubuntu 22',
                    marker = {'color': '#b6bccf'},
                    text= [ 20705, 20777, 2092],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[99, 2099, 889])
                    )
    data = [trace1, trace2]
    figura = go.Figure(data=data)

    figura.update_traces(
         marker_line_color='rgb(8,48,107)',
        marker_line_width=1.5, 
        opacity=1
        )

    figura.update_layout(
        title_text='Gráfico de Select no PostgresSQL',
        height=500,
        xaxis_title="Valor da Carga",
        yaxis_title="Tempo em milissegundos",
        legend_title="Legenda",
        uniformtext_minsize=8, 
        uniformtext_mode='hide',
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )


    grafico7 = figura.to_html()

    trace1 = go.Bar(x = ['1000', '10000', '100000'],
                    y = [17.2, 137.5, 910.9],
                    name = 'Windows 11',
                    marker = {'color': '#68adfc'},
                    text= [17.2, 137.5, 910.9],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[2.8645519019344015, 44.984668768151586, 49.019165050341016])
                    )
    trace2 = go.Bar(x = ['1000', '10000', '100000'],#Falta o do Ubuntu
                    y = [ 25, 207, 1092],
                    name = 'Ubuntu 22',
                    marker = {'color': '#b6bccf'},
                    text= [ 25, 207, 1092],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[9, 29, 89])
                    )
    data = [trace1, trace2]
    figura = go.Figure(data=data)

    figura.update_traces(
         marker_line_color='rgb(8,48,107)',
        marker_line_width=1.5, 
        opacity=1
        )

    figura.update_layout(
        title_text='Gráficos Comparativo entre Windonws 11 e Ubuntu 22.',
        height=500,
        xaxis_title="Valor da Carga",
        yaxis_title="Tempo em milissegundos",
        legend_title="Legenda",
        uniformtext_minsize=8, 
        uniformtext_mode='hide',
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    grafico8 = figura.to_html()

    trace1 = go.Bar(x = ['1000', '10000', '100000'],
                    y = [17.2, 137.5, 910.9],
                    name = 'Windows 11',
                    marker = {'color': '#b6bccf'},
                    text= [17.2, 137.5, 910.9],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[2.8645519019344015, 44.984668768151586, 49.019165050341016])
                    )
    trace2 = go.Bar(x = ['1000', '10000', '100000'],#Falta o do Ubuntu
                    y = [ 25, 207, 1092],
                    name = 'Ubuntu 22',
                    marker = {'color': '#68adfc'},
                    text= [ 25, 207, 1092],
                    textposition='auto',
                    width=0.3,
                    error_y=dict(type='data', array=[9, 29, 89])
                    )
    data = [trace1, trace2]
    figura = go.Figure(data=data)

    figura = make_subplots(rows=2, cols=2 , 
                            subplot_titles = ("Gráfico de Insert", 
                            "Gráfico de Update",
                            "Gráfico de Select",
                            "Gráfico de Delete"
                            )
                        )

    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0887, 0.544, 1.0865],
                    name = 'Windows 11 VS Postgres',
                    marker = {'color': '#b6bccf'},
                    text=[0.0887, 0.544, 1.0865],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.0049433205036927864, 0.02915989958525339, 0.040226582751884815])),
                    row=1, col=1)
    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0661, 0.253, 2.1656],
                    name = 'Ubuntu 22 VS Postgres',
                    marker = {'color': '#68adfc'},
                    text=[0.0661, 0.253, 2.1656],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.007738649910551172, 0.008672861580959234, 0.035113223583310406])),
                    row=1, col=1)

    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [24.9, 270.1, 1587.5],
                    name = 'Windows 11 VS Mysql',
                    marker = {'color': '#f7ec6f'},
                    text=[0.0887, 0.544, 1.0865],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[4.764453210777755, 88.4641825655197, 50.73731730978261])),
                    row=1, col=1)
    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [ 25, 207, 2092],
                    name = 'Ubuntu 22 vs Mysql',
                    marker = {'color': '#e84925'},
                    text=[0.0661, 0.253, 2.1656],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[9, 99, 89])),
                    row=1, col=1)
                    

    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0887, 0.544, 1.0865],
                    name = 'Windows 11 VS Postgres',
                    marker = {'color': '#b6bccf'},
                    text=[0.0887, 0.544, 1.0865],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.0049433205036927864, 0.02915989958525339, 0.040226582751884815])),
                    row=1, col=2)
    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0661, 0.253, 2.1656],
                    name = 'Ubuntu 22 VS Postgres',
                    marker = {'color': '#68adfc'},
                    text=[0.0661, 0.253, 2.1656],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.007738649910551172, 0.008672861580959234, 0.035113223583310406])),
                    row=1, col=2)
    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0887, 0.544, 1.0865],
                    name = 'Windows 11 VS Mysql',
                    marker = {'color': '#f7ec6f'},
                    text=[0.0887, 0.544, 1.0865],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.0049433205036927864, 0.02915989958525339, 0.040226582751884815])),
                    row=1, col=2)
    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0661, 0.253, 2.1656],
                    name = 'Ubuntu 22 vs Mysql',
                    marker = {'color': '#e84925'},
                    text=[0.0661, 0.253, 2.1656],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.007738649910551172, 0.008672861580959234, 0.035113223583310406])),
                    row=1, col=2)
                    

    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0887, 0.544, 1.0865],
                    name = 'Windows 11 VS Postgres',
                    marker = {'color': '#b6bccf'},
                    text=[0.0887, 0.544, 1.0865],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.0049433205036927864, 0.02915989958525339, 0.040226582751884815])),
                    row=2, col=1)

    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0661, 0.253, 2.1656],
                    name = 'Ubuntu 22 VS Postgres',
                    marker = {'color': '#68adfc'},
                    text=[0.0661, 0.253, 2.1656],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.007738649910551172, 0.008672861580959234, 0.035113223583310406])),
                    row=2, col=1)
    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0887, 0.544, 1.0865],
                    name = 'Windows 11 VS Mysql',
                    marker = {'color': '#f7ec6f'},
                    text=[0.0887, 0.544, 1.0865],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.0049433205036927864, 0.02915989958525339, 0.040226582751884815])),
                    row=2, col=1)
    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0661, 0.253, 2.1656],
                    name = 'Ubuntu 22 vs Mysql',
                    marker = {'color': '#e84925'},
                    text=[0.0661, 0.253, 2.1656],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.007738649910551172, 0.008672861580959234, 0.035113223583310406])),
                    row=2, col=1)
                    

    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0887, 0.544, 1.0865],
                    name = 'Windows 11 VS Postgres',
                    marker = {'color': '#b6bccf'},
                    text=[0.0887, 0.544, 1.0865],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.0049433205036927864, 0.02915989958525339, 0.040226582751884815])),
                    row=2, col=2)
    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0661, 0.253, 2.1656],
                    name = 'Ubuntu 22 VS Postgres',
                    marker = {'color': '#68adfc'},
                    text=[0.0661, 0.253, 2.1656],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.007738649910551172, 0.008672861580959234, 0.035113223583310406])),
                    row=2, col=2)
    figura.append_trace(go.Bar(x = ['1000', '10000', '100000'],
                    y = [0.0887, 0.544, 1.0865],
                    name = 'Windows 11 VS Mysql',
                    marker = {'color': '#f7ec6f'},
                    text=[0.0887, 0.544, 1.0865],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.0049433205036927864, 0.02915989958525339, 0.040226582751884815])),
                    row=2, col=2)
    figura.add_bar(x = ['1000', '10000', '100000'],
                    y = [0.0661, 0.253, 2.1656], 
                    name = 'Ubuntu 22 vs Mysql',
                    marker = {'color': '#e84925'},
                    text=[0.0661, 0.253, 2.1656],
                    textposition='auto',
                    width=0.2,
                    error_y=dict(type='data', array=[0.007738649910551172, 0.008672861580959234, 0.035113223583310406]),
                    row=2, col=2)
                    

    figura.update_yaxes( 
        title_text = "Tempo em milissegundos", 
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    showline=True, linewidth=1, linecolor='black', row = 2, col = 2)
    figura.update_xaxes( 
        title_text = "Valor da Carga", 
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    showline=True, linewidth=1, linecolor='black', row = 2, col = 2)

    figura.update_yaxes( 
        title_text = "Tempo em milissegundos", 
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    showline=True, linewidth=1, linecolor='black', row = 2, col = 1)
    figura.update_xaxes( 
        title_text = "Valor da Carga", 
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    showline=True, linewidth=1, linecolor='black', row = 2, col = 1)

    figura.update_yaxes( 
        title_text = "Tempo em milissegundos", 
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    showline=True, linewidth=1, linecolor='black', row = 1, col = 2)
    figura.update_xaxes( 
        title_text = "Valor da Carga", 
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    showline=True, linewidth=1, linecolor='black', row = 1, col = 2)

    figura.update_yaxes( 
        title_text = "Tempo em milissegundos", 
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    showline=True, linewidth=1, linecolor='black', row = 1, col = 1)
    figura.update_xaxes( 
        title_text = "Valor da Carga", 
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    showline=True, linewidth=1, linecolor='black', row = 1, col = 1)


    figura.update_layout(
        title_text='Gráficos de comparação entre Windonws 11 e Ubuntu 22.',
        height=800,
        legend_title="Legenda",
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    grafico1 = figura.to_html()

    context = {
        'grafico1': grafico1,
        'grafico': grafico,
        'grafico2': grafico2,
        'grafico3': grafico3,
        'grafico4': grafico4,
        'grafico5': grafico5,
        'grafico6': grafico6,
        'grafico7': grafico7,
        'grafico8': grafico8,
        'menssagem': menssagem,
    }

    
    if request.method == 'GET':
        return render(request, 'dashboard.html', context=context)
    else:
        return render(request, 'dashboard.html', context=context)
    # return TemplateView.as_view(template_name="dashboard.html")
