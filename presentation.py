#!/usr/bin/python

import regex_tester as reg

def printe(num, text):
    print('------------------> %s\n\n%s' % (num, text))

def e1():
    example='''reg.match('test', 'test and tester and testing and Test')'''
    printe('1.1', example)
    exec(example)

    example='''reg.match('do', 'do and sudo and doofus and Doh!')'''
    printe('1.2', example)
    exec(example)

def e2():
    example='''reg.match('(?i)test', 'test and tester and testing and Test')'''
    printe('2.1', example)
    exec(example)

    example='''reg.match('(?i)do', 'do and sudo and doofus and Doh!')'''
    printe('2.2', example)
    exec(example)

def e3():
    print('''
Python:
    import re
    r = re.compile(pattern='test', flags=re.IGNORECASE)

PHP:
    // These two lines do the exact same thing.
    // Yes, you can choose your delimiters.
    $matched = preg_match('/test/i', 'TeStInG');
    $matched = preg_match('@test@i', 'TeStInG');

JavaScript:
    var regex = /test/i;
''')

def e4():
    print('''
Special chars must be escaped for literal match:

    $  (  )  *  +  .  ?  [  \  ^  {  |

(Note that the dash isn't in this list...)
''')

def e5():
    example='''reg.match('^mars$', 'mars')'''
    printe('5.1', example)
    exec(example)

    example='''reg.match('^mars$', 'marsupial')'''
    printe('5.2', example)
    exec(example)

    example='''reg.match('^mars', 'marsha, marsha, marsha!')'''
    printe('5.3', example)
    exec(example)

def e6():
    example='''reg.match('\Amartian\Z', 'martian')'''
    printe('6', example)
    exec(example)

def e7():
    example='''reg.match('^no$', 'no')'''
    printe('7.1', example)
    exec(example)

    example='''reg.match('^no?$', 'n')'''
    printe('7.2', example)
    exec(example)

    example='''reg.match('^no?$', 'no')'''
    printe('7.3', example)
    exec(example)

def e8():
    example='''reg.match('^no*', 'nooooooooooooo')'''
    printe('8.1', example)
    exec(example)

    example='''reg.match('^no*', 'n')'''
    printe('8.2', example)
    exec(example)

def e8b():
    example='''reg.match('a+', '123')'''
    printe('8b', example)
    exec(example)

def e8c():
    example='''reg.match('a*', '123')'''
    printe('8c', example)
    exec(example)

def e8d():
    example='''reg.vmatch('a*', '123')'''
    printe('8d', example)
    exec(example)

def e8e():
    example='''reg.replace('a*', '123', '__')'''
    printe('8e', example)
    exec(example)

def e9():
    example='''reg.match('^no+', 'nooo')'''
    printe('9.1', example)
    exec(example)

    example='''reg.match('^no+', 'n')'''
    printe('9.2', example)
    exec(example)

def e10():
    example='''reg.match('^no{10}', 'noooooooooo')'''
    printe('10.1', example)
    exec(example)

    example='''reg.match('^no{1000}', 'noooooooooooooooo')'''
    printe('10.2', example)
    exec(example)

def e11():
    example='''reg.match('^kahn{3,10}', 'kahn')'''
    printe('11.1', example)
    exec(example)

    example='''reg.match('^kahn{3,}', 'kahnnnnnnnnnnnnnnnnnnnnnnnn')'''
    printe('11.2', example)
    exec(example)

def e12():
    example='''reg.match('^no|yes$', 'yes')'''
    printe('12.1', example)
    exec(example)

    example='''reg.match('^no|yes$', 'no')'''
    printe('12.2', example)
    exec(example)

    example='''reg.match('^no|yes$', 'maybe')'''
    printe('12.3', example)
    exec(example)

def e13():
    example='''reg.match('jo|jon|joe', "say it ain't so, joe")'''
    printe('13.1', example)
    exec(example)

    example='''reg.match('joe|jon|jo', "say it ain't so, joe")'''
    printe('13.2', example)
    exec(example)

    example='''reg.match('joe|jon|jo', "say it ain't so, hwil hwheaton")'''
    printe('13.3', example)
    exec(example)

def e14():
    example='''reg.match('^952.555.1212$', '952-555_1212')'''
    printe('14.1', example)
    exec(example)

    phonenum='''952
555-1212'''

    example_p='''reg.match(
    '^952.555.1212$',
    '952-
    555-1212')'''
    example_x='''reg.match('^952.555.1212$', phonenum)'''
    printe('14.2', example_p)
    exec(example_x)

def e15():
    phonenum='''952
555-1212'''

    example_p='''reg.match(
    '(?s)^952.555.1212$',
    '952
    555-1212')'''
    example_x='''reg.match('(?s)^952.555.1212$', phonenum)'''
    printe('15', example_p)
    exec(example_x)

def e16():
    text='''wascally
wabbit'''

    example_p='''reg.match(
    '^wascally[\s\S]wabbit$',
    'wascally
    wabbit')'''
    example_x='''reg.match('^wascally[\s\S]wabbit$', text)'''
    printe('16', example_p)
    exec(example_x)

def e17():
    example='''reg.match('^\d\d\d.\d\d\d.\d\d\d\d$', '763-555-1234')'''
    printe('17', example)
    exec(example)

def e18():
    print('''
class   matches
-----   ------------------------------------------
\d      digit: 0-9
\s      whitespace character
\w      word character (digit, letter, underscore)
\D      non-digit
\W      non-word character
\S      non-whitespace character
''')

def e19():
    example='''reg.match('^\d\d\d\W\d\d\d\W\d\d\d\d$', '763-555-1234')'''
    printe('19.1', example)
    exec(example)

    example='''reg.match('^\d\d\d\W\d\d\d\W\d\d\d\d$', '763A555B1234')'''
    printe('19.2', example)
    exec(example)

    example='''reg.match('^\d\d\d\W\d\d\d\W\d\d\d\d$', '763_555_1234')'''
    printe('19.3', example)
    exec(example)

def e20():
    example='''reg.match('^\d\d\d[-._ ]\d\d\d[-._ ]\d\d\d\d$', '763_867_5309')'''
    printe('20.1', example)
    exec(example)

    example='''reg.match('^\d\d\d[-._ ]\d\d\d[-._ ]\d\d\d\d$', '763X867Y5309')'''
    printe('20.2', example)
    exec(example)

def e21():
    example='''reg.match('^[23456789]\d\d[-._][23456789]\d\d[-._]\d\d\d\d$', '763-867-5309')'''
    printe('21.1', example)
    exec(example)

    example='''reg.match('^[2-9]\d\d[-._][2-9]\d\d[-._]\d\d\d\d$', '952-867-5309')'''
    printe('21.2', example)
    exec(example)

    example='''reg.match('^[2-9]\d\d[-._][2-9]\d\d[-._]\d\d\d\d$', '763-155-1234')'''
    printe('21.3', example)
    exec(example)

def e22():
    print('''
range           contains
--------        ---------------------------------
[a-z]           lowercase letters "a" through "z"
[A-Z]           uppercase letters
[a-zA-Z]        all letters
[a-mA-M]        letters from "a" to "m"
[0-9]           numbers from 0 to 9
''')

def e23():
    example='''reg.match('^[2-9]\d\d[-._ ][2-9]\d\d[-._ ]\d{4}$', '763-555-1234')'''
    printe('23', example)
    exec(example)

def e24():
    print('''
custom [character class] notes:

- literal dash goes first or last (or needs to be escaped)

- only "\", "]", and "^" need to be escaped inside class (and "[" for Java)

- metacharacters like "." "?" "*" and "+" are not special in a class

- the caret (^) signals negation when it appears as the first character:

        [^2-9] matches any character other than 2 through 9
               (0, 1, letters, etc)
''')

def e25():
    example='''reg.match(r'\\b[nN]erd', "We're all nerds at The Nerdery")'''
    printe('25.1', example)
    exec(example)

    example='''reg.match(r'\\b[nN]erd', "We're all nerds at TheNerdery")'''
    printe('25.2', example)
    exec(example)

    example='''reg.match(r'\\B[nN]erd', "We're all nerds at TheNerdery")'''
    printe('25.3', example)
    exec(example)

def e26():
    example='''reg.match('(\d\d)/(\d\d)/(\d{4})', '04/22/1970')'''
    printe('26', example)
    exec(example)

def e27():
    example='''reg.vmatch('(\d\d)/(\d\d)/(\d{4})', '04/22/1970')'''
    printe('27', example)
    exec(example)

def e28():
    example='''reg.match('^My name is (Jan|Joe|Jon|Jo)$', 'My name is Jan')'''
    printe('28.1', example)
    exec(example)

    example='''reg.match('^My name is J(an|oe|on|o)$', 'My name is Joe')'''
    printe('28.2', example)
    exec(example)

    example='''reg.vmatch('^My name is J(an|oe|on|o)$', 'My name is Jo')'''
    printe('28.3', example)
    exec(example)

def e29():
    example='''reg.match('^My name is( really)? Ishmael$', 'My name is really Ishmael')'''
    printe('29.1', example)
    exec(example)

    example='''reg.match('^My name is( really)? Earl$', 'My name is Earl')'''
    printe('29.2', example)
    exec(example)

    example='''reg.match('^My name is( really){3,} Alice$', 'My name is really really Alice')'''
    printe('29.3', example)
    exec(example)

def e30():
    example='''reg.vreplace('(\w+) (\w+) (\w+)', 'order rearrange the', r'\\2 \\3 \\1')'''
    printe('30', example)
    exec(example)

def e30b():
    example='''reg.vreplace('(\w+) (\w+) (\w+)', 'order rearrange the this just like', r'\\2 \\3 \\1')'''
    printe('30b', example)
    exec(example)

def e31():
    example='''reg.vmatch('^My name is( really)? J(an|oe|on|o)$', 'My name is really Jan')'''
    printe('31.1', example)
    exec(example)

    example='''reg.vmatch('^My name is(?: really)? J(?:an|oe|on|o)$', 'My name is really Jan')'''
    printe('31.2', example)
    exec(example)

def e32():
    print('''
I feel really really happy!

I feel very very very very very happy!

I feel happy!
''')

def e33():
    example='''reg.match('^I feel( really| very)* happy!$', 'I feel really really happy!')'''
    printe('33.1', example)
    exec(example)

    example='''reg.match('^I feel( really| very)* happy!$', 'I feel really very really very happy!')'''
    printe('33.2', example)
    exec(example)

def e34():
    example='''reg.match(r'^I feel( really| very)\\1* happy!$', 'I feel really really happy!')'''
    printe('34.1', example)
    exec(example)

    example='''reg.match(r'^I feel( really| very)\\1* happy!$', 'I feel very very very happy!')'''
    printe('34.2', example)
    exec(example)

    example='''reg.match(r'^I feel( really| very)\\1* happy!$', 'I feel really very really very happy!')'''
    printe('34.3', example)
    exec(example)

def e35():
    example='''reg.match(r'^I feel((?: really| very)?)\\1* happy!$', 'I feel really really happy!')'''
    printe('35.1', example)
    exec(example)

    example='''reg.match(r'^I feel((?: really| very)?)\\1* happy!$', 'I feel happy!')'''
    printe('35.2', example)
    exec(example)

def e36():
    example='''reg.match('^happy$', "I'm not dead yet.")'''
    printe('36.1', example)
    exec(example)

    example='''reg.match('^happy$', "I don't want to go on the cart.")'''
    printe('36.2', example)
    exec(example)

def e37():
    print('''
^.*e --> "The quick brown fox jumped over the lazy dog."

match = ?
''')

def e38():
    example='''reg.match('^.*e', 'The quick brown fox jumped over the lazy dog.')'''
    printe('38', example)
    exec(example)

def e39():
    example='''reg.match('^.*?e', 'The quick brown fox jumped over the lazy dog.')'''
    printe('39', example)
    exec(example)

def e40():
    print('''
(x+x+)+y    -->    xxxxxxxxx

xxxxxxxxx   first pass with first x+
xxxxxxxx    backtrack one place
xxxxxxxxx   second x+ matches
xxxxxxxx    backtrack one looking for y
xxxxxxx     y? are you there?
xxxxxx      I thought I saw a "y" somewhere
xxxxx       *still* no y?
xxxx        y? come home: your family misses you
xxx         where the hell are you, y?!
xx          I'm not mad, just show yourself...
x           don't make me turn this car around...
(no match)  le sigh
''')

def e41():
    print('''
<html>.*?<head>.*?<title>.*?</title>.*?</head>.*?<body>.*?</body>.*?</html>
''')

def e42():
    print('''
<html>(?>.*?<head>)(?>.*?<title>)(?>.*?</title>)(?>.*?</head>)(?>.*?<body>)(?>.*?</body>).*?</html>
''')

def e43():
    print('''
(?x)           # verbose/comment mode
(.+?)          # lazy match capture
               #    start of filename into \1
(              # capture extension into \2
    \.[^.]*$   # last dot to end
   |           # or
    $          # forces \1 match to end if no dot
)              #
''')

def e44():
    print('''
(?x)
^(\d)(?!.*?\\1)
 (\d)(?!.*?\\2)
 (\d)(?!.*?\\3)
 (\d)(?!.*?\\4)
 (\d)(?!.*?\\5)
 (\d)(?!.*?\\6)
 (\d)(?!.*?\\7)
 (\d)(?!.*?\\8)
 (\d)(?!.*?\\9)
 \d$
''')

def e45():
    pattern='''(?x)
^(\d)(?!.*?\\1)
 (\d)(?!.*?\\2)
 (\d)(?!.*?\\3)
 (\d)(?!.*?\\4)
 (\d)(?!.*?\\5)
 (\d)(?!.*?\\6)
 (\d)(?!.*?\\7)
 (\d)(?!.*?\\8)
 (\d)(?!.*?\\9)
 \d$
'''
    example='''reg.match(pattern, '0978456231')'''
    printe('45.1', example)
    exec(example)

    example='''reg.match(pattern, '0978456241')'''
    printe('45.1', example)
    exec(example)

