import qrcode

# Taking UPI id as a input
upi_id = input("Enter your UPI ID : ")

# Defining the payment URL based on the UPI and the payment app

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Generating QR codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Saving the QR codes as PNG files

phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

# Display the Qr code

# print("PhonePe QR Code:")
phonepe_qr.show()
# print("\nPayTM QR Code:")
paytm_qr.show()
# print("\nGoogle Pay QR Code:")

google_pay_qr.show()

print("QR codes generated successfully!")

