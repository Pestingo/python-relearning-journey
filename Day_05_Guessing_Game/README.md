# Day 05: Random Number Guessing Game

## 📝 Overview
Day 05 focused on implementing data randomization, real-time comparison algorithms, and tracking progressive computational metrics (attempt counters). The application leverages core input handling patterns alongside conditional validation blocks to guide a user toward an unknown dynamic integer target.

---

## 🚀 Key Concepts Covered

### 1. Pseudo-Random Number Generation
* Importing standard packages (`random`) and using `.randint(start, stop)` to instantiate unpredictability into core program workflows.

### 2. Stream Exception Filtering
* Employing `try-except ValueError` barriers to gracefully reject alphanumeric characters and protect the environment against run-time operational crashes.

### 3. Dynamic State Counters
* Maintaining state across execution loops by incrementing runtime tracking variables (`attempts += 1`) to provide diagnostic scoring feedback upon completion.

---

## 🛠️ Project Structure
* `app.py`: The application game logic containing the random engine initialization, evaluation criteria, and user feedback prompts.

## 💻 How to Run
Ensure your terminal is in the project directory, then run:
```bash
python app.py