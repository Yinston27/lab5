import re
import timeit

# res = re.fullmatch("Meow", 'Meow')
# print(res)
# res = re.escape("http://www.python.org\n")
# print(repr(res))

# res = re.split('meow', 'kldcks;lcscmeowlsldklkddmeow')
# print(repr(res))

# print(re.sub('meow', 'bark', 'kjddkjlkdjnlmeowlksddnjdsmeow'))
# pattern = re.compile('[eg]{2}m')
# res = timeit.timeit('pattern.findall("eeqqm")', globals=globals(), number=10**7)
# print(res)


res = re.findall(r'M[aoi]ow[qg]', 'MaowqshkljM7777owj;jcmowg')
print(res)

# res = re.findall(r'm.*?eo', 'meowkdjoemmmeow93ijjnfemmmmeow eow')
# print(res)

# res = re.search(r'(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})', 'lkdlkdml;kmv12.12.3032kmd;kc;msdc')
# print(res.groupdict())


# res = re.findall(r'M\w*\s$', 'Mlsdl mdsdcMldsl Mskdlsdc ')
# print(res)