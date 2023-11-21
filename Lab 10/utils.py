import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


def replace_nulls(df: DataFrame, col_and_value: list[tuple[str, str | int | float]]):
    for i in col_and_value:
        df[i[0]].fillna(i[1], inplace=True)


def use_correction(input_df: DataFrame, correction_df: DataFrame, key='day', ignore=('day', 'date')) -> DataFrame:
    add_cols = [i for i in correction_df.keys() if i not in ignore]

    for i in correction_df[key]:
        input_df.loc[input_df[key] == i, add_cols] += \
            correction_df.loc[correction_df[key] == i, add_cols].values.tolist()[0]

    return input_df


def build_bar_chart(filename: str, title: str, names: list, counts: list):
    fig, ax = plt.subplots(figsize=(10, 10))
    bar_container = ax.bar(names, counts)

    ax.set(title=title)

    plt.xticks(rotation=30, ha='right')
    ax.bar_label(bar_container, fmt='{:,.0f}')

    plt.savefig(filename)


def build_date_line_chart(filename: str, df: DataFrame, title: str, ignore=('day', 'date', 'greatest losses direction')):
    df['date'] = pd.to_datetime(df['date'])
    columns = [i for i in df.keys() if i not in ignore]

    fig, ax = plt.subplots(figsize=(10, 10))

    ax.set_xlim(np.datetime64("2022-02-25"), np.datetime64("2023-11-05"))

    for column in columns:
        ax.plot(df['date'], df[column], label=column)

    ax.set(title=title)
    ax.grid(True)

    plt.legend()
    plt.xticks(rotation=30, ha='right')

    plt.savefig(filename)
