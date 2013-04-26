# Regex Presentation Outline

## Demonstration: A Totally Useful Real World Application

The "rename" Perl script.

Say we've just downloaded some MP3 files from an album by TNSH:

    1 You've Probably Never Heard Of It.mp3
    10 One More Song.mp3
    2 I Wish My Typewriter Had Helvetica.mp3
    3 Too Meta For You To Understand.mp3
    4 PBR On My Desert Boots.mp3
    5 Haircuts Are For Losers.mp3
    6 Organic Mouth Wash Blues.mp3
    7 Way Ironic, Don't You Think.mp3
    8 Niche Song.mp3
    9 Unnamed Song.mp3

There are two problems with these filenames. One, the numbers aren't zero-padded, causing the 10th song to be listed out of order, and two, we like to have the artist's name in the filename.

For this, I'd use "rename," which seems to come fairly standard on Linux distributions, and can be easily dropped on a Mac. Let's try:

    rename 's/^([0-9] )(.*)/0$1$2/' * -n

(We'll cover all of these squiggles in the presentation.)

`-n` let's us preview the rename. If all looks well, we can run it for real to get our filenames in order:

    01 You've Probably Never Heard Of It.mp3
    02 I Wish My Typewriter Had Helvetica.mp3
    [...]
    09 Unnamed Song.mp3
    10 One More Song.mp3

And then we'll run another rename command to add the band name, along with some ornamentation for the track numbers:

    rename 's/^(..) (.*)/TNSH -$1- $2/' *

Giving us:

    TNSH -01- You've Probably Never Heard Of It.mp3
    TNSH -02- I Wish My Typewriter Had Helvetica.mp3
    TNSH -03- Too Meta For You To Understand.mp3
    TNSH -04- PBR On My Desert Boots.mp3
    TNSH -05- Haircuts Are For Losers.mp3
    TNSH -06- Organic Mouth Wash Blues.mp3
    TNSH -07- Way Ironic, Don't You Think.mp3
    TNSH -08- Niche Song.mp3
    TNSH -09- Unnamed Song.mp3
    TNSH -10- One More Song.mp3

Wasn't that fun? Doesn't it make you super excited to learn more about regular expressions?

## The Basics

### Literal Text Matching

    presentation.py: e1()

        1.1
        reg.match('test', 'test and tester and testing and Test')
        
        1.2
        reg.match('do', 'do and sudo and doofus and Doh!')

Literal text matching works exactly as you might expect.

`test` will match "test" "tester" and "retesting".  However, by default it won't match "Test" unless you set the case-insensitivity flag.  How you set this flag varies from language to language.

    presentation.py: e2()

        2.1
        reg.match('(?i)test', 'test and tester and testing and Test')

        2.2
        reg.match('(?i)do', 'do and sudo and doofus and Doh!')

In some languages, it is required that you wrap your regular expressions in delimiters.  For example, in JavaScript, you can create a Regex literal by writing `var /test/;`.  The slashes are not part of your regular expression, they're just what you have to place at the beginning and end.  As you might expect, this means that you have to escape any slashes that appear in your regular expression with a backslash (`\`).

Not many languages support regular expression literals.  In most languages, you have to pass your regex to a function inside a string.  Depending on your language, it may or may not be required that you wrap your regex in delimiters inside the string.  However, in those languages that have you do so, you can often choose your own delimiters.

As an example, here is how our case-insensitive regex would look in Python, PHP, and JavaScript.

_presentation.py:_ __e3()__

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

_presentation.py:_ __e4()__

There are other characters that must be escaped with a backslash if you want to literally match them. They are `$`, `(`, `)`, `*`, `+`, `.`, `?`, `[`, `\`, `^`, `{`, and `|`.  Remember that your language might require you to double escape your backslashes, which can make things even harder to read.

The value of being able to pick your own delimiters is that you can choose a character that doesn't appear in the string, so you won't have to escape it.  For example, when matching URLs in PHP, I'll often use `@`, or for matching an email address `#`.  Which delimiters you can use vary, so check your docs for details.

### Matching the beginning or end of the string

    presentation.py: e5()

        5.1
        reg.match('^mars$', 'mars')

        5.2
        reg.match('^mars$', 'marsupial')

        5.3
        reg.match('^mars', 'marsha, marsha, marsha!')
            
What happens if you don't want to match a string like "testing", "retest" but just a string that only contains "test"?  To accomplish this, you can use `^` to match the beginning and `$` to match the end of the string. So, our pattern would become `^test$`.  Of course, you don't have to use these together. You can just write `^test` to match strings like `testing`.

You should also be aware that in some environments, `^` and `$` might not just mean match at the beginning and end of a string, but also at the beginning or end of a line.  Most regular expression engines require you to turn this feature on, but in Ruby and many text editors, it's on by default, and you can't turn it off.  If you want to turn this feature on, it's often called multiline mode.  In Ruby or most text editors, you can use `\A` and `\Z` instead of `^` and `$` to match just the beginning and end of a string.

    presentation.py: e6()
        
        reg.match('\Amartian\Z', 'martian')

Finally, it's important to note that `^` and `$` are non-consuming anchors. We'll learn more about this in a bit, but basically this just means that they don't actually match any characters, they just match a position.

### Regex Basics: ? * +

    presentation.py: e7()
        
        7.1
        reg.match('^no$', 'no')

        7.2
        reg.match('^no?$', 'n')

        7.3
        reg.match('^no?$', 'no')

Let's say you want to match some user input. You want to find out if the user entered "no".  `^no$` should do that nicely.  But what if you also wanted to allow the user to just enter  "n", with no `o`?  For that, you can use the `?` modifier.  The `?` means match the previous item zero or one times.  So, if our pattern becomes `^no?$`, it can match "n" or "no".  In other words, this means match n at the beginning of the string, then match an o if there's one there, otherwise, don't.

    presentation.py: e8()
    
        8.1
        reg.match('^no*', 'nooooooooooooo')

        8.2
        reg.match('^no*', 'n')

What if we wanted to accept "n", "no", or even "noooooooooo"?  For this, we can use the `*` modifier.  `*` means match the preceding item zero or more times.  `^no*$` should do what we want in this case.

    presentation.py: e8b()
    
        reg.match('a+', '123')
        
        not a match

Be careful with expressions that become "too optional." If you try to match `a+` against "123", you won't get a match. But what if we try to match `a*` against the same string?

    presentation.py: e8c()
    
        reg.match('a*', '123')

We have a match! But it's invisible. Running "vmatch" shows us several matches:

    presentation.py: e8d()
    
        reg.vmatch('a*', '123')
        
        1) start: 0, end: 0, match: 
        2) start: 1, end: 1, match: 
        3) start: 2, end: 2, match: 
        4) start: 3, end: 3, match: 
        
        123

These are zero-width matches. `a*` means zero or more stars, and when the engine can't find any matches on a, it will happily accept zero length strings. It might be clearer if we make some replacements:

    presentation.py: e8e()
    
        reg.replace('a*', '123', '__')
        
        __1__2__3__

See? The engine found four places where zero characters matches.

    presentation.py: e9()
    
        9.1
        reg.match('^no+', 'nooo')

        9.2
        reg.match('^no+', 'n')

What if we don't want to match "n" alone, but instead, we want to match "n" followed by one or more "o"s?  For that the `+` will do what we need.  `+` means match the preceding item one or more times. `^no+$` does the trick.

    presentation.py: e10()
    
        10.1
        reg.match('^no{10}', 'noooooooooo')

        10.2
        reg.match('^no{1000}', 'noooooooooooooooo')

Finally, since we've long since passed the boundary of contrivance, let's say we want to match "noooooooooo", with exactly ten "o"s.  We could of course do `^noooooooooo$`, but this solution quickly becomes impractical as the number of desired o's increases.  To match the previous item exactly N times, we use braces, `{N}`, where n is an integer >= 0.  So, the better solution to matching "noooooooooo" with exactly 10 "o"s is `^no{10}$`.

    presentation.py: e11()
    
        11.1
        reg.match('^kahn{3,10}', 'kahn')

        11.2
        reg.match('^kahn{3,}', 'kahnnnnnnnnnnnnnnnnnnnnnnnn')

This modifier has a bit more flexibility than that, however.  If you want to match "no" having between three and ten o's, you can write `^no{3,10}$`.  If you want to match three to infinity o's, you can simply do `^no{3,}$`.

### Alternation

    presentation.py: e12()
    
        12.1
        reg.match('^no|yes$', 'yes')

        12.2
        reg.match('^no|yes$', 'no')

        12.3
        reg.match('^no|yes$', 'maybe')

What if you wanted to match either "no" or "yes"?  You can do so by simply writing `^no|yes$`.  The `|` basically means "or".  If the first option doesn't match, it tries the second, and so on.

Keep in mind that regular expressions are evaluated from left to right, so the first match is tried first, then the second, and so on.  Once a match is found, no more matches are attempted.

    presentation.py: e13()
    
        13.1
        reg.match('jo|jon|joe', "say it ain't so, joe")

        13.2
        reg.match('joe|jon|jo', "say it ain't so, joe")

        13.3
        reg.match('joe|jon|jo', "say it ain't so, hwil hwheaton")

So, what if you want to match a string that contains either "jon", "joe", or "jo"?  The regular expression `jo|jon|joe` would match, but not necessarily always what you want.  Since the first alternative to match is always used, this would cause this pattern to always match "jo", even for "jon" or "joe".  The proper way to write this would be `joe|jon|jo`

Something else to keep in mind is that, for efficiency,  if you know that a particular alternative will occur far more frequently than another, you might want to list the more frequent alternative first.

### Matching Any Character

Let's say we wanted to match a string that only contained a particular phone number, 952-555-1212. It may or may not have dash delimiters, or it might be written with underscores or periods instead of dashes.  One not very good way to solve this problem would be to use the following regex:

    ^952.555.1212$
    
    presentation.py: e14()
    
        14.1
        reg.match('^952.555.1212$', '952-555_1212')
        
        14.2
        reg.match(
            '^952.555.1212$',
            '952-
            555-1212'
        )

The `.` character matches any character, with one caveat.  It does not match newline characters, unless you turn on the "single line" mode in your regular expression engine.  (Java calls this the "dot all" mode.)

    presentation.py: e15()
    
        reg.match(
            '(?s)^952.555.1212$',
            '952
            555-1212'
        )

If setting this mode is not possible (for example, if you're using JavaScript), one hack to accomplish the same thing is to write something like `[\s\S]`.  We'll discuss what this pattern actually says in the next section.

    presentation.py: e16()
    
        reg.match(
            '^wascally[\s\S]wabbit$',
            'wascally
            wabbit'
        )

However, for our purposes, we don't want the `.` to match newlines.  In fact, it will match a lot of characters that we don't want it to.  This is why I only use `.` when nothing else will do.  Usually, something else does.

### Character Classes

So, as you undoubtedly noticed, our phone number example isn't very good.  first, it only matches one particular phone number, and second, it would match "952Q55561212", and several other invalid strings.  Fortunately character classes give us the chance to fix these issues.

    presentation.py: e17()
    
        reg.match('^\d\d\d.\d\d\d.\d\d\d\d$', '763-555-1234')

First, let's make our pattern match any digits, not just the ones we specified.  To do this, we can use the following regular expression:

    ^\d\d\d.\d\d\d.\d\d\d\d$

As you may have guessed, `\d` matches one digit character, 0 through 9.

    presentation.py: e18()

Other character class shortcuts that are available are `\s` to match any whitespace character, and `\w` to match any word character.  (A word character is defined as any digit, any letter, and the underscore.  See the docs for your particular regex engine for the definition of a letter, as some match any letter from the whole of Unicode, and others only consider the latin alphabet defined in ASCII.)

        e18()
        class   matches
        -----   ------------------------------------------
        \d      digit: 0-9
        \s      whitespace character
        \w      word character (digit, letter, underscore)
        \D      non-digit
        \W      non-word character
        \S      non-whitespace character

Capitalized versions of these shortcuts are also available, and they match the exact opposite of their lower-case counterparts.  `\D` matches any non-digit character, `\W` matches any non-word character, and `\S` matches any non-whitespace character.

    presentation.py: e19()
    
        19.1
        reg.match('^\d\d\d\W\d\d\d\W\d\d\d\d$', '763-555-1234')

        19.2
        reg.match('^\d\d\d\W\d\d\d\W\d\d\d\d$', '763A555B1234')

        19.3
        reg.match('^\d\d\d\W\d\d\d\W\d\d\d\d$', '763_555_1234')

So, with this knowledge, we can improve our regular expression a bit:

    ^\d\d\d\W\d\d\d\W\d\d\d\d$

This is still not perfect.  First, we're assuming that this is a US phone number, and US phone numbers can't have their area codes or prefixes start with a 1 or a 0.  Second, while we did make sure that we don't match any letters or  digits between the parts of the phone number, there are still a lot of characters that we don't want to be used.  We also prevented the underscore from being used, which seems like a reasonable character to allow.

    presentation.py: e20()
    
        20.1
        reg.match('^\d\d\d[-._ ]\d\d\d[-._ ]\d\d\d\d$', '763_867_5309')

        20.2
        reg.match('^\d\d\d[-._ ]\d\d\d[-._ ]\d\d\d\d$', '763X867Y5309')

What we need is a custom character class, where we can specify a list of characters that are permissible.  This is how we do that:

    ^\d\d\d[-._ ]\d\d\d[-._ ]\d\d\d\d$

Custom character classes are delimited by square brackets, and have their own set of metacharacters which we'll discuss more in a moment.

Now we will only match phone numbers that have their parts delimited by either a space, "-", "_" or a ".".  We now just need to solve the issue with the first digits of the prefix and area code not being 1.

    presentation.py: e21()
    
        21.1
        reg.match('^[23456789]\d\d[-._][23456789]\d\d[-._]\d\d\d\d$', '763-867-5309')
        
        21.2
        reg.match('^[2-9]\d\d[-._][2-9]\d\d[-._]\d\d\d\d$', '952-867-5309')

        21.3
        reg.match('^[2-9]\d\d[-._][2-9]\d\d[-._]\d\d\d\d$', '763-155-1234')

The obvious solution is:

    ^[23456789]\d\d[-._][23456789]\d\d[-._]\d\d\d\d$

But fortunately, there is a more concise way to write this:

    ^[2-9]\d\d[-._][2-9]\d\d[-._]\d\d\d\d$

    presentation.py: e22()
    
Writing something like `[a-z]` means match the lowercase letters a through z. The dash is a "range specifier."  You can also include multiple ranges in a single character class like `[a-zA-Z]`, which means match any letter, regardless of capitalization,.  The ordering is based on the character code values.

    e22()
    range           contains
    --------        ---------------------------------
    [a-z]           lowercase letters "a" through "z"
    [A-Z]           uppercase letters
    [a-zA-Z]        all letters
    [a-mA-M]        letters from "a" to "m"
    [0-9]           numbers from 0 to 9

    presentation.py: e23()
    
        reg.match('^[2-9]\d\d[-._ ][2-9]\d\d[-._ ]\d{4}$', '763-555-1234')

While we're making things more concise, let's shorten up this regular expression a bit more by using the braces we learned about earlier.

    ^[2-9]\d\d[-._ ][2-9]\d\d[-._ ]\d{4}$

    presentation.py: e24()
    
        custom [character class] notes:

        - literal dash goes first or last (or needs to be escaped)
    
        - only "\", "]", and "^" need to be escaped inside class (and "[" for Java)
    
        - metacharacters like "." "?" "*" and "+" are not special in a class
    
        - the caret (^) signals negation when it appears as the first character:
    
                [^2-9] matches any character other than 2 through 9
                       (0, 1, letters, etc)

If you want to use a literal dash character inside your character class, like we did above, you have to make sure that it is placed at either the beginning or the end of the class, so it can't be confused for a range specifier.  Alternatively, you can escape it with a `\`.

Also, only the "\", "]" and "^" characters need to be escaped if you wish them to have their literal meanings.  (If you're using Java, you'll also need to escape "[" as well.)  All of the other characters that have special meaning outside a character class, like the `.` character, have only their literal meanings inside a character class.

Finally, just like you can take the negatives of the word, digit and whitespace character classes, you can place a `^` at the beginning of a character class to do the same.  For example, `[^2-9]` will match any character that isn't in the range 2 through 9, inclusive.

### Word Boundaries

Writing `\b` in your regular expression will cause the regex engine to try to match a word boundary at that point.  Like the `^` and `$`, it does not actually match any text, just a position.

    presentation.py: e25()
    
        25.1
        reg.match(r'\\b[nN]erd', "We're all nerds at The Nerdery")

        25.2
        reg.match(r'\\b[nN]erd', "We're all nerds at TheNerdery")

        25.3
        reg.match(r'\\B[nN]erd', "We're all nerds at TheNerdery")

A word boundary is a position that has a word character on one side, and either a non-word character or the beginning or the end of the string on the other.

    \b[nN]erd

This would match the strings "nerd" or "Nerdery", but not "TheNerdery".

`\B` will match on a non-word boundary, or in other words, everywhere where `\b` won't match.

## Grouping and Capturing

### Capturing Groups

    presentation.py: e26()
    
        reg.match('(\d\d)/(\d\d)/(\d{4})', '04/22/1970')

Consider the case where you want to match a date, and pull out just the month, day, and year parts.  This is quite simple with capturing groups:

    (\d\d)/(\d\d)/(\d{4})

    presentation.py: e27()
    
        reg.vmatch('(\d\d)/(\d\d)/(\d{4})', '04/22/1970')
        
            1) start: 0, end: 10, match: 04/22/1970
               groups: ('04', '22', '1970')

Using the API for your regular expression engine, you should then be able to pull the characters matched from within the first set of parenthesis out of the first matching group, the second from the second, and the third from the third group.

### Grouping

Even if you don't care to access what was matched inside a set of parentheses, groups can still be quite useful.

Recall the earlier regular expression where we wanted to match Jo, Joe or Jon.  To keep things interesting, let's add "Jan" to that list.

    presentation.py: e28()
    
        28.1
        reg.match('^My name is (Jan|Joe|Jon|Jo)$', 'My name is Jan')

        28.2
        reg.match('^My name is J(an|oe|on|o)$', 'My name is Joe')

        28.3
        reg.vmatch('^My name is J(an|oe|on|o)$', 'My name is Jo')
        
            1) start: 0, end: 13, match: My name is Jo
               groups: ('o',)
        
Now, what happens if we want to extend that to match "My name is Jan", or "My name is Joe", etc.  The not very smart way to do that would be to write it all out, using alternation between each possible match.  Fortunately, if we use alternation inside a group, it will only consider the possible matches inside that group.  This means that we can write:

    ^My name is (Jan|Joe|Jon|Jo)$
    
Or minimally more efficient with less readability:

    ^My name is J(an|oe|on|o)$

    presentation.py: e29()
    
        29.1
        reg.match('^My name is( really)? Ishmael$', 
                  'My name is really Ishmael')

        29.2
        reg.match('^My name is( really)? Earl$',
                  'My name is Earl')

        29.3
        reg.match('^My name is( really){3,} Alice$',
                  'My name is really really Alice')

In addition, you can apply modifiers to groups.  So, if you wanted to optionally match the word "really" after the is, you could write:

    ^My name is( really)? Ishmael$

Of course, other modifiers work as well, so you can write:

    ^My name is( really){3,} Alice$

This would of course require that "really" appear three or more times in that position in order to match the string.

Capturing groups are numbered from left to right, based on the position of their left parenthesis.  Non-capturing groups, and other parenthesized groups, such as look-around expressions don't effect the count.

    presentation.py: e30()
    
        reg.vreplace('(\w+) (\w+) (\w+)',
                     'order rearrange the', r'\2 \3 \1')
                     
            1) start: 0, end: 19, match: order rearrange the
               groups: ('order', 'rearrange', 'the')
               
            rearrange the order


The numbered groups can be used in regex replacements, where they are usually referred to with a backslash or dollar sign before the number, for example, in Python:

    re.sub('(\w+) (\w+) (\w+)', r'\2 \3 \1', 'order rearrange the')

Produces the result:

    rearrange the order

    presentation.py: e30b()
    
        reg.vreplace('(\w+) (\w+) (\w+)',
                     'order rearrange the this just like',
                     r'\2 \3 \1')
                     
            1) start: 0, end: 19, match: order rearrange the
               groups: ('order', 'rearrange', 'the')
            2) start: 20, end: 34, match: this just like
               groups: ('this', 'just', 'like')
            
            rearrange the order just like this

These are "backreferences," which we'll cover more in a moment.

### Non-Capturing Groups

    presentation.py: e31()
    
        31.1
        reg.vmatch('^My name is( really)? J(an|oe|on|o)$', 'My name is really Jan')

            1) start: 0, end: 21, match: My name is really Jan
               groups: (' really', 'an')
   
        31.2
        reg.vmatch('^My name is(?: really)? J(?:an|oe|on|o)$', 'My name is really Jan')
        
            1) start: 0, end: 21, match: My name is really Jan

Since we likely have no interest in actually capturing the "really" from the previous examples, it seems a bit wasteful for the regular expression engine to save it just in case we want it.  Fortunately, we can tell the engine that we won't need any of the groups by placing a `?:` just after the opening parenthesis:

    ^My name is(?: really)? J(?:an|oe|on|o)$

The increased efficiency may not balance out the decrease in readability, but non-capturing groups are especially helpful when we want to deal with the results of some captures but not others.

### Named Capturing Groups

Many regular expression engines (with the notable exception of JavaScript) offer the option to name your capturing groups, which has the potential to make things more readable.  Unfortunately, the syntax for doing this differs from engine to engine, so if this is something you're interested in, I recommend checking your documentation to find out if it's supported, and if so, how to use it.

### Backreferences

_presentation.py:_ __e32()__

How would you match strings like the following:

* I feel really really happy!
* I feel very very very very very happy!
* I feel happy!

In other words, you want to allow zero or more "really"s or "very"s, but you don't want to match something like "very really very very". You might start with:

    ^I feel( really| very)* happy!$
    
    presentation.py: e33()
    
        33.1
        reg.match('^I feel( really| very)* happy!$',
                  'I feel really really happy!')

        33.2
        reg.match('^I feel( really| very)* happy!$',
                  'I feel really very really very happy!')
    
This satisfies the first requirement, but not the second.  What we need is a way to match something again.  This is where backreferences come in.  To keep things simple, let's first look at how you would match this pattern if at least one "really" or "very" is required:

    ^I feel( really| very)\1* happy!$
    
    presentation.py: e34()
    
        reg.match(r'^I feel( really| very)\1* happy!$', 
                   'I feel really really happy!')

        reg.match(r'^I feel( really| very)\1* happy!$',
                   'I feel very very very happy!')

        reg.match(r'^I feel( really| very)\1* happy!$',
                   'I feel really very really very happy!')

The interesting part of this pattern is obvious: `( really| very)\1*`.  This can be broken down into two parts.  The first is `( really| very)` which is a capturing group, which either captures " really" or " very".  The next part `\1*` is a backreference to the first part.  It tells the regex engine to match the what we captured in the first part, zero or more times.

Just to be clear, let's walk through this as the regex engine would.  First the engine matches "I feel".  Next the " really" or " very" is hopefully matched.  If not, the engine declares failure.  If so, " really" or " very" is stored in the first matching group.  To keep the example simple, let's assume that " very" was matched and stored in the first group.

The regex engine next tries to match another " very", because that is what is stored in the first capturing group.  If it can't, it simply continues trying to match the rest of the pattern, since we used the `*` modifier, which means zero or more times.  If it does match another " very", it tries yet again to match " very", until it can't match anymore, at which point it continues trying to match the rest of the string.

Recall that in our initial specification for this problem, we said we wanted to match a series of "really"s or a series of "very"s, or nothing at all in that position.  The modification to make this happen is quite simple.

    ^I feel((?: really| very)?)\1* happy!$
    
    presentation.py: e35()

        reg.match(r'^I feel((?: really| very)?)\\1* happy!$',
                   'I feel really really happy!')

        reg.match(r'^I feel((?: really| very)?)\\1* happy!$',
                   'I feel happy!')

Now, after matching the "I feel" portion, it tries to match either really or very.  If it does, it still stores them in the first group, like before.  If it doesn't, the first group is empty.  Either way, like before, it then tries to match whatever is stored in the back-reference.  If the back reference is empty, it won't fail, because it simply won't match anything.

Finally, notice that we used non-capturing parenthesis inside our capturing group, to make it unambiguous that we want to capture something, even if it's nothing.

Even more finally:

    presentation.py: e36()
    
        reg.match('^happy$', "I'm not dead yet.")

        reg.match('^happy$', "I don't want to go on the cart.")

## Greed and Backtracking

### The Non-Greedy Modifier

    presentation.py: e37()
    
        ^.*e --> "The quick brown fox jumped over the lazy dog."

        match = ?

What would you expect the following regular expression to match when run against the string "The quick brown fox jumped over the lazy dog."

    ^.*e

Would you be surprised to learn that it will match "The quick brown fox jumped over the"?

    presentation.py: e38()
    
        reg.match('^.*e', 'The quick brown fox jumped over the lazy dog.')

To understand why this is, let's walk through how the regular expression engine runs the above expression.

First, the `^` matches at the beginning of the string.  Then, the `.*` means match any character, as many times as possible.  So, the regex engine happily does this, consuming everything until the end of the string.

But then, the engine reaches the `e`, which it obviously can't match, because it consumed the whole string.  So, the engine forces the `.*` to give up one of the characters it consumed, which would be a "." in our example.  It then tries to match this against the `e`, which it clearly can't do.  So, it repeats the process until the e matches.

So, in short, the reason the `e` matches the last "e" in the string is because the .* is greedy, and consumes as much as it can, and only gives up characters when it has to.

If you want to make the `*`, `+` or `?` operators lazy, simply append a `?`.  Here's what the previous regex would look like made non-greedy:

    ^.*?e
    
    presentation.py: e39()
    
        reg.match('^.*?e', 'The quick brown fox jumped over the lazy dog.')

This will match only the first "the".

In this case, the the `*` is lazy, so it first tries to match nothing.  However, when the engine can't match the `e`, it forces the `*` to consume one more character.  It keeps doing this, until the `e` matches, at which point it declares victory, and returns.

Finally, note that the lazy modifier also works on ranges.

### Preventing Backtracking

As you might have noticed, regular expression engines are pretty dumb.  Of course by dumb, I mean terrible at reading minds.  So, sometimes they need a little help figuring out what to do.  Consider the following intentionally terrible regular expression, taken from _The Regular Expression Cookbook_:

    (x+x+)+y
    
    presentation.py: e40()

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

Consider what would happen if you tried to use this to match the string "xxxxxxxxx".  On the first iteration, the first `x+` would match all the "x"s in the string, leaving none for the second `x+`.  So, some backtracking would occur to give the second `x+` an "x".  Then the engine would leave the group, and try to match the `y`.  When this failed, the engine would backtrack, and force the group to give up one more x, which would kick off several more iterations of backtracking inside the capturing group, and so on back to the beginning of the string.

_presentation.py:_ __e41()__

Let's consider another, more realistic though slightly simplified example, from the same book:

    <html>.*?<head>.*?<title>.*?</title>.*?</head>.*?<body>.*?</body>.*?</html>

First off, it's important to note that regular expressions are not very good at parsing HTML, and should only be used in limited circumstances when doing so.

As for this example, (which I don't recommend you use for a number of reasons) consider what happens when the `</html>` tag doesn't exist in the string.  Each non-greedy modifier gets back-tracked to in turn, causing this regular expression to have a worst-case running time of N^7, where N is the length of the string.

_presentation.py:_ __e42()__

The solution is (once again, from the same book):

    <html>(?>.*?<head>)(?>.*?<title>)(?>.*?</title>)(?>.*?</head>)(?>.*?<body>)(?>.*?</body>).*?</html>

The `(?>` tells the regex engine that once that particular group has matched something, it should forget about any possible backtracking in that group.

Also, some regex flavors allow you to apply possession to modifiers.  For example, `x++` would match all the "x"s it could, and never give any back.

Unfortunately, neither of these features are available in Perl or Python.

## Verbose Mode

This varies by regex engine, but you can use "verbose mode" to comment your regular expressions and spread them out. There are special rules for handling whitespace in this mode.

    presentation.py: e43()

        (?x)           # verbose/comment mode
        (.+?)          # lazy match capture
                       #    start of filename into \1
        (              # capture extension into \2
            \.[^.]*$   # last dot to end
           |           # or
            $          # forces \1 match to end if no dot
        )              #

## Recommended Reading

* _Mastering Regular Expressions_, by Jeffrey Friedl

* _Regular Expressions Cookbook_, by Jan Goyvaerts and Steven Levithan
