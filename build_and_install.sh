cd arcpy_templates

echo "ArcPy Project Template"
rm -f arcpy_project_template.zip
zip arcpy_project_template.zip arcpy_application.pyproj arcpy_project.vstemplate arcpy_script.py config.py *png
cp arcpy_project_template.zip /j/VisualStudio2017/Templates/ProjectTemplates/

echo "Arcpy Item Template"
rm -f arcpy_item_template.zip
zip arcpy_item_template.zip arcpy_script.py *png arcpy_item.vstemplate
cp arcpy_item_template.zip /j/VisualStudio2017/Templates/ItemTemplates/

cd ..

cd pythontoolbox_templates

echo "Python Toolbox Project Template"
rm -f pythontoolbox_project_template.zip
zip pythontoolbox_project_template.zip PythonToolbox.pyproj pythontoolbox_project.vstemplate PythonToolbox.pyt python_tool.py config.py *png

# Swipe a copy of this biz logic file from the arcpy_templates
cd ../arcpy_templates
zip ../pythontoolbox_templates/pythontoolbox_project_template.zip arcpy_script.py
cd ../pythontoolbox_templates

cp pythontoolbox_project_template.zip /j/VisualStudio2017/Templates/ProjectTemplates/

echo "Python Toolbox Item Template"
rm -f pythontoolbox_item_template.zip
zip pythontoolbox_item_template.zip python_tool.py *png
cp pythontoolbox_item_template.zip /j/VisualStudio2017/Templates/ItemTemplates/

echo "Restart VisualStudio to load the new template(s)."
echo "When you do the ZIP file will be copied to some secret place known only to Microsoft."
echo "(Hint, it's near %HOME%/AppData/Roaming/)"


