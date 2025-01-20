## Xush kelibsiz
## Dictionary

Uy vazifalarini va testlarni avtomatlashtirilgan tekshirish
- Ushbu repozitoriyani fork qiling
- Vazifalarni bajaring
- To‘g‘ri xabar bilan commit qiling

## Muammolar
### **count_jobs**

  Berilgan kasbga ega foydalanuvchilar sonini qaytaring.

**Misol 1:**

```Python
Input: 
data=[
  {
    'name': 'John', 
    'job': 'Developer'
  }, 
  {
    'name': 'Mary', 
    'job': 'Developer'
  }
  ]

job = 'Developer'
  
Output: 2

```
**Misol 2:**

```Python
Input: 
data = [
  {
    'name': 'John',
    'job': 'Barber'
  }, 
  {
    'name': 'Mary',
    'job': 'Developer'
  },
  {
    'name': 'Ann', 
    'job': 'Teacher'
  }
  ]
job = "Student"
Output: 0

```
**Cheklovlar:**
  - 0 <= len(data) <= 10^5
  - 0 <= len(job) <= 10^5

---

### **count_users_with_age**

  Berilgan yoshga ega foydalanuvchilar sonini qaytaring.

**Misol 1:**

```Python
Input: data = [
  {
    'name': 'John',
    'age': 27
  },
  {
    'name':'Mary', 
    'age': 42
  },
  {
    'name':'Ann',
    'age': 27
  }
  ]
age = 27
Output: 2
```
**Misol 2:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 35
  },
  {
    'name':'Mary', 
    'age': 20
  }
  ]
age = 38
Output: 0

```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5
  - 0 <= age <= 10^5

---

### **find_int_keys**

  Lug‘at ichidagi barcha butun son kalitlarini ro‘yxat sifatida qaytaring.

**Misol 1:**

```Python
Input: data = {
    'a': 1, 
    3 : 2, 
    'c': 3,
    10:'a'
  }
Output: [3, 10]

```
**Misol 2:**

```Python
Input: data = {
    "x": "23",
    "3": "y", 
    "z": "5", 
    7:'a'
  }
Output: [7]

```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5

---

### **find_length_of_values**

  Lug‘atdagi barcha qiymatlarning uzunliklari yig‘indisini qaytaring.

**Misol 1:**

```Python
Input: data = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }
Output: 9

```

**Misol 2:**

```Python
Input: data = {
    1 : "Khiva", 
    2 : "Namangan", 
    3 : "Samarkand", 
    4 : "Tashkent"
  }
Output: 30

```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5

---

### **find_max_key**

  Lug‘atdagi maksimal kalitni qaytaring.

**Misol 1:**

```Python
Input: data = {
    1: 'a', 
    2: 'b', 
    3: 'c'
  }
Output: 3

```
**Misol 2:**

```Python
Input: data = {
    1.4 :'a', 
    7.8 :'b', 
    4 : 'c'
  }
Output: 7.8

```
  - 0 <= len(data) <= 10^5

---

### **find_max_value**

  Lug‘atdagi maksimal qiymatni qaytaring.

**Misol 1:**

```Python
Input: data = {
    'a' : 1, 
    'b' : 2, 
    'c' : 3
  }
Output: 3

```
**Misol 2:**

```Python
Input: data  = {
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  }
Output: 0

```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5

---

### **get_max_age_user_name**

  Maksimal yoshga ega foydalanuvchi ismini qaytaring.

**Misol 1:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
Output: 'Mary'

```
**Misol 2:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  }, 
  {
    'name': 'Ban', 
    'age': 29
  }
]
Output: 'John'

```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5

---

