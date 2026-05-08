

## 🚀 EduPlatform - Online Education & Career Portal Backend

**EduPlatform** — bu o'quv markazlari, o'qituvchilar va talabalar uchun mo'ljallangan keng qamrovli LMS (Learning Management System) hamda karyera platformasi. Loyiha nafaqat ta'lim olish, balki vakansiyalar orqali ish topish va o'zaro real-vaqt rejimida muloqot qilish imkoniyatini beradi.

### 🛠 Texnologiyalar:

* **Backend:** Python 3.x, Django Framework.
* **Asinxron Aloqa:** Django Channels, WebSockets (Real-time chat uchun).
* **Ma'lumotlar Bazasi:** PostgreSQL (Production), SQLite (Development).
* **Real-time & Caching:** Redis (Channels layer uchun).
* **API Dokumentatsiya:** Swagger / Redoc.
* **Muhit:** Linux (Ubuntu).

---

### ✨ Asosiy Imkoniyatlar (Features):

#### 1. 💬 Mukammal Chat Tizimi (Real-time)

Telegram arxitekturasiga yaqinlashtirilgan asinxron chat tizimi:

* **Multimodal Xabarlar:** Matn, rasm, video, audio va turli hujjatlarni (.pdf, .doc) yuborish imkoniyati.
* **Contextual Chat:** Har bir suhbat aniq bir kurs yoki vakansiyaga bog'langan holda boshlanadi.
* **Media Management:** Fayllar hajmi va original nomini saqlagan holda tartib bilan saqlanadi.
* **Read Receipts:** Xabarlarning o'qilganlik holatini (is_read) kuzatish.

#### 2. 🎓 Kurslar va Ta'lim

* Kurslarni boshqarish (CRUD).
* Talabalarning kurslarga arizalar yuborish tizimi.

#### 3. 💼 Vakansiyalar Markazi (SkillSwap)

* Ish beruvchilar uchun vakansiyalar yaratish.
* Nomzodlar va ish beruvchilar o'rtasida to'g'ridan-to'g'ri chat orqali muloqot.

---

### 📂 Proyekt Strukturasi:

```text
ZenTask/
├── core/               # Loyiha sozlamalari
├── conversation/       # Chat, xabar va fayllar bilan ishlash app'i
├── event/              # Kurslar va ta'lim jarayoni app'i
├── vacancies/          # Ish va vakansiyalar boshqaruvi app'i
├── static/             # Statik fayllar
└── media/              # Foydalanuvchilar yuklagan video/rasmlar

```

---

### ⚙️ O'rnatish va Ishga tushirish:

1. **Repozitoriyani klonlash:**
```bash
git clone https://github.com/username/ZenTask.git
cd ZenTask

```


2. **Virtual muhitni sozlash:**

```bash
    python -m venv venv
    source venv/bin/activate  # Linux uchun
    ```

3.  **Kutubxonalarni o'rnatish:**
    
```bash
    pip install -r requirements.txt
    ```

4.  **Migratsiyalarni amalga oshirish:**
    
```bash
    python manage.py migrate
    ```

5.  **Serverni ishga tushirish:**
    ```bash
    python manage.py runserver
    ```

---

### 📝 API Endpoints (Chat qismi):
*   `POST /api/v1/chat/messages/` - Xabar va media fayl yuborish (`multipart/form-data`).
*   `GET /api/v1/chat/rooms/` - Foydalanuvchi suhbatlari ro'yxati.
*   `GET /api/v1/chat/rooms/{id}/messages/` - Xona ichidagi barcha xabarlar tarixi.

---

### 👨‍💻 Muallif:
**Akobir Marupov**
*   Python Backend Developer
*   LinkedIn: [Sizning LinkedIn Havolangiz]

---

### 📄 Litsenziya:
Ushbu loyiha MIT litsenziyasi ostida yaratilgan.

---

### Maslahat:
README faylini GitHub'ga yuklaganingizdan so'ng, yuqorida keltirilgan bo'limlarni loyihangizning real holatiga qarab biroz boyitishingiz mumkin. Masalan, Swagger dokumentatsiyasidan screenshotlar qo'shsangiz, yanada professional ko'rinadi!

```