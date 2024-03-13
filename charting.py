import tkinter as tk
import sqlite3
from tkinter import messagebox

# Function to submit new chart data to database
def submit_chart_data():
    # Open a new window for input
    input_window = tk.Toplevel()
    input_window.title("Input New Chart")

    # Labels and entry fields for input data
    tk.Label(input_window, text="Patient Name:").grid(row=0, column=0)
    patient_name_entry = tk.Entry(input_window)
    patient_name_entry.grid(row=0, column=1)

    tk.Label(input_window, text="Age:").grid(row=1, column=0)
    age_entry = tk.Entry(input_window)
    age_entry.grid(row=1, column=1)

    tk.Label(input_window, text="Symptoms:").grid(row=2, column=0)
    symptoms_entry = tk.Entry(input_window)
    symptoms_entry.grid(row=2, column=1)

    # Function to save data to database
    def save_to_database():
        patient_name = patient_name_entry.get()
        age = age_entry.get()
        symptoms = symptoms_entry.get()

        # Connect to SQLite database
        conn = sqlite3.connect("charts.db")
        c = conn.cursor()

        # Insert data into database
        c.execute("INSERT INTO charts (patient_name, age, symptoms) VALUES (?, ?, ?)", (patient_name, age, symptoms))

        # Commit changes and close connection
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Chart added successfully")
        input_window.destroy()

    # Button to save data
    tk.Button(input_window, text="Save", command=save_to_database).grid(row=3, columnspan=2)

# Function to display all records
def display_records():
    pass

# Function to export chart
def export_chart():
    pass

# Main menu GUI
def main_menu():
    root = tk.Tk()
    root.title("Charting App")

    # Buttons for different functionalities
    btn_new_chart = tk.Button(root, text="Input New Chart", command=submit_chart_data)
    btn_new_chart.pack()

    btn_display_records = tk.Button(root, text="Display Records", command=display_records)
    btn_display_records.pack()

    btn_export_chart = tk.Button(root, text="Export Chart", command=export_chart)
    btn_export_chart.pack()

    root.mainloop()

# Entry point of the application
if __name__ == "__main__":
    main_menu()
