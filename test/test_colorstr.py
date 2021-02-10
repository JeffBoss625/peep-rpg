from lib.constants import COLOR
import re

class FormatStr:
    def __init__(self, parts):
        self.parts = parts

    def __len__(self):
        return sum(len(p.s) for p in self.parts)

    def __getitem__(self, slc):
        slen = len(self)
        if isinstance(slc, int):
            if slc < 0:
                slc = slice(slen-slc, slen-slc + 1)
            else:
                slc = slice(slc, slc+1)

        else:
            if slc.start is None:
                slc.start = 0
            if slc.stop is None:
                slc.stop = slen

            if slice.step != 1:
                raise ValueError('only single step slice is handled')

        beg_idx, beg_off = skip_chars(self.parts, slc.start)
        parts = format_substr(self.parts, beg_idx, beg_off, slc.stop - slc.start)
        return FormatStr(parts)

    def __repr__(self):
        return ''.join(str(p) for p in self.parts)


# Skip up to n characters in the array of StrPart objects, returning the
# new index and char offset. Return (-1, -r) if less than n chars were available
# where r is the number left over (not skipped).
def skip_chars(parts, n):
    rem = n
    i = 0
    while rem > 0:
        # skip up to n characters
        p = parts[i]
        if rem < len(p.s):
            return i, rem

        rem -= len(p.s)
        i += 1

    if rem > 0:
        return -1, -rem

    return i, 0

# Return a new array of StrPart objects made up of up to n characters starting from
# parts[beg_idx][beg_off]
def format_substr(parts, beg_idx, beg_off, n):
    rem = n
    ret = []
    off = beg_off
    i = beg_idx
    while rem > 0:
        # skip up to n characters
        p = parts[i]
        avail = len(p.s) - off
        if rem < avail:
            ret.append(StrPart(p.code, p.arg, p.s[off, off + rem + 1]))
            break

        if off == 0:
            ret.append(p)
        else:
            ret.append(StrPart(p.code, p.arg, p.s[off, len(p.s) + 1]))

        off = 0
        rem -= avail
        i += 1

    return ret

class StrPart:
    def __init__(self, code, arg, s):
        self.code = code
        self.arg = arg
        self.s = s

    def __repr__(self):
        if self.code == '':
            return self.s
        return '<' + self.code + '(' + self.arg + ')' + self.s + '>'


def parse(s):
    parts = re.split(r'<(.*)\((.*)\):(.*)>', s)
    ret = []
    plain = parts.pop(0)
    if len(plain):
        ret.append(StrPart('', '', plain))

    while len(parts):
        ret.append(
            StrPart(parts.pop(0), parts.pop(0), parts.pop(0))
        )
        plain = parts.pop(0)
        if len(plain):
            ret.append(StrPart('', '', plain))

    return FormatStr(ret)

def test_parse():
    data = (
        # ('<c(red):hi there>', 'c', 'red', 'hi there'),
        ('wow. <c(red):hi there> how are you?', 'c', 'red', 'hi there'),
    )
    for fullstr, code, arg, s in data:
        res = parse(fullstr)
        print(res)
        # assert res.code == code
        # assert res.arg == arg
        # assert res.s == s