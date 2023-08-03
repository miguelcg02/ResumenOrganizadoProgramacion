%Secante: se ingresa el valor inicial (x0), la tolerancia del error (Tol) y el màximo nùmero de iteraciones (niter) 

function [n,xn,fm,E] = secante(x0,x1,Tol,niter)
    syms x

        f=(abs(x)^(x-1))-2.5*x-5;
        c=0;
        fm(c+1) = eval(subs(f,x0));
        f0=fm(c+1);
        fm(c+2) = eval(subs(f,x1));
        fe = fm(c+2);
        E(c+1)=Tol+1;
        E(c+2)=Tol+1;
        error=E(c+2);
        xn=x1;
        N(c+1)=c;
        N(c+2)=c;
        XN(c+1)=x0;
        XN(c+2) = xn;
        while error>Tol && fe~=0 && c<niter
            xm=xn-((fe*(xn-x0))/(fe-f0));
            XN(c+3)=xm;
            f0 = fe;
            fm(c+3)=eval(subs(f,xm));
            fe=fm(c+3);
            E(c+3)=abs(xm-xn);
            error=E(c+3);
            x0=xn;
            xn=xm;
            N(c+3)=c+1;
            c=c+1;
        end
        if fe==0
           
           n=c;
           fprintf('%f es raiz de f(x) \n',xn)
           disp(['      n                Xn                   Fx                   Error'])
           D=[N' XN' fm' E'];
            disp(D)

        elseif error<Tol
           
           n=c;
           fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f \n',xn,Tol)
           disp(['      n                Xn                   Fx                   Error'])
           D=[N' XN' fm' E'];
            disp(D)

        else 
           
           n=c;
           fprintf('Fracasó en %f iteraciones \n',niter)
           disp(['      n                Xn                   Fx                   Error'])
           D=[N' XN' fm' E'];
            disp(D)
        end
        
end