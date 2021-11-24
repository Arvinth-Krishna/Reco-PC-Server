@echo off

echo Installing required packages.

python -m pip install --user -r .\requirements.txt

SET exampleFile="dummy_env.txt"
SET newFile=".env."

echo Creating environment configuration file

IF EXIST %newFile% (
  echo Configuration file already exists!
) ELSE (
  copy %exampleFile% %newFile%
)
echo Done. Please fill the required field in %newFile%

pause
