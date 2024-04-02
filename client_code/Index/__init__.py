from ._anvil_designer import IndexTemplate
from anvil import *
import anvil.server
import json
import anvil.media

class Index(IndexTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    u = "https://appliapay.com/getMeasurements"
    dt = anvil.server.call('req', u)
    rxt = dt.get_bytes().decode('utf-8')
    rxt = json.loads(rxt)
    print(rxt)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    #csv  = anvil.server.call('download_csv', rxt)
    #anvil.media.download(csv)
