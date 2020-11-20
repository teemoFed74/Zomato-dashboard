#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:12:05 2020

@author: abdulkader
"""

from maindash import app,df

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px

avg_cost = df.avg_cost_per_country()
sum_rating = df.count_rating_text_rest()
dff = df.dataframe

def tab2_content():
    fig1 = px.pie(df.count_rest_per_country(),values='Count',names='Country', title ='Restaurants Distribution by Country' )
    
    fig2 = px.bar(avg_cost, x='Country', y='Average Cost for two in dollars',
             labels={'Country':'Average cost for two in dollars'}, height=400)
    
    fig3 = px.bar(sum_rating, x='Percentage', y='Rating',
             labels={'Percentage' : 'Rating Percentage'}, height=400)
    return html.Div([
            dbc.Card(
                dbc.CardBody(
                    [
                        dcc.Graph(id='pie-chart-country-dist',figure=fig1)
                        ]
                    ),
                className="mt-3",
                ),
            dbc.Card(
                dbc.CardBody(
                    [
                        dcc.Graph(id='bar-graph-cost-average',figure=fig2)
                        ]
                    ),
                className="mt-3",
                ),
            dbc.Card(
                dbc.CardBody(
                    [
                        dcc.Graph(id='bar-graph-rating-percentage',figure=fig3)
                        ]
                    ),
                className="mt-3",
                )
            
            ])