<<<<<<< HEAD
import numpy as np

########################################################
## Complete functions in skeleton codes below
## following instructions in each function.
## Do not modify existing function name or inputs.
## Do not test your codes here - use main.py instead.
## You may use any built-in functions from NumPy.
## You may define and call new functions as you see fit.
########################################################



def low_rank_approx(A, k):
    '''
    inputs:
      - A: m-by-n matrix
      - k: positive integer, k<=m, k<=n
    returns:
      X: m-by-n matrix that is an as-close-as-possible approximation of A
      up to rank k
    '''
    #TODO: Fill your work here
    u, s, vh = np.linalg.svd(A)
    # # print(u,s,vh)
    # new_s = np.zeros((s.shape[0],s.shape[0]))
    # new_s = np.fill_diagonal(new_s,s[:k])
    # print(u.shape,'\n',new_s.shape,'\n',vh.shape)
    # print(3, u[::k], new_s, vh[:k])
    # s[k:] = 0
    return u[:,:k]@np.diag(s[:k])@vh[:k]


def constrained_LLS(A, B):
    '''
    inputs:
      - A: n-by-n full rank matrix
      - B: n-by-n matrix
    returns:
      x: n-diemsional vector that minimises ||Ax||2 subject to ||Bx||2=1
    '''
    #TODO: Fill your work here
    eps = 1e-7
    # np.diag()
    u, s, vt = np.linlag.svd(B)
    s += eps
    s1 = np.diag(s)
    # even if B is not a full rank matrix
    # adding a eps into the diagonal elements would make it full rank
    temp_matrix = s1@vt
    new_matrix = A@temp_matrix.T
    u2, st, vt2 = np.linalg.svd(A)
    x = vt.T@s1@vt2[-1]
    return x




### you can optionally write your own functions like below ###

# def my_func_name(input1, input2, ...):
#     do something
#     return ...
# %%
=======
import numpy as np

########################################################
# Complete functions in skeleton codes below
# following instructions in each function.
# Do not modify existing function name or inputs.
# Do not test your codes here - use main.py instead.
# You may use any built-in functions from NumPy.
# You may define and call new functions as you see fit.
########################################################


def low_rank_approx(A, k):
    '''
    inputs: 
      - A: m-by-n matrix
      - k: positive integer, k<=m, k<=n
    returns:
      X: m-by-n matrix that is an as-close-as-possible approximation of A
         up to rank k
    '''
    u, s, vt = np.linalg.svd(A, full_matrices=False)
    return u[:, :k] @ np.diag(s[:k]) @ vt[:k]


def constrained_LLS(A, B):
    '''
    inputs:
      - A: n-by-n full rank matrix
      - B: n-by-n matrix
    returns:
      x: n-diemsional vector that minimises ||Ax||2 subject to ||Bx||2=1 
    '''
    eps = 1e-6  # small value to handle singular matrix
    _, s, vt = np.linalg.svd(B)
    s += min(eps, eps*s[0])  # add small value in case rank deficiency
    W = np.diag(s) @ vt  # full rank n-by-n matrix
    x = np.linalg.svd(A @ W.T)[2][-1]  # the smallest right singular vector
    return vt.T @ np.diag(1/s) @ x


### you can optionally write your own functions like below ###

# def my_func_name(input1, input2, ...):
#     do something
#     return ...
>>>>>>> 76adb372dc9e7f7b8eb85ebcb2943680a8d7eb29
