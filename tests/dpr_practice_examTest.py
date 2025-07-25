from checkpy import *
import pandas as pd
import typing
import pickle

only("dpr_practice_exam.py")

download("film.csv", "https://raw.githubusercontent.com/uvaai/exam-tests/main/data/film.csv")
download("dpr_practice_exam_outputs.pkl", "https://raw.githubusercontent.com/uvaai/exam-tests/main/outputs/dpr_practice_exam_outputs.pkl")

######## OOP ########

# ?????  https://github.com/minprog/checks/blob/2025/tests/dictsTest.py

######## Pandas ########

with open('dpr_practice_exam_outputs.pkl', 'rb') as f:
    outputs = pickle.load(f)

######## Q1 ########
fun1_def = (declarative
    .function("load_dataframe")
    .params("filename")
    .returnType(pd.DataFrame)
)

test_1 = test()(fun1_def)

@passed(test_1)
def test_load_dataframe():
    """load_dataframe correctly loads the data"""
    expected_df = outputs['load_dataframe_df']

    df = getFunction("load_dataframe")("film.csv")

    assert isinstance(df, pd.DataFrame), f"Expected return value to be a DataFrame, got {type(df)}"
    assert df.shape == expected_df.shape, f"Expected {expected_df.shape[0]} rows, {expected_df.shape[1]} columns, but got {df.shape}"

    pd.testing.assert_frame_equal(df, expected_df, check_like=True)


######## Q2 ########

fun2_def = (declarative
    .function("add_demidecade_column")
    .params("df")
    .returnType(pd.DataFrame)
)

test_2 = passed(test_load_dataframe, hide=False)(fun2_def)

@passed(test_2, hide=False)
def test_add_demidecade_column():
    """add_demidecade_column correctly calculates demidecades and adds a column"""
    input_df = outputs['load_dataframe_df']
    expected_df = outputs['add_demidecade_column_df']

    df = getFunction("add_demidecade_column")(input_df)

    assert isinstance(df, pd.DataFrame), f"Expected return value to be a DataFrame, got {type(df)}"
    assert df.shape == expected_df.shape, f"Expected {expected_df.shape[0]} rows, {expected_df.shape[1]} columns, but got {df.shape}"

    pd.testing.assert_frame_equal(df, expected_df, check_like=True)

######## Q3 ########

fun3_def = (declarative
    .function("average_duration_by_demidecade")
    .params("df")
    .returnType(pd.Series)
)

test_3 = passed(test_add_demidecade_column, hide=False)(fun3_def)

@passed(test_3, hide=False)
def test_average_duration_by_demidecade():
    """average_duration_by_demidecade correctly calculates averages"""
    input_df = outputs['add_demidecade_column_df']
    expected_s = outputs['duration_demidecade_series']

    s = getFunction("average_duration_by_demidecade")(input_df)

    assert isinstance(s, pd.Series), f"Expected return value to be a Series, got {type(s)}"

    pd.testing.assert_series_equal(s, expected_s, check_like=True)

######## Q4 ########

fun4_def = (declarative
    .function("longest_movies_demidecade")
    .params("duration_demidecade")
    .returnType(str)
    .description("longest_movies_demidecade() is correctly defined and works as expected")
)

test_4 = passed(test_average_duration_by_demidecade, hide=False)(fun4_def.call(outputs['duration_demidecade_series']).returns("The 5 year period with the longest movies on average was: 1960"))

######## Q5 ########

fun5_def = (declarative
    .function("count_movies_in_demidecade")
    .params("df", "demidecade")
    .returnType(str)
    .description("count_movies_in_demidecade() is correctly defined and works as expected")
)

test5_1 = passed(test_add_demidecade_column, hide=False)(fun5_def.call(outputs['add_demidecade_column_df'], 1965).returns("The 5 year period from 1965 had 70 movies"))
test5_2 = passed(test_add_demidecade_column, hide=False)(fun5_def.call(outputs['add_demidecade_column_df'], 1980).returns("The 5 year period from 1980 had 128 movies"))

######## Q6 ########

fun6_def = (declarative
    .function("reformat_names")
    .params("df")
    .returnType(pd.DataFrame)
)

test_6 = passed(test_add_demidecade_column, hide=False)(fun6_def)

@passed(test_6, hide=False)
def test_reformat_names():
    """reformat_names correctly calculates demidecades and adds a column"""
    input_df = outputs['add_demidecade_column_df']
    expected_df = outputs['reformat_names_df']

    df = getFunction("reformat_names")(input_df)

    assert isinstance(df, pd.DataFrame), f"Expected return value to be a DataFrame, got {type(df)}"
    assert df.shape == (1128, 10), f"Expected 1128 rows, 10 columns, but got {df.shape}"

    pd.testing.assert_frame_equal(df, expected_df, check_like=True)


######## Built-ins ########

######## Q1 ########


venue_seats = {'Tivoli': [('VIP', 'A1'), ('VIP', 'A2'), ('General', 'B1'), ('General', 'B2'), ('General', 'B3'), ('General', 'B4')],
            'Ahoy': [('VIP', 'A1'), ('VIP', 'A2'), ('VIP', 'A3'), ('General', 'B1'), ('General', 'B2'), ('General', 'C1'), ('General', 'C2'), ('General', 'D1'), ('General', 'D2')],
            'Ziggo Dome': [('General', 'A1'), ('General', 'B1'), ('General', 'C1'), ('General', 'D1')]}

concerts = [('Backstreet Boys', 'Ahoy', '11-02-2024'),
            ('Backstreet Boys', 'Tivoli', '12-02-2024'),
            ('Backstreet Boys', 'Ziggo Dome', '13-02-2024'),
            ('Golden Earring', 'Ahoy', '18-02-2024'),
            ('Greenday', 'Ziggo Dome', '18-02-2024')]

concert_database = {('Ahoy', 'Backstreet Boys', '11-02-2024'): [],
  ('Tivoli', 'Backstreet Boys', '12-02-2024'): [],
  ('Ziggo Dome', 'Backstreet Boys', '13-02-2024'): [],
  ('Ahoy', 'Golden Earring', '18-02-2024'): [],
  ('Ziggo Dome', 'Greenday', '18-02-2024'): []
}

fun1_def_bi = (declarative
    .function("initialize_concert_database")
    .params("concerts")
    .returnType(dict)
    .description("initialize_concert_database() is correctly defined and works as expected")
)

test_1_bi = test()(fun1_def_bi.call(concerts).returns(concert_database))

######## Q2 ########

fun2_def_bi = (declarative
    .function("populate_concert_database")
    .params("concert_database", "venue_seats")
    .returnType(dict)
    .description("populate_concert_database() is correctly defined and works as expected")
)

expected_database = {('Ahoy', 'Backstreet Boys', '11-02-2024'): [(None, 'VIP', 'A1'), (None, 'VIP', 'A2'), (None, 'VIP', 'A3'), (None, 'General', 'B1'), (None, 'General', 'B2'), (None, 'General', 'C1'), (None, 'General', 'C2'), (None, 'General', 'D1'), (None, 'General', 'D2')],
                     ('Tivoli', 'Backstreet Boys', '12-02-2024'): [(None, 'VIP', 'A1'), (None, 'VIP', 'A2'), (None, 'General', 'B1'), (None, 'General', 'B2'), (None, 'General', 'B3'), (None, 'General', 'B4')],
                     ('Ziggo Dome', 'Backstreet Boys', '13-02-2024'): [(None, 'General', 'A1'), (None, 'General', 'B1'), (None, 'General', 'C1'), (None, 'General', 'D1')],
                     ('Ahoy', 'Golden Earring', '18-02-2024'): [(None, 'VIP', 'A1'), (None, 'VIP', 'A2'), (None, 'VIP', 'A3'), (None, 'General', 'B1'), (None, 'General', 'B2'), (None, 'General', 'C1'), (None, 'General', 'C2'), (None, 'General', 'D1'), (None, 'General', 'D2')],
                     ('Ziggo Dome', 'Greenday', '18-02-2024'): [(None, 'General', 'A1'), (None, 'General', 'B1'), (None, 'General', 'C1'), (None, 'General', 'D1')]}

test_2_bi = test()(fun2_def_bi.call(concert_database, venue_seats).returns(expected_database))

# ######## Q3 ########

fun3_def_bi = (declarative
    .function("sell_ticket")
    .params("concert_database", "concert", "seat_number", "name")
    .returnType(None)
    .description("sell_ticket() is correctly defined and works as expected")
)

concert = ('Ahoy', 'Backstreet Boys', '11-02-2024')
seat_number = 'A3'
name = 'Jan Janssen'

test_3_bi = passed(test_2_bi, hide=False)(fun3_def_bi.call(concert_database, concert, seat_number, name))

seat_number = 'C1'
name = 'Bart Bakker'

test_3_2_bi = passed(test_2_bi, hide=False)(fun3_def_bi.call(concert_database, concert, seat_number, name))

# ######## Q4 ########

fun4_def_bi = (declarative
    .function("get_available_tickets")
    .params("concert_database", "concert")
    .returnType(list)
    .description("get_available_tickets() is correctly defined and works as expected")
)

concert = ('Ahoy', 'Backstreet Boys', '11-02-2024')
expected_available_tickets = [(None, 'VIP', 'A1'), (None, 'VIP', 'A2'), (None, 'General', 'B1'), (None, 'General', 'B2'), (None, 'General', 'C2'), (None, 'General', 'D1'), (None, 'General', 'D2')]

test_4_bi = passed(test_2_bi, hide=False)(fun4_def_bi.call(concert_database, concert).returns(expected_available_tickets))
