import streamlit as st
import pandas as pd
import os

def save_to_excel(data):
    filename = 'SimpleApp1.xlsx'

    # Load existing data from Excel file or create a new DataFrame
    try:
        df = pd.read_excel(filename)
    except FileNotFoundError:
        df = pd.DataFrame()

    # Append the new data to the DataFrame
    new_data = pd.DataFrame(data)
    df = df.append(new_data, ignore_index=True)

    # Save the updated DataFrame back to the Excel file
    df.to_excel(filename, index=False)

    # Commit and push the Excel file to GitHub
    os.system('git add SimpleApp1.xlsx')
    os.system('git commit -m "Update Excel file"')
    os.system('git push origin main')

def main():
    st.title("Simple Application")

    # Input fields
    detail = st.text_input("Detail")
    req_id = st.text_input("Req Id")
    date = st.date_input("Date")

    customer = st.text_input("Customer")
    delivery_loc = st.text_input("Delivery loc")
    sales_person = st.text_input("Sales person")
    sales_or_foc = st.selectbox("Sale type", ["Sale", "FOC"])

    invoice_number = st.text_input("Invoice number")
    invoice_date = st.date_input("Invoice date")

    sr_number = st.text_input("SR number")
    part_no = st.text_input("Part number")
    description = st.text_input("Description")
    qty = st.number_input("Quantity", min_value=1, step=1)
    price = st.number_input("Price", min_value=0.0, step=0.01)

    if st.button("Submit"):
        # Create a dictionary with the input data
        data = {
            "Detail": [detail],
            "Req Id": [req_id],
            "Date": [date],
            "Customer": [customer],
            "Delivery loc": [delivery_loc],
            "Sales person": [sales_person],
            "Sales or FOC (dd)": [sales_or_foc],
            "Invoice number": [invoice_number],
            "Invoice date": [invoice_date],
            "SR number": [sr_number],
            "Part number": [part_no],
            "Description": [description],
            "Quantity": [qty],
            "Price": [price]
        }
        
        # Call the save_to_excel function
        save_to_excel(data)
        st.success("Data saved successfully")

if __name__ == "__main__":
    main()
