@echo off

if "%1" == "html" (
    rmdir /S /Q build >NUL 2>NUL
    sphinx-build -b html root build
    sphinx-build -b gettext root build\gettext
    sphinx-intl update -p build/gettext -l zh_CN
) ^
else if "%1" == "open" (
    build\index.html >NUL 2>NUL
)
