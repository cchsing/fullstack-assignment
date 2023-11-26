try{
    .\.venv\Scripts\Activate.ps1
    Set-Location .\part_4\map_webserver
    python -m manage.py runserver
}
finally{
    Set-Location (Get-Item $MyInvocation.MyCommand.Source).Directory.FullName
    deactivate
}