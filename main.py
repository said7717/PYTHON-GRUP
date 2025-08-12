def parol_tekshir(parol):
    if len(parol) < 8:
        return "Parol juda qisqa!"
    elif parol.isdigit():
        return "Parol faqat raqamlardan iborat bolishi mumkin emas!"
    elif parol.isalpha():
        return "Parol faqat harflardan iborat bolishi mumkin emas!"
    else:
        return "Parol qabul qilindi."

print(parol_tekshir("123456"))
print(parol_tekshir("abcdefg"))
print(parol_tekshir("abc12345"))
print(parol_tekshir("qwertyuiopoiuytdfghjkl;"))