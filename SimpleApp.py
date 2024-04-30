import streamlit as st
import pandas as pd
import os

def save_to_excel(data):
    filename = 'SimpleApp1.xlsx'
    if not os.path.exists(filename):
        df = pd.DataFrame(columns=data.keys())
        df.to_excel(filename, index=False)
    
    df = pd.DataFrame(data)
    with pd.ExcelWriter(filename, mode='a', engine='openpyxl') as writer:
        if 'Sheet' not in writer.book.sheetnames:
            df.to_excel(writer, index=False, sheet_name='Sheet', engine='openpyxl')
        else:
            df.to_excel(writer, index=False, header=False, sheet_name='Sheet', startrow=writer.sheets['Sheet'].max_row, engine='openpyxl')

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
        st.success("Data saved to SimpleApp1.xlsx")

if __name__ == "__main__":
    main()
