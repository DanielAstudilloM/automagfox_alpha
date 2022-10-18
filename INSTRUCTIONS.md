INSTRUCTIONS

The script is designed to automate running the MAGFOX program for any amount of compositions desired. Compositions need to be placed on a tab delimited file in the structure of the provided examples "comp.txt" and "comp.xlsx", this can be easily done through excel and then saving as a tab delimited file named "comp.txt".

**WARNING!! THIS VERSION CONTAINS NO ERROR HANDLING MECHANISMS AND SHOULD DATA BE PROVIDED TO IT IN A WAY THAT IS NOT THE SPECIFIED IN THE PROVIDED EXAMPLES YOU MAY NOT BE WARNED OR NOTIFIED ABOUT MISTAKES IN THE CALCULATIONS. BEWARE OF THE ORDER THE COMPONENT COLUMNS IN THE EXAMPLES AS IT MUST REMAIN AS PRESENTED, OTHERWISE THE PROGRAM WILL THINK IT IS GETTING A DIFFERENT COMPOSITION. DO NOT ADD ADDITIONAL DATA OR COMPONENTS.**

This script requires an executable file for a modified version of MAGFOX. Since we cannot distribute the code for legal reasons, we provide instructions on how to modify the original publicly available files and how to compile the executable file.

The program and compilation should be done on any Linux system (including WSL) or mac (untested). Check the REQUIREMENTS.md file for information of required python libraries and fortran compilers required for running the program.

0.- Download all files from this repository into a folder.

1.- Download the SPICES suite of programs from https://www.lpi.usra.edu/lunar/tools/crystallizationcalculation/

2.- Follow the directories to reach ../SPICE_Programs/Programs/MAGFOX and copy the magfox.f90 file into the folder where the python script is located. No other file is needed.

3.- Open the magfox.f90 file with a text editor, preferably Notepad++ similar, or IDE. Make sure you can see the line numbers.

4.- After line 15 "CHARACTER (LEN=24) :: title(5)" add a new line with the following: CHARACTER (LEN=8) :: el(14)

5.- After line 35 (initially 34; "WRITE(6,3330)") add a new line with the following: OPEN(UNIT=9,FILE='INPUTER.txt',ACCESS='SEQUENTIAL',STATUS='OLD'). Delete this same command from line 41 (initially 39) as well as the CLOSE(9) from line 50 (initially 49). Do not leave empty lines when deleting.

6.- Replace line 38 for: READ(9,3333) inp

7.- Comment lines 52 through 54 and 56 through 69 by adding a ! symbol at the beggining of each line.

8.- Change the "READ(5," part of lines 73, 77, 80, 86, and 89 for "READ(9,", just change the 5 for 9, do not modify any other part of the lines.

9.- After line 90 add a new line with the following: CLOSE(9)

10.- Replace line 208 for this command: WRITE(1,8723) cyc,tab,tcm,tab,ol(6)/(ol(6)+ol(5)),tab,tab,tab,tab,tab,tab,tab

11.- Replace line 211 for this command: 8723 FORMAT(i4,a4,f7.1,a4,f7.3,a4,'0',a4,'0',a4,'0',a4,'0',a4,'0',a4,'0',a4,'0'). Make sure all of the modified lines match the indentation of the surrounding code.

12.- You are now ready to compile the program, save your changes on the same file or change the name if you desire to keep the original, but keep the .f90 extension. If using the recommended compiler, gfortran, you only need to use the console of your system. Go to the directory where the modified MAGFOX version is located and do the following command: "gfortran magfox.f90 -o a.out" (ignore the "). If you saved the modified file with a different name, replace magfox.f90 for the name of your file. This should create an executable file named a.out, the script will call this file to run the program.

13.-You may now run the program. As default it will fractionate at steps of 1% crystallization increments until 99 % crystallization is done at 2 bars of pressure. You may modify the the automagfox.py for crystallization step in line 117, endpoint in line 118 and pressure in line 110 (in bars). Additional options from the program are comented in the code.

14.- Make sure all files from this repository and the executable a.out file are all located in the same folder. Make sure all python libraries required are installed. You are now ready to run the program, you may do so from the console by typing: python3 automagfox.py, or do it directly from your IDE.

15.- Once the program is finished, a new Results folder will appear with the results of each sample on their own folder named after the names in the comp.txt file. MAGFOX returns 4 text files: the dat file contains a summary of all the process; the liq file shows the evolution of the liquid composition; the xtl file shows the endmember composition of crystal phases, the wfx file shows the abundances of crystalline phases. **WARNING: RUNNING THE PROGRAM A SECOND TIME WILL ERASE THE PREVIOUS RESULTS FOLDER, IF YOU WISH TO SAVE YOUR DATA YOU WILL NEED TO MANUALLY MOVE IT INTO ANOTHER FOLDER.**