# from plotly.offline import plot
# import plotly.graph_objs as go 

# fig = go.Figure(
#     data=go.Scattergeo(
#         lat=[55,32],
#         lon=[-19,34],
#         mode = 'lines',
#         marker_symbol = 'star',
#         line = dict(width = 2, color = 'blue'),
#         ))

# fig.update_layout(
#     title_text = 'Sword of St. Michael',
#     showlegend = False,
#     geo = dict(
#         resolution = 50,
#         showland = True,
#         showlakes = True,
#         landcolor = 'rgb(84, 61, 50)',
#         countrycolor = 'rgb(154, 135, 173)',
#         lakecolor = 'rgb(108, 227, 235)',
#         projection_type = 'requirerectngular',
#         coastlinewidth = 2,
#     )
# )

# plot(fig)

import json 
import requests
import pandas as pd

api_response = requests.get('https://aeropi.flightaware.come/aeroapi/flights/search?query=-latlong+%2244.953469+-11.045360+40.962321-104.046577%22', 
                            headers={'x-apikey':
                                'IhrFC6GxpoStaKG6A5qy6FVE0C5hOIhA'})
response_json =json.loads(api_response.content.decode())
flights = response_json.get('flights')
df = pd.DataFrame(flights)

print(response_json)
print(df)
