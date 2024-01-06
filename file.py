from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatIconButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

    
class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name = 'main'
        box_layout = BoxLayout(
            orientation='horizontal',
            spacing='10dp',
            padding='10dp',
        )
        card1 = MDCard(
            orientation='vertical',
            size_hint=(None, None),
            size=("250dp", "150dp"),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            padding='10dp',
            spacing='10dp',
            md_bg_color= 'lightblue',
            # icon='bed'
        )
        card2 = MDCard(
            orientation='vertical',
            size_hint=(None, None),
            size=("250dp", "150dp"),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            padding='20dp',
            spacing='10dp',
            md_bg_color= 'lightblue'
            
        )
        card3 = MDCard(
            orientation='vertical',
            size_hint=(None, None),
            size=("250dp", "150dp"),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            padding='20dp',
            spacing='10dp',
            md_bg_color= 'lightblue'
        )
        card1.add_widget(MDLabel(text="In Patient"))
        card2.add_widget(MDLabel(text="Out Patient"))
        card3.add_widget(MDLabel(text="Employees"))
        box_layout.add_widget(card1)
        box_layout.add_widget(card2)
        box_layout.add_widget(card3)
        # box_layout.add_widget(button)
        self.add_widget(box_layout)

class Patient(MDScreen):
    def __init__(self, **kwargs):
        super(Patient, self).__init__(**kwargs)
        self.name = 'Patient'
        box_layout = BoxLayout(
            orientation='vertical',
            spacing='10dp',
            padding='10dp'
        )
        card = MDCard(
            orientation='vertical',
            size_hint=(None, None),
            size=("280dp", "180dp"),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            padding='10dp',
            spacing='10dp'
        )
        # card.add_widget(MDLabel(text="Card on Other Screen"))
        # box_layout.add_widget(card)
        # self.add_widget(box_layout)
        def build():
            # self.theme_cls.theme_style = "Dark"
            # self.theme_cls.primary_palette = "Orange"
            return MDAnchorLayout(
                MDDataTable(
                    size_hint=(1, 0.8),
                    anchor_x='center', 
                    anchor_y='center',
                    padding=(0, dp(10), 0, 0),
                    # use_pagination=True,
                    # check=True,
                    column_data=[
                        ("Nom", dp(30)),
                        ("Prenom", dp(30)),
                        ("Age", dp(30)),
                        ("Gender", dp(30)),
                        ("staying", dp(30)),
                    ],
                )
            )
        table = build()
        self.add_widget(table)

def test():
    return [
                (
                    "334545",
                    "idrissi",
                    "Ahlam",
                    "Femme",
                    "Docteur",
            
                ),
                (
                    "32325",
                    "idrissi",
                    "Fouad",
                    "homme",
                    "Securite",
                ),
                (
                    "545335",
                    "bakkali",
                    "halima",
                    "Femme de mennage",
                    "Docteur",
                ),
                (
                    "33345",
                    "omrani",
                    "haïtam",
                    "homme",
                    "Chef du service des urgences",
                ),
                (
                    "3232",
                    "idrissi",
                    "Ahlam",
                    "Femme",
                    "Docteur",
                ),
            ]
class Employee(MDScreen):
    def __init__(self, **kwargs):
        super(Employee, self).__init__(**kwargs)
        self.name = 'Employee'
        def build():
            return MDAnchorLayout(
                MDDataTable(
                    size_hint=(1, 0.9),
                    anchor_x='center', 
                    anchor_y='center',
                    padding=(0, dp(10), 0, 0),
                    # use_pagination=True,
                    # check=True,
                    column_data=[
                        ("Id", dp(35)),
                        ("Nom", dp(35)),
                        ("Prenom", dp(30)),
                        ("Gender", dp(30)),
                        ("Post", dp(30)),
                    ],
                    row_data=test(),
                )
            )
        table = build()
        self.add_widget(table)

class Rooms(MDScreen):
    def __init__(self, **kwargs):
        super(Rooms, self).__init__(**kwargs)
        self.name = 'Rooms'
        def build():
            return MDAnchorLayout(
                MDDataTable(
                    size_hint=(.8, 0.7),
                    anchor_x='center', 
                    anchor_y='center',
                    padding=(0, dp(10), 0, 0),
                    # use_pagination=True,
                    # check=True,
                    column_data=[
                        ("Nombre de la chambre", dp(40)),
                        ("Nombre de lits vides", dp(40)),
                        ("Nombre de lits utilises", dp(40)),
                    ],
                    row_data=test(),
                )
            )
        table = build()
        self.add_widget(table)

class Example(MDApp):
    def build(self):
        
        # Create the screen manager
        self.screen_manager = MDScreenManager()
        
        # Add screens to the screen manager
        main_screen = MainScreen()
        Patient_screen = Patient()
        Employee_screen = Employee()
        Rooms_screen = Rooms()

        self.screen_manager.add_widget(main_screen)
        self.screen_manager.add_widget(Patient_screen)
        self.screen_manager.add_widget(Employee_screen)
        self.screen_manager.add_widget(Rooms_screen)
        
        self.screen_manager.current = 'main'

        # Create bottom navigation bar
        buttom_nav = MDBottomNavigation()
            
        # bottom_nav = bar()
        tab1 = MDBottomNavigationItem(name='main', text='Home', icon='hospital-box-outline')
        tab2 = MDBottomNavigationItem(name='other1', text='Patient', icon='account-group')
        tab3 = MDBottomNavigationItem(name='other2', text='Employee', icon='doctor')
        tab4 = MDBottomNavigationItem(name='other3', text='Rooms', icon='bed')
        
        tab1.text_color_normal = "#023e8a" 
        tab2.text_color_normal = "#023e8a"
        tab3.text_color_normal = "#023e8a"

        # Add screens to the tabs
        tab1.on_tab_press = lambda *args: self.switch_to_screen('main')
        tab2.on_tab_press = lambda *args: self.switch_to_screen('Patient')
        tab3.on_tab_press = lambda *args: self.switch_to_screen('Employee')
        tab4.on_tab_press = lambda *args: self.switch_to_screen('Rooms')
        
        # Add tabs to bottom navigation bar
        buttom_nav.add_widget(tab1)
        buttom_nav.add_widget(tab2)
        buttom_nav.add_widget(tab3)
        buttom_nav.add_widget(tab4)

        # Add screen manager and bottom navigation bar to the app layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.screen_manager)
        layout.add_widget(buttom_nav)

        return layout
    
    def switch_to_screen(self, screen_name):
        self.screen_manager.current = screen_name


Example().run()
