CPSC - 3990 Quantitative Financial Analysis and Comparison Using Python
Author: Matthew Gillett
Id: 001230643
--------------------------------------------------------------
Black-Scholes Finanical Model:
    - Call and Put Calculations W/O Dividend.
    - Call and Put Calculations With Dividend.
    - Parsing Through Pre-formated Data in Excel.
    - ** ASKS for dividend if there is not one just put 0
--------------------------------------------------------------
Compiling Code:
    - Spyder IDE:
        1. Make sure excel file is not open when runnig**
        2. Compile by using run file (green play button)
    - Terminal:
        1. python main.py
        2. Runs tests and everything from running main.py
--------------------------------------------------------------
blackscholes.py
    - Handles all calculation function for: 
        1. Call and Put with and without dividends.
        
BlackScholesTest.py
    - Testing functions use similar framework to mock.
        1. All four put and call calculations tested with and without  dividends. 
        2. Getting manual inputs as well as excel inputs.
        
exclparse.py
    - Handels pulling data from excel sheet if user does not want to manually input.

main.py
    - Overall execution of the program and running the tests: 
        1. Prompting the user choice for manual input/excel parse. 
        2. Runs test cases prior to running code to ensure functions are working correctly. 
        3. Handels sequence logic as well as terminal output.
        4. Plotter also runs through main to output chart for each calculation. 
        5. Overvalue or undervalue of option price.
        
plotter.py
    - Function for outputting the ITM, OTM, and ATM chart for visualizing call and put prices
--------------------------------------------------------------
Required Libraries:
    - Numpy, matplotlib, unittest
    - Can use "pip install numpy matplotlib plotter
--------------------------------------------------------------
Data:
    - Pulled from the FactSet data base.
    - Access through dhillon school of business student account.
--------------------------------------------------------------
** Does run on a standard terminal if python is installed and pip installed libraries
** If you want to run on IDE I used https://www.spyder-ide.org/ comes standard with all financial libraries
