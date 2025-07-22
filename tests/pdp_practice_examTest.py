from checkpy import *
import typing

only("pdp_practice_exam.py")

download("barca.txt", "https://raw.githubusercontent.com/uvaai/exam-tests/main/data/barca.csv")
download("barca_short.txt", "https://raw.githubusercontent.com/uvaai/exam-tests/main/data/barca_short.csv")

######## Q1 ########

fun1_def = (declarative
    .function("compute_three_for_two_discount")
    .params("product_price", "number_of_items")
    .returnType(float)
)

test1_1 = test()(fun1_def.call(2.35, 3).returns(2.35))
test1_2 = test()(fun1_def.call(2.35, 6).returns(4.7))
test1_3 = test()(fun1_def.call(2.35, 7).returns(4.7))
test1_4 = test()(fun1_def.call(2.35, 0).returns(0.0))
test1_5 = test()(fun1_def.call(3.20, 17).returns(16.0))

######## Q2 ########

fun2_def = (declarative
    .function("find_short_words")
    .params("text", "max_length")
    .returnType(typing.List[str])
)
test2_1 = test()(fun2_def.call("The story is", 3).returns(['The', 'is']))
test2_2 = test()(fun2_def.call("Magnificent", 3).returns([]))
test2_3 = test()(fun2_def.call("Magnificent", 15).returns(['Magnificent']))
test2_4 = test()(fun2_def.call("The story so far in the beginning the universe was created This has made a lot of people very angry and been widely regarded as a bad move", 3).returns(['The', 'so', 'far', 'in', 'the', 'the', 'was', 'has', 'a', 'lot', 'of', 'and', 'as', 'a', 'bad']))

######## Q3 ########

fun3_def = (declarative
    .function("values_to_keys")
    .params("dictionary")
    .returnType(typing.Dict[str, typing.List[str]])
)

test3_1 = test()(fun3_def.call({'Tullamore': 'Ireland', 'Suntory': 'Japan'}).returns({'Ireland': ['Tullamore'], 'Japan': ['Suntory']}))
test3_2 = test()(fun3_def.call({'Johnny Walker': 'Scotland', 'Glenfiddich': 'Scotland'}).returns({'Scotland': ['Johnny Walker', 'Glenfiddich']}))
test3_3 = test()(fun3_def.call({'Hibiki': 'Japan', 'Bushmills': 'Ireland', 'anCnoc': 'Scotland', 'Teeling': 'Ireland', 'Starward': 'Australia', 'Four Roses': 'USA', 'Aberlour': 'Scotland', 'Nikka': 'Japan', 'Bulleit': 'USA', 'Tullibardine': 'Scotland'}).returns({'Japan': ['Hibiki', 'Nikka'], 'Ireland': ['Bushmills', 'Teeling'], 'Scotland': ['anCnoc', 'Aberlour', 'Tullibardine'], 'Australia': ['Starward'], 'USA': ['Four Roses', 'Bulleit']}))

######## Q4 ########

fun4_def = (declarative
    .function("shutouts")
    .params("filename")
    .returnType(int)
)

test4_1 = test()(fun4_def.call("barca_short.txt").returns(2))
test4_2 = test()(fun4_def.call("barca.txt").returns(40))
