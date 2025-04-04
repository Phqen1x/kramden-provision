import gi
gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk
from utils import Utils

class OSLoadComplete(Adw.Bin):
    def __init__(self):
        super().__init__()
        self.set_margin_top(20)
        self.set_margin_bottom(20)
        self.set_margin_start(20)
        self.set_margin_end(20)
        self.title = "OS Load Complete"
        self.skip = False
        
        # Create a list box to hold the rows
        list_box = Gtk.ListBox()
        list_box.set_selection_mode(Gtk.SelectionMode.NONE)

        # Create Adwaita rows
        self.title_row = Adw.ActionRow()
        self.title_row.set_title("<b>OS Load Complete</b>")
        
        self.complete_row = Adw.ActionRow()
        self.complete_row.set_title("")

        list_box.append(self.title_row)
        list_box.append(self.complete_row)

        self.set_child(list_box)

    def complete(self):
        print("OSLoadComplete: complete")
        utils = Utils()
        utils.complete_reset("osload")

    # on_shown is called when the page is shown in the stack
    def on_shown(self):
        print("OSLoadComplete: on_shown")
        state = self.state.get_value()
        if all(state.values()):
            print("OSLoadComplete: All passed")
            self.complete_row.set_title("OS Load Complete: <b>PASSED</b>!")
            self.complete_row.set_subtitle(str(state))
        else:
            print("OSLoadComplete: Failed")
            self.complete_row.set_title("OS Load Complete: <b>FAILED</b>!")
            self.complete_row.set_subtitle(str(state))
