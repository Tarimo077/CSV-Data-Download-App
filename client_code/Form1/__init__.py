from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.media
import json

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    u = "https://appliapay.com/tefalAIData"
    dt = anvil.server.call('req', u)
    rxt = dt.get_bytes().decode('utf-8')
    rxt = json.loads(rxt)
    csv  = anvil.server.call('download_csv', rxt)
    anvil.media.download(csv)

  def sayonnabtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    u = "https://appliapay.com/sayonnaAIData"
    dt = anvil.server.call('req', u)
    rxt = dt.get_bytes().decode('utf-8')
    rxt = json.loads(rxt)
    csv  = anvil.server.call('download_csv', rxt)
    anvil.media.download(csv)

  def powerpotbtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    u = "https://appliapay.com/powerpotAIData"
    dt = anvil.server.call('req', u)
    rxt = dt.get_bytes().decode('utf-8')
    rxt = json.loads(rxt)
    csv  = anvil.server.call('download_csv', rxt)
    anvil.media.download(csv)
