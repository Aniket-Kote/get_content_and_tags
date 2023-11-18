import openpyxl


def w_excel(new_data):
    # Specify the file path of your Excel file
    file_path = 'op.xlsx'

    # Load the Excel workbook
    workbook = openpyxl.load_workbook(file_path)

    # Choose a specific sheet to work with (by default, it selects the first sheet)
    sheet = workbook.active

    # # Data to be inserted as a list of lists
    # new_data = [
    #     ['Name', 'Age', 'City'],
    #     ['John', 30, 'New York'],
    #     ['Alice', 25, 'Los Angeles'],
    #     ['Bob', 28, 'Chicago']
    # ]

    # Determine the starting cell where you want to insert the data
    start_row = sheet.max_row + 1  # Insert after the last row in the sheet

    # Insert the new data into the sheet
    for row_data in new_data:
        sheet.append(row_data)

    # Save the changes back to the Excel file
    workbook.save(file_path)

    # Close the workbook after writing
    workbook.close()
