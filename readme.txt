The generate.cmd does the following:
Converting CSV to TEX			via python script/CSV2cube.py TEMPcubes
Generating collective TEX for cubes	via python script/generateAlph.py cubes
Resizing images				using IrfanView 64 in its standard directory
Generating PDF (1st time)		via pdflatex.exe main.tex
Generating PDF (2nd time)		to update the toc and links
Deleting auxilliary files		as a cleanup