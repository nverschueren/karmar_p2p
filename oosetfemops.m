function p=oosetfemops(p)
fem=p.pdeo.fem; gr=p.pdeo.grid; 
[K,M,~]=fem.assema(gr,1,1,1); % FEM/mass matrices
p.mat.M=[M 0*M;0*M M]; p.mat.K=K;
if p.dim==2
    Kx=convection(fem,gr,[1;0]);
    [p.mat.Kxx,~,~]=fem.assema(gr,[1 0;0 0],1,1); 
    [p.mat.Kyy,~,~]=fem.assema(gr,[0 0;0 1],1,1); 
    bc1=gr.robinBC(0,0); % NBCs 
    bc2=gr.robinBC(1,0); % DBCs  
gr.makeBoundaryMatrix(bc1,bc1,bc1,bc2); % bottom, right, top,left 
[Q,G,~,~]=fem.assemb(gr); p.mat.Q1=Q; 
[i,j]=find(Q~=0); p.idx1=unique(i); % p.mat.Q1=Q; p.mat.G1=G; 
elseif p.dim==1
    Kx=p.pdeo.fem.convection(p.pdeo.grid,1 ); 
end

p.mat.Kx=[Kx 0*Kx; 0*Kx Kx];

end