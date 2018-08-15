# pythontoolbox_templates

The code here generates templates to use with Microsoft Visual Studio to create a "Python Toolbox" for ESRI ArcGIS Desktop.

If you are putting more than one tool in a toolbox, then you'd
first create a new python_toolbox project and then use 'add new item' to add tool classes
and then 'add new item' to add more business logic python files.

I used to break out a separate "business logic" python template but realized that's just the
same as my arcgis_templates arcpy_script.py

