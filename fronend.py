from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        text_color_normal: 0.101960784, 0.396078431, 0.619607843, 1
        panel_color: "#5fa8d3"
        selected_color_background: "#f8f9fa"
        text_color_active: "#1a659e"

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
'''
        )
    
        



Test().run()



# class MD3Card(MDCard):
#     '''Implements a material design v3 card.'''
#     text = StringProperty()
#     icon = StringProperty()