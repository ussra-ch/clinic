# Hospital Management App

## Description
The Clinic Management App is a locally deployable application written in Python using SQLAlchemy for database management and Kivy for the user interface. It is designed to streamline clinic operations, providing functionality for managing patients, employees, appointments, and room occupancy.

## Technologies Used
- **Python:** Backend development.
- **SQLAlchemy:** Database management.
- **Kivy:** User interface development.

## Prerequisites
Before running the Clinic Management App, ensure you have the following:
- Python installed on your machine.
- Access to a phpMyAdmin instance for managing the app's database.
- Basic understanding of Python programming and database concepts.

## Screens

### Home Screen
- Displays the clinic's menu and essential information.
- Allows users to add, view, and delete patient and employee information.


### Patient Screen
- Enables users to add, view, and delete patient information.
- Provides a user-friendly interface for managing patient records.

### Employee Screen
- Allows users to add, view, and delete employee information.
- Provides similar functionality to the patient screen for managing employee records.

### Appointment Screen
- Enables users to schedule appointments by selecting a patient, employee, room, and date.

### Room Screen
- Provides functionality to view and manage the occupancy status of clinic rooms.
- Allows users to toggle room states between empty and occupied by clicking on the corresponding buttons.

## Installation
1. Clone the repository to your local machine:
git clone git@github.com:ussra-ch/clinic.git
2. Navigate to the project directory:
cd clinic
3. Start the application:
python clinic2.py

## Usage
1. **Home Screen:**
- Upon starting the application, navigate to the home screen.
- Use the provided sections to manage patient and employee information.
<img src="homeScreen.png" alt="Home Screen" width="800"/>


2. **Patient and Employee Screens:**
- Access the patient and employee screens to add, view, and delete patient and employee information, respectively.
- Patient screen :
<img src="PatientScreen.png" alt="Patient Screen" width="800"/>
- Add Patient screen :
<img src="addPatient.png" alt="Add patient" width="800"/>
- Show patient's informations :
<img src="ShowPatient.png" alt="Show patient" width="800"/>
- Employee screen :
<img src="EmployeeScreen.png" alt="Employee Screen" width="800"/>
- Show Employee's informations :
<img src="showemployee.png" alt="Show employee" width="800"/>

3. **Appointment Screen:**
- Access the appointment screen to schedule new appointments.
<img src="AppointmentScreen.png" alt="Show employee" width="800"/>
- Select a patient, employee, room, and date to book an appointment.
<img src="addAppointment.png" alt="Show employee" width="800"/>

4. **Room Screen:**
- View the current occupancy status of clinic rooms.
- Toggle room states between empty and occupied by clicking on the corresponding buttons.
<img src="RoomScreen.png" alt="Show employee" width="800"/>

## Version History
- **Version 1.0:**
- Initial release with basic functionality.
