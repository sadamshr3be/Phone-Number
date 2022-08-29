import requests

ans = "Y"

while ans == "Y":



    number = int(input("Enter Number: "))

    upi = [
        str(number)+"@apl",
        str(number)+"@ybl",
        str(number)+"@oksbi",
        str(number)+"@okhdfcbank",
        str(number)+"@axl",
        str(number)+"@paytm",
        str(number)+"@ibl",
        str(number)+"@upi",
        str(number)+"@icici",
        str(number)+"@sbi",
        str(number)+"@kotak",
        str(number)+"@postbank",
        str(number)+"@axisbank",
        str(number)+"@okicici",
        str(number)+"@okaxis",
        str(number)+"@dbs",
        str(number)+"@barodampay",
        str(number)+"@idfcbank"
    ]

    for num in upi:
        response = requests.post('https://upibankvalidator.com/api/upiValidation', params={"upi":num})
        if "not yet registered" in response.text:
            continue
        else:
            print(response.text, num)

    ans = input("Do You Want To Check Another Number (Y/N): ").upper()
