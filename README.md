
## FastAPI REST API

A simple yet advanced REST API built with **FastAPI** in Python.

### 🔧 Features

* **CRUD Operations** (Create, Read, Update, Delete)
* **Search Items by Price Range**
* **Automatic API Docs with Swagger UI**
* Fast and easy to extend

---

### 📦 Requirements

* Python 3.8+
* FastAPI
* Uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
```

---

### ▶️ Running the App

```bash
uvicorn main:app --reload
```

Visit:

* API Root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 📌 API Endpoints

| Method | Endpoint             | Description                 |
| ------ | -------------------- | --------------------------- |
| GET    | `/`                  | API Home                    |
| GET    | `/items`             | List all items              |
| GET    | `/items/{item_name}` | Get specific item by name   |
| POST   | `/items/`            | Create a new item           |
| PUT    | `/items/{item_name}` | Update an existing item     |
| DELETE | `/items/{item_name}` | Delete an item              |
| GET    | `/search/`           | Search items by price range |

#### 🔍 Search Example:

```
GET /search/?min_price=50&max_price=150
```

---

### ✅ Example Item JSON:

```json
{
  "name": "Laptop",
  "price": 999.99,
  "quantity": 5,
  "description": "High-performance laptop"
}
```

---

### 📝 License

This project is open-source and free to use.

---

