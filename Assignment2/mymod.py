def EulerCauchy(F, t0, h, tfinal, y0):
    t = np.arange(t0,tfinal+h,h)
    y = np.ones(len(t))
    y[0] = y0
    for i in range(1,len(t)):
        s1 = F(y[i-1]) #F(t[i-1], y[i-1])
        y[i] = y[i-1] + s1*h 
    return y