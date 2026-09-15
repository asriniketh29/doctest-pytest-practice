'''
All the functions in this file convert markdown syntax into html.
Implementing these functions will give you practice learning the correct markdown syntax.
'''


def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".

    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    >>> compile_italic_underscore('_a_ and _b_')
    '<i>a</i> and <i>b</i>'
    >>> compile_italic_underscore('_a_ and _b')          # odd count: last one is literal
    '<i>a</i> and _b'
    >>> compile_italic_underscore('no underscores here')
    'no underscores here'
    >>> compile_italic_underscore('')
    ''
    '''

    while True:
        start = line.find("_")
        if start == -1:
            break
        end = line.find("_", start + 1)
        if end == -1:
            break

        # Replace only the matched _text_ pair
        content = line[start + 1:end]
        line = line[:start] + f"<i>{content}</i>" + line[end + 1:]

    return line


def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".

    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    >>> compile_bold_stars('**a** **b**')
    '<b>a</b> <b>b</b>'
    >>> compile_bold_stars('a * b * c')
    'a * b * c'
    >>> compile_bold_stars('***')
    '***'
 '''

    if line.count("**") < 2:
        return line

    parts = line.split("**")
    result = []

    for i, part in enumerate(parts):
        # Odd indexes represent the text inside matching ** pairs
        if i % 2 == 1 and i < len(parts) - 1:
            result.append(f"<b>{part}</b>")
        else:
            result.append(part)

    return "".join(result)
#    return line


def compile_links(line):
    '''
    Add <a> tags.

    HINT:
    The links and images are potentially more complicated because they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily find the start and stop locations using the strings find function.

    >>> compile_links('Click on the [course webpage](https://github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage](https://github.com/mikeizbicki/cmc-csci040)')
    '<a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)'
    >>> compile_links('this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040'
    >>> compile_links('[a](1) and [b](2)')
    '<a href="1">a</a> and <a href="2">b</a>'
    >>> compile_links('(parens) then [t](u)')
    '(parens) then <a href="u">t</a>'
    >>> compile_links('nothing here](oops)')
    'nothing here](oops)'
    '''

    while True:
        start_bracket = line.find("[")
        if start_bracket == -1:
            break

        end_bracket = line.find("]", start_bracket + 1)
        if end_bracket == -1:
            break

        # Ensure '(' immediately follows ']'
        if end_bracket + 1 >= len(line) or line[end_bracket + 1] != "(":
            # Skip invalid link structures (e.g., spaces between ] and ()
            line = line[:start_bracket] + \
                "TEMP_LBRACK" + line[start_bracket + 1:]
            continue

        end_paren = line.find(")", end_bracket + 2)
        if end_paren == -1:
            break

        text = line[start_bracket + 1:end_bracket]
        url = line[end_bracket + 2:end_paren]

        link_html = f'<a href="{url}">{text}</a>'
        line = line[:start_bracket] + link_html + line[end_paren + 1:]

    return line.replace("TEMP_LBRACK", "[")
