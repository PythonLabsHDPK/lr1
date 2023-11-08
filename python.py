# Функція для розрахунку довжини стрипільної ноги та кількості стрипільних ніг
def calculate_roof_legs(width, length):
    katet1 = width / 2
    gipoten = katet1 / 0.574 + 30
    count_of = (length / 100 + 1) * 2
    return gipoten, count_of

# Функція для розрахунку кількості досок обрешітки
def calculate_roof_planks(gipoten, length):
    planks_amount = (round(gipoten / 30 + 1)) * 2
    planks_amount450 = 0
    digit = 0
    if length > 600:
        digit = length // 600
        if length - 600 * digit > 450:
            digit += 1
        else:
            planks_amount450 = planks_amount
        planks_amount *= digit
    return planks_amount, planks_amount450

# Функція для розрахунку площі криші та кількості шиферин
def calculate_roof_area_and_sheets(gipoten, length):
    rf_size = gipoten * length
    amount_b_sh = length / 100
    amount_b_sh = round(amount_b_sh, 0)
    amount_a_sh = gipoten // 150
    dov_zal = gipoten - amount_a_sh * 150
    if dov_zal > 75:
        amount_a_sh = amount_a_sh + 1
    else:
        amount_a_sh = amount_a_sh + 0.5
    sh_amount = amount_a_sh * amount_b_sh * 2
    sh_amount = round(sh_amount, 0)
    return rf_size, sh_amount


a = float(input("Введіть ширину: "))
b = float(input("Введіть довжину: "))

gipoten, count_of = calculate_roof_legs(a, b)
planks_amount, planks_amount450 = calculate_roof_planks(gipoten, b)
rf_size, sh_amount = calculate_roof_area_and_sheets(gipoten, b)

print("Довжина стрипільної ноги: ", gipoten)
print("Кількість стрипільних ніг: ", count_of)
print("Кількість досок обре шітки600: ", planks_amount)
print("Кількість досок обрешітки450: ", planks_amount450)
print("Площа однієї сторони криші: ", rf_size)
print("Кількість шиферин: ", round(sh_amount, 0))
