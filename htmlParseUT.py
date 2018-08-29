# -*- coding: utf-8 -*-

import unittest
import htmlParse


class HtmlParseUT(unittest.TestCase):
    """
    Unit Test - HtmlParse
    """

    def test_get_list_1(self):
        """
        Simple case
        """
        html = """
        <table>
            <tr>
                <td>1</td>
                <td>2</td>
            </tr>
            <tr>
                <td>a</td>
                <td>b</td>
            </tr>
        </table>
        """
        list_2d = htmlParse.table_to_list(html)
        expected_list = [['1', '2'], ['a', 'b']]
        self.assertEqual(expected_list, list_2d)

    def test_get_list_2(self):
        """
        Colspan
        """
        html = """
        <table>
            <tr>
                <td colspan=2>1</td>
                <td>2</td>
            </tr>
            <tr>
                <td>a</td>
                <td>b</td>
                <td>c</td>
            </tr>
        </table>
        """
        list_2d = htmlParse.table_to_list(html)
        expected_list = [['1', '1', '2'], ['a', 'b', 'c']]
        self.assertEqual(expected_list, list_2d)

    def test_get_list_3(self):
        """
        Rowspan
        """
        html = """
        <table>
            <tr>
                <td rowspan=2>1</td>
                <td>2</td>
            </tr>
            <tr>
                <td>a</td>
            </tr>
        </table>
        """
        list_2d = htmlParse.table_to_list(html)
        expected_list = [['1', '2'], ['1', 'a']]
        self.assertEqual(expected_list, list_2d)

    def test_get_list_4(self):
        """
        Colspan + Rowspan
        """
        html = """
        <table>
            <tr>
                <td rowspan=2 colspan=2>1</td>
                <td>2</td>
            </tr>
            <tr>
                <td>a</td>
            </tr>
        </table>
        """
        list_2d = htmlParse.table_to_list(html)
        expected_list = [['1', '1', '2'], ['1', '1', 'a']]
        self.assertEqual(expected_list, list_2d)

    def test_get_list_5(self):
        """
        Colspan + Rowspan complex
        """
        html = """
        <table>
            <tr>
                <td>1</td>
                <td rowspan=3 colspan=2>2</td>
                <td rowspan=3 colspan=2>3</td>
                <td>4</td>
            </tr>
            <tr>
                <td rowspan=2>a</td>
                <td>b</td>
            </tr>
            <tr>
                <td>c</td>
            </tr>
        </table>
        """
        list_2d = htmlParse.table_to_list(html)
        expected_list = [['1', '2', '2', '3', '3', '4'], ['a', '2', '2', '3', '3', 'b'], ['a', '2', '2', '3', '3', 'c']]
        self.assertEqual(expected_list, list_2d)


if __name__ == '__main__':
    unittest.main()
