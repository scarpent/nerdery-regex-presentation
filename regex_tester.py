import re

red = '\033[0;31m'
cyan = '\033[0;36m'
no_color = '\033[0m'

def replace(pattern, string, replace='__'):
    regextester(pattern, string, replace)

def vreplace(pattern, string, replace='__'):
    regextester(pattern, string, replace, show_matches=True)

def match(pattern, string):
    regextester(pattern, string)

def vmatch(pattern, string):
    regextester(pattern, string, show_matches=True)

def regextester(pattern, string, replace=None, show_matches=False):

    r = re.compile(pattern)
    m = r.search(string)

    if m:

        i = 0
        idx = 0
        color = cyan
        newstring = ''

        while m:
            m_start = m.start()
            m_end = m.end()
            m_match = string[m_start:m_end]

            if show_matches:
                if i == 0:
                    print
                i += 1
                print(
                    '%d) start: %d, end: %d, match: %s' %
                    (i, m_start, m_end, m_match)
                )
                # capturing groups
                if m.groups():
                    print('   groups: ' + str(m.groups()))

            # build output string
            if replace:
                replace_with = re.sub(pattern, replace, m_match)
            else:
                replace_with = m_match

            newstring += string[idx:m.start()] + color + replace_with + no_color

            if color == red:
                color = cyan
            else:
                color = red

            idx = m_end

            if m_end == len(string): # infinite loop if
                break                #    m_start == m_end == len(string)
            elif m_start == m_end:   # zero-width match;
                m_end += 1           #    keep things moving along

            m = r.search(string, m_end)

        newstring += string[m_end:]
        print('\n%s\n' % newstring)

    else:
        print('\nnot a match\n')
