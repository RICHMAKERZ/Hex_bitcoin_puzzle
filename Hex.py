import os
import csv
import requests
from ecdsa import SigningKey, SECP256k1
import hashlib

def generate_address(private_key_hex):
    """
    توليد عنوان عام من مفتاح خاص باستخدام منحنى SECP256k1.
    """
    sk = SigningKey.from_string(bytes.fromhex(private_key_hex), curve=SECP256k1)
    vk = sk.get_verifying_key()
    public_key = vk.to_string("compressed").hex()
    sha256 = hashlib.sha256(bytes.fromhex(public_key)).hexdigest()
    ripemd160 = hashlib.new('ripemd160', bytes.fromhex(sha256)).hexdigest()
    address = "1" + ripemd160  # عنوان Bitcoin مبسط (بدون checksum)
    return address

def check_address_activity(address):
    """
    التحقق من نشاط العنوان باستخدام Blockchain.com API.
    """
    url = f"https://blockchain.info/rawaddr/{address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['final_balance'] > 0  # True إذا كان العنوان يحتوي على أموال
    except Exception as e:
        print(f"Error checking address {address}: {e}")
    return False

def scan_batches(batches, output_prefix, results_per_file=1000):
    """
    مسح النطاقات المحددة للعناوين النشطة وحفظها في ملفات CSV متعددة.
    """
    file_count = 1
    result_count = 0
    current_file = f"{output_prefix}_{file_count}.csv"
    
    # فتح أول ملف كتابة
    file = open(current_file, mode='w', newline='')
    writer = csv.writer(file)
    writer.writerow(['Private Key', 'Address', 'Status'])  # كتابة العناوين

    for batch in batches:
        start_hex, end_hex = batch
        start = int(start_hex, 16)
        end = int(end_hex, 16)
        
        for private_key_int in range(start, end + 1):
            private_key_hex = f"{private_key_int:064x}"
            address = generate_address(private_key_hex)
            is_active = check_address_activity(address)
            status = "Active" if is_active else "Inactive"

            # كتابة النتيجة
            writer.writerow([private_key_hex, address, status])
            result_count += 1
            print(f"Scanned: Private Key = {private_key_hex}, Address = {address}, Status = {status}")

            # إذا وصلنا إلى الحد الأقصى لكل ملف
            if result_count >= results_per_file:
                file.close()  # إغلاق الملف الحالي
                file_count += 1  # زيادة عدد الملفات
                current_file = f"{output_prefix}_{file_count}.csv"  # اسم الملف الجديد
                file = open(current_file, mode='w', newline='')
                writer = csv.writer(file)
                writer.writerow(['Private Key', 'Address', 'Status'])  # كتابة العناوين
                result_count = 0  # إعادة عداد النتائج
        
    file.close()  # إغلاق آخر ملف
    print("\nScanning complete. Results saved to multiple files.")

# النطاقات المحددة
batches = [
    ("574ec624aa1f283d4b98740e0b41dfdfa91ad44abb8ef8f4c6f9cdff89c4c3a8",
     "005147b67bb62727e8671e9f48e03235fd298d0a1f27f1986d80551b704504bc"),
    ("5dc156741146b949f310214f2739a007aed9ab6072cec034220e3de6cc1b536f",
     "c5d89092d817b080db49327a37c7bd3429fced6b40e88c9302be3c5b4fc44c25"),
]

# التنفيذ الرئيسي
if __name__ == "__main__":
    output_prefix = input("Enter output file prefix (e.g., results): ").strip()
    print("\nScanning for active addresses...")
    scan_batches(batches, output_prefix)
