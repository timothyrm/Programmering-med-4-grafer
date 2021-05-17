from numpy.lib.shape_base import _dstack_dispatcher
import plotly.express as px
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib as plt
#import dash
#import dash_html_components as html
#import dash_table



# HÄR LÄSER JAG IN ALLA FILER SÅ ATT JAG SEDAN KAN ANVÄNDA DOM I GRAFERNA
National_Daily_deaths = pd.read_csv('National_Daily_Deaths.csv')
cases_gender = pd.read_csv('Gender_Data.csv')
Regional_Totals = pd.read_csv('Regional_Totals_Data.csv')
Age = pd.read_csv('National_Total_Deaths_by_Age_Group.csv')

# HÄR SKAPAR JAG SUBPLOT FÖR ATT KUNNA GÖRA FLERA OLIKA GRAFER. SÅ ATT DOM KAN VARA BREVID VARANDRA PÅ ETT SNYGGT SÄTT.
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Antalet Döda", "Antalet Smittade per region", "Antalet Smittade per kön", "Antalet smittade per ålder")) #HÄR GÖR JAG TITLARNA OVANFÖR SUBPLOTSEN


# HÄR GÖR JAG EN BAR GRAF, VÄLDIGT SIMPEL OCH DEN FILTERERAR SÅ ATT Y OCH X ÄR FÖR DATUM OCH ANTALET DÖDA, SEDAN HAR JAG DEN PÅ ROW 1 OCH COL 1, SÅ ATT DEN HAMNAR LÄNGST UPP TILL VÄNSTER
fig.add_trace(go.Bar(
    x= National_Daily_deaths["Date"], y=National_Daily_deaths["National_Daily_Deaths"]), row=1, col=1)

# HAR GJORT SAMMA PÅ ALLA NEDAN
fig.add_trace(go.Bar(
    x=cases_gender['Gender'], y=cases_gender['Total_Cases']), row=2, col=1)

fig.add_trace(go.Bar(
    x=Regional_Totals["Region"], y=Regional_Totals["Total_Cases"]), row=1, col=2)

fig.add_trace(go.Bar(
    x=Age["Age_Group"], y=Age["Total_Cases"]), row=2, col=2)

#HÄR NEDAN HAR JAG GJORT X OCH Y TITLAR, LIKT XLABEL OCH YLABEL.
fig.update_xaxes(title_text="Datum", row=1, col=1)
fig.update_xaxes(title_text="Regioner", row=1, col=2)
fig.update_xaxes(title_text="Kön", row=2, col=1)
fig.update_xaxes(title_text="Ålder", row=2, col=2)

# Update yaxis properties
fig.update_yaxes(title_text="Antalet döda", row=1, col=1)
fig.update_yaxes(title_text="Antalet smittade", row=1, col=2)
fig.update_yaxes(title_text="Antalet smittade", row=2, col=1)
fig.update_yaxes(title_text="Antalet smittade", row=2, col=2)


#app = dash.Dash(DropdownMenu)


fig.update_layout(height=700, title_text="Olika grafer över antalet döda och smittade av COVID19",showlegend=False) #HÄR HAR JAG GJORT EN UPDATE LAYOUT VILKETLÅTER MIG UPPDATERA LAYOUTEN SÅ JAG KAN VÄLJA STORLEK OCH TITEL LÄNGST UPP
fig.write_html('first_figure.html', auto_open=True) #DENNA PRINTAR UT HEMSIDAN SOM DÅ HETER "first_figure.html"
