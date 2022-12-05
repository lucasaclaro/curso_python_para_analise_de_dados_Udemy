import pandas as pd
import plotly.express as px


city = ['Santo André', 'São Bernando do Campo', 'Diadema', 'São Caetano do Sul', 'Mauá', 'Ribeirão Pires', 'Rio Grande da Serra', 'São Paulo']
state = ['São Paulo', 'São Paulo', 'São Paulo', 'São Paulo', 'São Paulo', 'São Paulo', 'São Paulo', 'São Paulo']
lat = [-23.6666, -23.6944, -23.6865, -23.6226, -23.6687, -23.7141, -23.7452, -23.5489]
lon = [-46.5322, -46.5654, -46.6234, -46.5489, -46.4614, -46.4137, -46.4022, -46.6388]
sales = [100, 120, 90, 50, 70, 90, 250, 400]
dict_sales = {'City' : city, 'State' : state, 'Lat': lat, 'Lon': lon, 'Sales': sales}
data_base = pd.DataFrame(dict_sales)
#print(data_base)

fig = px.density_mapbox(data_base, lat='Lat', lon='Lon', z='Sales', radius=30, center=dict(lat=-23.700, lon=-46.5555), zoom=7, mapbox_style='stamen-terrain')
fig.show()