from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from sqlalchemy import create_engine, Column, Integer, String, Date, Enum, text, select
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.anchorlayout import AnchorLayout
from sqlalchemy import Column, Integer, Date, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
from kivy.uix.image import Image
from kivy.core.window import Window
from sqlalchemy import create_engine, Column, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout

#______________________________________________________CONNECTION WITH DATABASE______________________________________________________________________________

Base = declarative_base()
engine = create_engine('mysql://root:root@localhost/clinic', echo=True)
Session = sessionmaker(bind=engine)




#______________________________________________________FETCH DATA FROM PHPMYADMIN______________________________________________________________________________


def fetch_patients_from_db():
    session = Session()
    try:
        result = session.query(Patient_database).all()

        data_list = []
        for row in result:
            data_list.append((row.patient_id, row.first_name, row.last_name, row.gender))
        return data_list
    except Exception as e:
        print(f"Error patient: {e}")
        return None
    finally:
        session.close()

def fetch_appointments_from_db():
    session = Session()
    try:
        result = session.query(Appointment_database).all()

        data_list = []
        for row in result:
            employee_name = f"{row.employee.first_name} {row.employee.last_name}"
            employee_post = f"{row.employee.position}"
            patient_name = f"{row.patient.first_name} {row.patient.last_name}"
            data_list.append((row.appointment_id, employee_name,employee_post, patient_name, row.appointment_date))

        return data_list
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error fetching appointments from the database: {e}")
        return None
    finally:
        session.close()

def fetch_appointments_line(appointment_id):
    session = Session()
    try:
        appointment = session.query(Appointment_database).filter_by(appointment_id=appointment_id).first()
        if appointment:
            employee_name = appointment.employee.last_name if appointment.employee else ''
            patient_name = appointment.patient.last_name if appointment.patient else ''

            data_list = [
                (appointment.appointment_id, employee_name, patient_name, appointment.appointment_date, appointment.room)
            ]
            return data_list
        else:
            print(f"No appointment found with ID: {appointment_id}")
            return None
    except Exception as e:
        print(f"Error fetching appointment details: {e}")
        return None
    finally:
        session.close()

def fetch_patient_line(patient_id):

    session = Session()
    try:
        print("Fetching data for patient:", patient_id)
        result = session.query(Patient_database).filter_by(patient_id=patient_id).first()
        if result:
            data_list = [(result.patient_id, result.first_name, result.last_name,result.date_of_birth, result.gender, result.contact_number, result.email, result.address, result.blood_type)]
            return data_list
        else:
            print(f"No patient found with ID: {patient_id}")
            return None
    except Exception as e:
        print(f"Error fetching patient details: {e}")
        return None
    finally:
        session.close()

def fetch_employee_line(employee_id):
    session = Session()
    try:
        print("Fetching data for patient:", employee_id)
        result = session.query(Employee_database).filter_by(employee_id=employee_id).first()
        if result:
            data_list = [(result.employee_id, result.first_name, result.last_name,result.date_of_birth, result.gender, result.contact_number, result.email, result.address, result.position, result.department)]
            return data_list
        else:
            print(f"No employee found with ID: {employee_id}")
            return None
    except Exception as e:
        print(f"Error fetching employee details: {e}")
        return None
    finally:
        session.close()

def fetch_employees_from_db():
    session = Session()
    try:
        result = session.query(Employee_database).all()
        data_list = []
        for row in result:
            data_list.append((row.employee_id, row.first_name, row.last_name, row.gender, row.position))
        return data_list
    except Exception as e:
        print(f"Error employee: {e}")
        return None
    finally:
        session.close()

def fetch_room_states():
    session = Session()
    rooms = session.query(Room).all()
    session.close()
    room_states = {room.room_number: room.is_empty for room in rooms}

    return room_states




#______________________________________________________DELETE DATA IN PHPMYADMIN______________________________________________________________________________


def delete_patient_by_id_from_db(patient_id):
    session = Session()
    try:
        patient = session.query(Patient_database).filter_by(patient_id=patient_id).first()
        if patient:
            session.delete(patient)
            session.commit()
            print(f"Patient with ID {patient_id} deleted successfully.")
        else:
            print("Patient not found.")
    except Exception as e:
        print("\n")
        session.rollback()
        print(f"Error deleting patient: {e}")
    finally:
        session.close()

def delete_employee_by_id_from_db(employee_id):
    session = Session()
    try:
        employee = session.query(Employee_database).filter_by(employee_id=employee_id).first()
        if employee:
            session.delete(employee)
            session.commit()
            print(f"Patient with ID {employee_id} deleted successfully.")
        else:
            print("employee not found.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting employee: {e}")
    finally:
        session.close()

def delete_appointment_by_id_from_db(appointment_id):   
    session = Session()
    try:
        appointment = session.query(Appointment_database).filter_by(appointment_id=appointment_id).first()
        if appointment:
            session.delete(appointment)
            session.commit()
            print(f"appointment with ID {appointment_id} deleted successfully.")
        else:
            print("appointment not found.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting appointment: {e}")
    finally:
        session.close()




#______________________________________________________ADD DATA IN PHPMYADMIN______________________________________________________________________________

def add_patient(patient):
    session = Session()
    session.add(patient)
    session.commit()
    session.close()

def add_employee(employee):
    session = Session()
    session.add(employee)
    session.commit()
    session.close()

def add_appointment_2(appointment):
    session = Session()
    session.add(appointment)
    session.commit()
    session.close()




#______________________________________________________TABLEAU DES DONNEES______________________________________________________________________________

class Patient_database(Base):
    __tablename__ = 'patients'
    patient_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(Enum('Male', 'Female', 'Other'), nullable=False)
    contact_number = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    blood_type = Column(String(1), nullable=False)

    appointments = relationship('Appointment_database', back_populates='patient')

class Employee_database(Base):
    __tablename__ = 'Employees'
    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(Enum('Male', 'Female', 'Other'), nullable=False)
    contact_number = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    position = Column(String(1), nullable=False)
    department = Column(String(1), nullable=False)

    appointments = relationship('Appointment_database', back_populates='employee')

class Appointment_database(Base):
    __tablename__ = 'appointments'

    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('Employees.employee_id'), nullable=False)
    appointment_date = Column(Date, nullable=False)
    notes = Column(Text)
    room = Column(String(10))

    employee = relationship('Employee_database', back_populates='appointments')
    patient = relationship('Patient_database', back_populates='appointments')

class Room(Base):
    __tablename__ = 'rooms'
    room_number = Column(Integer, primary_key=True)
    is_empty = Column(Boolean, default=True)




#______________________________________________________PATIENTS PART______________________________________________________________________________

class PatientScreen(MDScreen, BoxLayout):
    def __init__(self, **kwargs):
        super(PatientScreen, self).__init__(**kwargs)
        self.name = 'PatientScreen'
        self.table = MDDataTable(
                    pos_hint={"center_y": 0.6, "center_x": 0.5},
                    size_hint=(0.9, 0.7),
                    use_pagination=True,
                    check=True,
                    column_data=[
                        ("ID", dp(35)),
                        ("Nom", dp(35)),
                        ("Prenom", dp(30)),
                        ("Gender", dp(30)),
                    ],
                )
        layout = MDFloatLayout() 
        layout.md_bg_color = "#AFC8CB"
        top_left_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=dp(85))


        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(dp(260), dp(0)), spacing=dp(10))


        buttons_layout.add_widget(
            MDRaisedButton(
                text="add patient",md_bg_color="#354f52", on_release=lambda x: self.switch_to_screen('add_page_patient')
            )
        )
        buttons_layout.add_widget(
            MDRaisedButton(
                text="delete patient",md_bg_color="#354f52", on_release=lambda x: self.delete_checked_rows()
            )
        )
        buttons_layout.add_widget(
            MDRaisedButton(
                text="show patient",md_bg_color="#354f52", on_press=lambda x:  self.show_dialog()
            )
        )

        top_left_layout.add_widget(buttons_layout)
        layout.add_widget(top_left_layout)
        layout.add_widget(self.table)
        self.add_widget(layout)
        self.refresh_from_db()
        self.selected_patient_id = None 
        self.table.bind(on_row_press=self.on_row_press)


    def on_enter(self, *args):
        self.refresh_from_db()


    def refresh_from_db(self):
        patient_data = fetch_patients_from_db()
        if patient_data is not None:
            self.table.update_row_data(instance_data_table=self.table, data=patient_data)


    def switch_to_screen(self, screen_name):
        self.manager.current = screen_name


    def delete_checked_rows(self):
        for data in self.table.get_row_checks():
            patient_id = data[0]
            delete_patient_by_id_from_db(patient_id)

        self.refresh_from_db()


    def on_row_press(self, instance_table, instance_row):
        self.selected_patient_id = instance_row.text
        self.refresh_from_db()


    def show_dialog(self, *args):

        if not self.selected_patient_id:
            return

        patient_data = fetch_patient_line(self.selected_patient_id)

        if patient_data:
            dialog = MDDialog(
                title="Informations du patient : ",
                text=f"Patient ID: {self.selected_patient_id}\n"
                f"First Name: {patient_data[0][1]}\n"
                f"Last Name: {patient_data[0][2]}\n"
                f"Date of birth: {patient_data[0][3]}\n"
                f"Gender: {patient_data[0][4]}\n"
                f"Contact number: {patient_data[0][5]}\n"
                f"Email: {patient_data[0][6]}\n"
                f"Address: {patient_data[0][7]}\n"
                f"Blood type: {patient_data[0][8]}\n",
                buttons=[
                    MDFlatButton(
                        text="Close",
                        on_release=lambda *args: dialog.dismiss()
                    ),
                ],
            )


            dialog.open()

class AddPatientScreen(MDScreen):
    def __init__(self, **kwargs):
        super(AddPatientScreen, self).__init__(**kwargs)
        self.name = 'add_page_patient'
        layout = GridLayout(cols=2, spacing=100, padding= 200)
        with self.canvas.before:
            window_width, window_height = Window.size
            self.background_image = Image(source='img/flou4.png', allow_stretch=True, size=(window_width, window_height))


        first_name = BoxLayout(orientation='vertical', spacing=5)
        first_name_label = Label(text="First Name :", color="black", size_hint=(None, None), size=(170, 30), font_size=30)
        self.first_name_input = TextInput(size_hint=(None, None), size=(470, 60))
        first_name.add_widget(first_name_label)
        first_name.add_widget(self.first_name_input)


        last_name = BoxLayout(orientation='vertical', spacing=5)
        last_name_label = Label(text="Last Name:", color="black", size_hint=(None, None), size=(160, 30), font_size=30)
        self.last_name_input = TextInput(size_hint=(None, None), size=(470, 60))
        last_name.add_widget(last_name_label)
        last_name.add_widget(self.last_name_input)


        dob = BoxLayout(orientation='vertical', spacing=5)
        dob_label = Label(text="Date of birth:", color="black", size_hint=(None, None), size=(180, 30), font_size=30)
        self.dob_input = TextInput(size_hint=(None, None), size=(470, 60))
        dob.add_widget(dob_label)
        dob.add_widget(self.dob_input)


        number = BoxLayout(orientation='vertical', spacing=5)
        number_label = Label(text="Contact Number :", color="black", size_hint=(None, None), size=(230, 30), font_size=30)
        self.number_input = TextInput(size_hint=(None, None), size=(470, 60))
        number.add_widget(number_label)
        number.add_widget(self.number_input)


        email = BoxLayout(orientation='vertical', spacing=5)
        email_label = Label(text="Email :", color="black", size_hint=(None, None), size=(100, 30), font_size=30)
        self.email_input = TextInput(size_hint=(None, None), size=(470, 60))
        email.add_widget(email_label)
        email.add_widget(self.email_input)


        adress = BoxLayout(orientation='vertical', spacing=5)
        adress_label = Label(text="Address :", color="black", size_hint=(None, None), size=(130, 30), font_size=30)
        self.adress_input = TextInput(size_hint=(None, None), size=(470, 60))
        adress.add_widget(adress_label)
        adress.add_widget(self.adress_input)


        blood = BoxLayout(orientation='vertical', spacing=5)
        blood_label = Label(text="Blood Type :", color="black", size_hint=(None, None), size=(180, 30), font_size=30)
        self.blood_input = TextInput(size_hint=(None, None), size=(470, 60))
        blood.add_widget(blood_label)
        blood.add_widget(self.blood_input)


        gender = BoxLayout(orientation='vertical', spacing=5)
        self.gender_button = MDFlatButton(
            text='Select Gender',
            pos_hint={'center_x': 0.25},
            on_release=self.show_gender_dropdown,
            theme_text_color="Custom",  # Required for the custom border color
            text_color=(0, 0, 0, 1),  # Text color
            line_color=(0, 0, 0, 1),
            md_bg_color="lightgrey"
        )
        self.gender_menu = MDDropdownMenu(
            caller=self.gender_button,
            items=[
                {"text": f"{gender}", "viewclass": "OneLineListItem","on_release": lambda x=f"{gender}": self.set_gender(x)}
                for gender in ["Male", "Female"]
            ],
            width_mult=4
        )
        gender.add_widget(self.gender_button)


        add_button = Button(text='Save', size_hint=(None, None), size=(200, 80), pos_hint={'center_x': 0.5}, background_color="#AFC8CB")
        add_button.on_press = lambda *args: self.add_patient()


        layout.add_widget(first_name)
        layout.add_widget(last_name)
        layout.add_widget(dob)
        layout.add_widget(number)
        layout.add_widget(email)
        layout.add_widget(adress)
        layout.add_widget(blood)
        layout.add_widget(gender)
        layout.add_widget(add_button)
        self.add_widget(layout)


    def show_gender_dropdown(self, button):
        # Open the gender dropdown menu
        self.gender_menu.open()


    def set_gender(self, item):
        # Set gender button text to the selected gender
        self.gender_button.text = item
        self.gender_menu.dismiss()


    def add_patient(self, *args):
        # Create a new patient instance
        first_name = self.first_name_input.text.strip()
        last_name = self.last_name_input.text.strip()
        date_of_birth = self.dob_input.text.strip()
        gender = self.gender_button.text.strip().capitalize()
        contact_number = self.number_input.text.strip()
        email = self.email_input.text.strip()
        address = self.adress_input.text.strip()
        blood_type = self.blood_input.text.strip()


        new_patient = Patient_database(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=datetime.strptime(date_of_birth, '%Y-%m-%d').date(),
            gender=gender,
            contact_number=contact_number,
            email=email,
            address=address,
            blood_type=blood_type
        )
        add_patient(new_patient)
        self.manager.current = "PatientScreen"




#______________________________________________________EMPLOYEES PART______________________________________________________________________________

class EmployeeScreen(MDScreen, BoxLayout):
    def __init__(self, **kwargs):
        super(EmployeeScreen, self).__init__(**kwargs)
        self.name = 'EmployeeScreen'
        self.build()


    def build(self):
        self.table =MDDataTable(
                pos_hint={"center_y": 0.6, "center_x": 0.5},
                size_hint=(0.9, 0.7),
                use_pagination=True,
                check=True,
                column_data=[
                    ("ID", dp(30)),
                    ("Nom", dp(30)),
                    ("Prenom", dp(30)),
                    ("Sexe", dp(30)),
                    ("Poste", dp(30)),
                ],
            )
        layout = MDFloatLayout() 
        layout.md_bg_color = "#AFC8CB"
        top_left_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=dp(85))

        # Horizontal BoxLayout for the buttons
        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(dp(260), dp(0)), spacing=dp(10))

        buttons_layout.add_widget(
            MDRaisedButton(
                text="add employee",md_bg_color="#354f52", on_release=lambda x: self.switch_to_screen('add_page_Employee')
            )
        )
        buttons_layout.add_widget(
            MDRaisedButton(
                text="delete employee",md_bg_color="#354f52", on_release=lambda x: self.delete_checked_rows()
            )
        )
        buttons_layout.add_widget(
            MDRaisedButton(
                text="show employee",md_bg_color="#354f52", on_press=lambda x:  self.show_dialog()
            )
        )

        top_left_layout.add_widget(buttons_layout)
        layout.add_widget(top_left_layout)
        layout.add_widget(self.table)
        self.add_widget(layout)
        self.refresh_from_db()
        self.selected_patient_id = None 
        self.table.bind(on_row_press=self.on_row_press)
    
    def on_enter(self, *args):
        self.refresh_from_db()

    def refresh_from_db(self):
        employee_data = fetch_employees_from_db()
        if employee_data is not None:
            self.table.update_row_data(instance_data_table=self.table, data=employee_data)

    def switch_to_screen(self, screen_name):
        self.manager.current = screen_name

    def delete_checked_rows(self):
        for data in self.table.get_row_checks():
            employee_id = data[0]
            delete_employee_by_id_from_db(employee_id)
        self.refresh_from_db()
        
    def on_row_press(self, instance_table, instance_row):
        self.selected_employee_id = instance_row.text
        self.refresh_from_db()

    def show_dialog(self, *args):
        if not self.selected_employee_id:
            return

        employee_data = fetch_employee_line(self.selected_employee_id)
        if employee_data:
            dialog = MDDialog(
                title="Informations du employee : ",
                text=f"Employee ID: {self.selected_employee_id}\n"
                    f"First Name: {employee_data[0][1]}\n"
                    f"Last Name: {employee_data[0][2]}\n"
                    f"Date of birth: {employee_data[0][3]}\n"
                    f"Gender: {employee_data[0][4]}\n"
                    f"Contact number: {employee_data[0][5]}\n"
                    f"Email: {employee_data[0][6]}\n"
                    f"Adress: {employee_data[0][7]}\n"
                    f"Position: {employee_data[0][8]}\n"
                    f"Department: {employee_data[0][9]}\n",
                buttons=[
                    MDFlatButton(
                        text="Close",
                        on_release=lambda *args: dialog.dismiss()
                    ),
                ],
            )
            dialog.open()

class AddEmployeeScreen(MDScreen):
    def __init__(self, **kwargs):
        super(AddEmployeeScreen, self).__init__(**kwargs)
        self.name = 'add_page_Employee'
        layout = GridLayout(cols=2, spacing=100, padding= 200)
        
        with self.canvas.before:
            window_width, window_height = Window.size
            self.background_image = Image(source='img/flou4.png', allow_stretch=True, size=(window_width, window_height))


        first_name = BoxLayout(orientation='vertical', spacing=5)
        first_name_label = Label(text="First Name :", color="black", size_hint=(None, None), size=(170, 30), font_size=30)
        self.first_name_input = TextInput(size_hint=(None, None), size=(470, 60))
        first_name.add_widget(first_name_label)
        first_name.add_widget(self.first_name_input)


        last_name = BoxLayout(orientation='vertical', spacing=5)
        last_name_label = Label(text="Last Name:", color="black", size_hint=(None, None), size=(160, 30), font_size=30)
        self.last_name_input = TextInput(size_hint=(None, None), size=(470, 60))
        last_name.add_widget(last_name_label)
        last_name.add_widget(self.last_name_input)


        dob = BoxLayout(orientation='vertical', spacing=5)
        dob_label = Label(text="Date of birth:", color="black", size_hint=(None, None), size=(180, 30), font_size=30)
        self.dob_input = TextInput(size_hint=(None, None), size=(470, 60))
        dob.add_widget(dob_label)
        dob.add_widget(self.dob_input)


        gender = BoxLayout(orientation='vertical', spacing=5)
        self.gender_button = MDFlatButton(
            text='Select Gender',
            pos_hint={'center_x': 0.25},
            on_release=self.show_gender_dropdown,
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1), 
            line_color=(0, 0, 0, 1),
            md_bg_color="lightgrey"
        )
        self.gender_menu = MDDropdownMenu(
            caller=self.gender_button,
            items=[
                {"text": f"{gender}", "viewclass": "OneLineListItem","on_release": lambda x=f"{gender}": self.set_gender(x)}
                for gender in ["Male", "Female"]
            ],
            width_mult=4
        )
        gender.add_widget(self.gender_button)


        number = BoxLayout(orientation='vertical', spacing=5)
        number_label = Label(text="Contact Number :", color="black", size_hint=(None, None), size=(230, 30), font_size=30)
        self.number_input = TextInput(size_hint=(None, None), size=(470, 60))
        number.add_widget(number_label)
        number.add_widget(self.number_input)


        email = BoxLayout(orientation='vertical', spacing=5)
        email_label = Label(text="Email :", color="black", size_hint=(None, None), size=(100, 30), font_size=30)
        self.email_input = TextInput(size_hint=(None, None), size=(470, 60))
        email.add_widget(email_label)
        email.add_widget(self.email_input)


        adress = BoxLayout(orientation='vertical', spacing=5)
        adress_label = Label(text="Address :", color="black", size_hint=(None, None), size=(130, 30), font_size=30)
        self.adress_input = TextInput(size_hint=(None, None), size=(470, 60))
        adress.add_widget(adress_label)
        adress.add_widget(self.adress_input)


        post = BoxLayout(orientation='vertical', spacing=5)
        post_label = Label(text="Position :", color="black", size_hint=(None, None), size=(120, 50), font_size=30)
        self.post_input = TextInput(size_hint=(None, None), size=(470, 60))
        post.add_widget(post_label)
        post.add_widget(self.post_input)


        department = BoxLayout(orientation='vertical', spacing=5)
        department_label = Label(text="Department :", color="black", size_hint=(None, None), size=(170, 30), font_size=30)
        self.department_input = TextInput(size_hint=(None, None), size=(470, 60))
        department.add_widget(department_label)
        department.add_widget(self.department_input)
        
        add_button = Button(text='Save', size_hint=(None, None), size=(200, 80), pos_hint={'center_x': 0.5},  background_color="#AFC8CB")
        add_button.on_press = lambda *args: self.add_employee()


        layout.add_widget(first_name)
        layout.add_widget(last_name)
        layout.add_widget(dob)
        layout.add_widget(number)
        layout.add_widget(email)
        layout.add_widget(adress)
        layout.add_widget(post)
        layout.add_widget(department)
        layout.add_widget(gender)
        layout.add_widget(add_button)
        self.add_widget(layout)


    def show_gender_dropdown(self, button):
        self.gender_menu.open()


    def set_gender(self, item):
        self.gender_button.text = item
        self.gender_menu.dismiss()


    def add_employee(self, *args):
        first_name = self.first_name_input.text.strip()
        last_name = self.last_name_input.text.strip()
        date_of_birth = self.dob_input.text.strip()
        gender = self.gender_button.text.strip().capitalize()
        contact_number = self.number_input.text.strip()
        email = self.email_input.text.strip()
        address = self.adress_input.text.strip()
        position = self.post_input.text
        department = self.department_input.text

        new_employee = Employee_database(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=datetime.strptime(date_of_birth, '%Y-%m-%d').date(),
            gender=gender,
            contact_number=contact_number,
            email=email,
            address=address,
            position=position,
            department= department,
        )
        add_employee(new_employee)
        
        self.manager.current = "EmployeeScreen"




#______________________________________________________APPOINTMENT SCREEN ______________________________________________________________________________

class Appointment(MDScreen, BoxLayout):
    def __init__(self, **kwargs):
        super(Appointment, self).__init__(**kwargs)
        self.name = 'Appointment'
        self.build()


    def build(self):
        self.table =MDDataTable(
                pos_hint={"center_y": 0.6, "center_x": 0.5},
                size_hint=(0.9, 0.7),
                use_pagination=True,
                check=True,
                column_data=[
                    ("ID", dp(30)),
                    ("employe", dp(30)),
                    ("poste", dp(24)),
                    ("patient", dp(30)),
                    ("date", dp(30)),
                ],
            )
        layout = MDFloatLayout() 
        layout.md_bg_color = "#AFC8CB"
        top_left_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=dp(85))
        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(dp(260), dp(0)), spacing=dp(10))


        buttons_layout.add_widget(
            MDRaisedButton(
                text="add appointment",md_bg_color="#354f52", on_release=lambda x: self.switch_to_screen('add_page_appointment')
            )
        )
        buttons_layout.add_widget(
            MDRaisedButton(
                text="delete appointment",md_bg_color="#354f52", on_release=lambda x: self.delete_checked_rows()
            )
        )
        buttons_layout.add_widget(
            MDRaisedButton(
                text="show appointment",md_bg_color="#354f52", on_press=lambda x:  self.show_dialog()
            )
        )


        top_left_layout.add_widget(buttons_layout)
        layout.add_widget(top_left_layout)
        layout.add_widget(self.table)
        self.add_widget(layout)
        self.refresh_from_db()
        self.selected_appointment_id = None 
        self.table.bind(on_row_press=self.on_row_press)


    def on_enter(self, *args):
        self.refresh_from_db()


    def refresh_from_db(self):
        appointment_data = fetch_appointments_from_db()
        if appointment_data is not None:
            self.table.update_row_data(instance_data_table=self.table, data=appointment_data)


    def switch_to_screen(self, screen_name):
        self.manager.current = screen_name


    def delete_checked_rows(self):
        for data in self.table.get_row_checks():
            appointment_id = data[0]
            delete_appointment_by_id_from_db(appointment_id)
        self.refresh_from_db()


    def on_row_press(self, instance_table, instance_row):
        self.selected_appointment_id = instance_row.text
        self.refresh_from_db()

    def show_dialog(self, *args):
        if not self.selected_appointment_id:
            return
        print("\n\n")
        print(self.selected_appointment_id)
        print("\n\n")
        appointment_data = fetch_appointments_line(self.selected_appointment_id)
        print("\n\n")
        print("Appointment data:", appointment_data)
        print("Length of appointment_data:", len(appointment_data))

        if appointment_data: 
            appointment_details = appointment_data[0]
            dialog = MDDialog(
                title="Informations sur le rendez-vous : ",
                text=f"Appointment: {appointment_details[0]}\n"
                    f"employee: {appointment_details[1]}\n" 
                    f"patient: {appointment_details[2]}\n"
                    f"Date: {appointment_details[3]}\n"
                    f"room: {appointment_details[4]}\n", 
                buttons=[
                    MDFlatButton(
                        text="Close",
                        on_release=lambda *args: dialog.dismiss()
                    ),
                ],
            )
            dialog.open()
        else:
            print("Invalid appointment data or data structure.")

class AddAppointmentScreen(MDScreen):
    def __init__(self, **kwargs):
        super(AddAppointmentScreen, self).__init__(**kwargs)
        self.name = 'add_page_appointment'
        layout = GridLayout(cols=2, spacing=0, padding=(50, 50, 180, 235)) 


        with self.canvas.before:
            window_width, window_height = Window.size
            self.background_image = Image(source='img/flou4.png', allow_stretch=True, size=(window_width, window_height))


        select_buttons_column = BoxLayout(orientation='vertical', spacing=50)


        employee_label = Label(color="black", size_hint=(None, None), size=(180, 30), font_size=30)
        self.employee_button = MDFlatButton(
            text='Select employee',
            pos_hint={'center_x': 0.5},
            on_release=self.show_employee_dropdown,
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            line_color=(0, 0, 0, 1),
            md_bg_color="lightgrey",
            size_hint=(None, None),
            size=(200, 40)
        )
        employee_data = fetch_employees_from_db()
        self.employee_menu = MDDropdownMenu(
            caller=self.employee_button,
            items=[
                {"text": f"{employee[1]} {employee[2]}", "viewclass": "OneLineListItem",
                "on_release": lambda x=employee: self.set_employee(x)}
                for employee in employee_data
            ],
            width_mult=4
        )
        select_buttons_column.add_widget(employee_label)
        select_buttons_column.add_widget(self.employee_button)


        patient_label = Label(color="black", size_hint=(None, None), size=(80, 30), font_size=30)
        self.patient_button = MDFlatButton(
            text='Select Patient',
            pos_hint={'center_x': 0.5},
            on_release=self.show_patient_dropdown,
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            line_color=(0, 0, 0, 1),
            md_bg_color="lightgrey",
            size_hint=(None, None),
            size=(200, 40)
        )
        patients_data = fetch_patients_from_db()
        self.patient_menu = MDDropdownMenu(
            caller=self.patient_button,
            items=[
                {"text": f"{patient[1]} {patient[2]}", "viewclass": "OneLineListItem",
                "on_release": lambda x=patient: self.set_patient(x)}
                for patient in patients_data
            ],
            width_mult=4
        )
        select_buttons_column.add_widget(patient_label)
        select_buttons_column.add_widget(self.patient_button)


        room_label = Label(color="black", size_hint=(None, None), size=(80, 30), font_size=30)
        self.room_button = MDFlatButton(
            text='Select Room',
            pos_hint={'center_x': 0.5},
            on_release=self.show_room_dropdown,
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            line_color=(0, 0, 0, 1),
            md_bg_color="lightgrey",
            size_hint=(None, None),
            size=(200, 40)
        )
        self.room_menu = MDDropdownMenu(
            caller=self.room_button,
            items=[
                {"text": f"{room}", "viewclass": "OneLineListItem","on_release": lambda x=f"{room}": self.set_room(x)}
                for room in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            ],
            width_mult=4
        )
        select_buttons_column.add_widget(room_label)
        select_buttons_column.add_widget(self.room_button)


        text_inputs_column = BoxLayout(orientation='vertical', spacing=50)
        doa_label = Label(text="date :", color="black", size_hint=(None, None), size=(80, 30), font_size=30)
        self.doa_input = TextInput(size_hint=(None, None), size=(470, 60))
        text_inputs_column.add_widget(doa_label)
        text_inputs_column.add_widget(self.doa_input)


        notes_label = Label(text="notes :", color="black", size_hint=(None, None), size=(80, 30), font_size=30)
        self.notes_input = TextInput(size_hint=(None, None), size=(470, 60), multiline=True, input_type='text')
        text_inputs_column.add_widget(notes_label)
        text_inputs_column.add_widget(self.notes_input)


        add_button = Button(text='Save', size_hint=(None, None), size=(200, 80), pos_hint={'center_x': 0.5}, background_color="#AFC8CB")
        add_button.on_press = lambda *args: self.add_appointment()


        layout.add_widget(select_buttons_column)
        layout.add_widget(text_inputs_column)
        layout.add_widget(add_button)
        self.add_widget(layout)

    def set_patient(self, patient_data):
        selected_patient = f"{patient_data[1]} {patient_data[2]}"
        print(f"Selected Employee: {selected_patient}")
        if isinstance(selected_patient, str):
            self.patient_button.text = selected_patient
            self.selected_patient = patient_data[0]
        else:
            print("Error: Patient data is not a valid string.")
            self.selected_employee = None

        self.patient_menu.dismiss()
    
    def set_employee(self, employee_data):

        selected_employee = f"{employee_data[1]} {employee_data[2]}"
        print(f"Selected Employee: {selected_employee}")
        if isinstance(selected_employee, str):
            self.employee_button.text = selected_employee
            self.selected_employee = employee_data[0]
        else:
            print("Error: Employee data is not a valid string.")
            self.selected_employee = None
        self.employee_menu.dismiss()

    def show_room_dropdown(self, button):
        self.room_menu.open()


    def show_patient_dropdown(self, *args):
        self.patient_menu.open()


    def show_employee_dropdown(self, *args):
        self.employee_menu.open()


    def set_room(self, item):
        self.room_button.text = item
        self.room_menu.dismiss()


    def add_appointment(self, *args):
        appointment_date = self.doa_input.text.strip()
        notes = self.notes_input.text.strip()
        room = self.room_button.text.strip().capitalize()


        if self.selected_employee is not None and self.selected_patient is not None:
            # Both employee and patient IDs are valid, proceed with creating the appointment
            new_appointment = Appointment_database(
                employee_id=self.selected_employee,
                patient_id=self.selected_patient,
                appointment_date=datetime.strptime(appointment_date, '%Y-%m-%d').date(),
                notes=notes,
                room=room
            )

            # Call your function to add the appointment to the database
            add_appointment_2(new_appointment)
            self.manager.current = "Appointment"
        else:
            print("Error: Invalid employee or patient selected.")


#______________________________________________________ROOMS PART ______________________________________________________________________________

class RoomScreen(Screen):
    def __init__(self, **kwargs):
        super(RoomScreen, self).__init__(**kwargs)
        self.rooms = fetch_room_states()
        self.name = 'RoomScreen'
        self.build()


    def build(self):
        scroll_view = ScrollView()
        table_layout = MDGridLayout(cols=3, spacing=dp(10), size_hint=(1, 1), pos_hint={'center_x': 1, 'center_y': 1})
        table_layout.md_bg_color = "#AFC8CB"
        with self.canvas.before:
            window_width, window_height = Window.size
            self.background_image = Image(source='img/flou4.png', allow_stretch=True, size=(window_width, window_height))

        table_layout.add_widget(MDLabel(text="Room ID", size_hint_x=1, width=dp(100), font_style="H6"))
        table_layout.add_widget(MDLabel(text="State", size_hint_x=1, width=dp(100), font_style="H6"))
        table_layout.add_widget(MDLabel(text="Button", size_hint_x=1, width=dp(100), font_style="H6"))

        for room_number, state in self.rooms.items():
            table_layout.add_widget(MDLabel(text=str(room_number), size_hint_x=None, width=dp(100), font_style="H6"))
            table_layout.add_widget(MDLabel(text="Empty" if state else "Occupied", size_hint_x=None, width=dp(100)))
            button = MDFillRoundFlatButton(
                text="On" if state else "Off",
                size_hint_x=None,
                width=dp(100),
                md_bg_color="#2d6c7a" if state else "#e76f51"
            )
            button.bind(on_press=self.create_toggle_room_callback(room_number))
            table_layout.add_widget(button)

        scroll_view.add_widget(table_layout)
        self.add_widget(scroll_view)


    def create_toggle_room_callback(self, room_number):
        def toggle_room_callback(instance):
            session = Session()
            room = session.query(Room).filter_by(room_number=room_number).first()
            if room:
                room.is_empty = not room.is_empty
                session.commit()
                session.close()

                session = Session()
                updated_room = session.query(Room).filter_by(room_number=room_number).first()
                session.close()

                if updated_room:
                    # Update button color based on the updated room state
                    button = instance
                    button.md_bg_color = "#2d6c7a" if updated_room.is_empty else "#e76f51"
                    button.text = "On" if updated_room.is_empty else "Off"
            else:
                print(f"Room with number {room_number} not found.")


        return toggle_room_callback




#______________________________________________________HOME SCREEN ______________________________________________________________________________

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name = 'main'


        with self.canvas.before:
            window_width, window_height = Window.size
            self.background_image = Image(source='img/back.jpeg', allow_stretch=True, size=(window_width, window_height))  # Replace with your image path


    def update_background(self, instance, value):
        self.background_image.pos = self.pos
        self.background_image.size = self.size




#______________________________________________________CLASS TO RUN THE CODE______________________________________________________________________________

class Example(MDApp):
    def build(self):

        # Create the screen manager
        self.screen_manager = ScreenManager()
        main_screen = MainScreen()
        Patient_screen = PatientScreen()
        Employee_screen = EmployeeScreen()
        Appointment_screen = Appointment()
        add_patient = AddPatientScreen()
        add_employee = AddEmployeeScreen()
        add_appointment = AddAppointmentScreen()
        room_screen = RoomScreen()

        
        self.screen_manager.add_widget(main_screen)
        self.screen_manager.add_widget(Patient_screen)
        self.screen_manager.add_widget(Employee_screen)
        self.screen_manager.add_widget(Appointment_screen)
        self.screen_manager.add_widget(add_patient)
        self.screen_manager.add_widget(add_employee)
        self.screen_manager.add_widget(add_appointment)
        self.screen_manager.add_widget(room_screen)
        

        buttom_nav = MDBottomNavigation(
            size_hint=(1, 0.017),
            selected_color_background="#AFC8CB",
            text_color_active="black",
        )

        tab1 = MDBottomNavigationItem(name='main', text='Home', icon='stethoscope')
        tab2 = MDBottomNavigationItem(name='PatientScreen', text='Patient', icon='account-group')
        tab3 = MDBottomNavigationItem(name='EmployeeScreen', text='Employee', icon='doctor')
        tab4 = MDBottomNavigationItem(name='AddAppointmentScreen', text='Appointment', icon='calendar-badge')
        tab5 = MDBottomNavigationItem(name='RoomScreen', text='Room', icon='bed')


        tab1.bind(on_tab_press=lambda x: self.switch_to_screen('main'))
        tab2.bind(on_tab_press=lambda x: self.switch_to_screen('PatientScreen'))
        tab3.bind(on_tab_press=lambda x: self.switch_to_screen('EmployeeScreen'))
        tab4.bind(on_tab_press=lambda x: self.switch_to_screen('Appointment'))
        tab5.bind(on_tab_press=lambda x: self.switch_to_screen('RoomScreen'))


        buttom_nav.add_widget(tab1)
        buttom_nav.add_widget(tab2)
        buttom_nav.add_widget(tab3)
        buttom_nav.add_widget(tab4)
        buttom_nav.add_widget(tab5)


        # Adjust size_hint and pos_hint of the BoxLayout containing the cards
        layout = BoxLayout(orientation='vertical', spacing=2, padding=2)
        layout.add_widget(self.screen_manager)
        layout.add_widget(buttom_nav)

        return layout


    def switch_to_screen(self, screen_name):
        self.screen_manager.current = screen_name

Example().run()