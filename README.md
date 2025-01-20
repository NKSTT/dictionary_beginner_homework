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

## get_min_age_user_name

  Lug'atdagi eng kichik yoshga ega foydalanuvchining ismini qaytaradi.

**Misol 1:**

```Python
Kirish: data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
Chiqish: 'John'
```
**Misol 2:**

```Python
Kirish: data = [
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
Chiqish: 'Mary'
```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5

## get_user_country

  Berilgan ismga ega foydalanuvchining mamlakatini qaytaradi.

**Misol 1:**

```Python
Kirish: data = [
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  }
]
name = "John"
Chiqish: 'USA'
```
**Misol 2:**

```Python
Kirish: data = [
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  },
  {
    'name': 'Henry', 
    'country': 'UK'
  },
  {
    'name': 'Sam', 
    'country': 'MEX'
  },
  {
    'name': 'Kevin', 
    'country': 'RUS'
  },
  {
    'name': 'Dustin', 
    'country': 'GER'
  }
]
name = "Henry"
Chiqish: 'UK'
```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5
  - 0 <= len(name) <= 10^5

## get_user_names_with_age_range

  Berilgan yosh oralig'idagi foydalanuvchilar ro'yxatini qaytaradi.

**Misol 1:**

```Python
Kirish: data = [
  {
    'name': 'John', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }
]
min_age = 18
max_age = 25
Chiqish: ['John','Ban']
```
**Misol 2:**

```Python
Kirish: data = [
  {
    'name': 'Anny', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 30
  }
]
min_age = 20
max_age = 30
Chiqish: ['Anny','Mary']
```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5
  - 0 <= max_age <= 10^5
  - 0 <= min_age <= 10^5

## get_user_names_with_age

  Berilgan yoshga ega foydalanuvchilar ro'yxatini qaytaradi.

**Misol 1:**

```Python
Kirish: data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
age = 27
```Chiqish: ['John']

**Misol 2:**

```Python
Kirish: data = [
  {
    'name': 'John', 
    'age': 30
  }, 
  {
    'name': 'Ann', 
    'age': 32
  }, 
  {
    'name': 'Sam', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 32
  }
]
age = 32
Chiqish: ['Ann','Mary']
```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5
  - 0 <= age <= 10^5

## get_user_names

  Berilgan mamlakatga ega foydalanuvchilar ro'yxatini qaytaradi.

**Misol 1:**

```Python
Kirish: data = [
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  }
]
country = "USA"
Chiqish: ["John"]
```
**Misol 2:**

```Python
Kirish: data = [
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  },
  {
    'name': 'Henry', 
    'country': 'UK'
  },
  {
    'name': 'Sam', 
    'country': 'MEX'
  },
  {
    'name': 'Kevin', 
    'country': 'RUS'
  },
  {
    'name': 'Dustin', 
    'country': 'GER'
  }
]
country = 'UK'
Chiqish: ["Mary","Henry"]
```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5
  - 0 <= len(country) <= 10^5

## sum_age_values

  Lug'atdagi barcha yosh qiymatlarini yig'indisini qaytaradi.

**Misol 1:**

```Python
Kirish: data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
Chiqish: 69
```
**Misol 2:**

```Python
Kirish: data = [
  {
    'name': 'John', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }
]
Chiqish: 87
```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5

## sum_dict_values

  Lug'atdagi barcha qiymatlarning yig'indisini qaytaradi.

**Misol 1:**

```Python
Kirish: data = {
    'a': 1, 
    'b': 2, 
    'c': 3
  }
Chiqish: 6

**Misol 2:**

Python
Kirish: data = {
    1: 23, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3
  }
Chiqish: 39.5
```
**Cheklovlar:**

  - 0 <= len(data) <= 10^5

## sum_even_values

  Lug'atdagi barcha juft qiymatlarning yig'indisini qaytaradi.
  
**Misol 1:**

```Python
Kirish: data = {
    'a': 1, 
    'b': 2, 
    'c': 3
  }
Chiqish: 2
```
**Misol 2:**

```Python
Kirish: data = {
    1: 22, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3
  }
Chiqish: 24
```

**Cheklovlar:**

  - 0 <= len(data) <= 10^5

## sum_float_values

  Lug'atdagi barcha float qiymatlarning yig'indisini qaytaradi.

**Misol 1:**

```Python
Kirish: data = {
    'a': 1, 
    'b' : 2.5, 
    'c': 3.0
  }
Chiqish: 5.5
```
**Misol 2:**

```Python
Kirish: data = {
    1: 22.4, 
    2: 3.5, 
    4: 1, 
    6: 7.6, 
    5: 2, 
    7: 3
  }
Chiqish: 33.5
```

**Cheklovlar:**

  - 0 <= len(data) <= 10^5
    
# Warning
- don't copy other solutions or any solution
- don't remove comments
only translete o'zbek 

