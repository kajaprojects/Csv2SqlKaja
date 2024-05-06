import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class SensorData(db.Model):
    __tablename__ = 'sensorData'
    value_id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime(timezone=True))  
    value = db.Column(db.Float)


class SensorDataInt(db.Model):
    __tablename__ = 'sensorDataInt'
    value_id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime(timezone=True))  
    value = db.Column(db.Integer)


class Sensor(db.Model):
    __tablename__ = 'sensor'
    sensor_id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.Integer)
    type = db.Column(db.String(10))
    name = db.Column(db.String(100))

class TransportLondon(db.Model):
    __tablename__ = 'TransportLondon'
    value_id = db.Column(db.Integer, primary_key=True)
    _postman_id = db.Column(db.String(100))
    name = db.Column(db.String(100))
    schema = db.Column(db.String(100))
    _exporter_id = db.Column(db.Integer)
"""    
    item_name = db.Column(db.String(100))
    item_item_name = db.Column(db.String(100))
    item_item_event_listen = db.Column(db.String(100))
    item_item_event_script_type = db.Column(db.String(100))
    item_item_event_script_exec = db.Column(db.String(100))
    item_item_request_method = db.Column(db.String(100))
    item_item_request_header = db.Column(db.String(100))
    item_item_request_body_mode = db.Column(db.String(100))
    item_item_request_body_formdata = db.Column(db.String(100))
    item_item_request_url_raw = db.Column(db.String(100))
    item_item_request_url_protocol = db.Column(db.String(100))
    item_item_request_url_host = db.Column(db.String(100))
    item_item_request_url_path = db.Column(db.String(100))
    item_item_request_url_query_key = db.Column(db.String(100))
    item_item_request_url_query_value = db.Column(db.String(100))
    item_item_response = db.Column(db.String(100))
    item_item_request_description = db.Column(db.String(100))
    item_item_request_header_key = db.Column(db.String(100))
    item_item_request_header_value = db.Column(db.String(100))
"""
"""
CREATE TABLE IF NOT EXISTS "TransportLondon" (
    "info_postman_id" TEXT,
    "info_name" TEXT,
    "info_schema" TEXT,
    "info_exporter_id" INT,
    "item_name" TEXT,
    "item_item_name" TEXT,
    "item_item_event_listen" TEXT,
    "item_item_event_script_type" TEXT,
    "item_item_event_script_exec" TEXT,
    "item_item_request_method" TEXT,
    "item_item_request_header" TEXT,
    "item_item_request_body_mode" TEXT,
    "item_item_request_body_formdata" TEXT,
    "item_item_request_url_raw" TEXT,
    "item_item_request_url_protocol" TEXT,
    "item_item_request_url_host" TEXT,
    "item_item_request_url_path" TEXT,
    "item_item_request_url_query_key" TEXT,
    "item_item_request_url_query_value" TEXT,
    "item_item_response" TEXT,
    "item_item_request_description" TEXT,
    "item_item_request_header_key" TEXT,
    "item_item_request_header_value" TEXT
"""