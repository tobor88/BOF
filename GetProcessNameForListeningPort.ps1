# On Windows, get the name of a process by the listening port

$ListeningPort = Read-Host "What port is the process listening on? Example: 80"

$ProcessID = Get-NetTCPConnection -State Listen | Where-Object -Property localport -like $ListeningPort | Select-Object -Property OwningProcess
Get-Process | Where-Object -Property Id -like $ProcessID.OwningProcess | Select-Object -Property ProcessName,Id
