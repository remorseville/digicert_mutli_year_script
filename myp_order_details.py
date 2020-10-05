import os
import requests
import json
import csv

api_key = ""        #DigiCert API Key
order_number =      #DigiCert order number / No quotes

headers = {
    'X-DC-DEVKEY': f'{api_key}',
    'Content-Type': "application/json"
}


# Gets Reissued Certificate Details & Processing
def details(order_id):
    url = f'https://www.digicert.com/services/v2/order/certificate/{order_id}/reissue'
    response = requests.request("GET", url, headers=headers)
    data = response.text
    json_data = json.loads(data)

    with open("_temp_", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["#", "certificate_id", "thumbprint", "serial_number", "common_name", "dns_names", "status", "valid_till", "days_left", "type"])
    file.close()

    counter = 0
    array = []
    for certs in json_data["certificates"]:

        counter = counter + 1
        cert_id = certs["id"]
        thumbprint = certs["thumbprint"]
        serial_number = certs["serial_number"]
        dns_names = certs["dns_names"]
        status = certs["status"]
        days = certs["days_remaining"]
        cn = certs["common_name"]

        try:
            valid_till = certs["valid_till"]
        except KeyError:
            valid_till = "null"

        if status != "":
            print(" Cert_ID #:", cert_id, cn, " Status:", status, " Valid Until:", valid_till, "   Days Left:", days,
                  "  Type: Reissue")
            string = str(dns_names)
            string = f'"${string}$"'
            string = string.replace(",", " ")
            new_dns_names = json.loads(string)
            array.append(
                [counter, cert_id, thumbprint, serial_number, cn, new_dns_names, status, valid_till, days,
                 "reissue"])

    dupe_data = dupe(order_number)  # Gets Duplicate Details for processing
    for certs in dupe_data["certificates"]:

        counter = counter + 1
        cert_id = certs["id"]
        thumbprint = certs["thumbprint"]
        serial_number = certs["serial_number"]
        dns_names = certs["dns_names"]
        status = certs["status"]
        days = certs["days_remaining"]
        cn = certs["common_name"]

        try:
            valid_till = certs["valid_till"]
        except KeyError:
            valid_till = "null"

        if status != "":
            print(" Cert_ID #:", cert_id, cn, " Status:", status, " Valid Until:", valid_till, "   Days Left:", days,
                  "  Type: Duplicate")
            string = str(dns_names)
            string = f'"${string}$"'
            string = string.replace(",", " ")
            new_dns_names = json.loads(string)
            array.append(
                [counter, cert_id, thumbprint, serial_number, cn, new_dns_names, status, valid_till, days, "duplicate"])

    with open("_temp_", "a", newline="\n", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',', lineterminator='\n')
        for x in array:
            writer.writerow([x])
        file.close()

    with open("_temp_", 'r') as file, open('data.csv', 'w') as outfile:
        text = file.read()
        text = text.replace("[", "")
        text = text.replace("]", "")
        text = text.replace('"', "")
        text = text.replace('$', '"')

        order_info = order_details(order_number)  # Gets order expiration date

        writer = csv.writer(outfile, delimiter=',')

        outfile.write(text)
        writer.writerow([order_info])
        file.close()
        outfile.close()
    os.remove("_temp_")


# Gets Duplicate Cert Details
def dupe(order_id):
    url = f'https://www.digicert.com/services/v2/order/certificate/{order_id}/duplicate'
    response = requests.request("GET", url, headers=headers)
    data = response.text
    json_data = json.loads(data)
    return json_data


# Gets order expiration date
def order_details(order_id):
    order_url = f'https://www.digicert.com/services/v2/order/certificate/{order_id}'
    response2 = requests.request("GET", order_url, headers=headers)
    data2 = response2.text
    json_data2 = json.loads(data2)
    # print(json_data2)
    order_val = json_data2["order_valid_till"]
    print(" Order Expiration Date: ", order_val)
    print(" CSV saved as 'data.csv'")
    return f"Order Expiration Date: {order_val}"


details(order_number)



