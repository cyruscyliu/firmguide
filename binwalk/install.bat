@echo off
SET BINWALK_HOME="C:\\Python37\\Lib\\site-packages\\binwalk"

copy core\* %BINWALK_HOME%\core
copy magic\* %BINWALK_HOME%\magic
copy modules\* %BINWALK_HOME%\modules
copy plugins\* %BINWALK_HOME%\plugins

