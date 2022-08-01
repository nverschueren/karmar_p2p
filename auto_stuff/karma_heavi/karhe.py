a=run('karhe')
b=run(a('HB1'),IPS=2,ICP=['c','PERIOD'],NMX=100,NPR=20)
c=run(b,IRS=10,IPS=9,ICP=['c','I'],NMX=30,NPR=2,DSMAX=1e-2)
