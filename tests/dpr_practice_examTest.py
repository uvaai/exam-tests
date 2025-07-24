from checkpy import *
import pandas as pd
import typing
import pickle

only("dpr_practice_exam.py")

download("film.csv", "https://raw.githubusercontent.com/uvaai/exam-tests/main/data/film.csv")
download("dpr_practice_exam_outputs.pkl")

with open('dpr_practice_exam_outputs.pkl', 'wb'):
    outputs = pickle.load('dpr_practice_exam_outputs.pkl')

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
    df = getFunction("load_dataframe")("film.csv")

    assert isintance(df, pd.DataFrame), f"Expected return value to be a DataFrame, got {type(df)}"
    assert df.shape == (1128, 9), f"Expected 1128 rows, 9 columns, but got {df.shape}"

    expected_df = outputs[0]

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
    input_df = outputs[0]

    df = getFunction("add_demidecade_column")(input_df)

    assert isintance(df, pd.DataFrame), f"Expected return value to be a DataFrame, got {type(df)}"
    assert df.shape == (1128, 10), f"Expected 1128 rows, 10 columns, but got {df.shape}"

    expected_df = outputs[1]

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
    input_df = outputs[1]

    df = getFunction("average_duration_by_demidecade")(input_df)

    assert isintance(df, pd.Series), f"Expected return value to be a Series, got {type(df)}"

    expected_df = outputs[2]

    pd.testing.assert_frame_equal(df, expected_df, check_like=True)

######## Q4 ########

fun4_def = (declarative
    .function("longest_movies_demidecade")
    .params("duration_demidecade")
    .returnType(str)
)

test_4 = passed(test_average_duration_by_demidecade, hide=False)(fun4_def.call(outputs[2]).returns("The 5 year period with the longest movies on average was: 1960"))

######## Q5 ########

fun5_def = (declarative
    .function("count_movies_in_demidecade")
    .params("df", "demidecade")
    .returnType(str)
)

test5_1 = passed(test_add_demidecade_column, hide=False)(fun5_def.call(outputs[1], 1965).returns("The 5 year period from 1965 had 70 movies"))
test5_2 = passed(test_add_demidecade_column, hide=False)(fun5_def.call(outputs[1], 1980).returns("The 5 year period from 1980 had 128 movies"))

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
    input_df = outputs[1]

    df = getFunction("reformat_names")(input_df)

    assert isintance(df, pd.DataFrame), f"Expected return value to be a DataFrame, got {type(df)}"
    assert df.shape == (1128, 10), f"Expected 1128 rows, 10 columns, but got {df.shape}"

    expected_df = outputs[3]

    pd.testing.assert_frame_equal(df, expected_df, check_like=True)
