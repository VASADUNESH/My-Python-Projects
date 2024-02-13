Tax Calculator GUI Application

This Python program, "tax_calculator.py", is a graphical user interface (GUI) application built using the `customtkinter` library. It allows users to calculate tax based on their income and tax rate.

Installation:

Before running the program, make sure you have installed the customtkinter library by executing the following command:
=>  pip install customtkinter


Program Description:

The program creates a simple GUI window titled "Tax calculator" with fields to input income and tax rate. Upon clicking the "Calculate" button, it computes the tax based on the provided inputs and displays the result.

Components of the Program:

1. Initialization:
   - The program initializes the GUI window using the CTk() class from the customtkinter library.
   - It sets the title, dimensions, and disables resizing of the window.

2. Input Fields:
   - The GUI includes input fields for entering income and tax rate, labeled accordingly.

3. Result Field:
   - It displays the calculated tax amount based on the provided income and tax rate.
   - Initially, it's set to display '0' as a default value.

4. Calculate Button:
   - The "Calculate" button triggers the computation of tax based on the entered values.
   - Upon clicking, it calls the "calculate_tax()" method.

5. Functionality:
   - The "calculate_tax()" method retrieves the income and tax rate from the input fields, computes the tax amount, and updates the result field.
   - It handles invalid input values gracefully by displaying an error message in the result field.

6. Main Loop:
   - The "run()" method starts the main event loop, allowing the GUI to respond to user interactions.
   - It keeps the window open until the user closes it.

7. Execution:
   - The program entry point checks if the script is being run directly ('__name__' == '__main__') and creates an instance of the 'tax_calculator' class, initiating the GUI application.

 Usage:

1. Run the program by executing the script.
2. Enter the income and tax rate in their respective fields.
3. Click the "Calculate" button to compute the tax amount.
4. View the calculated tax amount in the result field.

Note:

- Ensure that you have installed the 'customtkinter' library before running the program.
- The program assumes valid numeric inputs for income and tax rate. Invalid inputs will result in an error message.

This tax calculator provides a simple and user-friendly interface for quickly calculating taxes based on income and tax rate inputs.