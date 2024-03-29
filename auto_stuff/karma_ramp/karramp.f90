!---------------------------------------------------------------------- 
!---------------------------------------------------------------------- 
!   karramp :     Karma model with the ramp function (using an analytical approximation)
!---------------------------------------------------------------------- 
!---------------------------------------------------------------------- 

      SUBROUTINE FUNC(NDIM,U,ICP,PAR,IJAC,F,DFDU,DFDP) 
!     ---------- ---- 

      IMPLICIT NONE
      INTEGER, INTENT(IN) :: NDIM, ICP(*), IJAC
      DOUBLE PRECISION, INTENT(IN) :: U(NDIM), PAR(*)
      DOUBLE PRECISION, INTENT(OUT) :: F(NDIM)
      DOUBLE PRECISION, INTENT(INOUT) :: DFDU(NDIM,NDIM), DFDP(NDIM,*)

      DOUBLE PRECISION uu,w,v,de,eps,nb,c,inte,ka,the,efe,sigk

      uu=U(1)
      w=U(2)
      v=U(3)

      inte=PAR(1)
      c=PAR(2)
      nb=PAR(3)
      de=PAR(4)
      eps=PAR(5)
      ka=PAR(6)
	  
	  
      efe=-uu+2*(1.5-v*v*v*v)*(uu*uu-uu*uu*uu/4.0)+inte
	  
	  !analytical aproximation of the heaviside
  !    the=1/(1+EXP(-2*(uu-1)/ka)) 
  
      !analytical aproximation of the ramp function
	  sigk = (uu-1)/SQRT((uu-1)**2+ka*ka)
	  the =(uu-1)*(1+sigk)/2 
      
      F(1)= w
      F(2)= (c*w-efe)/de
      F(3)= eps*(the/nb-v)/c
	  
	  
      ! jacobian

            IF(IJAC.EQ.0)RETURN

      DFDU(1,1)=0.0
      DFDU(1,2)=1.0
      DFDU(1,3)=0.0

      DFDU(2,1)=-(-1 + 2*(1.5-v*v*v*v)*(2*uu-3*uu*uu/4.0))/de
      DFDU(2,2)=c/de
      DFDU(2,3)=2*4*v*v*v*(uu*uu-uu*uu*uu/4.0)/de

      DFDU(3,1)=eps*(1/2+sigk-sigk**3/2)/(nb*c)
      DFDU(3,2)=0.0
      DFDU(3,3)=-eps/c


      IF(IJAC.EQ.1)RETURN 

      DFDP(1,1:6)=0.0
      DFDP(1,2:4)=0

      DFDP(2,1)=-1/de
      DFDP(2,2)=w/de
      DFDP(2,3)=0.0
      DFDP(2,4)=-(c*w-efe)/(de**2)
      DFDP(2,5:6)=0.0


      DFDP(3,1)=0.0
      DFDP(3,2)=-eps*(the/nb-v)/(c**2)
	  DFDP(3,3)=-eps*(the/(nb**2))/c
      DFDP(3,4)=0.0
      DFDP(3,5)=(the/nb-v)/c
      DFDP(3,6)=-eps*ka*(uu-1)**2/(2*nb*c*(SQRT((uu-1)**2+ka*ka))**3)
      
      END SUBROUTINE FUNC



      SUBROUTINE STPNT(NDIM,U,PAR,T)
!     ---------- ----- 

      IMPLICIT NONE
      INTEGER, INTENT(IN) :: NDIM
      DOUBLE PRECISION, INTENT(INOUT) :: U(NDIM),PAR(*)
      DOUBLE PRECISION, INTENT(IN) :: T

       PAR(1)=0.0 !i
       PAR(2)=0.0001 !speed 
       PAR(3)=0.5 !nb
       PAR(4)=1.0 !D
       PAR(5)=0.01 !epsilon
       PAR(6)=0.001  !ka

       U(1)=1.495701892872247
       U(2)=0.0
       U(3)=0.9914027770768228

      END SUBROUTINE STPNT

      SUBROUTINE BCND 
      END SUBROUTINE BCND

      SUBROUTINE ICND 
      END SUBROUTINE ICND

      SUBROUTINE FOPT 
      END SUBROUTINE FOPT

      SUBROUTINE PVLS
      END SUBROUTINE PVLS
