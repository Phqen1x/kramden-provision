import gi
gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk
from utils import Utils

class KramdenNumber(Adw.Bin):
    def __init__(self):
        super().__init__()
        utils = Utils()
        self.set_margin_top(20)
        self.set_margin_bottom(20)
        self.set_margin_start(20)
        self.set_margin_end(20)
        self.title = "Identify"
        self.next = None
        self.skip = False

        #Create a Gtk.Entry
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Enter K-Number...")
        self.entry.connect("changed", self.on_entry_changed)
        self.entry.connect("activate", self.on_set_clicked)

        #Create a Set Button
        self.set_button = Gtk.Button.new_with_label("Set")
        self.set_button.set_sensitive(False)
        self.set_button.connect("clicked", self.on_set_clicked)

        self.set_button.add_css_class("button-green")

        hostname_label = Gtk.Label.new("K-Number: ")
        self.hostname = Gtk.Label.new(utils.get_hostname())
        knum_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        knum_box.append(hostname_label)
        knum_box.append(self.hostname)

        guide_text = Gtk.Label.new("Please enter K-Number")
        guide_text_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        guide_text_box.append(guide_text)

        #Add entry and button to a box
        entry_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        entry_box.append(self.entry)
        entry_box.append(self.set_button)

        #Add entry_box to the window
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.append(knum_box)
        vbox.append(guide_text_box)
        vbox.append(entry_box)

        alignment = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, hexpand=True)
        alignment.append(vbox)
        alignment.set_halign(Gtk.Align.CENTER)
        self.set_child(alignment)

    def on_entry_changed(self, widget):
        # Enable the button if the entry is not empty, else disable it
        if self.entry.get_text():
            self.set_button.set_sensitive(True)
        else:
            self.set_button.set_sensitive(False)

    def on_set_clicked(self, button):
        state = self.state.get_value()
        utils = Utils()
        entered_text = self.entry.get_text()
        if utils.set_hostname(entered_text):
            self.hostname.set_text(entered_text)
            if entered_text.lower().startswith("k"):
                state['KramdenNumber'] = True
                self.next()
                self.skip = True
            else:
                state['KramdenNumber'] = False
        print("knum:on_set_clicked " + str(self.state.get_value()))

    # on_shown is called when the page is shown in the stack
    def on_shown(self):
        utils = Utils()
        hostname = utils.get_hostname()
        state = self.state.get_value()
        if hostname.lower().startswith("k"):
            state['KramdenNumber'] = True
        else:
            state['KramdenNumber'] = False
        print("knum:on_shown " + str(self.state.get_value()))
