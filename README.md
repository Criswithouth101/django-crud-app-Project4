# 📚 The Literaalley

<img width="1423" height="616" alt="Screenshot 2025-10-27 at 22 24 07" src="https://github.com/user-attachments/assets/81c5f6c9-eade-41fe-aef2-62725026a232" />




**The Literaalley** is a cozy, book-lover’s web application that lets users build their own personal library — a digital nook for organizing books, writing reviews, and sharing thoughts.  

Users can sign up, log in, and manage their own collection of books — each with detailed metadata, cover images, and reader reviews. Built with **Django REST Framework** on the backend and **React** on the frontend, *The Literaalley* blends functionality with a warm, reader-friendly interface. ✨

---

## ✨ Features (MVP)

- 🔐 **User Authentication** — Sign up, log in, and log out securely.  
- 🏠 **Homepage Dashboard** — Navigate through your collection easily.  
- 📖 **Book Management**
  - Add a new book (title, author, genre, description, optional cover image)
  - Edit or delete your own books
  - View all your books in a clean, organized layout
- ⭐ **Reviews**
  - Add reviews (rating + comment) to any book  
  - View all reviews associated with a book  
- 🔍 **Search Bar** — Find books quickly by title or author.  
- 🔒 **User Privacy** — Users can only access and edit their own data.  

---

## 🧩 Tech Stack

### **Backend**
- [Django 5.2.7](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [CORS Headers](https://pypi.org/project/django-cors-headers/)
- Custom JWT Authentication (`authentication` app)
- Pagination and secure access control
- Before connecting the frontend, all API endpoints were tested using Postman, including authentication, CRUD operations for books, and review management.

### **Frontend**
- [React](https://react.dev/)
- [React Router DOM](https://reactrouter.com/)
- Modern functional components and hooks
- Fairy-cozy themed UI for a relaxed reading atmosphere ✨📖  

---
### **🪄 Usage**
- Register or log in to your account.
- Add books you own or love to read.
- Write reviews and rate them.
- Search and manage your personal library — it’s all yours!

--- 

### **Future Improvements**
- 📸 Upload custom book covers directly from the UI
- 💬 Public book sharing and comment threads

---

## ⚙️ Installation & Setup


### **Backend (Django)**

```bash
# Clone the repository
git clone https://github.com/yourusername/the-literaalley.git
cd the-literaalley/backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up the database
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run the development server
python manage.py runserver




