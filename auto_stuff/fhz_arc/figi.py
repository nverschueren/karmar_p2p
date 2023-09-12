def cu(u,c,labs,labs2):
    import matplotlib.pyplot as plt
    import numpy as np
    fig=plt.figure(figsize=(10,10))
    plt.plot(u['p'],u['s'])
    plt.plot(u(labs[0])['p'],u(labs[0])['s'],'cv')
    plt.plot(u(labs[1])['p'],u(labs[1])['s'],'cv')
    plt.plot(u(labs[2])['p'],u(labs[2])['s'],'co')
    plt.axvline(x=0.3047,color='green')
    plt.plot(c['p'],c['s'],color='red')
    plt.plot(c(labs2[0])['p'],c(labs2[0])['s'],'c+')
    plt.plot(c(labs2[1])['p'],c(labs2[1])['s'],'c*')

    ax=fig.gca()
    ax.set_xlabel('p')
    ax.set_ylabel('s')
    ax.set_ylim(0.36,1.3)
    
    plt.grid()
    plt.show(block=False)
    input("press any key to finish")

def cuall(u,c,labsu,labsc):
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import numpy as np
    fig=plt.figure(figsize=(10,3))
    gs=GridSpec(2,3)
    
    ax1=fig.add_subplot(gs[:,0])
    ax1.plot(u['p'],u['s'])
    ax1.plot(u(labsu[0])['p'],u(labsu[0])['s'],'cv')
    ax1.plot(u(labsu[1])['p'],u(labsu[1])['s'],'cv')
    ax1.plot(u(labsu[2])['p'],u(labsu[2])['s'],'co')
    ax1.axvline(x=0.3047,color='green')
    ax1.plot(c['p'],c['s'],color='red')
    ax1.plot(c(labsc[0])['p'],c(labsc[0])['s'],'c+')
    ax1.plot(c(labsc[1])['p'],c(labsc[1])['s'],'c*')
    ax1.set_xlabel('p')
    ax1.set_ylabel('s')
    ax1.set_ylim(0.36,1.3)
    ax1.grid()

    ax2=fig.add_subplot(gs[0,1])
    ax2.plot(c(labsc[0])['t']*5.1150000000E+002,c(labsc[0])['v'],'-g')
    ax2.plot(4*5.1150000000E+002/5, max(c(labsc[0])['v']),'c+')
    ax2.set_xlim(0,5.1150000000E+002)
    ax2.set_title('v(x)')
    ax2.set_xticks([])
    #ax2.grid()


    ax3=fig.add_subplot(gs[1,1])
    ax3.plot(c(labsc[1])['t']*5.1150000000E+002,c(labsc[1])['v'],'-g')
    ax3.plot(4*5.1150000000E+002/5, max(c(labsc[1])['v']),'c*')
    ax3.set_xlim(0,5.1150000000E+002)
#    ax3.set_ylabel('v')
    ax3.set_xlabel('t')
    #ax3.grid()

    ax4=fig.add_subplot(gs[:,2],projection='3d')
    ax4.plot(c(labsc[0])['v'],c(labsc[0])['d'],c(labsc[0])['w'])
    ax4.set_xlabel('v')
    ax4.set_ylabel('d')
    ax4.set_zlabel('w')
    ax4.view_init(30, 40)
    
    plt.show(block=False)
    input("press any key to finish")

def wigly(u,labs):
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import numpy as np
    fig=plt.figure(figsize=(6,7))
    gs=GridSpec(2,2)
    ax1=fig.add_subplot(gs[:,0])
    ax1.plot(u['p'],u['PERIOD'])
    ax1.set_xlabel('p')
    ax1.set_ylabel('T')

    ax1.plot(u(labs[0])['p'],u(labs[0])['PERIOD'],'cv')
    ax1.plot(u(labs[1])['p'],u(labs[1])['PERIOD'],'cp')
    


    ax1.set_ylim(30,700)
    
    ax2=fig.add_subplot(gs[0,1])
    ax2.plot(u(labs[0])['v'],u(labs[0])['w'],'r')
    ax2.plot(max(u(labs[0])['v']),max(u(labs[0])['w']),'cv')
    ax2.yaxis.tick_right()

    ax3=fig.add_subplot(gs[1,1])
    ax3.plot(u(labs[1])['v'],u(labs[1])['w'],'r')
    ax3.plot(max(u(labs[1])['v']),max(u(labs[1])['w']),'cp')
    ax3.yaxis.tick_right()
    ax3.set_xlabel('v')
    ax3.set_ylabel('w')
    
    
    plt.show(block=False)
    input("press any key to finish")


















    
