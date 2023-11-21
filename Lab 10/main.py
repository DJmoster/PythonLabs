import pandas as pd

from utils import replace_nulls, use_correction, build_bar_chart, build_date_line_chart

losses_data_frame = pd.read_csv('data/russia_losses_equipment.csv', sep=',')
correction_data_frame = pd.read_csv('data/russia_losses_equipment_correction.csv', sep=',')
personnel_data_frame = pd.read_csv('data/russia_losses_personnel.csv', sep=',')

# Видалення дублікатів по даті
losses_data_frame.drop_duplicates(subset=['date', 'day'], inplace=True)
correction_data_frame.drop_duplicates(subset=['date', 'day'], inplace=True)

# Заміна значень null у вибраних стовпцях на відповідні значення
replace_nulls(
    losses_data_frame,
    [
        ('military auto', 0.0),
        ('fuel tank', 0.0),
        ('special equipment', 0.0),
        ('mobile SRBM system', 0.0),
        ('greatest losses direction', ' '),
        ('vehicles and fuel tanks', 0.0),
        ('cruise missiles', 0.0),
        ('submarines', 0.0),
    ]
)

replace_nulls(
    correction_data_frame,
    [
        ('submarines', 0.0)
    ]
)

replace_nulls(
    personnel_data_frame,
    [
        ('POW', 0.0)
    ]
)

# Кореговані данні за допомогою correction_data_frame
corrected_data_frame = use_correction(losses_data_frame, correction_data_frame)

# Створення діаграми з середніми значеннями стовпців корегованих данних
corrected_mean = corrected_data_frame \
    .drop('day', axis='columns') \
    .mean(numeric_only=True)

build_bar_chart(
    'results/mean_diagram.png',
    'Середні значення стовпців',
    corrected_mean.keys().values,
    corrected_mean.values.tolist()
)

# Cтворення діаграми з останньою актуальною інформацією про втрати
actual_info = corrected_data_frame \
    .sort_values('day', ascending=False) \
    .drop(['date', 'day', 'greatest losses direction'], axis='columns') \
    .iloc[0]

build_bar_chart(
    'results/actual_diagram.png',
    'Актуальні дані',
    actual_info.keys().values,
    actual_info.values.tolist()
)

# Графік змінення кількості втраченої техніки
build_date_line_chart(
    'results/equipment_losses.png',
    corrected_data_frame,
    'Графік знищеної техніки'
)

# Графік змінення кількості втраченого особового складу
build_date_line_chart(
    'results/personnel_losses.png',
    personnel_data_frame,
    'Графік знищеного особового складу',
    ('day', 'date', 'personnel*', 'POW')
)

# losses_data_frame.to_csv('test.csv')
