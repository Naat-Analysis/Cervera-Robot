import sympy as sp
class funcion():
    def __init__(self, expr, var):
        self.expr = expr
        self.var = var
    
    def evaluate(self,a):
        fn=sp.lambdify(self.var,self.expr,'numpy')
        return fn(a)

    def sderiv(self):
        return sp.diff(self.expr, self.var)
    
    def sinteg(self):
        return sp.integrate(self.expr, self.var)
    
    def nderiv(self,a,h):
        return (self.evaluate(a+h)-self.evaluate(a-h))/(2*h)

    def ninteg(self,a,b):
        return sp.integrate(self.expr, (self.var, a, b))

