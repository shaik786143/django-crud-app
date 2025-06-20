# Django AWS CI/CD Example

![Build Status](https://github.com/shaik786143/django-crud-app/actions/workflows/django-cicd.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

This project demonstrates a Django application deployed to AWS EC2 using Docker and a GitHub Actions CI/CD pipeline. It includes integration with AWS RDS (database) and ECR (container registry).

---

## 🚀 Features
- Django CRUD app
- Dockerized for consistent deployment
- CI/CD pipeline with GitHub Actions
- Automatic deployment to AWS EC2
- Uses AWS RDS for database
- Static files support

---

## 📸 Screenshots

### Home Page
![Home Page](screenshots/homepage.png)

### GitHub Actions Workflow
![CI/CD Pipeline](screenshots/github-actions.png)

*Replace these images with your own screenshots in the `screenshots/` folder!*

---

## 📝 How to Clone and Run Locally

1. **Clone the repository:**
   ```sh
   git clone https://github.com/shaik786143/django-crud-app.git
   cd django-crud-app
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Open your browser:**
   - Go to `http://127.0.0.1:8000/`

---

## 🐳 How to Run with Docker (Locally)

1. **Build the Docker image:**
   ```sh
   docker build -t django-app .
   ```
2. **Run the container:**
   ```sh
   docker run -d -p 8000:8000 django-app
   ```
3. **Visit:**
   - `http://localhost:8000/`

---

## ☁️ How to Set Up CI/CD Pipeline (GitHub Actions + AWS)

### 1. **Fork or Clone this Repository**

### 2. **Create AWS Resources**
- **EC2 Instance** (Ubuntu recommended)
- **RDS Database** (MySQL/PostgreSQL)
- **ECR Repository** (for Docker images)
- **IAM User** with permissions for EC2, ECR, and RDS

### 3. **Add GitHub Secrets**
Go to your repo → Settings → Secrets and variables → Actions → New repository secret. Add:
- `AWS_ACCESS_KEY_ID` (from IAM user)
- `AWS_SECRET_ACCESS_KEY` (from IAM user)
- `EC2_SSH_KEY` (contents of your .pem file)
- `EC2_HOST` (EC2 public IP or DNS)
- `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` (from RDS)
- `AWS_REGION` (e.g., ap-south-1)

### 4. **Configure Your Django `settings.py`**
- Use environment variables for database settings (see `aws/settings.py`).
- Set `STATIC_ROOT` for static files.

### 5. **GitHub Actions Workflow**
- The `.github/workflows/django-cicd.yml` file is already set up to:
  - Build and push Docker image to ECR
  - SSH into EC2 and deploy the new image

### 6. **Deploy**
- Just push to the `main` branch:
  ```sh
  git add .
  git commit -m "Your message"
  git push
  ```
- The workflow will build, push, and deploy automatically.

---

## 📦 Project Structure

```
aws/
  aws/                # Django project settings
  testapp/            # Django app
  Dockerfile          # Docker build file
  docker-compose.yml  # For local dev (optional)
  requirements.txt    # Python dependencies
  .github/workflows/  # CI/CD pipeline config
```

---

## 🙋‍♂️ Author
- [shaik786143](https://github.com/shaik786143)

---

## 📝 License
This project is for learning and portfolio purposes. 