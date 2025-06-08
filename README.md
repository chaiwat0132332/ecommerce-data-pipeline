# 🛒 E-commerce Data Pipeline (Python + SQLite)

> ระบบ ETL จำลองข้อมูลร้านค้าออนไลน์: ดึง → แปลง → เก็บ → วิเคราะห์  
> เหมาะสำหรับใช้ใน Portfolio หรือสมัครงานสาย Data Engineer

---

## 📦 Tools & Tech
- Python 3 + Pandas
- SQLite (local database)
- Shell Script (`run_pipeline.sh`)
- Git + GitHub

---

## 🔁 Pipeline Flow
1. ดึงข้อมูลจาก Fake Store API (`fetch_data.py`)
2. ทำความสะอาดและแปลงข้อมูล (`transform_data.py`)
3. โหลดเข้า SQLite (`load_to_sqlite.py`)
4. วิเคราะห์ด้วย SQL (`analyze.py`)

---

## 📁 โครงสร้างโปรเจ็ค
ecommerce_data_pipeline/
├── scripts/ # Python scripts
├── data/ # raw & clean CSVs
├── db/ # SQLite database
├── run_pipeline.sh # pipeline รันอัตโนมัติ
├── pipeline.log # log ข้อมูลการรัน
└── README.md

---

## 📈 ตัวอย่างผลลัพธ์

| Category        | Avg Price | Total Products |
|----------------|-----------|----------------|
| Electronics     | 332.49    | 4              |
| Jewelry         | 276.99    | 4              |
| Men's Clothing  |  55.96    | 4              |

---

## ▶️ วิธีรันโปรเจ็ค

```bash
# ติดตั้งไลบรารีที่จำเป็น
pip install pandas requests

# รัน pipeline ทั้งหมด
sh run_pipeline.sh
ผลลัพธ์จะถูกบันทึกไว้ใน pipeline.log
ฐานข้อมูลจะอยู่ที่ db/ecommerce.db

ใช้โปรเจ็คนี้เพื่อ

ฝึกการทำ ETL pipeline ตั้งแต่ต้นจนจบ
ใช้โชว์ใน GitHub / Resume
ต่อยอดสู่ Airflow, Docker, หรือ Cloud ได้

Author

Chaiwat
GitHub: chaiwat0123323

⭐️ ฝาก Star ถ้าชอบ | Fork ไปต่อยอดได้เลย
