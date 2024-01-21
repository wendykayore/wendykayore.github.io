import pandas as pd
import plotly.express as px

data_paths = {
    "SurfTemp": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.AIRS3STM_006_SurfSkinTemp_A.20020901-20231130.180W_90S_180E_90N.csv",
    "SurfAirTemp": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.AIRX3STM_006_SurfAirTemp_A.20020901-20161031.74W_33S_34W_6N.csv",
    "RelHum": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.AIRS3STM_006_RelHum_A_H2OPrsLvls_A.1000hPa.20020901-20231130.74W_33S_34W_6N.csv",
}

y_names = {
    "SurfTemp": "Surface Temperature (C)",
    "SurfAirTemp": "Air Temperature (C)",
    "RelHum": "Relative Humidity (percentual)"
}

def create_chart(path, y_name, html_file, chart_title):
    data = pd.read_csv(path, skiprows=9,  usecols=[0,1], names=['Time',f'{y_name}'])

    # Read the times as dates and the methane concentrations as numeric values
    data['Time'] = pd.to_datetime(data['Time'])
    data[f'{y_name}'] = pd.to_numeric(data[f'{y_name}'])

    fig = px.line(data, x="Time", y=f'{y_name}', title=f'{chart_title}')
    fig.update_layout(title_x=0.5)
    fig.write_html(f"C:/pale-blue-dot-challenge/src/figures/{html_file}.html")

create_chart(data_paths["SurfTemp"], y_names["SurfTemp"], "SurfTemp", "Surface Temperature")
create_chart(data_paths["SurfAirTemp"], y_names["SurfAirTemp"], "SurfAirTemp", "Air Temperature at Surface")
create_chart(data_paths["RelHum"], y_names["RelHum"], "RelHum", "Relative Humidity")