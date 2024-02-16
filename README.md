<h1>Hospital Management App</h1>
Description
The Clinic Management App is a locally deployable application written in Python using SQLAlchemy for database management and Kivy for the user interface. It is designed to streamline clinic operations, providing functionality for managing patients, employees, appointments, and room occupancy.

Technologies Used
Python: Backend development.
SQLAlchemy: Database management.
Kivy: User interface development.
Prerequisites
Before running the Clinic Management App, ensure you have the following:

Python installed on your machine.
Access to a phpMyAdmin instance for managing the app's database.
Basic understanding of Python programming and database concepts.
Screens
Home Screen
Displays the clinic's menu and essential information.
Allows users to add, view, and delete patient and employee information.
Patient Screen
Enables users to add, view, and delete patient information.
Provides a user-friendly interface for managing patient records.
Employee Screen
Allows users to add, view, and delete employee information.
Provides similar functionality to the patient screen for managing employee records.
Appointment Screen
Enables users to schedule appointments by selecting a patient, employee, room, and date.
Room Screen
Provides functionality to view and manage the occupancy status of clinic rooms.
Allows users to toggle room states between empty and occupied by clicking on the corresponding buttons.
Installation
Clone the repository to your local machine:

bash
Copy code
git clone [repository-url]
Navigate to the project directory:

bash
Copy code
cd clinic-management-app
Install dependencies:

Copy code
pip install -r requirements.txt
Start the application:

css
Copy code
python main.py
Usage
Home Screen:

Upon starting the application, navigate to the home screen.
Use the provided sections to manage patient and employee information.
Patient and Employee Screens:

Access the patient and employee screens to add, view, and delete patient and employee information, respectively.
Appointment Screen:

Access the appointment screen to schedule new appointments.
Select a patient, employee, room, and date to book an appointment.
Room Screen:

View the current occupancy status of clinic rooms.
Toggle room states between empty and occupied by clicking on the corresponding buttons.
