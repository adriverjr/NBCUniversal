TITLE NBCUniversal Coding Exercise
cls
c:

cd \NBCUniversal
::create a lock file to prevent dual threads from running
IF EXIST nbcuniversal.lock GOTO :lock_in_place
copy /y nul "nbcuniversal.lock"

cd Working

::++++++++++++++++++++++++++++  Copy original files from landing pad to Archive +++++++++++++++++++++++++++::
copy c:\NBCUniversal\*.csv   c:\NBCUniversal\Archive

::***** Move All Files To a working folder *******
move c:\NBCUniversal\*.csv 	c:\NBCUniversal\Working\

::+++++++++++++++++++++++ Initiate extracting the data one file at a time +++++++++++++++++++++++++++::
::+++++++++++++++++++ Python script requires 2 parameters, filename and working directory +++++++++++::

for %%F in (*.csv) do ( 
  c:\NBCUniversal\Python\NBCUniversal_Formula1.py "%%F" c:\NBCUniversal\Working\
)


::+++++++++++++++++++++++ Let's clean this mama up +++++++++++++++++++++++++++::
:: no need to delete files from working folder, python will handle that
::del /q c:\NBCUniversal\Working\*.* 
del c:\NBCUniversal\nbcuniversal.lock
goto end

:lock_in_place
echo There is another process already running.  If this is not accurate, remove the file c:\NBCUniversal\nbcuniversal.lock

:end 



