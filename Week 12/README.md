# Personal information
FIRSTNAME: Hung
LASTNAME:  Hoang
MSSV: 20205333

####################################################################################### 
# Answers to Problem 2:  Fitting an SVM by hand
#
# Please list your final answers below for auto-grading.
#######################################################################################

# Problem 2b: what is the value of the margin  (only your final numeric answer)
PROB_SVMBYHAND_MARGIN: 2.83

# Problem 2d: what is the value of w_0  (only your final numeric answer)
PROB_SVMBYHAND_W0: -1


####################################################################################### 
# Answers to Problem 3:  VC Dimension (519 ONLY)
#
# Please list your final answers below for auto-grading.
#
# Your answer can be a number, or an expression in terms of the number of instances
# n or the dimensionality of the space d
#######################################################################################

# Problem 3a: What is the VC dimension (a number or equation in terms of n or d)
PROB_VC_SPHERE1: 123.456789

# Problem 3b: What is the VC dimension (a number or equation in terms of n or d)
PROB_VC_SPHERE2: 123.456789


#######################################################################################
# Answer to Implementation Exercise 2.3:  Analysis of the regularization parameter
#######################################################################################

# Copy and paste your brief paragraph describing the effect of the regularization 
# parameter from your PDF.
LOGREGIMPLEMENTATION_REGULARIZATION_ANALYSIS:
 As I increased the value of lambda, I observed that the theta is regularized since lambda penalizes those large values of theta. It is biased towards a much simpler model.  



#######################################################################################
# Answer to Implementation Exercise 3.4:  Effect of Kernel Parameters
#######################################################################################

# Copy and paste your brief paragraph describing the effect of varying the kernel  
# parameters and C from your PDF.
SVM_KERNELPARAMETEREFFECTS:
  
Polynomial Kernel: 
As I increase C, it overfits the data and has a low bias and high variance.
As I increase the degree, the model becomes more complex, and overfits the data.

Gaussian Kernel:
As I increase Gaussian Sigma, the decision boundary is expanding, and new test data is more likely to be classified to the certain category. 
As I increase C, it overfits the data and has a low bias and high variance.



#######################################################################################
# Answer to Implementation Exercise 3.5:  Optimal SVM parameters
#######################################################################################

# What was the optimal value you found for C?
SVM_OPTIMAL_C: 10

# What was the optimal value you found for sigma?
SVM_OPTIMAL_SIGMA: 10

# What is the estimated accuracy for your choice of optimal parameters?
SVM_OPTIMAL_ACCURACY: 0.9538


 
 
 
#######################################################################################
# Feedback on the Assignment
# 
# The following information will help us improve future versions of this assignment.
# It is completely optional, but highly appreciated.  Please be honest.
#######################################################################################

# Approximately how many hours did it take you to complete this assignment?
FEEDBACK_NUM_HOURS: 0

# Please list any typos / errors you noticed in the assignment description or skeleton code
FEEDBACK_ERRORS: |
    None
 
# Please describe any problems you encountered while completing this assignment
FEEDBACK_PROBLEMS: |
    None
    
