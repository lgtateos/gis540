class Parcel: 
    def __init__(self, value, zoning):
        '''Initialize this parcel's properties.'''
        self.value = value #initialize the value property
        self.zoning = zoning  #initialize the zoning property
        ### 4. Initialize another property called acreage, so that it is initialized from user input

    def calculateTax(self ):
        '''Returns the tax value based on the parcel zoning'''
        rate = 0.076 
        if self.zoning == "residential":
            rate = 0.075 
        elif self.zoning == "industrial":
            rate = 0.77
        tax = self.value*rate
        return tax

    ### 5. Define calculateSF, another procedure that returns the parcel area measured in sq ft
            ### By the way, 1 acre = 43560 sq. ft.

    #-------end of class definition-------

#-------- invocation begins ---------    
myParcel = Parcel(145000, "residential")
print( "Value:", myParcel.value)
print("Zoning:", myParcel.zoning)
mytax = myParcel.calculateTax()
print("Tax:", mytax)

### 1. Create another Parcel object called p2 (you choose the value and zoning).
### 2. Print the value of p2.
### 3. Calculate the tax on p2 and print the results.

### 6. Create another Parcel object called p3, a 5 acre agricultural property with 1000000. 
### 7. Call the new procedure calculateSF on p3 and print the results
### 8. put this code in a conditonal statement so that it only runs if __name__ is "__main__"