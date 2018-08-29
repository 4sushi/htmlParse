# HtmlParse

## Description

Simple library to parse HTML file. Only one method, to convert html table to a python list of 2 dimensions (exemple : `[[1,2,3],[1,2,3]]`).

## Python version

Python 2

## Examples 1

The HTML table :

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

```python
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
print(list_2d)
```

Output: 
```
['1', '2'], ['a', 'b']
```

## Examples 2

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

```python
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
print(list_2d)
```

Output:

```
[['1', '2', '2', '3', '3', '4'], ['a', '2', '2', '3', '3', 'b'], ['a', '2', '2', '3', '3', 'c']]
```