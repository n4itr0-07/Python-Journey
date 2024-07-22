# UPI QR Code Generator

This guide will help you generate QR codes for UPI payment apps (PhonePe, Paytm, and Google Pay) using Python and the `qrcode` library.

## Prerequisites

1. **Python**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **qrcode Library**: Install the `qrcode` library using pip.

   ```sh
   pip install qrcode[pil]
   ```

## Steps

### 1. Set Up the Python Script

Create a new Python file (e.g., `generate_upi_qr.py`) and open it in your favorite code editor.

### 2. Import Required Libraries

Add the following import statement at the top of your Python script:

```python
import qrcode
```

### 3. Take UPI ID as Input

Use the `input` function to take the UPI ID as input from the user:

```python
upi_id = input("Enter your UPI ID : ")
```

### 4. Define the Payment URLs

Define the UPI payment URLs for PhonePe, Paytm, and Google Pay:

```python
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
```

### 5. Generate QR Codes

Generate the QR codes for each payment app:

```python
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)
```

### 6. Save the QR Codes as PNG Files

Save the generated QR codes as PNG files:

```python
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")
```

### 7. Display the QR Codes

Display the generated QR codes:

```python
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
```

### 8. Confirm Completion

Print a success message to confirm that the QR codes have been generated:

```python
print("QR codes generated successfully!")
```

### 9. Full Script

Here is the complete script for reference:

```python
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

# Display the QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

print("QR codes generated successfully!")
```

## Running the Script

1. Open your terminal or command prompt.
2. Navigate to the directory where you saved the `generate_upi_qr.py` file.
3. Run the script using Python:

   ```sh
   python generate_upi_qr.py
   ```

4. Enter your UPI ID when prompted.

The script will generate and display QR codes for PhonePe, Paytm, and Google Pay, and save them as PNG files in the same directory.

[Follow Me ](https://linktr.ee/SalikSerajNaik)
