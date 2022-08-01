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

      DOUBLE PRECISION uu,w,v,de,eps,nb,c,inte,ka,the,efe

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
      
  !    the=1/(1+EXP(-2*(uu-1)/ka)) !analytical aproximation of the heaviside
      
      the=(uu-1)*(1+(uu-1)/SQRT((uu-1)**2+ka*ka))/2 !analytical aproximation of the ramp function
      
      
      F(1)= w
      F(2)= (c*w-efe)/de
      F(3)= eps*(the/nb-v)
      
      
      END SUBROUTINE FUNC

      SUBROUTINE STPNT(NDIM,U,PAR,T)
!     ---------- ----- 

      IMPLICIT NONE
      INTEGER, INTENT(IN) :: NDIM
      DOUBLE PRECISION, INTENT(INOUT) :: U(NDIM),PAR(*)
      DOUBLE PRECISION, INTENT(IN) :: T

       PAR(1)=0.0 !inten
       PAR(2)= 0.0001 !speed 
       PAR(3)=0.5 !nb
       PAR(4)=1.0 !D
       PAR(5)=0.01
       PAR(6)=0.001

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
