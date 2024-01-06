from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

KV = '''

<MD3Card>:
    padding: 4
    size_hint: None, None
    size: "200dp", "100dp"

    MDRelativeLayout:

        MDIconButton:
            icon: root.icon
            pos_hint: {"top": 1, "right": 1}

        MDLabel:
            id: label
            text: root.text
            adaptive_size: True
            color: "white"
            pos: "22dp", "12dp"
            bold: True

MDScreen:

    MDBottomNavigation:
        text_color_normal: 0.101960784, 0.396078431, 0.619607843, 1
        panel_color: "#5fa8d3"
        selected_color_background: "#f8f9fa"
        text_color_active: "#1a659e"
        on_switch: app.on_switch(*args)

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
            icon: 'hospital-box-outline'
            

            MDLabel:
                text: 'Dashboard'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Patient'
            icon: 'account-group'

            MDLabel:
                text: 'Patient s page'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Employee'
            icon: 'doctor'

            MDLabel:
                text: 'Employee s page'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Rooms'
            icon: 'bed'

            MDLabel:
                text: 'Rooms s page'
                halign: 'center'

        MDBoxLayout:
            id: box
            adaptive_size: True
            spacing: "56dp"
            pos_hint: {"center_x": .5, "center_y": .5}
<MD3Card>
    padding: 4
    size_hint: None, None
    size: "200dp", "100dp"

    MDRelativeLayout:


        MDLabel:
            id: label
            text: root.text
            adaptive_size: True
            color: "white"
            pos: "12dp", "12dp"
            bold: True


'''

class MD3Card(MDCard):
    '''Implements a material design v3 card.'''
    text = StringProperty()
    icon = StringProperty()

class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def on_start(self):
        custom_names = [
            {"name": "In Patient", "icon": "account-arrow-left-outline"},
            {"name": "Out Patient", "icon": "bed-empty"},
            {"name": "Employees", "icon": "doctor"},
        ]
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tabs_label, tab_text):
        if tab_text == "Home":
            self.root.ids.box.clear_widgets()
            custom_names = [
            {"name": "In Patient", "icon": "account-arrow-left-outline"},
            {"name": "Out Patient", "icon": "bed-empty"},
            {"name": "Employees", "icon": "doctor"},
        ]
        for custom_name in custom_names:
            card = MD3Card(
                line_color='#FFFFFF',
                style="elevated",
                text=custom_name["name"],
                md_bg_color='#5fa8d3',
                icon=custom_name["icon"],
                shadow_offset=(0, -3),
            )
            self.root.ids.box.add_widget(card)


Example().run()
