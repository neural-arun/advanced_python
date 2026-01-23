
# 🔁 ASYNCHRONOUS PROGRAMMING — KEY TERMS REVISION (MASTER)

---

## 1️⃣ Synchronous (Sync)

**Meaning:**

> Kaam **ek ke baad ek**, wait karke.

**Real life:**

* Phone call → jab tak baat khatam nahi, kuch aur nahi

**Programming:**

* Ek task khatam → tab next task

---

## 2️⃣ Asynchronous (Async)

**Meaning:**

> Wait karte hue **dusra kaam karna**.

**Real life:**

* Text bheja → kaam karta raha → reply aaya

**Important:**

* Async ≠ faster CPU
* Async = better time usage

---

## 3️⃣ Blocking

**Meaning:**

> Code **ruk jaata hai**, sab kuch ruk jaata hai.

**Example:**

```python
time.sleep(2)
```

**Effect:**

* Program freeze
* Event loop kuch nahi kar sakta

---

## 4️⃣ Non-Blocking

**Meaning:**

> Sirf current kaam rukta hai, **program nahi**.

**Example:**

```python
await asyncio.sleep(2)
```

**Effect:**

* Dusre tasks chalte rehte hain

---

## 5️⃣ Concurrency

**Meaning:**

> Ek hi time pe **multiple kaamon ka management**.

**Reality:**

* Single CPU core
* Fast switching

**Async = Concurrency**

---

## 6️⃣ Parallelism

**Meaning:**

> Sach mein ek saath kaam chalna.

**Reality:**

* Multiple CPU cores / GPU
* ML training, image processing

---

## 7️⃣ I/O Bound Work

**Meaning:**

> Jahan **wait zyada**, kaam kam.

**Examples:**

* Website request
* API call
* Database query

**Best tool:**
👉 **Async**

---

## 8️⃣ CPU Bound Work

**Meaning:**

> Jahan **calculation heavy** hoti hai.

**Examples:**

* Big loops
* ML training
* Image processing

**Best tool:**
👉 Multiprocessing / GPU
❌ Async useless here

---

## 9️⃣ `async def` (Async Function)

**Meaning:**

> Aisa function jo **pause/resume** ho sakta hai.

```python
async def work():
    ...
```

**Important truth:**

* Ye function **run nahi hota**
* Ye **coroutine** banata hai

---

## 🔟 Coroutine

**Meaning (most important):**

> Ek **paused function** jo baad mein resume ho sakta hai.

**Normal function:**

```
start → end
```

**Coroutine:**

```
start → pause → resume → pause → end
```

---

## 1️⃣1️⃣ `await`

**Meaning (LOCK THIS 🔒):**

> “Main yahan rukta hoon, event loop dusra kaam kar le.”

**Rules:**

* Sirf `async def` ke andar
* Sirf async cheezon ke saath

❌ Wrong:

```python
await time.sleep(1)
```

✅ Correct:

```python
await asyncio.sleep(1)
```

---

## 1️⃣2️⃣ Event Loop

**Meaning (simple):**

> **Manager** jo decide karta hai:

* kaunsa task chale
* kaunsa ruke
* kaunsa resume ho

**Important facts:**

* Single thread
* Single core
* Control sirf `await` pe milta hai

---

## 1️⃣3️⃣ Starvation

**Meaning:**

> Event loop ko **control hi nahi milta**.

**Cause:**

* Infinite loop
* Blocking code
* No `await`

---

## 1️⃣4️⃣ `await outside function` Error

**Meaning:**

> Python bol raha hai:
> “`await` sirf async function ke andar allowed hai”

**Fix:**
Hamesha ek `main()` async function banao.

---

## 1️⃣5️⃣ `asyncio.run()`

**Meaning:**

> Event loop **start** karne ka button.

```python
asyncio.run(main())
```

Iske bina:

* Async code chalega hi nahi

---

# 🧠 FINAL ONE-SCREEN SUMMARY (MOST IMPORTANT)

```
async def  → coroutine banta hai
await      → pause karta hai
event loop → manage karta hai
asyncio.run → system start karta hai
```

---

