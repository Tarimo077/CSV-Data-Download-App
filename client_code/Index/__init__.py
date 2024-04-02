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
    names = [item['name'] for item in rxt]
    self.drop_down_1.items = names
    self.button_1.visible = True
    self.button_1.enabled = True
    self.button_1.text = "Download " + self.drop_down_1.selected_value + " measurement"

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    da = {
      "q": self.drop_down_1.selected_value
    }
    dt = anvil.server.call('get_Data', da)
    rxt = dt.get_bytes().decode('utf-8')
    rxt = json.loads(rxt)
    csv  = anvil.server.call('download_csv', rxt)
    anvil.media.download(csv)

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_1.selected_value is None:
      self.button_1.visible = False
      self.button_1.enabled = False
    else:
      self.button_1.visible = True
      self.button_1.enabled = True
      self.button_1.text = "Download " + self.drop_down_1.selected_value + " measurement"
