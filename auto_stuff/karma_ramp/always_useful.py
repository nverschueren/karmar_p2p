def showmefour(a,labs):
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import numpy as np
    fig=plt.figure(figsize=(10,10))
    #    fig=plt.figure()
    
    gs=GridSpec(4,2) # 5 rows, 2 columns
    
    ax1=fig.add_subplot(gs[:,0]) # First row, first column
    ax2=fig.add_subplot(gs[0,1]) # First row, second column
    ax3=fig.add_subplot(gs[1,1]) # First row, third column
    ax4=fig.add_subplot(gs[2,1]) # First row, fourth column
    ax5=fig.add_subplot(gs[3,1])  #fifth

    ax1.plot(a['eps'],a['uq'],'-b',linewidth=2)
    ax1.plot(a(labs[0])['eps'],a(labs[0])['uq'],'rv')
    ax1.plot(a(labs[1])['eps'],a(labs[1])['uq'],'r^')
    ax1.plot(a(labs[2])['eps'],a(labs[2])['uq'],'r<')
    ax1.plot(a(labs[3])['eps'],a(labs[3])['uq'],'r>')

    ax2.plot(a(labs[0])['r'],a(labs[0])['u'],'-r')

    ax3.plot(a(labs[1])['r'],a(labs[1])['u'],'-r')
    ax4.plot(a(labs[2])['r'],a(labs[2])['u'],'-r')
    ax5.plot(a(labs[3])['r'],a(labs[3])['u'],'-r')

    R=np.max(a(labs[0])['r'])#labels
    ax2.plot(R,np.max(a(labs[0])['u']),'rv')
    ax3.plot(R,np.max(a(labs[1])['u']),'r^')
    ax4.plot(R,np.max(a(labs[2])['u']),'r<')
    ax5.plot(R,np.max(a(labs[3])['u']),'r>')
        
        
    plt.show(block=False)
    input("press any key to finish")



def doblebd(a,labs,b,labs2):
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import numpy as np
    fig=plt.figure(figsize=(10,10))
    
    #    fig=plt.figure()
    R=np.max(a(labs[0])['r'])#labels    
    gs=GridSpec(4,3) # 5 rows, 2 columns
    ax1=fig.add_subplot(gs[:,1]) # First row, first column
    
    ax2=fig.add_subplot(gs[0,0])

    ax3=fig.add_subplot(gs[1,0]) # First row, third column
    ax4=fig.add_subplot(gs[2,0]) # First row, fourth column
    ax5=fig.add_subplot(gs[3,0])  #fifth

    ax6=fig.add_subplot(gs[0,2])
    ax7=fig.add_subplot(gs[1,2])
    ax8=fig.add_subplot(gs[2,2])
    ax9=fig.add_subplot(gs[3,2])
    
    ax1.plot(a['eps'],a['uq'],'-b',linewidth=2)
    ax1.plot(b['eps'],b['uq'],'-r',linewidth=2)
    
    ax1.plot(a(labs[0])['eps'],a(labs[0])['uq'],'rv')
    ax1.plot(a(labs[1])['eps'],a(labs[1])['uq'],'r^')
    ax1.plot(a(labs[2])['eps'],a(labs[2])['uq'],'r<')
    ax1.plot(a(labs[3])['eps'],a(labs[3])['uq'],'r>')
    ax1.plot(b(labs2[0])['eps'],b(labs2[0])['uq'],'gv')
    ax1.plot(b(labs2[1])['eps'],b(labs2[1])['uq'],'g^')
    ax1.plot(b(labs2[2])['eps'],b(labs2[2])['uq'],'g<')
    ax1.plot(b(labs2[3])['eps'],b(labs2[3])['uq'],'g>')
    ax1.set_title('R=14')


    

    ax2.plot(a(labs[0])['r'],a(labs[0])['u'],'-r')
    ax3.plot(a(labs[1])['r'],a(labs[1])['u'],'-r')
    ax4.plot(a(labs[2])['r'],a(labs[2])['u'],'-r')
    ax5.plot(a(labs[3])['r'],a(labs[3])['u'],'-r')


    ax6.plot(b(labs2[0])['r'],b(labs2[0])['u'],'-g')
    ax7.plot(b(labs2[1])['r'],b(labs2[1])['u'],'-g')
    ax8.plot(b(labs2[2])['r'],b(labs2[2])['u'],'-g')
    ax9.plot(b(labs2[3])['r'],b(labs2[3])['u'],'-g')
    


    ax2.plot(R,np.max(a(labs[0])['u']),'rv')
    ax3.plot(R,np.max(a(labs[1])['u']),'r^')
    ax4.plot(R,np.max(a(labs[2])['u']),'r<')
    ax5.plot(R,np.max(a(labs[3])['u']),'r>')


    ax6.plot(R,np.max(b(labs2[0])['u']),'gv')
    ax7.plot(R,np.max(b(labs2[1])['u']),'g^')
    ax8.plot(R,np.max(b(labs2[2])['u']),'g<')
    ax9.plot(R,np.max(b(labs2[3])['u']),'g>')
        
        
    plt.show(block=False)
    input("press any key to finish")


def showmefour2(a,labs):
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import numpy as np
    fig=plt.figure(figsize=(10,10))
    #    fig=plt.figure()
    
    gs=GridSpec(8,2) # 5 rows, 2 columns
    
    ax1=fig.add_subplot(gs[:,0]) # First row, first column
    ax2=fig.add_subplot(gs[0,1]) # First row, second column
    ax3=fig.add_subplot(gs[1,1]) # First row, third column
    ax4=fig.add_subplot(gs[2,1]) # First row, fourth column
    ax5=fig.add_subplot(gs[3,1])  #fifth
    ax6=fig.add_subplot(gs[4,1])  #fifth
    ax7=fig.add_subplot(gs[5,1])  #fifth
    ax8=fig.add_subplot(gs[6,1])  #fifth
    ax9=fig.add_subplot(gs[7,1])  #fifth
    
    ax1.plot(a['eps'],a['uq'],'-b',linewidth=2)
    i=1
    dxdy=0.01
    ax1.text(a('LP'+str(i))['eps']+dxdy,a('LP'+str(i))['uq']+dxdy,str(i))
    ax1.plot(a('LP'+str(i))['eps'],a('LP'+str(i))['uq'],'or')
    i=i+1

    ax1.text(a('LP'+str(i))['eps']+dxdy,a('LP'+str(i))['uq']+dxdy,str(i))
    ax1.plot(a('LP'+str(i))['eps'],a('LP'+str(i))['uq'],'or')
    i=i+1

    ax1.text(a('LP'+str(i))['eps']+dxdy,a('LP'+str(i))['uq']+dxdy,str(i))
    ax1.plot(a('LP'+str(i))['eps'],a('LP'+str(i))['uq'],'or')
    i=i+1

    ax1.text(a('LP'+str(i))['eps']+dxdy,a('LP'+str(i))['uq']+dxdy,str(i))
    ax1.plot(a('LP'+str(i))['eps'],a('LP'+str(i))['uq'],'or')
    i=i+1

    ax1.text(a('LP'+str(i))['eps']+dxdy,a('LP'+str(i))['uq']+dxdy,str(i))
    ax1.plot(a('LP'+str(i))['eps'],a('LP'+str(i))['uq'],'or')
    i=i+1

    ax1.text(a('LP'+str(i))['eps']+dxdy,a('LP'+str(i))['uq']+dxdy,str(i))
    ax1.plot(a('LP'+str(i))['eps'],a('LP'+str(i))['uq'],'or')
    i=i+1

    ax1.text(a('LP'+str(i))['eps']+dxdy,a('LP'+str(i))['uq']+dxdy,str(i))
    ax1.plot(a('LP'+str(i))['eps'],a('LP'+str(i))['uq'],'or')
    i=i+1

    ax1.text(a('LP'+str(i))['eps']+dxdy,a('LP'+str(i))['uq']+dxdy,str(i))
    ax1.plot(a('LP'+str(i))['eps'],a('LP'+str(i))['uq'],'or')


    i=1
    ax2.plot(a('LP'+str(i))['t'],a('LP'+str(i))['u'],'-r')
    ax2.text(np.max(a('LP'+str(i))['t'])-dxdy,np.max(a('LP'+str(i))['u']),str(i))
    ax2.set_ylim(-1.5, 1.5)

    i=i+1
    ax3.plot(a('LP'+str(i))['t'],a('LP'+str(i))['u'],'-r')
    ax3.text(np.max(a('LP'+str(i))['t'])-dxdy,np.max(a('LP'+str(i))['u'])-50*dxdy,str(i))
    ax3.set_ylim(-1.5, 1.5)

    i=i+1
    ax4.plot(a('LP'+str(i))['t'],a('LP'+str(i))['u'],'-r')
    ax4.text(np.max(a('LP'+str(i))['t'])-dxdy,np.max(a('LP'+str(i))['u'])-50*dxdy,str(i))

    i=i+1
    ax5.plot(a('LP'+str(i))['t'],a('LP'+str(i))['u'],'-r')
    ax5.text(np.max(a('LP'+str(i))['t'])-dxdy,np.max(a('LP'+str(i))['u'])-50*dxdy,str(i))
    i=i+1
    ax6.plot(a('LP'+str(i))['t'],a('LP'+str(i))['u'],'-r')
    ax6.text(np.max(a('LP'+str(i))['t'])-dxdy,np.max(a('LP'+str(i))['u'])-50*dxdy,str(i))
    i=i+1
    ax7.plot(a('LP'+str(i))['t'],a('LP'+str(i))['u'],'-r')
    ax7.text(np.max(a('LP'+str(i))['t'])-dxdy,np.max(a('LP'+str(i))['u'])-50*dxdy,str(i))
    i=i+1
    ax8.plot(a('LP'+str(i))['t'],a('LP'+str(i))['u'],'-r')
    ax8.text(np.max(a('LP'+str(i))['t'])-dxdy,np.max(a('LP'+str(i))['u'])-50*dxdy,str(i))
    i=i+1
    ax9.plot(a('LP'+str(i))['t'],a('LP'+str(i))['u'],'-r')
    ax9.text(np.max(a('LP'+str(i))['t'])-dxdy,np.max(a('LP'+str(i))['u'])-50*dxdy,str(i))
    
    ax1.set_title('SH35 2D Neumann Boundary conditions')
    ax2.set_title(r'$q=1, \nu=2, L=30$')

    plt.show(block=False)
    input("press any key to finish")


def doblebd2(a,labs,b,labs2,fn):
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import numpy as np

    fs=12
    cm=1/2.54

    
#    fig=plt.figure(figsize=(4.3*cm,6*cm))
    fig=plt.figure(figsize=(7,8))
    
    SMALL_SIZE = 8
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 14
    
    plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    

    
    R=np.max(a(labs[0])['r'])#labels    
    gs=GridSpec(8,3) # 5 rows, 2 columns
    gs.update(wspace=0,hspace=0)
    ax1=fig.add_subplot(gs[:,0:2]) # First row, first column
    
    ax2=fig.add_subplot(gs[0,2]) # First row, second column
    ax3=fig.add_subplot(gs[1,2]) # First row, third column
    ax4=fig.add_subplot(gs[2,2]) # First row, fourth column
    ax5=fig.add_subplot(gs[3,2])  #fifth
    
    ax6=fig.add_subplot(gs[4,2])
    ax7=fig.add_subplot(gs[5,2])
    ax8=fig.add_subplot(gs[6,2])
    ax9=fig.add_subplot(gs[7,2])
    
    jump=50
    col='r'
    ax1.plot(a['eps'],a['uq'],'-b',linewidth=2)
#    ax1.plot(b['eps'],b['uq'],'-r',linewidth=2)
    ax1.plot(b['eps'][::jump],b['uq'][::jump],'-'+col,markersize=3)
    
#    ax1.plot(b['eps'][0:20000:jump],b['uq'][0:20000:jump],'-'+col,markersize=3)

    
    dxdy=0.01

        
    zero=np.array([[-1, 0],[1, 0]])     
        
    ax1.plot(zero[:,0],zero[:,1],'k-',linewidth=2)
    
    ax1.set_title('R=%.1f' % R)
                               
    ax1.set_xlim(-0.88,0.2)
    ax1.set_ylim(-0.02,1.1)

    ax1.set_xlabel('$\epsilon$')
    ax1.set_ylabel('$|| u||_*$')
    
    
    '''
    ax2.plot(a(labs[0])['r'],a(labs[0])['u'],'-b')
    ax3.plot(a(labs[1])['r'],a(labs[1])['u'],'-b')
    ax4.plot(a(labs[2])['r'],a(labs[2])['u'],'-b')
    ax5.plot(a(labs[3])['r'],a(labs[3])['u'],'-b')


    
   
    
    ax6.plot(b(labs2[0])['r'],b(labs2[0])['u'],'-r')
    ax7.plot(b(labs2[1])['r'],b(labs2[1])['u'],'-r')
    ax8.plot(b(labs2[2])['r'],b(labs2[2])['u'],'-r')
    ax9.plot(b(labs2[3])['r'],b(labs2[3])['u'],'-r')
    '''

    ax2.plot(a(labs[0])['r'],-a(labs[0])['u'],'-b')
    ax3.plot(a(labs[1])['r'],-a(labs[1])['u'],'-b')
    ax4.plot(a(labs[2])['r'],-a(labs[2])['u'],'-b')
    ax5.plot(a(labs[3])['r'],-a(labs[3])['u'],'-b')
    
    ax6.plot(b(labs2[0])['r'],-b(labs2[0])['u'],'-'+col)
    ax7.plot(b(labs2[1])['r'],-b(labs2[1])['u'],'-'+col)
    ax8.plot(b(labs2[2])['r'],-b(labs2[2])['u'],'-'+col)
    ax9.plot(b(labs2[3])['r'],-b(labs2[3])['u'],'-'+col)
    

    ax2.set_xlim(0,R)
    ax3.set_xlim(0,R)
    ax4.set_xlim(0,R)    
    ax5.set_xlim(0,R)
    ax6.set_xlim(0,R)
    ax7.set_xlim(0,R)
    ax8.set_xlim(0,R)
    ax9.set_xlim(0,R)

    ax2.set_xticks([])
    ax2.yaxis.tick_right()
    ax3.set_xticks([])
    ax3.yaxis.tick_right()
    ax4.set_xticks([])
    ax4.yaxis.tick_right()
    ax5.set_xticks([])
    ax5.yaxis.tick_right()
    ax6.set_xticks([])
    ax6.yaxis.tick_right()
    ax7.set_xticks([])
    ax7.yaxis.tick_right()
    ax8.set_xticks([])
    ax8.yaxis.tick_right()
    ax9.yaxis.tick_right()

    ax9.yaxis.set_label_position("right")
    ax9.set_xlabel(r'$\rho$')
    ax9.set_ylabel(r'$u(\rho)$')

    ax9.set_xticks([0, R])
    
    ax2.plot(R*0.9,np.min(a(labs[0])['u'])*0.9,'bo')
    ax3.plot(R*0.9,np.min(a(labs[1])['u'])*0.9,'bo')
    ax4.plot(R*0.9,np.min(a(labs[2])['u'])*0.9,'bo')
    ax5.plot(R*0.9,np.min(a(labs[3])['u'])*0.9,'bo')
    
    ax6.plot(R*0.9,np.min(b(labs2[0])['u'])*0.9,col+'P')
    ax7.plot(R*0.9,np.min(b(labs2[1])['u'])*0.9,col+'P')
    ax8.plot(R*0.9,np.min(b(labs2[2])['u'])*0.9,col+'P')
    ax9.plot(R*0.9,np.min(b(labs2[3])['u'])*0.9,col+'P')

    ax2.text(R*0.95,np.min(a(labs[0])['u'])*0.92,'1')
    ax3.text(R*0.95,np.min(a(labs[1])['u'])*0.92,'2')
    ax4.text(R*0.95,np.min(a(labs[2])['u'])*0.92,'3')
    ax5.text(R*0.95,np.min(a(labs[3])['u'])*0.92,'4')
    ax6.text(R*0.95,np.min(b(labs2[0])['u'])*0.92,'5')
    ax7.text(R*0.95,np.min(b(labs2[1])['u'])*0.92,'6')
    ax8.text(R*0.95,np.min(b(labs2[2])['u'])*0.92,'7')
    ax9.text(R*0.95,np.min(b(labs2[3])['u'])*0.92,'8')

    for i in range(0,4):
        ax1.plot(a(labs[i])['eps'],a(labs[i])['uq'],'bo')
        ax1.text(a(labs[i])['eps']+dxdy,a(labs[i])['uq']+dxdy,str(i+1),fontsize=fs)
        ax1.plot(b(labs2[i])['eps'],b(labs2[i])['uq'],col+'P',markersize=7)
        ax1.text(b(labs2[i])['eps']+dxdy,b(labs2[i])['uq']+dxdy,str(i+1+4))
        i=i+1

    
    fig.tight_layout()
    plt.savefig('./new_figure7/figure'+str(fn)+'.svg')
    plt.savefig('./new_figure7/figurenewd''.svg')
    
#    plt.show(block=False)
#    input("press any key to finish")
    
def showmefour3(b,labs,fn):
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import numpy as np
    fig=plt.figure(figsize=(10,10))
    #    fig=plt.figure()
    
#    gs=GridSpec(0,0) # 5 rows, 2 columns
    
 #   ax1=fig.add_subplot(gs[0,0]) # First row, first column
    jump=70
    plt.plot(b['eps'][::jump],b['uq'][::jump],'.-r',linewidth=2)
    dxdy=0.01
    for i in range(0,4):
        plt.plot(b(labs[i])['eps'],b(labs[i])['uq'],'rP',markersize=7)
        plt.text(b(labs[i])['eps']+dxdy,b(labs[i])['uq']+dxdy,str(i+1+4))
        i=i+1
          
        
    #plt.show(block=False)
    #input("press any key to finish")
    plt.savefig('./new_figure7/figure'+str(fn)+'.svg')
