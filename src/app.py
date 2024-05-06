from distutils.log import debug
from fileinput import filename
import pandas as pd
import os
from werkzeug.utils import secure_filename

import json

from flask import request, render_template, redirect, url_for, flash, session
from werkzeug.exceptions import abort

from . import create_app, database
from .models import SensorData, TransportLondon, Sensor, SensorDataInt

UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}

app = create_app()

# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'This is your secret key to utilize session in Flask'


@app.route('/',  methods=['GET'])
def index():
    sensors = database.get_all(SensorData)
    return render_template('index.html', sensors=sensors)

@app.route('/readDB', methods=['GET'])
def readDB():
    sensorData = database.get_all(SensorData)
    all_sensorData = []
    for sensor in sensorData:
        new_sensor = {
            "value_id": sensor.value_id,
            "sensor_id": sensor.sensor_id,
            "timestamp": sensor.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "value": sensor.value
        }

        all_sensorData.append(new_sensor)
    return json.dumps(all_sensorData), 200

@app.route('/readCSV', methods=['GET', 'POST'])
def readCSV():
    if request.method == 'POST':

        print(UPLOAD_FOLDER)
      # upload file flask
        f = request.files.get('file')
 
        # Extracting uploaded file name
        data_filename = secure_filename(f.filename) #poiscem in izberem datoteko CSV
 
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
 
        session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
 
        return render_template('readCSV2.html')
    return render_template("readCSV.html")
 
@app.route('/show_data')
def showData():
    # Uploaded File Path
    data_file_path = session.get('uploaded_data_file_path', None)
    # read csv
    #pd.options.display.max_rows = 99
    uploaded_df = pd.read_csv(data_file_path, encoding='unicode_escape', nrows=10) # preberem datoteko CSV in dam v Panadas
    # Converting to html Table
    uploaded_df_html = uploaded_df.to_html()
    return render_template('show_csv_data.html',
                           data_var=uploaded_df_html)
  
@app.route('/write_data')
def writeData():
    # Uploaded File Path
    data_file_path = session.get('uploaded_data_file_path', None)
    # read csv
    #pd.options.display.max_rows = 99
    uploaded_df = pd.read_csv(data_file_path, encoding='unicode_escape', nrows=10)
    #uploaded_df.reset_index(drop = True, inplace = True)
    uploaded_df = uploaded_df.convert_dtypes()
    num_of_rows = len(uploaded_df)
    
    for i in range(num_of_rows):
        #print(uploaded_df.iloc[i])
        value_id = int(uploaded_df.iloc[i]['value_id'])
        sensor_id = int(uploaded_df.iloc[i]['sensor_id'])
        timestamp = uploaded_df.iloc[i]['timestamp']
        value = uploaded_df.iloc[i]['value']
        #print(value_id, sensor_id, value)
        database.add_instance(SensorData, value_id=value_id, sensor_id=sensor_id, timestamp=timestamp, value=value)

    # Converting to html Table
    uploaded_df_html = uploaded_df.to_html()
    return render_template('write_csv_data.html', data_var=uploaded_df_html)

@app.route('/write_SensorDataInt')
def write_SensorDataInt():
    # Uploaded File Path
    data_file_path = session.get('uploaded_data_file_path', None)
    # read csv
    #pd.options.display.max_rows = 99
    uploaded_df = pd.read_csv(data_file_path, encoding='unicode_escape', nrows=10)
    #uploaded_df.reset_index(drop = True, inplace = True)
    uploaded_df = uploaded_df.convert_dtypes()
    num_of_rows = len(uploaded_df)
    
    for i in range(num_of_rows):
        #print(uploaded_df.iloc[i])
        value_id = int(uploaded_df.iloc[i]['value_id'])
        sensor_id = int(uploaded_df.iloc[i]['sensor_id'])
        timestamp = uploaded_df.iloc[i]['timestamp']
        value = int(uploaded_df.iloc[i]['value'])
        #print(value_id, sensor_id, value)
        database.add_instance(SensorDataInt, value_id=value_id, sensor_id=sensor_id, timestamp=timestamp, value=value)

    # Converting to html Table
    uploaded_df_html = uploaded_df.to_html()
    return render_template('write_SensorDataInt.html', data_var=uploaded_df_html)

@app.route('/write_sensor_data')
def writeSensorData():
    # Uploaded File Path
    data_file_path = session.get('uploaded_data_file_path', None)
    # read csv
    #pd.options.display.max_rows = 99
    uploaded_df = pd.read_csv(data_file_path, encoding='unicode_escape', nrows=10)
    #uploaded_df.reset_index(drop = True, inplace = True)
    uploaded_df = uploaded_df.convert_dtypes()
    num_of_rows = len(uploaded_df)
    
    for i in range(num_of_rows):
        #print(uploaded_df.iloc[i])
        node_id = int(uploaded_df.iloc[i]['node_id'])
        sensor_id = int(uploaded_df.iloc[i]['sensor_id'])
        type= uploaded_df.iloc[i]['type']
        name = uploaded_df.iloc[i]['name']
        #print(value_id, sensor_id, value)
        database.add_instance(Sensor, node_id=node_id, sensor_id=sensor_id, type=type, name=name)

    # Converting to html Table
    uploaded_df_html = uploaded_df.to_html()
    return render_template('write_sensor_data.html', data_var=uploaded_df_html)

@app.route('/readDBSensor', methods=['GET'])
def readDBSensor():
    sensors = database.get_all(Sensor)
    all_sensor = []
    for sensor in sensors:
        new_sensor = {
            "node_id": sensor.node_id,
            "sensor_id": sensor.sensor_id,
            "type": sensor.type,
            "name": sensor.name
        }

        all_sensor.append(new_sensor)
    return json.dumps(all_sensor), 200

@app.route('/readDBSensorDataInt', methods=['GET'])
def readDBSensorDataInt():
    sensorDataInt = database.get_all(SensorDataInt)
    all_sensorDataInt = []
    for sensor in sensorDataInt:
        new_sensor = {
            "value_id": sensor.value_id,
            "sensor_id": sensor.sensor_id,
            "timestamp": sensor.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "value": sensor.value
        }

        all_sensorDataInt.append(new_sensor)
    return json.dumps(all_sensorDataInt), 200

@app.route('/remove/<value_id>', methods=['DELETE'])
def remove(value_id):
    database.delete_instance(SensorData, id=value_id)
    return json.dumps("Deleted"), 200

@app.route('/readJSON', methods=['GET', 'POST'])
def readJSON():
    if request.method == 'POST':

        print(UPLOAD_FOLDER)
      # upload file flask
        f = request.files.get('file')
 
        # Extracting uploaded file name
        data_filename = secure_filename(f.filename)
 
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
 
        session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
 
        return render_template('readJSON2.html')
    return render_template("readJSON.html")

@app.route('/show_json_data')
def showDataJSON():
    # Uploaded File Path
    data_file_path = session.get('uploaded_data_file_path', None)
    # read csv
    uploaded_df = pd.read_json(data_file_path, encoding='utf-8-sig', typ="series")
    # Converting to html Table
    uploaded_df = pd.DataFrame(uploaded_df)
    uploaded_df_html = uploaded_df.to_html()
    return render_template('show_json_data.html', data_var=uploaded_df_html)

@app.route('/write_json_data')
def writeDataJSON():
    # Uploaded File Path
    data_file_path = session.get('uploaded_data_file_path', None)
    # read csv
    #pd.options.display.max_rows = 99
    uploaded_df = pd.read_json(data_file_path, encoding='utf-8-sig', typ="series")
    num_of_rows = len(uploaded_df)

    #for i in range(num_of_rows):
    #    print(uploaded_df.iloc[i])
    
    for i in range(num_of_rows):
        print('JSON ', uploaded_df.iloc[i])
        value_id = i + 1

        _postman_id = uploaded_df.iloc[i]['_postman_id']
        name = uploaded_df.iloc[i]['name']
        schema = uploaded_df.iloc[i]['schema']
        _exporter_id = int(uploaded_df.iloc[i]['_exporter_id'])
        """
        item_name = uploaded_df.iloc[i]['item_name']
        item_item_name = uploaded_df.iloc[i]['item_item_name']
        item_item_event_listen = uploaded_df.iloc[i]['item_item_event_listen']
        item_item_event_script_type = uploaded_df.iloc[i]['item_item_event_script_type']
        item_item_event_script_exec = uploaded_df.iloc[i]['item_item_event_script_exec']
        item_item_request_method = uploaded_df.iloc[i]['item_item_request_method']
        item_item_request_header = uploaded_df.iloc[i]['item_item_request_header']
        item_item_request_body_mode = uploaded_df.iloc[i]['item_item_request_body_mode']
        item_item_request_body_formdata = uploaded_df.iloc[i]['item_item_request_body_formdata']
        item_item_request_url_raw = uploaded_df.iloc[i]['item_item_request_url_raw']
        item_item_request_url_protocol = uploaded_df.iloc[i]['item_item_request_url_protocol']
        item_item_request_url_host = uploaded_df.iloc[i]['item_item_request_url_host']
        item_item_request_url_path = uploaded_df.iloc[i]['item_item_request_url_path']
        item_item_request_url_query_key = uploaded_df.iloc[i]['item_item_request_url_query_key']
        item_item_request_url_query_value = uploaded_df.iloc[i]['item_item_request_url_query_value']
        item_item_response = uploaded_df.iloc[i]['item_item_response']
        item_item_request_description = uploaded_df.iloc[i]['item_item_request_description']
        item_item_request_header_key = uploaded_df.iloc[i]['item_item_request_header_key']
        item_item_request_header_value = uploaded_df.iloc[i]['item_item_request_header_value']
        """
        #print(value_id, info_name, info_schema)
        database.add_instance(TransportLondon, value_id=value_id, 
                                               _postman_id=_postman_id, 
                                               name=name,
                                               schema=schema,
                                               _exporter_id=_exporter_id)
        """
                                               item_name=item_name,
                                               item_item_name=item_item_name,
                                               item_item_event_listen=item_item_event_listen)
        """
    # Converting to html Table
    uploaded_df = pd.DataFrame(uploaded_df)
    uploaded_df_html = uploaded_df.to_html()
    return render_template('write_json_data.html', data_var=uploaded_df_html)

@app.route('/readDBTransportLondon', methods=['GET'])
def readDBTransportLondon():
    transportLondon = database.get_all(TransportLondon)
    all_TransportLondon = []
    for transport in transportLondon:
        new_transport = {
            "value_id": transport.value_id,
            "_postman_id": transport._postman_id,
            "name": transport.name,
            "schema": transport.schema,
            "_exporter_id": transport._exporter_id
        }

        all_TransportLondon.append(new_transport)
    return json.dumps(all_TransportLondon), 200
