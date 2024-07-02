#import qrcode

def generate_qr_code(name, roll_number, branch, cgpa, filename):
    data = f"Name: {name}\nRoll Number: {roll_number}\nBranch: {branch}\nCGPA: {cgpa}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    name = input("Enter Name: ")
    roll_number = input("Enter Roll Number: ")
    branch = input("Enter Branch: ")
    cgpa = input("Enter CGPA: ")
    filename = input("Enter filename to save QR code as .png file: ")

    generate_qr_code(name, roll_number, branch, cgpa, filename)
    print(f"QR code saved as {filename}")
