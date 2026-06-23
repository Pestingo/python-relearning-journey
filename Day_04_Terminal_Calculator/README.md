# Day 04: Command-Line Terminal Calculator

## 📝 Overview
Day 04 focused on engineering an interactive terminal application. This project combines live stream user inputs via `input()`, string-to-float dynamic typecasting, infinite execution state loops, structural math conditions, and runtime evaluation safety (preventing mathematical zero-division system crashes).

---

## 🚀 Key Concepts Covered

### 1. Interactive Streams & Typecasting
* Utilizing `input()` to process runtime data parameters entered by the user.
* Converting string inputs into high-precision floating-point numbers (`float()`) to process accurate mathematical formulas.

### 2. Infinite State Control Loops
* Leveraging `while True` logic sequences to keep the application environment active and executing continuously until an explicit `break` keyword ("exit") is triggered.

### 3. Edge-Case Validation
* Nesting defensive conditional logic flags inside math blocks to capture and handle math errors (e.g., handling division parameters when a denominator equals `0`).

---

## 🛠️ Project Structure
* `app.py`: The application interface handling runtime evaluation logic, math operations, and input safety checkpoints.

## 💻 How to Run
```bash
python app.py