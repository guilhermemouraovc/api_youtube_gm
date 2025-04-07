import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
###dashboard
df = pd.read_csv("dados_f1.csv")
df["Data"] = pd.to_datetime(df["Data"])


app = dash.Dash(__name__)
app.title = "F1 Highlights 2024"
app._favicon = "f1_icon.png"

fig_views = px.bar(
    df.sort_values("Visualizações", ascending=False),
    x="Título",
    y="Visualizações",
    title="Visualizações por Vídeo",
    labels={"Visualizações": "Visualizações"},
)
fig_views.update_layout(
    xaxis_tickangle=-45,
    plot_bgcolor="#0e0e0e",
    paper_bgcolor="#0e0e0e",
    font_color="white",
    title_font_color="#E10600"
)


app.layout = html.Div(
    style={"backgroundColor": "#0e0e0e", "color": "#ffffff", "padding": "20px"},
    children=[
        html.Div([
            html.Img(src="/assets/f1_icon.png", style={"height": "50px", "float": "left", "marginRight": "15px"}),
            html.H1("Dashboard - F1 Highlights 2024", style={"color": "#E10600", "textAlign": "left"})
        ], style={"display": "flex", "alignItems": "center"}),
        
        dcc.Graph(figure=fig_views),

        html.Div([
            html.H3("Outras Métricas por Vídeo", style={"color": "#E10600"}),
            dcc.Graph(
                figure=px.scatter(
                    df,
                    x="Curtidas",
                    y="Comentários",
                    size="Visualizações",
                    hover_name="Título",
                    title="Curtidas vs Comentários (tamanho = visualizações)",
                    template="plotly_dark",
                    color_discrete_sequence=["#E10600"]
                )
            )
        ]),
        html.Div([
            html.Hr(style={"borderColor": "#333"}),
            html.P("Projeto disponível no GitHub:",
                   style={"marginBottom": "5px", "marginTop": "20px"}),
            html.A("https://github.com/guilhermemouraovc/api_youtube_gm",
                   href="https://github.com/guilhermemouraovc/api_youtube_gm",
                   target="_blank",
                   style={"color": "#E10600", "textDecoration": "none"})
        ], style={"textAlign": "center", "marginTop": "30px"})
        
    ]
)


if __name__ == '__main__':
    app.run(debug=True)