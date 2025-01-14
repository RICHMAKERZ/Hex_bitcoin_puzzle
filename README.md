# Hex_bitcoin_puzzle

Hex_bitcoin_puzzle is a Python script designed to scan ranges of Bitcoin private keys to generate corresponding Bitcoin addresses and check their activity. The results are stored in multiple CSV files, making it easier to analyze large amounts of data. This project is a great tool for educational purposes and exploring cryptographic principles.

---

## Features

- Generates Bitcoin addresses from private keys using the SECP256k1 elliptic curve.
- Checks the activity of Bitcoin addresses via the Blockchain.com API.
- Saves results in multiple CSV files, with each file containing up to 1000 results.
- Automatically creates new CSV files when the results exceed the file limit.

---

## Prerequisites

To run this script, you need the following:

1. **Python 3.7+**
2. **Required Python libraries**:
   - `ecdsa`
   - `requests`
   - `hashlib`

You can install the required libraries using pip:
```bash
pip install ecdsa requests
```

---

## Usage

1. Clone or download this repository.
2. Open a terminal and navigate to the script’s directory.
3. Run the script using Python:
   ```bash
   python hex.py
   ```
4. Enter the desired output file prefix (e.g., `results`).
5. The script will scan the predefined ranges of private keys and save the results in multiple CSV files.

---

## Example Output

If the output prefix is `results`, the script will create files such as:

- `results_1.csv`
- `results_2.csv`
- `results_3.csv`

Each file will contain columns:
- `Private Key`
- `Address`
- `Status`

---

## Customization

You can modify the `batches` variable in the script to specify different ranges of private keys. Ensure that the ranges are in hexadecimal format and 64 characters long.

Example:
```python
batches = [
    ("574ec624aa1f283d4b98740e0b41dfdfa91ad44abb8ef8f4c6f9cdff89c4c3a8",
     "005147b67bb62727e8671e9f48e03235fd298d0a1f27f1986d80551b704504bc"),
]
```

---

## Bitcoin Address for Support

If you find this project helpful and wish to support further development, consider sending Bitcoin to the following address:

**12yM3UBPiWDzE1asXdMsLFNQJ1MYosxaWD**

Your support is greatly appreciated!

---

## Disclaimer

This script is for educational purposes only. It should not be used for unauthorized activities. The author is not responsible for any misuse of this code.

---

## License

This project is open-source and available under the MIT License.

