@REM start /B C:\Sotiris\kafka\3.5.1\bin\windows\zookeeper-server-start.bat C:\Sotiris\kafka\3.5.1\config\zookeeper.properties
@REM start /B C:\Sotiris\kafka\3.5.1\bin\windows\kafka-server-start.bat C:\Sotiris\kafka\3.5.1\config\server.properties

start cmd /K C:\Sotiris\kafka\3.5.1\bin\windows\zookeeper-server-start.bat C:\Sotiris\kafka\3.5.1\config\zookeeper.properties
timeout /t 15 /nobreak
start cmd /K C:\Sotiris\kafka\3.5.1\bin\windows\kafka-server-start.bat C:\Sotiris\kafka\3.5.1\config\server.properties
timeout /t 5 /nobreak
 
call C:\Sotiris\kafka\3.5.1\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
pause