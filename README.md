# 📚 Jadidlar Bot — O'rnatish Yo'riqnomasi

## Loyiha tuzilmasi
```
jadidlar_bot/
├── bot.py              ← Telegram bot (Python)
├── requirements.txt    ← Kutubxonalar
└── webapp/
    └── index.html      ← Telegram Mini App (veb sahifa)
```

---

## 1-QADAM: Bot yaratish

1. Telegramda @BotFather ga yozing
2. `/newbot` buyrug'ini yuboring
3. Bot nomini kiriting (masalan: `JadidlarBot`)
4. Username kiriting (masalan: `jadidlar_uz_bot`)
5. **TOKEN** olasiz — uni saqlang

---

## 2-QADAM: Web App ni joylashtirish (hosting)

### GitHub Pages orqali (BEPUL):
1. GitHub.com da yangi repo oching
2. `webapp/index.html` faylini yuklang
3. Settings → Pages → Branch: main → / (root) → Save
4. Sizga link beriladi: `https://yourusername.github.io/repo-name/`

### Netlify orqali (BEPUL, osonroq):
1. netlify.com ga kiring
2. `webapp` papkasini drag & drop qiling
3. Avtomatik link olasiz

---

## 3-QADAM: bot.py ni sozlash

`bot.py` faylida 2 qatorni o'zgartiring:

```python
BOT_TOKEN = "123456:ABC-DEF..."  # ← o'z tokeningiz
WEBAPP_URL = "https://yourusername.github.io/jadidlar/"  # ← o'z linkingi
```

---

## 4-QADAM: Python kutubxonalarini o'rnatish

```bash
pip install -r requirements.txt
```

---

## 5-QADAM: Botni ishga tushirish

```bash
python bot.py
```

---

## 6-QADAM: Matnlarni kiritish

`webapp/index.html` faylida quyidagi joylarni to'ldiring:

```javascript
{
  id: "behbudi",
  name: "Mahmudxo'ja Behbudiy",
  bio: `[BU YERGA AVTOBIOGRAFIYANI YOZING]`,
  hayot: `[BU YERGA HAYOTI VA IJODINI YOZING]`
},
```

Har bir jadid uchun `bio` va `hayot` maydonlarini to'ldiring.

---

## Ishlash tartibi

1. Foydalanuvchi botga `/start` bosadi
2. Bot "📚 Jadidlarni tanlash" tugmasini chiqaradi
3. Tugma bosilganda **alohida tabda** veb sahifa ochiladi
4. Jadid tanlanadi → Avtobiografiya yoki Hayoti va ijodi
5. Matn ko'rsatiladi
6. **"Eshitish"** tugmasi bosilganda matn ovoz bilan o'qiladi

---

## Muammolar

| Muammo | Yechim |
|--------|--------|
| Ovoz ishlamayapti | HTTPS kerak (HTTP da TTS ishlamaydi) |
| Bot start bermayapti | Tokenni tekshiring |
| Sahifa ochilmayapti | WEBAPP_URL ni tekshiring |
