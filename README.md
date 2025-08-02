# 🔎 Simple Network Scanner (with Flask GUI)

A Python-based network scanner built using `scapy` and `Flask` that scans a subnet for live devices and open ports. Built in **Kali Linux** for cybersecurity projects and resumes.

---

## ⚙️ Features

- Scan entire local subnet (e.g., `192.168.1.0/24`)
- Shows live IPs, MAC addresses, and open ports
- Export results as `.txt`
- Flask-based web GUI
- Works on Kali Linux and any Linux distro with Python 3

---

## 🧰 Requirements

- Python 3
- `scapy`
- `flask`

---

## 🔧 Installation (Kali Linux & others)

### 1. Clone the Repo

```bash
git clone https://github.com/darshanchauhan11/simple-network-scanner.git
cd simple-network-scanner
```

### 2. Create Virtual Environment *(optional but recommended)*

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Scanner (Web GUI)

```bash
sudo python3 app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

> **Note:** Run with `sudo` for access to low-level network scanning.

---

## 📄 File Structure

```
├── app.py                # Flask web app
├── requirements.txt      # Python dependencies
├── scan_results.txt      # Saved output
├── templates/
│   └── index.html        # Web UI
```

---

## ✏️ How It Works

- User inputs a subnet like `192.168.0.0/24`
- `scapy` sends ARP requests to each IP
- Results are displayed on the web interface
- You can export scan results as a `.txt` file

---

## 📌 Notes

- This is for educational and ethical use only.
- Tested on Kali Linux 2025.2 inside VMware.
- Do not scan networks without permission.

---

## 🧑‍💻 Author

**Darshan Chauhan**  
GitHub: [@darshanchauhan11](https://github.com/darshanchauhan11)

---

## ✅ To Upload this to GitHub

```bash
git add README.md
git commit -m "Add README with installation and usage steps"
git push
```
