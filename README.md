🧑‍💻 Created By
| Python & Django Developer
# 💰 Finance View Tracker

A clean, user-friendly **Django-based personal finance tracker** that lets users manage their income, expenses, and financial goals.  
Every user gets their own dashboard, transaction reports, goal tracking, and downloadable reports.

![Finance Tracker Screenshot](<img width="1904" height="892" alt="Screenshot from 2025-07-20 15-57-24" src="https://github.com/user-attachments/assets/31ccea70-ed11-44e3-bed0-c41fc9d8d15d" />
<img width="1904" height="892" alt="Screenshot from 2025-07-20 15-51-40" src="https://github.com/user-attachments/assets/b890cd07-a856-420f-a1cf-5597a8f175da" />
<img width="1904" height="892" alt="Screenshot from 2025-07-20 15-53-40" src="https://github.com/user-attachments/assets/4eee4b4c-b026-4948-a10d-ded57a504b76" />



---

## 🚀 Features

- 🔐 User Signup & Login (session-based)
- 📊 Personal Dashboard with:
  - Total Income
  - Total Expenses
  - Net Savings
- 🧾 Add & View Transactions (filtered per user)
- 🎯 Add & Track Financial Goals (with progress circles)
- 📁 Export transactions as Excel files
- ✅ CSRF-protected forms & secure authentication
- 🎨 Clean and responsive frontend (HTML, CSS)

---

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (default, can switch to PostgreSQL)
- **Export:** `xlsx.js` for Excel download
- **Authentication:** Django’s built-in auth system

---

## 📸 Pages

| Page            | Description                            |
|-----------------|----------------------------------------|
| `Signup/Login`  | User registration and secure login     |
| `Dashboard`     | Summary of income, expenses, savings   |
| `Add Transaction` | Add income/expense with type, date   |
| `Transaction Report` | View & download personal transactions |
| `Add Goal`      | Set goals with target & progress track |
| `Logout`        | Secure logout with session cleanup     |

---
📄 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

## ✅ How to Use

1. Copy the above and save it as `README.md` in your project root.
2. Replace placeholders (`your-username`, screenshot, etc.)
3. Commit and push to GitHub:

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/FinanceTracker.git
cd FinanceTracker
📦 Folder Structure
csharp
Copy
Edit
FinanceTracker/
│
├── financetracker/       # Main Django project
├── finance/              # Your app
│   ├── templates/        # HTML templates
│   ├── static/           # CSS & JS
│   ├── models.py         # Transaction & Goal models
│   ├── views.py          # Core logic
│   └── urls.py
├── db.sqlite3
└── manage.py


```bash
git add README.md
git commit -m "Add project README"
git push origin main
