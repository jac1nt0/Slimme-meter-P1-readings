import pyparsing as pp

header = pp.Word(pp.alphanums+ '/' + ' ' + '-')

year = pp.Word(pp.nums, exact=2)('year')
month = pp.Word(pp.nums, exact=2)('month')
day = pp.Word(pp.nums, exact=2)('day')
hour = pp.Word(pp.nums, exact=2)('hour')
minutes = pp.Word(pp.nums, exact=2)('minutes')
seconds = pp.Word(pp.nums, exact=2)('seconds')

TST = pp.Group(year + month + day + hour + minutes + seconds)('tst')

test_data = '''
/KFM5KAIFA-METER

1-3:0.2.8(42)
0-0:1.0.0(170424212445S)
0-0:96.1.1(4530303235303030303834323232373136)
1-0:1.8.1(000095.588*kWh)
1-0:1.8.2(000014.325*kWh)
1-0:2.8.1(000000.000*kWh)
1-0:2.8.2(000000.000*kWh)
0-0:96.14.0(0001)
1-0:1.7.0(02.177*kW)
1-0:2.7.0(00.000*kW)
0-0:96.7.21(00001)
0-0:96.7.9(00001)
1-0:99.97.0(1)(0-0:96.7.19)(000101000001W)(2147483647*s)
1-0:32.32.0(00000)
1-0:32.36.0(00000)
0-0:96.13.1()
0-0:96.13.0()
1-0:31.7.0(009*A)
1-0:21.7.0(02.177*kW)
1-0:22.7.0(00.000*kW)
0-1:24.1.0(003)
0-1:96.1.0(4730303139333430333130373337393136)
0-1:24.2.1(170424210000S)(00000.002*m3)
!5D8B
'''

def test():
  results = TST.scanString(test_data)
  for t,s,e in results:
    print t.name,":", t.value
  

if __name__=="__main__":
  test()
