import tkinter as tk  # Importing the tkinter library and aliasing it as 'tk'
from categorical import categorical_conditions  # Importing the 'categorical_conditions' module from a custom file
from numerical import numerical_conditions  # Importing the 'numerical_conditions' module from a custom file

def determine_weather_forecast(user_input):
    # Initialize the conditions dictionary for user input
    conditions = {}

    # Process the input
    for key, value in user_input.items():
        if key in categorical_conditions[0]['conditions']:
            conditions[key] = str(value).lower()  # Convert value to lowercase string and store in 'conditions' dictionary
        else:
            try:
                conditions[key] = float(value)  # Convert value to float and store in 'conditions' dictionary
            except ValueError:
                conditions[key] = str(value).lower()  # Convert value to lowercase string and store in 'conditions' dictionary

    # Find matching weather forecast based on conditions
    for rule in categorical_conditions:
        if all(key in conditions and conditions[key] == value for key, value in rule['conditions'].items()):
            return rule['result'], rule['explanation']  # Return the forecast and explanation if conditions match

    for rule in numerical_conditions:
        if all(
            (key in conditions and is_numerical(conditions[key]) and rule['conditions'][key][0] <= float(conditions[key]) <= rule['conditions'][key][1])
            if key in rule['conditions'] and len(rule['conditions'][key]) == 2
            else (key in conditions and conditions[key] == rule['conditions'][key])
            if key in rule['conditions']
            else True
            for key in rule['conditions']
        ):
            return rule['result'], rule['explanation']  # Return the forecast and explanation if conditions match

    return 'No matching weather forecast found.', 'Couldn\'t find any thing to Explain,you can fill the field again to pridict the weather'

def is_numerical(value):
    try:
        float(value)
        return True  # Return True if value can be converted to a float
    except ValueError:
        return False  # Return False if value cannot be converted to a float

# Define the list of parameters
parameters = [
    'Temperature', 'Humidity', 'Dew Point', 'Wind Speed',
    'Visibility', 'Precipitation', 'Cloud Cover', 'Wind Direction'
]

def determine_weather():
    user_input = {}

    # Get the values from the entry fields
    for parameter in parameters:
        value = entry_fields[parameter].get()
        user_input[parameter] = value  # Store the parameter value in the 'user_input' dictionary

    if all(value for value in user_input.values()):
        # If all fields are filled, determine the weather forecast
        forecast, explanation = determine_weather_forecast(user_input)
        result_label.config(text=f"Weather Forecast: {forecast}")
        explanation_label.config(text=f"Explanation: {explanation}")

        # Clear the entry fields
        for entry in entry_fields.values():
            entry.delete(0, tk.END)

        # Reset the focus to the first entry field
        entry_fields[parameters[0]].focus_set()
    else:
        # If any field is empty, hide the result labels
        forecast = "No matching weather forecast found."
        explanation = "Nothing to explain, please fill again"
        result_label.config(text=f"Weather Forecast: {forecast}")
        explanation_label.config(text=f"Explanation: {explanation}")

    # Update the grid layout
    result_label.grid(row=len(parameters) + 4, column=0, columnspan=2, sticky='w', padx=20, pady=(20, 5))
    explanation_label.grid(row=len(parameters) + 5, column=0, columnspan=2, sticky='w', padx=20, pady=5)

# Create the main window
window = tk.Tk()  # Create a new Tkinter window object
window.title("Weather Forecast Expert System")  # Set the window title

# Set the window size
window.geometry("700x500")

# Create a welcome message
welcome_label = tk.Label(window, text="Welcome to TSK Weather Forecasting!", font=('Arial', 16, 'bold'), fg='dark blue')
welcome_label.grid(row=0, column=0, pady=10, columnspan=2, sticky='w', padx=50)

# Create entry fields and labels for each parameter
entry_fields = {}
for i, parameter in enumerate(parameters):
    label = tk.Label(window, text=parameter, font=('Arial', 12), fg='black')
    label.grid(row=i + 1, column=0, padx=(20, 5), pady=5, sticky='w')
    entry = tk.Entry(window)  # Create an entry field widget
    entry.grid(row=i + 1, column=1, padx=(0, 20), pady=5)
    entry_fields[parameter] = entry  # Store the entry field in the 'entry_fields' dictionary

# Create the "Determine Weather" button
button = tk.Button(window, text="Determine Weather", command=determine_weather, bg='light green', width=20)
button.grid(row=len(parameters) + 3, column=0, pady=(20, 0), columnspan=2, sticky='n')

# Create labels for displaying the result
result_label = tk.Label(window, text="", font=('Arial', 12, 'bold'), fg='dark blue')
explanation_label = tk.Label(window, text="")

# Start the main event loop
window.mainloop()  # Run the Tkinter event loop
