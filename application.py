import pywebio
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_html, put_markdown, put_table

def Loan_details():
    empid = input("Enter your EmployeeID：", type=FLOAT)
    Loan_amount = input("Enter your Loan amount:", type=FLOAT)

    Loan_Interest = (Loan_amount / 100) * 6.75 
    put_markdown('#**Pay your Interest**')
    put_text("Loan amount to be paind for this month %.1f" %(Loan_amount))
    put_html('<br><br>')
    put_markdown('`%.1f` is your Loan Interest to be paid'%(Loan_Interest))
    put_html('<hr>')

if __name__ == "__main__":
    pywebio.start_server(Loan_details, port=8000)
