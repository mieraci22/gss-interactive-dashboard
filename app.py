# Import libraries again for a self-contained script
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output


# --- 1. APP SETUP ---
app = dash.Dash(__name__)
server = app.server # This line is needed for services like PythonAnywhere
app.title = "GSS Interactive Dashboard"

# --- 2. LAYOUT DEFINITION ---
app.layout = html.Div([
    html.H1("GSS Interactive Dashboard", style={'textAlign': 'center', 'color': '#FFFFFF'}),
    html.P("An exploration of gender, work, and attitudes from the 2018 General Social Survey.", style={'textAlign': 'center', 'color': '#CCCCCC'}),
    html.Hr(),
    html.H3("Explore Attitudes by Topic and Demographic", style={'color': '#FFFFFF'}),
    html.P("Select a survey question and a demographic group to see how responses vary.", style={'color': '#CCCCCC'}),
    
    html.Div([
        # Dropdown for selecting the variable
        dcc.Dropdown(
            id='variable-dropdown',
            options=[
                {'label': 'Job Satisfaction', 'value': 'satjob'},
                {'label': 'Working Mother Relationship', 'value': 'relationship'},
                {'label': 'Male Breadwinner', 'value': 'male_breadwinner'},
                {'label': 'Men Suited for Politics', 'value': 'men_bettersuited'},
                {'label': 'Working Mother and Child Suffering', 'value': 'child_suffer'},
                {'label': 'Men Overworking', 'value': 'men_overwork'}
            ],
            value='satjob', # Default value
            style={'color': '#000000'}
        ),
        # Dropdown for selecting the grouping
        dcc.Dropdown(
            id='group-dropdown',
            options=[
                {'label': 'Sex', 'value': 'sex'},
                {'label': 'Region', 'value': 'region'},
                {'label': 'Education Level', 'value': 'education'}
            ],
            value='sex', # Default value
            style={'color': '#000000'}
        ),
    ], style={'width': '80%', 'margin': 'auto'}),

    # Graph that will be updated by the callback
    dcc.Graph(id='interactive-barplot')
])

# --- 3. CALLBACK DEFINITION ---
@app.callback(
    Output('interactive-barplot', 'figure'),
    [Input('variable-dropdown', 'value'),
     Input('group-dropdown', 'value')]
)
def update_graph(selected_variable, selected_group):
    # Use a copy of the gss_clean DataFrame to avoid modifying the original
    df_copy = gss_clean.copy()
    
    # Drop missing values for the selected columns to prevent errors
    df_copy.dropna(subset=[selected_variable, selected_group], inplace=True)
    
    # For 'education', group into bins to make the plot readable
    if selected_group == 'education':
        df_copy['education'] = pd.cut(df_copy['education'],
                                     bins=[0, 8, 12, 15, 21],
                                     labels=['< High School', 'High School', 'Some College', 'College Grad+'])
        df_copy.dropna(subset=['education'], inplace=True)

    # Create the figure with a title that updates based on user selection
    fig = px.bar(
        df_copy,
        x=selected_variable,
        color=selected_group,
        barmode='group',
        labels={
            selected_variable: selected_variable.replace('_', ' ').title(),
            'count': 'Number of Respondents',
            selected_group: selected_group.title()
        },
        title=f"Responses for '{selected_variable.replace('_', ' ').title()}' grouped by '{selected_group.title()}'"
    )
    fig.update_layout(transition_duration=500)
    return fig

# --- 5. RUN THE APP ---
if __name__ == '__main__':
    app.run(debug=True, port=8051)