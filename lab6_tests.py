import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_book_selection_sort_1(self):
        input = [data.Book("Bill", "Sad"),
                 data.Book("John", "Happy")]
        expected = [data.Book("John", "Happy"),
                 data.Book("Bill", "Sad")]
        output = lab6.selection_sort_books(input)
        self.assertEqual(expected, output)
    def test_book_selection_sort_2(self):
        input = [data.Book("Apple", "Pie"),
                 data.Book("John", "Cena"),
                 data.Book("Henry", "Ford"),
                 data.Book("Killian", "Murphy")]
        expected = [data.Book("John", "Cena"),
                    data.Book("Henry", "Ford"),
                    data.Book("Killian", "Murphy"),
                    data.Book("Apple", "Pie")]
        output = lab6.selection_sort_books(input)
        self.assertEqual(expected, output)

    # Part 2
    def test_swap_case_1(self):
        input = "HELLO world"
        expected = "hello WORLD"
        output = lab6.swap_case(input)
        self.assertEqual(expected, output)

    def test_swap_case_2(self):
        input = "ÑFoVZ}4BSw"
        expected = "ñfOvz}4bsW"
        output = lab6.swap_case(input)
        self.assertEqual(expected, output)

    # Part 3
    def test_str_translate_1(self):
        input1 = "banana"
        input2 = "a"
        input3 = "4"
        expected = "b4n4n4"
        output = lab6.str_translate(input1,input2,input3)
        self.assertEqual(expected, output)
    def test_str_translate_2(self):
        input1 = "nkvdoqpdjk1gp"
        input2 = "d"
        input3 = "D"
        expected = "nkvDoqpDjk1gp"
        output = lab6.str_translate(input1,input2,input3)
        self.assertEqual(expected, output)

    # Part 4
    def test_histogram1(self):
        input = "kfdajf qkajedpfaj  dkaf"
        expected = {"k":3,"f":4,"d":3,"a":4,"j":3,"q":1,"e":1,"p":1}
        output = lab6.histogram_letters(input)
        self.assertEqual(expected,output)





if __name__ == '__main__':
    unittest.main()
