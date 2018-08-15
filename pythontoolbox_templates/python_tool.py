"""
Implements a geotool as a class.
Sample code here; you will end up deleting most of it.

@date:   $time$
@author: $username$
"""
from __future__ import print_function
import os
import sys
import logging
import arcpy
from arcpy import mapping as MAP

# Don't do real work in this file!
# Create an arcpy_script then import it here, for example,
from arcpy_script import Some_Sample_Function

class $safeitemname$(object):

    def __init__(self):  
        """Define the tool (tool name is the name of the class)."""
        self.label = self.__class__.__name__ # Use the class name here
        self.description = """Put some descriptive text here."""
        self.canRunInBackground = False
        self.category = $projectname$ # Use your own category here, or an existing one.
        #self.stylesheet = "" # I don't know how to use this yet.
        return

    def getParameterInfo(self):
        """Define parameter definitions.
Refer to https://desktop.arcgis.com/en/arcmap/latest/analyze/creating-tools/defining-parameters-in-a-python-toolbox.htm
        """       

        # params[0] 
        input_fc = arcpy.Parameter(name="input_fc",
                                   displayName="Input Feature Class",
                                   # Using a composite type here means I can 
                                   # enter either a feature class or a string into the form.
                                   datatype=["DEFeatureClass", "GPString"],
                                   parameterType="Required", # Required|Optional|Derived
                                   direction="Input", # Input|Output
                                   )
        # You can set filters here for example
        #input_fc.filter.list = ["Polygon"]
        # You can set a default if you want -- this makes debugging a little easier.
        input_fc.value = "my_fc.shp"
         
        # params[1] 
        field = arcpy.Parameter(name="field",
                                displayName="Name of a field",
                                datatype="Field",
                                parameterType="Required", # Required|Optional|Derived
                                direction="Input", # Input|Output
                                )
        # Define this so that the list of field names will be filled in in ArcCatalog
        field.parameterDependencies = [input_fc.name]

        # params[2] 
        datestamp = arcpy.Parameter(name="datestamp",
                                 displayName="A date string YYYY/MM/DD",
                                 datatype="GPDate",
                                 parameterType="Required", # Required|Optional|Derived
                                 direction="Input", # Input|Output
                                 )
        # You can set a default value here.
        datestamp.value = "2017/01/01"
        
        # params[3]
        depnumber = arcpy.Parameter(name="another_number",
                                    displayName="A number that depends on number",
                                    datatype="GPLong",
                                    parameterType="Required", # Required|Optional|Derived
                                    direction="Input", # Input|Output
                                    )
        # You could set a list of acceptable values here for example
        depnumber.filter.type = "Range"
        depnumber.filter.list = [100,500]
        # You can set a default value here.
        depnumber.value = 200
        
        # params[4] 
        output_fc = arcpy.Parameter(name="output_fc",
                                    displayName="Output feature class",
                                    datatype="DEFeatureClass",
                                    parameterType="Derived", # Required|Optional|Derived
                                    direction="Output", # Input|Output
                                    )
        # This is a derived parameter; it depends on the input feature class parameter.
        # You usually use this to define output for using the tool in ESRI models.
        output_fc.parameterDependencies = [input_fc.name]
        # Cloning tells arcpy you want the schema of this output fc to be the same as input_fc
        # See http://desktop.arcgis.com/en/desktop/latest/analyze/creating-tools/updating-schema-in-a-python-toolbox.htm#ESRI_SECTION1_0F3D82FC6ACA421E97AC6D23D95AF19D
        output_fc.schema.clone = True

        return [input_fc, field, datestamp, depnumber, output_fc]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

        if parameters[0].altered:
            # If the field is not in the new feature class
            # then switch to the first field
            try:
                l = [f.name for f in arcpy.ListFields(parameters[0].valueAsText)]
                if not parameters[1].valueAsText in l:
                    parameters[1].value = l[0]
            except:
                # Could not read the field list
                parameters[1].value = ""

        if not parameters[3].altered:
            # When you change the field called "number" then this function will
            # be called and the next field will change to its value * 100.        
            parameters[3].value = int(parameters[2].value)*100

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""

        if parameters[2].value == 2:
            parameters[2].setWarningMessage("Sample warning, you set the number to 2.")
        return

    def execute(self, parameters, messages):
        """The source code of your tool."""
        
        # Let's dump out what we know here.
        messages.addMessage("This is a test of your sample tool.")
        for param in parameters:
            messages.addMessage("Parameter: %s = %s" % (param.name, param.valueAsText) )
        
        # Get the parameters from our parameters list,
        # then call a generic python function.
        #
        # This separates the code doing the work from all
        # the crazy code required to talk to ArcGIS.
        
        # See http://resources.arcgis.com/en/help/main/10.2/index.html#//018z00000063000000
        input_fc  = parameters[0].valueAsText
        fieldname = parameters[1].valueAsText
        datestamp = parameters[2].valueAsText
        depnumber = parameters[3].value
        output_fc = parameters[4].valueAsText

        # Okay finally go ahead and do the work.
        Some_Sample_Function(input_fc, fieldname, datestamp)
        return
        
# ===================================================================================
if __name__ == "__main__":
    # This is an example of how you could set up a unit test for this tool.
    # You can run this tool from a debugger or from the command line
    # to check it for errors before you try it in ArcGIS.

    class Messenger(object):
        def addMessage(self, message):
            print(message) # You could also do logging here.

    import config

    MYNAME  = os.path.splitext(os.path.split(__file__)[1])[0]
    LOGFILE = MYNAME + ".log"
    logging.basicConfig(filename=LOGFILE, level=logging.DEBUG, format=config.LOGFORMAT)
    print("Writing log to %s" % LOGFILE)

    # Get an instance of the tool.
    tool = $safeitemname$()
    # Read its default parameters.
    params = sample.getParameterInfo()

    # Set some test values into the instance
    params[0].value = "my_fc.shp"
    params[1].value = "datestamp"
    params[2].value = "2017/04/01"
    params[3].value = 100
    params[4].value = "outputfile.txt"
    
    # Run it.
    tool.execute(params, Messenger())

# That's all!
