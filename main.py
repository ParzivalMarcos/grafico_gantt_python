import plotly.express as px
import plotly
import pandas as pd
import plotly.figure_factory as ff


def grafico_gantt():
    # -- Criando grafico de Gantt
    grafico = px.timeline(df,
                      x_start=data_inicio,
                      x_end=data_final,
                      y=tarefas,
                      color=perc_completado,
                      title='Grafico de Gantt com Python',
                      color_continuous_scale = px.colors.sequential.Magenta)

    # -- Ajustando Layout
    grafico.update_layout(
        title_font_size=40,
        font_size=18,
        title_font_family='Arial'
    )

    # -- Grafico Interativo
    # Renomeando colunas do Data Frame
    # df.rename(columns={
    #     "Tarefa": "Task",
    #     "Inicio": "Start",
    #     "Fim": "Finish"
    # }, inplace=True)
    #
    # grafico = ff.create_gantt(df)


    # Reordenando o gráfico
    grafico.update_yaxes(autorange='reversed')

    return grafico


def salvar_grafico_p_html(grafico):
    # -- Salvando Grafico e exportando para HTML
    plotly.offline.plot(grafico, filename='Grafico_Gantt.html')


if __name__ == '__main__':
    # -- Carregar DataFrame
    df = pd.read_excel('tarefas.xlsx', header=1)

    # -- Atribuindo os valores das colunas a variaveis
    tarefas = df['Tarefa']
    responsaveis = df['Responsável']
    data_inicio = df['Inicio']
    data_final = df['Fim']
    perc_completado = df['% Completado']

    gantt = grafico_gantt()
    salvar_grafico_p_html(grafico=gantt)


    # Referencias
    # https://pandas.pydata.org/pandas-docs/stable/
    # https://plotly.github.io/plotly.py-docs/generated/plotly.figure_factory.html
    # https://plotly.com/python/gantt/
    # https://plotly.com/python/builtin-colorscales/
