@echo off
setlocal enabledelayedexpansion

:: Windows Installer for Strong Password Generator
:: Author: Kote Shaburishvili

echo ========================================
echo  Strong Password Generator Installer
echo ========================================
echo.

:: Check if Python is installed (try both py and python)
set PYTHON_CMD=
py --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=py
) else (
    python --version >nul 2>&1
    if not errorlevel 1 (
        set PYTHON_CMD=python
    )
)

if "%PYTHON_CMD%"=="" (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3 from https://www.python.org/
    pause
    exit /b 1
)

:: Get Python version
for /f "tokens=2" %%i in ('%PYTHON_CMD% --version 2^>^&1') do set PYTHON_VER=%%i
echo [OK] Python %PYTHON_VER% detected (using %PYTHON_CMD%)

:: Check if passgen.py exists
if not exist "passgen.py" (
    echo [ERROR] passgen.py not found in current directory
    pause
    exit /b 1
)
echo [OK] passgen.py found

:: Define installation directory
set INSTALL_DIR=%USERPROFILE%\AppData\Local\Programs\PassGen
set WRAPPER_DIR=%USERPROFILE%\AppData\Local\Microsoft\WindowsApps

:: Create installation directory
if not exist "%INSTALL_DIR%" (
    echo Creating installation directory...
    mkdir "%INSTALL_DIR%"
)
echo [OK] Installation directory ready

:: Copy the Python script
echo Installing passgen.py...
copy /Y "passgen.py" "%INSTALL_DIR%\passgen.py" >nul
if errorlevel 1 (
    echo [ERROR] Failed to copy passgen.py
    pause
    exit /b 1
)
echo [OK] Script installed to %INSTALL_DIR%

:: Create wrapper batch file with the correct Python command
echo Creating passgen command...
(
    echo @echo off
    echo %PYTHON_CMD% "%INSTALL_DIR%\passgen.py" %%*
) > "%INSTALL_DIR%\passgen.bat"
echo [OK] Wrapper created

:: Check if WindowsApps directory exists (usually in PATH by default)
if exist "%WRAPPER_DIR%" (
    echo Creating shortcut in WindowsApps...
    copy /Y "%INSTALL_DIR%\passgen.bat" "%WRAPPER_DIR%\passgen.bat" >nul
    echo [OK] Command added to PATH
) else (
    echo [WARNING] WindowsApps directory not found
    echo You'll need to add %INSTALL_DIR% to your PATH manually
)

:: Ask about clipboard support
echo.
set /p CLIPBOARD="Install clipboard support (pyperclip)? [y/N]: "
if /i "%CLIPBOARD%"=="y" (
    echo Installing pyperclip...
    %PYTHON_CMD% -m pip install pyperclip
    if errorlevel 1 (
        echo [WARNING] Could not install pyperclip
        echo You can install it later with: %PYTHON_CMD% -m pip install pyperclip
    ) else (
        echo [OK] Clipboard support installed
    )
)

:: Success message
echo.
echo ========================================
echo [SUCCESS] Installation complete!
echo ========================================
echo.
echo Usage:
echo   passgen              # Interactive mode
echo   passgen -l 20 -s -n  # CLI mode
echo   passgen --help       # Show help
echo.
echo Try running: passgen
echo.

:: Ask to test
set /p TEST="Test the installation now? [y/N]: "
if /i "%TEST%"=="y" (
    echo.
    call passgen --version
)
