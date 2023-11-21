from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.media

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    file_path = self.file_loader_1.file
    retan = anvil.server.call('pdf_gen', file_path)
    anvil.media.download(retan)
