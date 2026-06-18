# Day 01: Dynamic Inventory & Text Analyzer

## 📝 Overview
On Day 01, I focused on rebuilding my foundational knowledge of Python, moving from basic data types to advanced string manipulation and dynamic memory structures. To lock in these core mechanics, I built a lightweight command-line utility that cleanses messy system strings and handles dynamic inventory tracking.

---

## 🚀 Key Concepts Covered

### 1. Variables & Types
* Declaring dynamic data types including Strings (`str`), Integers (`int`), Floats (`float`), and Booleans (`bool`).

### 2. Advanced String Manipulation
* **Modification:** Utilizing methods like `.strip()` to clean raw system inputs.
* **Slicing & Reversing:** Reversing text arrays efficiently using pythonic slicing indices: `[::-1]`.
* **Operations:** Combining strings using concatenation (`+`) and repetition (`*`).

### 3. Collections (Lists vs. Tuples)
* **Lists (Mutable):** Modifying indexes directly, removing items by value using `.remove()`, and popping elements dynamically using `.pop()`.
* **Tuples (Immutable):** Protecting system constants and metadata that must remain unchanged during runtime.

---

## 🛠️ Project Structure
* `app.py`: The core application containing text processing and inventory state management logic.

## 💻 How to Run
Ensure you have Python installed, then run the following command in your terminal:
```bash
python app.py