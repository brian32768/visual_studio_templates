# visual_studio_templates
Visual Studio templates for ESRI, Javascript, Node, OpenLayers, Python, etc... 
relevant to my GIS work (but apparently regarded as red-headed step children
by Microsoft).

## The story so far

I tried to follow the instructions on how to build a ".vsix" file, but
it failed in the usual "let's make everything so complicated and
opaque that it does not work" fashion often exhibited by Microsoft. It
works fine following the VB example but I don't use VB, I use Python
and Javascript... so I had to work around it.

To get started I built a python template ZIP file using the "Project
Export" wizard, then extracted the .vstemplate from it and built a new ZIP
around it. Since I could not convince VS to build the zip for me I created
a stupid brute force bash script for now.

The docs say that Visual Studio 2017 only supports VSIX files now but it's
not true. I can still drop a ZIP file into the right VS folder and VS
will unpack it the next time it launches so I am sticking with that
approach for now.

## Prerequisites

* At least VS 2017. I use the (free) Community Edition, currently I have 15.8.0 installed.
* For ESRI templates I am using ArcGIS 10.6 Desktop and Enterprise.

## Deploying templates

If all you want is to use these templates you can download the ZIP
files. Drag the zip files into the appropriate folders. I
use %HOME%/VisualStudio2017/Templates/{ItemTemplates|ProjectTemplates}
but I think the default is "%HOME%/Documents/Visual Studio
2017/Templates" I change the option in VS, "Tools->Options->Projects
and Solutions->Locations", so that it follows local convention.

After installing new templates you have to restart VS before it will see them.

## Building templates

First fork or clone this project, then open the "solution" in VS.

Make whatever changes you desire.

I crafted my pyproj and vstemplate files lovingly by hand, you will have to update them if you go this route, or use the wizard.

I have a bash script "install.sh" that zips and copies.

### Wizard alternative

Under Project, choose "Export Template". Choose the Project or Item option as needed.

The wizard stupidly always puts its zipped output in
"%HOME%/Documents/Visual Studio 2017/My Exported Templates"
and then you have to move the ZIP files yourself to whereever you actually want them.

## Template usage

After proper deployment, the templates
will show up when you create new projects or when you add an item.

## Miscellaneous

I don't remember where I got the ArcPY Python icon, maybe ESRI? If it
belongs to you and you don't want me using it, speak up and I will
remove it.
