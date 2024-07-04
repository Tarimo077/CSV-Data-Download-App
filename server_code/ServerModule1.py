import anvil.server
import os
import anvil.media
import pandas as pd
import anvil.server
import anvil.http

@anvil.server.callable
def req(m):
  headers = {
    "Content-Type": "application/json"
  }
  response = anvil.http.request(url=m, method='GET', username='admin', password='123Give!@#')
  return response

@anvil.server.callable
def get_Data(m):
  url = "https://appliapay.com/getMeasurementData"
  headers = {
    "Content-Type": "application/json"
  }
  response = anvil.http.request(url=url, data=m, method="GET", username='admin', password='123Give!@#')
  return response

@anvil.server.callable
def download_csv(arr):
  array = arr
  df = pd.DataFrame(array)
  df.to_csv('/tmp/output.csv', index=False)
  X_media = anvil.media.from_file('/tmp/output.csv', 'csv', 'consumption_data.csv')
  return X_media
