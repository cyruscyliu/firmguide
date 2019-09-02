@echo off
SET BINWALK_HOME="C:\\Python37\\Lib\\site-packages\\binwalk"

copy plugins\* %BINWALK_HOME%\plugins
copy magic\* %BINWALK_HOME%\magic
copy core\* %BINWALK_HOME%\core

