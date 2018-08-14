# visual_studio_templates
Visual Studio templates for ESRI, Javascript, Node, OpenLayers, Python, etc... relevant to my GIS work.

Refer to official Microsoft documentation at 
https://docs.microsoft.com/en-us/visualstudio/ide/creating-project-and-item-templates

## Prerequisites

* At least VS 2017. I use the (free) Community Edition, currently I have 15.7.6 installed.
* In VS, you need the extensibility package.
* For ESRI templates I am using ArcGIS 10.6 Desktop and Enterprise.

## What templates I have here.

arcpy_item/
  arcpy_script.py
  arcpy_item.vstemplate
  arcpy_icon.png
  arcpy_preview.png

arcpy_project/
  config.py
  arcpy_project.vstemplate
  arcpy_icon.png
  arcpy_preview.png

node_project/
  server.js    actually implements a little http server
  node.png

openlayers_project/
  
python_toolbox_project/

## Deploying templates

If all you want is to use these templates you can download the ZIP
files.  Then just drag the zip files into the appropriate folders. I
use %HOME%/VisualStudio2017/Templates/{ItemTemplates|ProjectTemplates}
but I think the default is "%HOME%/Documents/Visual Studio
2017/Templates" I change the option in VS, "Tools->Options->Projects
and Solutions->Locations", so that it follows local convention.

After installing new templates you have to restart VS before it will see them.

## Building templates

First fork or clone this project, then open the "solution" in VS.

Make whatever changes you desire.

Under Project, choose "Export Template". Choose the Project or Item option as needed.

The wizard stupidly always puts its output in
"%HOME%/Documents/Visual Studio 2017/My Exported Templates"
and then you have to move the ZIP files yourself to whereever you want them.

## Template usage

If you created both project and item templates and deployed them then they
will show up when you create new projects or when you add an item.

## Miscellaneous

I don't remember where I got the ArcPY Python icon, maybe ESRI? If it
belongs to you and you don't want me using it, speak up and I will
remove it.
