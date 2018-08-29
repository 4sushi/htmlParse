# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re


def table_to_list(html, encoding='utf-8'):
    """
    Transform a HTML table to a list of 2 dimensions
    Split values of colspan and rowspan
    Repair table (maybe not stable)
    Note : Untested with a lot of encoding
    :param html: html code
    :type html: str
    :param encoding: document encoding
    :rtype encoding: str
    :rtype: list[list[str]]
    """

    def __add_cell(table, i_line, i_col, val, nb_line, nb_col):
        while len(table) <= i_line:
            table.append([])
            nb_line += 1
        # Repair table
        while len(table[i_line]) < i_col:
            table[i_line].append('')
        table[i_line].insert(i_col, val)
        if len(table[i_line]) > nb_col:
            nb_col = len(table[i_line])
        return nb_line, nb_col

    def __get_cell_val(cell, encoding):
        text = cell.get_text(separator=' ')  # bs4
        if not isinstance(text, str):
            text = text.encode(encoding)
        if text is None or text == " ":
            text = ""
        return text

    soup = BeautifulSoup(html, 'html.parser')
    table = []
    nb_col = 0
    nb_line = 0
    # Transform BF object to list 2d with metadata (text, colspan, rowspan)
    tr_list = soup.find_all('tr')
    for i_tr, tr in enumerate(tr_list):
        table.append([])
        td_th_list = tr.find_all(re.compile(r'(td|th)'))
        for cell in td_th_list:
            # Calculate rowspan and colspan
            colspan_val = 1
            rowspan_val = 1
            if 'colspan' in cell.attrs:
                colspan_val = int(cell.attrs['colspan'])
            if 'rowspan' in cell.attrs:
                rowspan_val = int(cell.attrs['rowspan'])
            cell_info = {'colspan': colspan_val, 'rowspan': rowspan_val, 'text': __get_cell_val(cell, encoding)}
            table[-1].append(cell_info)
        if len(td_th_list) > nb_col:
            nb_col = len(td_th_list)
    nb_line = len(tr_list)
    del tr_list, soup

    i_col = 0
    # Transform list 2d with metadata to a list of string
    # Split rowspan and colspan
    while i_col < nb_col:
        i_line = 0
        while i_line < nb_line:
            # Repair table
            while i_col >= len(table[i_line]):
                table[i_line].append('')
            cell = table[i_line][i_col]
            if type(cell) is not dict:
                i_line += 1
                continue
            for i_colspan in range(i_col, i_col + cell['colspan']):
                for i_rowspan in range(i_line, i_line + cell['rowspan']):
                    if i_colspan == i_col and i_rowspan == i_line:
                        continue
                    nb_line, nb_col = __add_cell(table, i_rowspan, i_colspan, cell['text'], nb_line, nb_col)
            # Update cell value to string
            table[i_line][i_col] = cell['text']
            i_line += 1
        i_col += 1

    return table
