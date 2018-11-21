# twistytex

A script to simplyfy updating a PDF of a collection of magic cubes.

The generate.cmd does the following:

- **Converting CSV to TEX**			  via python script/CSV2cube.py cubes
- **Generating collective**       TEX for cubes	via python script/generateAlph.py cubes
- **Resizing images**				      using IrfanView 64 in its standard directory
- **Generating PDF (1st time)**		via pdflatex.exe main.tex
- **Generating PDF (2nd time)**		to update the toc and links
- **Deleting auxilliary files**		as a cleanup

Some example cubes are already listed in the CSV file. Corresponding pictures are in the pictures folder.
