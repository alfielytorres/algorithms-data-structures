'''

                            Online Python Debugger.
                Code, Run and Debug Python program online.
Write your code in this editor and press "Debug" button to debug program.

'''
def accept_hypothesis(mu_hat, mu, sigma, n):
    z_score = (mu_hat-mu)/(sigma/n**0.5)
    if z_score < 0:
        z_score *= -1
    
    P = 0 
    
    if z_score < 0.5:
        P = 0.5
    elif z_score < 1:
        P = 0.3
    elif z_score < 2:
        P = 0.15
    else: 
        P = 0.02
    
    p_value = 2*P
    return p_value <= 0.05



answer = accept_hypothesis(5, 20, 4, 16)
print(answer)
