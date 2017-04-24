import pyparsing as pp

header = pp.Word(pp.alphanums+ '/' + ' ' + '-')

year = pp.Word(pp.nums, exact=2)('year')
month = pp.Word(pp.nums, exact=2)('month')
day = pp.Word(pp.nums, exact=2)('day')
hour = pp.Word(pp.nums, exact=2)('hour')
minutes = pp.Word(pp.nums, exact=2)('minutes')
seconds = pp.Word(pp.nums, exact=2)('seconds')

TST = pp.Group(year + month + day + hour + minutes + seconds)('tst')
