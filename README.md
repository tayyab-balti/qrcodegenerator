# 🧾 QR Code Generator & Scanner

A Django-based web application for generating and scanning secure QR codes tied to 11-digit mobile numbers. Ideal for payment systems or identity verification at petrol pumps or similar use cases.

---

## 🚀 Features

✅ Generate QR codes with custom data and mobile numbers  
✅ Scan uploaded QR code images and validate them against database records  
✅ Simple and responsive UI using CSS  
✅ Automatically deletes valid scanned codes for security  
✅ File validation and mobile number checking  
✅ Secure and minimal backend logic using Django

---

## 📸 Screenshots

| QR Code Generator |

![Generate](https://github.com/user-attachments/assets/3e86f81b-8d3d-4306-8011-8ec6677a343d)

![Generate-Output](https://github.com/user-attachments/assets/af3857eb-5260-4d13-aed9-e9c8e694502c)

![General-Image](https://github.com/user-attachments/assets/74c77de8-ab88-4a17-9e03-2bb5da459efb)

| QR Code Scanner |

![Scan](https://github.com/user-attachments/assets/75296f55-535e-49f7-bee3-9a4873590024)

![Scan-Output](https://github.com/user-attachments/assets/886679d3-ba3c-426c-b0ef-c958167d1079)

---

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS (custom)
- **QR Code Generator:** `qrcode` Python library  
- **QR Code Scanner:** `pyzbar`, `Pillow`  
- **Storage:** Local file system (`FileSystemStorage`)  
- **Database:** SQLite (default Django DB)

---

## 🧪 How It Works

### 🔹 Generate QR Code
1. User enters a mobile number (11 digits) and a text value.
2. A QR code image is generated with the combined data.
3. QR code is saved and available for download.

### 🔹 Scan QR Code
1. User uploads a QR code image and provides a mobile number.
2. Image is scanned and validated.
3. If matched, the QR entry and QR image are deleted (one-time use).

---

## 💻 Getting Started

### ⚙️ Requirements

- Python 3.8+
- Django 4.x
- `qrcode`, `pyzbar`, `Pillow`

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/tayyab-balti/qrcodegenerator.git
