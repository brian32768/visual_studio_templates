# $projectname$

I should fix up this README.md template sometime.

## Set up Node.JS

You need to have Node.JS installed.
I use the Portable version, and I manually add the location
to the PATH environmnent variable so that VS can use it.

## Install OpenLayers
Refer to http://openlayers.org/en/latest/doc/tutorials/bundle.html

You need to install the OpenLayers node package.

There is a package.json file included here so you probably don't
need to do this step,

  npm init

but if you do then it will edit package.json and update it.

Then you need the OpenLayers 5 package:

  npm install ol

That's it, you should be able to run (F5) server.js
and that should launch a browser. If it fails to launch
a browser the URL is http://localhost:1337

Or maybe you should do

 npm test

instead?
