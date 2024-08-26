import frappe
import requests
import os
import csv


@frappe.whitelist()
def fetch_fund_data():
    file_path = "funds.csv"
    if not os.path.exists(file_path):
        csv_url = "https://api.kite.trade/mf/instruments"
        response = requests.get(csv_url)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                file.write(response.content)

    funds_data = process_csv(file_path)

    for fund in funds_data:
        if fund[2] != 'growth' or fund[4] != 'direct':
            continue
        exists = frappe.db.exists("Fund", fund[0])
        if exists:
            pass
            # existing_fund = frappe.get_doc("Fund", fund[0])
            # existing_fund.update({
            # "tradingsymbol": fund[0], 
            # "dividend_type": fund[2],
            #     "scheme_type": fund[3],
            #     "plan": fund[4],
            #     "last_price": fund[5]
            # })
            # existing_fund.save()
        else:
            new_fund = frappe.get_doc({
                "doctype": "Fund",
                "tradingsymbol": fund[0], 
                "fund_name": fund[1],
                "dividend_type": fund[2],
                "scheme_type": fund[3],
                "plan": fund[4],
                "last_price": fund[5]
            })
            new_fund.insert()

    frappe.db.commit()
    return "Fund updated successfully"

def process_csv(file_path):
    data = []
    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(
                (
                    row["tradingsymbol"],
                    row["name"],
                    row["dividend_type"],
                    row["scheme_type"],
                    row["plan"],
                    row["last_price"],
                )
            )
    return data