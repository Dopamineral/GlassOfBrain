'''
This file holds some useful tools, will add to them as needed.
Part of class tutorial, check out this link for more info:


'''


class SmartData():
    def __init__(self,x,y,name=None):
        self.x = x
        self.y = y
        self.name = name
        
        self.meanx = self.calculate_mean(x)
        self.meany = self.calculate_mean(x)
        self.varx = self.calculate_variance(x)
        self.vary = self.calculate_variance(y)
        self.covarxy = self.calculate_covariance(x,y)
        self.stdx = self.calculate_std(x)
        self.stdy = self.calculate_std(y)
        self.corrxy = self.calculate_correlation(x,y)
        self.R2xy = self.calculate_R2(x,y)
        
    def calculate_mean(self,number_list):
        '''Calculates mean of number list '''
        number_of_elements = len(number_list)
        sum_of_elements = 0
        for ii in range(number_of_elements):
            sum_of_elements = sum_of_elements + number_list[ii]
        mean_value = sum_of_elements / number_of_elements
       
        return mean_value
        
    def calculate_variance(self,number_list):
        '''calculates sample variance of number list '''
        #std = sqrt(sum of squares (number in the list - number_list_mean)/number_of_elements)
        number_list_mean = self.calculate_mean(number_list) #notice how we use a function within a function!
        sum_of_squares = 0
        for ii in range(len(number_list)):
            square_val = (number_list[ii] - number_list_mean)**2
            sum_of_squares = sum_of_squares + square_val
            
        variance_value = (sum_of_squares / (len(number_list)-1)) 
    
        return variance_value
    
    def calculate_covariance(self,number_list_x, number_list_y):
        '''calculates sample covariance for two number_lists'''
        
        number_list_x_mean = self.calculate_mean(number_list_x)
        number_list_y_mean = self.calculate_mean(number_list_y)
        
        numerator = 0 
        for ii in range(len(number_list_x)):
            x_part = number_list_x[ii] - number_list_x_mean 
            y_part = number_list_y[ii] - number_list_y_mean 
            numerator = numerator + (x_part * y_part)
            
        covariance = numerator / (len(number_list_x) -1)
        
        return covariance 
    
    def calculate_std(self,number_list):
        '''calculates std of number list using variance'''
        std = self.calculate_variance(number_list)**(1/2)
        return std
    
    def calculate_correlation(self,number_list_x, number_list_y):
        ''' calculates correlation between x and y number lists using cov and std'''
        #corr = cov(x,y)/std(x)*std(y)
        cov = self.calculate_covariance(number_list_x,number_list_y)
        stdx = self.calculate_std(number_list_x)
        stdy = self.calculate_std(number_list_y)
        
        correlation = cov / (stdx*stdy)
        
        return correlation
    
    def calculate_R2(self,number_list_x, number_list_y):
        '''calculates R2 quickly'''
        R2 = self.calculate_correlation(number_list_x, number_list_y)**2
        return R2
    
    def print_summary_statistics(self):
        '''prints summary statistics of data pair'''
        xdata = self.x
        ydata = self.y
        
        # x
        xdata_mean = self.calculate_mean(xdata)
        xdata_variance = self.calculate_variance(xdata)
        xdata_std = self.calculate_std(xdata)
        # y
        ydata_mean = self.calculate_mean(ydata)
        ydata_variance = self.calculate_variance(ydata)
        ydata_std = self.calculate_std(ydata)
        # x y
        xydata_covariance = self.calculate_covariance(xdata,ydata)
        xydata_correlation = self.calculate_correlation(xdata,ydata)
        xydata_R2 = self.calculate_R2(xdata,ydata)
        
        # print statements
        if self.name == None:
            print('Summary Statistics')
        else:
            print(f'Summary Statistics of {self.name}')
        print(f'x, mean: {xdata_mean:.02f}, var: {xdata_variance:.02f}, std: {xdata_std:.02f}')
        print(f'y, mean: {ydata_mean:.02f}, var: {ydata_variance:.02f}, std: {ydata_std:.02f}')
        print(f'xy, cov: {xydata_covariance:.02f}, corr: {xydata_correlation:.02f}, R2: {xydata_R2:.02f}')
        print('--------------------------------------------------')

