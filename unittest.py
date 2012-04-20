import sqlitecache
import translationunitcache
from parsehelp import *


opts = ["-x", "c++",
        "-Wall",
        "-I/usr/lib/clang/3.0/include/",
        "-I/usr/lib/clang/2.1/include/",
        "-I/usr/lib/gcc/i686-apple-darwin10/4.2.1/include/",
        "-I/usr/lib/gcc/i686-apple-darwin11/4.2.1/include/",
        "-IC:/MinGW/include",
        "-I/path/to/sources/1",
        "-I/path/to/sources/2"]


sqlitecache.sqlCache.clear()

tu = translationunitcache.tuCache.get_translation_unit("unittest.cpp", ["-x", "c++"])
sqlitecache.indexer.index(tu.var.cursor)

f = open("unittest.cpp")
fulldata = f.read()
f.close()

offset = 10
line, column = get_line_and_column_from_offset(fulldata, offset)
offset2 = get_offset_from_line_and_column(fulldata, line, column)
if offset != offset2:
    raise Exception("Offset to line and column conversion failed, %d != %d" % (offset, offset2))


if extract_line_at_offset(fulldata, get_offset_from_line_and_column(fulldata, 12, 4)) != "std::vector<A> v;":
    raise Exception("Line extraction didn't work")


offset = get_offset_from_line_and_column(fulldata, 10, 3)
comp = sqlitecache.sqlCache.complete(fulldata[:offset], extract_line_until_offset(fulldata, offset), "")
if comp == None or comp[0][1] != "test":
    raise Exception("Completion of A didn't work")

offset = get_offset_from_line_and_column(fulldata, 14, 11)
comp = sqlitecache.sqlCache.complete(fulldata[:offset], extract_line_until_offset(fulldata, offset), "")
if comp == None or comp[0][1] != "test":
    raise Exception("Completion of std::vector<A> didn't work")

offset = get_offset_from_line_and_column(fulldata, 20, 12)
comp = sqlitecache.sqlCache.complete(fulldata[:offset], extract_line_until_offset(fulldata, offset), "")
if comp == None or len(comp) == 0 or comp[0][1] != "test":
    raise Exception("Completion of typedeffed std::vector<A> didn't work")

offset = get_offset_from_line_and_column(fulldata, 31, 20)
comp = sqlitecache.sqlCache.complete(fulldata[:offset], extract_line_until_offset(fulldata, offset), "")
if comp == None or len(comp) == 0 or comp[0][1] != "test":
    raise Exception("Completion of member typedeffed std::vector<A> didn't work")

offset = get_offset_from_line_and_column(fulldata, 32, 21)
comp = sqlitecache.sqlCache.complete(fulldata[:offset], extract_line_until_offset(fulldata, offset), "")
if comp == None or len(comp) == 0 or comp[0][1] != "test":
    raise Exception("Completion of member std::vector<A> didn't work")

offset = get_offset_from_line_and_column(fulldata, 43, 28)
comp = sqlitecache.sqlCache.complete(fulldata[:offset], extract_line_until_offset(fulldata, offset), "")
if comp == None or len(comp) == 0 or comp[0][1] != "test":
    raise Exception("Completion of member std::vector<AV> didn't work")

offset = get_offset_from_line_and_column(fulldata, 44, 29)
comp = sqlitecache.sqlCache.complete(fulldata[:offset], extract_line_until_offset(fulldata, offset), "")
if comp == None or len(comp) == 0 or comp[0][1] != "test":
    raise Exception("Completion of member std::vector<std::vector<A> > didn't work")

offset = get_offset_from_line_and_column(fulldata, 55, 36)
comp = sqlitecache.sqlCache.complete(fulldata[:offset], extract_line_until_offset(fulldata, offset), "")
if comp == None or len(comp) == 0 or comp[0][1] != "test":
    raise Exception("Completion of member std::vector<std::vector<AV> > didn't work")

offset = get_offset_from_line_and_column(fulldata, 56, 37)
comp = sqlitecache.sqlCache.complete(fulldata[:offset], extract_line_until_offset(fulldata, offset), "")
if comp == None or len(comp) == 0 or comp[0][1] != "test":
    raise Exception("Completion of member std::vector<std::vector<std::vector<A> > > didn't work")